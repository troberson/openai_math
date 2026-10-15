r"""The extracted self-tests for `notes/scripts/verify_t0_chains.py` and `notes/reports/t0-chains.md`.

The checker's passes are: the anchor pass (every backticked `path:line` resolves to a file that
exists with the line in range); the fenced-block pass (each block attributed to the nearest preceding
anchor, matched as joined text against the same number of source lines); the quotation pass (each
*"…"* pinned to an anchor in its own row, verbatim modulo whitespace); the count pass (the count
phrases re-derived from the ledger, `notes/tables/subfindings.tsv`, `notes/reports/t0-triage.md` and
the `.bib` layer); the summary-table and chain-table passes (field by field); the family-block pass
(one block per population family, each naming exactly its own two manuscripts with titles verbatim on
the family's anchor line, and each Citation layer line matching the recomputed counts); the named-list
pass; the family-268 verification-directory pass; and the render diff against `render_reports.py`.

Each fault below mutates the page text in memory, so no page is written. `verify_t0_chains.py`'s
`population()` is under `functools.cache` (`:118`): the checker writes nothing and the tests mutate
page text, so a second call in the same process cannot see a different corpus, and the fifteen
`check()` calls this file makes pay the corpus walk once.

**The needles are derived at run time, not recorded.** A needle that quotes a page line has to be
re-measured by hand whenever the page's layout moves — measured 2026-10-13, one three-line paragraph
edit moved five needles and a declared line count. Each needle here is a function of the mutated page
and the checker's own measured population: the page line is found in the mutated text, the ledger
tier and the recomputed counts come from `population()`. A needle must fire for its own fault and for
no other, and must not fire on the clean page.

The last fault is not a content change: it pads the table cells. A row pattern that requires exactly
one space after each pipe reads **0** rows from the padded page, so the table pass is silently
skipped; the tolerant `\s*` form reads the same rows it reads from the clean page.
`test_padded_table_is_read_by_the_tolerant_pattern` pins the row count, which is the assertion that
distinguishes the two patterns — the padding needle fires against the pre-fix pattern too, because the
padded page differs from the writer's render either way.

Run: `python3 notes/scripts/run_tests.py notes/scripts/tests/test_t0_chains.py -q`
"""

import pathlib
import re

import pytest
import verify_t0_chains as v

PAGE = pathlib.Path("notes/reports/t0-chains.md")


def pad_table(p):
    r"""Pads every cell of every pipe-delimited table row with two spaces. The strict single-space
    row pattern reads 0 rows from this text; the tolerant `\s*` pattern reads the same rows it reads
    from the clean page."""
    out = []
    for line in p.split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            line = "| " + "  |  ".join(cells) + "  |"
        out.append(line)
    return "\n".join(out)


def row_of(text, sub):
    """The 1-based page line carrying `sub`. A sub that appears on more than one line makes the
    needle ambiguous, so the derivation fails loudly rather than picking the first."""
    lines = text.split("\n")
    hits = [i + 1 for i, line in enumerate(lines) if sub in line]
    assert len(hits) == 1, f"{sub!r} appears on {len(hits)} lines of the mutated page"
    return hits[0]


def anchor_of(text, n):
    """The `overview.tex:NNN` anchor on page line n."""
    return int(re.search(r"overview\.tex:(\d+)", text.split("\n")[n - 1]).group(1))


def block_start(text, n):
    """The 1-based page line the fenced-block pass reports for a block containing page line n: the
    pass names the opening fence, not the mutated line inside the block."""
    lines = text.split("\n")
    for i in range(n - 1, -1, -1):
        if lines[i].startswith("```"):
            return i + 1
    raise AssertionError(f"no opening fence above page line {n}")


def phrase(chk, m, label):
    """The count phrase the writer measures for `label`."""
    return next(p for p, lab in chk.count_phrases(m) if lab == label)


def citation(chk, fam):
    """The recomputed Citation layer triple for a family: `.bib` files, intra-family edges, mutual pairs."""
    m = chk.population()
    return (len(m["bibs"][fam]), len(m["fam_edges"][fam]), m["mutual"][fam])


def bump(p, pat, delta):
    """Change the page's own count at `pat` by `delta`, keeping its comma formatting. The mutation's
    input is the page as it stands, so a measured count that moves does not need a hand-edit here."""
    m = re.search(pat, p)
    assert m, f"{pat!r} not in the page"
    raw = m.group(1)
    n = int(raw.replace(",", ""))
    new = f"{n + delta:,}" if "," in raw else str(n + delta)
    span = m.group(0)
    return p[:m.start()] + span.replace(raw, new, 1) + p[m.end():]


