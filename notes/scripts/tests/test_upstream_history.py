"""The self-tests for `notes/scripts/verify_upstream_history.py`.

The checker verifies the three `notes/development/upstream_history/` pages against git, the release files, and
disk: anchors resolve, quotations match the anchored lines verbatim, fenced blocks match their
nearest anchor, every date-suffixed slug exists as a `preprints/` directory, every markdown link
resolves, the per-anchor needles carry the content they claim, every count phrase is re-derived from
git + disk, and both tables are checked row by row. This file injects fourteen faults, one per form
the page uses, and asserts each fires the pass that owns it: a count phrase moved, a table row
deleted, a quotation word changed, a quotation cell whose closing quote is removed, a paraphrase
dressed as a quote, an anchor shifted, an anchor
path that is not a file, a slug renamed, a tier list truncated, a config name altered, an entry count
moved, a directory count moved, a quotation inserted with no anchor in its paragraph, and a link that does not resolve.

The slug needle is the SLUG pass only — the table pass reports the same fact as "table: '…' is not a
preprints/ directory" — so the needle here is `": slug '"`, which the table pass cannot print.

Every fault is built from a real phrase, a real row, a real anchor, and a real link in the page as
committed, so a checker that only re-reads its own regexes cannot pass. Each test asserts the injected
text differs from the page it started from. The clean test asserts the passes are silent on all three
pages as committed, the needles are silent, and the slug pass is not vacuous.

The checker reads no argv and the passes take page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_upstream_history.py -q
"""
import re

import pytest
import verify_upstream_history as chk
from catlib.anchors import range_facts

pytestmark = pytest.mark.mutant

PAGE_301 = "notes/development/upstream_history/2026-10-07_3014888.md"
PAGE_FD = "notes/development/upstream_history/2026-10-07_fd4aeeb.md"

# Faults in the pages' own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("count phrase moved", PAGE_301, "phrase absent from page",
     lambda t: bump(t, r"\*\*(\d+) files added, \d+ deleted, \d+ modified\*\*", -1)),
    ("table row deleted", PAGE_301, "fixes rows",
     lambda t: "\n".join(l for l in t.split("\n")
                         if not l.startswith("| 376 | `Incompressible-Box-Transport"))),
    ("quotation word altered", PAGE_301, "not verbatim in its anchored lines",
     lambda t: t.replace("supplies the annulus proof of the circuit estimate",
                         "supplies the annulus proof of the bound estimate")),
    ("quotation cell emptied", PAGE_301, "quotation cell carries no",
     lambda t: t.replace("including the projected-force and pressure bounds\"*",
                         "including the projected-force and pressure bounds*")),
    ("paraphrase dressed as a quote", PAGE_301, "not verbatim in its anchored lines",
     lambda t: t.replace('The resulting count is therefore"*',
                         'so the count is therefore nonzero"*')),
    ("anchor shifted", PAGE_301, "not verbatim in its anchored lines",
     lambda t: t.replace("`history.md:19`", "`history.md:18`")),
    ("anchor path that is not a file", PAGE_301, "is not a file",
     lambda t: t.replace("preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/README.md:21",
                         "preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-8-2026/README.md:21")),
    ("slug renamed", PAGE_301, ": slug '",
     lambda t: t.replace("`Taming-implies-compatibility-on-four-manifolds-October-6-2026`",
                         "`Taming-implies-compatibility-on-four-manifolds-October-5-2026`")),
    ("tier list truncated", PAGE_301, "phrase absent from page",
     lambda t: drop_tier(t, r"for ((?:\d{3} )+\d{3})")),
    ("config name altered", PAGE_301, "new configs",
     lambda t: t.replace("`FourierLLogL`", "`FourierLLogL2`")),
    ("entry count moved", PAGE_301, "main_results entries",
     lambda t: entry_bump(t, chk)),
    ("directory count moved", PAGE_301, "phrase absent from page",
     lambda t: bump(t, r"\*\*(\d+)\*\* directories", -1)),
    ("quotation with no anchor", PAGE_FD, "no anchor in its paragraph",
     lambda t: t.replace("Nothing. `git diff",
                         'Nothing. *"a quotation with no anchor at all"* `git diff')),
    ("link that does not resolve", PAGE_301, "does not exist",
     lambda t: t.replace("[`history.md`](../../../history.md)", "[`history.md`](../../../historyx.md)")),
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
    """The three page passes, the needle pass, and the slug count are all silent on the committed pages."""
    problems: list = []
    hits = 0
    for name in mod.PAGES:
        hits += len(mod.SLUG.findall(pages[name]))
        mod.check_page(name, pages[name], p, problems)
        mod.check_counts(name, pages[name], p, problems)
        mod.check_tables(name, pages[name], p, problems)
    mod.check_needles(p, problems)
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
    mod.check_counts(page, cand, p, found)
    mod.check_tables(page, cand, p, found)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


