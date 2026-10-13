#!/usr/bin/env python3
"""Verify every citation in a family summary page against the files it names. Writes nothing.

The page body cites sources as [S4:29], [S4:29–56] or [S4]; the Sources table at the bottom maps
S# to a file. Two passes read the same table:

  Pass B (markers)  - resolve every marker, print the line it names, flag out-of-range, blank and
                      reversed-range positions, check the table's declared line counts against the
                      files on disk, resolve every markdown link from the page's own directory, and
                      require zero raw HTML anywhere in the page.
  Pass C (quotes)   - every quoted span of a cited unit must appear, verbatim, in the lines that
                      unit cites. Pass B proves a line exists; it proves nothing about the text we
                      attribute to it, so a paraphrase dressed as a quote passes Pass B.

Pass A (the needle check: does the page contain the specific strings the reading pass recorded) is
written per page against that page's own findings, so it is not promoted here.

Passes B and C both prove things about the text at a cited line; neither says the line belongs to
the family the page is about. An upstream update leaves the manuscripts it replaced on disk, tracked
in git, with their names unchanged, so a page can stay green through B and C while describing a
manuscript the release no longer names. Two more passes close that gap:

  Pass D (supersession) - every manuscript directory the page names must be one the catalog's
                      overview entry currently names, and it must be named by *this* family. A
                      directory that is on disk and named by no family is a superseded manuscript.
  Pass E (bare cites) - a citation in a unit that carries no quotation makes a location claim, and
                      in a file whose blocks are keyed by family number (CONTENTS.md, overview.tex,
                      README.md, notes/*.md) the only legal location is the family's own block.
                      Files with no family key — manuscripts, Lean sources, yaml, tsv — are skipped:
                      the pass makes no claim about them.

--mutant is gone: the self-tests live in `notes/scripts/tests/test_summaries.py`, run through
`notes/scripts/run_tests.py`. Seven tests inject in memory over the real pages' own text — a quotation
corrupted in each form a page uses (inline, wrapped across line breaks, block quote), a fabricated
quotation, the manuscript root retargeted to a superseded sibling, and a bare locator citation moved
above the family's own block — each asserted against the pass that owns it. The tests mirror the
checker's own selection: the first target of each form per page, and a page whose target has no word
boundary is skipped. This script measures; it no longer injects.

Usage: python3 notes/scripts/verify_summaries.py                 # every page under notes/summaries
       python3 notes/scripts/verify_summaries.py <page.md> ...   # named pages only

What stays in this file, deliberately: the family-keyed block rules (`BLOCK_RULES`, `NOTE_ENTRY`),
which are pass E's contract, not the page's; and Pass A, which is written per page against that page's
findings. The page grammar (`ROW`, `CELL`, `MARKER`, `QUOTE`, `LINK`, `ENTITY`, `TAG`, `PAPDIR`), the
`Page` class, the marker/unit joins, the block-quote attribution rule (`candidates`), the span rule
(`spans_of`), the two unit exemptions (`FORMAT_EXAMPLE`, `PRIOR`), the lenient `errors="replace"` read
of a declared source, and the manuscript-ownership map are in `catlib/summaries.py`, shared with
`locate_summary_quotes.py`, `refresh_summary_line_counts.py`, `check_summary_manuscripts.py`,
`measure_summaries_seed.py` and `seed_quotes.py`.
"""
import argparse
import os
import re
import sys
from pathlib import Path

from catlib.paths import ROOT, SUMMARIES_DIR, read_text
from catlib.summaries import (
    ENTITY,
    FORMAT_EXAMPLE,
    LINK,
    MARKER,
    PAPDIR,
    PRIOR,
    QUOTE,
    TAG,
    Page,
    candidates,
    label,
    markers,
    named_dirs,
    spans_of,
    units,
    usable,
)
from catlib.text import strip_markup as norm

SUMMARIES = SUMMARIES_DIR

# Pass E applies only to files whose blocks are keyed by the family number, because that is the only
# case where "the family's own block" is a fact the file itself records. Manuscript and Lean files
# carry no family key, so the pass makes no claim about them.
BLOCK_RULES = {
    "CONTENTS.md": (re.compile(r"^\*\*(\d{1,3})\."), re.compile(r"^\*\*\d{1,3}\.")),
    "overview.tex": (re.compile(r"^\\resultentry\{(\d{1,3})\}"), re.compile(r"^\\resultentry\{")),
    "README.md": (re.compile(r"^\|\s*(\d{1,3})\s*\|"), None),
}
NOTE_ENTRY = re.compile(r"^- \*\*(\d{1,3})\*\*")


