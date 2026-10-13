#!/usr/bin/env python3
"""Verify every citation in notes/reports/scope-exclusions.md against the shipped scope notes. Writes nothing.

The page carries one table row per family with a scope note. Each row is either **None stated.** or a
sequence of “quotation” `lean/docs/NNN.md:<line>` pairs. Five passes read the same rows:

  Pass A (coverage)  - exactly 242 rows, one per family that has a `## Scope` section, each id exactly
                       once, matching the files on disk.
  Pass B (anchors)   - every citation names a file that exists, a line that exists, and a line inside
                       that file's `## Scope` section. A citation to the Comparator table is a real
                       line in a real file and proves nothing about scope, so the span is checked.
  Pass C (quotes)    - every quotation must appear, verbatim, on the line it cites. Pass B proves the
                       line exists; it proves nothing about the text attributed to it.
  Pass D (numbers)   - the Measurements table and the prose counts are re-measured from the files on
                       disk and compared with what the page states.
  Pass E (sync)      - the page is compared with notes/scripts/render_reports.py's render of it, so
                       prose the count passes never parse cannot drift from the writer's template.
                       Pass D proves the numbers are measured; it proves nothing about the sentences
                       around them.

The self-tests live in `tests/test_scope_exclusions.py`: they corrupt a real quotation, cite a real
quotation to a line outside the Scope section, invent a quotation the file does not contain, delete a
family row, and alter a prose count outside the measured tables (visible only to Pass E), asserting
Pass A-E flags each while the real page stays silent. This script measures; it no longer injects.

Usage: python3 notes/scripts/verify_scope_exclusions.py
       python3 -m pytest tests/test_scope_exclusions.py -q
"""
import re
import sys
from pathlib import Path

import extract_scope_notes as ex
from catlib import render as RD
from catlib import yaml as Y
from catlib.paths import DOCS_DIR
from catlib.text import strip_markup as norm

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "reports" / "scope-exclusions.md"

ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*$")
PAIR = re.compile(r"^“(.+)”\s*`lean/docs/(\d{3})\.md:(\d+)`$")
MEASURE = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
TAG = re.compile(r"<[a-zA-Z/][^>]*>")
ENTITY = re.compile(r"&#[0-9]+;|&[a-zA-Z][a-zA-Z0-9]*;")
COUNTS = re.compile(r"(\d+) of (\d+) sections state at least one exclusion, carrying (\d+) exclusion")
NONE_LINE = re.compile(r"(\d+) state none\.")


def entry_rows(lines):
    """(family, cell, doc line) for every row of the Entries table, skipping the header and rule."""
    out = []
    for n, line in enumerate(lines, 1):
        m = ROW.match(line)
        if not m:
            continue
        if m.group(1) == "Family" or set(m.group(2)) <= {"-"}:
            continue
        out.append((m.group(1), m.group(2), n))
    return out


def measured():
    """Every number the page states, recomputed from the files on disk."""
    import statistics

    texts = {p: p.read_text(encoding="utf-8", errors="replace").splitlines()
             for p in Y.doc_files()}
    spans = {p: Y.scope_span_lines(t) for p, t in texts.items()}
    counts = [last - first + 1 for first, last in (sp for sp in spans.values() if sp)]

    def hits(phrases):
        # The section text, not the whole file: the same rule the extractor reports.
        return sum(1 for p, sp in spans.items() if sp
                   and any(phrase in " ".join(texts[p][sp[0] - 1:sp[1]]).lower()
                           for phrase in phrases))

    return {
        "Scope notes": len(texts),
        "Docs with both `## Scope` and `## Comparator links`": sum(
            1 for t in texts.values()
            if any(l.strip() == "## Scope" for l in t)
            and any(l.strip() == "## Comparator links" for l in t)),
        "`## Scope` section lines": sum(counts),
        "Scope-note lines, all files": sum(len(t) for t in texts.values()),
        "Lines per section (min / median / max)":
            f"{min(counts)} / {int(statistics.median(counts))} / {max(counts)}",
        "Docs hit by the 5-phrase narrow list": hits(ex.NARROW),
        "Docs hit by the 24-phrase broad list": hits(ex.BROAD),
    }


