r"""The tracked probe for the split rule's boundary semantics.

The split table records one row per boundary, transcribed from a committed page. A measured phrase
that gains an item between two recorded boundaries gains it *inside* a recorded run, not at a
boundary, so a part has to match as an ordered token subsequence. Only the part's first token is
anchored at position 0, which is what keeps the wider rule a boundary rule: content landing at a
boundary still raises.

The divergence this probe documents was measured 2026-10-18 against the prefix rule
(`flex(pre).match(rest)`, adjacent tokens), which raises the moment a recorded part stops being the
whole contiguous span. 14 of the 134 recorded parts have a subsequence span wider than the recorded
part, but only one of them is a content insertion - the scope-notes row in `index-design.md` (25
recorded tokens, 31 in the measured span). The other 13 are line-wraps: their token count is
unchanged, and the adjacent `\s+` prefix rule already matches across the newline. That is why the
prefix rule fails on exactly 1 part, not 14, and why widening to a subsequence is what makes the
table valid: it is that one content-grown part that the contiguous rule cannot read.

The probe asserts the documented intent, not the current behaviour: every recorded part matches as
an anchored ordered subsequence, the 14 span-widening parts are absorbed, and the prefix rule fails
on exactly the 1 content insertion.

Run: python3 notes/scripts/run_tests.py notes/scripts/tests/probes/test_split_subsequence.py -q
     python3 notes/scripts/run_tests.py -m probe -q
"""

import sys

import pytest

sys.path.insert(0, "/home/tamara/Downloads/_Git/math/notes/scripts")

# pylint: disable=wrong-import-position
from catlib import templates as TPL
from catlib import text as TX

pytestmark = pytest.mark.probe

# The 14 parts whose measured span is wider than the recorded part, as (page, label, part tokens,
# span tokens). Equal token counts are line-wraps (the adjacent rule already matches); a larger
# span count is a content insertion (the adjacent rule fails).
GAP_ROWS = [
    ("notes/README.md", "scan_links", 6, 6),
    ("notes/development/index-design.md", "added TSV byte figures", 12, 12),
    ("notes/development/index-design.md", "added TSV byte figures", 12, 12),
    ("notes/development/index-design.md", "added TSV byte figures", 12, 12),
    ("notes/development/index-design.md", "added TSV byte figures", 12, 12),
    ("notes/development/index-design.md", "added TSV byte figures", 25, 31),
    ("notes/development/index-design.md", "disk link check", 10, 10),
    ("notes/development/index-links.md", "prose_notesdoc", 12, 12),
    ("notes/development/index-links.md", "prose_notesdoc", 16, 16),
    ("notes/development/index-links.md", "prose_regchecked", 4, 4),
    ("notes/reports/links.md", "rec_all", 8, 8),
    ("notes/reports/links.md", "knob_quote", 4, 4),
    ("notes/reports/topics.md", "tp_headline", 15, 15),
    ("notes/reports/topics.md", "tp_yieldhist", 19, 19),
]

MEASURED = {"parts": 134, "exact": 120, "gap": 14, "content": 1}

SEP_SUBSEQ = r"[\s\S]*?"  # the subsequence separator apply_split uses for a recorded part
SEP_ADJ = r"\s+"  # the prefix rule's separator: adjacent tokens only


def subsequence_span(part, rest):
    """Shortest span at the start of `rest` realizing `part` as an ordered token subsequence."""
    pos = 0
    for tok in part.split():
        m = TX.flex_part(tok, SEP_SUBSEQ).search(rest, pos)
        if m is None:
            return None
        pos = m.end()
    return rest[:pos]


def collect():
    """Walk the writer's label registry, recording every apply_split call it makes.

    The probe reads the recorded parts from the call itself, so the population is the table as the
    writer uses it, not a copy of the table.
    """
    calls = []
    raises = []
    state = {"page": None}
    orig = TX.apply_split

    def spy(label, phrase, prefixes):
        calls.append((state["page"], label, phrase, list(prefixes)))
        try:
            return orig(label, phrase, prefixes)
        except ValueError:
            raises.append((state["page"], label))
            return {}

    TX.apply_split = spy
    try:
        for page in sorted(TPL.ALL_PAGES):
            state["page"] = page
            TPL.LABELS[page]()
    finally:
        TX.apply_split = orig
    return calls, raises


