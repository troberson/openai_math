"""The self-tests for `notes/scripts/verify_named_conjectures.py`.

Each test corrupts the page in memory (never on disk) in one of the twelve ways the checker used to
inject, and asserts the pass that owns that corruption reports a problem: the quotation pass (an
inline quotation, a quotation wrapped across lines, an invented quotation), the anchor pass (a start
line shifted, a path absent from disk), the Measurements pass (a derived count), the entry-set pass
(an entry deleted, an entry for a family outside the population, a population entry demoted to the
promoted level), the verdict pass (a verdict word), and the citation pass (a citation truncated
before its `\\end`, a citation whose path is not on disk). Each test asserts the mutated lines differ
from the page they started from: a mutation that finds no target is a failed test, not a pass.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_named_conjectures.py -q
"""
import pytest

from catlib.layout import reorder

pytestmark = pytest.mark.mutant


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_named_conjectures")


@pytest.fixture(scope="module")
def base(mod):
    return mod.read_text(mod.PAGE).split("\n")


@pytest.fixture(scope="module")
def rows(mod):
    return reorder(mod.ledger_rows())


@pytest.fixture(scope="module")
def expected(mod, rows):
    return mod.measure(rows)[0]


@pytest.fixture(scope="module")
def pop(mod, rows):
    return mod.measure(rows)[1]


def first_heading(mod, lines):
    """The first population entry heading the page carries."""
    for i, l in enumerate(lines):
        if mod.HEADING.match(l):
            return i, l
    raise AssertionError("the page carries no population entry")


def outside_fam(rows, pop):
    """A ledger family the population excludes — the entry the page must not carry."""
    return next(r["fam"] for r in rows if r["fam"] not in pop)


def problems(mod, lines, expected, pop, rows):
    """The five passes, run on page lines, returning the problems they report."""
    out: list = []
    anchors, verdicts = mod.check_quotes(lines, out)
    cites = mod.check_citations(lines, out)
    mod.check_entry_set(lines, pop, rows, out)
    mod.check_measurements(lines, expected, anchors, verdicts, cites, out)
    mod.check_formalization_claim(lines, rows, out)
    return out


def check(mod, lines, base, expected, pop, rows, needle):
    """Asserts the mutation landed and the checker reports the needle for it."""
    assert lines != base, "the mutation target is gone from the page — nothing was injected"
    hits = [p for p in problems(mod, lines, expected, pop, rows) if needle in p]
    assert hits, f"the pass that owns this corruption did not report it ({needle})"
    return hits


def test_clean_page(mod, base, expected, pop, rows):
    assert not problems(mod, base, expected, pop, rows), "the real page must be silent"


def test_inline_quotation_corrupted(mod, base, expected, pop, rows):
    qb = mod.quote_blocks(base)
    lines = list(base)
    a = qb[0][1]
    lines[a] = lines[a].replace("\\begin{theorem", "\\begin{theorm", 1)
    check(mod, lines, base, expected, pop, rows, "quotation does not match")


def test_wrapped_quotation_corrupted(mod, base, expected, pop, rows):
    qb = mod.quote_blocks(base)
    lines = list(base)
    for _, a, b in qb:
        if b - a < 2:
            continue
        mid = (a + b) // 2
        lines[mid] = lines[mid].replace("the", "txe", 1)
        if lines[mid] != base[mid]:
            break
    check(mod, lines, base, expected, pop, rows, "quotation does not match")


def test_invented_quotation(mod, base, expected, pop, rows):
    qb = mod.quote_blocks(base)
    lines = list(base)
    lines[qb[0][1]] = '  "This sentence is not in the shipped manuscript."'
    check(mod, lines, base, expected, pop, rows, "quotation does not match")


def test_anchor_start_line_shifted(mod, base, expected, pop, rows):
    lines = list(base)
    for i, l in enumerate(lines):
        m = mod.ANCHOR.search(l)
        if m:
            lines[i] = (l[:m.start()] + "[`%s:%d-%d`]" % (m.group(1), int(m.group(2)) + 1,
                                                          int(m.group(3))) + l[m.end():])
            break
    check(mod, lines, base, expected, pop, rows, "does not open a statement environment")


def test_anchor_path_absent(mod, base, expected, pop, rows):
    lines = list(base)
    for i, l in enumerate(lines):
        m = mod.ANCHOR.search(l)
        if m:
            lines[i] = (l[:m.start()] + "[`preprints/No-Such-Manuscript/build/main.tex:%s-%s`]"
                        % (m.group(2), m.group(3)) + l[m.end():])
            break
    check(mod, lines, base, expected, pop, rows, "anchor path not on disk")


def test_measurements_count_corrupted(mod, base, expected, pop, rows):
    lines = list(base)
    for i, l in enumerate(lines):
        if l.startswith("- `pop_families`"):
            # The mutation's input is the page's own recorded count, so a count that moves does not
            # need a hand-edit here.
            lines[i] = l[:l.rfind(" ") + 1] + str(int(l.rsplit(" ", 1)[1]) + 1)
            break
    check(mod, lines, base, expected, pop, rows, "measurements:")


def test_population_entry_deleted(mod, base, expected, pop, rows):
    lines = list(base)
    i, _l = first_heading(mod, lines)
    j = i + 1
    while j < len(lines) and not lines[j].startswith("## "):
        j += 1
    del lines[i:j]
    check(mod, lines, base, expected, pop, rows, "population families with no entry")


def test_entry_outside_population_added(mod, base, expected, pop, rows):
    lines = list(base)
    for i, l in enumerate(lines):
        if l.startswith("## Discrepancies"):
            lines[i:i] = [f"### {outside_fam(rows, pop)} - A family outside the population",
                          "", "- **Reading**: `match`. Injected.", ""]
            break
    check(mod, lines, base, expected, pop, rows, "entries outside the population")


def test_verdict_word_changed(mod, base, expected, pop, rows):
    lines = list(base)
    for i, l in enumerate(lines):
        if l.strip().startswith("- **Reading**: `match`"):
            lines[i] = l.replace("`match`", "`wider`", 1)
            break
    hits = check(mod, lines, base, expected, pop, rows, "verdict_wider")
    assert any("wider" in p for p in hits), "the changed verdict word is not named in the problem"


def test_prose_citation_truncated(mod, base, expected, pop, rows):
    lines = list(base)
    for _i, path, a, b in mod.prose_citations(base):
        if path and b > a:
            for j, l in enumerate(lines):
                m = mod.CITE.search(l)
                if m and m.group(1) == path and int(m.group(3)) == b:
                    lines[j] = l[:m.start()] + "`%s:%d-%d`" % (path, a, b - 1) + l[m.end():]
                    break
            break
    check(mod, lines, base, expected, pop, rows, "citation line")


def test_prose_citation_path_absent(mod, base, expected, pop, rows):
    lines = list(base)
    for _i, path, a, b in mod.prose_citations(base):
        if path.startswith("build/"):
            for j, l in enumerate(lines):
                m = mod.CITE.search(l)
                if m and m.group(1) == path:
                    lines[j] = (l[:m.start()] + "`build/no-such-file.tex:%d-%d`" % (a, b)
                                + l[m.end():])
                    break
            break
    check(mod, lines, base, expected, pop, rows, "resolves to no single manuscript file")


def test_population_entry_demoted(mod, base, expected, pop, rows):
    lines = list(base)
    i, l = first_heading(mod, lines)
    lines[i] = "####" + l[3:]
    check(mod, lines, base, expected, pop, rows, "is in the population, so it is not promoted")
