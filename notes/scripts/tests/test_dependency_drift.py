"""The extracted self-tests for `notes/scripts/verify_dependency_drift.py` and the two pages.

The checker's passes are: the anchor pass (every `path:line` and `path:a-b` resolves, a bare `:N`
against the nearest explicit path); the quotation pass (every blockquote and every checked code span
verbatim against the source it cites); the table pass (the 23-row patch table equal to the TSV row by
row in descending order); the name-list pass (each named library list equal to the measured set); the
count pass (every count phrase re-measured from the TSV, `lean/lakefile.lean`, `lean/formalization.yaml`
and the patch files); and the render diff against `render_reports.py`.

Each fault below mutates the page text in memory, so no page is written. `verify_dependency_drift.py`'s
`measure()` is under `functools.cache` (`:185`): the checker writes nothing and the tests mutate page
text, so a second call in the same process cannot see a different corpus, and the eleven `check()` calls
this file makes pay the TSV, lakefile, yaml and patch-file walk once.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_dependency_drift.py -q`
"""

import pathlib

import pytest

PAGE = pathlib.Path("notes/dependency-drift.md")

# (label, needle, mutation). A needle must fire for its own fault and for no other, and must not
# fire on the clean page.
MUTANTS = [
    ("blockquote paraphrased as a quote",
     "page:56: blockquote != lean/lakefile.lean:291",
     lambda p: p.replace("compatibility patch was lost during dependency resolution.",
                         "compatibility patch was lost by dependency resolution.", 1)),
    ("anchor out of range",
     "anchor lean/lakefile.lean:486 out of range (335 lines)",
     lambda p: p.replace("`lean/lakefile.lean:10`–`:86`", "`lean/lakefile.lean:10`–`:486`", 1)),
    ("table row count shifted",
     "table PrimeNumberTheoremAnd: patch lines 39905 != TSV 39904",
     lambda p: p.replace("| PrimeNumberTheoremAnd | 244 | 39,904 |",
                         "| PrimeNumberTheoremAnd | 244 | 39,905 |", 1)),
    ("name dropped from the zero-import list",
     "name list zero-import list != computed: missing ['orbicurve-cores'] extra []",
     lambda p: p.replace("`oka`, `orbicurve-cores`,", "`oka`,", 1)),
    ("patch-line total shifted",
     "count missing from page: patch lines -> '160,187'",
     lambda p: p.replace("160,187", "160,186")),
    ("phase count shifted",
     "count missing from page: pre-resolution libraries -> '**11**'",
     lambda p: p.replace("| **11** | **6,658** |", "| **10** | **6,658** |", 1)),
    ("ordering-violation count shifted",
     "count missing from page: yaml ordering violations -> '5 entries violate'",
     lambda p: p.replace("and 5 entries violate it", "and 6 entries violate it", 1)),
    ("code span paraphrased",
     "page:66: code span not found in source: 's!\".{label}-bootstrap-{pid}-{stamp}\"'",
     lambda p: p.replace("`s!\".{plan.label}-bootstrap-{pid}-{stamp}\"`",
                         "`s!\".{label}-bootstrap-{pid}-{stamp}\"`", 1)),
    ("table row dropped",
     "patch-size table omits orbicurve-cores",
     lambda p: p.replace("| orbicurve-cores | **0** | 695 |\n", "", 1)),
    # Prose no count phrase reads: the deps-record row count in the opening sources sentence.
    # Only the render diff can see it, so the needle is the page line the render diff names.
    ("prose row count outside the phrase list",
     "page line 3: page 'Measured 2026-10-07 from three sources only",
     lambda p: p.replace("`notes/tables/formalization-deps.tsv` (31 rows, 8 fields)",
                         "`notes/tables/formalization-deps.tsv` (32 rows, 8 fields)", 1)),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(load, text):
    v = load("verify_dependency_drift")
    problems, (n_anchor, n_quote, n_span, n_table, n_sync) = v.check(text)
    assert problems == []
    assert (n_anchor, n_quote, n_span, n_table, n_sync) == (52, 7, 9, 23, 0)
    m = v.measure()
    assert (len(m["declared"]), len(m["patched"]), m["total_lines"], m["total_hunks"],
            m["tc_patches"], len(m["froms"])) == (30, 23, 160187, 734, 22, 8)
    assert (len(m["pre"]), len(m["post"]), len(m["zero"]), len(m["zero_nopatch"]),
            len(m["violations"])) == (11, 12, 19, 5, 5)
    assert (int(m["median_import"]), int(m["median_zero"])) == (2575, 408)
    assert set(m["pre"]).isdisjoint(m["post"])
    assert set(m["pre"]) | set(m["post"]) == set(m["patched"])
    assert set(m["lana"]) == set(m["pre"])


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_dependency_drift")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs = v.check(cand)[0]
    assert any(needle in p for p in probs), f"{label}: needle did not fire\n{probs}"
