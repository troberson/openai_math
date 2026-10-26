#!/usr/bin/env python3
"""Write notes/gen/tables/gate-rows.tsv: the wall time of each row of the last completed gate run.

The report is **read**, not produced. `.qwen/tmp/reports/gate_run1.txt` is the driver's output for the
last completed run, and the driver truncates it at run start, so a writer reading it sees the previous
completed run — which is what the census page records. A writer that ran the gate would be a gate row
that runs the gate, so this script is a post-gate step and is deliberately not in `gate.py`'s `ROWS`.

Row format, as the driver prints it:

    exit 0 :: build_catalog.py :: families 372 manuscripts 719 … in 0.1s

`spec` is the second field of the ` :: ` split — the invocation exactly as `gate.py` lists it, so the
`run_tests.py … -q` form and the `--check-only` flag are part of the key. `seconds` is the trailing
` in N.Ns` field. The driver prints no total wall, so the table has per-row times and their sum, not a
wrap time.

Reconciliation is against `gate.py`'s `ROWS` block, parsed with `ast` (the block is one array of
`(spec, needs, writes)` triples, so a regex over the specs would mis-split a spec containing a
parenthesis). The TSV must carry exactly one row per gate row, in list order, and every spec must
appear exactly once in the report.

Usage: python3 notes/scripts/measure_gate_rows.py [--check-only]
"""
from __future__ import annotations

import ast
import json
import re
import sys
from datetime import datetime

from catlib.atomic import RECORDS_ROOT
from catlib.paths import GATE_REPORT, GATE_ROWS_TSV, SCRIPTS, read_text
from catlib.promote import key_for, promote, row_key
from catlib.tsv import csv_text

OUT = GATE_ROWS_TSV
GATE_PY = SCRIPTS / "gate.py"
KEY = key_for("measure_gate_rows.py", tuple(sys.argv[1:]))
COLUMNS = ["spec", "cold", "seconds"]


def gate_rows() -> list[tuple[str, str, str]]:
    """gate.py's ROWS as (spec, needs, writes), parsed from the source, not from a regex."""
    tree = ast.parse(read_text(GATE_PY))
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "ROWS":
            return [tuple(item) for item in ast.literal_eval(node.value)]
    raise SystemExit(f"ROWS assignment not found in {GATE_PY}")


def parse_report(text: str) -> list[dict[str, str]]:
    """The row lines the driver printed: exit code, spec, report text, wall time."""
    rows = []
    for line in text.splitlines():
        if not line.startswith("exit "):
            continue
        parts = line.split(" :: ")
        if len(parts) < 3:
            continue
        m = re.search(r" in (\d+\.\d+)s$", parts[-1])
        if not m:
            continue
        rows.append({"spec": parts[1], "seconds": m.group(1), "exit": parts[0].split()[1]})
    return rows


def cold_of(spec: str, seconds: str) -> str:
    """The cold cost: the wall the row's subprocess last paid.

    A keyable row's record carries that wall, so a skipped row (this run's wall ~0) still
    names what the last real run cost. A non-keyable row always runs, so this run's wall is
    its cold cost. The figure names its rule: cold is the last actual run, seconds is this run.
    """
    rk = row_key(spec)
    if rk is None:
        return seconds
    rec_path = RECORDS_ROOT / rk[0] / "row.json"
    if rec_path.is_file():
        wall = json.loads(rec_path.read_text(encoding="utf-8")).get("wall")
        if wall is not None:
            return f"{float(wall):.1f}"
    return seconds


def write(rows: list[dict[str, str]]) -> None:
    promote(OUT, KEY, csv_text(COLUMNS,
            [{"spec": r["spec"], "cold": cold_of(r["spec"], r["seconds"]),
              "seconds": r["seconds"]} for r in rows]))


def report(rows: list[dict[str, str]], specs: list[str]) -> None:
    total = sum(float(r["seconds"]) for r in rows)
    seen = [r["spec"] for r in rows]
    failed = [r["spec"] for r in rows if r["exit"] != "0"]
    print(f"report file            {GATE_REPORT.relative_to(GATE_REPORT.parents[3])}")
    print(f"report mtime           {datetime.fromtimestamp(GATE_REPORT.stat().st_mtime):%Y-%m-%d %H:%M:%S}")
    print(f"gate rows (gate.py)    {len(specs)}")
    print(f"rows read from report  {len(rows)}  equal {len(rows) == len(specs)}")
    print(f"order equal to ROWS    {seen == specs}")
    print(f"specs in report not in ROWS  {len(set(seen) - set(specs))} {sorted(set(seen) - set(specs))[:3]}")
    print(f"specs in ROWS not in report  {len(set(specs) - set(seen))} {sorted(set(specs) - set(seen))[:3]}")
    print(f"specs repeated in report     {len(seen) - len(set(seen))}")
    print(f"sum of seconds         {total:.1f}")
    print(f"rows with exit != 0    {len(failed)} {failed[:3]}")
    print(f"heaviest row           {max(rows, key=lambda r: float(r['seconds']))['spec']} "
          f"{max(float(r['seconds']) for r in rows):.1f}")


def main() -> int:
    if not GATE_REPORT.is_file():
        raise SystemExit(f"gate report not on disk: {GATE_REPORT}")
    rows = parse_report(read_text(GATE_REPORT))
    specs = [spec for spec, _needs, _writes in gate_rows()]
    if not rows:
        print("PROBLEM: no row lines in the report")
        return 1
    if "--check-only" not in sys.argv[1:]:
        write(rows)
    report(rows, specs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
