#!/usr/bin/env python3
r"""Measure the quote-spec resolver over the 24 summaries pages and classify every quoted span.

The seeder at `seed_quotes.py` seeds a spec for each span this probe classifies, so the probe is the
measurement the seeded table is checked against: it counts the spans the pages carry, the class each
round-trip lands in, and the window width each spec names. Report-only; writes nothing.

The span set and the citation attribution are `catlib.summaries.spans_of` and
`catlib.summaries.candidates` — the same rules `verify_summaries.py` pass C runs, so a span this probe
counts is the span the checker checks, and a span it attributes is the span the checker attributes. The
classification is `catlib.quotes.seed_page`: `raw` when the resolved span is the page's quote
byte-for-byte, `folded` when it is equal only after the checker's normalizer (the page dropped markup
the source carries), `none` when the cited file does not carry the span.

Measured 2026-10-13 over the 25 pages: **1038** spans of 12 characters or more, **966** raw-equal,
**57** fold-equal, **15** not located, **0** resolving to text the page does not quote. **832** spans
are inline and **206** are block quotes. **335** spans sit in one source line and **688** sit across 2
to 26 lines; the widths are 1:335 2:339 3:187 4:64 5:29 6:12 7:9 8:13 9:5 10:6 11:4 12:1 13:3 14:2
15:1 16:3 17:2 18:2 19:2 20:2 21:1 26:1, and the 15 unlocated spans carry no width, so the width
histogram sums to 1,023.

Usage: python3 notes/scripts/measure_summaries_seed.py
"""
from collections import Counter

from catlib.paths import SUMMARIES_DIR
from catlib.quotes import seed_page
from catlib.summaries import Page


def main() -> int:
    pages = sorted(SUMMARIES_DIR.rglob("*.md"))
    counts: Counter[str] = Counter()
    widths: Counter[int] = Counter()
    forms: Counter[str] = Counter()
    folded: list[tuple[str, str, str, str]] = []
    missing: list[tuple[str, str, str, str]] = []
    spans = 0
    for p in pages:
        page = Page(p, p.read_text(encoding="utf-8").splitlines())
        for sid, which, span, start, end, _head, _tail, mode in seed_page(page):
            spans += 1
            counts[mode] += 1
            forms[which] += 1
            if mode == "none":
                missing.append((p.name, sid, which, span[:60]))
                continue
            widths[end - start + 1] += 1
            if mode == "folded":
                folded.append((p.name, sid, which, span[:60]))
    print(f"pages {len(pages)}  spans {spans}  raw {counts['raw']}"
          f"  folded {counts['folded']}  not located {counts['none']}")
    print(f"forms: inline {forms['inline']}  block {forms['block']}")
    print("widths:", sorted(widths.items()))
    print(f"single-line {widths[1]}  multi-line {sum(v for k, v in widths.items() if k > 1)}")
    print(f"folded spans ({len(folded)}):")
    for name, sid, which, span in folded:
        print(f"  {name} [{sid}] {which} {span!r}")
    print(f"not located ({len(missing)}):")
    for name, sid, which, span in missing:
        print(f"  {name} [{sid}] {which} {span!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
