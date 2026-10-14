"""The self-tests for `notes/scripts/verify_counterexample_crosscheck.py`.

The checker verifies `notes/reports/counterexample-crosscheck.md` against the shipped files: the 28-family
population, its tier split, the ledger sums, the entry/config/gap counts, the carrier-typed count and
the stub `sorry` totals are recomputed from the ledger, `overview.tex`, `lean/formalization.yaml`,
`lean/docs/` and `lean/ComparatorChallenges/`; every anchor resolves; every fenced block matches its
nearest preceding anchor at consecutive lines; every `*"…"*` quote is pinned to the anchor in its own
line; the 28-row summary table, the 12-row T3 gap table and the 9-row T2 table are checked row by
row; each entry's yaml block, statement anchor and carrier anchor are checked against the file; each
T3 block names exactly its own configs; and the page is compared with `render_reports.py`'s render of
it. Lean is read as text — `lake`, `lean` and `comparator` are never invoked, so no verdict here can
mean a proof was checked.

This file injects fourteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: a tier swapped in the summary table, a config count moved, a statement anchor shifted, a
carrier body word changed, a claim quote word changed, a yaml anchor shifted, a gap row's family
changed, a `sorry` count moved, a T2 row deleted, a T2 config taken from another family, a carrier
paraphrase, an anchor file that is not on disk, a quote moved to another family's line, and a prose
count no count phrase covers — the last is visible only to the render diff.

**The needles that name a measured figure are derived at run time, not recorded.** The table needles
read the mutated page's own rows against the recomputation; the block needles read the anchor the
mutated page attributes the block to and the block line the mutation touched; the quote needles read
the anchor the mutated quote line carries; and the statement needle reads the true statement line from
the file, so it reports the anchor the page no longer carries rather than the line the page now names.

**A needle that reports the first mismatch cross-fires when two faults share the same pass.** The two
summary-table faults share the summary pass, so a first-mismatch needle built from the mutated page
gives the same string for both. Keying it to the family the mutation touched makes each fire for its
own row. The two carrier-block faults behave the same way for a second reason: the paraphrased line is
a substring of the line it was paraphrased from, so a first-mismatch needle fires on the word fault
too. Keying to the block line the mutation touched fixes both.

The needles that stay literal are the mutation's own inputs — the invented anchor file, the `sorry`
label, and the prose denominator label.

Every fault is built from a real row, a real anchor, a real block line, a real quote and a real count
phrase in the page as committed. Each test asserts the injected text differs from the page it started
from, and each needle is the problem string the pass that owns that form prints — measured specific,
each needle fires for its own fault and for no other.

The clean test asserts the passes are silent and pins the four population counts they report: 172
anchors, 295 block lines, 38 quotations and 0 sync problems. A page with fewer anchors, block lines or
quotations is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_counterexample_crosscheck.py -q
"""
import re

import pytest

pytestmark = pytest.mark.mutant

ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(T\d)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|")


def row_of(c, sub):
    """The 1-based page line carrying `sub`; a sub on two lines makes the needle ambiguous."""
    lines = c.split("\n")
    hits = [i + 1 for i, line in enumerate(lines) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


def summary_rows(c):
    """The mutated page's summary-table rows, read the way the pass reads them."""
    out = []
    for ln in c.split("\n"):
        m = ROW.match(ln)
        if m:
            out.append((m.group(1), m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5))))
    return out


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


def summary_needle(c, _mod, v, fam):
    """The summary-table problem, keyed to the family the mutation touched. The pass reports the first
    mismatch, which is the same string for any two faults in this table, so keying to the row the
    mutation edited is what keeps the two needles distinct. The row number is the family's position in
    the population order, which is the order the pass compares."""
    want = {f: (f, v["per"][f]["tier"], len(v["per"][f]["configs"]),
                len(v["per"][f]["entries"]), len(v["per"][f]["gaps"])) for f in v["pop"]}
    got = {r[0]: r for r in summary_rows(c)}
    if fam in got and got[fam] != want[fam]:
        return f"summary table row {list(v['pop']).index(fam) + 1}: {got[fam]} != {want[fam]}"
    raise AssertionError(f"the mutated summary table carries no mismatch for {fam}")


