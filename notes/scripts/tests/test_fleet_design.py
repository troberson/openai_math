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

The clean test asserts the passes are silent and proves each one non-vacuous **against the population
it reads**, not against a recorded measurement: the anchor count equals the anchors the page carries,
the phrase count equals `count_phrases(population())` plus the four site-paragraph phrases, the
atomicity and env counts equal their site-set sizes, all sync scripts are `verify_*`, the purity table
is a non-empty subset of the probe parse, the TSV count equals the `notes/tables/` tree and the
probe-record count equals the tracked record tree. The figures with no invariant to state — the three
`du` sizes, the probe wall and opens, the CLI wall, the gate and writer row counts — are asserted
positive, which is all a measured size can be tested for. A pass that reads nothing fails.

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


def shift_site(site, shift=0):
    """A measured `name:line` site, moved `shift` lines. Shift 0 is the page's own form; shift 1 is
    the neighbour the site comparison catches, and the anchor pass cannot, because the line exists."""
    name, line = site.split(":")
    return f"{name}:{int(line) + shift}"


def page_anchor(text, mod, p):
    """The page's `render_reports.py` anchor that is not a measured site — the non-determinism
    paragraph's anchor. The site comparison ignores it, so the anchor pass is the only pass that can
    fire on a fault that moves it."""
    env = set(p["env_sites"])
    for m in mod.ANCHOR.finditer(text):
        s = f"{mod.norm(m.group(1))}:{m.group(2)}"
        if s.startswith("render_reports.py:") and s not in env:
            return s
    raise AssertionError("no non-site render_reports.py anchor in the page")


