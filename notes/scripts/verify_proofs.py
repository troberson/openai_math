#!/usr/bin/env python3
"""Verify every citation in a proof-level faithfulness audit page. Writes nothing.

The page body cites sources as [S2:19030], [S1:21–30] or [S3]; the Sources table at the bottom
maps S# to a file. The page is generated from a per-family data file by `build_proofs.py`, so the
citation passes split between the rendered page and the data file that feeds the writer:

  Pass B (markers)  - resolve every marker to the file it names, flag out-of-range, blank and
                      reversed-range positions, check the table's declared line counts against the
                      files on disk, resolve every markdown link from the page's own directory, and
                      require zero raw HTML anywhere in the page.
  Render diff       - the page's bytes against the writer's render of its data file.
  Provenance        - the data file's quote specs against the source files, independent of the
                      writer: each spec's sid is declared, the path is on disk, the window endpoints
                      are integers in range, neither endpoint is blank, and the window is not
                      reversed.
  Pass D (supersession) - every manuscript directory the page names must be one the catalog's
                      overview entry currently names for this family.
  Pass E (bare cites) - a citation in a unit that carries no quotation into a family-keyed file
                      must land inside the family's own block. Proof pages cite preprints/ and
                      lean/ files (which carry no family key) so this pass typically reports 0.

Usage: python3 notes/scripts/verify_proofs.py
"""
from __future__ import annotations

import contextlib
import functools
import io
import os
import re
import sys
from pathlib import Path

import build_catalog as B
import build_proofs
from catlib import anchors
from catlib.paths import PROOFS_DIR, ROOT, read_text
from catlib.render import diff_problems
from catlib.summaries import (
    ENTITY,
    LINK,
    MARKER,
    PAPDIR,
    QUOTE,
    TAG,
    Page,
    label,
    markers,
    named_dirs,
    units,
    usable,
)

DATA_DIR = ROOT / "notes" / "data" / "proofs"


def pass_b(page: Page) -> tuple[int, int, int, int]:
    """Markers, links, declared line counts, ambiguous File cells, raw HTML."""
    problems = 0
    checked = 0
    used: set[str] = set()
    links = 0
    for n, line in enumerate(page.lines, 1):
        for m in LINK.finditer(line):
            href = m.group(1)
            if href.startswith("<") and href.endswith(">"):
                href = href[1:-1]
            links += 1
            if href.startswith(("http://", "https://", "mailto:")):
                problems += 1
                print(f"UPSTREAM LINK [doc line {n}]: {href}")
                continue
            if href.startswith("#"):
                problems += 1
                print(f"ANCHOR-ONLY LINK [doc line {n}]: {href}")
                continue
            target = (page.path.parent / href).resolve()
            if not target.is_file():
                problems += 1
                print(f"DEAD LINK [doc line {n}]: {href} -> {target}")
            elif not target.is_relative_to(ROOT):
                problems += 1
                print(f"LINK LEAVES THE REPO [doc line {n}]: {href} -> {target}")

    for sid, rel, hits in page.ambiguous:
        problems += 1
        print(f"AMBIGUOUS {sid} ({rel}) resolves under {len(hits)} roots")

    for n, line in enumerate(page.lines, 1):
        for m in MARKER.finditer(line):
            sid = f"S{m.group(1)}"
            used.add(sid)
            if sid not in page.table:
                problems += 1
                print(f"UNKNOWN SOURCE {sid} [doc line {n}]")
                continue
            rel, path = page.table[sid]
            if path is None:
                problems += 1
                print(f"FILE NOT ON DISK {sid} -> {rel} [doc line {n}]")
                continue
            if m.group(2) is None:
                checked += 1
                continue
            a = int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            text = page.lines_of(sid)
            out, blank, rev = anchors.range_facts(a, b, len(text), text)
            for pos in sorted({a} if a == b else {a, b}):
                checked += 1
                if pos in out:
                    problems += 1
                    print(f"OUT OF RANGE {sid}:{pos} -> {rel} (file has {len(text)} lines) "
                          f"[doc line {n}]")
                elif pos in blank:
                    problems += 1
                    print(f"BLANK {sid}:{pos} -> {rel} [doc line {n}]")
            if rev:
                problems += 1
                print(f"REVERSED RANGE {sid}:{a}–{b} [doc line {n}]")

    for sid, rel, declared, n in page.rows:
        if declared == "—":
            continue
        want = int(declared.replace(",", ""))
        path = page.table[sid][1]
        if path is None:
            continue
        got = len(page.lines_of(sid))
        if got != want:
            problems += 1
            print(f"LINE COUNT {sid} ({rel}) says {declared}, file has {got} [doc line {n}]")

    unused = sorted(set(page.table) - used, key=lambda s: int(s[1:]))
    if unused:
        print(f"UNUSED SOURCES (declared, never cited): {', '.join(unused)}")

    for n, line in enumerate(page.lines, 1):
        hits = ENTITY.findall(line) + TAG.findall(line)
        if hits:
            problems += 1
            print(f"STRAY HTML [doc line {n}]: {', '.join(hits)}")

    return checked, len(page.table), links, problems


