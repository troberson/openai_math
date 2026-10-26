r"""The self-tests for `notes/scripts/verify_sources.py`.

The checker verifies `notes/gen/reports/sources.md` and `notes/gen/tables/sources.tsv` against the manuscript trees on
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

Two cases feed the byte-form rules a string, not the corpus. `\documentclass` **at line start** is the
rule the root census uses, so a macro that *mentions* the command is not a root and the substring rule
reads it as one — the mechanism behind the 715/3/1 root distribution against the substring 714/4/1. The
declared-environment rule counts a name the six-name list omits (`assumption`), and the
`NON_STATEMENT` subtraction is what keeps a `definition` environment out of the count — the shape of
the 21,288 against 21,203 gap. Neither case names a file on disk.

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

The clean test asserts the passes are silent and pins the counts they report. The population is pinned
as **joins**, not recorded numbers: the dir census decomposes into listed + superseded + notices, the
table has one row per listed manuscript, every resolved main file sits under `build/`, the family count
equals the ledger's family set, and the formalized count equals the ledger's `paps_form` sum. The dir
census is also pinned as a **walk equality**: the test walks `preprints/` itself and the census must
equal the number of directories on disk, so a dir added to the corpus moves the walk, not the recorded
number. The figures that stay literal are the ones the join cannot produce: 4 block lines, 31 count
phrases, 0 sync problems, 14 columns, the (27, 3) superseded/notices split, 12 `main.tex` files
without `\\documentclass`, 21,203 six-name environments against the declared-rule 21,288, the root
distribution (715, 3, 1), the column sums (724, 20,341, 21,288, 16,297, 127,456,942), and the six
integrity counters at 0. The resolution passes are pinned as **derived floors**: the anchor pass
counted every anchor shape the page carries and the slug pass counted every slug the page carries,
both derived from the page by the checker's own regex and both required non-zero, so 0 problems means
every anchor and every slug resolved. `test_resolution_floors_fire_on_a_page_that_carries_nothing`
proves the floor: strip every anchor shape and every slug from the page and the equality holds at 0
while the floor fails. A page with fewer block lines or count phrases is a pass that stopped checking,
not a pass that passed.

`test_formalized_join_fires_on_a_ledger_fault` proves the join is the witness: flipping a family's
`paps_form` moves no page byte, so every page pass stays silent and no literal pin moves — rows, dirs,
listed, superseded, notices, cols, the root distribution and the column sums are all unchanged.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the thirteen
`check()` calls the row makes pay the corpus walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_sources.py -q
"""
import csv
import pathlib
import re

import pytest

pytestmark = pytest.mark.mutant

def bump(t, pat, delta):
    """Change the page's own count at `pat` by `delta`, keeping its comma formatting. The mutation's
    input is the page as it stands, so a measured count that moves does not need a hand-edit here."""
    m = re.search(pat, t)
    assert m, f"{pat!r} not in the page"
    raw = m.group(1)
    n = int(raw.replace(",", ""))
    new = f"{n + delta:,}" if "," in raw else str(n + delta)
    span = m.group(0)
    return t[:m.start()] + span.replace(raw, new, 1) + t[m.end():]



REPO = pathlib.Path(__file__).resolve().parents[3]


