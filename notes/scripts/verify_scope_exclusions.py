#!/usr/bin/env python3
"""Verify every citation in notes/scope-exclusions.md against the shipped scope notes. Writes nothing.

The page carries one table row per family with a scope note. Each row is either **None stated.** or a
sequence of “quotation” `lean/docs/NNN.md:<line>` pairs. Four passes read the same rows:

  Pass A (coverage)  - exactly 235 rows, one per family that has a `## Scope` section, each id exactly
                       once, matching the files on disk.
  Pass B (anchors)   - every citation names a file that exists, a line that exists, and a line inside
                       that file's `## Scope` section. A citation to the Comparator table is a real
                       line in a real file and proves nothing about scope, so the span is checked.
  Pass C (quotes)    - every quotation must appear, verbatim, on the line it cites. Pass B proves the
                       line exists; it proves nothing about the text attributed to it.
  Pass D (numbers)   - the Measurements table and the prose counts are re-measured from the files on
                       disk and compared with what the page states.

--mutant proves the checker discriminates: it corrupts a real quotation, cites a real quotation to a
line outside the Scope section, invents a quotation the file does not contain, and deletes a family
row, asserting Pass A-D flags each while the real page stays silent.

Usage: python3 notes/scripts/verify_scope_exclusions.py
       python3 notes/scripts/verify_scope_exclusions.py --mutant
"""
import re
import sys
from pathlib import Path

import extract_scope_notes as ex
from verify_summaries import norm

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "scope-exclusions.md"
DOCS = ROOT / "lean" / "docs"

ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*$")
PAIR = re.compile(r"^“(.+)”\s*`lean/docs/(\d{3})\.md:(\d+)`$")
MEASURE = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
TAG = re.compile(r"<[a-zA-Z/][^>]*>")
ENTITY = re.compile(r"&#[0-9]+;|&[a-zA-Z][a-zA-Z0-9]*;")
COUNTS = re.compile(r"(\d+) of (\d+) sections state at least one exclusion, carrying (\d+) exclusion")
NONE_LINE = re.compile(r"(\d+) state none\.")


def scope_span(lines):
    """(first, last) 1-based line numbers of the `## Scope` section, or None."""
    start = next((i for i, ln in enumerate(lines) if ln.strip() == "## Scope"), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return start + 1, end


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
             for p in sorted(DOCS.glob("*.md"))}
    spans = {p: scope_span(t) for p, t in texts.items()}
    counts = [last - first + 1 for first, last in spans.values() if first]

    def hits(phrases):
        # The section text, not the whole file: the same rule the extractor reports.
        return sum(1 for p, (first, last) in spans.items() if first
                   and any(phrase in " ".join(texts[p][first - 1:last]).lower()
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
    on_disk = {p.stem for p in DOCS.glob("*.md")}
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
            path = DOCS / f"{cited_fam}.md"
            if not path.is_file():
                problems.append(f"{fam} row at doc line {n}: {path.name} does not exist")
                continue
            src = path.read_text(encoding="utf-8", errors="replace").splitlines()
            span = scope_span(src)
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

    stated = [int(x) for x in COUNTS.search("\n".join(lines)).groups()] if COUNTS.search("\n".join(lines)) else None
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
        m = re.search(r"^\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|\s*$", block, re.M)
        if not m:
            problems.append(f"measurements table names no value for: {label}")
        elif m.group(1) != str(value):
            problems.append(f"measurements table says {label} = {m.group(1)}, files give {value}")

    return problems, len(rows), excl_rows, quotes


def main():
    mutant = "--mutant" in sys.argv
    lines = PAGE.read_text(encoding="utf-8").splitlines()
    problems, rows, excl, quotes = check(lines)
    print(f"page: {PAGE.relative_to(ROOT)}")
    print(f"rows {rows}, families with a stated exclusion {excl}, "
          f"none-stated {rows - excl}, quotations {quotes}")
    print(f"problems: {len(problems)}")
    for p in problems:
        print(f"  {p}")

    if not mutant:
        return 0 if not problems else 1

    print()
    print("mutants:")
    first_row = next(n for n, l in enumerate(lines, 1) if ROW.match(l))
    base = lines[first_row - 1]
    m = ROW.match(base)
    fam, cell = m.group(1), m.group(2)
    q = re.search(r"“([^”]+)”", cell).group(1)
    cite = re.search(r"`lean/docs/(\d{3})\.md:(\d+)`", cell)
    src = (DOCS / f"{fam}.md").read_text(encoding="utf-8", errors="replace").splitlines()
    first, last = scope_span(src)
    outside = next(n for n in range(last + 1, len(src) + 1) if src[n - 1].strip())

    cases = [
        # A real quotation with one word corrupted: Pass C must flag the text, not the anchor.
        ("corrupted quotation", base.replace(q, q.replace("the", "tbe", 1), 1), "not on"),
        # A real quotation cited to a real line outside the section: Pass B must check the span.
        ("citation outside the Scope section",
         base.replace(cite.group(0), f"`lean/docs/{fam}.md:{outside}`", 1),
         "outside the `## Scope` section"),
        # A quotation the cited file does not contain anywhere: Pass C must flag it.
        ("fabricated quotation",
         base.replace(q, "the formalization deliberately omits every companion result", 1),
         "not on"),
        # A paraphrase dressed as a quote: same section, same shape, different words.
        ("paraphrased quotation",
         base.replace(q, q.replace("are excluded in", "are omitted from", 1), 1),
         "not on"),
        # Line drift: a real quotation cited to a different non-blank real line in the same section.
        # Pass B accepts the anchor, so only Pass C can catch it.
        ("quotation cited to the wrong line in the section",
         base.replace(cite.group(0),
                      f"`lean/docs/{fam}.md:{next(n for n in range(int(cite.group(2)) + 1, last + 1) if src[n - 1].strip())}`",
                      1),
         "not on"),
    ]

    undetected = 0
    for name, mutated, expect in cases:
        cand = list(lines)
        cand[first_row - 1] = mutated
        got, _, _, _ = check(cand)
        hit = [p for p in got if expect in p]
        if not hit:
            undetected += 1
        print(f"  {name}: {'detected' if hit else 'UNDETECTED'} ({len(got)} problems)")

    # A family row deleted: Pass A must notice the table no longer covers the 235 notes.
    cand = [l for i, l in enumerate(lines) if i != first_row - 1]
    got, _, _, _ = check(cand)
    hit = [p for p in got if "no row" in p]
    if not hit:
        undetected += 1
    print(f"  deleted family row ({fam}): {'detected' if hit else 'UNDETECTED'} ({len(got)} problems)")

    print(f"undetected mutants: {undetected}")
    return 0 if (undetected == 0 and not problems) else 1


if __name__ == "__main__":
    sys.exit(main())
