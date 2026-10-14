"""The self-tests for `notes/scripts/verify_sources.py`.

The checker verifies `notes/reports/sources.md` and `notes/tables/sources.tsv` against the manuscript trees on
disk. TSV integrity: 719 rows over the shipped header, every `pdf` on disk and non-empty, every
`main_tex` a file that declares `\\documentclass` at line start, every `fam` in the ledger, every
family's row count equal to the ledger `paps`, every resolved main file under `build/`, and the
`roots` distribution equal to a fresh line-start recount over the listed manuscripts. Anchors: every
backticked `path:line` names a file that exists and a line inside it, and every fenced block is
attributed to its nearest preceding anchor and matched at consecutive lines. Slugs: every backticked
manuscript directory name exists under `preprints/`. Counts: all 31 bold phrases are rebuilt from a
fresh recount — the disk census, the column sums, the main-file outcomes, the root distribution, the
six-name environment total and the per-name gap. The page is compared with `render_reports.py`'s
render of it. The checker keeps its own corpus walk: a checker that re-derived the environment counts
through the writer's record store would prove nothing about the writer.

This file injects twelve faults, one per check form the page uses, and asserts each fires the pass
that owns it: an anchor line shifted, an anchor file renamed, a block line altered, a column count, a
byte figure, the six-name count, the gap breakdown, a manuscript directory name, the root
distribution, the disk census, the formalized share, and a prose count no count phrase covers — the
last is visible only to the render diff.

**The needles that name a measured figure are derived at run time, not recorded.** The block needle is
keyed to the byte the mutation touched: the block carrying that byte is the block the pass reports, and
the reported line is the line the byte sits on. The anchor-shifted fault is keyed to the shifted anchor
for the same reason — the line the page names is **inside** the file, so the anchor pass is silent and
the block pass is what fires, attributing the block to the anchor the mutated page carries. The needles
that stay literal are the mutation's own inputs — the renamed anchor file, the renamed directory slug,
the prose figure — and the count labels, which carry no measured figure.

Every fault is built from a real anchor, a real block line, a real count phrase, a real directory slug
and a real prose line in the page as committed. Each test asserts the injected text differs from the
page it started from, and each needle is the problem string the pass that owns that form prints —
measured specific, each needle fires for its own fault and for no other. The render-diff line fires
for every fault, so no needle is that line.

The clean test asserts the passes are silent and pins the counts they report: 2 anchors, 7 slugs, 4
block lines, 31 count phrases, 0 sync problems, 719 rows over 14 columns, 749 directories on disk
(719 listed, 27 superseded, 3 withdrawal notices), 372 families, 172 formalized, 12 `main.tex` files
without `\\documentclass`, 21,203 six-name environments against the declared-rule 21,288, and the six
integrity counters at 0. A page with fewer anchors, slugs, block lines or count phrases is a pass that
stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the thirteen
`check()` calls the row makes pay the corpus walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_sources.py -q
"""
import pytest

pytestmark = pytest.mark.mutant