def pass_b(page):
    """Markers, links, declared line counts, ambiguous File cells, raw HTML.

    Returns (positions, sources, links, problems).
    """
    problems = 0
    checked = 0
    used = set()
    links = 0
    for n, line in enumerate(page.lines, 1):
        for m in LINK.finditer(line):
            href = m.group(1)
            links += 1
            if href.startswith(("http://", "https://", "mailto:")):
                problems += 1
                print(f"UPSTREAM LINK [doc line {n}]: {href} — this page links relatively, not upstream")
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
        print(f"AMBIGUOUS {sid} ({rel}) resolves under {len(hits)} roots: "
              f"{', '.join(str(h) for h in hits)} — the File cell is not the repository-relative path")

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
                print(f"{sid} = {rel}")
                continue
            a = int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            text = page.lines_of(sid)
            for pos in ({a} if a == b else {a, b}):
                checked += 1
                if not 0 < pos <= len(text):
                    problems += 1
                    print(f"OUT OF RANGE {sid}:{pos} -> {rel} (file has {len(text)} lines) "
                          f"[doc line {n}]")
                elif not text[pos - 1].strip():
                    problems += 1
                    print(f"BLANK {sid}:{pos} -> {rel} [doc line {n}]")
            if a > b:
                problems += 1
                print(f"REVERSED RANGE {sid}:{a}–{b} [doc line {n}]")
            span = " ".join(text[a - 1:max(a, b)]).strip()
            print(f"{sid}:{a}" + (f"–{b}" if b != a else "") + f" -> {rel} | {span[:58]}")

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

    # Zero HTML anywhere, including inside block quotes. The release writes HTML in its blurbs
    # (&emsp;, <i>p</i>); the page renders that markup as markdown and drops the indentation
    # entity, so a tag or entity surviving in the finished page is a paste artifact.
    for n, line in enumerate(page.lines, 1):
        hits = ENTITY.findall(line) + TAG.findall(line)
        if hits:
            problems += 1
            print(f"STRAY HTML [doc line {n}]: {', '.join(hits)}")

    return checked, len(page.table), links, problems


def pass_c(page):
    """Quote fidelity. Returns (spans, misses)."""
    checked = misses = 0
    for start_line, unit, is_blockquote in units(page.lines):
        if not is_blockquote and PRIOR in unit:
            # A prior paragraph is explicitly not repo text; nothing in it is a quotation.
            continue
        cands = candidates(page, unit, start_line, is_blockquote)
        for span in spans_of(unit, is_blockquote):
            if not cands:
                print(f"NO CITATION in unit at doc line {start_line}: {span[:50]!r}")
                misses += 1
                continue
            hit = None
            for sid, a, b in cands:
                src = page.lines_of(sid)
                haystack = norm(" ".join(src[a - 1:max(a, b or a)]) if a else " ".join(src))
                if norm(span) in haystack:
                    hit = (sid, a, b)
                    break
            checked += 1
            if hit is None:
                misses += 1
                near = ", ".join(label(s, a, b) for s, a, b in cands[:4])
                print(f"NOT VERBATIM [doc line {start_line}] cited {near}")
                print(f"   page says : {norm(span)[:130]}")
                sid, a, b = cands[0]
                src = page.lines_of(sid)
                print(f"   line says : {norm(' '.join(src[a - 1:b] if a else src))[:130]}")
    return checked, misses


def pass_d(page):
    """Supersession. Every manuscript the page names must be one the catalog currently names for this family."""
    named = named_dirs()
    fam = page.fam
    seen: dict[str, int] = {}
    for n, line in enumerate(page.lines, 1):
        for d in PAPDIR.findall(line):
            seen.setdefault(d, n)
    if fam is None:
        print(f"NO FAMILY NUMBER in file name {page.path.name} — pass D cannot map the page to the catalog")
        return len(seen), 1
    problems = 0
    for d, n in sorted(seen.items(), key=lambda kv: kv[1]):
        owners = named.get(d)
        if owners is None:
            problems += 1
            print(f"SUPERSEDED MANUSCRIPT [doc line {n}]: preprints/{d}/ is on disk and tracked, but no "
                  f"family's overview entry names it — the release has moved on from this manuscript")
        elif fam not in owners:
            problems += 1
            print(f"OFF-FAMILY MANUSCRIPT [doc line {n}]: preprints/{d}/ is named by "
                  f"{', '.join(sorted(owners))}, not by family {fam}")
    return len(seen), problems


