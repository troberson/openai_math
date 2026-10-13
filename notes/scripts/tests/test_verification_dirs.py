"""The self-tests for `notes/scripts/verify_verification_dirs.py`.

The checker verifies `notes/reports/verification-dirs.md` against the 30 bundles it describes. Anchors:
every `path:line` and `path:a-b` resolves against the file, a prefixed path resolves against the
repo root, and a span fits inside the file. Quotations: each `*"…"*` in the family-348 section is
matched against the lines its anchor names, each row quote in the entry-point section is matched at
the anchored line exactly, and each `says "…"` phrase is matched against the README its slug names.
Counts: every bold count is re-derived from the bundles, the ledger, and the entry-point recomputation.
Ledger claims: the `covmd`/`inputs`/`verification` values the page asserts are re-checked from the
TSV. Entry-point counts: the class counts, the named/unnamed split, the rule-4 firing count, the
ledger join, and the two `rows.txt` files' size and byte identity. Table: one row per bundle in slug
order, with the family that slug belongs to. Coverage: every artifact a bundle's `COVERAGE.md` names
is on disk. Sync: the page bytes against `render_reports.py`'s render of it.

This file injects nineteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: an anchor line shifted, an anchor file renamed, a block line altered, a prose quote
altered, the passed-record count, the negative-test count, a ledger value, an abbreviated anchor, the
coverage-file artifact presence, an entry class count, the unnamed bundle count, an entry-section
quote, an entry-section anchor, the `rows.txt` size, a table row's family, the rule-4 firing count,
the entry-section ledger sum, a deleted table row, and a script line count inside an entry-point cell
that no count phrase reads — the last is visible only to the render diff.

Every fault is built from a real anchor, a real block line, a real quotation, a real count phrase, a
real ledger value, a real table row and a real entry cell in the page as committed. Each test asserts
the injected text differs from the page it started from, and each needle is the problem string the
pass that owns that form prints — measured specific, each needle fires for its own fault and for no
other. The generic render-diff line fires for every fault, so no needle is that line; the prose fault
is keyed to the page line the render diff names.

The clean test asserts the passes are silent and pins the counts they report: 42 anchors, 3 block
lines, 2 prose quotes, 27 row quotes, 1 says-quote, 16 count phrases, 5 ledger phrases, 9 entry
phrases, 30 table rows, 0 sync problems; the bundle population at 4 named `COVERAGE.md` files all
present, 9 shared, 7 identical, 2 differing, 8 entries, 0 mismatches, 53 identities, 21 interval
rows, 15 reported, 6 supplementary, 12 triangle rows, 9 determinant floors, 24 exact, 41
subintervals, 504 lines, 6 check functions, 9 printed keys, 13 `require` calls, 151 passed-record
occurrences, 11 checks with 8 negative and 7 ending `rejected`; and the entry recomputation at 30
bundles over 22 families, 28 named by a README section, 27 by a `## Verification` heading and 1 by
the other heading, 6 with no entry point, 0 rule-4 firings, 2 declaring READMEs, and the two
`rows.txt` files at 20 lines and 1,436 bytes, byte-identical. A page with fewer anchors, quotes,
phrases or rows is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` and `entry_measure()` are under
`functools.cache`, so the twenty `check()` calls the row makes pay the bundle walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_verification_dirs.py -q
"""
import re

import pytest

pytestmark = pytest.mark.mutant