@pytest.fixture(scope="module")
def measured():
    """(calls, raises, exact, gap_rows, fail_rows, content_insertions) for the module, once.

    `rest` is advanced by the subsequence span for every part, exactly as `apply_split` does (the
    subsequence rule never raises, so the walk stays in sync). A gap row is a part whose subsequence
    span is wider than the recorded part; a content insertion is a gap row whose span also carries
    more tokens - the case the adjacent prefix rule cannot read.
    """
    calls, raises = collect()
    exact, gap_rows, fail_rows, content_insertions = 0, [], [], []
    for page, label, phrase, prefixes in calls:
        rest = phrase
        for part in prefixes:
            if not part.split():
                continue
            rest = rest.lstrip()
            span = subsequence_span(part, rest)
            if span is None:
                fail_rows.append((page, label, part))
                continue
            is_gap = span != part
            if is_gap and len(span.split()) > len(part.split()):
                content_insertions.append((page, label, len(part.split()), len(span.split())))
            if is_gap:
                gap_rows.append((page, label, len(part.split()), len(span.split())))
            else:
                exact += 1
            rest = rest[len(span):]
    return calls, raises, exact, gap_rows, fail_rows, content_insertions


def test_population_is_non_vacuous(measured):
    """The probe read the writer's whole split surface, not a subset."""
    calls, _, exact, gap_rows, fail_rows, _ = measured
    assert calls, "the writer made no apply_split call - the probe read nothing"
    parts = exact + len(gap_rows) + len(fail_rows)
    assert parts == MEASURED["parts"], (parts, MEASURED["parts"])


def test_every_recorded_part_matches_as_an_ordered_subsequence(measured):
    """The documented intent: no recorded part fails the subsequence rule.

    Against the prefix rule this assertion fails, because a part whose run grew cannot be matched
    as the whole contiguous span.
    """
    _, raises, _, _, fail_rows, _ = measured
    assert not fail_rows, fail_rows[:6]
    assert not raises, raises[:6]


def test_span_widening_parts_are_absorbed(measured):
    """The 14 parts whose measured span is wider than the recorded part.

    A part match consumes only its own internal whitespace, so the inserted content lands in that
    part's slot. The gap rows are the measured boundaries where the span grew.
    """
    _, _, exact, gap_rows, _, _ = measured
    assert exact == MEASURED["exact"], (exact, MEASURED["exact"])
    assert len(gap_rows) == MEASURED["gap"], (len(gap_rows), MEASURED["gap"])
    assert sorted(gap_rows) == sorted(GAP_ROWS), gap_rows


def test_prefix_rule_fails_on_exactly_the_content_insertion(measured):
    """The probe's own witness that the wider rule is what makes the table valid.

    The adjacent prefix rule (`flex_part(part, SEP_ADJ)`) matches a part only when it is the whole
    contiguous span. It fails exactly on the content insertions - the gap rows whose span carries
    more tokens than the recorded part. The line-wrap gap rows have an unchanged token count and a
    whitespace-only widening, so the adjacent rule reads them. If the content-insertion set were not
    a proper subset of the gap set, the subsequence rule would be absorbing nothing the prefix rule
    could not already read, and the probe would prove no divergence.
    """
    _, _, _, gap_rows, _, content_insertions = measured
    gap_content = {(p, l, pt, st) for p, l, pt, st in gap_rows if st > pt}
    assert set(content_insertions) == gap_content, (content_insertions, gap_content)
    assert len(content_insertions) == MEASURED["content"], (len(content_insertions), MEASURED["content"])
    assert 0 < len(content_insertions) < len(gap_rows), (
        len(content_insertions),
        len(gap_rows),
    )