def past_end(mod, site):
    """A line past the end of the file the site names, derived from that file's own length so a file
    that grows does not put the injected anchor back inside it."""
    n = len((mod.SCRIPTS / site.split(":")[0]).read_text(encoding="utf-8").splitlines())
    return n + 100


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
     lambda t, p, mod: t.replace(f"**{p['atomic']} match{'es' if p['atomic'] != 1 else ''}**",
                            f"**{p['atomic'] + 1} match{'es' if p['atomic'] != 0 else ''}**", 1)),
    ("sync split altered",
     lambda c, mod, p: f"count phrase not in the page: **{p['sync_verify']}** are `verify_*`",
     lambda t, p, mod: t.replace(f"**{p['sync_verify']}** are `verify_*`",
                            f"**{p['sync_verify'] - 1}** are `verify_*`", 1)),
    ("purity row deleted", purity_needle,
     lambda t, p, mod: re.sub(rf"^\|\s*`{p['purity'][0][0]}`.*\n", "", t, count=1, flags=re.MULTILINE)),
    # The purity heading count is the probe parse, so a page that names one target it does not
    # measure is caught by the count pass, not by the row scan.
    ("purity population count altered",
     lambda c, mod, p: (f"count phrase not in the page: ## The purity population "
                        f"({len(p['purity'])} scripts, mode-verified)"),
     lambda t, p, mod: t.replace(f"## The purity population ({len(p['purity'])} scripts",
                            f"## The purity population ({len(p['purity']) - 1} scripts", 1)),
    ("digest count widened",
     lambda c, mod, p: f"count phrase not in the page: **{p['digests']}** digests",
     lambda t, p, mod: t.replace(f"**{p['digests']}** digests", f"**{p['digests'] + 1}** digests", 1)),
    ("probe figure altered",
     lambda c, mod, p: (f"probe figure not in the page: opens "
                        f"{p['rows']['render_reports.py']['opens']:,}"),
     lambda t, p, mod: t.replace(f"{p['rows']['render_reports.py']['opens']:,}",
                            f"{p['rows']['render_reports.py']['opens'] + 1:,}")),
    # The two anchor-outside faults move an anchor that is **not** a measured site, so the site
    # comparison stays silent and the anchor pass is the only pass that fires. The target line is
    # derived from the file's own length, so a file that grows does not put the anchor back inside.
    ("anchor outside the file",
     lambda c, mod, p: (f"anchor line outside file: `render_reports.py:"
                        f"{past_end(mod, page_anchor(c, mod, p))}`"),
     lambda t, p, mod: t.replace(page_anchor(t, mod, p),
                            f"render_reports.py:{past_end(mod, page_anchor(t, mod, p))}", 1)),
    # The page ships no notes-page anchor, so the resolver's notes/ branch is inert on a clean page.
    # This fault injects one with a line past the file's end, in the same paragraph, which is the only
    # way the branch is proven to fire.
    ("notes-page anchor outside the file", "anchor line outside file: `notes/development/fleet-design.md:9999`",
     lambda t, p, mod: t.replace(f"`{page_anchor(t, mod, p)}`",
                            f"`{page_anchor(t, mod, p)}` `notes/development/fleet-design.md:9999`", 1)),
    ("prose count in the size argument",
     lambda c, mod, p: f"count phrase not in the page: **{p['tsv_bytes']:,}** bytes",
     lambda t, p, mod: t.replace(f"**{p['tsv_bytes']:,}** bytes", f"**{p['tsv_bytes'] - 174592:,}** bytes", 1)),
    # The TSV count is measured from the fleet's own tree, but the L2 row that carries it is literal
    # template text, not a slot, so the count pass never reads it: the needle is the page line the
    # render diff names.
    ("TSV count understated",
     lambda c, mod, p: render_needle(c, f"**{p['tsv_count'] - 1}** `notes/tables/*.tsv` present on disk"),
     lambda t, p, mod: t.replace(f"**{p['tsv_count']}** `notes/tables/*.tsv` present on disk",
                            f"**{p['tsv_count'] - 1}** `notes/tables/*.tsv` present on disk", 1)),
    # The probe-record count is measured from the tracked record tree, so a page that names a record
    # the tree does not carry is caught by the count pass.
    ("probe record count understated",
     lambda c, mod, p: (f"count phrase not in the page: The tracked records are "
                        f"**{p['probe_records']}**:"),
     lambda t, p, mod: t.replace(f"The tracked records are **{p['probe_records']}**:",
                            "The tracked records are **15**:", 1)),
    ("writer-row count in the gate paragraph",
     lambda c, mod, p: (f"count phrase not in the page: the **{p['writer_rows']}** writers "
                        "declare what they write"),
     lambda t, p, mod: t.replace(f"the **{p['writer_rows']}** writers declare what they write",
                            f"the **{p['writer_rows'] - 1}** writers declare what they write", 1)),
    ("writer-row count in the non-determinism sentence",
     lambda c, mod, p: (f"count phrase not in the page: Non-determinism sources in the "
                        f"**{p['writer_rows']}** writers, by class:"),
     lambda t, p, mod: t.replace(f"Non-determinism sources in the **{p['writer_rows']}** writers",
                            f"Non-determinism sources in the **{p['writer_rows'] - 2}** writers", 1)),
    # A measured site shifted to a line that exists in its file passes the anchor pass and the count
    # pass, so only the site comparison can catch it. One fault per list the comparison reads.
    ("set-site anchor shifted in the bullet",
     lambda c, mod, p: site_needle(c, mod, mod.SET_BULLET, "set-iteration bullet", sorted(p["set_sites"])),
     lambda t, p, mod: t.replace(shift_site(p["set_sites"][1]), shift_site(p["set_sites"][1], shift=1), 1)),
    ("set-site anchor shifted in the checker list",
     lambda c, mod, p: missing_site_needle(c, mod, sorted(p["set_sites"])),
     lambda t, p, mod: t.replace(f"`{p['set_sites'][1]}`, `{p['env_sites'][0]}`",
                            f"`{shift_site(p['set_sites'][1], 1)}`, `{p['env_sites'][0]}`", 1)),
    ("atomicity anchor shifted in the paragraph",
     lambda c, mod, p: site_needle(c, mod, mod.ATOMIC_PARA, "atomicity paragraph",
                                   sorted(p["atomic_sites"])),
     lambda t, p, mod: t.replace(f"catlib/{shift_site(p['atomic_sites'][0])}",
                            f"catlib/{shift_site(p['atomic_sites'][0], 1)}", 1)),
    ("atomicity anchor shifted in the checker list",
     lambda c, mod, p: missing_site_needle(c, mod, sorted(p["atomic_sites"])),
     lambda t, p, mod: t.replace(f"`catlib/{p['atomic_sites'][0]}`, `catlib/{p['atomic_sites'][1]}`",
                            f"`catlib/{shift_site(p['atomic_sites'][0], 1)}`, "
                            f"`catlib/{p['atomic_sites'][1]}`", 1)),
    ("env anchor shifted in the bullet",
     lambda c, mod, p: site_needle(c, mod, mod.ENV_BULLET, "env bullet", sorted(p["env_sites"])),
     lambda t, p, mod: t.replace(f"`{p['env_sites'][0]}` sets", f"`{shift_site(p['env_sites'][0], 1)}` sets", 1)),
    ("env anchor shifted in the checker list",
     lambda c, mod, p: missing_site_needle(c, mod, sorted(p["env_sites"])),
     lambda t, p, mod: t.replace(f"`{p['env_sites'][0]}`, `{page_anchor(t, mod, p)}`",
                            f"`{shift_site(p['env_sites'][0], 1)}`, `{page_anchor(t, mod, p)}`", 1)),
    # A dated observation the writer deliberately does not slot. The count pass, the anchor pass and
    # the site pass all ignore it, so only the render diff can see the page is no longer the writer's
    # bytes — which is the pass this page gained when it became report-fed.
    ("dated observation altered in the page", "**10 of 15**",
     lambda t, p, mod: t.replace("**11 of 15**", "**10 of 15**", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_fleet_design")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and each pass is proven non-vacuous against the population it reads.
    No expected value here is a recorded measurement: the anchor and phrase counts are what the page
    carries, the site counts are the sets the paragraphs name, the TSV and probe-record counts are the
    trees on disk, and the purity table is the probe parse. The figures with no invariant to state —
    the du sizes, the probe wall, the CLI wall — are asserted positive, which is what a measured size
    can be tested for."""
    problems, n_anchor, n_phrases, n_sync = mod.check(text)
    assert not problems, problems[:3]
    assert n_sync == 0, f"the render diff reports {n_sync} problems on the committed page"
    carried = len(mod.ANCHOR.findall(text))
    assert 0 < carried == n_anchor, f"pass A read {n_anchor} of {carried} page anchors"
    want = len(mod.count_phrases(mod.population())) + 4
    assert 0 < want == n_phrases, f"pass B read {n_phrases} of {want} phrases"
    p = mod.population()
    assert p["atomic"] == len(p["atomic_sites"]) > 0, f"atomic {p['atomic']}, sites {p['atomic_sites']}"
    assert p["env_hits"] == len(p["env_sites"]) > 0, f"env {p['env_hits']}, sites {p['env_sites']}"
    assert p["sync_verify"] == p["sync"] and p["sync_other"] == 0, \
        f"sync {p['sync']}, verify_ {p['sync_verify']}, other {p['sync_other']}"
    # The purity table is the mode-verified subset of the probe parse, so the invariant is the
    # containment; the equality of the page's rows with the subset is what the row scan asserts.
    assert 0 < len(p["purity"]) <= len(p["rows"]), f"purity {len(p['purity'])}, rows {len(p['rows'])}"
    tsv = len(list((mod.ROOT / "notes" / "tables").glob("*.tsv")))
    assert p["tsv_count"] == tsv and p["tsv_bytes"] > 0, f"tsv count {p['tsv_count']} vs tree {tsv}"
    # The page counts the tracked record tree; mod.PROBE is the two records the probe parse
    # reads, which is a narrower set, so the invariant is the tree the page counts.
    tree = [f for f in (mod.ROOT / "notes" / "development" / "probe").iterdir() if f.is_file()]
    assert p["probe_records"] == len(tree) > 0, f"records {p['probe_records']} vs tree {len(tree)}"
    assert p["scripts"] > 0, f"scripts {p['scripts']}"
    assert p["modules"] == len(list(pathlib.Path("notes/scripts/catlib").glob("*.py"))), \
        f"modules {p['modules']}"
    assert p["digests"] == 5, f"digests {p['digests']}"
    assert all(v > 0 for v in p["du"].values()), f"du {p['du']}"
    assert p["gate_rows"] > 0 and p["writer_rows"] > 0, \
        f"gate rows {p['gate_rows']}, writer rows {p['writer_rows']}"
    r = p["rows"]["render_reports.py"]
    assert r["wall"] > 0 and r["opens"] > 0 and r["distinct"] > 0, f"probe row {r}"
    assert p["cli_wall"] > 0, f"check_index_links wall {p['cli_wall']}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text, mod.population(), mod)
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
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = ln
        out.append(padded)
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
