#!/usr/bin/env python3
"""Generate notes/catalog.tsv: one row per result family.

Reads only text metadata that ships in this repo:
  overview.tex, CONTENTS.md, lean/formalization.yaml, lean/docs/*.md,
  lean/ComparatorChallenges/*.json, preprints/ layout, reasoning_traces/.

Never invokes lean, lake, or comparator. Runtime is a few seconds.
"""

import re
from collections import defaultdict
from pathlib import Path

from catlib import ledger, overview, yaml
from catlib.paths import ROOT

OUT = ROOT / "notes" / "catalog.tsv"

# Re-exported for the scripts that import this module; the joins live in catlib/.
PAP = overview.PAP
MONTHS = overview.MONTHS
DATE_SUFFIX = overview.DATE_SUFFIX
SHAPES = ledger.SHAPES
read_args = overview.read_args
parse_overview = overview.parse_overview
parse_contents = overview.parse_contents
parse_yaml = yaml.parse_yaml
parse_challenges = yaml.parse_challenges
parse_docs = yaml.parse_docs
parse_traces = yaml.parse_traces
conditional_hits = ledger.conditional_hits
shapes_of = ledger.shapes_of
resolves_named = ledger.resolves_named
counterex_broad = ledger.counterex_broad
versions_of = ledger.versions_of
TARGET_NOUN = ledger.TARGET_NOUN
RESOLVE_VERB = ledger.RESOLVE_VERB
COUNTEREX_PHRASE = ledger.COUNTEREX_PHRASE

__all__ = [
    "COUNTEREX_PHRASE",
    "DATE_SUFFIX",
    "MONTHS",
    "OUT",
    "PAP",
    "RESOLVE_VERB",
    "ROOT",
    "SHAPES",
    "TARGET_NOUN",
    "conditional_hits",
    "counterex_broad",
    "main",
    "parse_challenges",
    "parse_contents",
    "parse_docs",
    "parse_overview",
    "parse_traces",
    "parse_yaml",
    "read_args",
    "resolves_named",
    "shapes_of",
    "versions_of",
]