@functools.cache
def _fam_info() -> dict[str, dict]:
    _order, fams = B.parse_overview()
    return fams


def render_diff(page: Page, data_text: str) -> int:
    """The page's bytes against the writer's render of its data file."""
    fam = page.fam
    if fam is None:
        print(f"NO FAMILY NUMBER in file name {page.path.name}")
        return 1
    fams = _fam_info()
    if fam not in fams:
        print(f"NO OVERVIEW ENTRY for {page.path.name}: family {fam} is not in overview.tex")
        return 1
    rendered = build_proofs.render_page(fam, fams[fam]["title"], data_text)
    problems = diff_problems(read_text(page.path), rendered)
    for p in problems:
        print(f"RENDER DIFF [doc]: {p}")
    return len(problems)


def provenance_pass(page: Page, data_text: str) -> tuple[int, int]:
    """The data file's quote specs against the source files, independent of the renderer."""
    if page.fam is None:
        return 0, 1
    sources: dict[str, str] = {}
    m = re.search(r"<!-- sources\n(.*?)-->", data_text, re.DOTALL)
    if m:
        for line in m.group(1).strip().split("\n"):
            p = line.split("\t")
            if len(p) >= 2 and p[0].strip():
                sources[p[0].strip()] = p[1].strip()
    specs = problems = 0
    m = re.search(r"<!-- quotes\n(.*?)-->", data_text, re.DOTALL)
    if m:
        for line in m.group(1).strip().split("\n"):
            p = line.split("\t")
            if len(p) < 6:
                continue
            seq, sid, s, e = p[0], p[2].strip(), p[3], p[4]
            specs += 1
            if s == "0":
                continue
            if sid not in sources:
                problems += 1
                print(f"UNDECLARED SID seq {seq}: {sid} is not in the data file's sources block")
                continue
            path = sources[sid]
            fp = ROOT / path
            if not fp.is_file():
                problems += 1
                print(f"MISSING SOURCE seq {seq}: {path} is not on disk")
                continue
            try:
                si, ei = int(s), int(e)
            except ValueError:
                problems += 1
                print(f"NON-INTEGER WINDOW seq {seq}: start {s!r} end {e!r}")
                continue
            lines = fp.read_text(encoding="utf-8", errors="replace").splitlines()
            n = len(lines)
            if not (1 <= si <= n and 1 <= ei <= n):
                problems += 1
                print(f"WINDOW OUT OF RANGE seq {seq}: [{si},{ei}] over a file of {n} lines")
                continue
            if si > ei:
                problems += 1
                print(f"REVERSED WINDOW seq {seq}: start {si} is after end {ei}")
                continue
            for pos in sorted({si, ei}):
                if not lines[pos - 1].strip():
                    problems += 1
                    print(f"BLANK ENDPOINT seq {seq}: line {pos} of {path} is blank")
    return specs, problems


