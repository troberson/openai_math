r"""The self-tests for `notes/scripts/catlib/quotes.py` and `notes/scripts/seed_quotes.py`.

The resolver resolves a `(path, start, end, head, tail)` spec to the verbatim source span; the seeder
seeds the specs for `notes/reports/subfinding-pairs.md` and the 24 summaries pages and requires each to
reproduce the page's quote. This file injects the faults the locator must catch: a head absent from the
window; a tail that occurs only before the head; a line number past the file's end; a window whose start
is after its end; a head that is unique in the line and still bounds a span running to a later
occurrence of the tail; a trailing `\qquad ` that must join to one space, not two; an HTML tag inside a
word the page spells without markup, where the raw span is NOT the page quote and only the folded
comparison is; math whose `<` and `>` make the folded line lose text the raw line keeps; and a quote
that wraps across lines.

The clean test pins the population the seeder reports for the two surfaces: **1,997** specs, **754**
from the pair page and **1,243** from the summaries pages; **1,981** seeded and **16** measured negatives
(the spans the cited file does not carry, seeded to `start` 0); **1,145** single-line and **836** range
specs; **274** heads widened past three words; **464** whole-quote specs; the `mode` split **1,922**
raw, **59** folded, **16** not located; **0** round-trip failures. The seeded table on disk must
reproduce every page quote, in its own class — byte-for-byte for `raw`, fold-equal for `folded` — so a
resolver that passes its synthetic cases and fails the corpus is caught.

The resolver measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_quotes.py -q
"""
import pathlib
from collections import Counter

import pytest
from catlib.paths import ROOT
from catlib.quotes import resolve, seed
from catlib.text import strip_markup as norm
from catlib.layout import reorder

PAGE = ROOT / "notes" / "reports" / "subfinding-pairs.md"
SRC = ROOT / "overview.tex"

# Family 262's shape: the title is quoted twice in one abstract, once as the entry title and once as
# the last `\href` label, so a head that occurs in both must resolve to the occurrence whose span is
# shortest -- the one inside the label the page quotes.
LINE_262 = (r"\resultentry{262}{Sharp one-dimensional Lieb--Thirring inequalities}"
            r"{Proves the sharp inequality for $1/2<\gamma<3/2$ with matrix potentials.}"
            r"\enspace\href{https://x/y.pdf}{Sharp one-dimensional Lieb--Thirring "
            r"inequalities for matrix potentials}")
QUOTE_262 = "Sharp one-dimensional Lieb--Thirring inequalities for matrix potentials"

# A head that occurs once, with a tail that occurs only at the far end: the span it bounds is the whole
# line, which is the fault `seed` must refuse by widening the head.
LINE_FAR = ("Sharp one-dimensional Lieb--Thirring inequalities are proved. "
            "The constant is scalar for matrix potentials.")

# A wrapped sentence whose first line ends with `\qquad ` -- the trailing space must not become two.
LINE_WRAP = [r"Let $G$ be finitely presented,\qquad ",
             r"and $ba\ne1$. The group $G$ admits",
             "a finite two-dimensional model."]
QUOTE_WRAP = (r"Let $G$ be finitely presented,\qquad and $ba\ne1$. The group $G$ admits "
              r"a finite two-dimensional model.")

# Math that makes strip_markup lose text: `\le` folds to a space, leaving a `<` and a `>` whose
# contents the HTML-tag rule deletes, so the folded line reads `for $04$, establishing`.
LINE_MATH = r"for $0<q\le4$ and to the Brownian continuum random tree for $q>4$ the bound is sharp."
QUOTE_MATH = r"for $0<q\le4$ and to the Brownian continuum random tree"

# A word the source writes with a tag inside it and the page writes without.
LINE_TAG = "prime-to-<i>p</i> is the density of the prime-to-p part of the group."
QUOTE_TAG = "prime-to-p is the density"

# (label, lines, start, end, head, tail, expected) — what resolve must return for each spec.
MUTANTS = [
    ("head absent from the window", [LINE_262], 1, 1, "Bogomolov-Pop reconstruction",
     "matrix potentials", None),
    ("tail occurs only before the head", [LINE_262], 1, 1, "Proves the sharp inequality",
     "Lieb--Thirring inequalities}", None),
    ("line past the file's end", [LINE_262], 2, 2, "Sharp one-dimensional", "potentials", None),
    ("window start after its end", [LINE_262], 2, 1, "Sharp one-dimensional", "potentials", None),
    # The span ends where the tail ends, so the line's trailing period is outside it: the fault is the
    # span running to the far tail, not the period.
    ("a unique head that bounds too long a span", [LINE_FAR], 1, 1,
     "Sharp one-dimensional Lieb--Thirring", "for matrix potentials", LINE_FAR[:-1]),
    ("a trailing \\qquad joins to one space", LINE_WRAP[:2], 1, 2,
     "Let $G$ be finitely presented,", "group $G$ admits",
     r"Let $G$ be finitely presented,\qquad and $ba\ne1$. The group $G$ admits"),
    ("a tag inside a word the page spells plain", [LINE_TAG], 1, 1,
     "prime-to-p is the density", "part of the group",
     "prime-to-<i>p</i> is the density of the prime-to-p part of the group"),
    ("math that makes the folded line lose text", [LINE_MATH], 1, 1,
     r"for $0<q\le4$ and", "random tree", QUOTE_MATH),
]

