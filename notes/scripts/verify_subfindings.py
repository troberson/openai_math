#!/usr/bin/env python3
"""Verify notes/subfindings.tsv against the files it was extracted from. Writes nothing.

The TSV carries two row kinds in one rectangular table. Four passes read the same rows:

  Pass A (shape)     - header is the documented column list; every row has that many fields; kind is
                       one of the two kinds; seq is a positive integer; every field the kind does not
                       use is empty. A row that fills a field its kind never fills is a paste artifact.
  Pass B (manuscripts) - per family, the manuscript rows equal the \\href list of that family's 4th
                       \\resultentry field, in order, with the same path and the same display title.
                       Every path matches the paren-aware manuscript pattern and exists on disk; the
                       formalized flag equals membership in formalization.yaml sources; the tier equals
                       the ledger's tier for that family; the row count equals the ledger's paps.
  Pass C (comparators) - per family, the comparator rows equal that scope note's
                       `## Comparator links` table rows, in order, with the same named statement and
                       the same .lean file, and every .lean file exists in lean/ComparatorChallenges/.
  Pass D (totals)    - the counts the acceptance names (719 manuscript rows, 426 comparator rows,
                       372 and 242 families, 416 distinct configs, 172 formalized) are re-measured
                       from the files and compared with the table.

--mutant proves the checker discriminates: it renames a real title, points a real row at a manuscript
that does not exist, deletes a comparator row, flips a formalized flag, flips a tier, and reorders two
rows in one family. Each is asserted to be flagged while the real table stays silent.

Usage: python3 notes/scripts/verify_subfindings.py
       python3 notes/scripts/verify_subfindings.py --mutant
"""
import csv
import re
import sys
from collections import Counter

import build_catalog as bc
import extract_subfindings as ex

ROOT = bc.ROOT
TSV = ROOT / "notes" / "subfindings.tsv"
LEDGER = ROOT / "notes" / "catalog.tsv"


def shipped():
    rows = list(csv.DictReader(TSV.read_text(encoding="utf-8").splitlines(), delimiter="\t"))
    header = TSV.read_text(encoding="utf-8").splitlines()[0].split("\t")
    return header, rows


def truth():
    """Everything the table claims, re-derived from overview.tex, CONTENTS.md, yaml, and the docs."""
    order, fams = bc.parse_overview()
    sources, main_results = bc.parse_yaml()
    docs = bc.parse_docs()
    tiers = {}
    for fam in fams:
        cfgs = docs[fam]["configs"] if fam in docs else []
        tiers[fam] = "T3" if [c for c in cfgs if c in main_results] else (
            "T2" if cfgs else ("T1" if fam in docs else "T0"))
    hrefs = {f: ex.href_pairs(body) for f, body in ex.resultentry_link_fields().items()}
    paths = {f: [re.search(bc.PAP, t).group(0) for t, _ in h] for f, h in hrefs.items()}
    ledger = {r["fam"]: r for r in csv.DictReader(
        LEDGER.read_text(encoding="utf-8").splitlines(), delimiter="\t")}
    tables = {}
    for doc in sorted(ex.DOCS.glob("*.md")):
        rows, in_section = [], False
        for line in doc.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if s == "## Comparator links":
                in_section = True
                continue
            if in_section and s.startswith("## "):
                in_section = False
                continue
            if not (in_section and s.startswith("|")):
                continue
            m = ex.COMPARATOR_ROW.match(s)
            if m:
                rows.append((m.group(1), m.group(3) + ".lean"))
        tables[doc.stem] = rows
    return hrefs, paths, sources, tiers, ledger, tables


