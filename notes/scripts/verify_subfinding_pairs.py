#!/usr/bin/env python3
"""Check notes/subfinding-pairs.md against the shipped files, and re-measure every number it prints.

Read-only: writes nothing. Run it before quoting any count from the page.

Checks, in order:

  population   every population family has exactly one block; no block for a family outside it.
  header       the block's overview.tex line is that family's \resultentry line; n is its manuscript
               count; the tier matches the generated ledger.
  quotes       every quoted clause and every quoted title appears verbatim on the cited line.
  ids          every [fam:seq] resolves in notes/subfindings.tsv to that family and that title.
  coverage     claimed and unclaimed are disjoint and cover the family's full seq set exactly.
  targets      the claimed set equals the set of ids used as pair targets.
  counts       the Summary table's numbers, the probe false-positive list, and the closing
               measurements are recomputed from the parsed lines.
  tail         the page ends with a "Not checked" section.

--mutant injects seven defects into the page text in memory and requires each to be reported.

Usage: python3 notes/scripts/verify_subfinding_pairs.py [--mutant]
"""
import csv
import re
import sys

import build_catalog as bc
import extract_subfinding_pairs as ep

ROOT = bc.ROOT
PAGE = ROOT / "notes" / "subfinding-pairs.md"
TSV = ROOT / "notes" / "subfindings.tsv"
LEDGER = ROOT / "notes" / "catalog.tsv"

HEADER = re.compile(r"^## (?P<fam>\d{3}) · `overview\.tex:(?P<line>\d+)` · "
                    r"n=(?P<n>\d+) · (?P<tier>T\d)\s*$")
PAIR = re.compile(r"^-\s+(?P<kind>main|clause):\s+\"(?P<q>.*?)\"\s+"
                  r"\(`overview\.tex:(?P<lq>\d+)`\)\s+->\s+(?P<rest>.*)$")
TARGET = re.compile(r"^\"(?P<t>.*?)\"\s+\(`overview\.tex:(?P<lt>\d+)`\)\s+"
                    r"\[(?P<fam>\d{3}):(?P<seq>\d+)\]$")
IDS = re.compile(r"^-\s+(?P<kind>claimed|unclaimed):\s*(?P<ids>.*?)\s*$")
ID = re.compile(r"^\d{3}:\d+$")
TABLE_ROW = re.compile(r"^\|\s*(?P<label>.+?)\s*\|\s*(?P<num>\d+)\s*\|\s*$")
FP_LIST = re.compile(r"Probe-vocabulary false positives: (?P<fams>[0-9, ]+)")
FP_COUNT = re.compile(r"(?P<n>\d+) of the (?P<tot>\d+) probe-hit families")


def load_inputs():
    """(overview.tex lines, {fam: resultentry line}, {(fam,seq): title}, {fam: n}, ledger rows)."""
    tex_lines = (ROOT / "overview.tex").read_text(encoding="utf-8").splitlines()
    entry_lines = ep.resultentry_lines()
    titles = {}
    for r in csv.DictReader(TSV.read_text(encoding="utf-8").splitlines(), delimiter="\t"):
        if r["kind"] == "manuscript":
            titles[(r["fam"], int(r["seq"]))] = r["title"]
    counts = {}
    for (fam, _) in titles:
        counts[fam] = counts.get(fam, 0) + 1
    ledger = {r["fam"]: r for r in csv.DictReader(
        LEDGER.read_text(encoding="utf-8").splitlines(), delimiter="\t")}
    return tex_lines, entry_lines, titles, counts, ledger


def population_of(counts):
    """The population, recomputed by the rule extract_subfinding_pairs.py prints."""
    _, fams = bc.parse_overview()
    low = {f: fams[f]["abstract"].lower() for f in fams}
    multi = {f for f, n in counts.items() if n > 1}
    probe_all = {f for f in fams if any(p in low[f] for p in ep.PROBE)}
    probe = probe_all & multi
    return sorted(probe | set(ep.DENSEST)), probe, probe_all, multi


