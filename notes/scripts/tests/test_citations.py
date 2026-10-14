"""The extracted self-tests for `notes/scripts/verify_citations.py` and `notes/reports/citations.md`.

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
this file makes pay the 521-file walk once. The file count is pinned as a **walk equality**: the test
walks `preprints/` for `.bib` files itself and the population's count must equal the walk, so a
bibliography added to a manuscript moves the walk, not the recorded number.

Two cases feed the accent rules a string, not the corpus. The shipped `catlib.bib.ACCENT` guard leaves
an escape applied to a letter (`\'a`) unfolded, so `norm_title` splits `Gy\'arf\'as's` into pieces,
while the checker's no-guard variant folds it into one word — the guard is what makes the two
normalizations disagree, and the page's sensitivity row is measured against that difference. The
apostrophe case: `catlib.text.fold_apostrophe` makes a U+2019 title and an ASCII title one key, where a
rule that strips only Unicode diacritics keeps the two spellings distinct.

**The needles that name a measured figure are derived at run time, not recorded.** The pair-layer
phrase, the headline crossing count, the cluster membership, the cluster composition, the work count
and the release-target count are rebuilt from the checker's own `measure()` dict, and the block-line
needle is rebuilt from the anchor the mutated page carries above the mutated block, so a band shift
moves the needle with the layout. The needles that stay literal are the mutation's own inputs — the
invented anchor path and the anchor line moved by one.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_citations.py -q`
"""

import collections
import pathlib
import re
import unicodedata

from catlib import bib
from catlib.text import fold_apostrophe

import pytest

PAGE = pathlib.Path("notes/reports/citations.md")

REPO = pathlib.Path(__file__).resolve().parents[3]


def tree_bib():
    """The `.bib` files under `preprints/`, walked by the test rather than counted by the checker. The
    population's file count is the census; this is the tree, so the equality is the invariant: the census
    counted every bibliography the corpus carries, and a `.bib` added to a manuscript moves the walk."""
    return list((REPO / "preprints").rglob("*.bib"))


def bib_blocks(c):
    """The fenced bibtex blocks of the mutated page, in order."""
    return re.findall(r"```bibtex\n(.*?)```", c, re.DOTALL)


def block_needle(c, sub):
    """The block-line problem the pass prints for the mutated line `sub`. The block's anchor is the
    last `preprints/...bib:line` above it, so the anchor is read from the mutated page, not recorded."""
    blk = next(b for b in bib_blocks(c) if sub in b)
    anch = re.findall(r"`(preprints/[^`]+?\.bib):(\d+)`", c[:c.index(blk)])
    assert anch, f"no anchor above the block carrying {sub!r}"
    path, line = anch[-1]
    plines = [l for l in blk.split("\n") if l.strip()]
    idx = next(i for i, l in enumerate(plines) if sub in l)
    return f"block line {idx + 1} does not match {path}:{int(line) + idx}"


def cluster_rows(c):
    """The >=5 cluster table of the mutated page: (mss, fams, disciplines, membership, composition)."""
    return re.findall(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([0-9 ]+)\|\s*([^|]+)\|\s*$",
                      c, re.MULTILINE)


def cluster_needle(c, v, M, cell, col):
    """The membership (col 3) or composition (col 4) problem for the row whose mutated cell is `cell`.
    The row's measured cluster is the same index of the checker's top-12 >=5 list, which is what the
    pass zips the table against."""
    rows = cluster_rows(c)
    hits = [i for i, r in enumerate(rows) if r[col].strip() == cell]
    assert len(hits) == 1, f"{cell!r} matches {len(hits)} cluster rows of the mutated page"
    idx = hits[0]
    clus = v.clusters(M["pairs"], 5)[:12]
    fams = rows[idx][3].strip()
    if col == 3:
        return f"cluster row {cell!r}: measured membership {' '.join(sorted({M['fam'][m] for m in clus[idx]}))}"
    cd = collections.Counter(M["disc"][m] for m in clus[idx])
    want = ", ".join("%s %d" % (d, n) for d, n in v.ranked(cd))
    return f"cluster row {fams}: composition {cell!r}, measured {want!r}"


