#!/usr/bin/env python3
"""Render notes/gen/proofs/ from the skeleton template and per-family data files.

Reads:
- notes/templates/proofs/proof.md.j2 (the skeleton)
- notes/data/proofs/<NNN>.md (per-family prose with {{seq}} tokens, a sources block
  and a quotes block, in the same grammar as the summary data files)
- overview.tex (the family title for the page title line)

Writes: notes/gen/proofs/<NNN>.md (flat, family number only) and its index README.

Proof audits are family-shaped: the set of `## sections` one page carries is not a
fixed canonical set the way the summary sections are, so the template renders
whichever sections the data file supplies, in the order it supplies them, then the
fixed `## Sources` table. The quote-resolution path (token -> normalized span + its
[S#:a-b] marker) is the one the summary renderer already carries, so this writer
imports it from build_summaries rather than re-implementing the join.

The renderer is pure over its digest key: it reads the working-tree template and
data files, resolves each quote through the normalizer, and stages the rendered
pages. A second run with the same inputs produces identical bytes.

Usage: python3 notes/scripts/build_proofs.py [--check-only]
"""
from __future__ import annotations

import pathlib
import re
import sys

import build_catalog as B
import build_summaries as BS
from catlib import normalizer
from catlib import text as CTEXT
from catlib.atomic import Staging, outdir_of
from catlib.paths import ROOT
from catlib.promote import key_for
from jinja2 import Environment, FileSystemLoader

TPL_DIR = ROOT / "notes" / "templates" / "proofs"
DATA_DIR = ROOT / "notes" / "data" / "proofs"
PROOFS_DIR = ROOT / "notes" / "gen" / "proofs"

ENV = Environment(loader=FileSystemLoader(str(TPL_DIR)),
                  keep_trailing_newline=True,
                  trim_blocks=True, lstrip_blocks=True, autoescape=False)

FAM_FILE = re.compile(r"^(\d{3})\.md$")


def parse_sources(lines: list[str], i: int) -> tuple[list[tuple[str, str, str]], int]:
    """Parse the `<!-- sources ... -->` block. Returns (sources, next index).

    Same grammar as the summary data files: one row per source, `sid \t path \t role`.
    """
    sources: list[tuple[str, str, str]] = []
    if i < len(lines) and lines[i].strip() == "<!-- sources":
        i += 1
        while i < len(lines) and lines[i].strip() != "-->":
            parts = lines[i].split("\t")
            if len(parts) >= 3:
                sources.append((parts[0], parts[1], parts[2]))
            i += 1
        i += 1  # skip -->
    return sources, i


def parse_quotes(lines: list[str], i: int) -> tuple[dict[int, dict], int]:
    """Parse the `<!-- quotes ... -->` block. Returns (quotes, next index).

    Same grammar as the summary data files: one row per quote token,
    `seq  which  sid  start  end  span`. A quote's span may run across several
    physical lines; every line after a row's first line, up to the next row, is a
    continuation of the most recent quote's span and is appended newline-joined.
    A continuation line is one whose first tab-field is not a positive integer.
    """
    quotes: dict[int, dict] = {}
    if i < len(lines) and lines[i].strip() == "<!-- quotes":
        i += 1
        cur_seq: int | None = None
        while i < len(lines) and lines[i].strip() != "-->":
            line = lines[i]
            parts = line.split("\t")
            seq_field = parts[0].strip() if parts else ""
            if len(parts) >= 6 and re.fullmatch(r"\d+", seq_field) is not None:
                cur_seq = int(seq_field)
                quotes[cur_seq] = {"which": parts[1], "sid": parts[2],
                                   "start": parts[3], "end": parts[4],
                                   "span": "\t".join(parts[5:])}
            elif cur_seq is not None:
                quotes[cur_seq]["span"] += "\n" + line
            i += 1
        i += 1  # skip -->
    return quotes, i


def parse_sections(lines: list[str], i: int) -> list[tuple[str, str]]:
    """The ordered `## <heading>` sections after the quotes block.

    Unlike the summary data files, the heading is free-form (a proof audit's
    sections are family-shaped), so the rule keeps the full heading text, not a
    single token. Content before the first `##` (the `<!-- family -->` and
    `<!-- title -->` lines) is preamble and is dropped.
    """
    sections: list[tuple[str, str]] = []
    current_key = ""
    current_lines: list[str] = []
    for line in lines[i:]:
        m = re.match(r"^## (.+)$", line)
        if m:
            if current_key:
                sections.append((current_key, "\n".join(current_lines).strip()))
            current_key = m.group(1).strip()
            current_lines = []
        elif current_key:
            current_lines.append(line)
    if current_key:
        sections.append((current_key, "\n".join(current_lines).strip()))
    return sections


def parse_data_file(text: str) -> tuple[list[tuple[str, str, str]], dict[int, dict], list[tuple[str, str]]]:
    """Parse a proof data file into (sources, quotes, sections)."""
    lines = text.split("\n")
    i = 0
    sources, i = parse_sources(lines, i)
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    quotes, i = parse_quotes(lines, i)
    sections = parse_sections(lines, i)
    sid2path = {sid: path for sid, path, _role in sources}
    for row in quotes.values():
        row["path"] = sid2path.get(row["sid"], "")
    return sources, quotes, sections


