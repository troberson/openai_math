"""The extracted self-tests for `notes/scripts/verify_dependency_drift.py` and the page.

The checker's passes are: the anchor pass (every `path:line` and `path:a-b` resolves, a bare `:N`
against the nearest explicit path); the quotation pass (every blockquote and every checked code span
verbatim against the source it cites); the table pass (the 23-row patch table equal to the TSV row by
row in descending order); the name-list pass (each named library list equal to the measured set); the
count pass (every count phrase re-measured from the TSV, `lean/lakefile.lean`, `lean/formalization.yaml`
and the patch files); and the render diff against `render_reports.py`.

Each fault below mutates the page text in memory, so no page is written. `verify_dependency_drift.py`'s
`measure()` is under `functools.cache` (`:185`): the checker writes nothing and the tests mutate page
text, so a second call in the same process cannot see a different corpus, and the eleven `check()` calls
this file makes pay the TSV, lakefile, yaml and patch-file walk once.

**The needles that name a measured figure are derived at run time, not recorded.** The count needles
are rebuilt from the checker's own `measure()` dict, the table needle from the mutated page's row
against the TSV value, the name-list needle from the checker's own `name_list()` read of the mutated
page against the measured set, the omitted-row needle from the measured patched set minus the mutated
page's table rows, the blockquote needle from the anchor the mutated blockquote line carries, the code-span
needle from the page line the mutated span sits on, and the render needle from the mutated page's line
number plus the clip the render diff prints. The needles that stay literal are the mutation's own
inputs — the anchor line written out of range.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_dependency_drift.py -q`
"""

import pathlib
import re

import pytest

PAGE = pathlib.Path("notes/reports/dependency-drift.md")


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


def blockquote_needle(c, sub):
    """The blockquote problem for the mutated line: the `path:line` the mutated blockquote cites."""
    n = row_of(c, sub)
    m = re.match(r"^> `([\w./+-]+\.\w+):(\d+): ", c.split("\n")[n - 1])
    assert m, f"page line {n} is not a blockquote"
    return f"page:{n}: blockquote != {m.group(1)}:{m.group(2)}"


def span_needle(c, sub):
    """The code-span problem for the mutated span: the page line it sits on, read from the mutated page."""
    return f"page:{row_of(c, sub)}: code span not found in source: {sub[:70]!r}"


def table_needle(c, v, m, name):
    """The table-row problem for `name`: the mutated page's patch-lines cell against the TSV value."""
    row = next(r for r in v.table_rows(c) if r[0] == name)
    return f"table {name}: patch lines {row[2]} != TSV {m['by_name'][name]['plines']}"


def omits_needle(c, v, m):
    """The table-omission problem: the measured patched library the mutated page's table no longer names."""
    seen = {r[0] for r in v.table_rows(c)}
    miss = [x for x in m["patched"] if x not in seen]
    assert len(miss) == 1, f"{len(miss)} measured patched libraries absent from the mutated table"
    return f"patch-size table omits {miss[0]}"


def name_list_needle(c, v, m):
    """The name-list problem: the checker's own read of the mutated page against the measured set."""
    got = v.name_list(c, "`direct_imports = 0`:", "ship a patch")
    return (f"name list zero-import list != computed: "
            f"missing {sorted(set(m['zero']) - set(got))} extra {sorted(set(got) - set(m['zero']))}")


def patch_total_needle(_c, v, m):
    """The patch-lines count problem, rebuilt from the measured total."""
    return f"count missing from page: patch lines -> {v.n(m['total_lines'])!r}"


def phase_count_needle(_c, _v, m):
    """The pre-resolution count problem, rebuilt from the measured phase array."""
    return f"count missing from page: pre-resolution libraries -> {'**' + str(len(m['pre'])) + '**'!r}"


def violation_needle(_c, _v, m):
    """The ordering-violation count problem, rebuilt from the measured violation list."""
    return f"count missing from page: yaml ordering violations -> " \
           f"{'%d entries violate' % len(m['violations'])!r}"


def anchor_needle(_c, _v, _m, line):
    """The out-of-range anchor problem: the mutated page's anchor line against the length of the
    file the anchor names, so the line count is measured at run time, not recorded."""
    total = len(pathlib.Path("lean/lakefile.lean")
                .read_text(encoding="utf-8", errors="replace").splitlines())
    return f"anchor lean/lakefile.lean:{line} out of range ({total} lines)"