def cell_set(p, key, idx, new):
    """Rewrite one cell of the table row carrying `key`, keeping the pipe-delimited form."""
    line = next(l for l in p.split("\n") if l.startswith("|") and key in l)
    cells = line.split("|")
    return p.replace(line, "|".join(cells[:idx] + [f" {new} "] + cells[idx + 1:]), 1)


def first_fam():
    """The first family of the population, which heads the summary table and its first block."""
    return v.population()["pop"][0]


def outside_fam():
    """A ledger family the population excludes — the block the page must not carry."""
    return next(f for f in sorted(v.population()["rows"]) if f not in v.population()["pop"])


def cite_bump(p, fam, delta):
    """Bump the intra-family-edge number in a family block's Citation layer line."""
    start = p.index("Citation layer: ", p.index(f"### {fam} — "))
    end = p.index("\n", start)
    line = p[start:end]
    m = list(re.finditer(r"\d+", line))[1]
    new = str(int(m.group()) + delta)
    return p[:start] + line[:m.start()] + new + line[m.end():] + p[end:]


def new_path():
    """The second manuscript of the first population family, with its filename changed."""
    return v.population()["mss"][first_fam()][1]["path"][:-4] + "x.pdf"


def quote_needle(sub):
    """The quotation pass's problem prefix for a mutated quote: the page line carrying `sub`, and the
    `overview.tex` anchor on that same line. `sub` must be unique in the mutated page, so it keys on
    the mutation's own byte, not on prose the page repeats."""
    def f(c, _v):
        n = row_of(c, sub)
        return f"quote at page line {n} is not on overview.tex:{anchor_of(c, n)}"
    return f


# (label, needle, mutation). A needle is a string, or a function of the mutated page and the loaded
# checker that returns the string the owning pass must print.
MUTANTS = [
    ("paraphrase dressed as a quotation",
     quote_needle("bound state for the SU(N) BFSS model"),
     lambda p: p.replace('*"The unique threshold bound state of the SU(N) BFSS model"*',
                         '*"The unique threshold bound state for the SU(N) BFSS model"*')),
    ("title swap",
     quote_needle("`overview.tex:625`) — *\"Positive eigenvalues"),
     lambda p: p.replace('*"Boundary-field gap"*',
                         '*"Positive eigenvalues of the relative SU(2) BFSS Hamiltonian"*')),
    ("chain table tier",
     lambda c, v: (f"chain table {v.CHAIN_FAMS[0]} tier 'T2' != ledger "
                   f"{v.population()['rows'][v.CHAIN_FAMS[0]]['tier']!r}"),
     lambda p: cell_set(p, f"| {v.CHAIN_FAMS[0]} |", 2, "T2")),
    ("edge count",
     lambda c, v: f"count phrase missing (intra-family edges): {phrase(v, v.population(), 'intra-family edges')!r}",
     lambda p: bump(p, r"\*\*(\d+)\*\* of the \d+ cite their sibling", 1)),
    ("anchor line out of range",
     lambda c, v: (f"anchor line out of range: overview.tex:9999 (file has "
                   f"{len(v.population()['overview'])} lines, page line "
                   f"{row_of(c, '(`overview.tex:9999`)')}"),
     lambda p: p.replace(re.search(r"\(`overview\.tex:\d+\`\)", p).group(0),
                         "(`overview.tex:9999`)", 1)),
    ("block for a family outside the population",
     lambda c, v: f"{outside_fam()}: block for a family outside the population",
     lambda p: p.replace(f"### {first_fam()} — ", f"### {outside_fam()} — ", 1)),
    ("table .bib count",
     lambda c, v: (f"{first_fam()}: table .bib {len(v.population()['bibs'][first_fam()]) + 1} "
                   f"!= recomputed {len(v.population()['bibs'][first_fam()])}"),
     lambda p: cell_set(p, f"| {first_fam()} |", 4,
                        str(len(v.population()["bibs"][first_fam()]) + 1))),
    ("manuscript path not on disk",
     lambda c, v: f"{first_fam()}/2: path {new_path()!r} != subfindings path",
     lambda p: p.replace(f"`{v.population()['mss'][first_fam()][1]['path']}`",
                         f"`{new_path()}`", 1)),
    ("population count phrase",
     lambda c, v: (f"count phrase missing (population): "
                   f"{phrase(v, v.population(), 'population')!r}"),
     lambda p: bump(p, r"\*\*(\d+)\*\* families carrying", 1)),
    ("mutual pairs list",
     lambda c, v: ("named list mismatch (mutual pairs): expected "
                   f"'{', '.join(v.population()['mutual_fams'])}'"),
     lambda p: p.replace(
         f"The mutual pairs are {', '.join(v.population()['mutual_fams'])}.",
         f"The mutual pairs are {', '.join(v.population()['mutual_fams'][1:])}.", 1)),
    ("fenced block line",
     lambda c, v: f"block at page line {block_start(c, row_of(c, 'journal = {Selecta Math.},'))} does not match",
     lambda p: p.replace("  journal = {Selecta Mathematica. New Series},",
                         "  journal = {Selecta Math.},")),
    ("citation layer count",
     lambda c, v: (f"{first_fam()}: citation layer "
                   f"{tuple(int(x) for x in v.CITE.search(v.collapse_ws(c)).groups())} "
                   f"!= recomputed {citation(v, first_fam())}"),
     lambda p: cite_bump(p, first_fam(), 1)),
    # Prose no count phrase reads: the heading name in the population rule. Only the render diff
    # sees it, so the needle is the page line the render diff names.
    ("prose count outside the phrase list",
     lambda c, v: f"page line {row_of(c, 'the remaining 94 families')}: page 'the remaining 94 families",
     lambda p: bump(p, r"the remaining (\d+) families", 1)),
    # Not a content change: the table is padded. A strict single-space row pattern reads 0 rows and
    # the population guard fires; the tolerant `\s*` pattern reads the rows, so the only problems are
    # the render diff, whose first changed line is the padded chain-table header.
    ("padded table cells",
     lambda c, v: f"page line {row_of(c, '| Fam  |  Tier  |')}: page '| Fam  |",
     pad_table),
]