def family_blocks(rel, lines, fam):
    """Line spans of family `fam`'s own block(s) in a file whose blocks are keyed by family number.

    Returns None when the file carries no family key at all — a statement about the file, not about
    the citation. A block runs from its start token to the line before the next family's start token.
    """
    rule = BLOCK_RULES.get(rel)
    if rule is None:
        if rel.startswith("notes/") and rel.endswith(".md"):
            rule = (NOTE_ENTRY, NOTE_ENTRY)
        else:
            return None
    start, nxt = rule
    out, cur = [], None
    for i, line in enumerate(lines, 1):
        m = start.match(line)
        if m and int(m.group(1)) == fam:
            if nxt is None:
                out.append((i, i))
                continue
            cur = i
        elif nxt is not None and nxt.match(line):
            if cur:
                out.append((cur, i - 1))
                cur = None
    if cur:
        out.append((cur, len(lines)))
    return out


def bare_locator_cites(page):
    """Markers with line numbers, in units carrying no quoted span, into family-keyed files.

    A unit with a quotation is judged by Pass C against the text it quotes. A unit with none makes a
    location claim, and the only location a summary page may cite in a family-keyed file is that
    family's own block — a page citing a neighbour's block is citing the wrong family's record.
    """
    if page.fam is None:
        return []
    fam = int(page.fam)
    out = []
    for start_line, unit, is_blockquote in units(page.lines):
        if is_blockquote or FORMAT_EXAMPLE in unit or PRIOR in unit:
            continue
        if any(len(m.group(1) or m.group(2)) >= 12 for m in QUOTE.finditer(unit)):
            continue
        for _, sid, a, b in usable(page, markers(unit)):
            if a is None:
                continue
            rel = page.table[sid][0]
            bl = family_blocks(rel, page.lines_of(sid), fam)
            if bl is None:
                continue
            out.append((start_line, sid, a, b, rel, bl))
    return out


def pass_e(page):
    """Bare line citations into family-keyed files must land inside the family's own block."""
    cites = problems = 0
    for start_line, sid, a, b, rel, bl in bare_locator_cites(page):
        cites += 1
        if not any(s <= b and a <= e for s, e in bl):
            problems += 1
            near = ", ".join(f"{s}-{e}" for s, e in bl[:3]) if bl else "no block for this family"
            print(f"CITE OUTSIDE FAMILY BLOCK [doc line {start_line}] {label(sid, a, b)} -> {rel}: "
                  f"family {page.fam}'s block is {near}")
    return cites, problems


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("pages", nargs="*", help="summary pages (default: every page under notes/summaries)")
    ap.add_argument("--quiet", action="store_true", help="print only the summary lines")
    args = ap.parse_args()

    if args.pages:
        docs = [Path(p).resolve() for p in args.pages]
    else:
        docs = sorted(SUMMARIES.rglob("*.md"))
    if not docs:
        print(f"no summary pages under {SUMMARIES}")
        sys.exit(1)

    import contextlib
    io = sys.stdout
    total_b = total_c = total_problems = 0
    for doc in docs:
        lines = read_text(doc).splitlines()
        page = Page(doc, lines)
        # The tree's index page is link-only: it names no manuscript directory and cites no
        # family-keyed file, so pass D and pass E have nothing to check and its family-number rule
        # would fire on a file named `README.md`. Passes B and C still run, so its links are checked.
        link_only = doc.name == "README.md"
        print(f"===== {doc.relative_to(ROOT)}")
        with contextlib.ExitStack() as stack:
            sink = stack.enter_context(open(os.devnull, "w", encoding="utf-8")) if args.quiet else io
            stack.enter_context(contextlib.redirect_stdout(sink))
            positions, sources, links, problems = pass_b(page)
            spans, misses = pass_c(page)
            dirs, stale = (0, 0) if link_only else pass_d(page)
            cites, outside = (0, 0) if link_only else pass_e(page)
            print(f"--- pass B: {positions} marker positions against {sources} declared sources, "
                  f"{links} markdown links resolved from the page directory, {problems} problems")
            print(f"--- pass C: {spans} quoted spans checked against their cited lines, "
                  f"{misses} not verbatim")
            print(f"--- pass D: {dirs} manuscript directories named by the page, {stale} superseded "
                  f"or off-family")
            print(f"--- pass E: {cites} bare line citations into family-keyed files, {outside} "
                  f"outside the family's own block")
        total_b += positions
        total_c += spans
        total_problems += problems + misses + stale + outside
    print(f"===== TOTAL {len(docs)} page(s): {total_b} marker positions, {total_c} quoted spans, "
          f"{total_problems} problems")
    sys.exit(1 if total_problems else 0)


if __name__ == "__main__":
    main()
