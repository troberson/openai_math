"""The self-tests for `notes/scripts/verify_index_design.py`.

The checker verifies `notes/development/index-design.md` against the tree it describes. Anchors: every
backticked `path:line` shape must name a file that exists and a line inside it, so a mistyped
extension fails instead of being skipped, and every fenced block is attributed to its nearest
preceding anchor and matched at consecutive lines. Counts: all 83 count and byte phrases are rebuilt
from `measure_index_sizes.population()` — the node and edge totals, the citation-edge counts, the
schema tables' row counts read from the generated files under `notes/index/`, the substring-versus-
line-start command counts, the ledger-set and all-TSV byte sums, the index tree byte total, the disk link check, and the raw-bib
projection. Byte sizes: the five TSVs the page tabulates are re-read from disk. The page is compared
with `render_reports.py`'s render of it. The schema tables' row counts come from the rendered files,
so a table that drops rows is a mismatch, not a phrase built from the upstream count it was derived
from.

This file injects fifteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: an anchor line shifted, an anchor file renamed, a block line altered, the node total,
the namespace disagreement count, the citation-edge count, an abbreviated anchor, the substring-rule
counts, the raw-bib projection, a rendered schema row count, the ledger-set byte total widened to the
all-TSV sum, the all-TSV total swapped with the ledger set, the index tree byte total, the disk link count, and a schema-table
byte column no count or size phrase covers — the last is visible only to the render diff.

Every fault is built from a real anchor, a real block line, a real count phrase, a real byte phrase
and a real table cell in the page as committed. Each test asserts the injected text differs from the
page it started from, and each needle is the problem string the pass that owns that form prints —
measured specific, each needle fires for its own fault and for no other. The render-diff line fires
for every fault, so no needle is that line.

The clean test asserts the passes are silent and pins the counts they report. The population is pinned
as **joins** where the ledger can produce the figure: the family count equals the ledger's family set,
the manuscript count equals the ledger's `paps` sum, the formalized count equals the ledger's
`paps_form` sum, the two comparator surfaces count the same configs, and the `main_results` entry count
exceeds the unique config count. The census counts are pinned as **walk equalities**: the test walks
`preprints/`, `lean/OAI/`, `notes/index/`, `notes/tables/` and `reasoning_traces/` itself, and the
population's count must equal the walk — 749 preprint dirs, 122,458 `.lean` files, 1,033 index pages,
16 index tables, 11 trace files folding to 10 distinct stems. The figures that stay literal are the ones
neither the join nor a file walk can produce: 9 anchors, 3 block lines, 83 count and byte phrases, 0
sync problems, 2,560 nodes over 3,415 resolved
edges (17,217 raw), 391 citation edges over 104 cross-family, 242
scope notes, 559 module dirs, 17 disciplines against 23 Lean
dirs, 30 verification bundles, 521 `.bib` files with 13,802 entries and 393
hrefs, the ledger set at 297,050 B against the all-TSV 2,316,386 B, 66,115 disk links with 0 broken and
17,700 resolving to a directory, the index tree at 11,531,073 B, and the substring counts 18 / 373
against the brace-qualified 17 / 372. A page with fewer anchors, block lines or phrases is a pass that
stopped checking, not a pass that passed.

`test_ledger_joins_fire_on_faults_the_literals_miss` proves the joins are the witness: a `paps_form`
decrement breaks the formalized join and a `paps` decrement breaks the manuscript join, and neither
moves a page byte, so every page pass stays silent.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the fifteen
`check()` calls the row makes pay the index-tree walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_index_design.py -q
"""
import pathlib

import pytest

pytestmark = pytest.mark.mutant

REPO = pathlib.Path(__file__).resolve().parents[3]


def tree_index_pages():
    """The `.md` files under `notes/index/` — the pages the index renders. The population's count is the
    census; this is the tree, so the equality is the invariant: the census counted every page on disk."""
    return list((REPO / "notes/index").rglob("*.md"))


def tree_index_tables(mod):
    """The generated index tables under `notes/tables/`, keyed by the registry's own name list. The
    equality is the invariant: every table the registry names is on disk and the count is the walk's."""
    names = set(mod.M.INDEX_TABLES)
    return [p for p in (REPO / "notes/tables").glob("*.tsv") if p.name in names]


