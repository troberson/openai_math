#!/usr/bin/env python3
"""Write notes/subfindings.tsv: the manuscript and comparator rows the catalog encodes.

Extraction only, no interpretation. Two row kinds in one file, typed by the `kind` column:

  kind=manuscript      one row per \\href in the 4th field of \\resultentry: the family, the row's
                       order within the family, the href's display title, the manuscript path,
                       whether formalization.yaml lists that manuscript, and the family's tier.
                       The display titles are the release's own structural encoding of sub-findings
                       - family 102 ships five hrefs titled Unique Games theorem / Optimal Max-Cut
                       hardness / Factor-two Vertex Cover hardness / Constant-factor Min-UnCut
                       hardness / Directed feedback vertex set hardness.
  kind=comparator-link one row per link row of a scope note's `## Comparator links` table: the
                       family, the row's order in the table, the named statement, and the .lean file.

Fields a kind does not use are empty, so the file stays one rectangular TSV.

The 4th field is read by slicing, not by group-splitting: `read_args` walks braces with an escape
count, so a display title containing a brace cannot shift the split. Regex group-splitting on nested
braces silently mis-slices.

Deterministic: rows are sorted by kind, family, then document order. Run it twice and diff.

Usage: python3 notes/scripts/extract_subfindings.py
"""
import csv
import re
import sys
from collections import Counter

import build_catalog as bc

ROOT = bc.ROOT
OUT = ROOT / "notes" / "subfindings.tsv"
DOCS = ROOT / "lean" / "docs"
LEDGER = ROOT / "notes" / "catalog.tsv"

COLS = ["kind", "fam", "seq", "title", "path", "formalized", "tier", "statement", "lean_file"]

# A comparator table row: | named statement | [Name.lean](../ComparatorChallenges/Name.lean) |
COMPARATOR_ROW = re.compile(
    r"^\|\s*(.+?)\s*\|\s*\[(.+?)\]\(\.\./ComparatorChallenges/(.+?)\.lean\)\s*\|\s*$")


def resultentry_link_fields():
    """{fam: raw body of the 4th \resultentry brace group}, by slice-based brace reading."""
    text = (ROOT / "overview.tex").read_text(encoding="utf-8")
    i = text.index("\\begin{document}")
    links = {}
    while True:
        ns = text.find("\\cataloguesection{", i)
        nr = text.find("\\resultentry{", i)
        if nr == -1:
            return links
        if ns != -1 and ns < nr:
            _, i = bc.read_args(text, ns + len("\\cataloguesection"))
            continue
        args, i = bc.read_args(text, nr + len("\\resultentry"))
        links[args[0]] = args[3]


def href_pairs(body):
    """[(target, display title)] for every \\href{...}{...} in a 4th-field body, in order."""
    out = []
    k = 0
    while True:
        h = body.find("\\href", k)
        if h == -1:
            return out
        j = h + len("\\href")
        while j < len(body) and body[j] in " \t\n":
            j += 1
        if j >= len(body) or body[j] != "{":
            k = h + len("\\href")
            continue
        groups, after = bc.read_args(body, j)
        if len(groups) == 2:
            out.append((groups[0].strip(), groups[1].strip()))
        k = after


def manuscript_rows(tiers, sources):
    """One row per \\href, in family order then document order."""
    links_by_fam = resultentry_link_fields()
    rows = []
    for fam in sorted(links_by_fam):
        for n, (target, title) in enumerate(href_pairs(links_by_fam[fam]), 1):
            m = re.search(bc.PAP, target)
            if m is None:
                print(f"{fam}: href target names no manuscript: {target[:80]}")
                continue
            path = m.group(0)
            rows.append({"kind": "manuscript", "fam": fam, "seq": n, "title": title,
                         "path": path, "formalized": 1 if path in sources else 0,
                         "tier": tiers[fam], "statement": "", "lean_file": ""})
    return rows


