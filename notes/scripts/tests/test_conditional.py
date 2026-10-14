r"""The self-tests for `notes/scripts/verify_conditional.py`.

The checker verifies `notes/reports/conditional.md` in three forms: a fenced block is matched against
the lines of the `path:line` anchor that precedes it, a prose quotation in *"…"* form is matched against
the file its nearest anchor names, and an inline `span` at `path:line` citation is matched against that
file. This file injects six faults, one per check form the page uses, and asserts each is caught by the
pass that owns it: two faults move a fenced block (a shifted anchor, an altered block line), one drops
the anchor a block depends on, one renames an anchor file, one alters a prose quotation, and one alters
an inline citation so the span is no longer in the file it cites.

Every fault is built from a real anchor, a real quotation, and a real span in the page as committed, so
a checker that only re-reads its own regexes cannot pass. Each test asserts the injected text differs
from the page it started from.

**The needles that name an anchor are derived at run time, not recorded.** Each needle asks the
checker's own `nearest_anchor` rule which anchor the pass attributes the mutated block, quote, or
citation to, and builds the problem string from that. A needle that carried the anchor as a literal
breaks the day the page's anchors move; the derivation follows the anchor. The two needles that stay
literal are the mutation's own inputs — the dropped anchor's message and the renamed file.

The clean test asserts the three passes are silent on the page as committed and that the measured
population is the one the checker reports.

The checker reads no argv and the passes take page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_conditional.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# The file the rename fault writes, and the block line the anchor-shift fault moves past.
RENAMED = "lean/OAI/ModelTheory/Categoricity/Mode.lean"


def block_anchor(mod, c, sub):
    """The anchor the fenced-block pass attributes the block containing `sub` to."""
    lines = c.split("\n")
    for start, body in mod.anchors.fenced_blocks(lines):
        if any(sub in l for l in body):
            return mod.anchors.nearest_anchor(lines, start, mod.ANCHOR)
    raise AssertionError(f"no fenced block contains {sub!r}")


def block_after_anchor(mod, c, sub):
    """The anchor the pass attributes the first fenced block following the line carrying `sub` to —
    the shape the anchor-shift fault makes: the mutation moves the anchor, the block is unchanged."""
    lines = c.split("\n")
    idx = next(i for i, l in enumerate(lines) if sub in l)
    for start, _body in mod.anchors.fenced_blocks(lines):
        if start > idx:
            return mod.anchors.nearest_anchor(lines, start, mod.ANCHOR)
    raise AssertionError(f"no fenced block follows the line carrying {sub!r}")


def prose_anchor(mod, c, sub):
    """The anchor the prose pass attributes the quotation containing `sub` to."""
    upto = c[: c.index(sub)].split("\n")
    return mod.anchors.nearest_anchor(upto, len(upto), mod.ANCHOR)


def inline_anchor(mod, c, sub):
    """The anchor the inline pass pairs with the citation whose span contains `sub`."""
    for m in mod.INLINE.finditer(c):
        span = m.group(1) or m.group(4)
        if sub in span:
            return (m.group(2) or m.group(5)), int(m.group(3) or m.group(6))
    raise AssertionError(f"no inline citation carries {sub!r}")


def block_needle(mod, c, sub, after):
    """The block pass's problem string for a mutated block: the anchor the pass attributes it to,
    read from the mutated page."""
    a = block_after_anchor(mod, c, sub) if after else block_anchor(mod, c, sub)
    return f"block line 0 != {a[0]}:{a[1]}"


def prose_needle(mod, c, sub):
    """The prose pass's problem string for a mutated quotation."""
    return f"prose quote not found in {prose_anchor(mod, c, sub)[0]}"


def inline_needle(mod, c, sub):
    """The inline pass's problem string for a mutated citation."""
    rel, at = inline_anchor(mod, c, sub)
    return f"inline citation not found in {rel}:{at}"


# (label, needle, mutation). A needle is a function of the mutated page and the loaded checker.
MUTANTS = [
    ("fenced block anchor shifted by one",
     lambda c, mod: block_needle(mod, c, "Main.lean:234", True),
     lambda t: t.replace("`lean/OAI/ModelTheory/Categoricity/Main.lean:233`",
                         "`lean/OAI/ModelTheory/Categoricity/Main.lean:234`", 1)),
    ("fenced block line altered",
     lambda c, mod: block_needle(mod, c, "theorem main (hCH : CH) :", False),
     lambda t: t.replace("theorem main (hCH : CH.{u}) :", "theorem main (hCH : CH) :", 1)),
    ("fenced block anchor dropped",
     "fenced block has no preceding file:line anchor",
     lambda t: t.replace("exists only as a challenge stub, "
                         "`lean/ComparatorChallenges/PartitionConsistency.lean:318`:",
                         "exists only as a challenge stub:", 1)),
    ("anchor file renamed",
     lambda c, mod: f"inline anchor file {RENAMED} does not exist",
     lambda t: t.replace("`lean/OAI/ModelTheory/Categoricity/Model.lean:101`",
                         f"`{RENAMED}:101`", 1)),
    ("prose quotation altered",
     lambda c, mod: prose_needle(mod, c, "and failure of Choice."),
     lambda t: t.replace("and failure of the Axiom of Choice.", "and failure of Choice.", 1)),
    ("inline citation altered",
     lambda c, mod: inline_needle(mod, c, "def PNeNP : Prop := P = NP"),
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
    want = needle(cand, mod) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"
