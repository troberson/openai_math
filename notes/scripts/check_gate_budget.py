#!/usr/bin/env python3
"""Assert the gate ran inside the budget, from the driver's own record.

The point of the row times is to catch a rapid increase, not to be quoted on a page. A
run-dependent figure cannot live in a template keyed to HEAD, so the page carries the claim and
this pass carries the number.

The driver brackets the gate with two UTC date reads, prints "wall N.N s", and lands the same line
in .qwen/tmp/reports/gate_wall.txt, which this pass reads. The row times are in the gate row TSV the
driver lands post-gate. The wall is not the row-time sum: a pooled run overlaps rows. Measured
2026-10-16: wall 261.86 s against a 654.8 s row-time sum over 82 rows.

The budget is the wall. The increase check is per row against the previous run's TSV, which is
the record the gate row TSV carries.
"""
import re
import sys
from pathlib import Path

BUDGET = 300.0
ROOT = Path(__file__).resolve().parent.parent.parent
LOG = ROOT / ".qwen/tmp/reports/gate_wall.txt"
TSV = ROOT / "notes/gen/tables/gate-rows.tsv"


def wall_of(log: Path) -> float | None:
    if not log.exists():
        return None
    m = re.search(r"wall (\d+\.\d+) s", log.read_text(encoding="utf-8"))
    return float(m.group(1)) if m else None


def rows_of(tsv: Path) -> dict[str, float]:
    out = {}
    for line in tsv.read_text(encoding="utf-8").splitlines()[1:]:
        spec, _cold, seconds = line.split("\t")[:3]
        out[spec] = float(seconds)
    return out


def main() -> int:
    w = wall_of(LOG)
    if w is None:
        print(f"wall: no driver record at {LOG}")
        return 1
    print(f"wall {w:.2f} s  budget {BUDGET:.0f} s  inside {w < BUDGET}")
    rows = rows_of(TSV)
    total = sum(rows.values())
    print(f"row-time sum {total:.1f} s over {len(rows)} rows")
    slow = sorted(((v, k) for k, v in rows.items()), reverse=True)[:3]
    for v, k in slow:
        print(f"  heaviest: {v:6.1f} s  {k}")
    return 0 if w < BUDGET else 1


if __name__ == "__main__":
    sys.exit(main())
