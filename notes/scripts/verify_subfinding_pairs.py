#!/usr/bin/env python3
"""Check notes/reports/subfinding-pairs.md against the shipped files, and re-measure every number it prints.

Read-only: writes nothing. Run it before quoting any count from the page.

Checks, in order:

  population   every population family has exactly one block; no block for a family outside it.
  header       the block's overview.tex line is that family's \resultentry line; n is its manuscript
               count; the tier matches the generated ledger.
  quotes       every quoted clause and every quoted title appears verbatim on the cited line.
  ids          every [fam:seq] resolves in notes/tables/subfindings.tsv to that family and that title.
  coverage     claimed and unclaimed are disjoint and cover the family's full seq set exactly.
  targets      the claimed set equals the set of ids used as pair targets.
  counts       the Summary table's numbers, the probe false-positive list, and the closing
               measurements are recomputed from the parsed lines.
  sync         the page is compared with notes/scripts/render_reports.py's render of it, so prose the
               count passes never parse cannot drift from the writer's template. The counts pass
               proves the numbers are measured; it proves nothing about the sentences around them.
  tail         the page ends with a "Not checked" section.

The self-tests are in notes/scripts/tests/test_subfinding_pairs.py: that file injects the eight page
defects, the last being a prose count outside every recomputed table -- visible only to the sync
check -- and asserts each fires the pass that owns it. `main()` reads no argv, so `--mutant` is inert
here.

Usage: python3 notes/scripts/verify_subfinding_pairs.py
"""
import re
import sys
from functools import cache
from typing import Optional

import build_catalog as bc
import extract_subfinding_pairs as ep
from catlib import overview, tsv
from catlib import render as RD
from catlib.paths import LEDGER_TSV, NOTES, OVERVIEW_TEX, ROOT, SUBFINDINGS_TSV


def new_block(fam: str, line: int, n: int, tier: str) -> dict:
    """A parsed block: the header fields, the pair list, and the two id partitions."""
    return {"fam": fam, "line": line, "n": n, "tier": tier,
            "pairs": [], "claimed": None, "unclaimed": None}

PAGE = NOTES / "reports" / "subfinding-pairs.md"

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


@cache
def load_inputs():
    """(overview.tex lines, {fam: resultentry line}, {(fam,seq): title}, {fam: n}, ledger rows)."""
    tex_lines = OVERVIEW_TEX.read_text(encoding="utf-8").splitlines()
    entry_lines = overview.overview_lines()
    titles = {}
    for r in tsv.read_rows(SUBFINDINGS_TSV):
        if r["kind"] == "manuscript":
            titles[(r["fam"], int(r["seq"]))] = r["title"]
    counts: dict[str, int] = {}
    for (fam, _) in titles:
        counts[fam] = counts.get(fam, 0) + 1
    ledger = {r["fam"]: r for r in tsv.read_rows(LEDGER_TSV)}
    return tex_lines, entry_lines, titles, counts, ledger


def population_of(counts):
    """The population, recomputed by the rule extract_subfinding_pairs.py prints."""
    _, fams = bc.parse_overview()
    low = {f: fams[f]["abstract"].lower() for f in fams}
    multi = {f for f, n in counts.items() if n > 1}
    probe_all = {f for f in fams if any(p in low[f] for p in ep.PROBE)}
    probe = probe_all & multi
    band = set(ep.band1(counts, low))
    band2 = set(ep.band2(counts, low))
    band3 = set(ep.band3(counts, low))
    return sorted(probe | set(ep.DENSEST) | band | band2 | band3), probe, probe_all, multi, \
        band, band2, band3


def parse_page(text, problems):
    """-> family blocks. A line that is neither a pair line nor a partition line is prose."""
    blocks: list = []
    current: Optional[dict] = None
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


def passes(text, inputs, population, probe, probe_all, multi):
    """-> (problems, measured). Every check the page is subject to."""
    tex_lines, entry_lines, titles, counts, ledger = inputs
    problems: list[str] = []
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


def check(text: str) -> tuple[list, dict]:
    """-> (problems, measured), the sync pass included. The self-tests call this with page text."""
    inputs = load_inputs()
    _, _, _, counts, _ = inputs
    population, probe, probe_all, multi, _band, _band2, _band3 = population_of(counts)
    problems, measured = passes(text, inputs, population, probe, probe_all, multi)
    problems.extend(RD.sync_problems(PAGE, text))
    return problems, measured


def main():
    for p in (PAGE, SUBFINDINGS_TSV, LEDGER_TSV):
        if not p.is_file():
            print(f"missing: {p.relative_to(ROOT)}")
            return 1

    inputs = load_inputs()
    _, _, _, counts, _ = inputs
    population, probe, probe_all, multi, band, band2, band3 = population_of(counts)
    text = PAGE.read_text(encoding="utf-8")
    problems, measured = passes(text, inputs, population, probe, probe_all, multi)
    sync = RD.sync_problems(PAGE, text)
    problems.extend(sync)

    print(f"population rule      (probe {ep.PROBE}) AND (>=2 manuscripts), "
          f"union {len(ep.DENSEST)} named densest families, "
          f"union band 1 (n==2, no probe word), union band 2 (n==3-4, no probe word), "
          f"union band 3 (n>=5, no probe word)")
    print(f"population           {len(population)} families, "
          f"{sum(counts[f] for f in population)} manuscripts")
    print(f"band 1               {len(band)} families, {2 * len(band)} manuscripts")
    print(f"band 2               {len(band2)} families, {sum(counts[f] for f in band2)} manuscripts")
    print(f"band 3               {len(band3)} families, {sum(counts[f] for f in band3)} manuscripts")
    print(f"page                 {PAGE.relative_to(ROOT)}")
    print()
    print("measured:")
    for label, value in measured.items():
        print(f"  {label:52} {value:4}")
    print(f"  {'sync problems':52} {len(sync):4}")
    print()
    print(f"problems             {len(problems)}")
    for p in problems:
        print(f"  {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