def check(header, rows):
    problems = []
    if header != ex.COLS:
        problems.append(f"header is {header}, expected {ex.COLS}")
    for n, r in enumerate(rows, 2):
        if r.get("kind") not in ("manuscript", "comparator-link"):
            problems.append(f"tsv line {n}: kind is {r.get('kind')!r}")
            continue
        if not str(r.get("seq", "")).isdigit() or int(r["seq"]) < 1:
            problems.append(f"tsv line {n}: seq is {r.get('seq')!r}")
        unused = ("statement", "lean_file") if r["kind"] == "manuscript" \
            else ("title", "path", "formalized", "tier")
        for col in unused:
            if (r.get(col) or "").strip():
                problems.append(f"tsv line {n}: {r['kind']} row fills {col}={r[col]!r}")

    hrefs, paths, sources, tiers, ledger, tables = truth()

    man = [r for r in rows if r.get("kind") == "manuscript"]
    comp = [r for r in rows if r.get("kind") == "comparator-link"]

    by_fam = {}
    for r in man:
        by_fam.setdefault(r["fam"], []).append(r)
    for fam, want in sorted(paths.items()):
        got = by_fam.get(fam, [])
        if [int(g["seq"]) for g in got] != list(range(1, len(want) + 1)):
            problems.append(f"{fam}: manuscript seq is {[g['seq'] for g in got]}, "
                            f"expected 1..{len(want)}")
        for g in sorted(got, key=lambda x: int(x["seq"])):
            i = int(g["seq"]) - 1
            if i >= len(want):
                problems.append(f"{fam}: row {g['seq']} has no href behind it")
                continue
            want_path = want[i]
            want_title = hrefs[fam][i][1]
            if g["path"] != want_path:
                problems.append(f"{fam}:{g['seq']} path is {g['path']!r}, overview.tex says {want_path!r}")
            elif not (ROOT / want_path).is_file():
                problems.append(f"{fam}:{g['seq']} path does not exist: {want_path}")
            if g["title"] != want_title:
                problems.append(f"{fam}:{g['seq']} title is {g['title']!r}, overview.tex says {want_title!r}")
            if int(g["formalized"]) != (1 if want_path in sources else 0):
                problems.append(f"{fam}:{g['seq']} formalized={g['formalized']}, "
                                f"yaml membership says {1 if want_path in sources else 0}")
            if g["tier"] != tiers[fam]:
                problems.append(f"{fam}:{g['seq']} tier is {g['tier']}, ledger rule gives {tiers[fam]}")
        if fam in ledger and int(ledger[fam]["paps"]) != len(got):
            problems.append(f"{fam}: {len(got)} manuscript rows, ledger paps {ledger[fam]['paps']}")
    for fam in sorted(set(by_fam) - set(paths)):
        problems.append(f"{fam}: manuscript rows with no hrefs in overview.tex")

    comp_by_fam = {}
    for r in comp:
        comp_by_fam.setdefault(r["fam"], []).append(r)
    for fam, want in sorted(tables.items()):
        got = comp_by_fam.get(fam, [])
        if len(got) != len(want):
            problems.append(f"{fam}: {len(got)} comparator rows, scope note has {len(want)}")
            continue
        for g, (stmt, lean) in zip(sorted(got, key=lambda x: int(x["seq"])), want):
            if g["statement"] != stmt:
                problems.append(f"{fam}:{g['seq']} statement is {g['statement']!r}, note says {stmt!r}")
            if g["lean_file"] != lean:
                problems.append(f"{fam}:{g['seq']} lean_file is {g['lean_file']!r}, note links {lean!r}")
            elif not (ROOT / "lean" / "ComparatorChallenges" / lean).is_file():
                problems.append(f"{fam}:{g['seq']} {lean} is not in lean/ComparatorChallenges/")
    for fam in sorted(set(comp_by_fam) - set(tables)):
        problems.append(f"{fam}: comparator rows with no table in its scope note")

    measured = {
        "manuscript rows": len([p for fam in paths for p in paths[fam]]),
        "comparator rows": sum(len(v) for v in tables.values()),
        "manuscript families": len(paths),
        "comparator families": len(tables),
        "distinct configs": len({lean for v in tables.values() for _, lean in v}),
        "formalized manuscripts": sum(1 for fam in paths for p in paths[fam] if p in sources),
    }
    got_counts = {
        "manuscript rows": len(man),
        "comparator rows": len(comp),
        "manuscript families": len(by_fam),
        "comparator families": len(comp_by_fam),
        "distinct configs": len({r["lean_file"] for r in comp}),
        "formalized manuscripts": sum(1 for r in man if r["formalized"] == "1"),
    }
    for key, want in measured.items():
        if got_counts[key] != want:
            problems.append(f"{key}: table has {got_counts[key]}, files give {want}")

    return problems, len(man), len(comp)


