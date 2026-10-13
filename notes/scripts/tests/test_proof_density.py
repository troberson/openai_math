"""The self-tests for `notes/scripts/measure_proof_density.py`.

The script measures proof density over the 719 manuscripts and tests whether it discriminates, under
a discrimination rule fixed before the statistics were run: a signal SEPARATES a tier pair when
AUC >= 0.65 and two-sided p < 0.01, and is SIZE-EXPLAINED on that pair when its AUC is within 0.03 of
the tex-KB AUC on the same pair. Every number it prints is derived from `notes/tables/sources.tsv`
joined to `notes/tables/catalog.tsv` by family number. The gates re-measure the population: rows,
distinct dirs, the family set on both sides, the per-family source rows against the ledger `paps`, the
proofs and statements sums, the tier counts, non-positive `tex_bytes`, negative counts, and every
source dir present under `preprints/`. The page check is not here: `notes/reports/proof-density.md` is
compared with `render_reports.py`'s render of it by `verify_page_sync.py`, which owns that pass.

This file injects eight faults into the TSV rows in memory and asserts each fires the gate that owns
it: a sources row dropped, a proofs count +1, a statements count +1, a family renamed, `tex_bytes`
zeroed, a tier label flipped, a dir row duplicated, and a negative proofs count.

Every fault is built from a real row of the two tables as committed. Each test asserts the mutated
rows differ from the rows they started from, and each needle is the gate problem string the pass that
owns that form prints — measured specific, each needle fires for its own fault and for no other. The
tier needle is `'T0': 129` rather than the whole dict, because the problem line prints the tier counts
in set-iteration order, which is not stable across processes.

The clean test asserts the gates are silent and pins the population they report: 719 sources rows over
719 distinct dirs, 372 families on both sides, 20,341 proofs, 21,288 statements, tiers
136/106/0/130, the ledger `paps` sum at 719, and the statistic self-test at 5/5 — the five
hand-computed AUCs, including the tie case `([1,2,3],[0,1,2])` at 7/9, which is 7/9 only when the
ranks are assigned over the jointly sorted pooled sample.

The script reads no argv, so `--mutant` and `--quiet` are inert, and the tests mutate rows in memory:
the script writes nothing and the tests write nothing.

The script measures; this file injects. Run:
  python3 notes/scripts/run_tests.py notes/scripts/tests/test_proof_density.py -q
"""
import pytest

pytestmark = pytest.mark.mutant

# Faults in the TSV rows, each keyed to the gate problem string the pass that owns it prints.
MUTANTS = [
    ("drop a sources row", "sources rows 718 != 719",
     lambda r, l: r.pop(0)),
    ("proofs +1 on one row", "proofs sum 20342 != 20341",
     lambda r, l: r[0].__setitem__("proofs", str(int(r[0]["proofs"]) + 1))),
    ("thms +1 on one row", "thms sum 21289 != 21288",
     lambda r, l: r[0].__setitem__("thms", str(int(r[0]["thms"]) + 1))),
    ("rename a family", "family sets differ: sources-only 1, ledger-only 1",
     lambda r, l: r[0].__setitem__("fam", "999")),
    ("zero tex_bytes", "1 rows with tex_bytes <= 0",
     lambda r, l: r[0].__setitem__("tex_bytes", "0")),
    ("flip a tier label", "'T0': 129",
     lambda r, l: l[0].__setitem__("tier", "T2")),
    ("duplicate a dir row", "sources rows 720 != 719",
     lambda r, l: r.append(dict(r[0]))),
    ("negative proofs", "1 rows with negative proofs/thms",
     lambda r, l: r[0].__setitem__("proofs", "-3")),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("measure_proof_density")


@pytest.fixture(scope="module")
def sources(mod):
    return [dict(r) for r in mod.read_tsv(mod.SOURCES)]


@pytest.fixture(scope="module")
def ledger(mod):
    return [dict(r) for r in mod.read_tsv(mod.LEDGER)]


def test_clean_population(mod, sources, ledger):
    """The gates are silent, and the population they report is pinned."""
    fams = mod.build_families(sources, ledger)
    problems = mod.gate_checks(sources, ledger, fams)
    assert not problems, problems[:3]
    assert len(sources) == 719 and len({r["dir"] for r in sources}) == 719, \
        f"rows {len(sources)}, dirs {len({r['dir'] for r in sources})}"
    assert len({r["fam"] for r in sources}) == 372 and len({r["fam"] for r in ledger}) == 372, \
        "family set not 372 on both sides"
    assert sum(int(r["proofs"]) for r in sources) == 20341, \
        f"proofs sum {sum(int(r['proofs']) for r in sources)}"
    assert sum(int(r["thms"]) for r in sources) == 21288, \
        f"thms sum {sum(int(r['thms']) for r in sources)}"
    tiers: dict = {}
    for d in fams.values():
        tiers[d["tier"]] = tiers.get(d["tier"], 0) + 1
    assert (tiers.get("T3", 0), tiers.get("T2", 0), tiers.get("T1", 0), tiers.get("T0", 0)) == \
        (136, 106, 0, 130), f"tier counts {tiers}"
    assert sum(int(r["paps"]) for r in ledger) == 719, f"ledger paps sum {sum(int(r['paps']) for r in ledger)}"


def test_statistic_selftest(mod):
    """The statistic is a claim too: the five hand-computed AUCs must all match."""
    ok, total = mod.selftest()
    assert (ok, total) == (5, 5), f"statistic self-test {ok}/{total}"


@pytest.mark.parametrize("label,needle,mut", MUTANTS)
def test_injected_faults(mod, label, needle, mut):
    """A fault in the rows, injected in memory. The needle is the gate problem string the pass that
    owns that form prints, so a gate that fires on something else is not a gate."""
    rows = [dict(r) for r in mod.read_tsv(mod.SOURCES)]
    led = [dict(r) for r in mod.read_tsv(mod.LEDGER)]
    before = [dict(r) for r in rows]
    mut(rows, led)
    assert rows != before or led != [dict(r) for r in mod.read_tsv(mod.LEDGER)], \
        f"{label}: mutation changed nothing"
    found = mod.gate_checks(rows, led, mod.build_families(rows, led))
    assert any(needle in x for x in found), f"{label}: NOT caught by {needle!r} ({found[:2]})"
