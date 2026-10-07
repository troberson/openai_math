#!/usr/bin/env python3
"""Triage the T0 families (no scope note, no challenge, no main result) by claim shape.

Reads notes/catalog.tsv; writes nothing. T0 is the tier with no coverage signal, so the
`shapes` column is the only discriminator available. Buckets are first-match and therefore a
partition *for triage ordering only* - the underlying `shapes` tags stay multi-label.

Usage: python3 notes/scripts/triage_t0.py [--tsv notes/catalog.tsv]
"""

import argparse
import collections
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# First match wins. Ordered by how cheaply the claim can be checked, not by importance.
BUCKETS = [
    ("C", "counterexample", "names an object that breaks a conjecture - cheapest to check"),
    ("R", "resolution", "resolves/proves/settles a named conjecture - largest claim, no evidence"),
    ("B", "bound", "bound, sharpness, power-saving, improvement"),
    ("K", "classification", "if and only if / classified / characterization"),
    ("U", "uniform", "uniformity over every object in a class"),
    ("O", None, "density, partial, undecidability, conditional - tagged but no bucket above"),
    ("N", None, "no shape tag at all - title is the only signal"),
]


def bucket_of(shapes: str) -> str:
    tags = set(shapes.split("|")) if shapes else set()
    for code, tag, _ in BUCKETS:
        if tag and tag in tags:
            return code
    return "N" if not tags else "O"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv", default=str(ROOT / "notes" / "catalog.tsv"))
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.tsv, encoding="utf-8"), delimiter="\t"))
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
