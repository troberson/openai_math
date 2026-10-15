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

The clean test asserts the passes are silent and pins the counts they report. The resolution passes are
pinned as **derived floors**: each pass counted exactly the population its own rule reads off the page —
the anchor pattern, the fenced-block walk, the quotation pattern — and each population is required
non-zero, so 0 problems means every anchor, block line and quotation resolved. The formalization
resolution is pinned as **relations**: every unique config resolves, every carrier-typed statement has a
resolved carrier, and the entry count exceeds the unique config count. The corpus measurements stay
literal: 0 sync problems, the six pairing classes, 2,288 theorem environments with 48 `a.e.` hits over
32 families, and the 32-row `a.e.` table. `test_resolution_floors_fire_on_a_page_that_carries_nothing`
strips every anchor shape and shows the anchor equality holds at 0 while the block and quotation
counters fall below the populations the page still carries — the floor is what keeps each pass honest.
A page with fewer count phrases is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` is under `functools.cache`, so the seventeen
`check()` calls the row makes pay the yaml/docs/OAI/preprints walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_faithfulness.py -q
"""
import re

import pytest
from catlib import anchors
from catlib import yaml as Y

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


def row_line(t, key):
    line = next((l for l in t.split("\n") if l.startswith("|") and key in l), None)
    assert line, f"row {key!r} absent from the page"
    return line


def row_cells(t, key, changes):
    """The table row carrying `key`, with each `(idx, delta)` cell changed."""
    line = row_line(t, key)
    cells = line.split("|")
    for idx, delta in changes:
        cells[idx] = str(int(cells[idx]) + delta)
    return t.replace(line, "|".join(cells), 1)


def multi_cell_row(t, idx):
    """The first table row whose `idx`-th cell is a comma list of more than one item — the row the
    overlap fault can shorten. Derived from the page's own rows, not from a recorded config name."""
    for line in t.split("\n"):
        if line.startswith("|"):
            cells = line.split("|")
            if len(cells) > idx and len(cells[idx].strip().split(", ")) > 1:
                return cells[1].strip()
    raise AssertionError(f"no row with a multi-item cell {idx}")


def drop_last_item(t, key, idx):
    """Drop the last item of a comma-list cell, so the page's row no longer carries a literal the
    population measures."""
    line = row_line(t, key)
    cells = line.split("|")
    items = cells[idx].strip().split(", ")
    assert len(items) > 1, f"row {key!r} cell {idx} carries one item"
    cells[idx] = " " + ", ".join(items[:-1]) + " "
    return t.replace(line, "|".join(cells), 1)


def delete_row(t, key):
    line = next((l for l in t.split("\n")
                 if l.startswith("|") and l.split("|")[1].strip() == key), None)
    assert line, f"row {key!r} absent from the page"
    return t.replace(line + "\n", "", 1)




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
    for row in t.split("\n"):
        if row.startswith("|") and row.endswith("|"):
            cells = row[1:-1].split("|")
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = row
        out.append(padded)
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
     lambda t, v: bump(t, r"Over the \*\*(\d+)\*\* `main_results` entries", 1)),
    ("resolved count", count_needle("resolved", resolved_phrase),
     lambda t, v: bump(t, r"\*\*(\d+)\*\* of the \d+ declarations resolve", -1)),
    ("carrier-typed count", count_needle("carrier-typed", typed_phrase),
     lambda t, v: bump(t, r"\*\*(\d+)\*\* of the \d+ statements are opaque", -1)),
    ("median body size", count_needle("body sizes", sizes_phrase),
     lambda t, v: bump(t, r"median \*\*(\d+)\*\*, max", 1)),
    ("literal census", count_needle("literals", literals_phrase),
     lambda t, v: bump(t, r"\*\*(\d+)\*\* distinct literals in total", 1)),
    ("pairing class count", count_needle("pairing a", pair_a_phrase),
     lambda t, v: bump(t, r"\*\*(\d+)\*\* lean-subset,", 1)),
    ("disjoint family", disjoint_needle,
     lambda t, v: row_cells(t, f"`{v['disjoint'][0][0]}`", [(2, -1)])),
    ("overlap extra literal", overlap_needle,
     lambda t, v: drop_last_item(t, multi_cell_row(t, 3), 3)),
    ("a.e. census", count_needle("a.e. census", ae_census_phrase),
     lambda t, v: bump(t, r"\*\*([\d,]+)\*\* theorem environments", 1)),
    ("a.e. row deleted",
     lambda c, mod, v: ae_deleted_needle(c, mod, v, str(v["ae_table"][0][0])),
     lambda t, v: delete_row(t, str(v["ae_table"][0][0]))),
    ("a.e. row count",
     lambda c, mod, v: ae_count_needle(c, mod, v, str(max(v["ae_table"], key=lambda r: r[1])[0])),
     lambda t, v: row_cells(t, str(max(v["ae_table"], key=lambda r: r[1])[0]), [(3, 1), (5, 1)])),
    ("statement anchor shifted",
     lambda c, mod, v: block_needle(c, mod, "IntegralMeans/Model.lean:34"),
     lambda t, v: t.replace("`lean/OAI/Analysis/IntegralMeans/Model.lean:33`",
                            "`lean/OAI/Analysis/IntegralMeans/Model.lean:34`", 1)),
    ("carrier rule narrowed", "A carrier rule that allows `private` and `protected` only",
     lambda t, v: t.replace("allows `private` and `protected` but not `noncomputable`",
                            "allows `private` and `protected` only", 1)),
    ("quote anchor shifted",
     lambda c, mod, v: quote_needle(c, mod, "lean/docs/260.md:10"),
     lambda t, v: t.replace("`lean/docs/260.md:11`", "`lean/docs/260.md:10`", 1)),
    # Prose no count phrase reads: the comparator-sorry figure in the limitations list.
    # Only the render diff can see it.
    ("prose count", "The 416 comparator files carry 540 `sorry`s",
     lambda t, v: bump(t, r"The \d+ comparator files carry (\d+) `sorry`s", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_faithfulness")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned as derived floors: each pass
    counted exactly the population its own rule reads off the page (the anchor pattern, the fenced-block
    walk, the quotation pattern), so 0 problems means every anchor, block line and quotation resolved,
    and a page carrying none fails the floor. The formalization resolution is pinned as relations:
    every unique config resolves, every carrier-typed statement has a resolved carrier, and the entry
    count exceeds the unique config count. The corpus measurements stay literal."""
    problems, n_anchor, n_block, n_quote, n_sync, v = mod.check(text)
    assert not problems, problems[:3]
    lines = text.split("\n")
    assert n_anchor == len(mod.ANCHOR.findall(text)) > 0, \
        f"anchors {n_anchor} against {len(mod.ANCHOR.findall(text))} shapes the page carries"
    blocks = sum(len(blk) for _i, blk in anchors.fenced_blocks(lines, dedent=True))
    assert n_block == blocks > 0, \
        f"block lines {n_block} against {blocks} block lines the page carries"
    assert n_quote == len(mod.QUOTE.findall(text)) > 0, \
        f"quotations {n_quote} against {len(mod.QUOTE.findall(text))} quotations the page carries"
    assert n_sync == 0, f"sync problems {n_sync}"
    assert v["resolved"] == v["unique"] > 0, \
        f"{v['resolved']} resolved declarations against {v['unique']} unique configs"
    assert v["carriers_ok"] == v["typed"] > 0, \
        f"{v['carriers_ok']} resolved carriers against {v['typed']} carrier-typed statements"
    assert v["entries"] > v["unique"] > 0, \
        f"{v['entries']} entries over {v['unique']} configs"
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
    cand = mut(text, mod.population())
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
    v = mod.population()
    for label, needle, mut in MUTANTS:
        cand = mut(base, v)
        found, _, _, _, _, v = mod.check(cand)
        want = needle(cand, mod, v) if callable(needle) else needle
        if not any(want in x for x in found):
            broken.append(f"{label}: {want!r}")
    assert not broken, f"layout shift breaks {len(broken)} needles: {broken[:3]}"


def test_resolution_floors_fire_on_a_page_that_carries_nothing(mod, text):
    """Stripping every anchor shape from the page drives the anchor pass to 0, and the block and
    quotation passes with it — a block with no preceding anchor is skipped, a quote with no anchor in
    its line is skipped. The page still carries blocks and quotations, so the pass counts less than the
    page carries: the equality the clean test asserts fails, which is what makes the floor non-vacuous."""
    cand = mod.ANCHOR.sub("", text)
    _p, n_anchor, n_block, n_quote, _s, _v = mod.check(cand)
    blocks = sum(len(blk) for _i, blk in anchors.fenced_blocks(cand.split("\n"), dedent=True))
    quotes = len(mod.QUOTE.findall(cand))
    assert n_anchor == len(mod.ANCHOR.findall(cand)) == 0, \
        f"the anchor pass counted {n_anchor} on a page with no anchors"
    assert n_block == 0 < blocks, \
        f"the block pass counted {n_block} of {blocks} block lines once the anchors were stripped"
    assert n_quote == 0 < quotes, \
        f"the quotation pass counted {n_quote} of {quotes} quotations once the anchors were stripped"


def test_carrier_rule_allows_noncomputable(mod):
    """The shipped carrier rule allows `noncomputable`, so `noncomputable def MainClaim : Prop := by`
    (`lean/OAI/Computability/MeanPayoff/Model.lean:113`) is found. A rule that allows only
    `private|protected` misses it — that is the 1-of-61 gap the page records. Neither string is a file
    on disk."""
    line = "noncomputable def MainClaim : Prop := by"
    assert mod.CARR.match(line), "the shipped carrier rule does not read a noncomputable carrier"
    narrow = re.compile(r"^\s*(?:private\s+|protected\s+)?(?:def|abbrev|structure)\s+"
                        r"([A-Za-z0-9_.]+)\s*:\s*(?:Prop\s*)?[:=]")
    assert not narrow.match(line), \
        "the narrowed rule reads the same line, so `noncomputable` is not what it excludes"
    assert narrow.match("private def MainClaim : Prop := by"), \
        "the narrowed rule does not read the private form it is built for"


def test_statement_rule_allows_the_qualified_name():
    """The shipped statement rule matches the qualified name minus `OAI.` as well as the bare tail, so
    `theorem ThorpNine.main :` (`lean/OAI/Probability/ThorpRouting/Main.lean:13`) is found for the
    declaration `OAI.ThorpNine.main`. A bare-tail rule reads 188 of the 189 declarations, so it misses
    this one. Both rules read `theorem main :`. Neither string is a file on disk."""
    decl = "OAI.ThorpNine.main"
    qualified = "theorem ThorpNine.main :"
    pat = Y.stmt_pattern(decl)
    bare = re.compile(r"^\s*(theorem|lemma|proposition|corollary|def|example)\s+main\b")
    assert re.match(pat, qualified), f"the shipped rule does not read {qualified!r}"
    assert not bare.match(qualified), \
        f"the bare-tail rule reads {qualified!r}, so the qualified branch is not what widens the read"
    plain = "theorem main :"
    assert re.match(pat, plain) and bare.match(plain), \
        "the shipped rule does not read the bare-tail form, so the two rules are not the same rule"


def start_only(a, _b, n):
    """The narrowed rule: check only the start position, which is what a single-line anchor read does."""
    return [] if 0 < a <= n else [a]


def test_range_facts_flags_a_range_past_the_end():
    """The shared range rule (`catlib.anchors.range_facts`) checks **both** ends, so a range whose end
    runs past the file is a problem; a rule that checks only the start position misses it. The line list
    is synthetic — no file is read."""
    n = 5
    out, blank, rev = anchors.range_facts(2, 10, n)
    assert out == [10], f"the shipped rule read {out}, so the end position is not checked"
    assert not blank and not rev, f"the shipped rule reported {blank} / {rev} for a range inside the file"
    assert not start_only(2, 10, n), \
        "the narrowed rule flags the past-end range, so it is not the rule that misses it"


def test_range_facts_flags_a_reversed_range_and_the_anchor_pass_accepts_it():
    """The shared rule returns the reversed flag; `verify_faithfulness.py` does not treat it as a
    problem, which is what the page records: only `verify_summaries.py` flags a reversed range. A rule
    that checks only positions reports no problem when both ends sit inside the file. The line list is
    synthetic — no file is read."""
    n = 5
    out, blank, rev = anchors.range_facts(5, 2, n)
    assert rev is True, "the shipped rule does not report the reversed range"
    assert not out and not blank, f"the shipped rule read {out} / {blank} for two inside positions"
    assert not start_only(5, 2, n), \
        "the narrowed rule flags the reversed range, so it is not the rule that misses it"
