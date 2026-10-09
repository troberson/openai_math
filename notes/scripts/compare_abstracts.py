#!/usr/bin/env python3
"""Compare each manuscript's own abstract with the abstract its family carries in overview.tex.

math-hqd.2. The ledger's claim-shape tags (`shapes`, `conditional`, `resolves_named`,
`counterex_broad`) are keyword rules over the abstract text in `overview.tex`. This script measures
what that text is relative to the manuscripts: is it the manuscript abstract, an abridgement of it,
or a rewrite? A plain run writes nothing and exits 1 when a reconciliation gate fails.

Three units, stated because they answer different questions:
  * manuscript-level: one comparison per manuscript dir listed in `notes/sources.tsv` (719 as of the
    2026-10-07 upstream merge), overview text vs that manuscript.
  * family-level: 372 comparisons, the best-matching manuscript in the family. A family carries up
    to 14 manuscripts and its overview abstract is a synthesis of them, so a low manuscript-level
    ratio is expected for multi-manuscript families and is not by itself a misstatement.
  * tag-level: the ledger's own rules applied to the overview text vs applied to the union of the
    family's manuscript abstracts, which is where the bead's question is answered.

Normalization is lossy and is stated in `norm`: LaTeX comments, cross-reference/citation macros,
math delimiters, braces, and whitespace runs are removed. Comparison is case-folded. A pair can
therefore read as identical while the shipped source differs in markup; the reverse cannot. Removing
a macro leaves a space where it sat, so a macro adjacent to punctuation ("...conjecture \\label{x}.")
cannot read identical — it reads abridged, which is the honest outcome for a normalizer that deletes
text.

`--tsv` writes `notes/abstracts.tsv` (one row per family) after the gates pass. `--mutant` corrupts
the measured population and fails if a gate goes uncaught.
"""

import csv
import difflib
import pathlib
import re
import statistics
import sys

import build_catalog as B

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRE = ROOT / "preprints"
LEDGER = ROOT / "notes" / "catalog.tsv"
SOURCES = ROOT / "notes" / "sources.tsv"
TSV_OUT = ROOT / "notes" / "abstracts.tsv"

# Macros whose arguments are references, not prose. Dropping them is what lets a manuscript abstract
# that says "\ref{thm:intro}" compare against an overview sentence that says the same theorem in words.
DROP = (r"label|ref|eqref|cite|citep|citet|url|hypertarget|labelcref|autoref"
        r"|newcommand|renewcommand|usepackage|documentclass|setlength|includegraphics")

RELATIONS = ("identical", "abridged", "divergent")
BUCKETS = ("<0.30", "0.30-0.50", "0.50-0.70", "0.70-0.90", ">=0.90")


def norm(s):
    """LaTeX abstract text -> comparable prose. Lossy; see the module docstring."""
    s = re.sub(r"(?<!\\)%.*", "", s)
    s = re.sub(r"\\begin\{abstract\}|\\end\{abstract\}", " ", s)
    s = re.sub(r"\\(" + DROP + r")\*?\s*(\[[^\]]*\])?\s*(\{[^{}]*\})?", " ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[{}$~]|\\\[|\\\]|\\\\", " ", s)
    return re.sub(r"\s+", " ", s).strip()


_CACHE: dict = {}


