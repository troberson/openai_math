"""The self-tests for `notes/scripts/verify_upstream_history.py`.

The checker verifies the `notes/development/upstream_history/` pages structurally: anchors
resolve, quotations match the anchored lines verbatim, fenced blocks match their nearest
anchor, every date-suffixed slug exists as a `preprints/` directory, and every markdown link
resolves. Historical count/table/needle validation is not re-derived against the current
release surface — the pages are historical records.

This file injects six structural faults, one per check form `check_page` uses, and asserts
each fires the pass that owns it: a quotation word changed, a paraphrase dressed as a quote,
an anchor shifted, an anchor path that is not a file, a slug renamed, and a link that does
not resolve.

Every fault is built from a real phrase, a real anchor, and a real link in the page as
committed, so a checker that only re-reads its own regexes cannot pass. Each test asserts the
injected text differs from the page it started from. The clean test asserts the passes are
silent on all pages as committed and the slug pass is not vacuous.

The checker reads no argv and the passes take page text, so nothing here writes a page: the
checker writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_upstream_history.py -q
"""

import pytest
import verify_upstream_history as chk

pytestmark = pytest.mark.mutant

# Faults in the pages' own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("quotation word altered",
     "notes/development/upstream_history/2026-10-07_3014888.md",
     "not verbatim in its anchored lines",
     lambda t: t.replace("supplies the annulus proof of the circuit estimate",
                         "supplies the annulus proof of the bound estimate")),
    ("paraphrase dressed as a quote",
     "notes/development/upstream_history/2026-10-07_3014888.md",
     "not verbatim in its anchored lines",
     lambda t: t.replace('The resulting count is therefore"*',
                         'so the count is therefore nonzero"*')),
    ("anchor shifted",
     "notes/development/upstream_history/2026-10-07_3014888.md",
     "not verbatim in its anchored lines",
     lambda t: t.replace("`history.md:38`", "`history.md:37`")),
    ("anchor path that is not a file",
     "notes/development/upstream_history/2026-10-07_3014888.md",
     "is not a file",
     lambda t: t.replace(
         "preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md:21",
         "preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-8-2026/README.md:21")),
    ("slug renamed",
     "notes/development/upstream_history/2026-10-07_3014888.md",
     ": slug '",
     lambda t: t.replace("`Taming-implies-compatibility-on-four-manifolds-October-6-2026`",
                         "`Taming-implies-compatibility-on-four-manifolds-October-5-2026`")),
    ("link that does not resolve",
     "notes/development/upstream_history/2026-10-07_3014888.md",
     "does not exist",
     lambda t: t.replace("[`history.md`](../../../history.md)",
                         "[`history.md`](../../../historyx.md)")),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_upstream_history")


@pytest.fixture(scope="module")
def p(mod):
    return mod.measure()


@pytest.fixture(scope="module")
def pages(mod):
    return {name: mod.read_text(mod.ROOT / name) for name in mod.PAGES}


def test_clean_pages(mod, p, pages):
    """The page passes and the slug count are all silent on the committed pages."""
    problems: list = []
    hits = 0
    for name in mod.PAGES:
        hits += len(mod.SLUG.findall(pages[name]))
        mod.check_page(name, pages[name], p, problems)
    assert not problems, problems[:3]
    assert hits > 0, "SLUG matched no token: the pass is vacuous, not passing"


@pytest.mark.parametrize("label,page,needle,mut", MUTANTS)
def test_injected_faults(mod, p, pages, label, page, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(pages[page])
    assert cand != pages[page], f"{label}: mutation changed nothing"
    found: list = []
    mod.check_page(page, cand, p, found)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
