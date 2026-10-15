"""The self-tests for `notes/scripts/verify_fleet_design.py`.

The checker verifies `notes/development/fleet-design.md` against the fleet it describes. Anchors: every
backticked `path:line` (or `path:a-b`) resolves against the file, a prefixed path under the repo
root, a bare script name under `notes/scripts/`, and a span fits inside the file. Counts: every
count phrase is re-derived by running the command the page names — the atomicity grep, the
sync-pass grep, the tree-digest `git rev-parse`, the `--ignored=matching` check, the TSV byte sum,
the three `du -sk` sizes, the gate row count, the three site counts, and the probe parse. Site
anchors: the atomicity paragraph, the env bullet, the set-iteration bullet and the checker-section
anchor list must each name exactly their measured `name:line` set — the count pass proves only the
count and the anchor pass only that the line exists, so a site shifted to a neighbouring line
passes both and only this comparison catches it. Tables: the purity table equals the probe parse,
scanned inside the purity section, and each amplification row is present. Sync: the page bytes
against `render_reports.py`'s render of it.

This file injects twenty faults, one per check form the page uses, and asserts each fires the pass
that owns it: the atomicity count, the sync split, a deleted purity row, the purity heading count,
the digest count, a probe figure, an anchor past the file's end, a notes-page anchor past the
file's end, the TSV byte figure, the TSV file count, the probe-record count, the writer-row count in
the gate paragraph, the writer-row count in the non-determinism sentence, and six site anchors shifted
by one line — two in the bullet, two in the checker list, two in the paragraph. The last is a dated
observation the writer deliberately leaves literal, so only the render diff can catch it.

**The needles that name a measured figure are derived at run time, not recorded.** The count needles
are rebuilt from the checker's own `population()` dict, the site needles from the paragraph the
checker scans in the mutated page plus the measured site set, the purity needle from the mutated
page's own table rows against the probe parse, and the render needle from the mutated page's line
number and the clip the render diff prints. The needles that stay literal are the mutation's own
inputs — the anchor line written past the file's end, the injected notes-page anchor, the dated
observation's new value.

Every fault is built from a real count phrase, a real probe figure, a real anchor, a real table row
and a real site anchor in the page as committed. Each test asserts the injected text differs from the
page it started from, and each needle is the problem string the pass that owns that form prints —
measured specific, each needle fires for its own fault and for no other. The render-diff line fires
for every fault, so no needle is that line.

The clean test asserts the passes are silent and pins the counts they report: 32 anchors, 24 count
and probe phrases, 0 sync problems, 2 atomicity matches over 67 scripts and 18 catlib modules, 12
sync scripts all `verify_*`, 5 tree digests, 1 ignored line, 25 TSVs at 2,408,089 bytes, 631M
`preprints/`, 1,740M `lean/OAI/`, 12M `notes/index/`, 79 gate rows, 11 writer rows, 1 env hit, 8
purity scripts,
the sites at `atomic.py:42` / `atomic.py:84`, `render_reports.py:1180`
and `build_catalog.py:128` / `build_index.py:591`, and the probe row the amplification table quotes
at 151.32 s wall over 117,360 opens, 18,935 distinct paths and 98,425 repeats. A page with fewer
anchors or phrases is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the
twenty-one `check()` calls the row makes pay the `git`/`du`/script-tree walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_fleet_design.py -q
"""
import pathlib
import re

import pytest

pytestmark = pytest.mark.mutant