def manuscript_abstract(d):
    """-> [(relpath, normalized text)] for one preprint dir.

    `notes/sources.tsv`'s `abstract` column is a per-dir flag, not a count, so it reads 1 for all
    719 listed dirs while the corpus ships 722 abstract environments — 3 dirs carry two. A dir
    yielding 0 is a reconciliation failure; a dir yielding 2+ is reported, and the manuscript-level
    pass compares the overview text with that dir's best-matching abstract. Cached because the
    manuscript-level and tag-level passes both read every dir.
    """
    if d not in _CACHE:
        found = []
        for p in sorted((PRE / d).rglob("*.tex")):
            t = p.read_text(encoding="utf-8", errors="replace")
            for m in re.findall(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", t, re.S):
                found.append((str(p.relative_to(PRE)), norm(m)))
        _CACHE[d] = found
    return _CACHE[d]


def relation(ov, ms):
    """identical / abridged / divergent for a normalized pair.

    "abridged" means the shorter text is the longer one with a contiguous middle deleted — prefix
    and suffix kept, middle removed, which is what an abridgement does. A contiguous-substring test
    alone misses that (it only catches deletions at one end), so the common prefix and suffix are
    stripped and the shorter side must be fully consumed.
    """
    a, b = ov.lower(), ms.lower()
    if a == b:
        return "identical"
    if a and b:
        if a in b or b in a:
            return "abridged"
        short, long_ = (a, b) if len(a) <= len(b) else (b, a)
        i = 0
        while i < len(short) and short[i] == long_[i]:
            i += 1
        j = 0
        while j < len(short) - i and short[len(short) - 1 - j] == long_[len(long_) - 1 - j]:
            j += 1
        if len(short) - i - j == 0:
            return "abridged"
    return "divergent"


def ratio(ov, ms):
    return difflib.SequenceMatcher(None, ov.lower(), ms.lower()).ratio()


def bucket(r):
    return (">=0.90" if r >= 0.90 else "0.70-0.90" if r >= 0.70 else
            "0.50-0.70" if r >= 0.50 else "0.30-0.50" if r >= 0.30 else "<0.30")


def stats(vals):
    v = sorted(vals)
    q = statistics.quantiles(v, n=10)
    return {"n": len(v), "min": v[0], "p10": q[0], "median": statistics.median(v),
            "p90": q[8], "max": v[-1]}


def measure():
    _order, fams = B.parse_overview()
    rows = list(csv.DictReader(SOURCES.open(encoding="utf-8"), delimiter="\t"))
    ledger = list(csv.DictReader(LEDGER.open(encoding="utf-8"), delimiter="\t"))

    # manuscript-level
    man = []
    envs = 0
    empty_dirs = []
    multi_dirs = []
    for r in rows:
        found = manuscript_abstract(r["dir"])
        envs += len(found)
        if not found:
            empty_dirs.append(r["dir"])
            continue
        if len(found) > 1:
            multi_dirs.append((r["fam"], r["dir"], len(found)))
        ov = norm(fams[r["fam"]]["abstract"])
        best = max(found, key=lambda x, ov=ov: ratio(ov, x[1]))
        man.append({"fam": r["fam"], "dir": r["dir"], "file": best[0],
                    "ratio": ratio(ov, best[1]), "relation": relation(ov, best[1]),
                    "ov": fams[r["fam"]]["abstract"], "ms": best[1]})

    # family-level: best-matching manuscript per family
    byfam = {}
    for m in man:
        cur = byfam.get(m["fam"])
        if cur is None or m["ratio"] > cur["ratio"]:
            byfam[m["fam"]] = m
    fams_sorted = sorted(byfam)

    # tag-level: ledger rules over the overview text vs over the family's manuscript abstracts
    dirs_by_fam = {}
    for r in rows:
        dirs_by_fam.setdefault(r["fam"], []).append(r["dir"])
    tag_dis = {}
    tag_tot = {s: {"ov": 0, "ms": 0, "man": 0} for s in sorted(B.SHAPES)}
    cond_dis = []
    cond_detail = []
    fam_shapes = {}
    for fam in sorted(dirs_by_fam):
        ov_text = fams[fam]["abstract"]
        ms_text = " ".join(t for d in dirs_by_fam[fam] for _, t in manuscript_abstract(d))
        ovs, mss = set(B.shapes_of(ov_text)), set(B.shapes_of(ms_text))
        fam_shapes[fam] = {"ov": sorted(ovs), "ms": sorted(mss)}
        for s in ovs:
            tag_tot[s]["ov"] += 1
        for s in mss:
            tag_tot[s]["ms"] += 1
        # Per-manuscript rate, the control for union inflation: a 14-manuscript family gets 14
        # chances to flag a shape, so the family-level ms column is "some manuscript flags it",
        # not "the family is that shape".
        for d in dirs_by_fam[fam]:
            for _, t in manuscript_abstract(d):
                for s in B.shapes_of(t):
                    tag_tot[s]["man"] += 1
        for s in ovs | mss:
            if (s in ovs) != (s in mss):
                tag_dis.setdefault(s, {"ov-only": [], "ms-only": []})[
                    "ov-only" if s in ovs else "ms-only"].append(fam)
        if ("conditional" in ovs) != ("conditional" in mss):
            cond_dis.append(fam)
            cond_detail.append({"fam": fam, "ov": ov_text, "ms": ms_text,
                                "ov_flags": "conditional" in ovs,
                                "ms_flags": "conditional" in mss})

    return {
        "families": len(fams),
        "manuscripts": len(rows),
        "sources_rows": len(rows),
        "abstract_envs": envs,
        "empty_dirs": empty_dirs,
        "multi_dirs": multi_dirs,
        "dirs_with_abstract": sum(1 for r in rows if manuscript_abstract(r["dir"])),
        "man": man,
        "fam_best": byfam,
        "fam_order": fams_sorted,
        "man_relation": {k: sum(1 for m in man if m["relation"] == k) for k in RELATIONS},
        "man_ratio": stats([m["ratio"] for m in man]),
        "man_buckets": {k: sum(1 for m in man if bucket(m["ratio"]) == k) for k in BUCKETS},
        "fam_relation": {k: sum(1 for f in fams_sorted if byfam[f]["relation"] == k)
                         for k in RELATIONS},
        "fam_ratio": stats([byfam[f]["ratio"] for f in fams_sorted]),
        "fam_buckets": {k: sum(1 for f in fams_sorted if bucket(byfam[f]["ratio"]) == k)
                        for k in BUCKETS},
        "fam_hi": [f for f in fams_sorted if byfam[f]["ratio"] >= 0.90],
        "fam_lo": [f for f in fams_sorted if byfam[f]["ratio"] < 0.05],
        "tag_dis": tag_dis,
        "tag_tot": tag_tot,
        "fam_shapes": fam_shapes,
        "fam_shape_dis": sorted(f for f in fam_shapes
                                if set(fam_shapes[f]["ov"]) != set(fam_shapes[f]["ms"])),
        "fam_shape_dis_ov_more": sum(1 for f in fam_shapes
                                     if len(set(fam_shapes[f]["ov"]) - set(fam_shapes[f]["ms"])) >
                                     len(set(fam_shapes[f]["ms"]) - set(fam_shapes[f]["ov"]))),
        "cond_dis": cond_dis,
        "cond_detail": cond_detail,
        "ledger_counts": {
            "conditional": sum(1 for r in ledger if r["conditional"] == "1"),
            "resolves_named": sum(1 for r in ledger if r["resolves_named"] == "1"),
            "counterex_broad": sum(1 for r in ledger if r["counterex_broad"] == "1"),
            "rows": len(ledger),
        },
        "recomputed": {
            "conditional": sum(1 for f in fams if "conditional" in B.shapes_of(fams[f]["abstract"])),
            "resolves_named": sum(1 for f in fams
                                  if B.resolves_named(fams[f]["title"], fams[f]["abstract"])),
            "counterex_broad": sum(1 for f in fams if B.counterex_broad(fams[f]["title"],
                                                                        fams[f]["abstract"])),
            "rows": len(fams),
        },
    }


def check(m):
    """Canonical gates. A failure means the comparison is not measuring what it claims to."""
    problems = []
    if m["families"] != 372:
        problems.append(f"families {m['families']} != 372")
    if m["manuscripts"] != m["sources_rows"]:
        problems.append(f"manuscripts {m['manuscripts']} != notes/sources.tsv rows {m['sources_rows']}")
    if m["dirs_with_abstract"] != m["manuscripts"]:
        problems.append(f"dirs with an abstract {m['dirs_with_abstract']} != manuscripts "
                        f"{m['manuscripts']} (notes/sources.tsv flags 1 for every dir)")
    if len(m["empty_dirs"]):
        problems.append(f"{len(m['empty_dirs'])} manuscript dirs carry no abstract environment: "
                        f"{m['empty_dirs'][:5]}")
    if m["abstract_envs"] < m["dirs_with_abstract"]:
        problems.append(f"abstract environments {m['abstract_envs']} < dirs with one "
                        f"{m['dirs_with_abstract']}")
    if len(m["man"]) != m["manuscripts"]:
        problems.append(f"comparisons {len(m['man'])} != manuscripts {m['manuscripts']}")
    if len(m["fam_best"]) != m["families"]:
        problems.append(f"family comparisons {len(m['fam_best'])} != families {m['families']}")
    for rel_key, buck_key, n, recs in (("man_relation", "man_buckets", m["manuscripts"], m["man"]),
                                        ("fam_relation", "fam_buckets", m["families"],
                                         list(m["fam_best"].values()))):
        if sum(m[rel_key].values()) != n:
            problems.append(f"{rel_key} relation counts sum to {sum(m[rel_key].values())}, not {n}")
        if sum(m[buck_key].values()) != n:
            problems.append(f"{buck_key} bucket counts sum to {sum(m[buck_key].values())}, not {n}")
        recount = {k: sum(1 for x in recs if x["relation"] == k) for k in RELATIONS}
        if recount != m[rel_key]:
            problems.append(f"{rel_key} {m[rel_key]} != recounted from the comparisons {recount}")
        rebucket = {k: sum(1 for x in recs if bucket(x["ratio"]) == k) for k in BUCKETS}
        if rebucket != m[buck_key]:
            problems.append(f"{buck_key} {m[buck_key]} != recounted from the comparisons {rebucket}")
    for name in m["ledger_counts"]:
        if m["ledger_counts"][name] != m["recomputed"][name]:
            problems.append(f"ledger {name} {m['ledger_counts'][name]} != recomputed from "
                            f"overview.tex {m['recomputed'][name]}")
    return problems


# Synthetic pairs: the relation classifier must label each one correctly, or the headline
# "0 identical / 0 abridged" is a property of the classifier rather than of the corpus.
SYNTH = [
    ("Proves the conjecture.", "Proves the conjecture.", "identical"),
    ("Proves the conjecture for every n.", "Proves the conjecture.", "abridged"),
    ("Proves the conjecture. It is sharp.", "Proves the conjecture.", "abridged"),
    ("Proves the conjecture.", "We construct a counterexample.", "divergent"),
    ("Proves the \\textbf{conjecture} for every n.", "Proves the conjecture for every n.", "identical"),
]

# Controls: real pairs whose measured relation is known, so a change to norm() that flattens the
# corpus is caught rather than reported as a finding.
CONTROLS = [
    ("198", "divergent", 0.90),
    ("240", "divergent", None),
    ("057", "divergent", None),
]

MUTANTS = {
    "manuscript dropped": lambda m: dict(m, man=m["man"][:-1]),
    "abstract env undercounted": lambda m: dict(m, abstract_envs=m["abstract_envs"] - 4),
    "family set widened": lambda m: dict(m, fam_best=dict(m["fam_best"], **{"999": m["man"][0]}),
                                         fam_order=sorted(set(m["fam_order"]) | {"999"})),
    "relation relabelled": lambda m: dict(m, man_relation={"identical": 1, "abridged": 0,
                                                           "divergent": len(m["man"]) - 1}),
    "bucket counts skewed": lambda m: dict(m, man_buckets={**m["man_buckets"],
                                                           "<0.30": m["man_buckets"]["<0.30"] + 1}),
    "ledger tag count altered": lambda m: dict(m, ledger_counts={**m["ledger_counts"],
                                                                 "conditional": 12}),
    "empty dir tolerated": lambda m: dict(m, empty_dirs=["A-dir-September-24-2026"]),
}


TSV_COLUMNS = ["fam", "n_man", "best_ratio", "relation", "best_dir", "best_file",
               "ov_shapes", "ms_shapes", "ov_only", "ms_only", "cond_ov", "cond_ms"]


def write_tsv(m):
    """notes/abstracts.tsv: one row per family, the per-family record the findings doc cites.

    `best_ratio`/`relation` are the family-level best match. `ov_shapes`/`ms_shapes` are the ledger's
    own rules applied to the overview text and to the union of the family's manuscript abstracts;
    `ov_only`/`ms_only` are their set differences. Rows are the unit the bead asked for — every
    divergent family gets a row, which at 372 rows is a table, not prose.
    """
    n_man = {}
    for x in m["man"]:
        n_man[x["fam"]] = n_man.get(x["fam"], 0) + 1
    with TSV_OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(TSV_COLUMNS)
        for fam in m["fam_order"]:
            b, sh = m["fam_best"][fam], m["fam_shapes"][fam]
            w.writerow([fam, n_man[fam], f"{b['ratio']:.3f}", b["relation"], b["dir"], b["file"],
                        " ".join(sh["ov"]), " ".join(sh["ms"]),
                        " ".join(sorted(set(sh["ov"]) - set(sh["ms"]))),
                        " ".join(sorted(set(sh["ms"]) - set(sh["ov"]))),
                        int("conditional" in sh["ov"]), int("conditional" in sh["ms"])])
    return TSV_OUT


def main():
    m = measure()

    if "--mutant" in sys.argv:
        uncaught = []
        for name, fn in MUTANTS.items():
            problems = check(fn(m))
            print(f"mutant {name}: {'caught' if problems else 'NOT CAUGHT'}"
                  f" ({len(problems)} problems)")
            if not problems:
                uncaught.append(name)
        bad_synth = []
        for ov, ms, want in SYNTH:
            got = relation(norm(ov), norm(ms))
            print(f"synthetic {want!r} -> {got!r}: {'ok' if got == want else 'WRONG'}")
            if got != want:
                bad_synth.append((ov, ms))
        mrel = {x["fam"]: x["relation"] for x in m["man"]}
        mrat = {x["fam"]: max(v["ratio"] for v in m["man"] if v["fam"] == x["fam"])
                for x in m["man"]}
        bad_ctrl = []
        for fam, want, floor in CONTROLS:
            ok = mrel.get(fam) == want and (floor is None or mrat.get(fam, 0) >= floor)
            print(f"control fam {fam}: want {want}"
                  f"{f' ratio>={floor}' if floor else ''} -> "
                  f"{mrel.get(fam)} {mrat.get(fam):.3f}: {'ok' if ok else 'WRONG'}")
            if not ok:
                bad_ctrl.append(fam)
        print(f"mutants not caught {len(uncaught)} of {len(MUTANTS)}   "
              f"synthetic wrong {len(bad_synth)}   controls wrong {len(bad_ctrl)}")
        raise SystemExit(1 if uncaught or bad_synth or bad_ctrl else 0)

    problems = check(m)
    for p in problems:
        print(f"PROBLEM {p}")
    if problems:
        raise SystemExit(1)

    if "--tsv" in sys.argv:
        write_tsv(m)
        print(f"wrote {TSV_OUT.relative_to(ROOT)}: {len(m['fam_order'])} rows")

    print(f"families            {m['families']}   manuscripts {m['manuscripts']}   "
          f"dirs with an abstract {m['dirs_with_abstract']}   "
          f"abstract environments {m['abstract_envs']} "
          f"({len(m['multi_dirs'])} dirs ship more than one)")
    print(f"ledger tags         conditional {m['ledger_counts']['conditional']}  "
          f"resolves_named {m['ledger_counts']['resolves_named']}  "
          f"counterex_broad {m['ledger_counts']['counterex_broad']}  "
          f"(recomputed from overview.tex: {m['recomputed']['conditional']} / "
          f"{m['recomputed']['resolves_named']} / {m['recomputed']['counterex_broad']})")

    for unit, _n, rel, rat, buck in (
            (f"MANUSCRIPT-LEVEL ({m['manuscripts']} comparisons: overview text vs that manuscript)",
             m["manuscripts"], m["man_relation"], m["man_ratio"], m["man_buckets"]),
            ("FAMILY-LEVEL (372 comparisons: overview text vs the best-matching manuscript)",
             m["families"], m["fam_relation"], m["fam_ratio"], m["fam_buckets"])):
        print(f"\n{unit}")
        print("  relation          " + "  ".join(f"{k}={rel[k]}" for k in RELATIONS))
        print(f"  difflib ratio     min {rat['min']:.3f}  p10 {rat['p10']:.3f}  "
              f"median {rat['median']:.3f}  p90 {rat['p90']:.3f}  max {rat['max']:.3f}")
        print("  buckets           " + "  ".join(f"{k}={buck[k]}" for k in BUCKETS))

    print(f"\n  families with a best match >=0.90  {m['fam_hi']}")
    print(f"  families with a best match <0.05   {len(m['fam_lo'])}: {m['fam_lo']}")

    print("\nTAG-LEVEL (ledger rules: overview text vs the union of the family's manuscript abstracts)")
    print(f"  {'shape':16}  ovfam msfam man{m['manuscripts']}  ov-only  ms-only")
    for s in sorted(B.SHAPES):
        d = m["tag_dis"].get(s, {"ov-only": [], "ms-only": []})
        t = m["tag_tot"][s]
        print(f"  {s:16} {t['ov']:5} {t['ms']:5} {t['man']:6}   {len(d['ov-only']):3}     {len(d['ms-only']):3}")
    print(f"  conditional disagreements: {len(m['cond_dis'])} families {m['cond_dis']}")
    print(f"  families disagreeing with the overview on >=1 shape: {len(m['fam_shape_dis'])} of "
          f"{m['families']} (overview carries strictly more shapes in "
          f"{m['fam_shape_dis_ov_more']} of them)")

    print("\nLARGEST DIVERGENCES (lowest family-level ratio; texts are the normalized forms)")
    for fam in sorted(m["fam_order"], key=lambda f: m["fam_best"][f]["ratio"])[:8]:
        b = m["fam_best"][fam]
        print(f"  fam {fam} ratio {b['ratio']:.3f}  {b['dir']}")
        print(f"    OV {b['ov']}")
        print(f"    MS {b['ms']}")

    print("\nCONDITIONAL TAG DISAGREEMENTS")
    for d in m["cond_detail"]:
        print(f"  fam {d['fam']} overview-flags={d['ov_flags']} manuscripts-flag={d['ms_flags']}")
        print(f"    OV {d['ov']}")
        print(f"    MS {d['ms']}")

    print(f"\nproblems {len(problems)}")
    raise SystemExit(1 if problems else 0)


if __name__ == "__main__":
    main()