POS = "preprints/Positively-curved-Einstein-four-manifolds-September-23-2026"
ZERO = "preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026"
HEIS = "preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026"

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("anchor line shifted", f"block line 0 != {POS}/verification/verify.py:495",
     lambda t: t.replace(f"`{POS}/verification/verify.py:496`",
                         f"`{POS}/verification/verify.py:495`", 1)),
    ("anchor file renamed", "06-certificates.tex does not exist",
     lambda t: t.replace("September-23-2026/build/sections/07-certificates.tex:14",
                         "September-23-2026/build/sections/06-certificates.tex:14", 1)),
    ("block line altered", f"block line 1 != {POS}/verification/verify.py:497",
     lambda t: t.replace('"Recomputed exact results differ from bundled results.json")',
                         '"Recomputed results differ from bundled results.json")', 1)),
    ("prose quote altered", f"quote not found in {ZERO}/verification/check_scalar_certificates.py",
     lambda t: t.replace("calculus, Jacobi comparison, and Sobolev arguments",
                         "calculus, Jacobi comparison, and Sobolev estimates", 1)),
    ("count altered", "count mismatch (passed-record count)",
     lambda t: t.replace("**151** such occurrences", "**150** such occurrences", 1)),
    ("negative-test count altered", "count mismatch (portability check counts)",
     lambda t: t.replace("ships **11** checks, **8** of them negative",
                         "ships **11** checks, **7** of them negative", 1)),
    ("ledger value altered", "ledger claim mismatch (family 348 verification value)",
     lambda t: t.replace("`verification` value of 2 for family 348",
                         "`verification` value of 1 for family 348", 1)),
    ("abbreviated anchor", "anchor file .../verification/verify.py does not exist",
     lambda t: t.replace(f"`{POS}/verification/verify.py:477`", "`.../verification/verify.py:477`", 1)),
    ("coverage artifact presence overstated", "count mismatch (coverage-file artifact presence)",
     lambda t: t.replace("all four are present in both directories",
                         "all five are present in both directories", 1)),
    ("entry class count altered", "entry-point count mismatch (entry-point class counts)",
     lambda t: t.replace("**12** top-level `README.md`", "**13** top-level `README.md`", 1)),
    ("unnamed bundle count altered", "entry-point count mismatch (unnamed bundle count)",
     lambda t: t.replace("**2** bundles ship a `verification/` tree",
                         "**3** bundles ship a `verification/` tree", 1)),
    ("entry-section quote altered", f"quote not found in {HEIS}/verification/README.md",
     lambda t: t.replace("*\"They verify finite scalar, thermal, and trial calculations, "
                         "not the analytic proof.\"*",
                         "*\"They verify finite scalar, thermal, and trial calculations, "
                         "not the analytic argument.\"*", 1)),
    ("entry-section anchor shifted", f"row quote anchored at {HEIS}/verification/README.md:53",
     lambda t: t.replace("chain-September-24-2026/verification/README.md:54`",
                         "chain-September-24-2026/verification/README.md:53`", 1)),
    ("rows.txt size altered", "entry-point count mismatch (rows.txt size and identity)",
     lambda t: t.replace("20 lines and 1436 bytes", "20 lines and 1437 bytes", 1)),
    ("table row family altered", "entry-point table family order: 18: 372 != 371",
     lambda t: t.replace("| 371 | `Stable-Self-Similar", "| 372 | `Stable-Self-Similar", 1)),
    ("rule 4 firing count altered", "entry-point count mismatch (rule 4 firing count)",
     lambda t: t.replace("Rule 4 fires for **0** bundles", "Rule 4 fires for **1** bundles", 1)),
    ("entry-section ledger sum altered", "entry-point count mismatch (entry-section ledger join)",
     lambda t: t.replace("sums to 30 dirs over 22 families", "sums to 31 dirs over 22 families", 1)),
    ("table row deleted", "entry-point table has 29 rows, the bundle count is 30",
     lambda t: re.sub(r"^\| 371 \| .*$\n", "", t, count=1, flags=re.MULTILINE)),
    # Prose no count phrase reads: the script's line count inside the family-067 entry-point cell.
    # The table check reads only the family column, so only the render diff can see it, and the
    # render-diff line truncates the cell, so the needle is the page line the diff names.
    ("entry cell line count altered", "page line 114",
     lambda t: t.replace("a 167-line script", "a 168-line script", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_verification_dirs")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, counters = mod.check(text, text)
    assert not problems, problems[:3]
    assert counters == (42, 3, 2, 27, 1, 16, 5, 9, 30, 0), f"counters {counters}"
    p = mod.population()
    assert (p["cov_named"], p["cov_present"], p["shared"], p["identical"], p["differ"],
            p["entries"], p["mismatches"]) == (4, 4, 9, 7, 2, 8, 0), f"cov {p['cov_named']}"
    assert (p["identities"], p["interval_rows"], p["reported"], p["supplementary"],
            p["triangle_rows"], p["det_floor"], p["exact"], p["subintervals"],
            p["lines"]) == (53, 21, 15, 6, 12, 9, 24, 41, 504), f"identities {p['identities']}"
    assert (p["checkfns"], p["printed_keys"], p["require"], p["passed"],
            p["checks"], p["negative"], p["ends_rejected"]) == (6, 9, 13, 151, 11, 8, 7), \
        f"passed {p['passed']}"
    e = mod.entry_measure()
    assert (e["dirs"], e["fams"], e["named"], e["ver"], e["run"], e["no_entry"],
            e["rule4"], e["declaring"]) == (30, 22, 28, 27, 1, 6, 0, 2), \
        f"entry dirs {e['dirs']}, named {e['named']}, no_entry {e['no_entry']}"
    assert e["classes"] == {"none": 6, "top-level README.md": 12, "top-level script by name": 5,
                            "subdirectory README.md": 6, "subdirectory README.txt": 1}, e["classes"]
    assert (e["rows_lines"], e["rows_bytes"], e["rows_identical"]) == (20, 1436, True), \
        f"rows.txt {e['rows_lines']} lines"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _ = mod.check(cand, cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
