#!/usr/bin/env python3
"""Measure the node and edge population an index over this release would carry.

Report-only; writes nothing and runs nothing. Every count in notes/index-design.md comes from
population() here, so the design record quotes numbers a command reproduces.

Rules stated where they matter:

- `overview.tex` defines both `\\resultentry` and `\\cataloguesection` with `\\newcommand`, so a
  substring count of the command name is one too high: 18 and 373. Counts require the command at the
  start of a line: 17 and 372. The brace-qualified substring also reads 17 and 372, only because
  each definition writes `}[n]{` after the name.
- Traces are counted as distinct stems over files: the Mézard–Parisi trace ships as both `.pdf` and
  `.tex`, so 11 files carry 10 traces.
- Family→config is counted per family as a set, which is why it reads 405 here and 415 in
  notes/links.tsv, where 7 scope notes link one config twice.
- Manuscript ownership is the path component after `preprints`, never `parts[-2]`.
"""
import collections
import csv
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRE = ROOT / "preprints"
OAI = ROOT / "lean" / "OAI"
CHAL = ROOT / "lean" / "ComparatorChallenges"
DOCS = ROOT / "lean" / "docs"
YAML = ROOT / "lean" / "formalization.yaml"
LEDGER = ROOT / "notes" / "catalog.tsv"
LINKS = ROOT / "notes" / "links.tsv"
SUBF = ROOT / "notes" / "subfindings.tsv"


