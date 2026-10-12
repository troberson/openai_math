"""The extracted self-tests for `notes/scripts/verify_citations.py` and `notes/citations.md`.

The checker's passes are: the population gates (521 `.bib` files, 513 owner manuscripts, 13,802
entries, 372 ledger families, 719 manuscript owners, 17 disciplines, 4 depth levels, 9 field types);
the work-table pass (one row per work, its manuscript count equal to the measured owning set, its
quoted title the most frequent verbatim form for its normalized title at the anchor line); the
fenced-block pass (each block matched against its nearest preceding anchor); the count pass (the
population, cited-key, work-layer, pair-layer, discipline-crossing, cluster, release-layer, coverage
and sensitivity numbers); and the completeness pass (the discipline-crossing list, the >=5 cluster
table and the release-target table complete in both directions — no measured row missing, no page row
unmeasured).

Each fault below mutates the page text in memory, so no page is written. `verify_citations.py`'s
`measure()` is under `functools.cache` (`:75`): the checker writes nothing and the tests mutate page
text, so a second call in the same process cannot see a different corpus, and the ten `check()` calls
this file makes pay the 521-file walk once.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_citations.py -q`
"""

import pathlib

import pytest

PAGE = pathlib.Path("notes/citations.md")

# (label, needle, mutation). A needle must fire for its own fault and for no other, and must not
# fire on the clean page.
MUTANTS = [
    ("paraphrase dressed as a quotation",
     "block line 2 does not match preprints/A-conditional-abelianity-theorem-for-special-fourfold-"
     "pairs-with-a-half-weight-divisor-October-5-2026/build/source/references.bib",
     lambda p: p.replace("author = {{The Stacks Project Authors}}",
                         "author = {{The Stacks Project editors}}")),
    ("invented anchor file",
     "work anchor absent on disk: preprints/No-such-manuscript-September-1-2026/build/references.bib:106",
     lambda p: p.replace("`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-"
                         "with-a-half-weight-divisor-October-5-2026/build/source/references.bib:106`",
                         "`preprints/No-such-manuscript-September-1-2026/build/references.bib:106`")),
    ("anchor off by one line",
     "no entry begins at preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-"
     "with-a-half-weight-divisor-October-5-2026/build/source/references.bib:105",
     lambda p: p.replace("half-weight-divisor-October-5-2026/build/source/references.bib:106`",
                         "half-weight-divisor-October-5-2026/build/source/references.bib:105`")),
    ("count drift in the pair table",
     "pair layer >=5: page does not contain '| \u22655 | **419** | 296 | **6** |'",
     lambda p: p.replace("| \u22655 | **419** |", "| \u22655 | **418** |")),
    ("headline crossing count",
     "headline crossing count: page does not contain '6 of 419 pairs at \u22655 shared titles "
     "cross a discipline boundary'",
     lambda p: p.replace("6 of 419 pairs at \u22655", "7 of 419 pairs at \u22655")),
    ("cluster membership swap",
     "cluster row '033 034 039 036 037 046 051 054 056 057 058 065 066 068': measured membership "
     "033 034 035 036 037 046 051 054 056 057 058 065 066 068",
     lambda p: p.replace("033 034 035 036 037 046 051 054 056 057 058 065 066 068",
                         "033 034 039 036 037 046 051 054 056 057 058 065 066 068")),
    ("work count drift",
     "work 'The {Stacks Project}': page says 43 manuscripts, measured 42",
     lambda p: p.replace("| 42 | `The {Stacks Project}`", "| 43 | `The {Stacks Project}`")),
    ("cluster discipline composition",
     "cluster row 260 335 336 346: composition 'Mathematical physics 12, Differential geometry 3'",
     lambda p: p.replace("Mathematical physics 11, Differential geometry 4",
                         "Mathematical physics 12, Differential geometry 3")),
    ("release-target count",
     "release row 'Log-abundance-in-characteristic-zero-September-24-2026' at 12, measured",
     lambda p: p.replace("| 11 | `Log-abundance-in-characteristic-zero-September-24-2026`",
                         "| 12 | `Log-abundance-in-characteristic-zero-September-24-2026`")),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8")


def test_clean_page(load, text):
    v = load("verify_citations")
    assert v.check(text) == []
    m = v.measure(v.norm_title)
    m2 = v.measure(v.norm_noguard)
    assert (len(m["files"]), len(m["owners"]), m["n_entries"], len(m["inv"]),
            len(m["shared"]), len(m["pairs"])) == (521, 513, 13802, 8775, 2251, 3668)
    assert (len(m2["inv"]), len(m2["shared"]), len(m2["pairs"])) == (8765, 2254, 3676)
    assert (m2["all_keys"], m2["cited"], len(m2["depth"]), m2["discs"], m2["fams"],
            len(m2["led"]), len(m2["man2fam"]), len(m2["titles"])) == (13797, 13058, 4, 17, 299,
                                                                       372, 719, 513)
    assert (len(m2["release"]), m2["release_entries"], m2["release_listed"],
            len(m2["rinv"]), len(m2["rpairs"])) == (277, 432, 393, 268, 203)


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_citations")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs = v.check(cand)
    assert any(needle in p for p in probs), f"{label}: needle did not fire\n{probs}"
