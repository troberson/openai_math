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

--mutant injects the six defects the page records, into the table text in memory, and requires
each to be reported. The injections are targeted from the parsed rows, so they follow the table
when a row's anchor or name changes; an injection that finds no target is reported as NOT INJECTED
and fails the run, so a mutant cannot pass by quietly stopping applying.
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


def selection():
    """(ledger rows, selected fams, \\resultentry lines)."""
    led = {r["fam"]: r for r in csv.DictReader(LEDGER.read_text(encoding="utf-8").splitlines(),
                                              delimiter="\t")}
    want = {r["fam"] for r in led.values()
            if r["resolves_named"] == "1" and "resolution" in r["shapes"].split("|")}
    return led, want, resultentry_lines()


def check(text, led, want, entries):
    """-> (problems, rows). Every check the table is subject to, run on table text."""
    problems = []
    lines = text.split("\n")
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

    rows = list(csv.DictReader(text.splitlines(), delimiter="\t"))
    got = {r["fam"] for r in rows}
    if want - got:
        problems.append(f"missing families: {sorted(want - got)}")
    if got - want:
        problems.append(f"families outside the selection: {sorted(got - want)}")
    if len(rows) != len(want):
        problems.append(f"{len(rows)} rows for {len(want)} selected families")

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
    return problems, rows


def _row(text, fam):
    """The single table line for fam, and its index in the line list."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith(f"{fam}\t"):
            return lines, i
    return lines, None


def _set_field(text, fam, idx, value):
    lines, i = _row(text, fam)
    if i is None:
        return text
    fields = lines[i].split("\t")
    fields[idx] = value
    lines[i] = "\t".join(fields)
    return "\n".join(lines)


def mutants(text, led, want):
    """The six defects the page records, targeted from the parsed rows."""
    rows = list(csv.DictReader(text.splitlines(), delimiter="\t"))
    anchored = [r for r in rows if re.fullmatch(r"overview\.tex:\d+", r["abstract_line"])]
    named = [r for r in rows if surname_tokens(r["conjecture"])]
    outside = sorted(set(led) - want - {r["fam"] for r in rows})[0]
    anchor_fam, anchor_line = anchored[0]["fam"], int(anchored[0]["abstract_line"].split(":")[1])
    conf_fam, gap_fam, name_fam, wide_fam = rows[0]["fam"], rows[1]["fam"], named[0]["fam"], rows[0]["fam"]
    gap_text = rows[1]["gap"]
    return [
        ("anchor shifted by two lines",
         lambda t: _set_field(t, anchor_fam, 9, f"overview.tex:{anchor_line + 2}")),
        ("a blanked prior_confidence",
         lambda t: _set_field(t, conf_fam, 5, "")),
        ("a family added outside the selection",
         lambda t: t.rstrip("\n") + "\n" + "\t".join(
             [outside, led[outside]["discipline"], led[outside]["tier"],
              "an added row outside the selection", "not a prior judgment", "low",
              "a synthetic release claim", "synthetic gap", "1", "overview.tex:1"])),
        ("a consequence assertion in a gap field",
         lambda t: _set_field(t, gap_fam, 7, gap_text + "; it opens the door to the general case")),
        ("a conjecture renamed to a name absent from its abstract",
         lambda t: _set_field(t, name_fam, 3, "Zauner dimension-six mutually unbiased bases conjecture")),
        ("a row widened to 11 fields",
         lambda t: _append_field(t, wide_fam)),
    ]


def _append_field(text, fam):
    lines, i = _row(text, fam)
    if i is None:
        return text
    lines[i] = lines[i] + "\textra field"
    return "\n".join(lines)


def main():
    mutant = "--mutant" in sys.argv[1:]
    led, want, entries = selection()
    text = TSV.read_text(encoding="utf-8")
    problems, rows = check(text, led, want, entries)

    tiers = {}
    for r in rows:
        tiers[r.get("surprise_tier", "?")] = tiers.get(r.get("surprise_tier", "?"), 0) + 1
    conf = {}
    for r in rows:
        conf[r.get("prior_confidence", "?")] = conf.get(r.get("prior_confidence", "?"), 0) + 1
    resolved = sum(1 for r in rows
                   if re.fullmatch(r"overview\.tex:\d+", r["abstract_line"])
                   and entries.get(r["fam"], (None,))[0] == int(r["abstract_line"].split(":")[1]))

    print(f"rows: {len(rows)}  selected: {len(want)}  fields: 10")
    print(f"surprise_tier: " + " ".join(f"{k}:{v}" for k, v in sorted(tiers.items())))
    print(f"prior_confidence: " + " ".join(f"{k}:{v}" for k, v in sorted(conf.items())))
    print(f"anchors resolved to \\resultentry lines: {resolved}")

    if problems:
        print(f"\n{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  -", p)
        if not mutant:
            return 1

    if mutant:
        print("\nmutants:")
        cases = mutants(text, led, want)
        failed = []
        for name, fn in cases:
            mutated = fn(text)
            if mutated == text:
                print(f"  {name:52} NOT INJECTED (table text changed — fix the mutant)")
                failed.append(name)
                continue
            found, _ = check(mutated, led, want, entries)
            if not found:
                print(f"  {name:52} NOT REPORTED")
                failed.append(name)
            else:
                print(f"  {name:52} reported: {found[0]}")
        print(f"mutants {len(cases)}  uncaught {len(failed)} {failed}")
        return 1 if (problems or failed) else 0

    print("problems: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
