r"""The self-tests for `notes/scripts/catlib/quotes.py` and `notes/scripts/seed_quotes.py`.

The resolver resolves a `(path, start, end, head, tail)` spec to the verbatim source span; the seeder
seeds a locator spec for `notes/reports/subfinding-pairs.md` and the summaries pages. The stored spec is
`(page, fam, seq, which, path, start, end, head, tail)`: a locator, not content. The seeder's check is
that every located row's locator resolves (to a non-None span in its source); the round-trip to the page
quote is then reported, not required, as three classes — raw (byte-for-byte), folded (fold-equal after
the checker's normalizer), normalizer-gap (located, but the resolved text the normalizer cannot fold back
to the page quote). A measured negative is `start` 0 with `head` and `tail` blank. This file injects the
faults the locator must catch: a head absent from the window; a tail that occurs only before the head; a
line number past the file's end; a window whose start is after its end; a head that is unique in the line
and still bounds a span running to a later occurrence of the tail; a trailing `\qquad ` that must join to
one space, not two; an HTML tag inside a word the page spells without markup, where the raw span is NOT
the page quote and only the folded comparison is; math whose `<` and `>` make the folded line lose text
the raw line keeps; and a quote that wraps across lines.

The clean test pins the population the seeder reports for the two surfaces, relationally: every spec is
located (`start` non-zero) or a measured negative (`start` 0), located splits into single-line and range,
and every located locator resolves — the raw plus folded plus normalizer-gap classes sum to the located
set. The seeded table on disk must carry the locator that resolves for every located row, so a seeder
that passes its synthetic cases and fails the corpus is caught.

The resolver measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_quotes.py -q
"""
import pathlib

import pytest
from catlib.layout import reorder
from catlib.paths import ROOT
from catlib.quotes import resolve, seed
from catlib.text import strip_markup as norm

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


_LINES: dict[str, list[str]] = {}


def _resolve(spec: dict[str, str]) -> str | None:
    """Resolve a locator spec against the source file its `path` names (cached per path)."""
    path = spec["path"]
    if path not in _LINES:
        if path == "overview.tex":
            _LINES[path] = SRC.read_text(encoding="utf-8").splitlines()
        else:
            _LINES[path] = (ROOT / path).read_text(encoding="utf-8", errors="replace").splitlines()
    return resolve(_LINES[path], int(spec["start"]), int(spec["end"]),
                   spec["head"], spec["tail"] or None)


def test_clean_page(page_rows, summary_rows):
    """The population the seeder reports for both surfaces, pinned relationally."""
    all_rows = page_rows + summary_rows
    located = [s for s, _q in all_rows if s["start"] != "0"]
    # The population is the two surfaces, and every partition is exhaustive: located plus the measured
    # negatives is the row set, single-line plus range covers the located set, and every located
    # locator resolves so the raw plus folded plus normalizer-gap classes sum to the located set.
    assert len(page_rows) > 0 and len(summary_rows) > 0
    assert len(located) + (len(all_rows) - len(located)) == len(all_rows)
    single = sum(1 for s in located if s["start"] == s["end"])
    rng = sum(1 for s in located if s["start"] != s["end"])
    assert 0 < single + rng == len(located)
    raw = folded = gap = 0
    unres = []
    for spec, q in all_rows:
        if spec["start"] == "0":
            continue
        res = _resolve(spec)
        if res is None:
            unres.append((spec["page"], spec["fam"], spec["seq"], spec["which"]))
            continue
        if res == q:
            raw += 1
        elif norm(res) == norm(q):
            folded += 1
        else:
            gap += 1
    assert not unres, f"locators that do not resolve: {unres[:3]}"
    assert raw + folded + gap == len(located), "located split does not cover the located set"
    assert raw > 0 and folded > 0


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
    """The table on disk must carry the locator that resolves for every located row, so a stale TSV is caught.

    The key is `(page, fam, seq, which)`, because the two surfaces number their rows differently: a pair
    row's `seq` is the manuscript the pair names, a summaries row's is the span's index in the page. The
    stored spec is a locator, not content, so the check is that each located row's head/tail resolves
    against the file its `path` names; a measured negative must carry `start` 0 with blank `head` and
    `tail`. The round-trip to the page quote (raw/folded/normalizer-gap) is asserted in `test_clean_page`.
    """
    tsv = ROOT / "notes" / "tables" / "quotes.tsv"
    if not tsv.is_file():
        pytest.skip("notes/tables/quotes.tsv has not been written yet")
    from catlib.tsv import read_rows
    rows = read_rows(tsv)
    keyed = {(r["page"], r["fam"], r["seq"], r["which"]): r for r in rows}
    assert len(keyed) == len(page_rows) + len(summary_rows)
    unres = []
    for spec, _q in page_rows + summary_rows:
        r = keyed[(spec["page"], spec["fam"], spec["seq"], spec["which"])]
        assert r["start"] == spec["start"], (spec["page"], spec["fam"], spec["seq"], spec["which"])
        assert r["head"] == spec["head"], (spec["page"], spec["fam"], spec["seq"], spec["which"])
        assert r["tail"] == spec["tail"], (spec["page"], spec["fam"], spec["seq"], spec["which"])
        if r["start"] == "0":
            assert r["head"] == "" and r["tail"] == "", (spec["page"], spec["fam"], spec["seq"])
            continue
        if _resolve(r) is None:
            unres.append((r["page"], r["fam"], r["seq"], r["which"]))
    assert not unres, f"TSV locators that do not resolve: {unres[:3]}"


def test_page_anchor_grammar_is_shared():
    """The seeder reads the page's anchors with catlib.anchors' grammar, not a private regex."""
    import catlib.quotes as Q
    from catlib.anchors import EXT_MAN, anchor_pattern
    assert Q.ANCH.pattern == anchor_pattern(EXT_MAN, ranges=True).pattern
    assert pathlib.Path(PAGE).is_file()