def entry_bump(t, chk):
    """Bump the first config row whose count the measured population confirms and whose count is above
    1, so the row the table pass reads disagrees with the release."""
    p = chk.measure()
    for m in re.finditer(r"(?m)^\|\s*\d{3}\s*\|\s*`\w+`\s*\|\s*(\d+)\s*\|", t):
        n = int(m.group(1))
        if 1 < n == p["main_post"].get(m.group(0).split("`")[1]):
            return t[:m.start()] + m.group(0).replace(m.group(1), str(n - 1), 1) + t[m.end():]
    raise AssertionError("no confirmed config row with a count above 1")


def bump(t, pat, delta):
    """Change the page's own count at `pat` by `delta`. The mutation's input is the page as it stands,
    so a measured count that moves does not need a hand-edit here."""
    m = re.search(pat, t)
    assert m, f"{pat!r} not in the page"
    raw = m.group(1)
    new = f"{int(raw.replace(',', '')) + delta:,}" if "," in raw else str(int(raw) + delta)
    span = m.group(0)
    return t[:m.start()] + span.replace(raw, new, 1) + t[m.end():]


def drop_tier(t, pat):
    """Drop one family from the page's own tier list, keeping the phrase form."""
    m = re.search(pat, t)
    assert m, "no tier list in the page"
    fams = m.group(1).split()
    new = " ".join(fams[:-2] + fams[-1:])
    return t.replace(m.group(0), f"for {new}", 1)


def pad_cells(t):
    """Pad every table cell with two spaces."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_dropped(mod, p, pages):
    """The opposite direction from the padding-tolerant checkers: `check_tables` (`:468`, `:494`)
    matches rows with byte-exact single-space regexes, so padding must drop every row, not be
    tolerated. The tree is not formatted, so a padded cell can only arrive by hand; the test asserts
    the checker's byte-form contract."""
    cand = pad_cells(pages[mod.PAGE_301])
    assert cand != pages[mod.PAGE_301], "padding changed nothing"
    found: list = []
    mod.check_tables(mod.PAGE_301, cand, p, found)
    assert any("0 fixes rows" in x for x in found), \
        f"padding did not drop the fixes rows: {found[:2]}"
    assert any("configs in the table []" in x for x in found), \
        f"padding did not drop the config rows: {found[:2]}"


def start_only(a, n):
    """The narrowed rule: check only the start position, which is what a single-line anchor read does."""
    return [] if 0 < a <= n else [a]


def test_range_facts_flags_a_range_past_the_end():
    """The anchor pass checks **both** ends of a `path:a-b` anchor through `catlib.anchors.range_facts`,
    so a range whose end runs past the file is a problem; a rule that checks only the start position
    misses it. The line count is synthetic — no file is read."""
    n = 1784
    out, blank, rev = range_facts(684, 1900, n)
    assert out == [1900], f"the shipped rule read {out}, so the end position is not checked"
    assert not blank and not rev, f"the shipped rule reported {blank} / {rev}"
    assert not start_only(684, n), \
        "the start-only rule flags the past-end range, so it is not the rule that misses it"