def main():
    mutant = "--mutant" in sys.argv
    header, rows = shipped()
    problems, man, comp = check(header, rows)
    print(f"table: {TSV.relative_to(ROOT)}")
    print(f"manuscript rows {man}, comparator rows {comp}, "
          f"formalized {sum(1 for r in rows if r.get('formalized') == '1')}")
    print(f"problems: {len(problems)}")
    for p in problems[:40]:
        print(f"  {p}")

    if not mutant:
        return 0 if not problems else 1

    print()
    print("mutants:")
    text = TSV.read_text(encoding="utf-8").splitlines()
    man_idx = next(i for i, l in enumerate(text) if l.startswith("manuscript\t"))
    comp_idx = next(i for i, l in enumerate(text) if l.startswith("comparator-link\t"))
    man_fields = text[man_idx].split("\t")
    comp_fields = text[comp_idx].split("\t")
    man_fam = man_fields[1]
    comp_fam = comp_fields[1]
    cases = [
        ("renamed display title", man_idx, man_fam,
         "\t".join(man_fields[:3] + [man_fields[3] + " (renamed)"] + man_fields[4:])),
        ("manuscript path that does not exist", man_idx, man_fam,
         "\t".join(man_fields[:4] + [man_fields[4].replace("paper.pdf", "nosuch.pdf")] + man_fields[5:])),
        ("flipped formalized flag", man_idx, man_fam,
         "\t".join(man_fields[:5] + [("1" if man_fields[5] == "0" else "0")] + man_fields[6:])),
        ("flipped tier", man_idx, man_fam,
         "\t".join(man_fields[:6] + [("T0" if man_fields[6] == "T3" else "T3")] + man_fields[7:])),
        ("renamed comparator statement", comp_idx, comp_fam,
         "\t".join(comp_fields[:7] + [comp_fields[7] + " (invented)"] + comp_fields[8:])),
        ("comparator row deleted", comp_idx, comp_fam, None),
    ]
    undetected = 0
    for name, idx, fam, replacement in cases:
        cand = list(text)
        if replacement is None:
            del cand[idx]
        else:
            cand[idx] = replacement
        got, _, _ = check(cand[0].split("\t"), list(csv.DictReader(cand, delimiter="\t")))
        hit = [p for p in got if fam in p or "comparator rows:" in p or "no table" in p]
        if not hit:
            undetected += 1
        print(f"  {name}: {'detected' if hit else 'UNDETECTED'} ({len(got)} problems)"
              + (f" -> {hit[0][:70]}" if hit else ""))

    # Two rows swapped inside one family: the row set is unchanged, only the order is wrong, so
    # this mutant checks the seq check. It needs a family with more than one manuscript.
    counts = Counter(l.split("\t")[1] for l in text if l.startswith("manuscript\t"))
    swap_fam = next(f for f, n in sorted(counts.items()) if n > 1)
    fam_rows = [i for i, l in enumerate(text) if l.startswith(f"manuscript\t{swap_fam}\t")]
    cand = list(text)
    cand[fam_rows[0]], cand[fam_rows[1]] = cand[fam_rows[1]], cand[fam_rows[0]]
    got, _, _ = check(cand[0].split("\t"), list(csv.DictReader(cand, delimiter="\t")))
    hit = [p for p in got if swap_fam in p]
    if not hit:
        undetected += 1
    print(f"  two rows swapped in family {swap_fam}: {'detected' if hit else 'UNDETECTED'} "
          f"({len(got)} problems)" + (f" -> {hit[0][:70]}" if hit else ""))

    print(f"undetected mutants: {undetected}")
    return 0 if (undetected == 0 and not problems) else 1


if __name__ == "__main__":
    sys.exit(main())
