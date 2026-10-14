r"""The extracted self-tests for `notes/scripts/verify_t0_chains.py` and `notes/reports/t0-chains.md`.

The checker's passes are: the anchor pass (every backticked `path:line` resolves to a file that
exists with the line in range); the fenced-block pass (each block attributed to the nearest preceding
anchor, matched as joined text against the same number of source lines); the quotation pass (each
*"…"* pinned to an anchor in its own row, verbatim modulo whitespace); the count pass (the count
phrases re-derived from the ledger, `subfindings.tsv`, `notes/reports/t0-triage.md` and the `.bib` layer);
the summary-table and chain-table passes (field by field); the family-block pass (one block per
population family, each naming exactly its own two manuscripts with titles verbatim on the family's
anchor line, and each Citation layer line matching the recomputed counts); the named-list pass; the
family-268 verification-directory pass; and the render diff against `render_reports.py`.

Each fault below mutates the page text in memory, so no page is written. `verify_t0_chains.py`'s
`population()` is under `functools.cache` (`:118`): the checker writes nothing and the tests mutate
page text, so a second call in the same process cannot see a different corpus, and the fifteen
`check()` calls this file makes pay the corpus walk once.

The last fault is not a content change: it pads the table cells. A row pattern that requires exactly
one space after each pipe reads **0** rows from the padded page, so the table pass is silently
skipped; the tolerant `\s*` form reads the same rows it reads from the clean page. `test_padded_table`
pins the row count, which is the assertion that distinguishes the two patterns.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_t0_chains.py -q`
"""

import pathlib

import pytest

PAGE = pathlib.Path("notes/reports/t0-chains.md")


def pad_table(p):
    r"""Pads every cell of every pipe-delimited table row with two spaces. The strict single-space
    row pattern reads 0 rows from this text; the tolerant `\s*` pattern reads the same rows it reads
    from the clean page."""
    out = []
    for line in p.split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            line = "| " + "  |  ".join(cells) + "  |"
        out.append(line)
    return "\n".join(out)

# (label, needle, mutation). A needle must fire for its own fault and for no other, and must not
# fire on the clean page.
MUTANTS = [
    ("paraphrase dressed as a quotation",
     ("quote at page line 378 is not on overview.tex:629: 'The unique threshold bound state for the "
      "SU(N) BFSS model'"),
     lambda p: p.replace('*"The unique threshold bound state of the SU(N) BFSS model"*',
                         '*"The unique threshold bound state for the SU(N) BFSS model"*')),
    ("title swap",
     ("quote at page line 367 is not on overview.tex:625: 'Positive eigenvalues of the relative SU(2) "
      "BFSS Hamiltonian'"),
     lambda p: p.replace('*"Boundary-field gap"*',
                         '*"Positive eigenvalues of the relative SU(2) BFSS Hamiltonian"*')),
    ("chain table tier",
     "chain table 032 tier 'T2' != ledger 'T0'",
     lambda p: p.replace("| 032 | T0 | 5 |", "| 032 | T2 | 5 |")),
    ("edge count",
     ("count phrase missing (intra-family edges): '**15** of the 27 cite their sibling: **8** mutual "
      "pairs and **7** one-directional'"),
     lambda p: p.replace("**15** of the 27 cite their sibling",
                         "**16** of the 27 cite their sibling")),
    ("anchor line out of range",
     "anchor line out of range: overview.tex:9999 (file has 860 lines, page line 70)",
     lambda p: p.replace("(`overview.tex:716`)", "(`overview.tex:9999`)")),
    ("block for a family outside the population",
     "301: block for a family outside the population",
     lambda p: p.replace("### 300 — ", "### 301 — ")),
    ("table .bib count",
     "035: table .bib 3 != recomputed 1",
     lambda p: p.replace("| 035 | A&CG | bound, classification | 1 | 0 | 0 |",
                         "| 035 | A&CG | bound, classification | 3 | 0 | 0 |")),
    ("manuscript path not on disk",
     ("065/2: path 'preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-"
      "2026/paper.pdf' != subfindings path"),
     lambda p: p.replace(
         "preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/"
         "article.pdf",
         "preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/"
         "paper.pdf")),
    ("population count phrase",
     "count phrase missing (population): '**27** families carrying **54** manuscripts'",
     lambda p: p.replace("**27** families carrying", "**28** families carrying")),
    ("mutual pairs list",
     "named list mismatch (mutual pairs): expected '041, 077, 217, 265, 268, 286, 302, 368'",
     lambda p: p.replace("The mutual pairs are 041, 077, 217, 265, 268, 286, 302, 368.",
                         "The mutual pairs are 077, 217, 265, 268, 286, 302, 368.")),
    ("fenced block line",
     ("block at page line 96 does not match preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-"
      "Dualizable-Kn-Local-Spectra-September-24-2026/build/refere"),
     lambda p: p.replace("  journal = {Selecta Mathematica. New Series},",
                         "  journal = {Selecta Math.},")),
    ("citation layer count",
     "268: citation layer (2, 3, 1) != recomputed (2, 2, 1)",
     lambda p: p.replace("Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.\n\n"
                         "### 270 — ",
                         "Citation layer: 2 `.bib` files, 3 intra-family edges, 1 mutual pair.\n\n"
                         "### 270 — ")),
    # Prose no count phrase reads: the heading name in the population rule. Only the render diff
    # sees it, so the needle is the page line the render diff names.
    ("prose count outside the phrase list",
     "page line 7: page 'the remaining 94 families",
     lambda p: p.replace("the remaining 93 families", "the remaining 94 families")),
    # Not a content change: the table is padded. A strict single-space row pattern reads 0 rows and
    # the population guard fires; the tolerant `\s*` pattern reads the rows, so the only problems are
    # the render diff, whose first changed line is the padded chain-table header.
    ("padded table cells",
     "page line 51: page '| Fam  |",
     pad_table),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8")


def test_clean_page(load, text):
    v = load("verify_t0_chains")
    res = v.check(text)
    assert res["problems"] == []
    assert (res["anchors"], res["blocks"], res["quotes"], res["counts"], res["sync"]) == \
        (120, 3, 61, 12, 0)
    assert (res["sum_rows"], res["chain_rows"], res["heads"], res["bullets"],
            res["lists"], res["files"]) == (27, 5, 27, 54, 4, 2)


def test_padded_table_is_read_by_the_tolerant_pattern(load, text):
    r"""The discriminating assertion for the padding fault: the padded page must yield the same row
    counts as the clean page. A row pattern that requires exactly one space after each pipe reads 0
    summary rows and 0 chain rows from the padded text, so the table pass reports nothing about the
    table and the page reads clean apart from the population guard; the tolerant `\s*` pattern reads
    the rows. Measured 2026-10-13: 0 / 0 against the pre-fix pattern, 27 / 5 against the fixed one."""
    v = load("verify_t0_chains")
    clean = v.check(text)
    res = v.check(pad_table(text))
    assert res["sum_rows"] == clean["sum_rows"] == 27, \
        f"{res['sum_rows']} summary rows read from the padded table"
    assert res["chain_rows"] == clean["chain_rows"] == 5, \
        f"{res['chain_rows']} chain rows read from the padded table"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_t0_chains")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs = v.check(cand)["problems"]
    assert any(needle in p for p in probs), f"{label}: needle did not fire\n{probs}"
