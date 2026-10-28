#!/usr/bin/env python3
"""Extract per-family data files from the current summary pages.

One-time bootstrap: reads each of the 60 family pages, replaces each quoted span
with its seq token, maps headings to canonical names, and writes
``notes/data/summaries/<NNN>.md``. The data files are the renderer's input;
after this bootstrap they are tracked in git and edited as prose.

The extraction is the inverse of ``catlib.quotes.seed_page``: the seeder finds
every quote by delimiters and reading order and assigns seqs; the extractor
reverses that, slotting each span with its ``{{seq}}`` token.

The data file carries two things the renderer cannot derive:
1. The section bodies (prose) with ``{{seq}}`` quote tokens.
2. The Sources table's file paths and role descriptions (per sid).
Line counts are computed by the renderer from disk. Links are derived from paths.

Usage: python3 notes/scripts/extract_summary_data.py [--check-only]
"""
from __future__ import annotations

import pathlib
import re
import sys

from catlib.quotes import seed_page
from catlib.summaries import CELL, ROW, Page

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "notes" / "data" / "summaries"
SUMM = ROOT / "notes" / "gen" / "summaries"

HEADING_MAP: dict[str, str] = {
    "Original CONTENTS.md summary": "contents",
    "Undergraduate summary": "undergraduate",
    "Undergraduate explanation": "undergraduate",
    "Graduate summary": "graduate",
    "Graduate explanation": "graduate",
    "History of the conjecture": "history",
    "History of the conjecture (if known)": "history",
    "History and prior work": "history",
    "History and context": "history",
    "History": "history",
    "History of the conjectures": "history",
    "Prior work": "history",
    "Consequences": "consequences",
    "Consequences now that the proof has been found": "consequences",
    "Consequences and open directions": "consequences",
    "Consequences now that the counterexamples exist": "consequences",
    "Consequences now that the proof has been found (if known)": "consequences",
    "Section skeleton": "section_skeleton",
    "Comparison with the formalized statement": "formalized",
    "What is formalized": "formalized",
    "Headline theorem": "headline",
    "Coverage": "coverage",
    "Coverage, as four layers": "coverage",
    "Three manuscripts": "undergraduate",
}

MECHANICAL = {"Sources", "Links", "Bibliography"}


def parse_sources(lines: list[str]) -> list[tuple[str, str, str]]:
    """The Sources table rows as (sid, path, role) triples."""
    out: list[tuple[str, str, str]] = []
    for line in lines:
        m = ROW.match(line)
        if not m:
            continue
        sid, cell, _declared, role = m.group(1), m.group(2), m.group(3), m.group(4)
        pm = CELL.search(cell)
        path = pm.group(1) if pm else ""
        out.append((sid, path, role))
    return out


def slot_inline(text: str, span: str, seq: int) -> str:
    """Replace an inline quoted span with its token, preserving the quote marks."""
    token = "{{" + str(seq) + "}}"
    for qo, qc in (("\u201c", "\u201d"), ('"', '"')):
        quoted = qo + span + qc
        if quoted in text:
            return text.replace(quoted, qo + token + qc, 1)
    if span in text:
        return text.replace(span, token, 1)
    return text


def slot_block(text: str, span: str, seq: int) -> str:
    """Replace a block quote with ``> {{seq}}``.

    The span is the seeder's joined text (no ``> `` prefix). The page carries
    the block as ``> ``-prefixed lines. Find the block by its first words.
    """
    token = "> {{" + str(seq) + "}}"
    words = span.split()
    if len(words) < 3:
        return text
    probe = " ".join(words[:4])
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith(">") and probe in ln:
            j = i
            while j + 1 < len(lines) and lines[j + 1].startswith(">"):
                j += 1
            lines[i:j + 1] = [token]
            return "\n".join(lines)
    return text


def extract_page(page_path: pathlib.Path) -> str | None:
    """One page's data file text, or None if the page has no family number."""
    lines = page_path.read_text(encoding="utf-8").splitlines()
    page = Page(page_path, lines)
    fam = page.fam
    if fam is None:
        return None
    name_m = re.match(r"^(\d{3})-(.+)\.md$", page_path.name)
    slug = name_m.group(2) if name_m else ""
    specs = seed_page(page)
    sources = parse_sources(lines)

    text = "\n".join(lines)
    for i in range(len(specs) - 1, -1, -1):
        sid, which, span, start, end, _, _, _ = specs[i]
        if not span:
            continue
        seq = i + 1
        if which == "block":
            text = slot_block(text, span, seq)
        else:
            text = slot_inline(text, span, seq)

    sections: list[tuple[str, list[str]]] = []
    current_heading = ""
    current: list[str] = []
    for line in text.split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            continue
        if line.startswith("## "):
            if current_heading:
                sections.append((current_heading, current))
            current_heading = line[3:].strip()
            current = []
        else:
            current.append(line)
    if current_heading:
        sections.append((current_heading, current))

    out: list[str] = []
    if sources:
        out.append("<!-- sources")
        for sid, path, role in sources:
            out.append(f"{sid}\t{path}\t{role}")
        out.append("-->")
        out.append("")
    if specs:
        out.append("<!-- quotes")
        for i, (sid, which, span, start, end, _head, _tail, _mode) in enumerate(specs, 1):
            out.append(f"{i}\t{which}\t{sid}\t{start}\t{end}\t{span}")
        out.append("-->")
        out.append("")
    out.append(f"<!-- family {fam} -->")
    if slug:
        out.append(f"<!-- slug {slug} -->")
    out.append("")
    for heading, sec_lines in sections:
        if heading in MECHANICAL:
            continue
        canon = HEADING_MAP.get(heading, heading.lower().replace(" ", "_"))
        body = "\n".join(sec_lines).strip()
        if body:
            out.append(f"## {canon}")
            out.append("")
            out.append(body)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    check_only = "--check-only" in sys.argv
    pages = sorted(
        p for p in SUMM.glob("*/*.md")
        if p.name != "README.md" and re.match(r"^\d{3}-", p.name)
    )
    print(f"family pages: {len(pages)}")

    if not check_only:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    problems = 0
    for p in pages:
        m = re.match(r"^(\d{3})-", p.name)
        if m is None:
            print(f"  {p.name}: NO FAMILY NUMBER")
            problems += 1
            continue
        fam = m.group(1)
        data_text = extract_page(p)
        if data_text is None:
            print(f"  {p.name}: NO FAMILY NUMBER")
            problems += 1
            continue
        n_slots = len(re.findall(r"\{\{\d+\}\}", data_text))
        if not check_only:
            (DATA_DIR / f"{fam}.md").write_text(data_text, encoding="utf-8")
        print(f"  {fam}: {n_slots} slots, {len(data_text)} bytes")
    print(f"problems: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
