"""The self-tests for `notes/scripts/verify_verification_dirs.py`.

The checker verifies `notes/reports/verification-dirs.md` against the 30 bundles it describes. Anchors:
every `path:line` and `path:a-b` resolves against the file, a prefixed path resolves against the
repo root, and a span fits inside the file. Quotations: each `*"…"*` in the family-348 section is
matched against the lines its anchor names, each row quote in the entry-point section is matched at
the anchored line exactly, and each `says "…"` phrase is matched against the README its slug names.
Counts: every bold count is re-derived from the bundles, the ledger, and the entry-point recomputation.
Ledger claims: the `covmd`/`inputs`/`verification` values the page asserts are re-checked from the
TSV. Entry-point counts: the class counts, the named/unnamed split, the rule-4 firing count, the
ledger join, and the two `rows.txt` files' size and byte identity. Table: one row per bundle in slug
order, with the family that slug belongs to. Coverage: every artifact a bundle's `COVERAGE.md` names
is on disk. Sync: the page bytes against `render_reports.py`'s render of it.

This file injects nineteen faults, one per check form the page uses, and asserts each fires the pass
that owns it: an anchor line shifted, an anchor file renamed, a block line altered, a prose quote
altered, the passed-record count, the negative-test count, a ledger value, an abbreviated anchor, the
coverage-file artifact presence, an entry class count, the unnamed bundle count, an entry-section
quote, an entry-section anchor, the `rows.txt` size, a table row's family, the rule-4 firing count,
the entry-section ledger sum, a deleted table row, and a script line count inside an entry-point cell
that no count phrase reads — the last is visible only to the render diff.

**The needles that name a measured figure are derived at run time, not recorded.** The count, ledger
and entry-point needles are rebuilt from the checker's own `count_phrases()`, `ledger_phrases()` and
`entry_phrases()` applied to the measured population; the two table needles read the mutated page's
own rows against the recomputation; the block needle is keyed to the byte the mutation touched, so it
reports the block the fault sits in — the two block faults share a block, and a needle that scans
every block and reports the first mismatch is the same function for both; the quote needles re-run the
checker's anchor-selection rule on the mutated page, so the anchor a quote is pinned to comes from the
page, not from a recorded string; and the render needle reads the mutated page's line number plus the
clip the render diff prints. The needles that stay literal are the mutation's own inputs — the renamed
anchor file and the abbreviated anchor.

Every fault is built from a real anchor, a real block line, a real quotation, a real count phrase, a
real ledger value, a real table row and a real entry cell in the page as committed. Each test asserts
the injected text differs from the page it started from, and each needle is the problem string the
pass that owns that form prints — measured specific, each needle fires for its own fault and for no
other. The generic render-diff line fires for every fault, so no needle is that line; the prose fault
is keyed to the page line the render diff names.

The clean test asserts the passes are silent and pins the counts they report: 42 anchors, 3 block
lines, 2 prose quotes, 27 row quotes, 1 says-quote, 16 count phrases, 5 ledger phrases, 9 entry
phrases, 30 table rows, 0 sync problems; the bundle population at 4 named `COVERAGE.md` files all
present, 9 shared, 7 identical, 2 differing, 8 entries, 0 mismatches, 53 identities, 21 interval
rows, 15 reported, 6 supplementary, 12 triangle rows, 9 determinant floors, 24 exact, 41
subintervals, 504 lines, 6 check functions, 9 printed keys, 13 `require` calls, 151 passed-record
occurrences, 11 checks with 8 negative and 7 ending `rejected`; and the entry recomputation over 22
families, 28 named by a README section, 27 by a `## Verification` heading and 1 by
the other heading, 6 with no entry point, 0 rule-4 firings, 2 declaring READMEs, and the two
`rows.txt` files at 20 lines and 1,436 bytes, byte-identical. The bundle count is pinned as a **walk
equality**: the test walks `preprints/` for directories carrying a `verification/` directory itself and
the entry pass's count must equal the walk, so a bundle added to the corpus moves the walk, not the
recorded number. A page with fewer anchors, quotes,
phrases or rows is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing. `population()` and `entry_measure()` are under
`functools.cache`, so the twenty `check()` calls the row makes pay the bundle walk once.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_verification_dirs.py -q
"""
import pathlib
import re

import pytest

pytestmark = pytest.mark.mutant

REPO = pathlib.Path(__file__).resolve().parents[3]