@pytest.fixture(scope="module")
def text():
    return PAGE.read_text(encoding="utf-8")


def test_clean_page(load, text):
    v = load("verify_t0_chains")
    res = v.check(text)
    assert res["problems"] == []
    assert res["sync"] == 0
    carried = len(v.ANCHOR.findall(text))
    assert 0 < carried == res["anchors"]
    n_block = len(list(v.anchors.fenced_blocks(text.split("\n"))))
    assert 0 < n_block == res["blocks"]
    # The quote pass counts only the quotations pinned to an anchor, so the page carries more
    # quotations than the pass verifies.
    n_quote = len(v.QUOTE.findall(text))
    assert 0 < res["quotes"] <= n_quote
    want = len(list(v.count_phrases(v.population())))
    assert 0 < want == res["counts"]
    assert 0 < len(v.population()["pop"]) == res["sum_rows"] == res["heads"]
    assert 0 < len(v.CHAIN_FAMS) == res["chain_rows"]
    assert 0 < v.population()["mss_n"] == res["bullets"]
    # The pass counts its three named lists plus the no-.bib sentence: the checker's own structure,
    # not a measured figure.
    assert res["lists"] == 4
    assert 0 < len(v.VER268) == res["files"]


def test_padded_table_is_read_by_the_tolerant_pattern(load, text):
    r"""The discriminating assertion for the padding fault: the padded page must yield the same row
    counts as the clean page. A row pattern that requires exactly one space after each pipe reads 0
    summary rows and 0 chain rows from the padded text, so the table pass reports nothing about the
    table and the page reads clean apart from the population guard; the tolerant `\s*` pattern reads
    the rows. Measured 2026-10-13: 0 / 0 against the pre-fix pattern, 27 / 5 against the fixed one."""
    v = load("verify_t0_chains")
    clean = v.check(text)
    res = v.check(pad_table(text))
    assert res["sum_rows"] == clean["sum_rows"] == len(v.population()["pop"]), \
        f"{res['sum_rows']} summary rows read from the padded table"
    assert res["chain_rows"] == clean["chain_rows"] == len(v.CHAIN_FAMS), \
        f"{res['chain_rows']} chain rows read from the padded table"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(load, text, label, needle, mut):
    v = load("verify_t0_chains")
    cand = mut(text)
    assert cand != text, f"{label}: the page text changed, the needle is stale"
    probs = v.check(cand)["problems"]
    want = needle(cand, v) if callable(needle) else needle
    assert any(want in p for p in probs), f"{label}: needle did not fire\n{probs}"