def row_of(c, sub):
    """The 1-based page line carrying `sub`; a sub on two lines makes the needle ambiguous."""
    lines = c.split("\n")
    hits = [i + 1 for i, line in enumerate(lines) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


def block_needle(c, mod, sub):
    """The fenced-block problem, keyed to the byte the mutation touched. The block carrying `sub` is the
    block the pass reports, and the reported line is the line `sub` sits on. The pass walks the page's
    own fences and reads the anchor in the nine lines above, so the walk is re-run here."""
    lines = c.split("\n")
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("```"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            j = i + 1
            blk = []
            while j < len(lines) and not lines[j].lstrip().startswith("```"):
                ln = lines[j]
                blk.append(ln[len(indent):] if ln.startswith(indent) and ln.strip() else ln)
                j += 1
            anchor = None
            for k in range(i - 1, max(i - 9, -1), -1):
                found = mod.ANCHOR.findall(lines[k])
                if found:
                    anchor = (found[-1][0], int(found[-1][1]))
                    break
            if anchor is not None:
                rel, at = anchor
                n = next((k for k, ln in enumerate(blk) if sub in ln), None)
                if n is None:
                    if sub not in f"{rel}:{at}":
                        i = j + 1
                        continue
                    n = 0
                src = (mod.ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
                got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
                if got != blk[n]:
                    return f"block line {n} != {rel}:{at + n}"
            i = j + 1
        else:
            i += 1
    raise AssertionError(f"no block carries {sub!r} in the mutated page")


# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("anchor line shifted",
     lambda c, mod: block_needle(c, mod, "pgfmanual-en-macros.tex:1176"),
     lambda t: t.replace("pgfmanual-en-macros.tex:1177", "pgfmanual-en-macros.tex:1176", 1)),
    ("anchor file renamed", "build/paper.yml does not exist",
     lambda t: t.replace("build/paper.tex:1", "build/paper.yml:1", 1)),
    ("block line altered",
     lambda c, mod: block_needle(c, mod, "\\def\\extractclass#1#3@{"),
     lambda t: t.replace("\\def\\extractclass#1#2@{%", "\\def\\extractclass#1#3@{%", 1)),
    ("column count", "count mismatch (subsection count)",
     lambda t: t.replace("**16,297**", "**16,290**", 1)),
    ("byte figure", "count mismatch (tex bytes)",
     lambda t: t.replace("**127,456,942**", "**127,000,000**", 1)),
    ("six-name count", "count mismatch (six-name count)",
     lambda t: t.replace("quotes **21,203** for", "quotes **21,288** for", 1)),
    ("gap breakdown", "count mismatch (env gap breakdown)",
     lambda t: t.replace("`assumption` 22, `foundation` 13", "`assumption` 21, `foundation` 13", 1)),
    ("directory name", "October-6-2026 is not a preprints/ directory",
     lambda t: t.replace("`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026`",
                         "`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-6-2026`", 1)),
    ("root distribution", "count mismatch (roots distribution)",
     lambda t: t.replace("715 with 1, 3 with 2, 1 with 3", "716 with 1, 2 with 2, 1 with 3", 1)),
    ("disk census", "count mismatch (disk census)",
     lambda t: t.replace("the **719** the release lists", "the **720** the release lists", 1)),
    ("formalized share", "count mismatch (formalized share)",
     lambda t: t.replace("at **172** of 719 manuscripts", "at **173** of 719 manuscripts", 1)),
    # Prose the count pass never reads: 717 is the bead's substring figure, quoted for the record,
    # not a measured needle. Only the render diff can see it.
    ("prose count", "718 dirs",
     lambda t: t.replace("measures 717 dirs", "measures 718 dirs", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_sources")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, n_anchor, n_block, n_slug, n_phrases, n_sync = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_slug, n_block, n_phrases, n_sync) == (2, 7, 4, 31, 0), \
        f"anchors {n_anchor}, slugs {n_slug}, block lines {n_block}, phrases {n_phrases}, sync {n_sync}"
    m = mod.population()
    assert (m["rows"], m["cols"], m["dirs"], m["listed"], m["superseded"], m["notices"]) == \
        (719, 14, 749, 719, 27, 3), f"rows {m['rows']}, cols {m['cols']}, dirs {m['dirs']}"
    assert (m["fams"], m["formalized"], m["main_no_dc"], m["six"], m["decl"]) == \
        (372, 172, 12, 21203, 21288), f"fams {m['fams']}, formalized {m['formalized']}, envs {m['six']}"
    rd = m["rootdist"]
    assert (rd[1], rd[2], rd[3]) == (715, 3, 1), f"root distribution {dict(rd)}"
    s = m["sums"]
    assert (s["roots"], s["proofs"], s["thms"], s["subsections"], s["tex_bytes"]) == \
        (724, 20341, 21288, 16297, 127456942), f"column sums {dict(s)}"
    for key in ("pdf_missing", "main_missing", "main_not_root", "fam_outside", "paps_diff",
                "pdf_ov_diff"):
        assert m[key] == 0, f"integrity {key}: {m[key]} differences"
    assert m["main_under_build"] == 719, f"main_under_build {m['main_under_build']} of 719"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _, _, _, _, _ = mod.check(cand)
    want = needle(cand, mod) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"