def parse_page(text, problems):
    """-> family blocks. A line that is neither a pair line nor a partition line is prose."""
    blocks = []
    current = None
    for n, line in enumerate(text.splitlines(), 1):
        h = HEADER.match(line)
        if h:
            current = {"fam": h.group("fam"), "line": int(h.group("line")),
                       "n": int(h.group("n")), "tier": h.group("tier"),
                       "pairs": [], "claimed": None, "unclaimed": None}
            blocks.append(current)
            continue
        if line.startswith("## "):
            current = None
            continue
        if current is None:
            continue
        m = PAIR.match(line)
        if m:
            rest = m.group("rest")
            t = TARGET.match(rest)
            if t is None:
                if rest.strip() != "unmatched":
                    problems.append(f"page:{n}: pair line ends with neither a title nor "
                                    f"'unmatched': {rest[:60]}")
                target = None
            else:
                target = {"t": t.group("t"), "lt": int(t.group("lt")),
                          "fam": t.group("fam"), "seq": int(t.group("seq"))}
            current["pairs"].append({"kind": m.group("kind"), "q": m.group("q"),
                                     "lq": int(m.group("lq")), "target": target, "line": n})
            continue
        m = IDS.match(line)
        if m:
            ids = m.group("ids").split()
            bad = [x for x in ids if not ID.match(x)]
            if bad:
                problems.append(f"page:{n}: malformed id in {m.group('kind')}: {bad}")
            if current.get(m.group("kind")) is not None:
                problems.append(f"page:{n}: family {current['fam']} has two "
                                f"{m.group('kind')} lines")
            current[m.group("kind")] = ids
    return blocks


