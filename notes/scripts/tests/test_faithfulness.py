"""The self-tests for `notes/scripts/verify_faithfulness.py`.

The checker verifies `notes/reports/formalization-faithfulness.md` against the shipped files: the entry and
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

**The needles that name a measured figure are derived at run time, not recorded.** The count needles
are rebuilt from the checker's own `population()` dict, the three table needles from the mutated page's
rows against the recomputation, the block needle from the anchor the mutated page attributes the block
to, and the quote needle from the anchor the mutated quote line carries. The needles that stay literal
are the mutation's own inputs — the carrier-rule wording and the comparator-sorry prose line.

The two `a.e.` table needles are keyed to the family each mutation touches. The pass reports the length
difference for **any** table difference, so a length needle fires for both faults; and deleting a row
shifts every row after it, so a first-mismatch needle fires for both. Keying the count needle to the
mutated row's own mismatch, and the deletion needle to the recomputation row for the deleted family,
is what makes each fire for its own fault and for no other.

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
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the sixteen
`check()` calls the row makes pay the yaml/docs/OAI/preprints walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_faithfulness.py -q
"""
import pytest

pytestmark = pytest.mark.mutant


def row_of(c, sub):
    """The 1-based page line carrying `sub`; a sub on two lines makes the needle ambiguous."""
    lines = c.split("\n")
    hits = [i + 1 for i, line in enumerate(lines) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


def pad_cells(t):
    """Pad every table cell with two spaces. The row regexes allow whitespace, so the passes must read
    the same rows; a regex that required exact spacing would drop rows, and the row-count line is what
    would show it."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def count_needle(label, phrase):
    """A count needle: the phrase the pass demands, built from the measured population."""
    def f(_c, _mod, v):
        want = phrase(v)
        return f"count mismatch ({label}): page does not contain {want!r}"
    return f


def table_rows(c, mod, pat, ints):
    """The mutated page's rows for a table pattern, with the numeric cells read as ints when asked."""
    out = []
    for ln in c.split("\n"):
        m = pat.match(ln)
        if m:
            cells = [int(g) if ints[i] else mod.norm(g) for i, g in enumerate(m.groups())]
            out.append(tuple(cells))
    return out


def disjoint_needle(c, mod, v):
    """The disjoint-table problem: the mutated page's rows against the recomputation."""
    rows = table_rows(c, mod, mod.DISROW, [False, False, False])
    want = [(cfg, fam, mod.norm(", ".join(str(x) for x in lits))) for cfg, fam, lits in v["disjoint"]]
    return f"disjoint table {rows} != {want}"


def overlap_needle(c, mod, v):
    """The overlap-table problem: the first row the mutated page no longer matches."""
    rows = table_rows(c, mod, mod.OVROW, [False, False, False, False])
    want = [(cfg, fam, mod.norm(", ".join(str(x) for x in extra)),
             mod.norm(", ".join(str(x) for x in shared))) for cfg, fam, extra, shared in v["overlap"]]
    for w, g in zip(want, rows, strict=False):
        if w != g:
            return f"overlap row {g[0]}: {g} != {w}"
    raise AssertionError("no overlap row mismatch in the mutated page")


def ae_count_needle(c, mod, v, fam):
    """The a.e.-table problem for a shifted count: the mutated row's own mismatch. Keyed to the family
    the mutation touched, so a row deleted elsewhere does not make it fire. The family cell stays a
    string — the recomputation keys rows by the 3-digit family, not an int."""
    rows = table_rows(c, mod, mod.AEROW, [False, True, True, True, True])
    want = {r[0]: r for r in v["ae_table"]}
    got = {r[0]: r for r in rows}
    if fam in got and got[fam] != want[fam]:
        return f"a.e. row {fam}: {got[fam]} != {want[fam]}"
    raise AssertionError(f"the mutated table carries no count mismatch for {fam}")


def ae_deleted_needle(c, mod, v, fam):
    """The a.e.-table problem for a deleted row: the recomputation row for the deleted family, which
    the pass pairs with the row that moved into its place. Keyed to the deleted family, so a count
    shifted in a different row does not make it fire."""
    rows = table_rows(c, mod, mod.AEROW, [False, True, True, True, True])
    want = {r[0]: r for r in v["ae_table"]}
    for w, a in zip(v["ae_table"], rows, strict=False):
        if w == want[fam] and w != a:
            return f"a.e. row {a[0]}: {a} != {w}"
    raise AssertionError(f"the mutated table carries no shifted pair for {fam}")


def block_needle(c, mod, sub):
    """The fenced-block problem for a shifted anchor: the block is attributed to the anchor the mutated
    page carries above it, so the anchor and the mismatching line are both read from the mutated page."""
    lines = c.split("\n")
    for i, blk in mod.anchors.fenced_blocks(lines, dedent=True):
        found = mod.anchors.nearest_anchor(lines, i, mod.ANCHOR)
        if found is None:
            continue
        rel, at = found[0], int(found[1])
        src = (mod.ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
        for n, want in enumerate(blk):
            got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
            if mod.norm(got) != mod.norm(want):
                return f"block line {n} != {rel}:{at + n}"
    raise AssertionError(f"no block mismatch below {sub!r} in the mutated page")


def quote_needle(c, mod, sub):
    """The quotation problem for a shifted anchor: the anchor the mutated quote line carries."""
    row = c.split("\n")[row_of(c, sub) - 1]
    found = mod.ANCHOR.findall(row)
    assert found, f"no anchor on the line carrying {sub!r}"
    return f"quote not on {found[0][0]}:{found[0][1]}"


def entries_phrase(v):
    return (f"Over the **{v['entries']}** `main_results` entries over "
            f"**{v['unique']}** unique configs")


def resolved_phrase(v):
    return f"**{v['resolved']}** of the {v['unique']} declarations resolve"


def typed_phrase(v):
    return f"**{v['typed']}** of the {v['resolved']} statements are opaque"


def sizes_phrase(v):
    return (f"min **{v['size_min']}** line, median **{v['size_med']}**, "
            f"max **{v['size_max']}**, sum **{v['size_sum']}** lines")


def literals_phrase(v):
    return (f"**{v['with_lit']}** of the **{v['carriers_ok']}** carriers carry at least one "
            f"integer literal; **{v['lit_total']}** distinct literals in total")


def pair_a_phrase(v):
    return f"**{v['pair']['exact']}** exact, **{v['pair']['subset']}** lean-subset,"


def ae_census_phrase(v):
    return (f"**{v['env_total']:,}** theorem environments; **{v['ae_envs']}** carry an "
            f"`a.e.`-style phrase")


# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("entries count", count_needle("entries", entries_phrase),
     lambda t: t.replace("Over the **200** `main_results` entries",
                         "Over the **201** `main_results` entries", 1)),
    ("resolved count", count_needle("resolved", resolved_phrase),
     lambda t: t.replace("**189** of the 189 declarations resolve",
                         "**188** of the 189 declarations resolve", 1)),
    ("carrier-typed count", count_needle("carrier-typed", typed_phrase),
     lambda t: t.replace("**61** of the 189 statements are opaque",
                         "**60** of the 189 statements are opaque", 1)),
    ("median body size", count_needle("body sizes", sizes_phrase),
     lambda t: t.replace("median **6**, max **17**", "median **7**, max **17**", 1)),
    ("literal census", count_needle("literals", literals_phrase),
     lambda t: t.replace("**126** distinct literals in total",
                         "**127** distinct literals in total", 1)),
    ("pairing class count", count_needle("pairing a", pair_a_phrase),
     lambda t: t.replace("**31** lean-subset,", "**32** lean-subset,", 1)),
    ("disjoint family", disjoint_needle,
     lambda t: t.replace("| `AuslanderReiten` | 199 | 2 |",
                         "| `AuslanderReiten` | 198 | 2 |", 1)),
    ("overlap extra literal", overlap_needle,
     lambda t: t.replace("| `GrahamSpherical` | 172 | 2, 12, 50 | 0, 1 |",
                         "| `GrahamSpherical` | 172 | 2, 12 | 0, 1 |", 1)),
    ("a.e. census", count_needle("a.e. census", ae_census_phrase),
     lambda t: t.replace("**2,288** theorem environments", "**2,289** theorem environments", 1)),
    ("a.e. row deleted", lambda c, mod, v: ae_deleted_needle(c, mod, v, "154"),
     lambda t: t.replace("| 154 | 6 | 0 | 0 | 0 |\n", "", 1)),
    ("a.e. row count", lambda c, mod, v: ae_count_needle(c, mod, v, "238"),
     lambda t: t.replace("| 238 | 1 | 13 | 4 | 9 |", "| 238 | 1 | 12 | 4 | 8 |", 1)),
    ("statement anchor shifted",
     lambda c, mod, v: block_needle(c, mod, "IntegralMeans/Model.lean:34"),
     lambda t: t.replace("`lean/OAI/Analysis/IntegralMeans/Model.lean:33`",
                         "`lean/OAI/Analysis/IntegralMeans/Model.lean:34`", 1)),
    ("carrier rule narrowed", "A carrier rule that allows `private` and `protected` only",
     lambda t: t.replace("allows `private` and `protected` but not `noncomputable`",
                         "allows `private` and `protected` only", 1)),
    ("quote anchor shifted",
     lambda c, mod, v: quote_needle(c, mod, "lean/docs/260.md:10"),
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
    found, _, _, _, _, v = mod.check(cand)
    want = needle(cand, mod, v) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def test_padded_table_cells_are_still_read(mod, text):
    """Padding every table cell must not change what the passes read. The three row regexes allow
    whitespace, so a padded page must report no table problem and the same three row counts. A regex
    that required exact spacing would drop rows, and the row-count line is what would show it — that is
    the discriminator, not the render diff, which fires for the padding either way."""
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    found, _, _, _, _, v = mod.check(cand)
    table = [p for p in found if "table" in p]
    assert not table, f"padded rows are not read: {table[:2]}"
    counts = (len(table_rows(cand, mod, mod.AEROW, [False, True, True, True, True])),
              len(table_rows(cand, mod, mod.DISROW, [False, False, False])),
              len(table_rows(cand, mod, mod.OVROW, [False, False, False, False])))
    assert counts == (len(v["ae_table"]), len(v["disjoint"]), len(v["overlap"])), \
        f"padded tables read {counts}, population {len(v['ae_table'])}, " \
        f"{len(v['disjoint'])}, {len(v['overlap'])}"


def shift(text):
    """Two lines inserted after the page's first `## ` heading — a layout change that moves every
    line number below it and changes no measured count."""
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("## "):
            return "".join(lines[:i + 1]) + "<!-- band shift -->\n\n" + "".join(lines[i + 1:])
    raise AssertionError("the page has no ## heading to shift")


def test_layout_shift_is_invisible(mod, text):
    """A page-line shift must not break a needle. A needle built from the mutated page re-derives
    the anchor its mutation touches, so it moves with the page; a needle that recorded the anchor
    string from the page as committed fires a message the shifted page never prints, and this test
    names it."""
    base = shift(text)
    broken = []
    for label, needle, mut in MUTANTS:
        cand = mut(base)
        found, _, _, _, _, v = mod.check(cand)
        want = needle(cand, mod, v) if callable(needle) else needle
        if not any(want in x for x in found):
            broken.append(f"{label}: {want!r}")
    assert not broken, f"layout shift breaks {len(broken)} needles: {broken[:3]}"