def main():
    _order, fams = parse_overview()
    fam_paps = parse_contents()
    sources, main_results = parse_yaml()
    challenges = parse_challenges()
    docs = parse_docs()
    trace_by_fam, trace_unlisted = parse_traces()

    # Keyed by directory basename: `dirs` below holds names, not paths, and a
    # Path-vs-str membership test silently yields zero for every family.
    ver_dirs = {p.parent.name for p in (ROOT / "preprints").glob("*/verification")}
    inputs_dirs = {p.parent.name for p in (ROOT / "preprints").glob("*/INPUTS.md")}
    covmd_dirs = {p.parent.parent.name for p in (ROOT / "preprints").glob("*/verification/COVERAGE.md")}

    # Page presence is a filesystem fact, not a derived claim: the directory name is the
    # discipline lowercased with spaces hyphenated, so the glob is the whole test.
    summary_fams = {p.name[:3] for p in (ROOT / "notes" / "summaries").glob("*/*.md")
                    if re.match(r"^\d{3}-", p.name)}

    cols = [
        "fam", "discipline", "title", "paps", "paps_form", "tier", "chal", "mainres",
        "scope_note", "scope_chars", "verification", "inputs", "covmd", "trace",
        "shapes", "conditional", "resolves_named", "counterex_broad", "companions",
        "companion_word", "versions", "summary",
    ]
    rows = []
    for fam in sorted(fams):
        info = fams[fam]
        paths = fam_paps.get(fam, [])
        tex_paths = info["tex_paps"]
        all_paths = sorted(set(paths) | set(tex_paths))
        d = docs.get(fam)
        cfgs = d["configs"] if d else []
        in_main = [c for c in cfgs if c in main_results]
        if in_main:
            tier = "T3"
        elif cfgs:
            tier = "T2"
        elif d:
            tier = "T1"
        else:
            tier = "T0"
        shapes = shapes_of(info["abstract"])
        refs = sorted(set(re.findall(r"result (\d{3})", info["abstract"])))
        dirs = {Path(p).parts[-2] for p in all_paths}
        rows.append({
            "fam": fam,
            "discipline": info["discipline"],
            "title": info["title"],
            "paps": len(all_paths),
            "paps_form": sum(1 for p in all_paths if p in sources),
            "tier": tier,
            "chal": len(cfgs),
            "mainres": len(in_main),
            "scope_note": 1 if d else 0,
            "scope_chars": d["scope_chars"] if d else 0,
            "verification": sum(1 for x in dirs if x in ver_dirs),
            "inputs": sum(1 for x in dirs if x in inputs_dirs),
            "covmd": sum(1 for x in dirs if x in covmd_dirs),
            "trace": "|".join(sorted(trace_by_fam.get(fam, []))),
            "shapes": "|".join(shapes),
            "conditional": 1 if "conditional" in shapes else 0,
            "resolves_named": resolves_named(info["title"], info["abstract"]),
            "counterex_broad": counterex_broad(info["title"], info["abstract"]),
            "companions": "|".join(refs),
            "companion_word": 1 if re.search(r"\bcompanion", info["abstract"], re.I) else 0,
            "versions": versions_of(all_paths),
            "summary": 1 if fam in summary_fams else 0,
        })

    with OUT.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")

    # ---- report: every number quoted in notes/README.md comes from here ----
    paps_all = [p for fam in fams for p in set(fam_paps.get(fam, [])) | set(fams[fam]["tex_paps"])]
    print(f"families            {len(fams)}")
    print(f"manuscripts         {len(set(paps_all))}")
    print(f"formalized (yaml)   {len(sources)}")
    print(f"challenges          {len(challenges)}")
    print(f"main_results        {sum(main_results.values())} entries / {len(main_results)} unique configs")
    print(f"scope notes         {len(docs)}")
    print(f"verification dirs   {len(ver_dirs)}   INPUTS.md {len(inputs_dirs)}   COVERAGE.md {len(covmd_dirs)}")
    n_trace = sum(len(v) for v in trace_by_fam.values())
    print(f"reasoning traces    {n_trace} attributed by README.md, {len(trace_unlisted)} on disk unattributed")
    if trace_unlisted:
        print(f"  unattributed      {trace_unlisted}")
    print("\ntier                " + "  ".join(f"{t}={sum(1 for r in rows if r['tier'] == t)}"
                                              for t in ("T3", "T2", "T1", "T0")))
    print("shapes              " + "  ".join(f"{n}={sum(1 for r in rows if n in r['shapes'].split('|'))}"
                                            for n in SHAPES))
    multi = sum(1 for r in rows if len([s for s in r["shapes"].split("|") if s]) >= 3)
    plain = sum(1 for r in rows if not r["shapes"])
    print(f"                    {multi} families match >=3 shapes, {plain} match none")
    print(f"conditional         {[r['fam'] for r in rows if r['conditional']]}")
    rn = {r["fam"] for r in rows if r["resolves_named"]}
    res = {r["fam"] for r in rows if "resolution" in r["shapes"].split("|")}
    print(f"resolves_named      {len(rn)} families   `resolution` tag {len(res)}   "
          f"union {len(rn | res)}")
    print(f"                    {len(rn & res)} both, {len(res - rn)} tag-only "
          f"{sorted(res - rn)}, {len(rn - res)} column-only")
    print("                    " + "  ".join(
        f"{t}={sum(1 for r in rows if r['tier'] == t and r['resolves_named'])}"
        for t in ("T3", "T2", "T1", "T0")))
    cb = {r["fam"] for r in rows if r["counterex_broad"]}
    ct = {r["fam"] for r in rows if "counterexample" in r["shapes"].split("|")}
    print(f"counterex_broad     {len(cb)} of {len(rows)} families flagged (title+abstract)   "
          f"`counterexample` tag {len(ct)}   tag-only {len(ct - cb)}   flag-only {len(cb - ct)}")
    print("                    " + "  ".join(
        f"{t}={sum(1 for r in rows if r['tier'] == t and r['counterex_broad'])}"
        for t in ("T3", "T2", "T1", "T0"))
        + f"   {sum(int(r['paps']) for r in rows if r['counterex_broad'])} manuscripts behind them")
    print(f"versions>0          {sum(1 for r in rows if r['versions'])} families, "
          f"{sum(r['versions'] for r in rows)} dated re-issues")
    print(f"companion word      {sum(r['companion_word'] for r in rows)} families")
    print(f"summary pages       {sum(1 for r in rows if r['summary'])} of {len(rows)} families, "
          f"{sum(int(r['paps']) for r in rows if r['summary'])} manuscripts behind them")

    print("\n# discipline  fams  scope_notes  paps  paps_form")
    disc = defaultdict(lambda: [0, 0, 0, 0])
    for r in rows:
        c = disc[r["discipline"]]
        c[0] += 1
        c[1] += r["scope_note"]
        c[2] += r["paps"]
        c[3] += r["paps_form"]
    for name, (f, s, p, pf) in sorted(disc.items(), key=lambda kv: -kv[1][0]):
        print(f"{name:38} {f:4} {s:11} {p:5} {pf:9}")

    # Cross-check the two independent family -> manuscript mappings.
    tex_only = [(f, x) for f, x in
                ((f, sorted(set(fams[f]["tex_paps"]) - set(fam_paps.get(f, [])))) for f in sorted(fams)) if x]
    md_only = [(f, x) for f, x in
               ((f, sorted(set(fam_paps.get(f, [])) - set(fams[f]["tex_paps"]))) for f in sorted(fams)) if x]
    print(f"overview.tex links absent from CONTENTS.md: "
          f"{sum(len(x) for _, x in tex_only)} across {len(tex_only)} families")
    for f, x in tex_only:
        print(f"  fam {f}: {x}")
    print(f"CONTENTS.md links absent from overview.tex: "
          f"{sum(len(x) for _, x in md_only)} across {len(md_only)} families")
    for f, x in md_only:
        print(f"  fam {f}: {x}")
    missing = [f for f in sorted(fams) if not fam_paps.get(f)]
    if missing:
        print(f"families with no CONTENTS.md manuscript link: {missing}")
    print(f"rows written        {len(rows)} -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
