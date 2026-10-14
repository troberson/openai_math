#!/usr/bin/env python3
r"""Measure the needle fleet: how many needles are recorded and how many are derived.

Report-only: writes nothing, runs nothing. It parses each `notes/scripts/tests/test_*.py` with `ast`
and reports, per file: the number of injected faults, how many needles are a literal string (recorded)
and how many are a callable (derived at run time), the numeric literals inside each needle expression,
and the numeric literals in the clean test's asserted tuples.

The derived count is the phase-1 progress measure. A needle that quotes a page line or a corpus count
has to be re-measured by hand when the page moves; a needle built from the mutated page and the
checker's measured population does not. The numeric-literal count is reported as the expression text,
which includes the strings a derivation uses to locate its mutation — so the derived/literal split, not
the literal count, is the number that says whether a needle is recorded.

Run: python3 notes/scripts/measure_needles.py
"""
from __future__ import annotations

import ast
import pathlib
import re

TESTS = pathlib.Path("notes/scripts/tests")


def needle_slots(tree):
    """The (label, needle) pairs in the file's MUTANTS list."""
    out = []
    for mod in tree.body:
        if isinstance(mod, ast.Assign) and getattr(mod.targets[0], "id", "") == "MUTANTS":
            for el in mod.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                    label = el.elts[0].value if isinstance(el.elts[0], ast.Constant) else "?"
                    out.append((label, el.elts[1]))
    return out


def clean_pins(tree):
    """The numeric literals in the clean test's asserted tuples."""
    nums = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or not node.name.startswith("test_clean"):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Tuple):
                nums += re.findall(r"\d+", ast.unparse(sub))
    return nums


def main():
    files = sorted(TESTS.glob("test_*.py"))
    rec = der = nums = pins = 0
    rec_num = rec_str = 0
    print(f"== test files {len(files)}")
    for f in files:
        tree = ast.parse(f.read_text(encoding="utf-8"))
        slots = needle_slots(tree)
        r = sum(1 for _, n in slots if isinstance(n, ast.Constant))
        d = sum(1 for _, n in slots if not isinstance(n, ast.Constant))
        # A recorded needle that carries a digit is a measured figure re-measured by hand; one that
        # carries no digit is a structural message and stays a string.
        rn = sum(1 for _, n in slots if isinstance(n, ast.Constant) and re.search(r"\d", n.value))
        rs = r - rn
        n = sum(len(re.findall(r"\d+", ast.unparse(x))) for _, x in slots)
        p = clean_pins(tree)
        rec += r
        der += d
        nums += n
        pins += len(p)
        rec_num += rn
        rec_str += rs
        print(f"{f.name:38} faults {len(slots):3}  recorded {r:3}  numeric {rn:3}  "
              f"structural {rs:3}  derived {d:3}  needle digits {n:3}  clean pins {len(p):3}")
    print(f"TOTAL faults {rec + der}  recorded {rec} (numeric {rec_num}, structural {rec_str})  "
          f"derived {der}  needle digits {nums}  clean pins {pins}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
