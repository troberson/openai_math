"""The self-tests for `notes/scripts/verify_abstracts.py`.

Each test injects one corruption into the text of `notes/reports/abstracts.md` in memory and asserts the pass
that owns it reports a problem: the quotation pass (word altered, fabricated, repointed), the marker
pass (marker deleted, marker absent from the table, table path missing on disk), the count pass
(headline, tag row, bucket row, disagreement count, multi-abstract directory), and the sync pass (a
prose count no phrase in `count_phrases()` names, visible only in the render diff). Every quotation
mutant is built from a real quotation on the real page and every count mutant from a real phrase, so
a checker that only re-reads its own regexes cannot pass. Each test asserts the injected text differs
from the page it started from: a mutant whose target string is absent is a failed test, not a pass.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_abstracts.py -q
"""
import re

import pytest

pytestmark = pytest.mark.mutant

ELLIPSIS = "…"
BKEY = ("<0.30", "0.30-0.50", "0.50-0.70", "0.70-0.90", ">=0.90")


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_abstracts")


@pytest.fixture(scope="module")
def page(mod):
    return mod.PAGE.read_text(encoding="utf-8", errors="replace")


@pytest.fixture(scope="module")
def table(mod, page):
    tbl, dupes = mod.parse_table(page.splitlines())
    assert tbl, "no Sources table rows parsed — the page has no table"
    assert not dupes, f"a source is declared twice: {dupes}"
    return tbl


@pytest.fixture(scope="module")
def counts(mod):
    return mod.population()


@pytest.fixture(scope="module")
def target(mod, page, table):
    """(quote match, marker start, marker end) for the quotation the mutants are built from: a real
    span over 40 characters, its source a manuscript `.tex`, and the word `prove` inside it."""
    q = next(m for m in mod.QUOTE.finditer(page)
             if len(m.group(1)) > 40 and mod.marker_after(page, m.end())
             and table.get(mod.marker_after(page, m.end()).group(1), "").endswith(".tex")
             and "prove" in m.group(1))
    mk = mod.marker_after(page, q.end())
    gap_m = re.match(r"[ \t\r\n)]*", page[q.end():q.end() + 12])
    gap = gap_m.end() if gap_m else 0
    start = q.end() + gap
    return q, start, start + len(mk.group(0))


def problems(mod, cand, table, counts):
    return mod.check(cand, table, counts)[0]


def flagged(mod, cand, table, counts, needle):
    return [p for p in problems(mod, cand, table, counts) if needle in p]


def test_clean_page(mod, page, table, counts):
    assert len(table) == 35, f"the Sources table has {len(table)} rows, expected 35"
    assert problems(mod, page, table, counts) == [], "the real page must be silent"


def test_quotation_word_altered(mod, page, table, counts, target):
    q, _s, _e = target
    cand = page[:q.start()] + "“" + q.group(1).replace("prove", "disprove", 1) + "”" + page[q.end():]
    assert cand != page, "the quotation target is gone from the page"
    hits = flagged(mod, cand, table, counts, "not in")
    assert hits, "the quotation pass did not flag a word altered inside a real quotation"


def test_quotation_fabricated(mod, page, table, counts, target):
    q, _s, _e = target
    cand = page[:q.start()] + "“the ledger proves every family is formalized in Lean” [S1]\n" + page[q.start():]
    assert cand != page
    hits = flagged(mod, cand, table, counts, "not in overview.tex")
    assert hits, "the fabricated quotation was not checked against overview.tex"


def test_quotation_repointed_at_a_file_that_lacks_it(mod, page, table, counts, target):
    _q, start, end = target
    cand = page[:start] + "[S31]" + page[end:]
    assert cand != page
    hits = flagged(mod, cand, table, counts, "not in notes/tables/abstracts.tsv")
    assert hits, "a quotation repointed at a table row that cannot carry it was not flagged"


def test_marker_deleted(mod, page, table, counts, target):
    _q, start, end = target
    cand = page[:start] + page[end:]
    assert cand != page
    hits = flagged(mod, cand, table, counts, "no [S#] marker")
    assert hits, "a quotation left without its marker was not flagged"


