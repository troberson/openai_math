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
import pytest

pytestmark = pytest.mark.mutant

# Faults in the census page's own text, each keyed to the problem string the check prints.
PAGE_CASES = [
    ("writer target altered", "page says 'notes/catalog-x.tsv'",
     lambda t: t.replace("| `build_catalog.py` | `notes/tables/catalog.tsv` |",
                         "| `build_catalog.py` | `notes/catalog-x.tsv` |")),
    ("writer row deleted", "writer extract_links.py: page says None",
     lambda t: t.replace("| `extract_links.py` | `notes/tables/links.tsv` | single run; cached "
                         "bytes == promoted bytes under the key | `notes/reports/links.md` |\n", "")),
    ("generated TSV count understated", "tsv census cell",
     lambda t: t.replace("**23** generated, **2** hand-authored",
                         "**22** generated, **2** hand-authored")),
    ("index file count altered", "census row notes/index/",
     lambda t: t.replace("| `notes/index/` | **1,033** |", "| `notes/index/` | **1,034** |")),
    ("collision name altered", "collision sentence",
     lambda t: t.replace("**1** shared basename — `README.md`",
                         "**2** shared basenames — `README.md` and `topics.tsv`")),
    ("checker name altered", "non-writers",
     lambda t: t.replace("| `verify_sources.py` |", "| `verify_sources2.py` |")),
    ("unchecked page claimed as checked", "md census cell",
     lambda t: t.replace("| `verify_abstracts.py` | `notes/reports/abstracts.md` |",
                         "| `verify_abstracts.py` | `notes/reports/abstracts.md`, "
                         "`notes/reports/counterexample-tag.md` |")),
    ("Not checked section deleted", "no '## Not checked' section",
     lambda t: t.replace("## Not checked", "## Checked")),
    ("summaries count altered", "census row notes/summaries/",
     lambda t: t.replace("| `notes/summaries/` | **40** |", "| `notes/summaries/` | **25** |")),
    ("templates count altered", "census row notes/templates/",
     lambda t: t.replace("| `notes/templates/` | **24** |", "| `notes/templates/` | **3** |")),
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
     lambda t: t.replace("registry: **19** entries", "registry: **17** entries", 1)),
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


def test_clean_pages(mod):
    """The census page, the templates census, and the generated ledger readme are all silent."""
    assert mod.check(mod.read_text(mod.PAGE)) == [], mod.check(mod.read_text(mod.PAGE))[:3]
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
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            ln = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        out.append(ln)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod, page):
    cand = pad_cells(page)
    assert cand != page, "padding changed nothing"
    assert mod.census_rows(cand) == mod.census_rows(page), \
        f"padded census reads {mod.census_rows(cand)}, clean page {mod.census_rows(page)}"
    assert mod.check(cand) == mod.check(page), \
        f"padded page reports {mod.check(cand)}, clean page {mod.check(page)}"


def test_format_boundary_count_altered(mod, page):
    """Pass G re-measures the checker-parsed page population, so a page carrying a stale count is
    flagged by the measured figure, not by the sentence's shape."""
    cand = page.replace("**25** checker-parsed pages", "**24** checker-parsed pages", 1)
    assert cand != page, "format-boundary count altered: mutation changed nothing"
    needle = f"**{len(mod.checker_pages() | mod.test_pages())}** checker-parsed pages"
    found = mod.check(cand)
    assert any(needle in x for x in found), \
        f"format-boundary count altered: NOT caught ({found[:2]})"


def test_checker_parsed_page_not_ignored(mod, page):
    """Pass G reads the ignore rule from disk, so the mutation drops a rule in memory. Without
    `notes/reports/*.md` every report page a checker parses sits outside the rule, and the pass names
    each one."""
    real = mod.ignore_rules

    def fewer():
        return [(neg, rx) for neg, rx in real() if not rx.pattern.startswith(r"notes/reports/")]

    mod.ignore_rules = fewer
    found = mod.check(page)
    mod.ignore_rules = real
    assert any("checker-parsed page is not prettier-ignored" in x for x in found), \
        f"format-boundary rule dropped: NOT caught ({found[:2]})"
