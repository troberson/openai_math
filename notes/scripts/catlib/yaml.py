"""lean/formalization.yaml, ComparatorChallenges/*.json, lean/docs/*.md, README.md traces.

The yaml carries `sources:` (manuscripts) and `status.main_results:` (config/declaration/file
triples) as two flat lists with **nothing linking them**, and no family key. family -> config
comes only from the `../ComparatorChallenges/(X).lean` links inside lean/docs/<NNN>.md, so a
reader that wants the chain walks family -> config (scope note) -> declaration -> file.

Source-level facts are source-level: the yaml states `scope: "Partial progress."`,
`automation: methods: [agent]`, `review: status: unchecked`. Zero `sorry` in source is not a
comparator pass, and it does not mean the library elaborates.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from catlib.paths import (
    COMPARATOR_DIR,
    DOCS_DIR,
    FORMALIZATION_YAML,
    OAI_DIR,
    README_MD,
    REASONING_TRACES,
    read_text,
)

CONFIG_KEY = re.compile(r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json")
SOURCE_ID = re.compile(r"^\s*id:\s*\.\./(" + r"preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf" + r")", re.M)
DOC_CONFIG = re.compile(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean")
DOC_PAP = re.compile(r"\]\(\.\./\.\./(preprints/(?:[^\s(){}\\]|\([0-9]+\))*\.pdf)\)")
SCOPE_SPAN = re.compile(r"^## Scope\n(.*?)(?=^## |\Z)", re.M | re.S)
TRACE_ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*\[[^\]]*\]\(reasoning_traces/([^)]+?)\.(?:pdf|tex)\)", re.M)


def parse_yaml_text(text: str) -> tuple[set[str], Counter]:
    """-> (set of formalized manuscript paths, {config stem: entry count}) for a **string**.

    The text-level core `parse_yaml()` delegates to; a checker that compares two revisions of
    the release reads both from a `git show <rev>:lean/formalization.yaml` string.
    """
    sources = set(SOURCE_ID.findall(text))
    main = Counter(CONFIG_KEY.findall(text))
    return sources, main


def parse_yaml() -> tuple[set[str], Counter]:
    """-> (set of formalized manuscript paths, {config stem: count of main_results entries})."""
    return parse_yaml_text(read_text(FORMALIZATION_YAML))


def main_results_entries() -> list[dict[str, Any]]:
    """Every main_results entry with its yaml line anchor: {config, declaration, file, line}.

    The anchor is the entry's `file:` line; a checker that quotes a 3-line entry block anchors
    at `file-line - 2`, which is where the `- comparator_config:` line sits.
    """
    lines = read_text(FORMALIZATION_YAML).splitlines()
    out: list[dict[str, Any]] = []
    entry: dict[str, Any] = {}
    for n, line in enumerate(lines, 1):
        m = CONFIG_KEY.search(line)
        if m:
            entry = {"config": m.group(1), "line": n}
            out.append(entry)
            continue
        m = re.search(r"^\s*declaration:\s*(\S+)", line)
        if m and entry:
            entry["declaration"] = m.group(1)
            continue
        m = re.search(r"^\s*file:\s*(\S+)", line)
        if m and entry:
            entry["file"] = m.group(1)
            entry["file_line"] = n
            entry = {}
    return out


def parse_challenges() -> dict[str, dict[str, Any]]:
    """-> {config stem: {theorems, definitions, nanoda}}."""
    out: dict[str, dict[str, Any]] = {}
    for p in sorted(COMPARATOR_DIR.glob("*.json")):
        d = json.loads(read_text(p))
        out[p.stem] = {
            "theorems": len(d.get("theorem_names") or []),
            "definitions": len(d.get("definition_names") or []),
            "nanoda": bool(d.get("enable_nanoda")),
        }
    return out


def parse_docs() -> dict[str, dict[str, Any]]:
    """-> {fam: {configs, paps, scope_chars}}; the only family -> config join the repo supports."""
    docs: dict[str, dict[str, Any]] = {}
    for p in sorted(DOCS_DIR.glob("*.md")):
        fam = p.stem
        text = read_text(p)
        cfgs = DOC_CONFIG.findall(text)
        paps = DOC_PAP.findall(text)
        m = SCOPE_SPAN.search(text)
        docs[fam] = {
            "configs": sorted(set(cfgs)),
            "paps": sorted(set(paps)),
            "scope_chars": len(m.group(1).strip()) if m else 0,
        }
    return docs


def parse_traces() -> tuple[dict[str, list[str]], list[str]]:
    """-> ({fam: [trace stems]}, stems on disk that README.md does not attribute).

    README.md tabulates every released reasoning trace against its result family, so the mapping
    is read from the release rather than guessed from filenames.
    """
    text = read_text(README_MD)
    rows = TRACE_ROW.findall(text)
    by_fam: dict[str, list[str]] = defaultdict(list)
    for fam, stem in rows:
        if stem not in by_fam[fam]:
            by_fam[fam].append(stem)
    listed = {s for stems in by_fam.values() for s in stems}
    on_disk = {p.stem for p in REASONING_TRACES.iterdir() if p.is_file()}
    return by_fam, sorted(on_disk - listed)


def scope_span(text: str) -> str:
    """The `## Scope` section body of a scope note, the load-bearing part of the note."""
    m = SCOPE_SPAN.search(text)
    return m.group(1).strip() if m else ""


def scope_span_lines(lines: list[str]) -> tuple[int, int] | None:
    """(first, last) 1-based line numbers of a scope note's `## Scope` section, or None.

    The line-number form of scope_span(), measured equivalent over all 242 notes: 242 hits for
    each rule and 0 docs where one fires and the other does not. A checker that pins a quotation
    to `lean/docs/NNN.md:<line>` needs the span, not the body.
    """
    start = next((i for i, ln in enumerate(lines) if ln.strip() == "## Scope"), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ")), len(lines))
    return start + 1, end


def doc_files() -> list[Path]:
    """The 242 scope notes, sorted. len() of this is every "scope notes" count in the repo."""
    return sorted(DOCS_DIR.glob("*.md"))


def yaml_lines(tolerant: bool = False) -> list[str]:
    """formalization.yaml as lines, for readers that quote it by line anchor.

    `tolerant=True` replaces undecodable bytes instead of raising; checkers use it because a
    checker must report on a file, not die on it, while a generator must not silently write a
    count derived from mangled text. The two rules are kept as one named parameter so a reader
    can see which one a script asked for.
    """
    text = FORMALIZATION_YAML.read_text(encoding="utf-8",
                                         errors="replace" if tolerant else "strict")
    return text.splitlines()


def oai_lean_files() -> Iterator[Path]:
    """Every .lean under lean/OAI/ — 122,458 files, 26,060,031 lines. Iterating is minutes."""
    yield from OAI_DIR.rglob("*.lean")


def oai_lean_count() -> int:
    """The lean/OAI file census, the figure every coverage answer quotes."""
    return sum(1 for _ in oai_lean_files())
