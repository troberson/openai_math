"""The self-tests for `notes/scripts/verify_index_design.py`.

The checker verifies `notes/development/index-design.md` against the tree it describes. Anchors: every
backticked `path:line` shape must name a file that exists and a line inside it, so a mistyped
extension fails instead of being skipped, and every fenced block is attributed to its nearest
preceding anchor and matched at consecutive lines. Counts: all 82 count and byte phrases are rebuilt
from `measure_index_sizes.population()` — the node and edge totals, the citation-edge counts, the
schema tables' row counts read from the generated files under `notes/index/`, the substring-versus-
line-start command counts, the ledger-set and all-TSV byte sums, the disk link check, and the raw-bib
projection. Byte sizes: the five TSVs the page tabulates are re-read from disk. The page is compared
with `render_reports.py`'s render of it. The schema tables' row counts come from the rendered files,
so a table that drops rows is a mismatch, not a phrase built from the upstream count it was derived
from.

This file injects fourteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: an anchor line shifted, an anchor file renamed, a block line altered, the node total,
the namespace disagreement count, the citation-edge count, an abbreviated anchor, the substring-rule
counts, the raw-bib projection, a rendered schema row count, the ledger-set byte total widened to the
all-TSV sum, the all-TSV total swapped with the ledger set, the disk link count, and a schema-table
byte column no count or size phrase covers — the last is visible only to the render diff.

Every fault is built from a real anchor, a real block line, a real count phrase, a real byte phrase
and a real table cell in the page as committed. Each test asserts the injected text differs from the
page it started from, and each needle is the problem string the pass that owns that form prints —
measured specific, each needle fires for its own fault and for no other. The render-diff line fires
for every fault, so no needle is that line.

The clean test asserts the passes are silent and pins the counts they report: 9 anchors, 3 block
lines, 82 count and byte phrases, 0 sync problems, 2,560 nodes over 3,415 resolved edges (17,217 raw),
391 citation edges over 104 cross-family, 1,033 index pages and 16 tables, 372 families over 719
manuscripts, 242 scope notes, 416 configs, 200 `main_results` entries over 189 configs, 172 formalized,
749 preprint dirs, 122,458 `.lean` files, 559 module dirs, 17 disciplines against 23 Lean dirs, 10
traces in 11 files, 30 verification bundles, 521 `.bib` files with 13,802 entries and 393 hrefs, the
ledger set at 297,050 B against the all-TSV 2,252,773 B, 66,108 disk links with 0 broken and 17,700
resolving to a directory, and the substring counts 18 / 373 against the brace-qualified 17 / 372. A
page with fewer anchors, block lines or phrases is a pass that stopped checking, not a pass that
passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the fifteen
`check()` calls the row makes pay the index-tree walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_index_design.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

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
     lambda t: t.replace("together totals **2252773** B", "together totals **297050** B", 1)),
    ("disk link count", "count mismatch (disk link check)",
     lambda t: t.replace("covers **66,108** links", "covers **66,109** links", 1)),
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


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, n_anchor, n_block, n_phrases, n_sync = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_block, n_phrases, n_sync) == (9, 3, 82, 0), \
        f"anchors {n_anchor}, block lines {n_block}, phrases {n_phrases}, sync {n_sync}"
    p = mod.population()
    assert (p["nodes"], p["edges_resolved"], p["edges_rawbib"], p["resolved"], p["cross"]) == \
        (2560, 3415, 17217, 391, 104), f"nodes {p['nodes']}, edges {p['edges_resolved']}"
    assert (p["index_pages"], p["index_tables"], p["families"], p["manuscripts"],
            p["scope_notes"], p["chal_json"], p["chal_lean"]) == \
        (1033, 16, 372, 719, 242, 416, 416), f"index pages {p['index_pages']}, families {p['families']}"
    assert (p["mr_entries"], p["mr_configs"], p["formalized"], p["preprint_dirs"],
            p["lean_files"], p["lean_mods"], p["disciplines"], p["lean_disc"]) == \
        (200, 189, 172, 749, 122458, 559, 17, 23), f"main_results {p['mr_entries']}, lean {p['lean_files']}"
    assert (p["traces"], p["trace_files"], p["ver_dirs"], p["bib_files"], p["bib_entries"],
            p["bib_hrefs"]) == (10, 11, 30, 521, 13802, 393), f"traces {p['traces']}, bib {p['bib_files']}"
    assert (p["ledger_set_bytes"], p["all_tsv_bytes"], p["disk_links"], p["disk_broken"],
            p["disk_dirs"], p["rawbib_kib"]) == (297050, 2252773, 66108, 0, 17700, 2021), \
        f"ledger set {p['ledger_set_bytes']}, all TSV {p['all_tsv_bytes']}, links {p['disk_links']}"
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