def comparator_rows():
    """One row per link row of each scope note's `## Comparator links` table, in table order."""
    rows = []
    for doc in sorted(DOCS.glob("*.md")):
        fam = doc.stem
        lines = doc.read_text(encoding="utf-8", errors="replace").splitlines()
        in_section = False
        seq = 0
        for line in lines:
            s = line.strip()
            if s == "## Comparator links":
                in_section = True
                continue
            if in_section and s.startswith("## "):
                in_section = False
                continue
            if not (in_section and s.startswith("|")):
                continue
            m = COMPARATOR_ROW.match(s)
            if m is None:
                # The header and the | --- | --- | rule are the only other table lines.
                if s == "| Result | Comparator statement |" or set(s) <= {"-", "|", " "}:
                    continue
                print(f"{doc.name}: comparator table line not parsed: {s[:70]}")
                continue
            seq += 1
            rows.append({"kind": "comparator-link", "fam": fam, "seq": seq, "title": "",
                         "path": "", "formalized": "", "tier": "",
                         "statement": m.group(1), "lean_file": m.group(3) + ".lean"})
    return rows


def ledger_paps():
    """{fam: paps} as the generated ledger states it."""
    if not LEDGER.is_file():
        print(f"{LEDGER.name} not found - run notes/scripts/build_catalog.py first")
        return {}
    return {r["fam"]: int(r["paps"]) for r in
            csv.DictReader(LEDGER.read_text(encoding="utf-8").splitlines(), delimiter="\t")}


def main():
    _order, fams = bc.parse_overview()
    sources, main_results = bc.parse_yaml()
    docs = bc.parse_docs()
    tiers = {}
    for fam in fams:
        cfgs = docs[fam]["configs"] if fam in docs else []
        in_main = [c for c in cfgs if c in main_results]
        tiers[fam] = "T3" if in_main else ("T2" if cfgs else ("T1" if fam in docs else "T0"))

    manuscripts = manuscript_rows(tiers, sources)
    comparators = comparator_rows()

    OUT.write_text("\t".join(COLS) + "\n" + "\n".join(
        "\t".join(str(r[c]) for c in COLS) for r in manuscripts + comparators) + "\n",
        encoding="utf-8")

    paps = ledger_paps()
    href_by_fam = Counter(r["fam"] for r in manuscripts)
    mismatch = {f: (href_by_fam[f], paps[f]) for f in paps if href_by_fam[f] != paps[f]}
    configs = {r["lean_file"] for r in comparators}
    titles = [r["title"] for r in manuscripts]

    print(f"wrote {OUT.relative_to(ROOT)}: {len(manuscripts) + len(comparators)} rows")
    print(f"manuscript rows       {len(manuscripts)} over {len(href_by_fam)} families")
    print(f"comparator rows       {len(comparators)} over "
          f"{len({r['fam'] for r in comparators})} families, {len(configs)} distinct .lean files")
    print(f"paps vs href count    {len(mismatch)} mismatches over {len(paps)} families")
    for fam, (h, p) in sorted(mismatch.items()):
        print(f"  {fam}: {h} hrefs, ledger paps {p}")
    print(f"formalized flag       {sum(int(r['formalized']) for r in manuscripts)} manuscripts")
    print("tiers of manuscript rows  " + "  ".join(
        f"{t}={sum(1 for r in manuscripts if r['tier'] == t)}" for t in ("T3", "T2", "T1", "T0")))
    print(f"display titles        {len(set(titles))} distinct over {len(titles)} rows; "
          f"{sum(1 for t in set(titles) if titles.count(t) > 1)} titles used by >1 row")
    print(f"multi-manuscript families {sum(1 for c in href_by_fam.values() if c > 1)}, "
          f"carrying {sum(c for c in href_by_fam.values() if c > 1)} rows")
    dupes = sorted(f for f, c in Counter(r["fam"] for r in comparators).items()
                   if len([x for x in comparators if x["fam"] == f]) >
                   len({x["lean_file"] for x in comparators if x["fam"] == f}))
    print(f"families repeating a .lean file in their table: {len(dupes)} {' '.join(dupes)}")

    print()
    print("Not checked: whether a display title matches a clause of the family abstract, and whether")
    print("a named statement names a theorem that exists in the .lean file. Both are reading calls;")
    print("this file extracts what the release writes, nothing more.")


if __name__ == "__main__":
    sys.exit(main())
