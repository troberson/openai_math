#!/usr/bin/env python3
"""Verify every notes/tables TSV parses as RFC 4180 quoting.

GitHub's TSV viewer flags a `"` that is not at a field start as illegal quoting. Python's
`csv.DictReader(delimiter='\t')` is lenient — it treats a mid-field quote as literal data — so
the repo's checkers are silent on this class and GitHub is the only witness. This pass applies
GitHub's rule to every TSV under `notes/tables/`.

Rules, per field:
  - a field that does not start with `"` carries no `"` at all;
  - a field that starts with `"` closes inside the same field, and every interior `"` is doubled.

Writes nothing. Exit 0 means clean.

The self-tests live in `notes/scripts/tests/test_tsv_quoting.py`: they inject the four defects
into table text in memory and assert the pass that owns each one reports it. This script
measures; it injects nothing.

Usage:
  python3 notes/scripts/verify_tsv_quoting.py
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_tsv_quoting.py -q
"""
import sys

from catlib.paths import TABLES

QUOTE = '"'


def check(text, name):
    """-> (problems, rows, legal quoted fields). The quoting rule, run on table text."""
    problems = []
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if not lines:
        return [f"{name}: empty table"], 0, 0
    header = lines[0].split("\t")
    quoted = 0
    for i, row in enumerate(lines[1:], 2):
        fields = row.split("\t")
        if len(fields) != len(header):
            problems.append(f"{name}:{i}: {len(fields)} fields, header has {len(header)}")
        for j, f in enumerate(fields):
            col = header[j] if j < len(header) else "?"
            if QUOTE not in f:
                continue
            if f[0] != QUOTE:
                problems.append(
                    f"{name}:{i}: field {j} ({col}) carries a quote at offset "
                    f"{f.index(QUOTE)}, not at the field start")
                continue
            quoted += 1
            if len(f) < 2 or not f.endswith(QUOTE):
                problems.append(f"{name}:{i}: field {j} ({col}) opens a quoted field that does not close")
                continue
            inner = f[1:-1]
            k = 0
            bad = None
            while k < len(inner):
                if inner[k] == QUOTE:
                    if k + 1 >= len(inner) or inner[k + 1] != QUOTE:
                        bad = k
                        break
                    k += 2
                else:
                    k += 1
            if bad is not None:
                problems.append(f"{name}:{i}: field {j} ({col}) has an undoubled interior quote at offset {bad}")
    return problems, len(lines) - 1, quoted


def main():
    files = sorted(TABLES.glob("*.tsv"))
    problems: list[str] = []
    rows = 0
    quoted = 0
    for p in files:
        pr, n, q = check(p.read_text(encoding="utf-8"), p.name)
        problems.extend(pr)
        rows += n
        quoted += q
    print(f"files: {len(files)}  rows: {rows}  quoted fields: {quoted}")
    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  -", p)
        return 1
    print("problems: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