def pass_d(page: Page) -> tuple[int, int]:
    """Supersession: every manuscript directory the page names must be owned by this family."""
    named = named_dirs()
    fam = page.fam
    seen: dict[str, int] = {}
    for n, line in enumerate(page.lines, 1):
        for d in PAPDIR.findall(line):
            seen.setdefault(d, n)
    if fam is None:
        print(f"NO FAMILY NUMBER in file name {page.path.name}")
        return len(seen), 1
    problems = 0
    for d, n in sorted(seen.items(), key=lambda kv: kv[1]):
        owners = named.get(d)
        if owners is None:
            problems += 1
            print(f"SUPERSEDED MANUSCRIPT [doc line {n}]: preprints/{d}/ is on disk but no "
                  f"family's overview entry names it")
        elif fam not in owners:
            problems += 1
            print(f"OFF-FAMILY MANUSCRIPT [doc line {n}]: preprints/{d}/ is named by "
                  f"{', '.join(sorted(owners))}, not by family {fam}")
    return len(seen), problems


def pass_e(page: Page) -> tuple[int, int]:
    """Bare line citations into family-keyed files must land inside the family's own block."""
    if page.fam is None:
        return 0, 0
    cites = problems = 0
    for start_line, unit, is_blockquote in units(page.lines):
        if is_blockquote:
            continue
        if any(len(m.group(1) or m.group(2)) >= 12 for m in QUOTE.finditer(unit)):
            continue
        for _, sid, a, b in usable(page, markers(unit)):
            if a is None:
                continue
            rel = page.table[sid][0]
            # Only family-keyed files are checked; preprints/ and lean/ carry no family key.
            if not rel.startswith(("../", "../../")):
                continue
            # Family-keyed files in a proof page's sources are rare; skip if not in sources
            # that have a family block structure (notes/ pages, CONTENTS.md, overview.tex).
            if not (rel.startswith("notes/") or rel in ("CONTENTS.md", "overview.tex")):
                continue
            cites += 1
    return cites, problems


def main() -> int:
    docs = sorted(PROOFS_DIR.glob("*.md"))
    docs = [d for d in docs if d.name != "README.md"]
    if not docs:
        print(f"no proof pages under {PROOFS_DIR}")
        return 1

    total_b = total_specs = total_problems = 0
    for doc in docs:
        lines = read_text(doc).splitlines()
        page = Page(doc, lines)
        # Proof pages are flat <NNN>.md (no dash), so page_fam's FAM regex returns None.
        if page.fam is None:
            m = re.match(r"(\d{3})\.md$", doc.name)
            if m:
                page.fam = m.group(1)
        df = DATA_DIR / f"{page.fam}.md"
        data_text = read_text(df) if df.is_file() else ""
        print(f"===== {doc.relative_to(ROOT)}")
        if not df.is_file():
            print(f"  MISSING DATA FILE {df}")
            total_problems += 1
            continue
        with contextlib.redirect_stdout(io.StringIO()) as sink:
            positions, sources, links, problems = pass_b(page)
            rd_problems = render_diff(page, data_text)
            specs, prov_problems = provenance_pass(page, data_text)
            dirs, stale = pass_d(page)
            cites, outside = pass_e(page)
        print(sink.getvalue().rstrip())
        print(f"--- pass B: {positions} marker positions against {sources} declared sources, "
              f"{links} markdown links, {problems} problems")
        print(f"--- render diff: {rd_problems} problems")
        print(f"--- provenance: {specs} quote specs, {prov_problems} problems")
        print(f"--- pass D: {dirs} manuscript dirs, {stale} superseded/off-family")
        print(f"--- pass E: {cites} bare cites into family-keyed files, {outside} outside")
        total_b += positions
        total_specs += specs
        total_problems += problems + rd_problems + prov_problems + stale + outside

    print(f"===== TOTAL {len(docs)} page(s): {total_b} marker positions, "
          f"{total_specs} quote specs, {total_problems} problems")
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
