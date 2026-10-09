#!/usr/bin/env python3
"""Print the population for the title<->abstract reading pass, with the raw material per family.

Report-only: writes nothing. The page it feeds is notes/subfinding-pairs.md, written by reading.

The population is a union of two rules, both stated here in code:

  probe     a family with >=2 manuscripts whose abstract contains one of PROBE, matched
            case-insensitively as a substring of the abstract.
  densest   the ten families math-el4.4 names by manuscript count.

PROBE is the vocabulary the bead lists, with the stem the bead's own count implies: `independ`
reproduces the bead's 35, `independent` gives 34. The bead's per-phrase counts are over all 372
abstracts; its population count (51) is stated over the 167 multi-manuscript families and is NOT
reproduced by PROBE - the union over that set is 40, and 9 of the bead's 10 densest names are
outside it. So the population here is probe-union-densest, not the bead's 51.

Per family the report prints: the overview.tex line of its \resultentry, the manuscript count, the
tier, the abstract, and every display title in document order with its path. The reading pass quotes
a clause of the abstract and the title it matches; both quotes live on the same line.

Usage: python3 notes/scripts/extract_subfinding_pairs.py
"""
import csv
import re
import sys

import build_catalog as bc

ROOT = bc.ROOT
TSV = ROOT / "notes" / "subfindings.tsv"
LEDGER = ROOT / "notes" / "catalog.tsv"

# The counts math-el4.4 prints beside each phrase, quoted so a fresh run can be read against them.
BEAD_COUNTS = {"also prove": 25, "independ": 35, "also establish": 5, "as a consequence": 1}

# Case-insensitive substrings of the family abstract. The bead's counts (25 / 35 / 5 / 1) are the
# all-372 hits of these four, which is why the second entry is a stem and not the word.
PROBE = ["also prove", "independ", "also establish", "as a consequence"]

# The bead's densest names, by manuscript count: 034 n=14, 237 n=13, 260 n=13, 238 n=12, 376 n=9,
# 014 n=8, 032 n=8, 227 n=8, 068 n=7, 211 n=7.
DENSEST = ["034", "237", "260", "238", "376", "014", "032", "227", "068", "211"]


def resultentry_lines():
    """{fam: 1-based overview.tex line of its \resultentry}."""
    out = {}
    for n, line in enumerate((ROOT / "overview.tex").read_text(encoding="utf-8").splitlines(), 1):
        m = re.search(r"\\resultentry\{(\d{3})\}", line)
        if m and m.group(1) not in out:
            out[m.group(1)] = n
    return out


def main():
    if not TSV.is_file():
        print(f"{TSV.name} not found - run notes/scripts/extract_subfindings.py first")
        return 1
    if not LEDGER.is_file():
        print(f"{LEDGER.name} not found - run notes/scripts/build_catalog.py first")
        return 1

    _order, fams = bc.parse_overview()
    rows = list(csv.DictReader(TSV.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
    titles = {}
    paths = {}
    for r in rows:
        if r["kind"] == "manuscript":
            titles.setdefault(r["fam"], []).append(r["title"])
            paths.setdefault(r["fam"], []).append(r["path"])
    counts = {f: len(v) for f, v in titles.items()}
    lines = resultentry_lines()
    ledger = {r["fam"]: r for r in csv.DictReader(
        LEDGER.read_text(encoding="utf-8").splitlines(), delimiter="\t")}

    multi = {f for f, n in counts.items() if n > 1}
    low = {f: fams[f]["abstract"].lower() for f in fams}
    per_phrase = {p: {f for f in fams if p in low[f]} for p in PROBE}
    probe_all = set().union(*per_phrase.values())
    probe = probe_all & multi
    population = sorted(probe | set(DENSEST))

    print(f"population rule: (abstract contains one of {PROBE}) AND (>=2 manuscripts), "
          f"union the bead's {len(DENSEST)} densest names")
    print()
    print("per-phrase hits over all 372 abstracts (the bead's counts):")
    for p in PROBE:
        print(f"  {p!r:20} {len(per_phrase[p]):3}   (bead states {BEAD_COUNTS[p]})")
    print(f"probe union over all 372      {len(probe_all)}")
    print(f"multi-manuscript families     {len(multi)}, carrying {sum(counts[f] for f in multi)} manuscripts")
    print(f"probe union over the multi set {len(probe)}   (the bead states 51; no rule tried reproduces it)")
    print(f"bead densest names in probe   {[d for d in DENSEST if d in probe]}")
    print(f"bead densest names outside    {[d for d in DENSEST if d not in probe]}")
    print()
    print(f"POPULATION {len(population)} families, "
          f"{sum(counts[f] for f in population)} manuscripts")
    print("families: " + " ".join(population))
    print()
    print("raw material, one block per family:")
    for fam in population:
        tier = ledger[fam]["tier"]
        print(f"=== {fam}  overview.tex:{lines[fam]}  n={counts[fam]}  tier={tier}  "
              f"paps_form={ledger[fam]['paps_form']}")
        print(f"ABSTRACT: {fams[fam]['abstract']}")
        print(f"PROBE HIT: {[p for p in PROBE if p in low[fam]]}")
        for i, t in enumerate(titles[fam], 1):
            print(f"  [{fam}:{i}] {t}")
            print(f"          {paths[fam][i - 1]}")
        print()

    print("Not checked: which abstract clause states a sub-finding, and which display title it")
    print("matches. That pairing is the reading pass; this report only lays out what is to be read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