def row_of(c, sub):
    """The 1-based page line carrying `sub`; a sub on two lines makes the needle ambiguous."""
    lines = c.split("\n")
    hits = [i + 1 for i, line in enumerate(lines) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


def render_needle(c, sub):
    """The render-diff sample line for the mutated line: the page's 1-based line number and the clip
    the diff prints for it, both read from the mutated page."""
    n = row_of(c, sub)
    line = c.split("\n")[n - 1]
    clip = repr(line if len(line) <= 80 else line[:80] + "…")
    return f"page line {n}: page {clip}"


def purity_needle(c, _mod, p):
    """The purity-table problem for the mutated page: its rows, scanned inside the purity section as
    the checker scans them, against the probe parse."""
    sec = re.search(r"## The purity population.*?(?=\n## )", c, re.DOTALL)
    assert sec, "purity section absent from the mutated page"
    rows = re.findall(r"^\|\s*`([^`]+\.py)`\s*\|", sec.group(0), re.MULTILINE)
    want = [s for s, _, _ in p["purity"]]
    return f"purity table rows {sorted(rows)} != population {sorted(want)}"


def site_needle(c, mod, pat, label, sites):
    """The site-paragraph problem for the mutated page: the anchors that paragraph names, read out of
    the mutated page, against the measured site set."""
    sec = pat.search(c)
    assert sec, f"{label} absent from the mutated page"
    named = sorted(f"{mod.norm(m.group(1))}:{m.group(2)}" for m in mod.ANCHOR.finditer(sec.group(0)))
    return f"{label} names {named}, measured {sites}"


def missing_site_needle(c, mod, sites):
    """The checker-section problem for the mutated page: the measured site the anchor paragraph no
    longer carries. One site per fault, so the derivation names exactly one."""
    four = mod.ANCHORS_PARA.search(c)
    assert four, "checker-section anchors paragraph absent from the mutated page"
    listed = {f"{mod.norm(m.group(1))}:{m.group(2)}" for m in mod.ANCHOR.finditer(four.group(0))}
    miss = [s for s in sites if s not in listed]
    assert len(miss) == 1, f"{len(miss)} measured sites absent from the checker paragraph"
    return f"site {miss[0]} absent"


# (label, needle, mutation). A needle is a function of the mutated page, the loaded checker and the
# measured population; a mutation is a function of the page.
MUTANTS = [
    ("atomicity count shifted",
     lambda c, mod, p: (f"count phrase not in the page: **{p['atomic']} "
                        f"match{'es' if p['atomic'] != 1 else ''}**"),
     lambda t: t.replace("**2 matches**", "**1 match**", 1)),
    ("sync split altered",
     lambda c, mod, p: f"count phrase not in the page: **{p['sync_verify']}** are `verify_*`",
     lambda t: t.replace("**12** are `verify_*`", "**11** are `verify_*`", 1)),
    ("purity row deleted", purity_needle,
     lambda t: re.sub(r"^\|\s*`check_index_links\.py`.*\n", "", t, count=1, flags=re.MULTILINE)),
    # The purity heading count is the probe parse, so a page that names one target it does not
    # measure is caught by the count pass, not by the row scan.
    ("purity population count altered",
     lambda c, mod, p: (f"count phrase not in the page: ## The purity population "
                        f"({len(p['purity'])} scripts, mode-verified)"),
     lambda t: t.replace("## The purity population (8 scripts",
                         "## The purity population (7 scripts", 1)),
    ("digest count widened",
     lambda c, mod, p: f"count phrase not in the page: **{p['digests']}** digests",
     lambda t: t.replace("**5** digests", "**6** digests", 1)),
    ("probe figure altered",
     lambda c, mod, p: (f"probe figure not in the page: opens "
                        f"{p['rows']['render_reports.py']['opens']:,}"),
     lambda t: t.replace("117,360", "117,361")),
    # The site anchors moved when the writer gained the basename slots: the env site is the single
    # 1180, so each env fault shifts it to its neighbour. The two anchor-outside faults move an anchor
    # that is **not** a measured site (`render_reports.py:2043`, whose first occurrence is the
    # non-determinism paragraph), so the site comparison stays silent and the anchor pass is the only
    # pass that fires. The line is past the file's end (4,000 against a 3,664-line file).
    ("anchor outside the file", "anchor line outside file: `render_reports.py:4000`",
     lambda t: t.replace("render_reports.py:2043", "render_reports.py:4000", 1)),
    # The page ships no notes-page anchor, so the resolver's notes/ branch is inert on a clean page.
    # This fault injects one with a line past the file's end, in the same paragraph, which is the only
    # way the branch is proven to fire.
    ("notes-page anchor outside the file", "anchor line outside file: `notes/development/fleet-design.md:9999`",
     lambda t: t.replace("`render_reports.py:2043`",
                         "`render_reports.py:2043` `notes/development/fleet-design.md:9999`", 1)),
    ("prose count in the size argument",
     lambda c, mod, p: f"count phrase not in the page: **{p['tsv_bytes']:,}** bytes",
     lambda t: t.replace("**2,408,089** bytes", "**2,233,627** bytes", 1)),
    # The TSV count is measured from the fleet's own tree, but the L2 row that carries it is literal
    # template text, not a slot, so the count pass never reads it: the needle is the page line the
    # render diff names. The tree carries 25 TSVs since `math-faz.6` moved the 16 generated tables
    # into it.
    ("TSV count understated",
     lambda c, mod, p: render_needle(c, "**24** `notes/tables/*.tsv` present on disk"),
     lambda t: t.replace("**25** `notes/tables/*.tsv` present on disk",
                         "**24** `notes/tables/*.tsv` present on disk", 1)),
    # The probe-record count is measured from the tracked record tree, so a page that names a record
    # the tree does not carry is caught by the count pass.
    ("probe record count understated",
     lambda c, mod, p: (f"count phrase not in the page: The tracked records are "
                        f"**{p['probe_records']}**:"),
     lambda t: t.replace("The tracked records are **30**:", "The tracked records are **15**:", 1)),
    ("writer-row count in the gate paragraph",
     lambda c, mod, p: (f"count phrase not in the page: the **{p['writer_rows']}** writers "
                        "declare what they write"),
     lambda t: t.replace("the **11** writers declare what they write",
                         "the **10** writers declare what they write", 1)),
    ("writer-row count in the non-determinism sentence",
     lambda c, mod, p: (f"count phrase not in the page: Non-determinism sources in the "
                        f"**{p['writer_rows']}** writers, by class:"),
     lambda t: t.replace("Non-determinism sources in the **11** writers",
                         "Non-determinism sources in the **9** writers", 1)),
    # A measured site shifted to a line that exists in its file passes the anchor pass and the count
    # pass, so only the site comparison can catch it. One fault per list the comparison reads.
    ("set-site anchor shifted in the bullet",
     lambda c, mod, p: site_needle(c, mod, mod.SET_BULLET, "set-iteration bullet", sorted(p["set_sites"])),
     lambda t: t.replace("build_index.py:591", "build_index.py:592", 1)),
    ("set-site anchor shifted in the checker list",
     lambda c, mod, p: missing_site_needle(c, mod, sorted(p["set_sites"])),
     lambda t: t.replace("`build_index.py:591`, `render_reports.py:1180`",
                         "`build_index.py:592`, `render_reports.py:1180`", 1)),
    ("atomicity anchor shifted in the paragraph",
     lambda c, mod, p: site_needle(c, mod, mod.ATOMIC_PARA, "atomicity paragraph",
                                   sorted(p["atomic_sites"])),
     lambda t: t.replace("catlib/atomic.py:42", "catlib/atomic.py:43", 1)),
    ("atomicity anchor shifted in the checker list",
     lambda c, mod, p: missing_site_needle(c, mod, sorted(p["atomic_sites"])),
     lambda t: t.replace("`catlib/atomic.py:42`, `catlib/atomic.py:84`",
                         "`catlib/atomic.py:43`, `catlib/atomic.py:84`", 1)),
    ("env anchor shifted in the bullet",
     lambda c, mod, p: site_needle(c, mod, mod.ENV_BULLET, "env bullet", sorted(p["env_sites"])),
     lambda t: t.replace("`render_reports.py:1180` sets", "`render_reports.py:1185` sets", 1)),
    ("env anchor shifted in the checker list",
     lambda c, mod, p: missing_site_needle(c, mod, sorted(p["env_sites"])),
     lambda t: t.replace("`render_reports.py:1180`, `render_reports.py:2043`",
                         "`render_reports.py:1185`, `render_reports.py:2043`", 1)),
    # A dated observation the writer deliberately does not slot. The count pass, the anchor pass and
    # the site pass all ignore it, so only the render diff can see the page is no longer the writer's
    # bytes — which is the pass this page gained when it became report-fed.
    ("dated observation altered in the page", "**10 of 15**",
     lambda t: t.replace("**11 of 15**", "**10 of 15**", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_fleet_design")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, n_anchor, n_phrases, n_sync = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_phrases, n_sync) == (32, 24, 0), \
        f"anchors {n_anchor}, phrases {n_phrases}, sync {n_sync}"
    p = mod.population()
    modules = len(list(pathlib.Path("notes/scripts/catlib").glob("*.py")))
    assert (p["atomic"], p["scripts"], p["modules"]) == (2, 67, modules), \
        f"atomic {p['atomic']}, scripts {p['scripts']}, modules {p['modules']} (walk {modules})"
    assert (p["sync"], p["sync_verify"], p["sync_other"]) == (12, 12, 0), \
        f"sync {p['sync']}, verify_ {p['sync_verify']}, not {p['sync_other']}"
    assert (p["digests"], p["ignored"], p["tsv_count"], p["tsv_bytes"]) == (5, 1, 25, 2408089), \
        f"digests {p['digests']}, ignored {p['ignored']}, tsv {p['tsv_bytes']}"
    assert (p["du"]["preprints"], p["du"]["oai"], p["du"]["index"]) == (631, 1740, 12), \
        f"du {p['du']}"
    assert (p["gate_rows"], p["writer_rows"], p["env_hits"], len(p["purity"])) == (79, 11, 1, 8), (
        f"gate rows {p['gate_rows']}, writer rows {p['writer_rows']}, env hits {p['env_hits']}, "
        f"purity {len(p['purity'])}")
    assert sorted(p["atomic_sites"]) == ["atomic.py:42", "atomic.py:84"], p["atomic_sites"]
    assert sorted(p["env_sites"]) == ["render_reports.py:1180"], p["env_sites"]
    assert sorted(p["set_sites"]) == ["build_catalog.py:128", "build_index.py:591"], p["set_sites"]
    r = p["rows"]["render_reports.py"]
    assert (r["wall"], r["opens"], r["distinct"], r["repeats"]) == (151.32, 117360, 18935, 98425), \
        f"probe row {r}"
    assert p["cli_wall"] == 1.23, f"check_index_links wall {p['cli_wall']}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _, _, _ = mod.check(cand)
    p = mod.population()
    want = needle(cand, mod, p) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def pad_cells(t):
    """Pad every table cell with two spaces. The purity row pattern (`verify_fleet_design.py:362`)
    allows whitespace around the script cell, so padding must read the same 8 rows. The page is
    report-fed, so padding always breaks the render diff; `check()` appends the sync problems last, so
    the criterion is the non-sync problem list, and the sync count must rise."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod, text):
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    clean_problems, _a, _p, clean_sync = mod.check(text)
    pad_problems, _a, _p, pad_sync = mod.check(cand)
    assert pad_problems[:len(pad_problems) - pad_sync] == \
        clean_problems[:len(clean_problems) - clean_sync], \
        f"padded page reports non-sync problems {pad_problems[:len(pad_problems) - pad_sync]}, " \
        f"clean page {clean_problems[:len(clean_problems) - clean_sync]}"
    assert pad_sync > clean_sync, "padding did not change the bytes the render diff compares"
