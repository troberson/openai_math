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

Every fault is built from a real count phrase, a real probe figure, a real anchor, a real table row
and a real site anchor in the page as committed. Each test asserts the injected text differs from
the page it started from, and each needle is the problem string the pass that owns that form prints
— measured specific, each needle fires for its own fault and for no other. The render-diff line
fires for every fault, so no needle is that line.

The clean test asserts the passes are silent and pins the counts they report: 32 anchors, 24 count
and probe phrases, 0 sync problems, 2 atomicity matches over 65 scripts and 18 catlib modules, 12
sync scripts all `verify_*`, 5 tree digests, 1 ignored line, 9 TSVs at 909,768 bytes, 631M
`preprints/`, 1,740M `lean/OAI/`, 14M `notes/index/`, 78 gate rows, 10 writer rows, 1 env hit, 8
purity scripts,
the sites at `atomic.py:42` / `atomic.py:84`, `render_reports.py:1162`
and `build_catalog.py:128` / `build_index.py:583`, and the probe row the amplification table quotes
at 151.32 s wall over 117,360 opens, 18,935 distinct paths and 98,425 repeats. A page with fewer
anchors or phrases is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the
twenty-one `check()` calls the row makes pay the `git`/`du`/script-tree walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_fleet_design.py -q
"""
import re

import pytest

pytestmark = pytest.mark.mutant

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("atomicity count shifted", "count phrase not in the page: **2 matches**",
     lambda t: t.replace("**2 matches**", "**1 match**", 1)),
    ("sync split altered", "count phrase not in the page: **12** are `verify_*`",
     lambda t: t.replace("**12** are `verify_*`", "**11** are `verify_*`", 1)),
    ("purity row deleted", "purity table rows",
     lambda t: re.sub(r"^\|\s*`check_index_links\.py`.*\n", "", t, count=1, flags=re.MULTILINE)),
    # The purity heading count is the probe parse, so a page that names one target it does not
    # measure is caught by the count pass, not by the row scan.
    ("purity population count altered",
     "count phrase not in the page: ## The purity population (8 scripts, mode-verified)",
     lambda t: t.replace("## The purity population (8 scripts",
                         "## The purity population (7 scripts", 1)),
    ("digest count widened", "count phrase not in the page: **5** digests",
     lambda t: t.replace("**5** digests", "**6** digests", 1)),
    ("probe figure altered", "probe figure not in the page: opens 117,360",
     lambda t: t.replace("117,360", "117,361")),
    # The site anchors moved when the writer's env construction collapsed into one launch site: the
    # env site is now the single 1162, so each env fault shifts it to its neighbour, and the
    # anchor-outside fault uses a line past the file's end (4,000 against a 3,664-line file), which
    # is the form the anchor pass flags.
    ("anchor outside the file", "anchor line outside file: `render_reports.py:4000`",
     lambda t: t.replace("render_reports.py:1162", "render_reports.py:4000", 1)),
    # The page ships no notes-page anchor, so the resolver's notes/ branch is inert on a clean page.
    # This fault injects one with a line past the file's end, which is the only way the branch is
    # proven to fire.
    ("notes-page anchor outside the file", "anchor line outside file: `notes/development/fleet-design.md:9999`",
     lambda t: t.replace("`render_reports.py:1162`",
                         "`render_reports.py:1162` `notes/development/fleet-design.md:9999`", 1)),
    ("prose count in the size argument", "count phrase not in the page: **909,768** bytes",
     lambda t: t.replace("**909,768** bytes", "**909,767** bytes", 1)),
    # The TSV count and the writer-row count are measured from the fleet's own tree and the ROWS block,
    # so a page that names a count the measurement contradicts is caught by the count pass.
    ("TSV count understated",
     "count phrase not in the page: **9** `notes/tables/*.tsv` present on disk",
     lambda t: t.replace("**9** `notes/tables/*.tsv` present on disk",
                         "**8** `notes/tables/*.tsv` present on disk", 1)),
    # The probe-record count is measured from the tracked record tree, so a page that names a record
    # the tree does not carry is caught by the count pass. The tree carries 10 records, so the needle
    # names 10 and the fault understates that.
    ("probe record count understated",
     "count phrase not in the page: The tracked records are **10**:",
     lambda t: t.replace("The tracked records are **10**:", "The tracked records are **9**:", 1)),
    ("writer-row count in the gate paragraph",
     "count phrase not in the page: the **10** writers declare what they write",
     lambda t: t.replace("the **10** writers declare what they write",
                         "the **9** writers declare what they write", 1)),
    ("writer-row count in the non-determinism sentence",
     "count phrase not in the page: Non-determinism sources in the **10** writers, by class:",
     lambda t: t.replace("Non-determinism sources in the **10** writers",
                         "Non-determinism sources in the **9** writers", 1)),
    # A measured site shifted to a line that exists in its file passes the anchor pass and the count
    # pass, so only the site comparison can catch it. One fault per list the comparison reads.
    ("set-site anchor shifted in the bullet",
     "set-iteration bullet names ['build_catalog.py:128', 'build_index.py:584'",
     lambda t: t.replace("build_index.py:583", "build_index.py:584", 1)),
    ("set-site anchor shifted in the checker list", "site build_index.py:583 absent",
     lambda t: t.replace("`build_index.py:583`, `render_reports.py:1162`",
                         "`build_index.py:584`, `render_reports.py:1162`", 1)),
    ("atomicity anchor shifted in the paragraph", "atomicity paragraph names ['atomic.py:43'",
     lambda t: t.replace("catlib/atomic.py:42", "catlib/atomic.py:43", 1)),
    ("atomicity anchor shifted in the checker list", "site atomic.py:42 absent",
     lambda t: t.replace("`catlib/atomic.py:42`, `catlib/atomic.py:84`",
                         "`catlib/atomic.py:43`, `catlib/atomic.py:84`", 1)),
    ("env anchor shifted in the bullet",
     "env bullet names ['render_reports.py:1163'",
     lambda t: t.replace("`render_reports.py:1162` sets", "`render_reports.py:1163` sets", 1)),
    ("env anchor shifted in the checker list", "site render_reports.py:1162 absent",
     lambda t: t.replace("`render_reports.py:1162`, `render_reports.py:2043`",
                         "`render_reports.py:1163`, `render_reports.py:2043`", 1)),
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
    assert (p["atomic"], p["scripts"], p["modules"]) == (2, 65, 18), \
        f"atomic {p['atomic']}, scripts {p['scripts']}, modules {p['modules']}"
    assert (p["sync"], p["sync_verify"], p["sync_other"]) == (12, 12, 0), \
        f"sync {p['sync']}, verify_ {p['sync_verify']}, not {p['sync_other']}"
    assert (p["digests"], p["ignored"], p["tsv_count"], p["tsv_bytes"]) == (5, 1, 9, 909768), \
        f"digests {p['digests']}, ignored {p['ignored']}, tsv {p['tsv_bytes']}"
    assert (p["du"]["preprints"], p["du"]["oai"], p["du"]["index"]) == (631, 1740, 14), \
        f"du {p['du']}"
    assert (p["gate_rows"], p["writer_rows"], p["env_hits"], len(p["purity"])) == (78, 10, 1, 8), (
        f"gate rows {p['gate_rows']}, writer rows {p['writer_rows']}, env hits {p['env_hits']}, "
        f"purity {len(p['purity'])}")
    assert sorted(p["atomic_sites"]) == ["atomic.py:42", "atomic.py:84"], p["atomic_sites"]
    assert sorted(p["env_sites"]) == ["render_reports.py:1162"], p["env_sites"]
    assert sorted(p["set_sites"]) == ["build_catalog.py:128", "build_index.py:583"], p["set_sites"]
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
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