def gap_needle(c, mod, v):
    """The gap-table problem: the mutated page's rows against the recomputed T3 gap set."""
    got = sorted((m.group(1), m.group(2)) for ln in c.split("\n") if (m := mod.GAPROW.match(ln)))
    want = sorted((cfg, f) for f in v["pop"] if v["per"][f]["tier"] == "T3"
                  for cfg in v["per"][f]["gaps"])
    if got != want:
        return f"gap table lists {got}, expected {want}"
    raise AssertionError("the mutated gap table matches the recomputation")


def t2_families_needle(c, mod, v):
    """The T2-table problem for a deleted row: the mutated page's family column against the population."""
    fams = [m.group(1) for ln in c.split("\n") if (m := mod.T2ROW.match(ln))]
    want = [f for f in v["pop"] if v["per"][f]["tier"] == "T2"]
    if fams != want:
        return f"T2 table families {fams} != {want}"
    raise AssertionError("the mutated T2 table carries the population families")


def t2_config_needle(c, mod, v, fam):
    """The T2-table problem for a config taken from another family, keyed to the row the mutation
    touched: the mutated cell's configs against that family's measured gaps."""
    for ln in c.split("\n"):
        m = mod.T2ROW.match(ln)
        if m and m.group(1) == fam:
            cfgs = re.findall(r"`([A-Za-z0-9_]+)`", m.group(2))
            want = v["per"][fam]["gaps"]
            if cfgs != want:
                return f"T2 row {fam}: configs {cfgs} != {want}"
    raise AssertionError(f"the mutated T2 table carries no row {fam}")


