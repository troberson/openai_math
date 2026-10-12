"""The self-tests for `notes/scripts/verify_faithfulness.py`.

The checker verifies `notes/formalization-faithfulness.md` against the shipped files: the entry and
config counts, the resolved-declaration count, the carrier-typed and resolved-carrier counts, the
carrier body sizes, the literal census, the four pairing classes, the `a.e.` environment census and
the family/config intersection are recomputed from `lean/formalization.yaml`, `lean/docs/`,
`lean/OAI/` and `preprints/` by the checker's own declaration, carrier, environment and literal rules
— not `measure_faithfulness.py`'s; every `path:line` anchor resolves inside its file; every fenced
block is attributed to its nearest preceding anchor and matched at consecutive lines; every `*"…"*`
quote is pinned to the anchor in its own line; the disjoint, overlap and `a.e.` tables are checked row
by row; and the page is compared with `render_reports.py`'s render of it. Lean is read as text —
`lake`, `lean` and `comparator` are never invoked, so no verdict here can mean a proof was checked.

This file injects fifteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: the entries count, the resolved count, the carrier-typed count, the median body size,
the literal census, a pairing class count, a disjoint table family, an overlap table's extra literal,
the `a.e.` census, an `a.e.` row deleted, an `a.e.` row count, a statement anchor shifted, the carrier
rule narrowed (the widening the page names), a quote anchor shifted, and a prose count no count phrase
covers — the last is visible only to the render diff.

Every fault is built from a real count phrase, a real table row, a real anchor, a real quote and a
real prose line in the page as committed. Each test asserts the injected text differs from the page it
started from, and each needle is the problem string the pass that owns that form prints — measured
specific, each needle fires for its own fault and for no other. The render-diff line fires for every
fault, so no needle is that line.

The clean test asserts the passes are silent and pins the counts they report: 10 anchors, 30 block
lines, 1 quotation, 0 sync problems, 200 entries over 189 configs, 189 resolved declarations, 61
carrier-typed statements, 61 resolved carriers, the six pairing classes, 2,288 theorem environments
with 48 `a.e.` hits over 32 families, and the 32-row `a.e.` table. A page with fewer anchors, block
lines or quotations is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_faithfulness.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("entries count", "count mismatch (entries)",
     lambda t: t.replace("Over the **200** `main_results` entries",
                         "Over the **201** `main_results` entries", 1)),
    ("resolved count", "count mismatch (resolved)",
     lambda t: t.replace("**189** of the 189 declarations resolve",
                         "**188** of the 189 declarations resolve", 1)),
    ("carrier-typed count", "count mismatch (carrier-typed)",
     lambda t: t.replace("**61** of the 189 statements are opaque",
                         "**60** of the 189 statements are opaque", 1)),
    ("median body size", "count mismatch (body sizes)",
     lambda t: t.replace("median **6**, max **17**", "median **7**, max **17**", 1)),
    ("literal census", "count mismatch (literals)",
     lambda t: t.replace("**126** distinct literals in total",
                         "**127** distinct literals in total", 1)),
    ("pairing class count", "count mismatch (pairing a)",
     lambda t: t.replace("**31** lean-subset,", "**32** lean-subset,", 1)),
    ("disjoint family", "disjoint table [('AuslanderReiten', '198', '2')",
     lambda t: t.replace("| `AuslanderReiten` | 199 | 2 |",
                         "| `AuslanderReiten` | 198 | 2 |", 1)),
    ("overlap extra literal",
     "overlap row GrahamSpherical: ('GrahamSpherical', '172', '2, 12', '0, 1')",
     lambda t: t.replace("| `GrahamSpherical` | 172 | 2, 12, 50 | 0, 1 |",
                         "| `GrahamSpherical` | 172 | 2, 12 | 0, 1 |", 1)),
    ("a.e. census", "count mismatch (a.e. census)",
     lambda t: t.replace("**2,288** theorem environments", "**2,289** theorem environments", 1)),
    ("a.e. row deleted", "a.e. table has 31 rows",
     lambda t: t.replace("| 154 | 6 | 0 | 0 | 0 |\n", "", 1)),
    ("a.e. row count", "a.e. row 238: ('238', 1, 12, 4, 8)",
     lambda t: t.replace("| 238 | 1 | 13 | 4 | 9 |", "| 238 | 1 | 12 | 4 | 8 |", 1)),
    ("statement anchor shifted",
     "block line 0 != lean/OAI/Analysis/IntegralMeans/Model.lean:34",
     lambda t: t.replace("`lean/OAI/Analysis/IntegralMeans/Model.lean:33`",
                         "`lean/OAI/Analysis/IntegralMeans/Model.lean:34`", 1)),
    ("carrier rule narrowed", "A carrier rule that allows `private` and `protected` only",
     lambda t: t.replace("allows `private` and `protected` but not `noncomputable`",
                         "allows `private` and `protected` only", 1)),
    ("quote anchor shifted", "quote not on lean/docs/260.md:10",
     lambda t: t.replace("`lean/docs/260.md:11`", "`lean/docs/260.md:10`", 1)),
    # Prose no count phrase reads: the comparator-sorry figure in the limitations list.
    # Only the render diff can see it.
    ("prose count", "The 416 comparator files carry 540 `sorry`s",
     lambda t: t.replace("The 416 comparator files carry 539 `sorry`s",
                         "The 416 comparator files carry 540 `sorry`s", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_faithfulness")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, n_anchor, n_block, n_quote, n_sync, v = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_block, n_quote, n_sync) == (10, 30, 1, 0), \
        f"anchors {n_anchor}, block lines {n_block}, quotations {n_quote}, sync {n_sync}"
    assert (v["entries"], v["unique"], v["resolved"], v["typed"], v["carriers_ok"]) == \
        (200, 189, 189, 61, 61), f"entries {v['entries']}, unique {v['unique']}, resolved {v['resolved']}, typed {v['typed']}, carriers {v['carriers_ok']}"
    pr = v["pair"]
    assert (pr["exact"], pr["subset"], pr["overlap"], pr["disjoint"],
            pr["carrier_no_literal"], pr["no_headline_literal"], pr["no_family"]) == \
        (1, 31, 15, 2, 10, 2, 0), f"pairing classes {dict(pr)}"
    assert (v["env_total"], v["ae_envs"], len(v["ae_fams"]), len(v["inter"]),
            len(v["cfgs"]), v["ae_with"], v["ae_without"]) == (2288, 48, 32, 19, 54, 19, 35), \
        f"a.e. census {v['env_total']} envs, {v['ae_envs']} hits, {len(v['ae_fams'])} families"
    assert len(v["ae_table"]) == 32 and len(v["disjoint"]) == 2 and len(v["overlap"]) == 15, \
        f"tables: a.e. {len(v['ae_table'])}, disjoint {len(v['disjoint'])}, overlap {len(v['overlap'])}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _, _, _, _, _ = mod.check(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
