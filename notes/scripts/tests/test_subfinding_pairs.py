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
text, so a second call in the same process cannot see a different corpus, and the nine `check()` calls
this file makes pay the `overview.tex`, `subfindings.tsv` and ledger walk once.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_subfinding_pairs.py -q`
"""

import pathlib

import pytest

PAGE = pathlib.Path("notes/subfinding-pairs.md")

# (label, needle, mutation). A needle must fire for its own fault and for no other, and must not
# fire on the clean page.
MUTANTS = [
    ("paraphrase dressed as a quote",
     "009: page:69: quoted clause is not verbatim on overview.tex:94: "
     "Also proves Bogomolov-Pop reconstruction from abelian-by-cen",
     lambda p: p.replace('"Also proves Bogomolov--Pop reconstruction',
                         '"Also proves Bogomolov-Pop reconstruction', 1)),
    ("clause anchor on the wrong line",
     "009: page:69: clause anchor overview.tex:95 differs from the block anchor 94",
     lambda p: p.replace("`overview.tex:94`) -> \"The Bogomolov-Pop",
                         "`overview.tex:95`) -> \"The Bogomolov-Pop", 1)),
    ("title id borrowed from another family",
     "009: page:69: target id 010:3 is from another family",
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
     "Summary table: titles claimed by no clause states 60, measured 94",
     lambda p: p.replace("| titles claimed by no clause | 94 |",
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
     "page line 35: page 'tried and rejected: `also` (57)",
     lambda p: p.replace("tried and rejected: `also` (56)",
                         "tried and rejected: `also` (57)", 1)),
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
        (49, 203, 62, 47, 18, 109, 94, 40, 17, 6)
    assert (measured["probe hits over all 372"], measured["probe hits over the multi set"],
            measured["multi-manuscript families"]) == (62, 40, 167)
    inputs = v.load_inputs()
    _, _, _, counts, _ = inputs
    population, probe, probe_all, multi = v.population_of(counts)
    assert (len(population), len(probe), len(probe_all), len(multi)) == (49, 40, 62, 167)


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_subfinding_pairs")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs = v.check(cand)[0]
    assert any(needle in p for p in probs), f"{label}: needle did not fire\n{probs}"