def block_needle(c, mod, sub):
    """The fenced-block problem, keyed to the byte the mutation touched. The block carrying `sub` is the
    block the pass reports, and the reported line is the line `sub` sits on — the first-mismatch rule
    would report the same line for two faults in one block, and a paraphrased line is a substring of
    the line it was paraphrased from, so a first-mismatch needle cross-fires."""
    lines = c.split("\n")
    for i, blk in mod.anchors.fenced_blocks(lines, dedent=True):
        found = mod.anchors.nearest_anchor(lines, i, mod.ANCHOR)
        if found is None:
            continue
        rel, at = found[0], int(found[1])
        n = next((k for k, ln in enumerate(blk) if sub in ln), None)
        if n is None:
            if sub not in f"{rel}:{at}":
                continue
            n = 0
        src = (mod.ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
        want = blk[n]
        got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
        if mod.norm(got) != mod.norm(want):
            return f"block line {n} != {rel}:{at + n}"
    raise AssertionError(f"no block carries {sub!r} in the mutated page")


def quote_needle(c, mod, sub):
    """The quote problem, keyed to the mutated line. A quote can wrap across page lines, so the mutated
    word is not always on the line the anchor sits on; `sub` is the locating string of the line the
    quote starts on, and the anchor the pass pins the quote to is read from that line."""
    row = c.split("\n")[row_of(c, sub) - 1]
    span = row.find(sub)
    found = mod.ANCHOR.findall(row[span:])[:1] or mod.ANCHOR.findall(row[:span])[-1:]
    assert found, f"no anchor on the line carrying {sub!r}"
    return f"quote not on {found[0][0]}:{found[0][1]}"


def statement_needle(c, mod, v, sub):
    """The statement-anchor problem, keyed to the mutated anchor. The true statement line is read from
    the file, so the needle reports the anchor the page no longer carries, not the line the page now
    names."""
    row = c.split("\n")[row_of(c, sub) - 1]
    m = mod.ANCHOR.search(row)
    assert m, f"no anchor on the line carrying {sub!r}"
    rel = m.group(1)
    for f in v["pop"]:
        for cfg in v["per"][f]["entries"]:
            decl, r, _y = v["mr"][cfg]
            if f"lean/{r}" != rel:
                continue
            at, _blk = mod.cx.declaration_statement(decl, r)
            if at is not None and f"`lean/{r}:{at}`" not in c:
                return f"no statement anchor at lean/{r}:{at}"
    raise AssertionError(f"no population statement in {rel} is missing from the mutated page")


# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("tier swapped in the summary table",
     lambda c, mod, v: summary_needle(c, mod, v, "047"),
     lambda t: t.replace("| 047 | T3 | 1 | 1 | 0 |", "| 047 | T2 | 1 | 1 | 0 |", 1)),
    ("config count moved",
     lambda c, mod, v: summary_needle(c, mod, v, "172"),
     lambda t: t.replace("| 172 | T3 | 7 | 2 | 5 |", "| 172 | T3 | 6 | 2 | 4 |", 1)),
    ("statement anchor shifted",
     lambda c, mod, v: statement_needle(c, mod, v, "lean/OAI/Algebra/AffineCancellation/Main.lean:33"),
     lambda t: t.replace("`lean/OAI/Algebra/AffineCancellation/Main.lean:32`",
                         "`lean/OAI/Algebra/AffineCancellation/Main.lean:33`", 1)),
    ("carrier body word",
     lambda c, mod, v: block_needle(c, mod, "ringKrullDim A = 5"),
     lambda t: t.replace("ringKrullDim A = 4", "ringKrullDim A = 5", 1)),
    ("claim quote word",
     lambda c, mod, v: quote_needle(c, mod, "Claim 2 (`overview.tex:170`) — *\"It also disproves the Dolgachev"),
     lambda t: t.replace("disproving affine-space cancellation", "disproving affine-space duality", 1)),
    ("yaml anchor shifted",
     lambda c, mod, v: block_needle(c, mod, "lean/formalization.yaml:1042"),
     lambda t: t.replace("`lean/formalization.yaml:1041`", "`lean/formalization.yaml:1042`", 1)),
    ("gap row family", gap_needle,
     lambda t: t.replace("| `BalancedRyser` | 162 |", "| `BalancedRyser` | 185 |", 1)),
    ("sorry count moved", "count mismatch (stub sorries)",
     lambda t: t.replace("carrying **55** `sorry` occurrences",
                         "carrying **57** `sorry` occurrences", 1)),
    ("T2 row deleted", t2_families_needle,
     lambda t: t.replace("| 151 | `C1EntropyCounterexample` | `lean/docs/151.md:15` |\n", "", 1)),
    ("T2 config from another family",
     lambda c, mod, v: t2_config_needle(c, mod, v, "151"),
     lambda t: t.replace("`C1EntropyCounterexample` | `lean/docs/151.md:15`",
                         "`Naimark` | `lean/docs/151.md:15`", 1)),
    ("carrier paraphrase",
     lambda c, mod, v: block_needle(c, mod, "Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)"),
     lambda t: t.replace("¬ Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)",
                         "Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)", 1)),
    ("anchor file absent", "anchor file lean/OAI/Geometry/Arnold/Nope.lean does not exist",
     lambda t: t.replace("`lean/OAI/Geometry/Arnold/Main.lean:14`",
                         "`lean/OAI/Geometry/Arnold/Nope.lean:14`", 1)),
    ("quote moved to another family",
     lambda c, mod, v: quote_needle(c, mod, "Claim 2 (`overview.tex:218`) — *\"It also disproves the Dolgachev"),
     lambda t: t.replace("Claim 2 (`overview.tex:170`) — *\"It also disproves the Dolgachev",
                         "Claim 2 (`overview.tex:218`) — *\"It also disproves the Dolgachev", 1)),
    # Prose no count phrase reads: the formalized-manuscript denominator in the population
    # paragraph. Only the render diff can see it.
    ("prose count", "count mismatch (ledger paps_form/paps)",
     lambda t: t.replace("formalized manuscripts out of **50**.",
                         "formalized manuscripts out of **51**.", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_counterexample_crosscheck")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8")


def test_clean_page(mod, text):
    """Every pass is silent, and the four population counts the passes report are pinned."""
    problems, n_anchor, n_block, n_quote, n_sync, v = mod.check(text)
    assert not problems, problems[:3]
    assert (n_anchor, n_block, n_quote, n_sync) == (172, 295, 38, 0), \
        f"anchors {n_anchor}, block lines {n_block}, quotations {n_quote}, sync {n_sync}"
    assert len(v["pop"]) == 28, f"population {len(v['pop'])}, not 28"


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
    """Padding every table cell must not change what the passes read. The row regexes allow whitespace,
    so a padded page must report no table problem and the same row counts. A regex that required exact
    spacing would drop rows, and the row-count line is what would show it — that is the discriminator,
    not the render diff, which fires for the padding either way."""
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    found, _, _, _, _, v = mod.check(cand)
    table = [p for p in found if "table" in p]
    assert not table, f"padded rows are not read: {table[:2]}"
    assert len(summary_rows(cand)) == len(v["pop"]), \
        f"padded summary table reads {len(summary_rows(cand))} rows, population {len(v['pop'])}"
    t2 = [m.group(1) for ln in cand.split("\n") if (m := mod.T2ROW.match(ln))]
    assert t2 == [f for f in v["pop"] if v["per"][f]["tier"] == "T2"], \
        f"padded T2 table reads {t2}"