def render_page(fam: str, title: str, data_text: str) -> str:
    """Render one family's proof page."""
    sources, quotes, sections = parse_data_file(data_text)

    main_tex_map: dict[str, str] = {}
    for _sid, path, _role in sources:
        mt = BS._main_tex_for(path)
        if mt:
            main_tex_map[path] = mt

    resolved: list[tuple[str, str]] = []
    for key, body in sections:
        stripped = BS.strip_own_markers(body, quotes)

        def _replace(m: re.Match[str]) -> str:
            prefix = m.group(1) or ""
            text = BS.resolve_token(m.group(2), quotes, main_tex_map, fam)
            if prefix and text.startswith("```"):
                return text
            return prefix + text

        out = re.sub(r"(?:(> ))?\{\{(\d+)\}\}", _replace, stripped)
        out = BS.expand_bare_markers(out, quotes)
        resolved.append((key, out))

    # Expand manuscript macros in the body's own math regions (the quote path does this
    # through normalize_window; the body path needs the same, so a macro the manuscript
    # defines renders, not raw). The union preamble is every preprint source's preamble.
    body_preamble = "\n".join(
        BS.get_preamble(path) for _sid, path, _role in sources
        if path.startswith("preprints/")
    )
    if body_preamble:
        resolved = [(k, normalizer.normalize_body_math(v, body_preamble)) for k, v in resolved]

    src_rows: list[str] = []
    for sid, path, role in sources:
        lc = BS.lines_of(path)
        href = f"../../../{path}"
        if "(" in path or ")" in path:
            href = f"<{href}>"
        src_rows.append(f"| {sid} | [`{path}`]({href}) | {lc} | {role} |")

    template = ENV.get_template("proof.md.j2")
    return template.render(p={
        "fam": fam,
        "title": CTEXT.fold_dashes(title),
        "sections": [{"name": k, "body": v} for k, v in resolved],
        "sources_rows": "\n".join(src_rows),
    })


def generate_readme(fams: dict[str, dict], page_fams: dict[str, str]) -> str:
    """Render the proofs index README from the rendered page set, ordered by family number."""
    rows = []
    for fam in sorted(page_fams, key=int):
        title = CTEXT.fold_dashes(fams[fam]["title"])
        rows.append(f"- [{fam}](./{fam}.md) — {title}")
    page_list = "\n".join(rows)
    n = len(page_fams)
    return f"""# Proof-level faithfulness audits

{n} per-family audits comparing a preprint's proof with its Lean formalization. The
statement-level comparison is family-specific; the proof-level comparison follows the
shared protocol in the data file [`README.md`](../../data/proofs/README.md) — the
"lost in translation" failure modes, the seven extraction targets, the reparameterization
test, and the sign audit.

Each page is rendered by `build_proofs.py` from a hand-edited data file
(`notes/data/proofs/<NNN>.md`) and the page skeleton; the checker
(`verify_proofs.py`) measures the rendered bytes and writes nothing.

## The pages

{page_list}

## Not checked

- A green page proves the citation surface, not the mathematics: it names the lines each
  quote sits on, and those lines are what they say. It does not re-derive the proof.
- Nothing in this repo builds, and no Lean run was made here; a Lean statement is evidence
  the claim was stated and proved by the agent, not independently verified.
"""


def main() -> int:
    check_only = "--check-only" in sys.argv

    key = key_for("build_proofs.py", tuple(sys.argv[1:]))
    st = Staging("build_proofs", key, outdir_of(sys.argv[1:]))

    _order, fams = B.parse_overview()

    data_files = sorted(p for p in DATA_DIR.glob("*.md") if FAM_FILE.match(p.name))
    print(f"data files: {len(data_files)}")

    problems = 0
    pages_written = 0
    written: set[pathlib.Path] = set()
    page_fams: dict[str, str] = {}
    for df in data_files:
        fam = df.stem
        if fam not in fams:
            print(f"  {fam}: NOT IN OVERVIEW")
            problems += 1
            continue
        info = fams[fam]
        data_text = df.read_text(encoding="utf-8")
        sources, quotes, _sections = parse_data_file(data_text)
        for sid, path, _role in sources:
            if not (ROOT / path).is_file():
                print(f"  {fam}: {sid} MISSING SOURCE {path}")
                problems += 1
        page_text = render_page(fam, info["title"], data_text)
        out = PROOFS_DIR / f"{fam}.md"
        if not check_only:
            st.stage(out, page_text)
        written.add(out)
        page_fams[fam] = info["title"]
        pages_written += 1
        # Quick sanity: count unresolved tokens.
        unresolved = len(re.findall(r"\{\{\d+\}\}", page_text))
        if unresolved:
            print(f"  {fam}: {unresolved} UNRESOLVED TOKENS")
            problems += 1

    readme = PROOFS_DIR / "README.md"
    readme_text = generate_readme(fams, page_fams)
    if not check_only:
        st.stage(readme, readme_text)
    written.add(readme)

    if not check_only:
        st.promote()
        stale = sorted(p for p in PROOFS_DIR.rglob("*.md") if p not in written)
        for p in stale:
            p.unlink()
        for d in sorted((x for x in PROOFS_DIR.rglob("*") if x.is_dir()),
                        key=lambda x: -len(x.parts)):
            if not any(d.iterdir()):
                d.rmdir()
        print(f"stale swept       {len(stale)} files")

    print(f"pages rendered: {pages_written}")
    print(f"problems: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