def tsv(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def count_lines(text, command):
    """Lines that *start* with a command, so a \\newcommand definition never counts."""
    return len([l for l in text.split("\n") if l.startswith("\\" + command)])


def population():
    rows = tsv(LEDGER)
    paps = [int(r["paps"]) for r in rows]
    ov = (ROOT / "overview.tex").read_text(encoding="utf-8")
    yml = YAML.read_text(encoding="utf-8")

    disc_dirs = [p for p in OAI.iterdir() if p.is_dir()]
    mod_dirs = [p for d in disc_dirs for p in d.iterdir() if p.is_dir()]
    lean_files = sum(1 for _ in OAI.rglob("*.lean"))

    ent = re.findall(
        r"comparator_config:\s*ComparatorChallenges/([A-Za-z0-9_]+)\.json\s*\n"
        r"\s*declaration:\s*(\S+)\s*\n\s*file:\s*(\S+)", yml)
    cfgs = {c for c, _, _ in ent}
    files = {f for _, _, f in ent}
    mod_of_file = {str(pathlib.PurePosixPath(f).parent) for f in files}
    ns_agree = sum(1 for _, d, f in ent if pathlib.PurePosixPath(f).parts[2] == d.split(".")[1])

    cfg_by_fam = {}
    dup_docs = 0
    for p in sorted(DOCS.glob("*.md")):
        found = re.findall(r"\.\./ComparatorChallenges/([A-Za-z0-9_]+)\.lean",
                           p.read_text(encoding="utf-8"))
        dup_docs += 1 if len(found) > len(set(found)) else 0
        cfg_by_fam[p.stem] = set(found)
    occ = sum(len(v) for v in cfg_by_fam.values())
    all_cfg = set().union(*cfg_by_fam.values())
    cfg2file = {c: f for c, _, f in ent}
    reach = len({f for f, cs in cfg_by_fam.items() if cs & set(cfg2file)})

    bib = list(PRE.rglob("*.bib"))
    bib_entries = 0
    for b in bib:
        txt = b.read_text(encoding="utf-8", errors="replace")
        bib_entries += len(re.findall(r"^\s*@\w+\s*{", txt, re.M))

    trace_files = [p for p in sorted((ROOT / "reasoning_traces").rglob("*")) if p.is_file()]
    ver = [r for r in rows if int(r["verification"]) > 0]
    sf = tsv(SUBF)
    kc = collections.Counter(r["kind"] for r in sf)
    links = {r["edge"]: r for r in tsv(LINKS)}
    bibrow = links["manuscript->corpus manuscript (bib href)"]
    resolved = int(re.search(r"(\d+) resolved edges", bibrow["detail"]).group(1))
    cross = int(re.search(r"(\d+) cross-family", bibrow["detail"]).group(1))
    msc_scanned = int(re.search(r"files scanned: (\d+)", links["family->MSC code"]["detail"]).group(1))
    kw_dirs = int(links["manuscript->\\keywords macro"]["count"])

    sizes = {}
    for p in sorted((ROOT / "notes").glob("*.tsv")):
        n = len([l for l in p.read_text(encoding="utf-8").split("\n") if l.strip()]) - 1
        sizes[p.name] = (p.stat().st_size, n)

    nodes = (len(rows) + sum(paps) + len(disc_dirs) + len(mod_dirs) + len(list(CHAL.glob("*.json")))
             + len(cfgs) + len(list(DOCS.glob("*.md"))) + len({p.stem for p in trace_files})
             + sum(int(r["verification"]) for r in rows))
    edges = (sum(paps) + len(rows) + sum(int(r["paps_form"]) for r in rows) + occ + len(ent)
             + resolved + len(sf))

    return {
        # nodes
        "families": len(rows),
        "manuscripts": sum(paps),
        "disciplines": count_lines(ov, "cataloguesection{"),
        "resultentries": count_lines(ov, "resultentry{"),
        "preprint_dirs": len([p for p in PRE.iterdir() if p.is_dir()]),
        "tex_files": len(list(PRE.rglob("*.tex"))),
        "bib_files": len(bib),
        "bib_entries": bib_entries,
        "lean_disc": len(disc_dirs),
        "lean_mods": len(mod_dirs),
        "lean_files": lean_files,
        "chal_json": len(list(CHAL.glob("*.json"))),
        "chal_lean": len(list(CHAL.glob("*.lean"))),
        "scope_notes": len(list(DOCS.glob("*.md"))),
        "mr_entries": len(ent),
        "mr_configs": len(cfgs),
        "mr_files": len(files),
        "mr_dirs": len(mod_of_file),
        "trace_files": len(trace_files),
        "traces": len({p.stem for p in trace_files}),
        "ver_dirs": sum(int(r["verification"]) for r in rows),
        "ver_fams": len(ver),
        "inputs": sum(int(r["inputs"]) for r in rows),
        "covmd": sum(int(r["covmd"]) for r in rows),
        # edges
        "e_fam_man": sum(paps),
        "e_fam_disc": len(rows),
        "formalized": sum(int(r["paps_form"]) for r in rows),
        "fam_cfg_occ": occ,
        "fam_cfg_distinct": len(all_cfg),
        "fam_cfg_fams": len(cfg_by_fam),
        "ns_agree": ns_agree,
        "reach": reach,
        "cfg_in_both": len(all_cfg & set(cfg2file)),
        "sf_rows": len(sf),
        "sf_man": kc["manuscript"],
        "sf_comp": kc["comparator-link"],
        "resolved": resolved,
        "cross": cross,
        "bib_hrefs": int(bibrow["count"]),
        "msc_scanned": msc_scanned,
        "kw_dirs": kw_dirs,
        "msc_hits": int(links["family->MSC code"]["count"]),
        "bib_kw": int(links["bibliography entry->keywords field"]["count"]),
        # granularity
        "max_paps": max(paps),
        "fams_1": sum(1 for p in paps if p == 1),
        "fams_2": sum(1 for p in paps if p >= 2),
        # rules the design record quotes alongside the counts
        "dup_docs": dup_docs,
        "substr_disc": ov.count("\\cataloguesection"),
        "substr_res": ov.count("\\resultentry"),
        "brace_disc": ov.count("\\cataloguesection{"),
        "brace_res": ov.count("\\resultentry{"),
        "builds_on": len(re.findall(r"relationship:\s*builds-on", yml)),
        "sf_bpr": sizes["subfindings.tsv"][0] / sizes["subfindings.tsv"][1],
        "ledger_set_bytes": sum(s for s, _ in sizes.values()),
        "rawbib_kib": bib_entries * 150 // 1024,
        "res_kib": resolved * 150 // 1024,
        "kw_pct": 100.0 * kw_dirs / sum(paps),
        # totals
        "nodes": nodes,
        "edges_resolved": edges,
        "edges_rawbib": edges + bib_entries,
        "sizes": sizes,
    }


def main():
    p = population()
    print("NODES")
    for k in ("families", "manuscripts", "disciplines", "resultentries", "preprint_dirs",
              "tex_files", "bib_files", "bib_entries", "lean_disc", "lean_mods", "lean_files",
              "chal_json", "chal_lean", "scope_notes", "mr_entries", "mr_configs", "mr_files",
              "mr_dirs", "trace_files", "traces", "ver_dirs", "ver_fams", "inputs", "covmd"):
        print(f"  {k:20} {p[k]}")
    print("EDGES")
    for k in ("e_fam_man", "e_fam_disc", "formalized", "fam_cfg_occ", "fam_cfg_distinct",
              "fam_cfg_fams", "mr_entries", "ns_agree", "reach", "cfg_in_both", "sf_rows",
              "sf_man", "sf_comp", "resolved", "cross", "bib_hrefs", "msc_hits", "msc_scanned",
              "bib_kw", "kw_dirs"):
        print(f"  {k:20} {p[k]}")
    print("GRANULARITY")
    for k in ("max_paps", "fams_1", "fams_2"):
        print(f"  {k:20} {p[k]}")
    print("RULES")
    print(f"  substring counts (no line-start rule) disc {p['substr_disc']} res {p['substr_res']}")
    print(f"  brace-qualified substring counts    disc {p['brace_disc']} res {p['brace_res']}")
    print(f"  scope notes linking a config twice {p['dup_docs']}")
    print(f"  yaml builds-on declarations       {p['builds_on']}")
    print(f"  subfindings B/row                 {p['sf_bpr']:.1f}")
    print(f"  notes/*.tsv total bytes           {p['ledger_set_bytes']}")
    print(f"  \\keywords share of manuscripts    {p['kw_pct']:.1f}%")
    print("TOTALS")
    print(f"  nodes (excl. {p['lean_files']} .lean files) {p['nodes']}")
    print(f"  edges (resolved citations)        {p['edges_resolved']}")
    print(f"  edges (incl. raw bib)             {p['edges_rawbib']}")
    print("SIZES")
    for name, (size, n) in p["sizes"].items():
        print(f"  {name:28} {size:7} B over {n:5} rows  {size / max(n, 1):5.1f} B/row")
    print(f"  projected raw-bib table      {p['bib_entries'] * 150 // 1024} KiB at 150 B/row")
    print(f"  projected resolved-edge table {p['resolved'] * 150 // 1024} KiB at 150 B/row")


if __name__ == "__main__":
    main()
