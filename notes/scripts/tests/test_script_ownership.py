"""The self-tests for `notes/scripts/verify_script_ownership.py`.

The census derives the writer set from the scripts' own source, re-measures every count in
`notes/scripts/README.md`, requires every script to be named in the page and in the ledger readme's
command block, and compares the generated `notes/README.md` with the writer's render of it. This
file injects eighteen faults, one per check form the page uses, and asserts each is caught by the
pass that owns it: eleven faults in the census page's text, one prose count in the generated ledger
readme (which only the render diff can see), four faults in `notes/development/templates.md`, and two faults in
the writer sources that move a write target out of the derived writer set.

Every fault is built from a real row, a real count, and a real line of a real file, so a checker
that only re-reads its own regexes cannot pass. Each test asserts the injected text differs from the
page it started from. The clean test asserts all three passes are silent on the pages as committed.

The passes take page text, so nothing here writes a page: the census checker writes nothing and the
tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_script_ownership.py -q
"""
import re

import pytest

pytestmark = pytest.mark.mutant


def bump(t, pat, delta=1):
    """Find the page's own count phrase by shape and change its number. The mutation's input is the
    page as it stands, not a transcription of a measured value, so a count that moves with the corpus
    does not require a hand-edit here."""
    m = re.search(pat, t)
    assert m, f"{pat!r} not in the page"
    raw = m.group(1)
    n = int(raw.replace(",", ""))
    new = f"{n + delta:,}" if "," in raw else str(n + delta)
    span = t[m.start():m.end()]
    assert f"**{raw}**" in span, f"no bolded {raw!r} in the matched span"
    return t[:m.start()] + span.replace(f"**{raw}**", f"**{new}**", 1) + t[m.end():]



# Faults in the census page's own text, each keyed to the problem string the check prints.
PAGE_CASES = [
    ("writer target altered", "page says 'notes/catalog-x.tsv'",
     lambda t: t.replace("| `build_catalog.py` | `notes/gen/tables/catalog.tsv` |",
                         "| `build_catalog.py` | `notes/catalog-x.tsv` |")),
    ("writer row deleted", "writer extract_links.py: page says None",
     lambda t: t.replace("| `extract_links.py` | `notes/gen/tables/links.tsv` | single run; cached "
                         "bytes == promoted bytes under the key | `notes/gen/reports/links.md` |\n", "")),
    ("generated TSV count understated", "tsv census cell",
     lambda t: bump(t, r"\*\*(\d+)\*\* generated, \*\*\d+\*\* hand-authored", -1)),
    ("index file count altered", "census row notes/gen/index/",
     lambda t: bump(t, r"\| `notes/gen/index/` \| \*\*([\d,]+)\*\* \|", 1)),
    ("collision name altered", "collision sentence",
     lambda t: bump(t, r"\*\*(\d+)\*\* shared basename", 1)),
    ("checker name altered", "non-writers",
     lambda t: t.replace("| `verify_sources.py` |", "| `verify_sources2.py` |")),
    ("unchecked page claimed as checked", "md census cell",
     lambda t: t.replace("| `verify_abstracts.py` | `notes/gen/reports/abstracts.md` |",
                         "| `verify_abstracts.py` | `notes/gen/reports/abstracts.md`, "
                         "`notes/gen/reports/counterexample-tag.md` |")),
    ("Not checked section deleted", "no '## Not checked' section",
     lambda t: t.replace("## Not checked", "## Checked")),
    ("summaries count altered", "census row notes/gen/summaries/",
     lambda t: bump(t, r"\| `notes/gen/summaries/` \| \*\*(\d+)\*\* \|", -15)),
    ("templates count altered", "census row notes/templates/",
     lambda t: bump(t, r"\| `notes/templates/` \| \*\*(\d+)\*\* \|", -24)),
]

def shift_slot_cell(t):
    """Shift the slot-count cell of the README.md.j2 row. The row's line, byte and slot counts are
    measured from the template, so the fault has to be built from the row as it stands, not from a
    literal transcription of them."""
    row = next((l for l in t.splitlines() if l.startswith("| `README.md.j2`")), "")
    cells = row.split("|")
    cells[4] = f" {int(cells[4]) + 1} "
    return t.replace(row, "|".join(cells), 1)


