#!/usr/bin/env python3
"""Triage the T0 families (no scope note, no challenge, no main result) by claim shape.

Reads notes/gen/tables/catalog.tsv; writes nothing. T0 is the tier with no coverage signal, so the
`shapes` column drives the buckets. The ledger's `resolves_named` and `counterex_broad` columns
are second and third T0 discriminators and are deliberately not read here: buckets are first-match,
so a broader signal added to the first-match chain would move families between buckets -- widening
`counterexample` to the broad rule moves every T0 family that carries the flag but not the tag into
C. The underlying `shapes` tags stay multi-label; the T0 counts for both columns are printed below.

Usage: python3 notes/scripts/triage_t0.py [--tsv notes/gen/tables/catalog.tsv]

The tier, the shape tags, and the first-match bucket rule are the package's
(`catlib.ledger`); the prose each bucket carries is report formatting and stays here.
"""

import argparse
import collections

from catlib.ledger import T0_BUCKETS, bucket_of, read_ledger
from catlib.paths import LEDGER_TSV

# What each bucket means, keyed by code. The order and the tags are `catlib.ledger.T0_BUCKETS`;
# this is the report's wording, not a join.
BUCKET_PROSE = {
    "C": "names an object that breaks a conjecture - cheapest to check",
    "R": "resolves/proves/settles a named conjecture - largest claim, no evidence",
    "B": "bound, sharpness, power-saving, improvement",
    "K": "if and only if / classified / characterization",
    "U": "uniformity over every object in a class",
    "O": "density, partial, undecidability, conditional - tagged but no bucket above",
    "N": "no shape tag at all - title is the only signal",
}

BUCKETS = [(code, tag, BUCKET_PROSE[code]) for code, tag in T0_BUCKETS]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv", default=str(LEDGER_TSV))
    args = ap.parse_args()

    rows = read_ledger(args.tsv)
    t0 = [r for r in rows if r["tier"] == "T0"]
    for r in t0:
        r["bucket"] = bucket_of(r["shapes"])

    print(f"ledger rows {len(rows)}  T0 {len(t0)}  "
          f"manuscripts {sum(int(r['paps']) for r in t0)}  "
          f"formalized {sum(int(r['paps_form']) for r in t0)}")
    print()

    counts = collections.Counter(r["bucket"] for r in t0)
    print("bucket  fams  paps  meaning")
    for code, tag, why in BUCKETS:
        n = counts.get(code, 0)
        paps = sum(int(r["paps"]) for r in t0 if r["bucket"] == code)
        label = tag or "other" if code == "O" else tag or "untagged"
        print(f"{code:6} {n:5}  {paps:5}  {label}: {why}")
    print(f"{'total':6} {sum(counts.values()):5}  "
          f"{sum(int(r['paps']) for r in t0):5}  (reconciles with T0 above: "
          f"{sum(counts.values()) == len(t0)})")

    print()
    print("bucket x discipline (fams with >=2):")
    for code, _, _ in BUCKETS:
        c = collections.Counter(r["discipline"] for r in t0 if r["bucket"] == code)
        top = ", ".join(f"{d} {n}" for d, n in c.most_common() if n >= 2)
        print(f"  {code}: {top or '-'}")

    print()
    print("multi-manuscript T0 (>=3 paps) - most exposed, least checked:")
    for r in sorted((r for r in t0 if int(r["paps"]) >= 3), key=lambda r: -int(r["paps"])):
        print(f"  {r['fam']} {r['bucket']} {int(r['paps']):2}p {r['discipline'][:26]:26} {r['title'][:52]}")

    print()
    print("T0 with >=3 shape tags (densest claims):")
    dense = [r for r in t0 if len(r["shapes"].split("|")) >= 3]
    print(f"  {len(dense)} families: {', '.join(r['fam'] for r in dense)}")

    print()
    print("T0 ledger discriminators (flags, deliberately not read into buckets):")
    for label, col in [("resolves_named", "resolves_named"), ("counterex_broad", "counterex_broad")]:
        hits = [r for r in t0 if r[col] == "1"]
        by = collections.Counter(r["bucket"] for r in hits)
        order = [f"{c}{by[c]}" for c, _, _ in BUCKETS if by[c]]
        print(f"  {label}: {len(hits)} of {len(t0)} T0 families; by bucket {' '.join(order)}")
        if col == "resolves_named":
            nn = sorted(r["fam"] for r in t0 if r["bucket"] == "N" and r[col] == "1")
            print(f"    named in N: {len(nn)} of {counts.get('N', 0)}: {' '.join(nn)}")
        else:
            out = [f"{r['fam']}({r['bucket']})" for r in sorted(hits, key=lambda r: r["fam"])
                   if r["bucket"] != "C"]
            print(f"    flagged outside C: {len(out)}: {' '.join(out)}")

    print()
    print("named T0 sets:")
    for label, pred in [
        ("conditional", lambda r: "conditional" in r["shapes"]),
        ("undecidability", lambda r: "undecidability" in r["shapes"]),
        ("counterexample", lambda r: "counterexample" in r["shapes"]),
        ("companion word", lambda r: r["companion_word"] == "1"),
    ]:
        fams = [r["fam"] for r in t0 if pred(r)]
        print(f"  {label} ({len(fams)}): {', '.join(fams) or '-'}")

    print()
    print("number-theory opening families (001-031) in T0:")
    nt = [r for r in t0 if r["fam"] <= "031"]
    print(f"  {len(nt)}: {', '.join(r['fam'] for r in nt)}")


if __name__ == "__main__":
    main()