# (label, lines, quote, start, end, expected spec) — what seed must return, and how the spec resolves.
SEEDS = [
    ("the doubled title resolves to the shortest span", [LINE_262], QUOTE_262, 1, 1,
     (1, 1, "Sharp one-dimensional Lieb--Thirring", "for matrix potentials")),
    ("a wrapped quote seeds a range, not a single line", LINE_WRAP, QUOTE_WRAP, 1, 3,
     (1, 3, "Let $G$ be", "finite two-dimensional model.")),
    ("a quote absent from the window seeds nothing", [LINE_262],
     "the optimal constant is the scalar one-bound-state value", 1, 1, None),
    ("a short quote seeds the whole quote with no boundary", [LINE_TAG], QUOTE_TAG, 1, 1,
     (1, 1, QUOTE_TAG, None)),
    ("math the folded line loses is located in the raw line", [LINE_MATH], QUOTE_MATH, 1, 1,
     (1, 1, r"for $0<q\le4$ and", "continuum random tree")),
]


@pytest.fixture(scope="module")
def page_rows():
    import seed_quotes as S
    return reorder(S.rows(S.SRC.read_text(encoding="utf-8").splitlines()))


@pytest.fixture(scope="module")
def summary_rows():
    import seed_quotes as S
    return S.summary_rows()


def test_clean_page(page_rows, summary_rows):
    """The population the seeder reports for both surfaces, pinned."""
    all_rows = page_rows + summary_rows
    seeded = [s for s, _q in all_rows if s["start"] != "0"]
    assert len(page_rows) == 754
    assert len(summary_rows) == 1243
    assert len(all_rows) == 1997
    assert len(seeded) == 1981
    assert sum(1 for s in seeded if s["start"] == s["end"]) == 1145
    assert sum(1 for s in seeded if s["start"] != s["end"]) == 836
    assert sum(1 for s in seeded if len(s["head"].split()) > 3) == 274
    assert sum(1 for s in seeded if s["tail"] == "") == 464
    modes = Counter(s["mode"] for s, _q in all_rows)
    assert (modes["raw"], modes["folded"], modes["none"]) == (1922, 59, 16), modes
    # Every seeded spec must reproduce its quote in its own class, so a spec that resolves to text the
    # page does not quote is a failure, not a pass.
    cache: dict[str, list[str]] = {}
    bad = []
    for spec, q in all_rows:
        if spec["start"] == "0":
            continue
        key = spec["path"]
        if key not in cache:
            cache[key] = (ROOT / key).read_text(encoding="utf-8", errors="replace").splitlines()
        got = resolve(cache[key], int(spec["start"]), int(spec["end"]),
                      spec["head"], spec["tail"] or None)
        ok = got == q if spec["mode"] == "raw" else got is not None and norm(got) == norm(q)
        if not ok:
            bad.append((spec["page"], spec["fam"], spec["seq"], spec["which"], spec["mode"]))
    assert not bad, bad[:3]


@pytest.mark.parametrize("label,src,start,end,head,tail,expected", MUTANTS)
def test_resolve_faults(src, start, end, head, tail, expected, label):
    assert resolve(src, start, end, head, tail) == expected, label


@pytest.mark.parametrize("label,src,quote,start,end,expected", SEEDS)
def test_seed_faults(src, quote, start, end, expected, label):
    got = seed(src, quote, start, end)
    assert got == expected, label
    if got is not None:
        s, e, head, tail = got
        span = resolve(src, s, e, head, tail)
        assert span is not None, f"{label}: the seeded spec does not resolve to a span"
        # A page quote that carries markup the source does not is equal to the raw span only after
        # the checker's normalizer; the raw span is the record, so fold-equality is the honest test.
        assert span == quote or norm(span) == norm(quote), label


def test_seeded_table_reproduces_the_page(page_rows, summary_rows):
    """The table on disk must carry the specs that reproduce every page quote, so a stale TSV is caught.

    The key is `(page, fam, seq, which)`, because the two surfaces number their rows differently: a pair
    row's `seq` is the manuscript the pair names, a summaries row's is the span's index in the page. The
    round-trip is per class — byte-for-byte for `raw`, fold-equal for `folded` — and a `none` row must
    carry no spec, so its `start` is 0.
    """
    tsv = ROOT / "notes" / "tables" / "quotes.tsv"
    if not tsv.is_file():
        pytest.skip("notes/tables/quotes.tsv has not been written yet")
    from catlib.tsv import read_join_rows
    rows = read_join_rows(tsv)
    keyed = {(r["page"], r["fam"], r["seq"], r["which"]): r for r in rows}
    assert len(keyed) == len(page_rows) + len(summary_rows)
    cache: dict[str, list[str]] = {}
    for spec, q in page_rows + summary_rows:
        r = keyed[(spec["page"], spec["fam"], spec["seq"], spec["which"])]
        assert r["mode"] == spec["mode"], (spec["page"], spec["fam"], spec["seq"], spec["which"])
        if r["mode"] == "none":
            assert r["start"] == "0" and r["end"] == "0", (spec["page"], spec["fam"], spec["seq"])
            continue
        key = r["path"]
        if key not in cache:
            cache[key] = (ROOT / key).read_text(encoding="utf-8", errors="replace").splitlines()
        got = resolve(cache[key], int(r["start"]), int(r["end"]), r["head"], r["tail"] or None)
        ok = got == q if r["mode"] == "raw" else got is not None and norm(got) == norm(q)
        assert ok, (spec["page"], spec["fam"], spec["seq"], spec["which"], r["mode"])


def test_page_anchor_grammar_is_shared():
    """The seeder reads the page's anchors with catlib.anchors' grammar, not a private regex."""
    import catlib.quotes as Q
    from catlib.anchors import EXT_MAN, anchor_pattern
    assert Q.ANCH.pattern == anchor_pattern(EXT_MAN, ranges=True).pattern
    assert pathlib.Path(PAGE).is_file()
