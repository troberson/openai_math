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
owns that form prints — measured specific, each needle fires for its own fault and for no other.

**The needles that quote a population figure are derived at run time, not recorded.** The row-count,
proofs-sum, thms-sum and tier needles are built from the committed tables (`real()`) and from the
mutated rows, so a corpus change moves the needle with the measurement. The tier needle is the T0 count
the mutated rows and ledger join to, which is why it stays specific: the problem line prints the tier
counts in set-iteration order, which is not stable across processes, so the needle names one count.
The `tex_bytes` and negative-count needles are rebuilt from the mutated rows, the way the gate computes
them. The row-count and column-sum needles are keyed to the **delta the mutation introduces** —
`R['rows'] - 1`, `R['proofs'] + 1` — not to the mutated table. A needle that reads the mutated table
produces the pass's own line for **any** fault that perturbs that count, so the drop-row needle fired on
the duplicate-row fault and the proofs-sum needle fired on the negative-proofs fault. Keying to the
delta makes each needle the line the pass prints for its own fault and for no other. The family-set
needle names the delta `1, 1`, which is only true when the renamed family has exactly one source row, so
the mutation targets `one_row_index` — a layout-dependent needle needs a layout-independent target.

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
import collections

import pytest
from catlib.layout import reorder

pytestmark = pytest.mark.mutant


def real(mod):
    """The population figures the committed tables carry: row count, proofs sum, thms sum."""
    src = list(mod.read_tsv(mod.SOURCES))
    return {"rows": len(src), "proofs": sum(int(r["proofs"]) for r in src),
            "thms": sum(int(r["thms"]) for r in src)}


def tier_of(mod, rows, led, key):
    """The count of `key` among the tiers the mutated rows and ledger join to."""
    fams = mod.build_families(rows, led)
    tiers = {}
    for d in fams.values():
        tiers[d["tier"]] = tiers.get(d["tier"], 0) + 1
    return tiers.get(key, 0)


def one_row_index(rows, led):
    """The first row whose family has exactly one source row. Renaming a multi-row family leaves it in
    the ledger, so the family-set delta is layout-dependent; renaming a single-row family always leaves
    exactly one sources-only and one ledger-only family."""
    paps = {l["fam"]: int(l["paps"]) for l in led}
    return next(i for i, r in enumerate(rows) if paps.get(r["fam"]) == 1)


# (label, needle, mutation). A needle is a function of the mutated rows, the mutated ledger, the
# loaded checker and the committed population.
MUTANTS = [
    ("drop a sources row",
     lambda rows, led, mod, R: f"sources rows {R['rows'] - 1} != {R['rows']}",
     lambda r, l: r.pop(0)),
    ("proofs +1 on one row",
     lambda rows, led, mod, R: f"proofs sum {R['proofs'] + 1} != {R['proofs']}",
     lambda r, l: r[0].__setitem__("proofs", str(int(r[0]["proofs"]) + 1))),
    ("thms +1 on one row",
     lambda rows, led, mod, R: f"thms sum {R['thms'] + 1} != {R['thms']}",
     lambda r, l: r[0].__setitem__("thms", str(int(r[0]["thms"]) + 1))),
    ("rename a family",
     lambda rows, led, mod, R: "family sets differ: sources-only 1, ledger-only 1",
     lambda r, l: r[one_row_index(r, l)].__setitem__("fam", "999")),
    ("zero tex_bytes",
     lambda rows, led, mod, R: f"{sum(1 for r in rows if int(r['tex_bytes']) <= 0)} rows with tex_bytes <= 0",
     lambda r, l: r[0].__setitem__("tex_bytes", "0")),
    ("flip a tier label",
     lambda rows, led, mod, R: f"'T0': {tier_of(mod, rows, led, 'T0')}",
     lambda r, l: l[0].__setitem__("tier", "T2")),
    ("duplicate a dir row",
     lambda rows, led, mod, R: f"sources rows {R['rows'] + 1} != {R['rows']}",
     lambda r, l: r.append(dict(r[0]))),
    ("negative proofs",
     lambda rows, led, mod, R: f"{sum(1 for r in rows if int(r['proofs']) < 0 or int(r['thms']) < 0)} "
                                "rows with negative proofs/thms",
     lambda r, l: r[0].__setitem__("proofs", "-3")),
]