def check(text, inputs, population, probe, probe_all, multi):
    """-> (problems, measured). Every check the page is subject to."""
    tex_lines, entry_lines, titles, counts, ledger = inputs
    problems = []
    blocks = parse_page(text, problems)

    block_fams = [b["fam"] for b in blocks]
    dupes = sorted({f for f in block_fams if block_fams.count(f) > 1})
    if dupes:
        problems.append(f"blocks repeated for families: {dupes}")
    missing = sorted(set(population) - set(block_fams))
    if missing:
        problems.append(f"population families with no block: {missing}")
    extra = sorted(set(block_fams) - set(population))
    if extra:
        problems.append(f"blocks for families outside the population: {extra}")

    accepted = main_accepted = unmatched = 0
    fams_with_pair = fams_with_unmatched = 0
    claimed_total = unclaimed_total = 0
    for b in blocks:
        fam = b["fam"]
        if entry_lines.get(fam) != b["line"]:
            problems.append(f"{fam}: block cites overview.tex:{b['line']}, \resultentry is on "
                            f"{entry_lines.get(fam)}")
        if counts.get(fam) != b["n"]:
            problems.append(f"{fam}: block says n={b['n']}, subfindings.tsv has {counts.get(fam)}")
        if ledger[fam]["tier"] != b["tier"]:
            problems.append(f"{fam}: block says tier {b['tier']}, ledger says {ledger[fam]['tier']}")
        line_text = tex_lines[b["line"] - 1] if b["line"] - 1 < len(tex_lines) else ""
        used = set()
        for p in b["pairs"]:
            if p["q"] not in line_text:
                problems.append(f"{fam}: page:{p['line']}: quoted clause is not verbatim on "
                                f"overview.tex:{b['line']}: {p['q'][:60]}")
            if b["line"] != p["lq"]:
                problems.append(f"{fam}: page:{p['line']}: clause anchor overview.tex:{p['lq']} "
                                f"differs from the block anchor {b['line']}")
            t = p["target"]
            if t is None:
                unmatched += 1
                continue
            if p["kind"] == "clause":
                accepted += 1
            else:
                main_accepted += 1
            if t["fam"] != fam:
                problems.append(f"{fam}: page:{p['line']}: target id {t['fam']}:{t['seq']} is "
                                f"from another family")
            elif (t["fam"], t["seq"]) not in titles:
                problems.append(f"{fam}: page:{p['line']}: target id {t['fam']}:{t['seq']} is "
                                f"not a manuscript row")
            if titles.get((t["fam"], t["seq"])) != t["t"]:
                problems.append(f"{fam}: page:{p['line']}: quoted title is not the title of "
                                f"{t['fam']}:{t['seq']}: {t['t']!r} vs "
                                f"{titles.get((t['fam'], t['seq']), '')!r}")
            if t["t"] not in line_text:
                problems.append(f"{fam}: page:{p['line']}: quoted title is not verbatim on "
                                f"overview.tex:{b['line']}: {t['t']}")
            if b["line"] != t["lt"]:
                problems.append(f"{fam}: page:{p['line']}: title anchor overview.tex:{t['lt']} "
                                f"differs from the block anchor {b['line']}")
            if f"{t['fam']}:{t['seq']}" in used:
                problems.append(f"{fam}: page:{p['line']}: title {t['fam']}:{t['seq']} paired twice")
            used.add(f"{t['fam']}:{t['seq']}")
        claimed = set(b.get("claimed") or [])
        unclaimed = set(b.get("unclaimed") or [])
        if b.get("claimed") is None:
            problems.append(f"{fam}: block has no claimed line")
        if b.get("unclaimed") is None:
            problems.append(f"{fam}: block has no unclaimed line")
        full = {f"{fam}:{s}" for s in range(1, counts.get(fam, 0) + 1)}
        if claimed & unclaimed:
            problems.append(f"{fam}: ids in both claimed and unclaimed: {sorted(claimed & unclaimed)}")
        if full - (claimed | unclaimed):
            problems.append(f"{fam}: ids in neither partition: {sorted(full - (claimed | unclaimed))}")
        if (claimed | unclaimed) - full:
            problems.append(f"{fam}: ids not in this family's manuscript set: "
                            f"{sorted((claimed | unclaimed) - full)}")
        if claimed != used:
            problems.append(f"{fam}: claimed {sorted(claimed)} != paired targets {sorted(used)}")
        claimed_total += len(claimed)
        unclaimed_total += len(unclaimed)
        if any(p["kind"] == "clause" and p["target"] for p in b["pairs"]):
            fams_with_pair += 1
        if any(p["target"] is None for p in b["pairs"]):
            fams_with_unmatched += 1

    measured = {
        "families read": len(blocks),
        "manuscripts in the population": sum(b["n"] for b in blocks),
        "sub-finding clause pairs accepted": accepted,
        "headline clause pairs accepted": main_accepted,
        "clauses recorded unmatched": unmatched,
        "titles claimed by a clause": claimed_total,
        "titles claimed by no clause": unclaimed_total,
        "families with >=1 accepted sub-finding pair": fams_with_pair,
        "families with >=1 clause recorded unmatched": fams_with_unmatched,
        "families with an accepted sub-finding pair and no probe hit":
            sum(1 for b in blocks
                if any(p["kind"] == "clause" and p["target"] for p in b["pairs"])
                and b["fam"] not in probe),
    }

    table = {}
    for line in text.splitlines():
        m = TABLE_ROW.match(line.strip())
        if m:
            table[m.group("label")] = int(m.group("num"))
    for label, value in measured.items():
        if label not in table:
            problems.append(f"Summary table has no row for: {label}")
        elif table[label] != value:
            problems.append(f"Summary table: {label} states {table[label]}, measured {value}")
    if sum(b["n"] for b in blocks) != sum(counts[f] for f in population):
        problems.append(f"block manuscript totals {sum(b['n'] for b in blocks)} != population "
                        f"{sum(counts[f] for f in population)}")

    m = FP_LIST.search(text)
    if m is None:
        problems.append("no probe false-positive sentence found")
    else:
        listed = [x.strip() for x in m.group("fams").split(",") if x.strip()]
        bad = [f for f in listed if f not in probe]
        if bad:
            problems.append(f"false-positive list names families with no probe hit: {bad}")
        num = FP_COUNT.search(text[m.end():])
        if num is None:
            problems.append("false-positive sentence states no count")
        elif int(num.group("n")) != len(listed):
            problems.append(f"false-positive list has {len(listed)} families, the sentence says "
                            f"{num.group('n')}")
        elif int(num.group("tot")) != len(probe):
            problems.append(f"sentence says {num.group('tot')} probe-hit families, "
                            f"measured {len(probe)}")

    if "## Not checked" not in text:
        problems.append("page has no '## Not checked' section")

    measured["probe hits over all 372"] = len(probe_all)
    measured["probe hits over the multi set"] = len(probe)
    measured["multi-manuscript families"] = len(multi)
    return problems, measured


