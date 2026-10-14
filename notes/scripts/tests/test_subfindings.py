"""The self-tests for `notes/scripts/verify_subfindings.py`.

Each test injects one corruption into the bytes of `notes/tables/subfindings.tsv` in memory and asserts
the pass that owns it reports a problem: the manuscript pass (a display title renamed, a path moved off
the `overview.tex` path the row must carry, a formalized flag flipped against `formalization.yaml`, a
tier flipped against the ledger rule), the comparator pass (a named statement renamed, a row deleted so
the family's count no longer matches its scope note), and the seq check (two rows swapped inside one
family, which leaves the row set unchanged and only the order wrong). Every mutant is built from a real
row of the real table, so a checker that only re-reads its own regexes cannot pass. Each test asserts
the injected text differs from the table it started from: a mutant whose target row is absent is a
failed test, not a pass. The shape pass has no mutant here — it is exercised by the header and by the
fields each kind leaves empty, which the real table carries.

The path mutant is caught by the comparison with `overview.tex`, not by the on-disk branch: the
checker tests the *truth* path for existence, so a row whose path is mutated hits the mismatch branch
first. The on-disk branch fires on the release's own data, not on a row mutation, and no mutant here
can reach it.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_subfindings.py -q
"""
import csv

import pytest

from catlib.layout import reorder

pytestmark = pytest.mark.mutant


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_subfindings")


@pytest.fixture(scope="module")
def text(mod):
    return reorder(mod.TSV.read_text(encoding="utf-8").splitlines())


@pytest.fixture(scope="module")
def man_row(text):
    """The first manuscript row whose path is a `paper.pdf`, as fields, and the family it belongs
    to. The path mutant replaces the file name, so a row whose path is not `paper.pdf` makes the
    mutation inert — picking by path keeps the mutant effective when the row order moves."""
    idx = next(i for i, line in enumerate(text)
               if line.startswith("manuscript\t") and line.split("\t")[4].endswith("paper.pdf"))
    fields = text[idx].split("\t")
    return idx, fields, fields[1]


@pytest.fixture(scope="module")
def comp_row(text):
    """The first comparator row, as fields, and the family it belongs to."""
    idx = next(i for i, l in enumerate(text) if l.startswith("comparator-link\t"))
    fields = text[idx].split("\t")
    return idx, fields, fields[1]


def problems(mod, cand):
    rows = list(csv.DictReader(cand, delimiter="\t"))
    return mod.check(cand[0].split("\t"), rows)[0]


def flagged(mod, cand, needle, fam):
    """The problems that name the family the mutant touched, so a needle found in a problem about a
    different family is not a pass."""
    return [p for p in problems(mod, cand) if needle in p and fam in p]


def test_clean_table(mod, text):
    assert problems(mod, text) == [], "the real table must be silent"


def test_display_title_renamed(mod, text, man_row):
    idx, fields, fam = man_row
    cand = list(text)
    cand[idx] = "\t".join([*fields[:3], fields[3] + " (renamed)", *fields[4:]])
    assert cand != text, "the manuscript row is gone from the table"
    hits = flagged(mod, cand, "title is", fam)
    assert hits, "a display title renamed against overview.tex was not flagged"


def test_manuscript_path_that_does_not_exist(mod, text, man_row):
    idx, fields, fam = man_row
    cand = list(text)
    cand[idx] = "\t".join([*fields[:4], fields[4].replace("paper.pdf", "nosuch.pdf"), *fields[5:]])
    assert cand != text, "the manuscript path is not in the row the mutant is built from"
    hits = flagged(mod, cand, "path is", fam)
    assert hits, "a row whose path disagrees with overview.tex was not flagged"


def test_flipped_formalized_flag(mod, text, man_row):
    idx, fields, fam = man_row
    cand = list(text)
    cand[idx] = "\t".join([*fields[:5], "1" if fields[5] == "0" else "0", *fields[6:]])
    assert cand != text, "the formalized flag is not in the row the mutant is built from"
    hits = flagged(mod, cand, "yaml membership", fam)
    assert hits, "a formalized flag flipped against formalization.yaml was not flagged"


def test_flipped_tier(mod, text, man_row):
    idx, fields, fam = man_row
    cand = list(text)
    cand[idx] = "\t".join([*fields[:6], "T0" if fields[6] == "T3" else "T3", *fields[7:]])
    assert cand != text, "the tier is not in the row the mutant is built from"
    hits = flagged(mod, cand, "tier is", fam)
    assert hits, "a tier flipped against the ledger rule was not flagged"


def test_renamed_comparator_statement(mod, text, comp_row):
    idx, fields, fam = comp_row
    cand = list(text)
    cand[idx] = "\t".join([*fields[:7], fields[7] + " (invented)", *fields[8:]])
    assert cand != text, "the comparator statement is gone from the table"
    hits = flagged(mod, cand, "statement is", fam)
    assert hits, "a named statement renamed against its scope note was not flagged"


def test_comparator_row_deleted(mod, text, comp_row):
    idx, _fields, fam = comp_row
    cand = list(text)
    del cand[idx]
    assert cand != text, "the comparator row is gone from the table"
    hits = flagged(mod, cand, "comparator rows", fam)
    assert hits, "a deleted comparator row left the family's count unflagged"


def test_two_rows_swapped_in_one_family(mod, text):
    """The row set is unchanged, only the order is wrong, so this is the only mutant that exercises
    the seq check. It needs a family with more than one manuscript."""
    counts: dict = {}
    for l in text:
        if l.startswith("manuscript\t"):
            counts[l.split("\t")[1]] = counts.get(l.split("\t")[1], 0) + 1
    swap_fam = next(f for f, n in sorted(counts.items()) if n > 1)
    fam_rows = [i for i, l in enumerate(text) if l.startswith(f"manuscript\t{swap_fam}\t")]
    cand = list(text)
    cand[fam_rows[0]], cand[fam_rows[1]] = cand[fam_rows[1]], cand[fam_rows[0]]
    assert cand != text, "the two rows are identical, so the swap injects nothing"
    hits = flagged(mod, cand, "manuscript seq", swap_fam)
    assert hits, "a same-family row swap left the seq order unflagged"