def test_marker_absent_from_the_table(mod, page, table, counts):
    cand = page + "\nAn unlisted source [S99] is cited here.\n"
    assert cand != page
    hits = flagged(mod, cand, table, counts, "not in the Sources table")
    assert hits, "a marker with no table row was not flagged"


def test_table_path_missing_on_disk(mod, page, counts):
    cand = "\n".join(l for l in page.splitlines() if not l.startswith("| S31 |"))
    assert cand != page, "the S31 table row is gone from the page"
    tbl, _ = mod.parse_table(cand.splitlines())
    tbl["S31"] = "notes/does-not-exist.tsv"
    hits = flagged(mod, cand, tbl, counts, "does not exist")
    assert hits, "a table row pointing at a path that is not on disk was not flagged"


def test_headline_count_altered(mod, page, table, counts):
    n = len(counts["man"])
    cand = page.replace(f"**0 identical, 0 abridged, {n} divergent.**",
                        f"**0 identical, 0 abridged, {n + 3} divergent.**", 1)
    assert cand != page, "the headline phrase is gone from the page"
    hits = flagged(mod, cand, table, counts, "count mismatch (headline relation counts)")
    assert hits, "the count pass did not flag the altered headline"


def test_tag_table_row_skewed(mod, table, counts):
    t = counts["tag_tot"]["classification"]
    d = counts["tag_dis"].get("classification", {"ov-only": [], "ms-only": []})
    row = (f"| classification | {t['ov']} | {t['ms']} | {t['man']} | {len(d['ov-only'])} "
           f"| {len(d['ms-only'])} |")
    cand = row.replace(f"| {t['ms']} |", f"| {t['ms'] - 1} |", 1)
    assert cand != row, "the classification row is not on the page"
    hits = flagged(mod, cand, table, counts, "count mismatch (tag row classification)")
    assert hits, "a skewed tag-table row was not flagged"


def test_bucket_count_moved(mod, table, counts):
    mb, fb = counts["man_buckets"], counts["fam_buckets"]
    brow = (f"| count | {' / '.join(str(mb[k]) for k in BKEY)} "
            f"| {' / '.join(str(fb[k]) for k in BKEY)} |")
    cand = brow.replace(f"{mb['<0.30']} /", f"{mb['<0.30'] + 3} /", 1)
    assert cand != brow, "the bucket row is not on the page"
    hits = flagged(mod, cand, table, counts, "count mismatch (bucket row)")
    assert hits, "a moved bucket count was not flagged"


def test_disagreement_count_altered(mod, page, table, counts):
    dis = sum(1 for f, sh in counts["fam_shapes"].items() if sh["ov"] != sh["ms"])
    cand = page.replace(f"**{dis} of {counts['families']} families have at least one shape "
                        f"disagreement between the two texts;",
                        f"**{dis - 1} of {counts['families']} families have at least one shape "
                        f"disagreement between the two texts;", 1)
    assert cand != page, "the disagreement phrase is gone from the page"
    hits = flagged(mod, cand, table, counts, "count mismatch (shape disagreement count)")
    assert hits, "an altered disagreement count was not flagged"


def test_multi_abstract_directory_renamed(mod, page, table, counts):
    fam_id, mdir, _k = counts["multi_dirs"][-1]
    date = "-".join(mdir.rsplit("-", 2)[1:])
    cand = page.replace(f"`{mdir}`", f"`{mdir[:-len(date)]}November-1-2026`", 1)
    assert cand != page, "the multi-abstract directory name is gone from the page"
    hits = flagged(mod, cand, table, counts, f"count mismatch (multi-abstract directory {fam_id})")
    assert hits, "a renamed multi-abstract directory was not flagged"


def test_prose_count_outside_the_phrase_list(mod, page, table, counts):
    """The count pass never reads 692 — it is prose, in no phrase `count_phrases()` names. Only the
    sync pass, which compares the page with the writer's render, can see it."""
    cand = page.replace("The 692 manuscript", "The 693 manuscript", 1)
    assert cand != page, "the prose count is gone from the page"
    hits = flagged(mod, cand, table, counts, "page is not the writer's render")
    assert hits, "a prose count outside the phrase list was not flagged by the sync pass"
