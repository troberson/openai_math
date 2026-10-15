#!/usr/bin/env python3
r"""Measure the needle fleet: how many needles are recorded, how many are derived, and which
recorded needles name a figure their own mutation does not write.

Report-only: writes nothing, runs nothing. It parses each `notes/scripts/tests/test_*.py` with `ast`
and reports, per file: the number of injected faults, how many needles are a literal string (recorded)
and how many are a callable (derived at run time), the numeric literals inside each needle expression,
the numeric literals in the clean test's asserted tuples, and the recorded needles whose digits are
absent from the mutation's own text.

The derived count is the phase-1 progress measure. A needle that quotes a page line or a corpus count
has to be re-measured by hand when the page moves; a needle built from the mutated page and the
checker's measured population does not. The numeric-literal count is reported as the expression text,
which includes the strings a derivation uses to locate its mutation — so the derived/literal split, not
the literal count, is the number that says whether a needle is recorded.

The last column is the rule that makes the recorded/literal judgment checkable. A recorded needle
whose digits all appear in the string constants its mutation writes names the mutation's own input —
an invented href, an invented path, an anchor line written out of range, a rewritten phrase — so it
stays a literal by rule. A recorded needle carrying a digit its mutation never writes names a measured
figure the phase-1 pass missed.

Run: python3 notes/scripts/measure_needles.py
"""
from __future__ import annotations

import ast
import pathlib
import re

TESTS = pathlib.Path("notes/scripts/tests")


def needle_slots(tree):
    """The (label, needle, mutation) triples in the file's MUTANTS list."""
    out = []
    for mod in tree.body:
        if isinstance(mod, ast.Assign) and getattr(mod.targets[0], "id", "") == "MUTANTS":
            if isinstance(mod.value, ast.Tuple):
                for el in mod.value.elts:
                    if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                        label = el.elts[0].value if isinstance(el.elts[0], ast.Constant) else "?"
                        out.append((label, el.elts[1], el.elts[2]))
    return out


def input_slots(tree):
    """The tuples in a file's INPUTS list — synthetic rule cases, not page mutations.

    A synthetic test feeds the rule a string the rule must classify, so the string is the test's
    own input by construction and the needle-input rule does not apply to it.
    """
    out = []
    for mod in tree.body:
        if isinstance(mod, ast.Assign) and getattr(mod.targets[0], "id", "") == "INPUTS":
            if isinstance(mod.value, ast.Tuple):
                for el in mod.value.elts:
                    if isinstance(el, ast.Tuple):
                        out.append(el)
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


def mutation_text(node):
    """The string constants a mutation callable writes into the page."""
    return " ".join(s.value for s in ast.walk(node)
                    if isinstance(s, ast.Constant) and isinstance(s.value, str))


# A needle digit that names a row, a layer, or a family/sequence key is a locator the pass prints
# from the row it flags, not a figure the mutation writes.
LOCATOR = re.compile(r"layer[ -]\d+|\b\d{3}/\d+\b")


def not_inputs(slots):
    """Recorded needles with a digit their own mutation's text does not contain."""
    out = []
    for label, needle, mut in slots:
        if not isinstance(needle, ast.Constant) or not isinstance(needle.value, str):
            continue
        digits = re.findall(r"\d+", LOCATOR.sub("", needle.value))
        if not digits:
            continue
        text = mutation_text(mut)
        missing = [d for d in digits if d not in text]
        if missing:
            out.append((label, needle.value, missing))
    return out


def main():
    files = sorted(TESTS.glob("test_*.py"))
    rec = der = nums = pins = inp = 0
    rec_num = rec_str = 0
    missed = 0
    print(f"== test files {len(files)}")
    for f in files:
        tree = ast.parse(f.read_text(encoding="utf-8"))
        slots = needle_slots(tree)
        r = sum(1 for _, n, _m in slots if isinstance(n, ast.Constant))
        d = sum(1 for _, n, _m in slots if not isinstance(n, ast.Constant))
        # A recorded needle that carries a digit is a measured figure re-measured by hand; one that
        # carries no digit is a structural message and stays a string.
        rn = sum(1 for _, n, _m in slots
                 if isinstance(n, ast.Constant) and isinstance(n.value, str) and re.search(r"\d", n.value))
        rs = r - rn
        n = sum(len(re.findall(r"\d+", ast.unparse(_x))) for _, _x, _m in slots)
        p = clean_pins(tree)
        syn = len(input_slots(tree))
        bad = not_inputs(slots)
        rec += r
        der += d
        nums += n
        pins += len(p)
        inp += syn
        rec_num += rn
        rec_str += rs
        missed += len(bad)
        print(f"{f.name:38} faults {len(slots):3}  recorded {r:3}  numeric {rn:3}  "
              f"structural {rs:3}  derived {d:3}  needle digits {n:3}  clean pins {len(p):3}  "
              f"synthetic {syn:3}  not inputs {len(bad):3}")
        for label, value, miss in bad:
            print(f"    {label}: {value}  missing {','.join(miss)}")
    print(f"TOTAL faults {rec + der}  recorded {rec} (numeric {rec_num}, structural {rec_str})  "
          f"derived {der}  needle digits {nums}  clean pins {pins}  synthetic {inp}  "
          f"not inputs {missed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
