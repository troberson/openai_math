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

import measure_names as M
import pytest
from catlib.text import first_group

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


def bump(t, pat, delta):
    """Change the page's own count at `pat` by `delta`. The mutation's input is the page as it stands,
    so a measured count that moves does not need a hand-edit here."""
    m = re.search(pat, t)
    assert m, f"{pat!r} not in the page"
    raw = m.group(1)
    new = str(int(raw) + delta)
    span = m.group(0)
    return t[:m.start()] + span.replace(raw, new, 1) + t[m.end():]


def new_also(c):
    """The `also` yield the mutated page states — the value the mutation wrote, read back."""
    return first_group(r"tried and rejected: `also` \((\d+)\)", c)


def new_pairs(c):
    """The accepted-clause-pairs count the mutated page states."""
    return first_group(r"Reading it yields \*\*(\d+)\*\* accepted clause pairs", c)


def pad_cells(t):
    """Pad every table cell with two spaces. The row regex allows whitespace, so the pass must read the
    same rows; a regex that required exact spacing would drop rows, and the missing-row line is what
    would show it."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = ln
        out.append(padded)
    return "\n".join(out)


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
     lambda c, v, m: (f"Summary table: titles claimed by no clause states "
                      f"{m['titles claimed by no clause'] - 86}, measured {m['titles claimed by no clause']}"),
     lambda p: bump(p, r"\| titles claimed by no clause \| (\d+) \|", -86)),
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
     lambda c, v, m: (f"page line {row_of(c, f'tried and rejected: `also` ({new_also(c)})')}: "
                      f"page 'tried and rejected: `also` ({new_also(c)})"),
     lambda p: bump(p, r"tried and rejected: `also` \((\d+)\)", 1)),
    ("the filter-cost clause count in prose altered",
     lambda c, v, m: (f"page line {row_of(c, f'Reading it yields **{new_pairs(c)}** accepted clause pairs')}: "
                      f"page '  densest targets. Reading it yields **{new_pairs(c)}** accepted clause pairs"),
     lambda p: bump(p, r"Reading it yields \*\*(\d+)\*\* accepted clause pairs", -1)),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(load, text):
    v = load("verify_subfinding_pairs")
    problems, measured = v.check(text)
    assert problems == []
    inputs = v.load_inputs()
    _, _, _, counts, _ = inputs
    population, probe, probe_all, multi, band, band2, band3 = v.population_of(counts)
    # The page carries one block per population family, so the read count is the population size.
    assert 0 < len(population) == measured["families read"]
    assert 0 < sum(counts[f] for f in population) == measured["manuscripts in the population"]
    # Every manuscript title is claimed by a clause or by none: the partition is exhaustive.
    assert measured["titles claimed by a clause"] + measured["titles claimed by no clause"] == \
        measured["manuscripts in the population"]
    assert measured["sub-finding clause pairs accepted"] > 0
    assert measured["headline clause pairs accepted"] > 0
    assert measured["clauses recorded unmatched"] > 0
    assert measured["families with >=1 accepted sub-finding pair"] <= measured["families read"]
    assert measured["families with >=1 clause recorded unmatched"] <= measured["families read"]
    assert measured["families with an accepted sub-finding pair and no probe hit"] <= \
        measured["families with >=1 accepted sub-finding pair"]
    assert measured["probe hits over the multi set"] <= measured["probe hits over all 372"]
    assert 0 < len(multi) == measured["multi-manuscript families"]
    assert len(probe) <= len(probe_all) <= len(multi)
    # The rejected-rule bands are nested by construction: the widest is the loosest rule.
    assert 0 < len(band3) < len(band2) < len(band)


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_subfinding_pairs")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs, measured = v.check(cand)
    want = needle(cand, v, measured) if callable(needle) else needle
    assert any(want in p for p in probs), f"{label}: needle did not fire\n{probs}"


def test_padded_table_cells_are_still_read(load, text):
    """Padding every Summary-table cell must not change what the pass reads. The row regex allows
    whitespace, so a padded page must report no missing row and the same ten values. A regex that
    required exact spacing would drop rows, and the missing-row line is what would show it — that is the
    discriminator, not the render diff, which fires for the padding either way."""
    v = load("verify_subfinding_pairs")
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    probs, measured = v.check(cand)
    missing = [p for p in probs if "Summary table" in p]
    assert not missing, f"padded rows are not read: {missing[:2]}"
    got = {m.group("label"): int(m.group("num")) for ln in cand.split("\n")
           if (m := v.TABLE_ROW.match(ln.strip())) and m.group("label") in measured}
    n_summary = len([ln for ln in text.split("\n")
                            if (m := v.TABLE_ROW.match(ln.strip())) and m.group("label") in measured])
    assert 0 < n_summary == len(got), \
        f"padded page reads {len(got)} Summary rows, the clean page carries {n_summary}"
    assert all(got[k] == measured[k] for k in got), \
        f"padded table values differ: {[k for k in got if got[k] != measured[k]]}"


def test_verbatim_quote_is_the_raw_bytes():
    """The pairs checker compares a quoted clause as a raw substring of the family's `\\resultentry`
    line, so a quote that de-LaTeXes `Gy\\'arf\\'as's` to `Gyárfás's` fails against the bytes
    `overview.tex:405` ships. The accent fold (`measure_names.fold`) accepts the same quote, so the
    byte rule is the stricter rule. Neither string is read from the corpus."""
    line = r"Gy\'arf\'as's conjecture is false for k = 5"
    quote = "Gy\xe1rf\xe1s's"
    assert quote not in line, "the raw substring test accepted the de-LaTeXed quote"
    assert M.fold(quote) in M.fold(line), \
        f"the accent fold read {M.fold(line)!r}, so it does not accept the de-LaTeXed quote"
