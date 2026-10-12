"""The self-tests for `notes/scripts/verify_conditional.py`.

The checker verifies `notes/conditional.md` in three forms: a fenced block is matched against the
lines of the `path:line` anchor that precedes it, a prose quotation in *"…"* form is matched against
the file its nearest anchor names, and an inline `span` at `path:line` citation is matched against
that file. This file injects six faults, one per check form the page uses, and asserts each is caught
by the pass that owns it: two faults move a fenced block (a shifted anchor, an altered block line),
one drops the anchor a block depends on, one renames an anchor file, one alters a prose quotation,
and one alters an inline citation so the span is no longer in the file it cites.

Every fault is built from a real anchor, a real quotation, and a real span in the page as committed,
so a checker that only re-reads its own regexes cannot pass. Each test asserts the injected text
differs from the page it started from. The clean test asserts the three passes are silent on the page
as committed and that the measured population is the one the checker reports.

The checker reads no argv and the passes take page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_conditional.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("fenced block anchor shifted by one",
     "block line 0 != lean/OAI/ModelTheory/Categoricity/Main.lean:234",
     lambda t: t.replace("`lean/OAI/ModelTheory/Categoricity/Main.lean:233`",
                         "`lean/OAI/ModelTheory/Categoricity/Main.lean:234`", 1)),
    ("fenced block line altered",
     "block line 0 != lean/OAI/ModelTheory/Categoricity/Main.lean:233",
     lambda t: t.replace("theorem main (hCH : CH.{u}) :", "theorem main (hCH : CH) :", 1)),
    ("fenced block anchor dropped",
     "fenced block has no preceding file:line anchor",
     lambda t: t.replace("exists only as a challenge stub, "
                         "`lean/ComparatorChallenges/PartitionConsistency.lean:318`:",
                         "exists only as a challenge stub:", 1)),
    ("anchor file renamed",
     "inline anchor file lean/OAI/ModelTheory/Categoricity/Mode.lean does not exist",
     lambda t: t.replace("`lean/OAI/ModelTheory/Categoricity/Model.lean:101`",
                         "`lean/OAI/ModelTheory/Categoricity/Mode.lean:101`", 1)),
    ("prose quotation altered",
     "prose quote not found in lean/docs/244.md",
     lambda t: t.replace("and failure of the Axiom of Choice.", "and failure of Choice.", 1)),
    ("inline citation altered",
     "inline citation not found in lean/OAI/Combinatorics/KMedian/Hardness/Model.lean:30",
     lambda t: t.replace("def PNeNP : Prop := P ≠ NP", "def PNeNP : Prop := P = NP", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_conditional")


@pytest.fixture(scope="module")
def page(mod):
    return mod.PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(mod, page):
    """The three passes are silent on the page as committed, and the population is the measured one."""
    problems, unanchored, counts = mod.check(page)
    assert not problems, problems[:3]
    assert counts == (5, 14, 1, 7), counts
    assert unanchored == 15, unanchored


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, page, label, needle, mut):
    """A fault in each of the three check forms, injected in memory. The needle is the problem string
    the pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(page)
    assert cand != page, f"{label}: mutation changed nothing"
    found, _, _ = mod.check(cand)
    assert found, f"{label}: no problems reported"
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
