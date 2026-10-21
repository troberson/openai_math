#!/usr/bin/env python3
r"""Seed the quote-spec table for the pair-line page and the 24 summaries pages, and prove the
resolved span reproduces every quote.

A spec is `(page, fam, seq, which, path, start, end, span)`: the source file, the line window
the quote sits on, and the verbatim source span the seeder resolved. The renderer reads `span`
directly and feeds it to the normalizer; it never re-resolves. `head`/`tail` are seeder-internal:
the seeder uses them once, at seed time, to bound a span inside the window, then discards them.
`mode` (raw/folded/none) is not stored: for a generated page there is no independent quote to
classify.

**The two page grammars are two seeders.** `notes/reports/subfinding-pairs.md` cites by anchor:

    - main|clause: "<clause>" (`overview.tex:94`) -> "<title>" (`overview.tex:94`) [009:3]

The anchors inside it are read with `catlib.quotes.ANCH`, which is `catlib.anchors.anchor_pattern` with the
manuscript extension set and ranges allowed -- the same grammar the page's checker uses. `which` is
`clause`, `main`, or `title`; `seq` is the manuscript the pair names. The window is seeded from the anchored
line and widened downward to `MAXW` lines, because a manuscript sentence wraps.

A summaries page cites by a `[Sn:line]` marker, so the window is the range the marker names and no widening
is needed. The span set, the attribution and the classification are the shared rules
(`catlib.summaries.spans_of`, `catlib.summaries.candidates`, `catlib.quotes.seed_page`), so the specs seeded
here are exactly the spans `verify_summaries.py` pass C checks. `which` is `inline` or `block`; `seq` is the
span's index in the page, which is also the slot key the per-family template's quote slots join to.

The table lands at `notes/tables/quotes.tsv` through the promote registry, so the cached bytes and the
tracked bytes are the same bytes. `--check-only` runs the full measurement and writes nothing.

Usage: python3 notes/scripts/seed_quotes.py [--tsv] [--check-only]
"""
import re
import sys

from catlib.paths import ROOT, SUMMARIES_DIR
from catlib.promote import key_for, promote
from catlib.quotes import ANCH, resolve, seed, seed_page
from catlib.summaries import Page
from catlib.text import strip_markup
from catlib.tsv import csv_text, rows_text

PAGE = ROOT / "notes" / "reports" / "subfinding-pairs.md"
SRC = ROOT / "overview.tex"
OUT = ROOT / "notes" / "tables" / "quotes.tsv"
PAGES = str(PAGE.relative_to(ROOT))

COLS = ("page", "fam", "seq", "which", "path", "start", "end", "span")

# The widest window the pair-line seeder widens a spec to. Measured 2026-10-12: every pair-line quote
# sits on the anchored line, and the summaries spans, seeded against the range their own marker names,
# reach 26 lines, so this bound is never reached by the page it applies to.
MAXW = 24

HEADER = re.compile(r"^## (?P<fam>\d{3}) · `overview\.tex:(?P<line>\d+)` · n=(?P<n>\d+) · (?P<tier>T\d)$")
PAIR = re.compile(r'^-\s+(?P<kind>main|clause):\s+"(?P<q>.*?)"\s+\((?P<a>`[^`]+`)\)\s+->\s+(?P<rest>.*)$')
TARGET = re.compile(r'^"(?P<t>.*?)"\s+\((?P<a>`[^`]+`)\)\s+\[(?P<fam>\d{3}):(?P<seq>\d+)\]$')


def anchor(text: str) -> tuple[str, int, int]:
    """The (path, start, end) a backticked anchor names, read with the shared page grammar."""
    m = ANCH.search(text)
    if not m:
        return ("", 0, 0)
    start = int(m.group(2))
    return (m.group(1), start, int(m.group(3)) if m.group(3) else start)


def rows(lines: list[str]) -> list[tuple[dict[str, str], str]]:
    """Every pair-line quote in the page, seeded to a spec with its resolved span."""
    out: list[tuple[dict[str, str], str]] = []
    fam = ""
    for ln in PAGE.read_text(encoding="utf-8").splitlines():
        h = HEADER.match(ln)
        if h:
            fam = h.group("fam")
            continue
        m = PAIR.match(ln)
        if not m:
            continue
        t = TARGET.match(m.group("rest"))
        path, start, end = anchor(m.group("a"))
        items = [(m.group("kind"), m.group("q"), t.group("seq") if t else "")]
        if t:
            items.append(("title", t.group("t"), t.group("seq")))
        for which, q, seq in items:
            got = seed(lines, q, start, end + MAXW - 1)
            if got is None:
                out.append(({"page": PAGES, "fam": fam, "seq": seq, "which": which, "path": path,
                             "start": "0", "end": "0", "span": ""}, q))
                continue
            s, e, head, tail = got
            span = resolve(lines, s, e, head, tail) or ""
            out.append(({"page": PAGES, "fam": fam, "seq": seq, "which": which, "path": path,
                         "start": str(s), "end": str(e), "span": span}, q))
    return out


