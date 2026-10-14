"""The extracted self-tests for `notes/scripts/verify_scope_exclusions.py`.

The checker measures; this file injects. Each test corrupts one part of `notes/reports/scope-exclusions.md`
in memory, runs the checker's own passes over the mutated lines, and requires the pass that owns that
defect to name it. Nothing here writes a page: a mutation is a list of lines, never the file.

The seven defects, and the pass that must see each:

  Pass A (coverage)  - a family row deleted, so the table no longer covers the scope notes on disk.
  Pass B (anchors)   - a real quotation cited to a real line outside the file's `## Scope` section.
  Pass C (quotes)    - a real quotation with one word corrupted; a quotation the cited file does not
                       contain; a paraphrase dressed as a quote; a real quotation cited to the wrong
                       line inside the section (Pass B accepts that anchor, so only Pass C can flag it).
  Pass E (sync)      - a prose count Pass D never parses, visible only in the render diff.

Run: python3 -m pytest tests/test_scope_exclusions.py -q
"""

import re

import pytest
from catlib import render as RD
from catlib import yaml as Y

ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*$")
CITE = re.compile(r"`lean/docs/(\d{3})\.md:(\d+)`")

pytestmark = pytest.mark.mutant


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_scope_exclusions")


@pytest.fixture(scope="module")
def page(mod):
    return mod.PAGE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def lines(page):
    return page.splitlines()


@pytest.fixture(scope="module")
def setup(mod, lines):
    """The first Entries row, its quotation, its citation, and the cited file's Scope span."""
    first = next(n for n, line in enumerate(lines, 1) if ROW.match(line))
    base = lines[first - 1]
    row = ROW.match(base)
    assert row is not None, f"the first Entries row is not a table row: {base[:60]}"
    fam, cell = row.group(1), row.group(2)
    qm = re.search(r"“([^”]+)”", cell)
    if qm is None:
        pytest.skip(f"the first Entries row carries no quotation: {base[:60]}")
    assert qm is not None, "the first Entries row carries no quotation"
    quote = qm.group(1)
    cite = CITE.search(cell)
    src = (mod.DOCS_DIR / f"{fam}.md").read_text(encoding="utf-8", errors="replace").splitlines()
    span = Y.scope_span_lines(src)
    assert span is not None, "the first Entries row's scope note has no `## Scope` section"
    _first, last = span
    outside = next(n for n in range(last + 1, len(src) + 1) if src[n - 1].strip())
    return {"first": first, "base": base, "fam": fam, "quote": quote,
            "cite": cite, "src": src, "last": last, "outside": outside}


def problems(mod, cand, page):
    """The checker's passes over mutated lines. The lines are rebuilt as page text so the sync pass
    sees the same bytes a page on disk carries."""
    text = "\n".join(cand) + ("\n" if page.endswith("\n") else "")
    return mod.check(cand)[0] + RD.sync_problems(mod.PAGE, text)


def flagged(mod, cand, page, needle):
    return [p for p in problems(mod, cand, page) if needle in p]


def test_clean_page(mod, lines, page):
    assert problems(mod, lines, page) == []


def test_corrupted_quotation(mod, lines, setup, page):
    """A real quotation with one word corrupted: Pass C must flag the text, not the anchor."""
    s = setup
    cand = list(lines)
    cand[s["first"] - 1] = s["base"].replace(s["quote"], s["quote"].replace("the", "tbe", 1), 1)
    assert cand != lines, "the mutation changed nothing"
    assert flagged(mod, cand, page, "not on"), "Pass C did not flag the corrupted quotation"


def test_citation_outside_the_scope_section(mod, lines, setup, page):
    """A real quotation cited to a real line outside the section: Pass B must check the span."""
    s = setup
    cand = list(lines)
    cand[s["first"] - 1] = s["base"].replace(s["cite"].group(0),
                                             f"`lean/docs/{s['fam']}.md:{s['outside']}`", 1)
    assert cand != lines, "the mutation changed nothing"
    assert flagged(mod, cand, page, "outside the `## Scope` section"), \
        "Pass B did not flag the citation outside the section"


def test_fabricated_quotation(mod, lines, setup, page):
    """A quotation the cited file does not contain anywhere: Pass C must flag it."""
    s = setup
    cand = list(lines)
    cand[s["first"] - 1] = s["base"].replace(
        s["quote"], "the formalization deliberately omits every companion result", 1)
    assert cand != lines, "the mutation changed nothing"
    assert flagged(mod, cand, page, "not on"), "Pass C did not flag the fabricated quotation"


def test_paraphrased_quotation(mod, lines, setup, page):
    """A paraphrase dressed as a quote: same section, same shape, different words."""
    s = setup
    cand = list(lines)
    cand[s["first"] - 1] = s["base"].replace(s["quote"],
                                             s["quote"].replace("are excluded in", "are omitted from", 1), 1)
    assert cand != lines, "the mutation changed nothing"
    assert flagged(mod, cand, page, "not on"), "Pass C did not flag the paraphrase"


def test_quotation_cited_to_the_wrong_line_in_the_section(mod, lines, setup, page):
    """Line drift: a real quotation cited to a different non-blank real line in the same section.
    Pass B accepts the anchor, so only Pass C can catch it."""
    s = setup
    moved = next(n for n in range(int(s["cite"].group(2)) + 1, s["last"] + 1) if s["src"][n - 1].strip())
    cand = list(lines)
    cand[s["first"] - 1] = s["base"].replace(s["cite"].group(0),
                                             f"`lean/docs/{s['fam']}.md:{moved}`", 1)
    assert cand != lines, "the mutation changed nothing"
    assert flagged(mod, cand, page, "not on"), "Pass C did not flag the line drift"


def test_deleted_family_row(mod, lines, setup, page):
    """Pass A must notice the table no longer covers the scope notes on disk."""
    s = setup
    cand = [line for i, line in enumerate(lines) if i != s["first"] - 1]
    assert len(cand) == len(lines) - 1, "the row was not removed"
    assert flagged(mod, cand, page, "no row"), "Pass A did not flag the deleted row"


def test_prose_count_outside_the_measured_tables(mod, lines, page):
    """How many scope notes a merge added is not a Measurements row and not one of the prose counts
    Pass D reads. Only the render diff can see it."""
    prose = next(n for n, line in enumerate(lines) if line.startswith("plus the 7 that the 2026-10-07"))
    cand = list(lines)
    cand[prose] = cand[prose].replace("plus the 7 that", "plus the 8 that", 1)
    assert cand != lines, "the mutation changed nothing"
    assert flagged(mod, cand, page, "page is not the writer's render"), \
        "the render diff did not flag the prose count"


def pad_cells(t):
    """Pad every table cell with two spaces. The row regexes allow whitespace, so padding must read
    the same rows; a regex that required exact spacing would drop every row and the pass would report
    no row for each family, so the row count is the discriminator, not the render diff."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def row_count(mod, t):
    """Rows the pass's row regex matches in the page text."""
    return sum(1 for ln in t.splitlines() if mod.ROW.match(ln))


def test_padded_table_cells_are_still_read(mod, page):
    cand = pad_cells(page)
    assert cand != page, "padding changed nothing"
    assert row_count(mod, cand) == row_count(mod, page), \
        f"padded table reads {row_count(mod, cand)} rows, clean page {row_count(mod, page)}"
    assert mod.check(cand.splitlines()) == mod.check(page.splitlines()), \
        f"padded page reports {mod.check(cand.splitlines())} problems, clean page " \
        f"{mod.check(page.splitlines())}"
