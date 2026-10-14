"""The extracted self-tests for `notes/scripts/verify_subfinding_pairs.py` and the page.

The checker's passes are: the population pass (one block per population family, none outside); the
header pass (the block's `overview.tex` line is that family's `\resultentry`, `n` is its manuscript
count, the tier matches the ledger); the quotation pass (every clause and every title verbatim on the
cited line, and the clause's own anchor equal to the block anchor); the id pass (every `[fam:seq]`
resolves in `notes/tables/subfindings.tsv` to that family's manuscript row, and the quoted title is
that row's title); the coverage pass (`claimed` and `unclaimed` disjoint and covering the family's
full seq set); the target pass (`claimed` equals the set of ids used as pair targets); the counts pass
(the Summary table equal to the recomputation, the false-positive list consistent with the probe set);
the tail pass; and the render diff against `render_reports.py`.

Each fault below mutates the page text in memory, so no page is written. `verify_subfinding_pairs.py`'s
`load_inputs()` is under `functools.cache` (`:54`): the checker writes nothing and the tests mutate page
text, so a second call in the same process cannot see a different corpus, and the ten `check()` calls
this file makes pay the `overview.tex`, `subfindings.tsv` and ledger walk once.

**The needles that name a page line or a measured count are derived at run time, not recorded.** The
block-header line for a family is found in the mutated page, so a band shift moves the needle with the
layout; the Summary-table needle's measured value comes from the checker's own `measured` dict. The
needles that stay literal are the mutation's own inputs — the anchor written, the id borrowed, the id
duplicated, the id dropped, the family inserted, the count written.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_subfinding_pairs.py -q`
"""

import pathlib
import re

import pytest

PAGE = pathlib.Path("notes/reports/subfinding-pairs.md")


def block_head(c, fam):
    """The 1-based page line of the block header for `fam`, and the `overview.tex` anchor it names."""
    for i, line in enumerate(c.split("\n")):
        m = re.match(rf"^## {fam} · `overview\.tex:(\d+)`", line)
        if m:
            return i + 1, int(m.group(1))
    raise AssertionError(f"no block header for {fam}")


def row_of(c, sub):
    """The 1-based page line carrying `sub`; a sub on more than one line makes the needle ambiguous."""
    hits = [i + 1 for i, line in enumerate(c.split("\n")) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


# (label, needle, mutation). A needle is a function of the mutated page, the loaded checker and the
# measured dict; a mutation is a function of the page.
MUTANTS = [
    ("paraphrase dressed as a quote",
     lambda c, v, m: (f"009: page:{row_of(c, 'Also proves Bogomolov-Pop reconstruction')}: quoted "
                      f"clause is not verbatim on overview.tex:{block_head(c, '009')[1]}: Also "
                      "proves Bogomolov-Pop reconstruction from abelian-by-cen"),
     lambda p: p.replace('"Also proves Bogomolov--Pop reconstruction',
                         '"Also proves Bogomolov-Pop reconstruction', 1)),
    ("clause anchor on the wrong line",
     lambda c, v, m: (f"009: page:{row_of(c, '`overview.tex:95`) -> \"The Bogomolov-Pop')}: clause "
                      f"anchor overview.tex:95 differs from the block anchor {block_head(c, '009')[1]}"),
     lambda p: p.replace("`overview.tex:94`) -> \"The Bogomolov-Pop",
                         "`overview.tex:95`) -> \"The Bogomolov-Pop", 1)),
    ("title id borrowed from another family",
     lambda c, v, m: (f"009: page:{row_of(c, 'reconstruction theorem\" (`overview.tex:94`) [010:3]')}: "
                      "target id 010:3 is from another family"),
     lambda p: p.replace("[009:3]", "[010:3]", 1)),
    ("an id in both partitions",
     "041: ids in both claimed and unclaimed: ['041:1']",
     lambda p: p.replace("- claimed: 041:1 041:2\n- unclaimed:",
                         "- claimed: 041:1 041:2\n- unclaimed: 041:1", 1)),
    ("a title dropped from the partition",
     "034: ids in neither partition: ['034:3']",
     lambda p: p.replace("- unclaimed: 034:3 034:5 034:6",
                         "- unclaimed: 034:5 034:6", 1)),
    ("a stale Summary-table count",
     lambda c, v, m: (f"Summary table: titles claimed by no clause states 60, "
                      f"measured {m['titles claimed by no clause']}"),
     lambda p: p.replace("| titles claimed by no clause | 146 |",
                         "| titles claimed by no clause | 60 |", 1)),
    ("a block outside the population",
     "blocks for families outside the population: ['008']",
     lambda p: p.replace("## 009 · `overview.tex:94` · n=3 · T2",
                         "## 008 · `overview.tex:92` · n=1 · T0\n\n"
                         "- main: \"x\" (`overview.tex:92`) -> unmatched\n"
                         "- claimed:\n- unclaimed:\n\n"
                         "## 009 · `overview.tex:94` · n=3 · T2", 1)),
    # Prose the counts pass never parses: the rejected-rule yields are narrative, not a
    # Summary-table row. Only the render diff can see them, so the needle is the page line it names.
    ("a rejected-rule yield in prose altered",
     lambda c, v, m: f"page line {row_of(c, 'tried and rejected: `also` (57)')}: page 'tried and rejected: `also` (57)",
     lambda p: p.replace("tried and rejected: `also` (56)",
                         "tried and rejected: `also` (57)", 1)),
    ("the filter-cost clause count in prose altered",
     lambda c, v, m: (f"page line {row_of(c, 'Reading it yields **140** accepted clause pairs')}: "
                      "page '  densest targets. Reading it yields **140** accepted clause pairs"),
     lambda p: p.replace("Reading it yields **141** accepted clause pairs",
                         "Reading it yields **140** accepted clause pairs", 1)),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(load, text):
    v = load("verify_subfinding_pairs")
    problems, measured = v.check(text)
    assert problems == []
    assert (measured["families read"], measured["manuscripts in the population"],
            measured["sub-finding clause pairs accepted"],
            measured["headline clause pairs accepted"],
            measured["clauses recorded unmatched"],
            measured["titles claimed by a clause"],
            measured["titles claimed by no clause"],
            measured["families with >=1 accepted sub-finding pair"],
            measured["families with >=1 clause recorded unmatched"],
            measured["families with an accepted sub-finding pair and no probe hit"]) == \
        (167, 514, 203, 165, 18, 368, 146, 153, 17, 119)
    assert (measured["probe hits over all 372"], measured["probe hits over the multi set"],
            measured["multi-manuscript families"]) == (62, 40, 167)
    inputs = v.load_inputs()
    _, _, _, counts, _ = inputs
    population, probe, probe_all, multi, band, band2, band3 = v.population_of(counts)
    assert (len(population), len(probe), len(probe_all), len(multi), len(band), len(band2),
            len(band3)) == (167, 40, 62, 167, 73, 37, 17)


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_subfinding_pairs")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs, measured = v.check(cand)
    want = needle(cand, v, measured) if callable(needle) else needle
    assert any(want in p for p in probs), f"{label}: needle did not fire\n{probs}"