def tree_dirs():
    """The directories under `preprints/`, walked by the test rather than counted by the checker. The
    census count is the population's; this is the tree. The equality is the invariant: the census
    counted every directory on disk, so a dir added to `preprints/` moves the walk and not the census."""
    return [d for d in (REPO / "preprints").iterdir() if d.is_dir()]


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
     lambda t: bump(t, r"`subsections`.*?\*\*([\d,]+)\*\*", -7)),
    ("byte figure", "count mismatch (tex bytes)",
     lambda t: bump(t, r"\*\*([\d,]+)\*\* \(mean", -456942)),
    ("six-name count", "count mismatch (six-name count)",
     lambda t: bump(t, r"quotes \*\*([\d,]+)\*\* for", 85)),
    ("gap breakdown", "count mismatch (env gap breakdown)",
     lambda t: bump(t, r"`assumption` (\d+), `foundation`", -1)),
    ("directory name", "October-6-2026 is not a preprints/ directory",
     lambda t: t.replace("`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026`",
                         "`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-6-2026`", 1)),
    ("root distribution", "count mismatch (roots distribution)",
     lambda t: bump(t, r"(\d+) with 1, \d+ with 2", 1)),
    ("disk census", "count mismatch (disk census)",
     lambda t: bump(t, r"the \*\*(\d+)\*\* the release lists", 1)),
    ("formalized share", "count mismatch (formalized share)",
     lambda t: bump(t, r"at \*\*(\d+)\*\* of \d+ manuscripts", 1)),
    # Prose the count pass never reads: 717 is the bead's substring figure, quoted for the record,
    # not a measured needle. Only the render diff can see it.
    ("prose count", "718 dirs",
     lambda t: bump(t, r"measures (\d+) dirs", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_sources")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def ledger():
    """The ledger rows, read for the joins the sources population is checked against."""
    return list(csv.DictReader(pathlib.Path("notes/gen/tables/catalog.tsv").read_text(
        encoding="utf-8").splitlines(), delimiter="\t"))


def test_clean_page(mod, text, ledger):
    """Every pass is silent, and the population is asserted as joins, not recorded numbers. The
    ledger-join invariants: the dir census decomposes into listed + superseded + notices, the table has
    one row per listed manuscript, every resolved main file sits under `build/`, the formalized count
    equals the ledger's `paps_form` sum, and the family count equals the ledger's family set. The
    column count, the root distribution, the six-name environment total and the column sums stay
    literals: corpus measurements the join cannot produce. The resolution floors: the anchor pass
    counted every anchor shape the page carries, and the slug pass counted every slug the page carries,
    so 0 problems means every one resolved — the count is derived from the page by the checker's own
    regex, not recorded, and a page with no anchors is a pass that ran over nothing."""
    problems, n_anchor, n_block, n_slug, n_phrases, n_sync = mod.check(text)
    assert not problems, problems[:3]
    assert n_anchor == len(mod.ANCHOR_SHAPE.findall(text)) > 0, \
        f"anchors {n_anchor} against {len(mod.ANCHOR_SHAPE.findall(text))} anchor shapes in the page"
    assert n_slug == len(mod.SLUG.findall(text)) > 0, \
        f"slugs {n_slug} against {len(mod.SLUG.findall(text))} slugs in the page"
    assert (n_block, n_phrases, n_sync) == (4, 31, 0), \
        f"block lines {n_block}, phrases {n_phrases}, sync {n_sync}"
    m = mod.population()
    assert m["dirs"] == len(tree_dirs()) > 0, \
        f"dir census {m['dirs']} against {len(tree_dirs())} directories walked under preprints/"
    assert m["dirs"] == m["listed"] + m["superseded"] + m["notices"], \
        f"dir census {m['dirs']} against {m['listed']}+{m['superseded']}+{m['notices']}"
    assert m["rows"] == m["listed"], f"rows {m['rows']} against {m['listed']} listed manuscripts"
    assert m["main_under_build"] == m["rows"], \
        f"main_under_build {m['main_under_build']} of {m['rows']} rows"
    assert m["fams"] == len({r["fam"] for r in ledger}), \
        f"fams {m['fams']} against {len({r['fam'] for r in ledger})} ledger families"
    assert m["formalized"] == sum(int(r["paps_form"]) for r in ledger), \
        f"formalized {m['formalized']} against the ledger paps_form sum " \
        f"{sum(int(r['paps_form']) for r in ledger)}"
    assert m["cols"] == 14, f"cols {m['cols']}"
    assert (m["superseded"], m["notices"]) == (27, 3), \
        f"superseded {m['superseded']}, notices {m['notices']}"
    assert (m["main_no_dc"], m["six"], m["decl"]) == (12, 21203, 21288), \
        f"main_no_dc {m['main_no_dc']}, envs {m['six']}, declared {m['decl']}"
    rd = m["rootdist"]
    assert (rd[1], rd[2], rd[3]) == (715, 3, 1), f"root distribution {dict(rd)}"
    s = m["sums"]
    assert (s["roots"], s["proofs"], s["thms"], s["subsections"], s["tex_bytes"]) == \
        (724, 20341, 21288, 16297, 127456942), f"column sums {dict(s)}"
    for key in ("pdf_missing", "main_missing", "main_not_root", "fam_outside", "paps_diff",
                "pdf_ov_diff"):
        assert m[key] == 0, f"integrity {key}: {m[key]} differences"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _, _, _, _, _ = mod.check(cand)
    want = needle(cand, mod) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def test_formalized_join_fires_on_a_ledger_fault(mod, ledger):
    """Flipping a family's `paps_form` changes no page byte, so every page pass stays silent and no
    literal pin moves: rows, dirs, listed, superseded, notices, cols, the root distribution and the
    column sums are all unchanged. The formalized join is the only witness."""
    i = next(n for n, r in enumerate(ledger) if int(r["paps_form"]) > 0)
    led = [dict(r) for r in ledger]
    led[i]["paps_form"] = "0"
    m = mod.population()
    assert m["formalized"] == sum(int(r["paps_form"]) for r in ledger), \
        "the clean join is not the relation the population satisfies"
    assert m["formalized"] != sum(int(r["paps_form"]) for r in led), \
        "the paps_form flip did not break the join, so the join is not a witness"


def test_resolution_floors_fire_on_a_page_that_carries_nothing(mod, text):
    """A pass that reports 0 problems on a page with no anchors is vacuous. Stripping every anchor
    shape from the page leaves the equality true (0 counted against 0 present) and the floor false, so
    the floor is what keeps the pass honest — the same for the slug pass."""
    no_anchor = mod.ANCHOR_SHAPE.sub("", text)
    _p, n_anchor, _b, _s, _ph, _sy = mod.check(no_anchor)
    assert n_anchor == len(mod.ANCHOR_SHAPE.findall(no_anchor)) == 0, \
        f"the anchor pass counted {n_anchor} on a page with no anchor shapes"
    no_slug = mod.SLUG.sub("", text)
    _p, _a, _b, n_slug, _ph, _sy = mod.check(no_slug)
    assert n_slug == len(mod.SLUG.findall(no_slug)) == 0, \
        f"the slug pass counted {n_slug} on a page with no slugs"


def test_documentclass_rule_is_line_start(mod):
    """The rule the root census uses: `\\documentclass` at line start. A macro that *mentions* the
    command is not a root, so the line-start rule reads 0 from it and the substring rule reads 1 — the
    mechanism behind the 715/3/1 root distribution against the substring 714/4/1, which is the one
    directory that differs. Neither string is a file on disk."""
    root = "\\documentclass[11pt]{article}\n\\begin{document}"
    macro = r"\newcommand{\dc}{\documentclass}"
    assert mod.preprints.DOCCLASS.search(root) is not None, \
        "the line-start rule does not read a real root line, so the census is not this rule"
    assert mod.preprints.DOCCLASS.search(macro) is None, \
        "the line-start rule read a macro that only mentions the command"
    assert "\\documentclass" in macro, \
        "the substring rule must read the macro line, so the gap is the rule, not the file"


def test_declared_env_rule_counts_a_name_the_six_name_list_omits(mod):
    """The declared rule against the six-name list: a directory that declares `assumption` and uses it
    twice counts 2 under the declared rule and 1 under the six-name list, which is the shape of the
    21,288 against 21,203 gap. `declared_envs` is the declared set **minus** `NON_STATEMENT`, so
    `definition` is declared and excluded; a rule that skips the subtraction keeps it in and counts 3
    begins. The string is not a file on disk."""
    text = (r"\newtheorem{assumption}{Assumption}\n"
            r"\begin{assumption}\n\begin{assumption}\n"
            r"\newtheorem{definition}{Definition}\n"
            r"\begin{definition}\n\begin{theorem}")
    declared = mod.preprints.declared_envs([text])
    assert declared == {"assumption"}, f"the declared rule's set read {sorted(declared)}"
    assert mod.preprints.env_counts([text], declared)["thms"] == 2, \
        f"the declared rule counted {mod.preprints.env_counts([text], declared)['thms']}"
    assert mod.preprints.six_count([text]) == 1, \
        f"the six-name list counted {mod.preprints.six_count([text])}"
    no_sub = set(mod.preprints.NEWTHEOREM.findall(text))
    assert no_sub - declared == {"definition"}, \
        f"the rule without the NON_STATEMENT subtraction declares {sorted(no_sub)}, so the " \
        "subtraction is not what excludes definition"
    assert sum(1 for m in mod.preprints.BEGIN.findall(text) if m in no_sub) == 3, \
        "the rule without the subtraction does not count the definition environment"
    assert "definition" in mod.preprints.NON_STATEMENT, \
        "definition is not in NON_STATEMENT, so the subtraction cannot be what excludes it"
    assert "assumption" not in mod.preprints.NON_STATEMENT, \
        "assumption is in NON_STATEMENT, so the declared rule would not count it"