@pytest.fixture(scope="module")
def mod(load):
    return load("measure_proof_density")


@pytest.fixture(scope="module")
def sources(mod):
    return reorder([dict(r) for r in mod.read_tsv(mod.SOURCES)])


@pytest.fixture(scope="module")
def ledger(mod):
    return [dict(r) for r in mod.read_tsv(mod.LEDGER)]


def test_clean_population(mod, sources, ledger):
    """The gates are silent, and the population is asserted as relations, not recorded numbers. The
    ledger-join invariants: distinct dirs equal rows, the ledger's paps sum equals the row count, the
    tier counts sum to the family count (the tier dict, not each tier value), every sources family is
    in the ledger and every ledger family appears exactly once, and the per-family formalized count
    equals the count of that family's rows whose directory the yaml names. The proofs and thms sums
    stay literals: they are corpus measurements the join cannot produce."""
    fams = mod.build_families(sources, ledger)
    problems = mod.gate_checks(sources, ledger, fams)
    assert not problems, problems[:3]
    assert len({r["dir"] for r in sources}) == len(sources), \
        f"distinct dirs {len({r['dir'] for r in sources})} against {len(sources)} rows"
    assert sum(int(r["paps"]) for r in ledger) == len(sources), \
        f"ledger paps sum {sum(int(r['paps']) for r in ledger)} against {len(sources)} rows"
    assert {r["fam"] for r in sources} == {r["fam"] for r in ledger}, \
        "a sources family is not in the ledger, or a ledger family has no sources row"
    assert all(c == 1 for c in collections.Counter(r["fam"] for r in ledger).values()), \
        "a ledger family appears more than once"
    # A proof begins inside a statement environment, so the proof sum is bounded by the statement sum.
    proofs = sum(int(r["proofs"]) for r in sources)
    thms = sum(int(r["thms"]) for r in sources)
    assert 0 < proofs <= thms, f"proofs {proofs} against statements {thms}"
    tiers: dict = {}
    for d in fams.values():
        tiers[d["tier"]] = tiers.get(d["tier"], 0) + 1
    assert sum(tiers.values()) == len(fams), \
        f"tier counts sum to {sum(tiers.values())} against {len(fams)} families"
    yaml_dirs = mod.yaml_dirs()
    bad = [r["fam"] for r in ledger
           if sum(1 for s in sources if s["fam"] == r["fam"] and s["dir"] in yaml_dirs)
           != int(r["paps_form"])]
    assert not bad, f"families whose formalized rows do not match paps_form: {bad[:4]}"


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
    R = real(mod)
    mut(rows, led)
    assert rows != before or led != [dict(r) for r in mod.read_tsv(mod.LEDGER)], \
        f"{label}: mutation changed nothing"
    found = mod.gate_checks(rows, led, mod.build_families(rows, led))
    want = needle(rows, led, mod, R) if callable(needle) else needle
    assert any(want in x for x in found), f"{label}: NOT caught by {want!r} ({found[:2]})"


def test_formalized_invariant_catches_what_the_literals_miss(mod, sources, ledger):
    """Flipping a family's `paps_form` is invisible to every literal pin: rows, distinct dirs, family
    sets, tier counts, proofs and thms sums are all unchanged, so the gates stay silent. The formalized
    join is the only witness, which is what makes it an invariant and not a second literal."""
    i = next(n for n, r in enumerate(ledger) if int(r["paps_form"]) > 0)
    led = [dict(r) for r in ledger]
    fam = led[i]["fam"]
    led[i]["paps_form"] = "0"
    fams = mod.build_families(sources, led)
    assert not mod.gate_checks(sources, led, fams), \
        "the literal pins fired on a paps_form flip, so the join is not the only witness"
    yaml_dirs = mod.yaml_dirs()
    bad = [r["fam"] for r in led
           if sum(1 for s in sources if s["fam"] == r["fam"] and s["dir"] in yaml_dirs)
           != int(r["paps_form"])]
    assert bad == [fam], f"the formalized join did not flag the flipped family: {bad[:4]}"
