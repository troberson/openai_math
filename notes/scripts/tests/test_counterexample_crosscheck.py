"""The self-tests for `notes/scripts/verify_counterexample_crosscheck.py`.

The checker verifies `notes/counterexample-crosscheck.md` against the shipped files: the 28-family
population, its tier split, the ledger sums, the entry/config/gap counts, the carrier-typed count and
the stub `sorry` totals are recomputed from the ledger, `overview.tex`, `lean/formalization.yaml`,
`lean/docs/` and `lean/ComparatorChallenges/`; every anchor resolves; every fenced block matches its
nearest preceding anchor at consecutive lines; every `*"…"*` quote is pinned to the anchor in its own
line; the 28-row summary table, the 12-row T3 gap table and the 9-row T2 table are checked row by
row; each entry's yaml block, statement anchor and carrier anchor are checked against the file; each
T3 block names exactly its own configs; and the page is compared with `render_reports.py`'s render of
it. Lean is read as text — `lake`, `lean` and `comparator` are never invoked, so no verdict here can
mean a proof was checked.

This file injects fourteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: a tier swapped in the summary table, a config count moved, a statement anchor shifted, a
carrier body word changed, a claim quote word changed, a yaml anchor shifted, a gap row's family
changed, a `sorry` count moved, a T2 row deleted, a T2 config taken from another family, a carrier
paraphrase, an anchor file that is not on disk, a quote moved to another family's line, and a prose
count no count phrase covers — the last is visible only to the render diff.

Every fault is built from a real row, a real anchor, a real block line, a real quote and a real count
phrase in the page as committed. Each test asserts the injected text differs from the page it started
from, and each needle is the problem string the pass that owns that form prints — measured specific,
each needle fires for its own fault and for no other.

The clean test asserts the passes are silent and pins the four population counts they report: 172
anchors, 295 block lines, 38 quotations and 0 sync problems. A page with fewer anchors, block lines or
quotations is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_counterexample_crosscheck.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("tier swapped in the summary table", "summary table row 1: ('047', 'T2', 1, 1, 0)",
     lambda t: t.replace("| 047 | T3 | 1 | 1 | 0 |", "| 047 | T2 | 1 | 1 | 0 |", 1)),
    ("config count moved", "summary table row 11: ('172', 'T3', 6, 2, 4)",
     lambda t: t.replace("| 172 | T3 | 7 | 2 | 5 |", "| 172 | T3 | 6 | 2 | 4 |", 1)),
    ("statement anchor shifted",
     "no statement anchor at lean/OAI/Algebra/AffineCancellation/Main.lean:32",
     lambda t: t.replace("`lean/OAI/Algebra/AffineCancellation/Main.lean:32`",
                         "`lean/OAI/Algebra/AffineCancellation/Main.lean:33`", 1)),
    ("carrier body word", "block line 1 != lean/OAI/Algebra/AffineCancellation/Model.lean:21",
     lambda t: t.replace("ringKrullDim A = 4", "ringKrullDim A = 5", 1)),
    ("claim quote word", "quote not on overview.tex:170",
     lambda t: t.replace("disproving affine-space cancellation", "disproving affine-space duality", 1)),
    ("yaml anchor shifted", "block line 0 != lean/formalization.yaml:1042",
     lambda t: t.replace("`lean/formalization.yaml:1041`", "`lean/formalization.yaml:1042`", 1)),
    ("gap row family", "gap table lists [('BalancedRyser', '185')",
     lambda t: t.replace("| `BalancedRyser` | 162 |", "| `BalancedRyser` | 185 |", 1)),
    ("sorry count moved", "count mismatch (stub sorries)",
     lambda t: t.replace("carrying **55** `sorry` occurrences",
                         "carrying **57** `sorry` occurrences", 1)),
    ("T2 row deleted", "T2 table families ['100', '161'",
     lambda t: t.replace("| 151 | `C1EntropyCounterexample` | `lean/docs/151.md:15` |\n", "", 1)),
    ("T2 config from another family", "T2 row 151: configs ['Naimark']",
     lambda t: t.replace("`C1EntropyCounterexample` | `lean/docs/151.md:15`",
                         "`Naimark` | `lean/docs/151.md:15`", 1)),
    ("carrier paraphrase", "block line 3 != lean/OAI/Algebra/AffineCancellation/Model.lean:23",
     lambda t: t.replace("¬ Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)",
                         "Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)", 1)),
    ("anchor file absent", "anchor file lean/OAI/Geometry/Arnold/Nope.lean does not exist",
     lambda t: t.replace("`lean/OAI/Geometry/Arnold/Main.lean:14`",
                         "`lean/OAI/Geometry/Arnold/Nope.lean:14`", 1)),
    ("quote moved to another family", "quote not on overview.tex:218",
     lambda t: t.replace("Claim 2 (`overview.tex:170`) — *\"It also disproves the Dolgachev",
                         "Claim 2 (`overview.tex:218`) — *\"It also disproves the Dolgachev", 1)),
    # Prose no count phrase reads: the formalized-manuscript denominator in the population
    # paragraph. Only the render diff can see it.
    ("prose count", "count mismatch (ledger paps_form/paps)",
     lambda t: t.replace("formalized manuscripts out of **50**.",
                         "formalized manuscripts out of **51**.", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_counterexample_crosscheck")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and the four population counts the passes report are pinned."""
    problems, n_anchor, n_block, n_quote, n_sync, v = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_block, n_quote, n_sync) == (172, 295, 38, 0), \
        f"anchors {n_anchor}, block lines {n_block}, quotations {n_quote}, sync {n_sync}"
    assert len(v["pop"]) == 28, f"population {len(v['pop'])}, not 28"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _, _, _, _, _ = mod.check(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