def check(lines):
    """Every problem found in the page. Empty list means the page is clean."""
    problems = []
    for n, line in enumerate(lines, 1):
        if TAG.search(line) or ENTITY.search(line):
            problems.append(f"doc line {n}: raw HTML markup")

    rows = entry_rows(lines)
    on_disk = {p.stem for p in Y.doc_files()}
    seen = [f for f, _, _ in rows]
    if len(seen) != len(set(seen)):
        dupes = sorted({f for f in seen if seen.count(f) > 1})
        problems.append(f"family ids repeated in the Entries table: {' '.join(dupes)}")
    missing = sorted(on_disk - set(seen))
    extra = sorted(set(seen) - on_disk)
    if missing:
        problems.append(f"families with a scope note and no row: {' '.join(missing)}")
    if extra:
        problems.append(f"rows naming no scope note: {' '.join(extra)}")
    if len(rows) != len(on_disk):
        problems.append(f"Entries table has {len(rows)} rows, {len(on_disk)} scope notes on disk")

    quotes = 0
    excl_rows = 0
    for fam, cell, n in rows:
        if cell.strip() == "**None stated.**":
            continue
        excl_rows += 1
        parts = [p.strip() for p in cell.split("·")]
        for part in parts:
            m = PAIR.match(part)
            if not m:
                problems.append(f"{fam} row at doc line {n}: not a quotation-plus-citation pair: {part[:60]}")
                continue
            quote, cited_fam, cited_line = m.group(1), m.group(2), int(m.group(3))
            quotes += 1
            if cited_fam != fam:
                problems.append(f"{fam} row at doc line {n}: cites {cited_fam}.md")
            path = DOCS_DIR / f"{cited_fam}.md"
            if not path.is_file():
                problems.append(f"{fam} row at doc line {n}: {path.name} does not exist")
                continue
            src = path.read_text(encoding="utf-8", errors="replace").splitlines()
            span = Y.scope_span_lines(src)
            if span is None:
                problems.append(f"{fam} row at doc line {n}: {path.name} has no `## Scope` section")
                continue
            first, last = span
            if not first <= cited_line <= last:
                problems.append(f"{fam} row at doc line {n}: {path.name}:{cited_line} is outside the "
                                f"`## Scope` section (lines {first}-{last})")
                continue
            if cited_line > len(src):
                problems.append(f"{fam} row at doc line {n}: {path.name}:{cited_line} is past the file end")
                continue
            if norm(quote) not in norm(src[cited_line - 1]):
                problems.append(f"{fam} row at doc line {n}: quotation not on {path.name}:{cited_line}")

    hits = COUNTS.search("\n".join(lines))
    stated = [int(x) for x in hits.groups()] if hits else None
    if stated is None:
        problems.append("prose count line for exclusions not found")
    else:
        none = NONE_LINE.search("\n".join(lines))
        stated_none = int(none.group(1)) if none else -1
        if stated != [excl_rows, len(rows), quotes] or stated_none != len(rows) - excl_rows:
            problems.append(f"prose counts {stated} + {stated_none} none, "
                            f"table gives {excl_rows} + {len(rows)} + {quotes} + {len(rows) - excl_rows} none")

    block = "\n".join(lines)
    for label, value in measured().items():
        m = re.search(r"^\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|\s*$", block, re.MULTILINE)
        if not m:
            problems.append(f"measurements table names no value for: {label}")
        elif m.group(1) != str(value):
            problems.append(f"measurements table says {label} = {m.group(1)}, files give {value}")

    return problems, len(rows), excl_rows, quotes


def main():
    text = PAGE.read_text(encoding="utf-8")
    lines = text.splitlines()
    problems, rows, excl, quotes = check(lines)
    sync = RD.sync_problems(PAGE, text)
    problems.extend(sync)
    print(f"page: {PAGE.relative_to(ROOT)}")
    print(f"rows {rows}, families with a stated exclusion {excl}, "
          f"none-stated {rows - excl}, quotations {quotes}")
    print(f"sync problems: {len(sync)}")
    print(f"problems: {len(problems)}")
    for p in problems:
        print(f"  {p}")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