def tree_bundles():
    """The manuscript directories under `preprints/` that carry a `verification/` directory, walked by
    the test. The entry pass's dir count is the census; this is the tree, so the equality is the
    invariant: the pass counted every bundle on disk, and a bundle added to the corpus moves the walk."""
    return [d for d in (REPO / "preprints").iterdir()
            if d.is_dir() and (d / "verification").is_dir()]

POS = "preprints/Positively-curved-Einstein-four-manifolds-September-23-2026"
ZERO = "preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026"
HEIS = "preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026"


def row_of(c, sub):
    """The 1-based page line carrying `sub`; a sub on two lines makes the needle ambiguous."""
    lines = c.split("\n")
    hits = [i + 1 for i, line in enumerate(lines) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


def _clip(line):
    return repr(line if len(line) <= 80 else line[:80] + "…")


def render_needle(c, sub):
    """The render-diff sample line for the mutated line: the page's 1-based line number and the clip
    the diff prints for it, both read from the mutated page."""
    n = row_of(c, sub)
    return f"page line {n}: page {_clip(c.split(chr(10))[n - 1])}"


def phrase_needle(kind, label, phrases):
    """A count needle: the phrase the pass demands for `label`, rebuilt from the measured population."""
    def f(_c, mod, ctx):
        want = next(p for p, lab in phrases(mod, ctx) if lab == label)
        return f"{kind} ({label}): page does not contain {want!r}"
    return f


def entry_join_needle(_c, _mod, ctx):
    """The entry-section ledger join, rebuilt from the checker's own ledger claims."""
    lv = ctx["lv"]
    want = f"sums to {lv['dirs']} dirs over {lv['fams']} families"
    return f"entry-point count mismatch (entry-section ledger join): page does not contain {want!r}"


def table_rows(c, mod):
    """The mutated page's entry-point table families, read the way the pass reads them."""
    return re.findall(r"^\| (\d{3}) \|", mod.section_bodies(c)[0][1], re.MULTILINE)


def family_needle(c, mod, ctx):
    """The table family-order problem: the mutated page's rows against the recomputed slug order. The
    pass reports the 1-based row index, so the needle reports the same index."""
    rows = table_rows(c, mod)
    want = ctx["e"]["table"]
    bad = [f"{i + 1}: {rows[i]} != {want[i]}" for i in range(min(len(rows), len(want))) if rows[i] != want[i]]
    return f"entry-point table family order: {'; '.join(bad)}"


def deleted_row_needle(c, mod, ctx):
    """The table-omission problem: the mutated page's row count against the bundle count."""
    return f"entry-point table has {len(table_rows(c, mod))} rows, the bundle count is {ctx['e']['dirs']}"


def block_needle(c, mod, sub):
    """The fenced-block problem, keyed to the byte the mutation touched. The two block faults sit in
    the same block, so a needle that scans every block and reports the first mismatch is the same
    function for both and cross-fires. Keying on the mutated byte — the shifted anchor, or the altered
    block line — selects the block the pass reports, and the anchor and the first mismatching line are
    read from that block."""
    for _, body in mod.section_bodies(c):
        if sub not in body:
            continue
        lines = body.split("\n")
        for i, blk in mod.anchors.fenced_blocks(lines, dedent=True):
            anchor = mod.anchors.nearest_anchor(lines, i, mod.ANCHOR, window=9)
            if anchor is None:
                continue
            rel, at = anchor[0], int(anchor[1])
            if sub not in f"{rel}:{at}" and not any(sub in ln for ln in blk):
                continue
            src = (mod.ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
            for n, want in enumerate(blk):
                got = src[at - 1 + n] if at - 1 + n < len(src) else "<past end of file>"
                if got != want:
                    return f"block line {n} != {rel}:{at + n}"
    raise AssertionError(f"no block carries {sub!r} in the mutated page")


def quote_needle(c, mod, sub):
    """The quote problem for a mutated quote: the anchor the pass pins it to, re-derived from the
    mutated page by the checker's own rule — the anchor in the quote's line, else the first anchor in
    the four lines below it."""
    lines = c.split("\n")
    idx = row_of(c, sub) - 1
    row = lines[idx]
    span = row.find(sub)
    found = mod.ANCHOR.findall(row[span:])[:1] or mod.ANCHOR.findall(row[:span])[-1:]
    if not found:
        found = next(mod.ANCHOR.findall(ln) for ln in lines[idx + 1:idx + 5])
    assert found, f"no anchor on or below the line carrying {sub!r}"
    return f"quote not found in {found[0][0]}"


def row_quote_needle(c, mod, sub):
    """The row-quote problem for a shifted anchor: the anchor the mutated table row carries."""
    row = c.split("\n")[row_of(c, sub) - 1]
    found = mod.ANCHOR.findall(row)
    assert found, f"no anchor on the row carrying {sub!r}"
    return f"row quote anchored at {found[0][0]}:{found[0][1]}"


COUNT = phrase_needle("count mismatch", "passed-record count", lambda mod, ctx: mod.count_phrases(ctx["v"]))
NEGATIVE = phrase_needle("count mismatch", "portability check counts",
                         lambda mod, ctx: mod.count_phrases(ctx["v"]))
COVERAGE = phrase_needle("count mismatch", "coverage-file artifact presence",
                         lambda mod, ctx: mod.count_phrases(ctx["v"]))
CLASSES = phrase_needle("entry-point count mismatch", "entry-point class counts",
                        lambda mod, ctx: mod.entry_phrases(ctx["e"]))
UNNAMED = phrase_needle("entry-point count mismatch", "unnamed bundle count",
                        lambda mod, ctx: mod.entry_phrases(ctx["e"]))
ROWS = phrase_needle("entry-point count mismatch", "rows.txt size and identity",
                     lambda mod, ctx: mod.entry_phrases(ctx["e"]))
RULE4 = phrase_needle("entry-point count mismatch", "rule 4 firing count",
                      lambda mod, ctx: mod.entry_phrases(ctx["e"]))
LEDGER = phrase_needle("ledger claim mismatch", "family 348 verification value",
                       lambda mod, ctx: mod.ledger_phrases(ctx["lv"]))

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("anchor line shifted",
     lambda c, mod, ctx: block_needle(c, mod, f"{POS}/verification/verify.py:495"),
     lambda t: t.replace(f"`{POS}/verification/verify.py:496`",
                         f"`{POS}/verification/verify.py:495`", 1)),
    ("anchor file renamed", "06-certificates.tex does not exist",
     lambda t: t.replace("September-23-2026/build/sections/07-certificates.tex:14",
                         "September-23-2026/build/sections/06-certificates.tex:14", 1)),
    ("block line altered",
     lambda c, mod, ctx: block_needle(c, mod, '"Recomputed results differ from bundled results.json'),
     lambda t: t.replace('"Recomputed exact results differ from bundled results.json")',
                         '"Recomputed results differ from bundled results.json")', 1)),
    ("prose quote altered",
     lambda c, mod, ctx: quote_needle(c, mod, "calculus, Jacobi comparison, and Sobolev estimates"),
     lambda t: t.replace("calculus, Jacobi comparison, and Sobolev arguments",
                         "calculus, Jacobi comparison, and Sobolev estimates", 1)),
    ("count altered", COUNT,
     lambda t: t.replace("**151** such occurrences", "**150** such occurrences", 1)),
    ("negative-test count altered", NEGATIVE,
     lambda t: t.replace("ships **11** checks, **8** of them negative",
                         "ships **11** checks, **7** of them negative", 1)),
    ("ledger value altered", LEDGER,
     lambda t: t.replace("`verification` value of 2 for family 348",
                         "`verification` value of 1 for family 348", 1)),
    ("abbreviated anchor", "anchor file .../verification/verify.py does not exist",
     lambda t: t.replace(f"`{POS}/verification/verify.py:477`", "`.../verification/verify.py:477`", 1)),
    ("coverage artifact presence overstated", COVERAGE,
     lambda t: t.replace("all four are present in both directories",
                         "all five are present in both directories", 1)),
    ("entry class count altered", CLASSES,
     lambda t: t.replace("**12** top-level `README.md`", "**13** top-level `README.md`", 1)),
    ("unnamed bundle count altered", UNNAMED,
     lambda t: t.replace("**2** bundles ship a `verification/` tree",
                         "**3** bundles ship a `verification/` tree", 1)),
    ("entry-section quote altered",
     lambda c, mod, ctx: quote_needle(c, mod, "not the analytic argument"),
     lambda t: t.replace("*\"They verify finite scalar, thermal, and trial calculations, "
                         "not the analytic proof.\"*",
                         "*\"They verify finite scalar, thermal, and trial calculations, "
                         "not the analytic argument.\"*", 1)),
    ("entry-section anchor shifted",
     lambda c, mod, ctx: row_quote_needle(c, mod, "chain-September-24-2026/verification/README.md:53"),
     lambda t: t.replace("chain-September-24-2026/verification/README.md:54`",
                         "chain-September-24-2026/verification/README.md:53`", 1)),
    ("rows.txt size altered", ROWS,
     lambda t: t.replace("20 lines and 1436 bytes", "20 lines and 1437 bytes", 1)),
    ("table row family altered", family_needle,
     lambda t: t.replace("| 371 | `Stable-Self-Similar", "| 372 | `Stable-Self-Similar", 1)),
    ("rule 4 firing count altered", RULE4,
     lambda t: t.replace("Rule 4 fires for **0** bundles", "Rule 4 fires for **1** bundles", 1)),
    ("entry-section ledger sum altered", entry_join_needle,
     lambda t: t.replace("sums to 30 dirs over 22 families", "sums to 31 dirs over 22 families", 1)),
    ("table row deleted", deleted_row_needle,
     lambda t: re.sub(r"^\| 371 \| .*$\n", "", t, count=1, flags=re.MULTILINE)),
    # Prose no count phrase reads: the script's line count inside the family-067 entry-point cell.
    # The table check reads only the family column, so only the render diff can see it, and the
    # render-diff line truncates the cell, so the needle is the page line the diff names.
    ("entry cell line count altered",
     lambda c, mod, ctx: render_needle(c, "a 168-line script"),
     lambda t: t.replace("a 167-line script", "a 168-line script", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_verification_dirs")


@pytest.fixture(scope="module")
def text(mod):
    return mod.PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(mod, text):
    """Every pass is silent, and the counts the passes report are pinned."""
    problems, counters = mod.check(text, text)
    assert not problems, problems[:3]
    assert counters == (42, 3, 2, 27, 1, 16, 5, 9, 30, 0), f"counters {counters}"
    p = mod.population()
    assert (p["cov_named"], p["cov_present"], p["shared"], p["identical"], p["differ"],
            p["entries"], p["mismatches"]) == (4, 4, 9, 7, 2, 8, 0), f"cov {p['cov_named']}"
    assert (p["identities"], p["interval_rows"], p["reported"], p["supplementary"],
            p["triangle_rows"], p["det_floor"], p["exact"], p["subintervals"],
            p["lines"]) == (53, 21, 15, 6, 12, 9, 24, 41, 504), f"identities {p['identities']}"
    assert (p["checkfns"], p["printed_keys"], p["require"], p["passed"],
            p["checks"], p["negative"], p["ends_rejected"]) == (6, 9, 13, 151, 11, 8, 7), \
        f"passed {p['passed']}"
    e = mod.entry_measure()
    assert e["dirs"] == len(tree_bundles()) > 0, \
        f"entry dirs {e['dirs']} against {len(tree_bundles())} bundles walked under preprints/"
    assert (e["fams"], e["named"], e["ver"], e["run"], e["no_entry"],
            e["rule4"], e["declaring"]) == (22, 28, 27, 1, 6, 0, 2), \
        f"named {e['named']}, no_entry {e['no_entry']}"
    assert e["classes"] == {"none": 6, "top-level README.md": 12, "top-level script by name": 5,
                            "subdirectory README.md": 6, "subdirectory README.txt": 1}, e["classes"]
    assert (e["rows_lines"], e["rows_bytes"], e["rows_identical"]) == (20, 1436, True), \
        f"rows.txt {e['rows_lines']} lines"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, text, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(text)
    assert cand != text, f"{label}: mutation changed nothing"
    found, _ = mod.check(cand, cand)
    ctx = {"mod": mod, "v": mod.population(), "lv": mod.ledger_claims(mod.ledger_rows()),
           "e": mod.entry_measure()}
    want = needle(cand, mod, ctx) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def pad_cells(t):
    """Pad every table cell with two spaces."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_dropped(mod, text):
    """The opposite direction from the padding-tolerant checkers: the entry-point table reader
    (`:405`) matches rows with the byte-exact `^\\| (\\d{3}) \\|`, so padding must drop every row, not
    be tolerated. Measured: 30 rows on the clean page, 0 on the padded page, and the pass reports the
    row count against the bundle count. The page is prettier-ignored, so the padding never reaches the
    tracked tree; the test asserts the ignore rule too."""
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    found, counters = mod.check(cand, cand)
    assert counters[8] == 0, f"the padded page still reads {counters[8]} entry-point rows"
    assert any("entry-point table has 0 rows, the bundle count is 30" in x for x in found), \
        f"padding did not drop the entry-point rows: {found[:3]}"
    ignore = (mod.PAGE.parents[2] / ".prettierignore").read_text(encoding="utf-8").splitlines()
    assert "notes/reports/*.md" in ignore, \
        "the verification-dirs page is not prettier-ignored, so a format pass would pad it"