def summary_rows() -> list[tuple[dict[str, str], str]]:
    """Every quoted span the 24 summaries pages carry, seeded to a spec with its resolved span.

    `path` is the file the page's `[Sn]` row resolves to, repo-relative, so a row names a file the
    renderer can read without knowing the manuscript root. A span with no usable citation, or one the
    cited file does not carry, is seeded to `start` 0 with `span` empty (a measured negative).
    """
    out: list[tuple[dict[str, str], str]] = []
    for p in sorted(SUMMARIES_DIR.rglob("*.md")):
        page = Page(p, p.read_text(encoding="utf-8").splitlines())
        for n, (sid, which, span, start, end, head, tail, mode) in enumerate(seed_page(page), 1):
            src = page.table.get(sid, ("", None))[1]
            if mode == "none" or src is None:
                span_cell = ""
            else:
                # `span` is the page's quote; store the resolved SOURCE text the normalizer
                # renders, which is `span` byte-for-byte for raw and carries the markup the
                # page dropped for folded.
                span_cell = resolve(page.lines_of(sid), start, end, head, tail or None) or ""
            out.append(({"page": str(p.relative_to(ROOT)), "fam": page.fam or "", "seq": str(n),
                         "which": which, "path": str(src.relative_to(ROOT)) if src else "",
                         "start": str(start), "end": str(end), "span": span_cell}, span))
    return out


def main() -> int:
    args = tuple(sys.argv[1:])
    lines = SRC.read_text(encoding="utf-8").splitlines()
    all_rows = rows(lines) + summary_rows()
    specs = [s for s, _q in all_rows]
    # The round-trip is span-vs-page-quote: the seeder stored the resolved source text, so a row
    # passes when that text is the page's quote byte-for-byte (raw) or equal after the checker's
    # normalizer (folded, the page dropped markup the source carries). A `span` that is neither
    # resolves to text the page does not quote, which is the failure. No re-resolution is needed:
    # the span is the resolved bytes, and `head`/`tail` are seeder-internal.
    bad: list[tuple[str, str, str]] = []
    for spec, q in all_rows:
        span = spec["span"]
        if span == "":
            # A measured negative: the cited file does not carry the span.
            continue
        ok = span == q or strip_markup(span) == strip_markup(q)
        if not ok:
            bad.append((f"{spec['page']} [{spec['fam']}:{spec['seq']} {spec['which']}]",
                        span[:30], f"span {span[:44]!r} vs quote {q[:44]!r}"))
    seeded = [s for s in specs if s["start"] != "0"]
    pair = [s for s in specs if s["page"] == PAGES]
    summ = [s for s in specs if s["page"] != PAGES]
    # The raw/folded split is derived from the stored span, not a recorded column: raw when the span
    # is the page quote byte-for-byte, folded when it is equal only after the normalizer.
    raw = sum(1 for s, q in all_rows if s["span"] != "" and s["span"] == q)
    folded = (sum(1 for s, q in all_rows if s["span"] != ""
                  and s["span"] != q and strip_markup(s["span"]) == strip_markup(q)))
    print(f"quotes in the pages: {len(specs)}")
    print(f"  pair-line specs ({PAGES}): {len(pair)}")
    print(f"  summaries specs ({len({s['page'] for s in summ})} pages): {len(summ)}")
    print(f"  specs seeded: {len(seeded)}   measured negatives (start 0): {len(specs) - len(seeded)}")
    print(f"  single-line spec: {sum(1 for s in seeded if s['start'] == s['end'])}"
          f"   range spec: {sum(1 for s in seeded if s['start'] != s['end'])}")
    print(f"  class: raw {raw}  folded {folded}  not located {len(specs) - len(seeded)}")
    print(f"  span reproduces the page quote: {len(seeded) - len(bad)} of {len(seeded)}")
    print(f"  round-trip failures: {len(bad)}")
    for where, head, why in bad:
        print(f"    [{where}] {head}  -- {why}")
    if "--tsv" in args:
        print()
        print(rows_text(COLS, specs))
    if "--check-only" in args:
        print("[check-only] nothing written")
    else:
        promote(OUT, key_for("seed_quotes.py", args), csv_text(COLS, specs))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
