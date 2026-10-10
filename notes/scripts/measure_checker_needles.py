#!/usr/bin/env python3
"""Report-only: what the template builder pays to derive each page checker's needles.

The builder derives a page's checker-coverage line by exec'ing the checker source and calling its
count_phrases/size_phrases with the population the checker exports (checker_needles below). That
derivation is the cost every render and census run carries, and it is not the figure
measure_checker_costs.sh reports, which times a checker's own run.

The page/checker pairs come from the builder's own registry, so the list cannot drift from the
pages the builder builds. A page whose checker exports no phrase functions prints 0 needles - the
NOT DERIVED case, measured rather than asserted.

Writes nothing. Run bare: python3 notes/scripts/measure_checker_needles.py
"""
from __future__ import annotations

import time

import build_report_templates as b
from catlib import paths as P


def main() -> int:
    total = 0.0
    needles_total = 0
    derived = 0
    for page, checker in sorted(b.ALL_PAGES.items()):
        start = time.time()
        needles = b.checker_needles(P.SCRIPTS / checker)
        elapsed = time.time() - start
        total += elapsed
        needles_total += len(needles)
        derived += 1 if needles else 0
        print(f"{checker:<34} {page:<38} {len(needles):3d} needles  {elapsed:7.2f}s")
    print(f"pages {len(b.ALL_PAGES)}  derived {derived}  needles {needles_total}  "
          f"derivation cost {total:.2f}s")
    print("NEEDLE_PROOF_DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
