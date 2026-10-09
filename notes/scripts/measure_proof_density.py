#!/usr/bin/env python3
"""Measure proof density over the 719 manuscripts and test whether it discriminates.

Report-only: writes nothing. Every number it prints is derived here, from
notes/sources.tsv (per-manuscript counts) joined to notes/catalog.tsv (tier and
claim-shape tags) by family number.

Pre-registered discrimination rule (fixed before the statistics were run, per the
conditional-tag discipline in notes/conditional.md):

    A signal SEPARATES a pair when AUC >= 0.65 and two-sided p < 0.01.
    A signal is SIZE-EXPLAINED on a pair when its AUC is within 0.03 of the
    tex-KB AUC on that same pair -- file size explains the separation, not density.

AUC is P(X > Y) for the first-named group over the second (Mann-Whitney U); 0.5 is
no separation. z uses the tie-corrected SD.

Usage: python3 notes/scripts/measure_proof_density.py [--mutant]
"""

import csv
import math
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SOURCES = REPO / "notes" / "sources.tsv"
LEDGER = REPO / "notes" / "catalog.tsv"

# Totals recorded in beads math-hqd.3 and in notes/sources.md, re-measured 2026-10-09 after the
# upstream merge (719 manuscripts / 20,341 proofs / 21,288 statements / tiers 136-106-0-130).
EXPECTED_ROWS = 719
EXPECTED_FAMS = 372
EXPECTED_PROOFS = 20341
EXPECTED_THMS = 21288
EXPECTED_TIERS = {"T3": 136, "T2": 106, "T1": 0, "T0": 130}

AUC_MIN = 0.65
P_MAX = 0.01
SIZE_TOLERANCE = 0.03

TIER_PAIRS = [("T0", "T2"), ("T0", "T3"), ("T2", "T3")]
SHAPES = ["uniform", "resolution", "bound", "counterexample", "partial",
          "classification", "density", "conditional", "undecidability"]
FLAGS = ["conditional", "resolves_named", "counterex_broad"]


