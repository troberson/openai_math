"""The self-tests for `notes/scripts/check_index_links.py`.

The checker scans the rendered index and reports broken links; this file injects the breaks. 21
injected hrefs — one per category the checker classifies, so a checker that only walks manuscript
paths fails — must not resolve and must classify as the category each claims; 8 real hrefs taken
from the rendered pages must resolve, because a checker that flags everything is useless; the
paren-balanced scanner must keep the CAT(0) path whole where `[^)]*` truncates it; and what the
classifier tags as a directory must be a directory on disk. The basename pass is the invariant
`math-faz.6` moved the 16 generated tables on: the index tree and `notes/tables/` share no
basename, so the two sets are required non-empty, the index must contain collisions, and a collision
is injected by handing the pass a shared name — a pass that returns 0 because a set is empty is not a
pass. The clean test asserts the scan baseline as the resolution invariant, not recorded counts: every
extracted link resolves to exactly one of directory or file, so the two counts sum to the link count
and nothing is broken, over a page set and a link set that are both non-empty.

The page's own prose is not mutated here: `verify_page_sync.py` owns the page check and mutates
the page in memory, so nothing in this file writes an index page. Every injected href is built
from a real page path, so a checker that only re-reads its own regexes cannot pass.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_index_links.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Injected hrefs that must all be reported broken, one per category the checker classifies.
INPUTS = [
    ("README.md", "disciplines/no-such.md", "index-page"),
    ("README.md", "no-such-table.tsv", "index-table"),
    ("README.md", "../tables/no-such-table.tsv", "tables-tsv"),
    ("README.md", "no-such-dir/", "index-dir"),
    ("README.md", "../no-such-note.md", "notes-doc"),
    ("names/cauchy.md", "../number-theory/999-no-such-family.md", "index-page"),
    ("names/cauchy.md", "../topics/no-such-topic.md", "index-page"),
    ("names/cauchy.md",
     ("../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-"
      "September-23-2026/no-such-file.tex"), "latex-source"),
    ("names/cauchy.md", "../../../preprints/No-Such-Manuscript/paper.pdf", "manuscript-pdf"),
    ("names/cauchy.md", "../../../preprints/No-Such-Manuscript/", "manuscript-dir"),
    ("names/cauchy.md", "../../../lean/ComparatorChallenges/no_such_config.json", "config-json"),
    ("names/cauchy.md", "../../../lean/ComparatorChallenges/NoSuch.lean", "config-lean"),
    ("names/cauchy.md", "../../../lean/OAI/No/Such/Module.lean", "lean-file"),
    ("names/cauchy.md", "../../../lean/OAI/No/Such/", "lean-dir"),
    ("names/cauchy.md", "../../../lean/docs/999.md", "scope-note"),
    ("names/cauchy.md", "../../../reasoning_traces/no-such-trace.pdf", "trace"),
    ("names/cauchy.md", "../../../nope/thing.lean", "release-surface"),
    ("differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md",
     "../../../preprints/No-Such-Manuscript/build/", "latex-build-tree"),
    ("differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md",
     "../../../preprints/No-Such-Manuscript/verification/", "verification-dir"),
    ("differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md",
     "../../../preprints/No-Such-Manuscript/README.md", "manuscript-readme"),
    ("differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md",
     "../../../preprints/No-Such-Manuscript/nothing.bib", "latex-bib"),
]

# Real hrefs taken from the rendered pages: a checker that flags everything is useless.
CONTROLS = [
    ("README.md", "../development/index-design.md"),
    ("README.md", "../tables/topics.tsv"),
    ("README.md", "../tables/names.tsv"),
    ("README.md", "names/"),
    ("names/cauchy.md", "../../tables/names.tsv"),
    ("names/cauchy.md", "../../../lean/docs/003.md"),
    ("differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md",
     "../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf"),
    ("differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md",
     "../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/build/"),
]

# What the classifier tags, against what is on disk: the directory set must be the directories.
CLASSIFIED = [
    ("preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/build/", "dir"),
    ("preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf", "file"),
    ("lean/docs/003.md", "file"),
    ("lean/OAI/Combinatorics", "dir"),
    ("notes/index/names/", "dir"),
    ("notes/reports/names.md", "file"),
    ("notes/tables/names.tsv", "file"),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("check_index_links")


def test_injected_hrefs_do_not_resolve(mod):
    """An injected target that exists on disk makes the test inert, so the checker would be
    reporting nothing while the self-test printed a pass."""
    inert = []
    for page, href, _cat in INPUTS:
        rel = mod.resolve(page, href)
        if (mod.ROOT / rel).exists():
            inert.append(f"{page} -> {href}: injected target resolves, the test is inert")
    assert not inert, inert
    assert len(INPUTS) == 21, f"{len(INPUTS)} injected hrefs, expected 21"


def test_injected_hrefs_classify_as_the_category_they_claim(mod):
    """A broken href must land in the category it is written to test. Three entry-point mutants
    were originally written with hrefs that left `notes/index/` and classified as `notes-doc`, so
    the mutants, not the checker, were the defect."""
    wrong = []
    for page, href, cat in INPUTS:
        rel = mod.resolve(page, href)
        if not (mod.ROOT / rel).exists() and mod.category(rel) != cat:
            wrong.append(f"{page} -> {href}: broken but classified {mod.category(rel)}, "
                         f"expected {cat}")
    assert not wrong, wrong


def test_real_hrefs_resolve(mod):
    absent = []
    for page, href in CONTROLS:
        rel = mod.resolve(page, href)
        if not (mod.ROOT / rel).exists():
            absent.append(f"{page} -> {href}: resolves to {rel}, which is absent")
    assert not absent, absent
    assert len(CONTROLS) == 8, f"{len(CONTROLS)} controls, expected 8"


def test_paren_balanced_scanner_keeps_the_cat0_path_whole(mod):
    """The path that breaks `[^)]*`: the naive pattern truncates at `(0)` and the truncated
    target does not exist, so a checker built on `[^)]*` reports a broken link that is not there.
    The baseline is 0 broken links, not 1."""
    naive, balanced = mod.trap()
    assert naive[1].endswith("CAT(0"), f"naive scan did not truncate: {naive[1]}"
    assert naive[2] is False, f"the truncated target {naive[1]!r} exists, so the trap is inert"
    assert balanced[1] == f"../../../{mod.CAT_DIR}/paper.pdf", \
        f"the balanced scan returned {balanced[1]!r}"
    assert balanced[2] is True, f"the whole path {balanced[1]!r} does not resolve"


def test_directory_categories_match_disk(mod):
    """A link that resolves to a directory is not a link to a file, so the classifier's directory
    set must be exactly the directories on disk. `notes/index/names/` was the defect the first
    self-test caught: it sits under `notes/index/` with no `.md` suffix and was tagged
    `index-table`."""
    missed = []
    for rel, expected in CLASSIFIED:
        on_disk = "dir" if (mod.ROOT / rel).is_dir() else "file"
        tagged = "dir" if mod.category(rel) in mod.DIR_CATEGORIES else "file"
        if on_disk != expected:
            missed.append(f"{rel}: on disk {on_disk}, the test expected {expected}")
        if on_disk == "dir" and tagged != "dir":
            missed.append(f"{rel}: a directory the classifier does not tag as one")
        if on_disk == "file" and tagged == "dir":
            missed.append(f"{rel}: a file the classifier tags as a directory")
    assert not missed, missed


def test_basename_collision_pass_is_nonvacuous(mod):
    """The invariant `math-faz.6` moved the 16 generated tables on: the index tree and
    `notes/tables/` share no file basename. A pass that reports 0 because one of the sets is empty
    is not a pass, so both sets are pinned and a collision is injected by handing the pass a shared
    name. `README.md` is the realistic shape: `notes/index/README.md` is the index entry point, and a
    `notes/tables/README.md` would make a bare `README.md` reference ambiguous between the trees. The
    pass is scoped to the two trees, not to the index alone: inside the index, 6 discipline names are
    also topic terms, so `disciplines/differential-geometry.md` and `topics/differential-geometry.md`
    share a basename. The pins are the resolution invariant and the floors, not recorded set sizes:
    the overlap is empty, both sets are non-empty, and the index must contain collisions — a pass that
    reports 0 collisions because the index set is empty, or because its dupe rule finds none, is not a
    pass."""
    idx = mod.basenames(mod.IDX)
    tab = mod.basenames(mod.TABLES)
    dupes = mod.basename_dupes(mod.IDX)
    assert len(idx) > 0, "the index tree contributes 0 basenames, so the overlap pass is vacuous"
    assert len(tab) > 0, "the tables tree contributes 0 basenames, so the overlap pass is vacuous"
    assert len(dupes) > 0, f"{len(dupes)} shared basenames inside the index, expected collisions"
    clean = mod.basename_overlap(idx, tab)
    assert clean == [], f"basename collisions: {clean[:3]}"
    injected = mod.basename_overlap(idx, tab | {"README.md"})
    assert injected == ["README.md"], f"injected collision read {injected}"


def test_clean_scan_baseline(mod):
    """The scan the page quotes: every link in every rendered page resolves. The pins are the
    resolution invariant, not recorded counts: every extracted link resolves to exactly one of
    directory or file, so the two counts sum to the link count and nothing is broken. The floors keep
    the scan non-vacuous — a scan over 0 pages and 0 links reports 0 broken and proves nothing."""
    m = mod.measure()
    assert len(m["pages"]) > 0, "the scan walked 0 index pages"
    assert len(m["links"]) > 0, "the scan extracted 0 links"
    assert not m["broken"], list(m["broken"][:5])
    assert m["dir_links"] + m["file_links"] == len(m["links"]), \
        f"{m['dir_links']} dir + {m['file_links']} file against {len(m['links'])} links"
    assert m["collisions"] == [], f"basename collisions: {m['collisions'][:3]}"
    assert m["contents_broken"] == [], m["contents_broken"][:5]