# Faults in the templates census page, each keyed to the pass that owns it.
TPL_CASES = [
    ("template row renamed", "report table rows",
     lambda t: t.replace("| `t0-chains.md.j2` |", "| `t0-chainz.md.j2` |", 1)),
    ("template page row deleted", "report table rows",
     lambda t: "\n".join(l for l in t.splitlines()
                         if not l.startswith("| `templates.md.j2`"))),
    ("template slot count shifted", "template row README.md.j2", shift_slot_cell),
    ("registry count altered", "registry sentence",
     lambda t: bump(t, r"registry: \*\*(\d+)\*\* entries", -5)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_script_ownership")


@pytest.fixture(scope="module")
def page(mod):
    return mod.read_text(mod.PAGE)


@pytest.fixture(scope="module")
def tpl(mod):
    return mod.read_text(mod.TEMPLATES_PAGE)


def cost_row(t, name):
    """The Cost table's own row for a checker."""
    return next(l for l in t.splitlines() if l.startswith(f"| `{name}`"))


def shift_cost_cell(t, name, delta=1.0):
    """Shift the Wall cell of a checker's row. The cell is measured from the gate run, so the fault is
    built from the row as it stands, not from a transcription of the measured time."""
    row = cost_row(t, name)
    cells = row.split("|")
    cells[-2] = f" {float(cells[-2]) + delta:.1f} "
    return t.replace(row, "|".join(cells), 1)


def shift_read_cell(t, name, delta=1):
    """Shift the Read cell of a checker's row. The cell is the checker's CHECKER_L1 entry length, so
    the fault is built from the row as it stands. A dash (an unkeyable row) cannot be shifted."""
    row = cost_row(t, name)
    cells = row.split("|")
    if cells[-4].strip() == "—":
        raise AssertionError(f"no numeric Read cell to shift on {name}'s row")
    cells[-4] = f" {int(cells[-4]) + delta} "
    return t.replace(row, "|".join(cells), 1)


def delete_cost_row(t, name):
    """Delete a checker's Cost row. The checker stays a gate row, so the page must account for it."""
    return t.replace(cost_row(t, name) + "\n", "", 1)


def cost_para(t, name):
    """The Cost-section paragraph for a checker: the line range beginning with the checker's name in
    backticks, ending at the next checker-name paragraph. A continuation line can begin with a
    backtick, so the boundary is the next paragraph naming a checker, not the next backtick."""
    lines = t.split("\n")
    starts = [k for k, l in enumerate(lines) if l.startswith("`verify_")]
    for i, k in enumerate(starts):
        if not lines[k].startswith(f"`{name}`"):
            continue
        end = starts[i + 1] if i + 1 < len(starts) else len(lines)
        seg = "\n".join(lines[k:end])
        if re.search(r"`run_tests\.py` row measures\s+\*\*[0-9.]+ s\*\*", seg):
            off = sum(len(x) + 1 for x in lines[:k])
            return off, off + sum(len(x) + 1 for x in lines[k:end])
    raise AssertionError(f"no Cost paragraph carries {name}'s run_tests figure")


def bump_calls(t, name, delta=1):
    """Change the `check()` count inside the checker's own Cost paragraph."""
    lo, hi = cost_para(t, name)
    m = re.search(r"the\s+(\d+)\s+`check\(\)`\s+calls", t[lo:hi])
    assert m, f"no check() count in the Cost paragraph for {name}"
    raw = m.group(1)
    new = str(int(raw) + delta)
    s, e = lo + m.start(), lo + m.end()
    return t[:s] + t[s:e].replace(raw, new, 1) + t[e:]


def delete_para(t, name):
    """Delete the checker's Cost paragraph."""
    lo, hi = cost_para(t, name)
    return t[:lo] + t[hi:]


def bump_num(t, pat, delta=1.0):
    """Find the page's own count phrase by shape and change its number, so a figure that moves with
    the gate run does not require a hand-edit here."""
    m = re.search(pat, t)
    assert m, f"{pat!r} not in the page"
    raw = m.group(1)
    new = f"{float(raw) + delta:.1f}"
    span = t[m.start():m.end()]
    return t[:m.start()] + span.replace(raw, new, 1) + t[m.end():]


# Faults in the Cost section, each keyed to the pass that owns it. Every figure the pass compares is
# measured: the Cold and Wall cells come from notes/gen/tables/gate-rows.tsv, the check() counts from the
# keyed check_calls.json record. The self-test row times are not in the page — a run-dependent figure
# cannot live in a template keyed to HEAD — so there is no row-figure mutant to inject.
COST_CASES = [
    ("Wall cell altered", "Wall cell for verify_findings.py",
     lambda t: shift_cost_cell(t, "verify_findings.py")),
    ("Read cell altered", "Read cell for verify_findings.py",
     lambda t: shift_read_cell(t, "verify_findings.py")),
    ("Cost row deleted", "is a checker row the Cost table does not carry",
     lambda t: delete_cost_row(t, "verify_findings.py")),
    ("check() count altered", "verify_named_results: the check() count is not 15",
     lambda t: bump_calls(t, "verify_named_results.py")),
    ("check() sentence deleted", "verify_citations: the check() count is not 12",
     lambda t: delete_para(t, "verify_citations.py")),
    ("checker sum altered", "the checker sum is not",
     lambda t: bump_num(t, r"The\s+\d+\s+checker\s+invocations\s+sum\s+to\s+\*\*([0-9.]+)\s+s\*\*")),
    ("row sum altered", "the row sum is not",
     lambda t: bump_num(t, r"row\s+times\s+sum\s+to\s+\*\*([0-9.]+)\s+s\*\*")),
    ("heaviest-row claim altered", "the heaviest row with a Wall cell is not",
     lambda t: bump_num(t, r"\*\*([0-9.]+)\s+s\*\*\s+is\s+the\s+heaviest\s+row\s+with\s+a\s+Wall\s+cell")),
    ("tail figure altered", "the tail names render_reports.py",
     lambda t: bump_num(t, r"`render_reports\.py`\s+([0-9.]+)\s+s")),
]

# Faults in the catlib read-surface sentence, each keyed to the needle the importer pass prints. The
# census page's importer figure is a literal the pass re-derives from the scripts' own sources (the
# rule the page names), so every figure is witnessed, not hand-swept. The count mutants are live
# because the page's literal agrees with the measurement; the non-importer faults move the anchors
# behind the count, not the count alone.
IMPORTER_CASES = [
    ("importer count altered", "importer sentence does not read",
     lambda t: bump(t, r"\*\*(\d+)\*\* of the \*\*\d+\*\* scripts call the package", -1)),
    ("measure_ count altered", "the measure_ importer count is not",
     lambda t: bump(t, r"\*\*(\d+)\*\* `measure_`", -1)),
    ("non-importer dropped", "non-importer list: page names",
     lambda t: t.replace("`measure_proof_density.py` and `measure_topics.py`, which",
                         "`measure_proof_density.py`, which", 1)),
    ("non-importer added", "non-importer list: page names",
     lambda t: t.replace("`check_gate_budget.py`, which reads",
                         "`check_gate_budget.py`, `zz_invented.py`, which reads", 1)),
]


@pytest.mark.parametrize("label,needle,mut", COST_CASES)
def test_cost_section_faults(mod, page, label, needle, mut):
    """A Wall cell, a row, a row figure, a check() count, or a sum in the Cost section, altered in
    memory. The pass re-derives every figure from the gate row TSV and the keyed record, so a checker
    that carried the numbers would report green on all ten."""
    cand = mut(page)
    assert cand != page, f"{label}: mutation changed nothing"
    found = mod.cost_problems(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


@pytest.mark.parametrize("label,needle,mut", IMPORTER_CASES)
def test_importer_sentence_faults(mod, page, label, needle, mut):
    """The importer count, a per-prefix count, or a non-importer name in the read-surface sentence,
    altered in memory. The pass re-derives the census from the scripts' own sources, so a page that
    carried the numbers would report green on all four."""
    cand = mut(page)
    assert cand != page, f"{label}: mutation changed nothing"
    found = mod.importer_problems(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


def test_clean_pages(mod):
    """The census page, the templates census, and the generated ledger readme are all silent."""
    assert mod.check(mod.read_text(mod.PAGE)) == [], mod.check(mod.read_text(mod.PAGE))[:3]
    assert mod.cost_problems(mod.read_text(mod.PAGE)) == [], \
        mod.cost_problems(mod.read_text(mod.PAGE))[:3]
    assert mod.templates_problems(mod.read_text(mod.TEMPLATES_PAGE)) == [], \
        mod.templates_problems(mod.read_text(mod.TEMPLATES_PAGE))[:3]
    assert mod.sync_problems(mod.README, mod.read_text(mod.README)) == [], \
        mod.sync_problems(mod.README, mod.read_text(mod.README))[:2]


@pytest.mark.parametrize("label,needle,mut", PAGE_CASES)
def test_census_page_faults(mod, page, label, needle, mut):
    """A count, a row, a name, or a section heading in the census page, altered in memory. The
    writer-count fault is derived from the measured writer set, so it is a separate test."""
    cand = mut(page)
    assert cand != page, f"{label}: mutation changed nothing"
    found = mod.check(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


def test_writer_count_altered(mod, page):
    """The writer split sentence names the measured writer count, so the fault has to be built from
    the measurement, not from a literal in the page."""
    n = len(mod.script_names())
    w = len(mod.writers())
    cand = page.replace(f"**{w}** writers over **{n}** scripts",
                        f"**{w - 1}** writers over **{n}** scripts")
    assert cand != page, "writer count altered: mutation changed nothing"
    found = mod.check(cand)
    assert any("writer split sentence" in x for x in found), \
        f"writer count altered: NOT caught ({found[:2]})"


def test_readme_prose_count_altered(mod):
    """No census check reads notes/README.md prose, so only the render diff sees a prose count moved.
    The page is generated, so the fault is injected in memory and the writer's render stays right."""
    text = mod.read_text(mod.README)
    cand = text.replace("A README section names 28 of the 30",
                        "A README section names 29 of the 30", 1)
    assert cand != text, "readme prose count altered: mutation changed nothing"
    found = mod.sync_problems(mod.README, cand)
    assert found, "readme prose count altered: NOT caught by the sync pass"
    assert any("page is not the writer's render" in x for x in found), \
        f"readme prose count altered: the sync pass printed {found[:2]}"


@pytest.mark.parametrize("label,needle,mut", TPL_CASES)
def test_templates_page_faults(mod, tpl, label, needle, mut):
    """A row, a slot count, or the registry sentence in notes/development/templates.md, altered in memory."""
    cand = mut(tpl)
    assert cand != tpl, f"{label}: mutation changed nothing"
    found = mod.templates_problems(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"


def test_atomic_write_retargeted(mod):
    """The derivation must key on the target the writer hands the package, not on the call name. A
    writer that retargets away from notes/ has to drop out of the writer set."""
    src = mod.read_text(mod.SCRIPTS / "render_reports.py")
    cand = src.replace("ST.stage(README_MD, render_page(README_MD))",
                       'ST.stage(pathlib.Path("README.md"), render_page(README_MD))', 1)
    assert cand != src, "atomic write retargeted: mutation changed nothing"
    before = mod.writer_targets(src)
    assert "notes/README.md" in before, "the clean source does not carry the target"
    assert "notes/README.md" not in mod.writer_targets(cand), \
        f"atomic write retargeted: NOT caught ({mod.writer_targets(cand)[:4]})"


def test_record_store_write_retargeted(mod):
    """`cached(KEY, "names.json", builder)` names no path, so the rule keys on the literal record
    name. A record name held in a variable is not a target the source writes down."""
    src = mod.read_text(mod.SCRIPTS / "measure_names.py")
    cand = src.replace('cached(KEY, "names.json", build_records)',
                       "cached(KEY, rec_name, build_records)", 1)
    assert cand != src, "record-store write retargeted: mutation changed nothing"
    want = mod.RECORD_PREFIX + "names.json"
    assert want in mod.writer_targets(src), "the clean source does not carry the target"
    assert want not in mod.writer_targets(cand), \
        f"record-store write retargeted: NOT caught ({mod.writer_targets(cand)[:4]})"


def pad_cells(t):
    """Pad every table cell with two spaces. The census and writers readers split each row and strip
    every cell, so padding must read the same rows; a byte-exact single-space row regex reads 9 of the
    10 clean census rows and 0 padded ones, and the pass then reports a census row for every target
    with `page says None`, so the problem list is the discriminator."""
    out = []
    for row in t.split("\n"):
        if row.startswith("|") and row.endswith("|"):
            cells = row[1:-1].split("|")
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = row
        out.append(padded)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod, page):
    cand = pad_cells(page)
    assert cand != page, "padding changed nothing"
    assert mod.census_rows(cand) == mod.census_rows(page), \
        f"padded census reads {mod.census_rows(cand)}, clean page {mod.census_rows(page)}"
    assert mod.check(cand) == mod.check(page), \
        f"padded page reports {mod.check(cand)}, clean page {mod.check(page)}"
