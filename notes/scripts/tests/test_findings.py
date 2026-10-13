"""The self-tests for `notes/scripts/verify_findings.py`.

The checker verifies `notes/reports/findings.md` in seven passes: the Sources table (rows exist, declare the
line count they have, every row is cited, the body's `[Sn]` markers are contiguous and in first-use
order), anchored quotations (a quotation next to a `[Sn:line]` marker must appear, markup aside, on
the lines it cites), the ledger (every catalog row rebuilt from the shipped files through `catlib`'s
parse functions, never through `build_catalog.main()`, which writes the TSV), the TSV and on-disk
counts, the extractors' own reports as subprocesses, the record-quoted counts, and the closing
`## Not checked` section with no preamble. This file injects six faults, one per check form the page
uses, and asserts each fires the pass that owns it: a quotation word changed, a real quotation cited
to the neighbouring line, a quotation fabricated, a ledger count moved, a Sources row deleted, and a
Sources line count aged.

Every fault is built from a real quotation, a real marker, a real count phrase, a real row and a real
line count in the page as committed, so a checker that only re-reads its own regexes cannot pass. Each
test asserts the injected text differs from the page it started from, and each needle is the problem
string the pass that owns that form prints — measured specific, each needle fires for its own fault and
for no other.

The clean test asserts the passes are silent on the page as committed, and pins the two population
counts the passes report: 31 Sources rows and 12 anchored quotations verified. A page with fewer
anchored quotations is a pass that stopped checking, not a pass that passed.

The checker reads no argv and `check()` takes page text, so nothing here writes a page: the checker
writes nothing and the tests write nothing.

The checker measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_findings.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Faults in the page's own text, each keyed to the problem string the pass that owns it prints.
MUTANTS = [
    ("quotation word altered", "conditional-ish",
     lambda t: t.replace("Five families are genuinely conditional",
                         "Five families are genuinely conditional-ish", 1)),
    ("quotation cited to the neighbouring line", "S8:8-8 carries no quotation",
     lambda t: t.replace("[S8:7]", "[S8:8]", 1)),
    ("fabricated quotation", "121 of 242 scope notes state at",
     lambda t: t.replace('"121 of 242 sections state at', '"121 of 242 scope notes state at')),
    ("ledger count moved", "count not stated as measured: T3 136 · T2 106",
     lambda t: t.replace("T3 136 · T2 106", "T3 137 · T2 105", 1)),
    ("Sources row deleted", "marker S14 cites no Sources row",
     lambda t: "\n".join(l for l in t.splitlines() if not l.startswith("| S14 |"))),
    ("Sources line count aged", "declares 896 lines",
     lambda t: t.replace("| 897 |", "| 896 |", 1)),
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
    cand = mut(page)
    assert cand != page, f"{label}: mutation changed nothing"
    found, _, _, _ = mod.check(cand)
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