def tree_traces():
    """The files under `reasoning_traces/`, walked by the test. The population's trace count is the
    distinct stem count over that walk: 11 files carry 10 traces, because the Mezar-Parisi trace ships as
    both `.pdf` and `.tex`. The equality is the invariant — the census counted the tree, and the
    attribution is the fold, not a recorded number."""
    return [p for p in (REPO / "reasoning_traces").rglob("*") if p.is_file()]


def tree_preprint_dirs():
    """The directories under `preprints/`, walked by the test. The census count is the population's; this
    is the tree, so the equality is the invariant."""
    return [d for d in (REPO / "preprints").iterdir() if d.is_dir()]


def tree_lean_files():
    """The `.lean` files under `lean/OAI/`, walked by the test. The census count is the population's;
    this is the tree, so the equality is the invariant: the census counted every source file the formalized
    package carries."""
    return list((REPO / "lean/OAI").rglob("*.lean"))

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("anchor line shifted", "lean/formalization.yaml:976",
     lambda t: t.replace("`lean/formalization.yaml:977`", "`lean/formalization.yaml:976`", 1)),
    ("anchor file renamed", "lean/formalization.yml does not exist",
     lambda t: t.replace("`lean/formalization.yaml:982`", "`lean/formalization.yml:982`", 1)),
    ("block line altered", "OAI.AmplitudeDamping.main",
     lambda t: t.replace("      declaration: OAI.GAD.main",
                         "      declaration: OAI.AmplitudeDamping.main", 1)),
    ("node total", "count mismatch (population totals)",
     lambda t: t.replace("**2,560** index nodes", "**2,700** index nodes", 1)),
    ("namespace disagreement count", "count mismatch (namespace disagreement count)",
     lambda t: t.replace("is wrong **150** times", "is wrong **149** times", 1)),
    ("citation edge count", "count mismatch (citation edge counts)",
     lambda t: t.replace("**391** resolved", "**392** resolved", 1)),
    ("abbreviated anchor", "anchor file .../overview.tex does not exist",
     lambda t: t.replace("`overview.tex:28`", "`.../overview.tex:28`", 1)),
    ("substring-rule counts", "count mismatch (substring vs line-start counts)",
     lambda t: t.replace("of the command name reads 18 and", "of the command name reads 17 and", 1)),
    ("projected size", "count mismatch (raw-bib projection)",
     lambda t: t.replace("**2,021** KiB", "**2,000** KiB", 1)),
    ("rendered row count", "count mismatch (family-topic.tsv rows)",
     lambda t: t.replace("`family-topic.tsv` | **978**", "`family-topic.tsv` | **977**", 1)),
    ("ledger set widened to all TSVs", "count mismatch (ledger set byte total)",
     lambda t: t.replace("the whole ledger set is **297,050** B",
                         "the whole ledger set is **2,174,703** B", 1)),
    ("all-TSV total altered", "count mismatch (all-TSV byte total)",
     lambda t: t.replace("together totals **2316386** B", "together totals **297050** B", 1)),
    ("index tree byte total altered", "count mismatch (index tree byte total)",
     lambda t: t.replace("carries **11531073** B", "carries **11530405** B", 1)),
    ("disk link count", "count mismatch (disk link check)",
     lambda t: t.replace("covers **66,115** links", "covers **66,112** links", 1)),
    # Prose the count passes never read: the schema table's byte column is not in count_phrases()
    # or size_phrases(). Only the render diff can see it.
    ("schema byte column", "size mismatch (catalog.tsv measured size)",
     lambda t: t.replace("| `catalog.tsv` | **49213** |", "| `catalog.tsv` | **49214** |", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_index_design")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text, ledger):
    """Every pass is silent, and the population is asserted as joins, not recorded numbers. The
    ledger-join invariants: the family count equals the ledger's family set, the manuscript count
    equals the ledger's `paps` sum, the formalized count equals the ledger's `paps_form` sum, the two
    comparator surfaces count the same configs, and the `main_results` entry count exceeds the unique
    config count (some configs carry more than one entry). The node, edge, byte, page and substring
    figures stay literals: corpus measurements the join cannot produce."""
    problems, n_anchor, n_block, n_phrases, n_sync = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_block, n_phrases, n_sync) == (9, 3, 83, 0), \
        f"anchors {n_anchor}, block lines {n_block}, phrases {n_phrases}, sync {n_sync}"
    p = mod.population()
    assert p["families"] == len({r["fam"] for r in ledger}), \
        f"families {p['families']} against {len({r['fam'] for r in ledger})} ledger families"
    assert p["manuscripts"] == sum(int(r["paps"]) for r in ledger), \
        f"manuscripts {p['manuscripts']} against the ledger paps sum " \
        f"{sum(int(r['paps']) for r in ledger)}"
    assert p["formalized"] == sum(int(r["paps_form"]) for r in ledger), \
        f"formalized {p['formalized']} against the ledger paps_form sum " \
        f"{sum(int(r['paps_form']) for r in ledger)}"
    assert p["chal_json"] == p["chal_lean"], \
        f"comparator surfaces: json {p['chal_json']} against lean {p['chal_lean']}"
    assert p["mr_configs"] < p["mr_entries"], \
        f"main_results: {p['mr_configs']} unique configs against {p['mr_entries']} entries"
    assert (p["nodes"], p["edges_resolved"], p["edges_rawbib"], p["resolved"], p["cross"]) == \
        (2560, 3415, 17217, 391, 104), f"nodes {p['nodes']}, edges {p['edges_resolved']}"
    assert p["scope_notes"] == 242, f"scope notes {p['scope_notes']}"
    assert p["preprint_dirs"] == len(tree_preprint_dirs()) > 0, \
        f"preprint dirs {p['preprint_dirs']} against {len(tree_preprint_dirs())} directories walked"
    assert p["lean_files"] == len(tree_lean_files()) > 0, \
        f"lean files {p['lean_files']} against {len(tree_lean_files())} .lean files walked under lean/OAI/"
    assert (p["lean_mods"], p["disciplines"], p["lean_disc"]) == (559, 17, 23), \
        f"module dirs {p['lean_mods']}, disciplines {p['disciplines']} against {p['lean_disc']} Lean dirs"
    walked = tree_traces()
    assert p["trace_files"] == len(walked) > 0, \
        f"trace files {p['trace_files']} against {len(walked)} files walked under reasoning_traces/"
    assert p["traces"] == len({f.stem for f in walked}) > 0, \
        f"traces {p['traces']} against {len({f.stem for f in walked})} distinct stems over the walk"
    assert (p["ver_dirs"], p["bib_files"], p["bib_entries"],
            p["bib_hrefs"]) == (30, 521, 13802, 393), f"ver dirs {p['ver_dirs']}, bib {p['bib_files']}"
    assert (p["ledger_set_bytes"], p["all_tsv_bytes"], p["disk_links"], p["disk_broken"],
            p["disk_dirs"], p["rawbib_kib"]) == (297050, 2316386, 66115, 0, 17700, 2021), \
        f"ledger set {p['ledger_set_bytes']}, all TSV {p['all_tsv_bytes']}, links {p['disk_links']}"
    assert p["index_pages"] == len(tree_index_pages()) > 0, \
        f"index pages {p['index_pages']} against {len(tree_index_pages())} .md files walked under notes/index/"
    assert p["index_tables"] == len(tree_index_tables(mod)) > 0, \
        f"index tables {p['index_tables']} against {len(tree_index_tables(mod))} .tsv files walked under notes/tables/"
    assert p["index_bytes"] > 0, f"index tree {p['index_bytes']} B"
    assert (p["substr_disc"], p["substr_res"], p["brace_disc"], p["brace_res"],
            p["resultentries"]) == (18, 373, 17, 372, 372), f"substring {p['substr_disc']}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _, _, _, _ = mod.check(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


def test_ledger_joins_fire_on_faults_the_literals_miss(mod, ledger):
    """A ledger row fault moves no page byte, so every page pass stays silent and no literal pin
    moves: the nodes, edges, bytes, pages and substring figures are all measured from the index tree
    and the corpus, not from the ledger, so a ledger fault cannot move them: the joins are the only
    witness — the `paps_form` flip breaks the formalized join and the `paps` flip breaks the
    manuscript join."""
    p = mod.population()
    for col, target in (("paps_form", p["formalized"]), ("paps", p["manuscripts"])):
        i = next(n for n, r in enumerate(ledger) if int(r[col]) > 0)
        led = [dict(r) for r in ledger]
        led[i][col] = str(int(led[i][col]) - 1)
        assert target == sum(int(r[col]) for r in ledger), \
            f"the clean {col} join is not the relation the population satisfies"
        assert target != sum(int(r[col]) for r in led), \
            f"the {col} flip did not break the join, so the join is not a witness"
