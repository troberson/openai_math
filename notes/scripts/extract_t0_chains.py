#!/usr/bin/env python3
r"""Report the T0 cross-family chains and the 27 two-manuscript second-pass families.

Report-only: writes nothing, runs nothing. Lean is never invoked, so nothing here checks a proof.

Population rule (all three conditions are needed to reproduce the 27):
  1. tier == T0 in notes/catalog.tsv,
  2. paps == 2 in notes/catalog.tsv,
  3. the family id appears in the second-pass reading sections of notes/t0-triage.md
     (the "Second pass: the remaining 93 families" heading through the line before
     "What the triage shows").
Repo-wide there are 96 families with exactly 2 manuscripts; 35 of them are T0; 8 of those 35
were read in the first pass, so 27 remain. The bead's "no coverage signal" framing holds for 26
of the 27 — 268 carries verification dirs on both manuscripts.

Chain rule: the release records a cross-family link only as a "result (NNN)" clause inside the
overview.tex abstract, which is what the ledger's `companions` column parses. That yields 2 edges
over 372 families. The `companion_word` column (\bcompanion in the same abstract) is a word, not
an edge: 9 families, none of them carrying a `companions` value.

Intra-family citation edges are manuscript-level: a release-labelled .bib entry (one carrying the
"OpenAI Math Release" note) whose href target is a preprints/<dir>/<file>.pdf that exists on disk,
where the citing and cited directories belong to the same family.
"""
import csv
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_catalog  # noqa: E402
import extract_links  # noqa: E402
import extract_subfinding_pairs as ep  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEDGER = ROOT / "notes" / "catalog.tsv"
SUBFINDINGS = ROOT / "notes" / "subfindings.tsv"
TRIAGE = ROOT / "notes" / "t0-triage.md"
SECOND_PASS_START = "## Second pass: the remaining 93 families"
SECOND_PASS_END = "## What the triage shows"
SIGNAL_COLS = ("paps_form", "chal", "mainres", "scope_note", "verification", "inputs", "covmd")


def ledger_rows():
    with LEDGER.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def second_pass_ids():
    text = TRIAGE.read_text(encoding="utf-8")
    a = text.index(SECOND_PASS_START)
    b = text.index(SECOND_PASS_END)
    return set(re.findall(r"\b(\d{3})\b", text[a:b]))


def manuscripts():
    """fam -> ordered list of manuscript rows from notes/subfindings.tsv."""
    out = {}
    with SUBFINDINGS.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["kind"] == "manuscript":
                out.setdefault(r["fam"], []).append(r)
    for rows in out.values():
        rows.sort(key=lambda r: int(r["seq"]))
    return out


def chain_edges(rows):
    vals = rows.values() if isinstance(rows, dict) else rows
    return [(r["fam"], e) for r in vals for e in r["companions"].split("|") if e]


def companion_word_fams(rows):
    vals = rows.values() if isinstance(rows, dict) else rows
    return [r["fam"] for r in vals if r["companion_word"] == "1"]


def release_bib_edges():
    """(citing_dir, cited_dir) for every release-labelled .bib href that resolves on disk.

    Scope is the listed manuscripts: a superseded edition on disk would count the same edge twice.
    """
    edges = set()
    for d, body in extract_links.bib_entries(extract_links.listed_dirs()):
        if "OpenAI Math Release" not in body:
            continue
        for url in extract_links.HREF.findall(body):
            m = extract_links.PREPRINT_URL.search(url)
            if m and (ROOT / "preprints" / m.group(1) / m.group(2)).exists():
                edges.add((d, m.group(1)))
    return edges


def bib_files(dirs):
    out = []
    for d in sorted(dirs):
        base = ROOT / "preprints" / d
        out += sorted(str(p.relative_to(ROOT)) for p in base.rglob("*.bib"))
    return out


def signal_sum(row):
    return sum(int(row[c]) for c in SIGNAL_COLS) + (1 if row["trace"] else 0) + int(row["summary"])


def population():
    rows = {r["fam"]: r for r in ledger_rows()}
    second = second_pass_ids()
    paps2 = [f for f, r in rows.items() if int(r["paps"]) == 2]
    t0_paps2 = [f for f in paps2 if rows[f]["tier"] == "T0"]
    pop = sorted(f for f in t0_paps2 if f in second)
    return {
        "rows": rows,
        "pop": pop,
        "paps2": sorted(paps2),
        "paps2_tiers": {t: sum(1 for f in paps2 if rows[f]["tier"] == t)
                        for t in ("T0", "T1", "T2", "T3")},
        "t0_paps2": sorted(t0_paps2),
        "first_pass": sorted(f for f in t0_paps2 if f not in second),
        "zero_signal": sorted(f for f in pop if signal_sum(rows[f]) == 0),
        "signal_outliers": sorted(f for f in pop if signal_sum(rows[f]) > 0),
    }


def intra_edges(dirs, edges):
    """Same-family citation edges among a set of manuscript directories, as (citing, cited)."""
    s = set(dirs)
    return sorted((a, b) for a, b in edges if a in s and b in s)


