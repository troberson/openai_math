#!/usr/bin/env python3
"""Verify notes/conjecture-standing.tsv against the shipped ledger and overview.tex.

Checks, in order:
  1. the file parses as TSV with exactly 10 fields per row and no comment lines;
  2. the fam set is exactly the resolves_named=1 / resolution-shape intersection;
  3. discipline and tier match notes/catalog.tsv for every row;
  4. prior_confidence is filled and in the recorded vocabulary;
  5. every abstract_line is `overview.tex:<n>` and line <n> of overview.tex is that
     family's \\resultentry, so the anchor names the abstract line the row reads;
  6. the conjecture field is named from that abstract: surname tokens of the row must
     occur in the abstract it cites (dash-normalized, case-insensitive);
  7. surprise_tier is 1..4;
  8. no row asserts consequence: the gap and standing fields must not contain the
     consequence vocabulary listed below.

Writes nothing. Exit 0 means clean.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TSV = ROOT / "notes" / "conjecture-standing.tsv"
LEDGER = ROOT / "notes" / "catalog.tsv"
TEX = ROOT / "overview.tex"

FIELDS = ["fam", "discipline", "tier", "conjecture", "standing_prior_2025",
          "prior_confidence", "release_claim", "gap", "surprise_tier", "abstract_line"]
CONFIDENCE = {"high", "medium", "low"}
TIERS = {"1", "2", "3", "4"}
CONSEQUENCE = re.compile(
    r"consequent|opens the door|paves the way|spawns|triggers|reshapes the field"
    r"|now implies|leads to a solution|has implications", re.I)
STOP = set("""the a an of and or for in on to with by as is are be it its their this that
these those from at every every all any each fixed nontrivial increasing general case cases
conjecture conjectures problem problems question questions theorem the""".split())


def resultentry_lines():
    """fam -> 1-based line number of its \\resultentry in overview.tex."""
    out = {}
    entry = re.compile(r"\\resultentry\{(\d+)\}")
    for n, line in enumerate(TEX.read_text(encoding="utf-8").split("\n"), 1):
        m = entry.match(line.strip())
        if m:
            out[m.group(1)] = (n, line)
    return out


def surname_tokens(conj):
    toks = re.split(r"[^0-9A-Za-z]+", conj)
    keep = []
    for t in toks:
        if len(t) < 4 or t.lower() in STOP:
            continue
        keep.append(t.lower())
    return keep


def main():
    problems = []
    lines = TSV.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    header = lines[0].split("\t")
    if header != FIELDS:
        problems.append(f"header is {header}, expected {FIELDS}")
    body = lines[1:]
    for i, row in enumerate(body, 2):
        if row.startswith("#"):
            problems.append(f"line {i}: comment line in a pure TSV")
        if len(row.split("\t")) != 10:
            problems.append(f"line {i}: {len(row.split(chr(9)))} fields, expected 10")

    rows = list(csv.DictReader(TSV.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
    led = {r["fam"]: r for r in csv.DictReader(LEDGER.read_text(encoding="utf-8").splitlines(),
                                             delimiter="\t")}
    want = {r["fam"] for r in led.values()
            if r["resolves_named"] == "1" and "resolution" in r["shapes"].split("|")}
    got = {r["fam"] for r in rows}
    if want - got:
        problems.append(f"missing families: {sorted(want - got)}")
    if got - want:
        problems.append(f"families outside the selection: {sorted(got - want)}")
    if len(rows) != len(want):
        problems.append(f"{len(rows)} rows for {len(want)} selected families")

    entries = resultentry_lines()
    for r in rows:
        fam = r["fam"]
        if fam not in led:
            problems.append(f"{fam}: not in the ledger")
            continue
        L = led[fam]
        if r["discipline"] != L["discipline"]:
            problems.append(f"{fam}: discipline {r['discipline']!r} != ledger {L['discipline']!r}")
        if r["tier"] != L["tier"]:
            problems.append(f"{fam}: tier {r['tier']!r} != ledger {L['tier']!r}")
        if r["prior_confidence"] not in CONFIDENCE:
            problems.append(f"{fam}: prior_confidence {r['prior_confidence']!r} not in {sorted(CONFIDENCE)}")
        if r["surprise_tier"] not in TIERS:
            problems.append(f"{fam}: surprise_tier {r['surprise_tier']!r} not in 1..4")
        m = re.fullmatch(r"overview\.tex:(\d+)", r["abstract_line"])
        if not m:
            problems.append(f"{fam}: abstract_line {r['abstract_line']!r} is not overview.tex:<n>")
            continue
        n = int(m.group(1))
        rec = entries.get(fam)
        if rec is None:
            problems.append(f"{fam}: no \\resultentry found in overview.tex")
        elif rec[0] != n:
            problems.append(f"{fam}: cites line {n}, its \\resultentry is line {rec[0]}")
        else:
            abstract = rec[1].lower().replace("--", "-")
            toks = surname_tokens(r["conjecture"])
            miss = [t for t in toks if t.replace("--", "-") not in abstract]
            if toks and len(miss) > len(toks) // 2:
                problems.append(f"{fam}: conjecture tokens {miss} absent from the cited abstract")
        for field in ("standing_prior_2025", "gap"):
            hit = CONSEQUENCE.search(r[field])
            if hit:
                problems.append(f"{fam}: {field} asserts consequence ({hit.group(0)!r})")
        for field in FIELDS:
            if not r[field].strip():
                problems.append(f"{fam}: empty {field}")

    tiers = {}
    for r in rows:
        tiers[r["surprise_tier"]] = tiers.get(r["surprise_tier"], 0) + 1
    conf = {}
    for r in rows:
        conf[r["prior_confidence"]] = conf.get(r["prior_confidence"], 0) + 1

    print(f"rows: {len(rows)}  selected: {len(want)}  fields: 10")
    print(f"surprise_tier: " + " ".join(f"{k}:{v}" for k, v in sorted(tiers.items())))
    print(f"prior_confidence: " + " ".join(f"{k}:{v}" for k, v in sorted(conf.items())))
    print(f"anchors resolved to \\resultentry lines: "
          f"{sum(1 for r in rows if re.fullmatch(r'overview\.tex:\d+', r['abstract_line']) and entries.get(r['fam'], (None,))[0] == int(r['abstract_line'].split(':')[1]))}")
    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  -", p)
        return 1
    print("problems: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