def work_needle(c, v, M, title):
    """The work-count problem for the row carrying `title`: the page's count is read from the mutated
    row, the measured count from the checker's inverted index."""
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+?):(\d+)`\s*\|\s*$", c, re.MULTILINE)
    hits = [r for r in rows if r[1] == title]
    assert len(hits) == 1, f"{title!r} matches {len(hits)} work rows of the mutated page"
    cnt = hits[0][0]
    return f"work {title!r}: page says {cnt} manuscripts, measured {len(M['inv'][v.norm_title(title)])}"


def release_needle(c, _v, M, name):
    """The release-row problem for the target `name`: the page's row is read from the mutated page and
    measured against the same index of the checker's top-10 release targets, which is what the pass
    zips the table against. The measured name is the target the checker pairs the row with."""
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*$", c, re.MULTILINE)
    hits = [i for i, r in enumerate(rows) if r[1] == name]
    assert len(hits) == 1, f"{name!r} matches {len(hits)} release rows of the mutated page"
    idx = hits[0]
    top = sorted(M["rinv"].items(), key=lambda kv: (-len(kv[1]), kv[0]))[:10]
    d, s = top[idx]
    return f"release row {name!r} at {rows[idx][0]}, measured {d!r} at {len(s)}"


def pair_needle(_c, _v, M, k):
    """The pair-layer phrase the count pass demands at threshold `k`, rebuilt from the measured pairs."""
    ps = [(a, b, n) for (a, b), n in M["pairs"].items() if n >= k]
    cb = "**" if k >= 5 else ""
    phrase = ("| \u2265%d | **%s** | %d | %s%s%s |"
              % (k, format(len(ps), ","), sum(1 for a, b, n in ps if M["fam"][a] == M["fam"][b]),
                 cb, format(sum(1 for a, b, n in ps if M["disc"][a] != M["disc"][b]), ","), cb))
    return f"pair layer >={k}: page does not contain {phrase!r}"


def headline_needle(_c, _v, M, k):
    """The crossing-count phrase the count pass demands at threshold `k`: the crossing count and the
    pair count at that threshold, both rebuilt from the measured pairs."""
    cross = sum(1 for (a, b), n in M["pairs"].items() if n >= k and M["disc"][a] != M["disc"][b])
    p5 = sum(1 for n in M["pairs"].values() if n >= k)
    return ("headline crossing count: page does not contain '%d of %s pairs at \u2265%d shared titles "
            "cross a discipline boundary'" % (cross, format(p5, ","), k))


# (label, needle, mutation). A needle is a function of the mutated page, the loaded checker and the
# measured dict; a mutation is a function of the page.
MUTANTS = [
    ("paraphrase dressed as a quotation",
     lambda c, v, M: block_needle(c, "author = {{The Stacks Project editors}}"),
     lambda p: p.replace("author = {{The Stacks Project Authors}}",
                         "author = {{The Stacks Project editors}}")),
    ("invented anchor file",
     "work anchor absent on disk: preprints/No-such-manuscript-September-1-2026/build/references.bib:106",
     lambda p: p.replace("`preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-"
                         "with-a-half-weight-divisor-October-5-2026/build/source/references.bib:106`",
                         "`preprints/No-such-manuscript-September-1-2026/build/references.bib:106`")),
    ("anchor off by one line",
     ("no entry begins at preprints/A-conditional-abelianity-theorem-for-special-fourfold-pairs-"
      "with-a-half-weight-divisor-October-5-2026/build/source/references.bib:105"),
     lambda p: p.replace("half-weight-divisor-October-5-2026/build/source/references.bib:106`",
                         "half-weight-divisor-October-5-2026/build/source/references.bib:105`")),
    ("count drift in the pair table",
     lambda _c, _v, M: pair_needle(_c, _v, M, 5),
     lambda p: p.replace("| \u22655 | **419** |", "| \u22655 | **418** |")),
    ("headline crossing count",
     lambda _c, _v, M: headline_needle(_c, _v, M, 5),
     lambda p: p.replace("6 of 419 pairs at \u22655", "7 of 419 pairs at \u22655")),
    ("cluster membership swap",
     lambda c, v, M: cluster_needle(c, v, M,
                                    "033 034 039 036 037 046 051 054 056 057 058 065 066 068", 3),
     lambda p: p.replace("033 034 035 036 037 046 051 054 056 057 058 065 066 068",
                         "033 034 039 036 037 046 051 054 056 057 058 065 066 068")),
    ("work count drift",
     lambda c, v, M: work_needle(c, v, M, "The {Stacks Project}"),
     lambda p: p.replace("| 42 | `The {Stacks Project}`", "| 43 | `The {Stacks Project}`")),
    ("cluster discipline composition",
     lambda c, v, M: cluster_needle(c, v, M,
                                    "Mathematical physics 12, Differential geometry 3", 4),
     lambda p: p.replace("Mathematical physics 11, Differential geometry 4",
                         "Mathematical physics 12, Differential geometry 3")),
    ("release-target count",
     lambda c, v, M: release_needle(c, v, M, "Log-abundance-in-characteristic-zero-September-24-2026"),
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
    assert len(m["files"]) == len(tree_bib()) > 0, \
        f"bib files {len(m['files'])} against {len(tree_bib())} .bib files walked under preprints/"
    assert (len(m["owners"]), m["n_entries"], len(m["inv"]),
            len(m["shared"]), len(m["pairs"])) == (513, 13802, 8775, 2251, 3668)
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
    M = v.measure(v.norm_title)
    want = needle(cand, v, M) if callable(needle) else needle
    assert any(want in p for p in probs), f"{label}: needle did not fire\n{probs}"


def pad_cells(t):
    """Pad every table cell with two spaces. The checker reads four page tables with whitespace-flexible
    row patterns (`verify_citations.py:244` work, `:306` pair, `:349` cluster, `:378` release — 20, 6,
    12 and 10 rows on the clean page), so padding must read the same rows. A byte-exact single-space
    pattern drops every row and the pass prints five row-count problems ("work table has 0 rows,
    expected 20" and the three table-count lines), so the pass's own problem list is the discriminator,
    not the render diff. The test compares the list, not its length, so a padding fault that adds a
    problem is caught."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(load, text):
    v = load("verify_citations")
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    assert v.check(cand) == v.check(text), \
        f"padded page reports {v.check(cand)}, clean page {v.check(text)}"


def test_accent_guard_leaves_an_escape_applied_to_a_letter(load):
    """The shipped `catlib.bib.ACCENT` guard `(?![a-zA-Z])` means an escape applied to a letter (`\\'a`)
    is not folded, so `norm_title` splits `Gy\\'arf\\'as's` into pieces, while the checker's no-guard
    variant folds it into one word. The guard is what makes the two normalizations disagree, and the
    page's sensitivity row is measured against that difference. Neither string is read from the corpus."""
    v = load("verify_citations")
    s = r"Gy\'arf\'as's Conjecture"
    assert bib.ACCENT.findall(s) == [], f"the guarded rule folded {bib.ACCENT.findall(s)}"
    assert v.ACCENT_NOGUARD.findall(s) == ["a", "a"], \
        f"the no-guard rule read {v.ACCENT_NOGUARD.findall(s)}"
    assert v.norm_title(s) == "gy arf as s conjecture", \
        f"the guarded rule normalized to {v.norm_title(s)!r}"
    assert v.norm_noguard(s) == "gyarfas s conjecture", \
        f"the no-guard rule normalized to {v.norm_noguard(s)!r}"
    assert v.norm_title(s) != v.norm_noguard(s), \
        "the two rules agree, so the guard is inert and the sensitivity row measures nothing"


def test_apostrophe_fold_makes_the_two_title_spellings_one_key():
    """`catlib.text.fold_apostrophe` folds U+2019 to ASCII before matching, so a title the release
    writes with a typographic apostrophe and one written with ASCII are one key. A rule that strips
    only Unicode diacritics leaves U+2019 in place, so the two spellings stay distinct. Neither string
    is read from the corpus."""
    uni, ascii_ = "Erd\u2019s Conjecture", "Erd's Conjecture"
    assert fold_apostrophe(uni) == ascii_, f"the fold read {fold_apostrophe(uni)!r}"

    def no_fold(s):
        decomposed = unicodedata.normalize("NFD", s)
        return "".join(c for c in decomposed if not unicodedata.combining(c))

    assert no_fold(uni) != no_fold(ascii_), \
        "the narrowed rule joins the two spellings, so it is not the fold that separates them"