def main():
    mutant = "--mutant" in sys.argv[1:]
    for p in (PAGE, TSV, LEDGER):
        if not p.is_file():
            print(f"missing: {p.relative_to(ROOT)}")
            return 1

    inputs = load_inputs()
    _, _, _, counts, _ = inputs
    population, probe, probe_all, multi = population_of(counts)
    text = PAGE.read_text(encoding="utf-8")
    problems, measured = check(text, inputs, population, probe, probe_all, multi)

    print(f"population rule      (probe {ep.PROBE}) AND (>=2 manuscripts), "
          f"union {len(ep.DENSEST)} named densest families")
    print(f"population           {len(population)} families, "
          f"{sum(counts[f] for f in population)} manuscripts")
    print(f"page                 {PAGE.relative_to(ROOT)}")
    print()
    print("measured:")
    for label, value in measured.items():
        print(f"  {label:52} {value:4}")
    print()
    print(f"problems             {len(problems)}")
    for p in problems:
        print(f"  {p}")

    if mutant:
        print()
        print("mutants:")
        cases = [
            ("paraphrase dressed as a quote",
             lambda t: t.replace('"Also proves Bogomolov--Pop reconstruction',
                                 '"Also proves Bogomolov-Pop reconstruction', 1)),
            ("anchor on the wrong line",
             lambda t: t.replace("`overview.tex:94`) -> \"The Bogomolov-Pop",
                                 "`overview.tex:95`) -> \"The Bogomolov-Pop", 1)),
            ("title id borrowed from another family",
             lambda t: t.replace("[009:3]", "[010:3]", 1)),
            ("an id in both partitions",
             lambda t: t.replace("- claimed: 041:1 041:2\n- unclaimed:",
                                 "- claimed: 041:1 041:2\n- unclaimed: 041:1", 1)),
            ("a title dropped from the partition",
             lambda t: t.replace("- unclaimed: 034:3 034:5 034:6",
                                 "- unclaimed: 034:5 034:6", 1)),
            ("a stale Summary-table count",
             lambda t: t.replace("| titles claimed by no clause | 94 |",
                                 "| titles claimed by no clause | 60 |", 1)),
            ("a block outside the population",
             lambda t: t.replace("## 009 · `overview.tex:94` · n=3 · T2",
                                 "## 008 · `overview.tex:92` · n=1 · T0\n\n"
                                 "- main: \"x\" (`overview.tex:92`) -> unmatched\n"
                                 "- claimed:\n- unclaimed:\n\n"
                                 "## 009 · `overview.tex:94` · n=3 · T2", 1)),
        ]
        missed = 0
        for name, fn in cases:
            mutated = fn(text)
            if mutated == text:
                print(f"  {name:42} NOT INJECTED (target text absent)")
                missed += 1
                continue
            found, _ = check(mutated, inputs, population, probe, probe_all, multi)
            if not found:
                print(f"  {name:42} NOT REPORTED")
                missed += 1
            else:
                print(f"  {name:42} reported: {found[0]}")
        print(f"mutants not caught   {missed} of {len(cases)}")
        if missed:
            print("  the checker is not sufficient")
            return 1
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