# (label, needle, mutation). A needle is a function of the mutated page, the loaded checker and the
# measured dict; a mutation is a function of the page.
MUTANTS = [
    ("blockquote paraphrased as a quote",
     lambda c, v, m: blockquote_needle(c, "compatibility patch was lost by dependency resolution."),
     lambda p: p.replace("compatibility patch was lost during dependency resolution.",
                         "compatibility patch was lost by dependency resolution.", 1)),
    ("anchor out of range",
     lambda c, v, m: anchor_needle(c, v, m, 486),
     lambda p: p.replace("`lean/lakefile.lean:10`–`:86`", "`lean/lakefile.lean:10`–`:486`", 1)),
    ("table row count shifted",
     lambda c, v, m: table_needle(c, v, m, "PrimeNumberTheoremAnd"),
     lambda p: p.replace("| PrimeNumberTheoremAnd | 244 | 39,904 |",
                         "| PrimeNumberTheoremAnd | 244 | 39,905 |", 1)),
    ("name dropped from the zero-import list",
     name_list_needle,
     lambda p: p.replace("`oka`, `orbicurve-cores`,", "`oka`,", 1)),
    ("patch-line total shifted", patch_total_needle,
     lambda p: p.replace("160,187", "160,186")),
    ("phase count shifted", phase_count_needle,
     lambda p: p.replace("| **11** | **6,658** |", "| **10** | **6,658** |", 1)),
    ("ordering-violation count shifted", violation_needle,
     lambda p: p.replace("and 5 entries violate it", "and 6 entries violate it", 1)),
    ("code span paraphrased",
     lambda c, v, m: span_needle(c, 's!".{label}-bootstrap-{pid}-{stamp}"'),
     lambda p: p.replace("`s!\".{plan.label}-bootstrap-{pid}-{stamp}\"`",
                         "`s!\".{label}-bootstrap-{pid}-{stamp}\"`", 1)),
    ("table row dropped", omits_needle,
     lambda p: p.replace("| orbicurve-cores | **0** | 695 |\n", "", 1)),
    # Prose no count phrase reads: the deps-record row count in the opening sources sentence.
    # Only the render diff can see it, so the needle is the page line the render diff names.
    ("prose row count outside the phrase list",
     lambda c, v, m: render_needle(c, "Measured 2026-10-07 from three sources only"),
     lambda p: p.replace("`notes/tables/formalization-deps.tsv` (31 rows, 8 fields)",
                         "`notes/tables/formalization-deps.tsv` (32 rows, 8 fields)", 1)),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8", errors="replace")


def test_clean_page(load, text):
    v = load("verify_dependency_drift")
    problems, (n_anchor, n_quote, n_span, n_table, n_sync) = v.check(text)
    assert problems == []
    assert (n_anchor, n_quote, n_span, n_table, n_sync) == (52, 7, 9, 23, 0)
    m = v.measure()
    assert (len(m["declared"]), len(m["patched"]), m["total_lines"], m["total_hunks"],
            m["tc_patches"], len(m["froms"])) == (30, 23, 160187, 734, 22, 8)
    assert (len(m["pre"]), len(m["post"]), len(m["zero"]), len(m["zero_nopatch"]),
            len(m["violations"])) == (11, 12, 19, 5, 5)
    assert (int(m["median_import"]), int(m["median_zero"])) == (2575, 408)
    assert set(m["pre"]).isdisjoint(m["post"])
    assert set(m["pre"]) | set(m["post"]) == set(m["patched"])
    assert set(m["lana"]) == set(m["pre"])


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_dependency_drift")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs = v.check(cand)[0]
    m = v.measure()
    want = needle(cand, v, m) if callable(needle) else needle
    assert any(want in p for p in probs), f"{label}: needle did not fire\n{probs}"


def pad_cells(t):
    """Pad every table cell with two spaces."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_dropped(load, text):
    """The opposite direction from the padding-tolerant checkers: the check-table reader (`:259`)
    matches rows with `startswith("| The ")`, so padding must drop every row, not be tolerated.
    Measured: 6 check rows on the clean page, 0 on the padded page, and the pass reports the row count
    against the prose figure. The patch-table reader (`:253`) splits and strips, so its 23 rows must
    survive padding. The page is prettier-ignored, so the padding never reaches the tracked tree; the
    test asserts the ignore rule too."""
    v = load("verify_dependency_drift")
    cand = pad_cells(text)
    assert cand != text, "padding changed nothing"
    assert len(v.table_rows(text)) == len(v.table_rows(cand)), \
        "the patch-table reader is strip-based, so padding must keep its rows"
    probs = v.check(cand)[0]
    assert any("drift table has 0 check rows" in p for p in probs), \
        f"padding did not drop the check rows: {probs[:3]}"
    ignore = pathlib.Path(".prettierignore").read_text(encoding="utf-8").splitlines()
    assert "notes/reports/*.md" in ignore, \
        "the dependency-drift page is not prettier-ignored, so a format pass would pad it"