def read_tsv(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def auc_p(a, b):
    """Mann-Whitney AUC = P(a > b), tie-corrected normal-approximation z and p."""
    n1, n2 = len(a), len(b)
    if n1 == 0 or n2 == 0:
        return None
    combined = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    ranks = {}
    i = 0
    tie_terms = 0
    while i < len(combined):
        j = i
        while j < len(combined) and combined[j][0] == combined[i][0]:
            j += 1
        avg = (i + 1 + j) / 2.0
        for k in range(i, j):
            ranks[k] = avg
        t = j - i
        if t > 1:
            tie_terms += t ** 3 - t
        i = j
    r1 = sum(ranks[k] for k, (_, g) in enumerate(combined) if g == 0)
    u = r1 - n1 * (n1 + 1) / 2.0
    n = n1 + n2
    auc = u / (n1 * n2)
    var = (n1 * n2 / 12.0) * ((n + 1) - tie_terms / float(n * (n - 1))) if n > 1 else 0.0
    if var <= 0:
        return auc, 0.0, 1.0
    z = (u - n1 * n2 / 2.0) / math.sqrt(var)
    p = math.erfc(abs(z) / math.sqrt(2.0))
    return auc, z, p


def median(vals):
    s = sorted(vals)
    n = len(s)
    if not n:
        return None
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0


def build_families(sources, ledger):
    fams = {}
    for row in sources:
        fam = row["fam"]
        d = fams.setdefault(fam, {"proofs": 0, "thms": 0, "bytes": 0, "rows": 0})
        d["proofs"] += int(row["proofs"])
        d["thms"] += int(row["thms"])
        d["bytes"] += int(row["tex_bytes"])
        d["rows"] += 1
    for row in ledger:
        d = fams.setdefault(row["fam"], {"proofs": 0, "thms": 0, "bytes": 0, "rows": 0})
        d["tier"] = row["tier"]
        d["paps"] = int(row["paps"])
        d["shapes"] = set(row["shapes"].split("|")) if row["shapes"] else set()
        for flag in FLAGS:
            d[flag] = row[flag]
    for d in fams.values():
        d["proofs_per_man"] = (d["proofs"] / d["rows"]) if d["rows"] else 0.0
        d["kb"] = d["bytes"] / 1024.0
        d["proofs_per_thm"] = (d["proofs"] / d["thms"]) if d["thms"] else 0.0
        d["proofs_per_kb"] = (d["proofs"] / d["kb"]) if d["kb"] else 0.0
        d["kb_per_man"] = (d["kb"] / d["rows"]) if d["rows"] else 0.0
    return fams


SIGNALS = [
    ("proofs", "proofs per family (raw)"),
    ("thms", "statements per family (declared rule)"),
    ("proofs_per_man", "proofs per manuscript"),
    ("proofs_per_thm", "proofs per statement"),
    ("proofs_per_kb", "proofs per tex KB"),
    ("kb_per_man", "tex KB per manuscript (size control)"),
]


def gate_checks(sources, ledger, fams):
    problems = []
    rows = len(sources)
    if rows != EXPECTED_ROWS:
        problems.append(f"sources rows {rows} != {EXPECTED_ROWS}")
    dirs = [r["dir"] for r in sources]
    if len(set(dirs)) != EXPECTED_ROWS:
        problems.append(f"distinct dirs {len(set(dirs))} != {EXPECTED_ROWS}")
    src_fams = {r["fam"] for r in sources}
    led_fams = {r["fam"] for r in ledger}
    if len(src_fams) != EXPECTED_FAMS:
        problems.append(f"families in sources {len(src_fams)} != {EXPECTED_FAMS}")
    if len(led_fams) != EXPECTED_FAMS:
        problems.append(f"families in ledger {len(led_fams)} != {EXPECTED_FAMS}")
    if src_fams != led_fams:
        problems.append(f"family sets differ: sources-only {len(src_fams - led_fams)}, "
                        f"ledger-only {len(led_fams - src_fams)}")
    paps_diff = sum(1 for f in led_fams
                    if fams[f]["rows"] != int(next(l["paps"] for l in ledger if l["fam"] == f)))
    if paps_diff:
        problems.append(f"per-family source rows differ from ledger paps in {paps_diff} families")
    if sum(int(r["proofs"]) for r in sources) != EXPECTED_PROOFS:
        problems.append(f"proofs sum {sum(int(r['proofs']) for r in sources)} != {EXPECTED_PROOFS}")
    if sum(int(r["thms"]) for r in sources) != EXPECTED_THMS:
        problems.append(f"thms sum {sum(int(r['thms']) for r in sources)} != {EXPECTED_THMS}")
    tiers = {}
    for f in led_fams:
        tiers[fams[f]["tier"]] = tiers.get(fams[f]["tier"], 0) + 1
    if {k: tiers.get(k, 0) for k in EXPECTED_TIERS} != EXPECTED_TIERS:
        problems.append(f"tier counts {tiers} != {EXPECTED_TIERS}")
    bad_bytes = sum(1 for r in sources if int(r["tex_bytes"]) <= 0)
    if bad_bytes:
        problems.append(f"{bad_bytes} rows with tex_bytes <= 0")
    bad_counts = sum(1 for r in sources if int(r["proofs"]) < 0 or int(r["thms"]) < 0)
    if bad_counts:
        problems.append(f"{bad_counts} rows with negative proofs/thms")
    missing = sum(1 for d in dirs if not (REPO / "preprints" / d).is_dir())
    if missing:
        problems.append(f"{missing} source dirs absent from preprints/")
    if sum(int(r["paps"]) for r in ledger) != EXPECTED_ROWS:
        problems.append(f"ledger paps sum {sum(int(r['paps']) for r in ledger)} != {EXPECTED_ROWS}")
    return problems


def compare(fams, key, groups):
    out = {}
    for name, vals in groups.items():
        other = [fams[f][key] for f in fams if f not in vals]
        res = auc_p([fams[f][key] for f in vals], other)
        if res:
            out[name] = (res[0], res[2], len(vals), len(other))
    return out


def report(fams, ledger, sources, quiet=False):
    problems = gate_checks(sources, ledger, fams)
    if not quiet:
        print("=== population ===")
        print(f"sources rows {len(sources)} | families {len(fams)} | "
              f"proofs {sum(d['proofs'] for d in fams.values())} | "
              f"thms {sum(d['thms'] for d in fams.values())}")
        tiers = {}
        for d in fams.values():
            tiers[d["tier"]] = tiers.get(d["tier"], 0) + 1
        print("tiers " + " ".join(f"{k}:{tiers.get(k, 0)}" for k in ("T3", "T2", "T1", "T0")))
        print("=== medians by tier ===")
        for key, label in SIGNALS:
            cells = []
            for t in ("T0", "T2", "T3"):
                vals = [d[key] for d in fams.values() if d["tier"] == t]
                cells.append(f"{t} {median(vals):.3f}")
            print(f"{label:34} " + "  ".join(cells))
        print(f"=== tier separations (AUC / p; threshold AUC>={AUC_MIN}, p<{P_MAX}) ===")
        for key, label in SIGNALS:
            cells = []
            for a, b in TIER_PAIRS:
                ga = [d[key] for d in fams.values() if d["tier"] == a]
                gb = [d[key] for d in fams.values() if d["tier"] == b]
                res = auc_p(ga, gb)
                mark = "*" if res and res[0] >= AUC_MIN and res[2] < P_MAX else " "
                cells.append(f"{a}>{b} {res[0]:.3f}/{res[2]:.2e}{mark}")
            print(f"{label:34} " + "  ".join(cells))
        print("=== verdict (pre-registered: SEPARATES = AUC>=%.2f and p<%.2f; "
              "SIZE-EXPLAINED = within %.2f of the tex-KB control) ===" %
              (AUC_MIN, P_MAX, SIZE_TOLERANCE))
        control = {}
        for pair in TIER_PAIRS:
            control[(pair, "family")] = auc_p(
                [d["kb"] for d in fams.values() if d["tier"] == pair[0]],
                [d["kb"] for d in fams.values() if d["tier"] == pair[1]])[0]
            control[(pair, "manuscript")] = auc_p(
                [d["kb_per_man"] for d in fams.values() if d["tier"] == pair[0]],
                [d["kb_per_man"] for d in fams.values() if d["tier"] == pair[1]])[0]
        print(f"{'tex KB per family (control)':34} " + "  ".join(
            f"{a}>{b} {control[((a, b), 'family')]:.3f}" for a, b in TIER_PAIRS))
        scale = {"proofs": "family", "thms": "family", "proofs_per_man": "manuscript",
                 "proofs_per_thm": None, "proofs_per_kb": None, "kb_per_man": "manuscript"}
        for key, label in SIGNALS:
            if key == "kb_per_man":
                continue
            cells = []
            for pair in TIER_PAIRS:
                ga = [d[key] for d in fams.values() if d["tier"] == pair[0]]
                gb = [d[key] for d in fams.values() if d["tier"] == pair[1]]
                auc, _, pval = auc_p(ga, gb)
                if auc >= AUC_MIN and pval < P_MAX:
                    if scale[key] and abs(auc - control[(pair, scale[key])]) <= SIZE_TOLERANCE:
                        verdict = "SIZE-EXPLAINED"
                    else:
                        verdict = "SEPARATES"
                else:
                    verdict = "NULL"
                cells.append(f"{pair[0]}>{pair[1]} {verdict}")
            print(f"{label:34} " + "  ".join(cells))
        print("=== claim-shape contrasts (in-shape vs rest) ===")
        for key, label in [("proofs", "proofs per family"), ("proofs_per_man", "proofs per manuscript"),
                           ("proofs_per_thm", "proofs per statement"), ("proofs_per_kb", "proofs per tex KB")]:
            for shape in SHAPES:
                grp = {f for f, d in fams.items() if shape in d["shapes"]}
                if len(grp) < 4:
                    print(f"{label:24} {shape:14} n={len(grp)} (too few)")
                    continue
                res = compare(fams, key, {shape: grp})[shape]
                mark = "*" if res[0] >= AUC_MIN and res[1] < P_MAX else " "
                print(f"{label:24} {shape:14} n={res[2]:3} AUC={res[0]:.3f} p={res[1]:.2e}{mark}")
        print("=== ledger flag contrasts ===")
        for key, label in [("proofs_per_man", "proofs per manuscript"),
                           ("proofs_per_thm", "proofs per statement"),
                           ("proofs_per_kb", "proofs per tex KB")]:
            for flag in FLAGS:
                grp = {f for f, d in fams.items() if d.get(flag) == "1"}
                res = compare(fams, key, {flag: grp})[flag]
                mark = "*" if res[0] >= AUC_MIN and res[1] < P_MAX else " "
                print(f"{label:24} {flag:16} n={res[2]:3} AUC={res[0]:.3f} p={res[1]:.2e}{mark}")
    return problems


def selftest():
    """The statistic is a claim too: check AUC against hand-computed values."""
    cases = [
        ([1, 2, 3], [0, 1, 2], 7 / 9.0),   # 6 wins + 2 ties (0.5 each) over 9 pairs
        ([4, 5, 6], [1, 2, 3], 1.0),
        ([1, 2], [3, 4], 0.0),
        ([1, 1, 1], [1, 1, 1], 0.5),
        ([1, 3, 5, 7], [2, 2, 6, 6], 8 / 16.0),
    ]
    ok = 0
    for a, b, want in cases:
        got = auc_p(a, b)[0]
        ok += abs(got - want) < 1e-9
    return ok, len(cases)


def mutants(fams_builder):
    """Each mutation must be caught by a gate. Returns (caught, total, details)."""
    sources = read_tsv(SOURCES)
    ledger = read_tsv(LEDGER)
    cases = []

    def apply(name, fn):
        rows = [dict(r) for r in sources]
        led = [dict(r) for r in ledger]
        fn(rows, led)
        fams = fams_builder(rows, led)
        probs = gate_checks(rows, led, fams)
        cases.append((name, bool(probs), probs[:2]))

    apply("drop a sources row", lambda r, l: r.pop(0))
    apply("proofs +1 on one row", lambda r, l: r[0].__setitem__("proofs", str(int(r[0]["proofs"]) + 1)))
    apply("thms +1 on one row", lambda r, l: r[0].__setitem__("thms", str(int(r[0]["thms"]) + 1)))
    apply("rename a family", lambda r, l: r[0].__setitem__("fam", "999"))
    apply("zero tex_bytes", lambda r, l: r[0].__setitem__("tex_bytes", "0"))
    apply("flip a tier label", lambda r, l: l[0].__setitem__("tier", "T2"))
    apply("duplicate a dir row", lambda r, l: r.append(dict(r[0])))
    apply("negative proofs", lambda r, l: r[0].__setitem__("proofs", "-3"))
    caught = sum(1 for _, ok, _ in cases if ok)
    return caught, len(cases), cases


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    sources = read_tsv(SOURCES)
    ledger = read_tsv(LEDGER)
    fams = build_families(sources, ledger)
    st_ok, st_total = selftest()
    problems = report(fams, ledger, sources, quiet=quiet)
    print("=== gates ===")
    print(f"statistic self-test {st_ok}/{st_total}")
    print("PROBLEMS " + str(len(problems) + (st_total - st_ok)))
    for p in problems:
        print("  " + p)
    if "--mutant" in args:
        caught, total, cases = mutants(build_families)
        print("=== mutants ===")
        for name, ok, detail in cases:
            print(f"  {'CAUGHT ' if ok else 'MISSED '} {name}" + ("" if ok else f" -> {detail}"))
        print(f"mutants caught {caught}/{total}")
        if caught != total:
            sys.exit(1)
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