def main():
    v = population()
    rows, pop = v["rows"], v["pop"]
    mss = manuscripts()
    edges = release_bib_edges()
    lines = ep.resultentry_lines()
    fam_dirs = {f: sorted({extract_links.owner(pathlib.Path(m["path"])) for m in mss[f]}) for f in pop}
    fam_edges = {f: intra_edges(fam_dirs[f], edges) for f in pop}
    fam_mutual = {f: sum(1 for a, b in fam_edges[f] if (b, a) in fam_edges[f]) // 2 for f in pop}
    fam_bibs = {f: bib_files(fam_dirs[f]) for f in pop}

    print("== population")
    print(f"repo-wide paps==2            {len(v['paps2'])}")
    print("  by tier                    " + "  ".join(
        f"{t}:{n}" for t, n in sorted(v["paps2_tiers"].items()) if n))
    print(f"T0 with paps==2              {len(v['t0_paps2'])}")
    print(f"  read in the first pass     {len(v['first_pass'])} ({' '.join(v['first_pass'])})")
    print(f"second-pass T0 paps==2       {len(pop)}")
    print(f"  zero coverage signal       {len(v['zero_signal'])}")
    print(f"  with a signal              {len(v['signal_outliers'])} "
          f"({' '.join(v['signal_outliers'])})")
    print(f"  manuscripts                {sum(int(rows[f]['paps']) for f in pop)}")

    print("\n== chains recorded by the release (result (NNN) in the overview abstract)")
    ce = chain_edges(rows)
    print(f"edges over {len(rows)} families   {len(ce)}")
    for src, dst in ce:
        print(f"  {src} -> {dst}  overview.tex:{lines[src]}  "
              f"tiers {rows[src]['tier']}/{rows[dst]['tier']}")
    cw = companion_word_fams(rows)
    print(f"companion_word families      {len(cw)} ({' '.join(cw)})")
    print(f"  carrying a companions edge {sum(1 for f in cw if rows[f]['companions'])}")

    print("\n== chain-family coverage columns")
    for f in ("001", "032", "002", "006", "311"):
        r = rows[f]
        print(f"  {f} {r['tier']} paps={r['paps']} paps_form={r['paps_form']} chal={r['chal']} "
              f"mainres={r['mainres']} scope_note={r['scope_note']} verification={r['verification']} "
              f"trace={r['trace'] or '-'} shapes={r['shapes']}")

    print(f"\n== the {len(pop)} families")
    for f in pop:
        r = rows[f]
        print(f"{f} {r['discipline']} {r['tier']} paps={r['paps']} shapes={r['shapes'] or '-'} "
              f"ver={r['verification']} cw={r['companion_word']} overview.tex:{lines[f]} "
              f"edges={len(fam_edges[f])} mutual={fam_mutual[f]} bibfiles={len(fam_bibs[f])}")

    print(f"\n== manuscripts of the {len(pop)}")
    for f in pop:
        for m in mss[f]:
            print(f"{f} {m['seq']} form={m['formalized']} {m['title']} | {m['path']}")

    print("\n== intra-family citation edges")
    for f in pop:
        print(f"{f} {len(fam_edges[f])} "
              + ("; ".join(f"{a}->{b}" for a, b in fam_edges[f]) if fam_edges[f] else "none"))
    print(f"families with >=1 edge      {sum(1 for f in pop if fam_edges[f])}")
    print(f"families with a mutual pair {sum(1 for f in pop if fam_mutual[f])}")
    print(f"families with one-way only  {sum(1 for f in pop if fam_edges[f] and not fam_mutual[f])}")
    print(f"families with none          {sum(1 for f in pop if not fam_edges[f])}")
    print(f"  of those, no .bib at all  {sum(1 for f in pop if not fam_edges[f] and not fam_bibs[f])}")
    print("  no-.bib families          "
          + " ".join(f for f in pop if not fam_edges[f] and not fam_bibs[f]))

    print("\n== reconciliation")
    print(f"population rows == ledger paps  "
          f"{all(len(mss[f]) == int(rows[f]['paps']) for f in pop)}")
    print(f"manuscript rows                 {sum(len(mss[f]) for f in pop)}")
    print(f"paths exist on disk             "
          f"{all((ROOT / m['path']).exists() for f in pop for m in mss[f])}")
    print(f"every manuscript dir has README "
          f"{all((ROOT / 'preprints' / extract_links.owner(pathlib.Path(m['path'])) / 'README.md').exists() for f in pop for m in mss[f])}")
    print(f"tier matches ledger             "
          f"{all(m['tier'] == rows[f]['tier'] for f in pop for m in mss[f])}")
    print(f"formalized flags all zero       "
          f"{all(m['formalized'] == '0' for f in pop for m in mss[f])}")
    print(f"population all T0               {all(rows[f]['tier'] == 'T0' for f in pop)}")
    print(f"overview anchors in range       "
          f"{all(1 <= lines[f] <= len((ROOT / 'overview.tex').read_text(encoding='utf-8').split(chr(10))) for f in pop)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
