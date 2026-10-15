r"""The self-tests for `notes/scripts/verify_findings.py`.

The checker verifies `notes/reports/findings.md` in seven passes: the Sources table (rows exist, declare
the line count they have, every row is cited, the body's `[Sn]` markers are contiguous and in first-use
order), anchored quotations (a quotation next to a `[Sn:line]` marker must appear, markup aside, on the
lines it cites), the ledger (every catalog row rebuilt from the shipped files through `catlib`'s parse
functions, never through `build_catalog.main()`, which writes the TSV), the TSV and on-disk counts, the
extractors' own reports as subprocesses, the record-quoted counts, and the closing `## Not checked`
section with no preamble. This file injects six faults, one per check form the page uses, and asserts
each fires the pass that owns it: a quotation word changed, a real quotation cited to the neighbouring
line, a quotation fabricated, a ledger count moved, a Sources row deleted, and a Sources line count aged.

Every fault is built from a real quotation, a real marker, a real count phrase, a real row and a real
line count in the page as committed, so a checker that only re-reads its own regexes cannot pass. Each
test asserts the injected text differs from the page it started from, and each needle is the problem
string the pass that owns that form prints — measured specific, each needle fires for its own fault and
for no other.

**The needles that quote a measured figure are derived at run time, not recorded.** The ledger-count
fault's needle is the tier phrase `needles(measured())` builds, so a tier shift moves the needle with
the measurement; the aged-line-count fault's needle is the targeted row's real file length minus one,
read from the file. The needles that stay literal are the mutation's own inputs — the word inserted,
the phrase fabricated, the row id deleted — which are the fault's identity, not corpus measurements.

The clean test asserts the passes are silent on the page as committed, and pins the two population
counts the passes report: 31 Sources rows and 12 anchored quotations verified. A page with fewer
anchored quotations is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_findings.py -q
"""
import re

import pytest
from catlib.text import first_group

pytestmark = pytest.mark.mutant

# The Sources row whose declared line count the aging fault ages.
AGED = "S11"
# The Sources row whose deletion the row-deletion fault removes.
DELETED = "S14"


def row_lines(mod, sid):
    """The real line count of the file the Sources row `sid` names."""
    table = mod.sources_rows(mod.PAGE.read_text(encoding="utf-8").splitlines())
    return len((mod.ROOT / table[sid][0]).read_text(encoding="utf-8", errors="replace").splitlines())


def first_marker(c):
    """The first line-numbered `[Sn:line]` marker in the mutated page's body — the marker the
    quotation pass reports first, which is the one the marker-move fault moves."""
    flat = re.sub(r"\s+", " ", c.split("## Sources")[0])
    m = next(m for m in re.finditer(r"\[S(\d+)(?::(\d+)(?:[–-](\d+))?)?\]", flat) if m.group(2))
    return f"S{m.group(1)}:{m.group(2)}-{m.group(2)}"


def tier_phrase(mod, m):
    """The tier count phrase the checker requires the page to carry."""
    return next(n for n in mod.needles(m) if n.startswith("T3 "))


def shift_tier(text, phrase):
    """Move the two tier counts the measured phrase carries, so the page states counts the
    measurement does not support. The numbers come from the phrase, not from a recorded literal."""
    t3 = int(first_group(r"T3 (\d+)", phrase))
    t2 = int(first_group(r"T2 (\d+)", phrase))
    return text.replace(phrase, phrase.replace(f"T3 {t3}", f"T3 {t3 + 1}")
                        .replace(f"T2 {t2}", f"T2 {t2 - 1}"), 1)


# (label, needle, mutation). A needle is a function of the mutated page, the loaded checker and the
# measured dict; a mutation is a function of the page and the checker.
MUTANTS = [
    ("quotation word altered",
     lambda c, mod, m: "conditional-ish",
     lambda t, mod: t.replace("Five families are genuinely conditional",
                             "Five families are genuinely conditional-ish", 1)),
    ("quotation cited to the neighbouring line",
     lambda c, mod, m: f"{first_marker(c)} carries no quotation",
     lambda t, mod: t.replace("[S8:7]", "[S8:8]", 1)),
    ("fabricated quotation",
     lambda c, mod, m: "121 of 242 scope notes state at",
     lambda t, mod: t.replace('"121 of 242 sections state at', '"121 of 242 scope notes state at')),
    ("ledger count moved",
     lambda c, mod, m: f"count not stated as measured: {tier_phrase(mod, m)[:80]}",
     lambda t, mod: shift_tier(t, tier_phrase(mod, mod.measured())[:80])),
    ("Sources row deleted",
     lambda c, mod, m: f"marker {DELETED} cites no Sources row",
     lambda t, mod: "\n".join(l for l in t.splitlines() if not l.startswith(f"| {DELETED} |"))),
    ("Sources line count aged",
     lambda c, mod, m: f"declares {row_lines(mod, AGED) - 1} lines",
     lambda t, mod: t.replace(f"| {row_lines(mod, AGED)} |", f"| {row_lines(mod, AGED) - 1} |", 1)),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("verify_findings")


@pytest.fixture(scope="module")
def page(mod):
    return (mod.NOTES / "reports" / "findings.md").read_text(encoding="utf-8")


def test_clean_page(mod, page):
    """All seven passes are silent, and the two population counts the passes report are pinned."""
    problems, _, table, quotes = mod.check(page)
    assert not problems, problems[:3]
    assert table == 31, f"Sources rows {table}, not 31"
    assert quotes == 12, f"anchored quotations {quotes}, not 12: the quotation pass is not checking"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, page, label, needle, mut):
    """A fault in each of the check forms, injected in memory. The needle is the problem string the
    pass that owns that form prints, so a pass that fires on something else is not a pass."""
    cand = mut(page, mod)
    assert cand != page, f"{label}: mutation changed nothing"
    found, m, _, _ = mod.check(cand)
    want = needle(cand, mod, m)
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def pad_cells(t):
    """Pad every table cell with two spaces. The row regex allows whitespace, so the sources pass must
    read the same rows; a regex that required exact spacing would drop rows, and the render diff fires
    for the padding either way, so the row count is the discriminator."""
    out = []
    for ln in t.split("\n"):
        if ln.startswith("|") and ln.endswith("|"):
            cells = ln[1:-1].split("|")
            padded = "|" + "|".join("  " + c.strip() + "  " for c in cells) + "|"
        else:
            padded = ln
        out.append(padded)
    return "\n".join(out)


def test_padded_table_cells_are_still_read(mod, page):
    cand = pad_cells(page)
    assert cand != page, "padding changed nothing"
    problems, _m, table, _q = mod.check(cand)
    src = [p for p in problems if "Sources" in p]
    assert not src, f"padded rows are not read: {src[:2]}"
    assert table == mod.check(page)[2], \
        f"padded table reads {table} rows, clean page {mod.check(page)[2]}"
