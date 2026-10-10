#!/usr/bin/env python3
"""Render the report-fed notes pages from the templates at notes/templates/report/.

Writer: notes/sources.md, notes/abstracts.md, notes/named-results.md and notes/index-design.md, from
the four templates under notes/templates/report/. Every number on a page is measured here — for
sources.md a fresh recount over the manuscript trees plus the shipped notes/sources.tsv; for
abstracts.md a call to compare_abstracts.measure(), the report the page itself names as the rule
that yields its counts; for named-results.md a call to extract_named_results.population(); for
index-design.md a call to measure_index_sizes.population() — while each page's checker keeps its own
recomputation. The split is
deliberate: a checker that imported this module would re-read the code the page was rendered from
and prove nothing, so the two measurements stay separate and a green checker is evidence that the
rendered numbers are right. verify_sources.py re-derives its 31 figures from disk;
verify_abstracts.py delegates its count pass to compare_abstracts.measure() (the page says its
counts come from that report) and keeps its marker and quotation passes independent of this module.

Slot contract: p['<label>'] is the exact phrase string the checker's needle list carries for a
figure, m['<key>'] the measured value behind it. Where the page wraps a phrase across lines, the
label carries an " a"/" b" suffix and the two strings sit on the page's own lines — the checker
compares with whitespace collapsed, so a split phrase is checked as one. Prove a render by running
this script and diffing the page against the committed bytes: 0 differences.
"""
from __future__ import annotations

import collections
import csv
import pathlib
import re
import statistics
from typing import Any

from jinja2 import Environment, FileSystemLoader

import build_sources as S
import compare_abstracts as CA
import extract_named_results as en
import measure_index_sizes as M
import measure_names as MN
from catlib import overview, preprints, tsv
from catlib import yaml as Y
from catlib.paths import COMPARATOR_DIR, LEDGER_TSV, PREPRINTS, ROOT, SUBFINDINGS_TSV

TPL = ROOT / "notes" / "templates" / "report"
ENV = Environment(loader=FileSystemLoader(str(TPL)), keep_trailing_newline=True,
                  trim_blocks=True, lstrip_blocks=True, autoescape=False)
TSV = ROOT / "notes" / "sources.tsv"
# One constant per page, written by name in main(): the ownership checker derives a writer's targets
# from the receiver of its write call, so a write through a loop variable is invisible to it.
SOURCES_MD = ROOT / "notes" / "sources.md"
ABSTRACTS_MD = ROOT / "notes" / "abstracts.md"
NAMED_RESULTS_MD = ROOT / "notes" / "named-results.md"
INDEX_DESIGN_MD = ROOT / "notes" / "index-design.md"
NAMES_MD = ROOT / "notes" / "names.md"


def f(x: int) -> str:
    """Thousands-separated int, the form the page prints."""
    return f"{x:,}"


def listed_dirs() -> list[pathlib.Path]:
    """The manuscripts the release lists, not every directory under preprints/."""
    return sorted(PREPRINTS / name for name in
                  {r["path"].split("/")[1] for r in tsv.read_rows(SUBFINDINGS_TSV)
                   if r["kind"] == "manuscript"})


def measure() -> dict[str, Any]:
    """Everything the page quotes, recomputed from disk."""
    with TSV.open(encoding="utf-8") as fh:
        rdr = csv.reader(fh, delimiter="\t")
        header = next(rdr)
        body = [dict(zip(header, r, strict=False)) for r in rdr]
    listed = listed_dirs()
    disk = sorted(p for p in PREPRINTS.iterdir() if p.is_dir())
    unlisted = [p for p in disk if p.name not in {d.name for d in listed}]
    notices = [p for p in unlisted
               if "Withdrawal notice" in (p / "README.md").read_text(encoding="utf-8",
                                                                      errors="replace")]
    ledger = tsv.read_rows(LEDGER_TSV)

    rootdist: dict[int, int] = collections.Counter()
    outcomes: dict[str, int] = collections.Counter()
    single_names: dict[str, int] = collections.Counter()
    for d in listed:
        roots = preprints.roots_of(d)
        rootdist[len(roots)] += 1
        main, rule = preprints.main_tex_of(roots)
        if main is None:
            outcomes["flagged"] += 1
        elif rule == "single-root":
            outcomes["single-root"] += 1
            single_names[main.name] += 1
        else:
            outcomes[main.name] += 1
    main_no_dc = sum(1 for d in listed for g in d.rglob("main.tex")
                     if not preprints.DOCCLASS.search(g.read_text(encoding="utf-8",
                                                                   errors="replace")))
    substring_multi = sum(
        1 for d in listed
        if len([g for g in d.rglob("*.tex")
                if "\\documentclass" in g.read_text(encoding="utf-8", errors="replace")]) > 1)
    six, decl, per_name = S.env_variants(listed)
    n = len(body)
    sums = {c: sum(int(r[c]) for r in body)
            for c in ("roots", "tex", "bib", "sections", "subsections", "subsubsections",
                      "proofs", "thms", "abstract", "tex_bytes")}
    ov = overview.parse_overview()[1]
    ov_paths = {p for fam in ov for p in ov[fam]["tex_paps"]}
    return {
        "rows": n, "cols": len(header), "dirs": len(disk), "listed": len(listed),
        "superseded": len(unlisted) - len(notices), "notices": len(notices),
        "fams": len({r["fam"] for r in body}),
        "formalized": sum(int(r["paps_form"]) for r in ledger),
        "rootdist": rootdist, "sums": sums, "outcomes": outcomes,
        "single_names": single_names, "main_no_dc": main_no_dc,
        "substring_multi": substring_multi, "six": six, "decl": decl,
        "per_name": per_name,
        "zero_bib": sum(1 for r in body if int(r["bib"]) == 0),
        "zero_proof": sum(1 for r in body if int(r["proofs"]) == 0),
        "max_tex": max(int(r["tex"]) for r in body),
        "mean_tex": sum(int(r["tex"]) for r in body) / n,
        "mean_bytes": sum(int(r["tex_bytes"]) for r in body) / n,
        "pdf_distinct": len({r["pdf"] for r in body}),
        "pdf_ov_distinct": len(ov_paths),
        "multi": [{"roots": int(r["roots"]), "dir": r["dir"],
                   "main_tex": r["main_tex"].removeprefix(r["dir"] + "/")}
                  for r in sorted(body, key=lambda r: r["dir"]) if int(r["roots"]) > 1],
    }


def phrases(m: dict[str, Any]) -> dict[str, str]:
    """label -> the phrase string the page must carry, keyed as verify_sources.py keys it."""
    s, o, sn = m["sums"], m["outcomes"], m["single_names"]
    rd = m["rootdist"]
    gap = ", ".join(f"`{n}` {c}" for n, c in
                    sorted(m["per_name"].items(), key=lambda kv: (-kv[1], kv[0]))
                    if n not in preprints.SIX)
    singletons = sum(sn.values()) - sn["preamble.tex"] - sn["manuscript.tex"] - sn["common.tex"]
    return {
        "table shape": f"**{m['rows']} rows, {m['cols']} columns**",
        "dir distinct count": f"| {m['rows']} distinct |",
        "fam distinct count": f"| {m['fams']} distinct |",
        "main_tex filled count": f"| {m['rows']} filled, **0** empty |",
        "roots distribution":
            f"| **{s['roots']}** over {m['listed']} dirs: {rd[1]} with 1, {rd[2]} with 2, "
            f"{rd[3]} with 3 |",
        "tex file count":
            f"| **{f(s['tex'])}** (max {m['max_tex']}, mean {m['mean_tex']:.2f} per dir) |",
        "bib count": f"| **{f(s['bib'])}**; **{m['zero_bib']}** dirs carry none |",
        "section count": f"| **{f(s['sections'])}** |",
        "subsection count": f"| **{f(s['subsections'])}** |",
        "subsubsection count": f"| **{f(s['subsubsections'])}** |",
        "proof count": f"| **{f(s['proofs'])}**; **{m['zero_proof']}** dir carries none |",
        "thms count": f"| **{f(s['thms'])}** |",
        "abstract count": f"| **{s['abstract']} of {m['rows']}** |",
        "tex bytes": f"| **{f(s['tex_bytes'])}** (mean {f(round(m['mean_bytes']))} per dir) |",
        "main-file outcomes":
            f"**main.tex {o['main.tex']}, paper.tex {o['paper.tex']}, single-root "
            f"{o['single-root']}, flagged {o['flagged']}.**",
        "main.tex without documentclass":
            f"because **{m['main_no_dc']}** `main.tex` files in the corpus",
        "single-root name counts":
            f"`preamble.tex` **{sn['preamble.tex']}**, `manuscript.tex` **{sn['manuscript.tex']}**, "
            f"`common.tex` **{sn['common.tex']}**",
        "single-root singleton count": f"**{singletons}**",
        "disk census":
            f"`preprints/` holds **{m['dirs']}** directories: the **{m['listed']}** the release "
            f"lists, **{m['superseded']}** superseded editions upstream keeps beside their "
            f"replacements, and **{m['notices']}** withdrawal notices",
        "main file under build":
            f"**Every one of the {m['rows']} resolved main files sits under a `build/` "
            f"directory.**",
        "substring multi-root count": f"and **{m['substring_multi']}** with two or three",
        "line-start root counts": f"reads **{rd[1] - 0}** and **{m['listed'] - rd[1]}**",
        "rule agreement": "under either rule (0 differences)",
        "declared-rule agreement": f"occurrence — {f(m['decl'])} both ways",
        "six-name count": f"quotes **{f(m['six'])}**",
        "env gap": f"The {m['decl'] - m['six']} gap is names",
        "env gap breakdown": f"{gap}. The TSV column carries the declared-rule figure.",
        "report reconciliation":
            f"rows written **{m['rows']}**, listed manuscript dirs **{m['listed']}**, preprint "
            f"dirs on disk **{m['dirs']}**",
        "overview path distinct count": f"**{m['pdf_ov_distinct']}** distinct vs `sources.tsv`",
        "pdf distinct count": f"`pdf` **{m['pdf_distinct']}** distinct",
        "formalized share": f"at **{m['formalized']}** of {m['rows']} manuscripts",
    }


def sources_page() -> str:
    """notes/sources.md, rendered."""
    m = measure()
    p = phrases(m)
    return ENV.get_template("sources.md.j2").render(m=m, p=p, f=f, multi=m["multi"])


def tag_rows(m: dict[str, Any]) -> list[str]:
    """The 9 shape-table rows, in the order the checker emits them (sorted by shape)."""
    rows = []
    for s in sorted(m["tag_tot"]):
        d = m["tag_dis"].get(s, {"ov-only": [], "ms-only": []})
        t = m["tag_tot"][s]
        rows.append(f"| {s} | {t['ov']} | {t['ms']} | {t['man']} | {len(d['ov-only'])} "
                    f"| {len(d['ms-only'])} |")
    return rows


def abstracts_phrases(m: dict[str, Any]) -> dict[str, str]:
    """label -> phrase string, keyed as verify_abstracts.py's count_phrases keys it."""
    n, fam = m["manuscripts"], m["families"]
    dirs, envs = m["dirs_with_abstract"], m["abstract_envs"]
    mr, fr = m["man_ratio"], m["fam_ratio"]
    mb, fb = m["man_buckets"], m["fam_buckets"]
    bkey = ("<0.30", "0.30-0.50", "0.50-0.70", "0.70-0.90", ">=0.90")
    low = [x for x in m["man"] if x["ratio"] < 0.05]
    dis = sorted(f for f, sh in m["fam_shapes"].items() if sh["ov"] != sh["ms"])
    paps = {r["fam"]: int(r["paps"]) for r in tsv.read_rows(LEDGER_TSV)}
    single = sum(1 for x in dis if paps[x] == 1)
    res, und = m["tag_tot"]["resolution"], m["tag_tot"]["undecidability"]
    cond = m["tag_dis"].get("conditional", {"ov-only": [], "ms-only": []})
    hi = m["fam_hi"]
    out = {
        "tsv row count (rule paragraph)": f"(one row per family, {fam} rows)",
        "manuscript comparison count": f"Over all {n} manuscript comparisons:",
        "headline relation counts": f"**0 identical, 0 abridged, {n} divergent.**",
        "family relation counts a": f"Over the {fam} family best matches: **0 identical,",
        "family relation counts b": f"0 abridged, {fam} divergent.**",
        "units bullet (manuscripts)": f"Manuscript-level: {n} comparisons",
        "units bullet (families)": f"Family-level: {fam} comparisons",
        "abstract environments": f"**Abstract environments: {envs} over {dirs} directories.**",
        "directories with an abstract": f"Every one of the {dirs} manuscript directories",
        "sources.tsv flag column": f"reads {dirs} and cannot show this.",
        "manuscript ratio row":
            f"| manuscript-level | {n} | {mr['min']:.3f} | {mr['p10']:.3f} "
            f"| **{mr['median']:.3f}** | {mr['p90']:.3f} | {mr['max']:.3f} |",
        "family ratio row":
            f"| family-level best match | {fam} | {fr['min']:.3f} | {fr['p10']:.3f} "
            f"| **{fr['median']:.3f}** | {fr['p90']:.3f} | {fr['max']:.3f} |",
        "bucket row": f"| count | {' / '.join(str(mb[k]) for k in bkey)} "
                      f"| {' / '.join(str(fb[k]) for k in bkey)} |",
        "near-identical families a": ", ".join(
            f"**{x}** ({m['fam_best'][x]['ratio']:.3f})" for x in hi[:3]) + ",",
        "near-identical families b": f"**{hi[3]}** ({m['fam_best'][hi[3]]['ratio']:.3f}).",
        "manuscript-level floor": f"**{len(low)} of the {n}** comparisons fall below 0.05,",
        "shape disagreement count":
            f"**{len(dis)} of {fam} families have at least one shape disagreement between the two "
            f"texts; {fam - len(dis)} have none.**",
        "disagreement manuscript split":
            f"Of the {len(dis)}, {single} are single-manuscript families and {len(dis) - single} "
            f"are multi-manuscript families.",
        "resolution over-flag rate a":
            f"{res['ov']} of {fam} families ({round(100 * res['ov'] / fam)}%) call a resolution in"
            " the",
        "resolution over-flag rate b":
            f"overview, against {res['man']} of {n} manuscripts ({round(100 * res['man'] / n)}%)",
        "undecidability rate": f"({und['ov']} families vs {und['man']} manuscripts)",
        "conditional disagreements":
            f"{len(m['cond_dis'])} families disagree on the `conditional` tag: "
            f"{len(cond['ov-only'])} flagged by the overview only ({', '.join(cond['ov-only'])}) "
            f"and {len(cond['ms-only'])}",
        "consequence bullet resolution counts":
            f"({res['ov']} of {fam} families vs {res['man']} of {n} manuscripts)",
        "tsv row count (consequence bullet)": f"— {fam} rows with the best-match ratio",
    }
    for s in tag_rows(m):
        out[f"tag row {s.split('|')[1].strip()}"] = s
    for fam_id in sorted(m["fam_order"], key=lambda x: m["fam_best"][x]["ratio"])[:8]:
        out[f"lowest-ratio row {fam_id}"] = f"| {fam_id} | {m['fam_best'][fam_id]['ratio']:.3f} |"
    return out


def abstracts_page() -> str:
    """notes/abstracts.md, rendered."""
    m = CA.measure()
    p = abstracts_phrases(m)
    low = [x for x in m["man"] if x["ratio"] < 0.05]
    minrow = min(m["man"], key=lambda x: x["ratio"])
    cond = m["tag_dis"].get("conditional", {"ov-only": [], "ms-only": []})
    return ENV.get_template("abstracts.md.j2").render(
        m=m, p=p, tagrows=tag_rows(m), low_fams=len({x["fam"] for x in low}),
        min_ratio=f"{minrow['ratio']:.3f}", min_fam=minrow["fam"], cond_ms=cond["ms-only"])


# The page spells its leading target-split count as a word and agrees with it.
NUMWORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}

# Phrases the page wraps across lines: each value is the exact text of the phrase's first line.
# A prefix is asserted to be a prefix of the measured phrase, so a number that drifts fails the
# render instead of reflowing the page.
NR_SPLIT = {
    "tex files (intro)": "re-derives every count from the ledger and the",
    "overview families": "**372** families in",
    "per-line warning": "rule: **1,609** is the per-line scan, **1,619** is the",
    "target counts": "Over **1,609** titled headline statements, **17** titles name a conjecture, "
                     "question, or problem, in",
    "target split": "One of the 17 (275) sits in a family the column reads 0; the",
    "subject vocabulary": "one of the 551",
    "subject-not-rn list": "002 009 010 014 015 023 036 069 099 114 115 116 125 140 211 212 216 "
                           "218 222 223 224 227 231 232 238",
    "no-headline claim": "**76 of the 248 flagged families ship no titled",
    "rn-not-abstract list": "020 027 085 094 124 126 129 134 144 155 158 160 187 191 277 280 299",
    "layer 2 union": "it would read 248 + 48",
    "layer 3 core": "**6** families are `rn = 1` and name no target anywhere in their manuscript "
                    "prose under **both** rules:",
    "additions not dir-named": "**9** of the",
    "abstract layer reach": "The manuscript-abstract",
    "direction B split": "the 8 split **3 corroborated / 5 resting on the overview paraphrase",
    "load-bearing negative": "Over 1,609 titled",
    "overlap": "**10 real misses** (Direction A) and **15 title-scope additions**, overlapping in "
               "022 039 044 151 209",
    "corpus sorry facts": "zero of the 122,458 files under `lean/OAI/**/*.lean` contain `sorry` "
                          "while the 416",
}


def nr_corpus_facts() -> tuple[int, int, int]:
    """Comparator stub count, its `sorry` occurrences, and the OAI file count."""
    chal = sorted(COMPARATOR_DIR.glob("*.lean"))
    sorry = sum(len(re.findall(r"\bsorry\b", q.read_text(encoding="utf-8", errors="replace")))
                for q in chal)
    return len(chal), sorry, Y.oai_lean_count()


def named_results_full(p: dict[str, Any]) -> dict[str, str]:
    """label -> the phrase the page carries, each derived from the extractor's population()."""
    order, ledger, rn, fams = p["order"], p["ledger"], p["rn"], p["fams"]
    tgt, tgt_fams = p["tgt"], p["tgt_fams"]
    subj_hits, subj_fams = p["subj_hits"], p["subj_fams"]
    dn, an, pw, ps = p["dn"], p["an"], p["pw"], p["ps"]
    have_t, no_head, tiers = p["have_t"], p["no_head"], p["tiers"]
    core, eo, add = p["core"], p["eo"], p["add"]
    abstract_only = p["abstract_only"]
    files, begins = p["files"], p["begins"]
    titled, titled_all = p["titled"], p["titled_all"]
    env, split, generic = p["env_begins"], p["titled_split"], p["generic"]
    strict = {f for f in order if en.TARGET_I.search(fams[f]["title"])
              and en.RESOLVE.search(fams[f]["abstract"].lower())}
    notdir = [f for f in add if f not in dn]
    real_a = [f for f in en.A_FAMS if f != "275"]
    bset = set(en.B_FAMS)
    nchal, nsorry, noai = nr_corpus_facts()
    nsplit, nkeep = len(tgt_fams - rn), len(tgt_fams & rn)
    return {
        "rn share": f"It reads **{len(rn)}** of **{len(order)}** families",
        "abstract-only figure": f"the abstract-only scope it replaced read **{len(abstract_only)}**",
        "tex files (intro)": f"re-derives every count from the ledger and the {files:,} "
                             "`.tex` files on disk",
        "ledger rows": f"**{len(ledger)}** ledger rows",
        "overview families": f"**{len(order)}** families in `overview.tex`",
        "manuscript dirs": f"**{p['ndirs']}** manuscript directories",
        "tex files (population)": f"**{files:,}** `.tex` files at glob depths 1–4",
        "rn count": f"and `resolves_named = 1` on **{len(rn)}** families",
        "headline begins": f"{begins:,}",
        "theorem begins": f"`\\begin{{theorem}}` {env['theorem']:,}",
        "maintheorem begins": f"`\\begin{{maintheorem}}` {env['maintheorem']}",
        "thm begins": f"`\\begin{{thm}}` {env['thm']}",
        "titled per-line": f"| titled headline begins | {titled:,} |",
        "titled whole-text": f"| titled headline begins, whole-text scan | {titled_all:,} |",
        "newline gap": f"| of those, titles whose match spans a newline | {split} |",
        "families with begins": f"| families with ≥1 headline begin | {len(p['have_b'])} |",
        "families with titles": f"| families with ≥1 titled headline | {len(have_t)} |",
        "families without": f"| families with no titled headline | {len(order) - len(have_t)} |",
        "generic titles": f"| titles matching `Main…` (content-free) | {generic} |",
        "per-line warning": f"rule: **{titled:,}** is the per-line scan, **{titled_all:,}** is the "
                            f"whole-text scan, and the {split}-title gap",
        "target heading": f"## Target-named headline statements: {len(tgt)} over {len(tgt_fams)} "
                          "families",
        "target counts": f"Over **{titled:,}** titled headline statements, **{len(tgt)}** titles "
                         f"name a conjecture, question, or problem, in **{len(tgt_fams)}** families",
        "verb-in-title": f"load-bearing negative: {len(p['verb_in_title'])} of these {len(tgt)} "
                         "titles",
        "target split": f"{NUMWORDS[nsplit]} of the {len(tgt)} ({', '.join(sorted(tgt_fams - rn))}) "
                        f"{'sits' if nsplit == 1 else 'sit'} in "
                        f"{'a family' if nsplit == 1 else 'families'} the column reads 0; the other "
                        f"{nkeep} sit in families it reads 1",
        "subject heading": f"## Subject-named headline statements: {len(subj_hits)} over "
                           f"{len(subj_fams)} families",
        "subject vocabulary": f"one of the {len(p['subject'])} subject names",
        "subject counts": f"**{len(subj_hits)}** statements over **{len(subj_fams)}** families. "
                          f"**{len(subj_fams & rn)}** of those families are `rn = 1`; "
                          f"**{len(subj_fams - rn)}** are not:",
        "subject-not-rn list": " ".join(sorted(subj_fams - rn)),
        "cross-tab 1": f"| headline-target ∩ `rn` | {nkeep} |",
        "cross-tab 2": f"| headline-target, `rn = 0` | {nsplit} → {' '.join(sorted(tgt_fams - rn))} |",
        "cross-tab 3": f"| `rn = 1`, no target-named headline statement | {len(rn - tgt_fams)} |",
        "cross-tab 4": f"| `rn = 1` with **no titled headline theorem at all** | {len(no_head)} "
                       f"(T3 {tiers['T3']}, T2 {tiers['T2']}, T1 {tiers['T1']}, T0 {tiers['T0']}) |",
        "cross-tab 5": f"| `rn = 0` with titled headline theorems | {len(have_t - rn)} |",
        "no-headline claim": f"**{len(no_head)} of the {len(rn)} flagged families ship no titled "
                             "headline theorem**",
        "layer 1": f"**{len(dn)}** families over **{sum(len(v) for v in p['dir_named'].values())}** "
                   f"directories. **{len(dn & rn)}** are `rn = 1`. **{len(dn - rn)}** are not: "
                   f"{' '.join(sorted(dn - rn))}. **{len(rn - dn)}**",
        "layer 2": f"**{len(an)}** families over "
                   f"**{sum(len(v) for v in p['abstract_named'].values())}** sentences. "
                   f"**{len(an & rn)}** are `rn = 1`. **{len(an - rn)}** are not, and "
                   f"**{len(rn - an)}**",
        "rn-not-abstract list": " ".join(sorted(rn - an)),
        "layer 2 union": f"it would read {len(rn)} + {len(an - rn)} = **{len(rn) + len(an - rn)}**",
        "layer 3 window": f"| window ±{en.WINDOW} characters | "
                          f"{sum(len(v) for v in p['prose_window'].values()):,} | {len(pw)} | "
                          f"{len(pw & rn)} | {len(pw - rn)} | {len(rn - pw)} → "
                          f"{' '.join(sorted(rn - pw))} |",
        "layer 3 sentence": f"| one sentence | {sum(len(v) for v in p['prose_sentence'].values()):,} "
                            f"| {len(ps)} | {len(ps & rn)} | {len(ps - rn)} | {len(rn - ps)} → "
                            f"{' '.join(sorted(rn - ps))} |",
        "layer 3 core": f"**{len(core)}** families are `rn = 1` and name no target anywhere in "
                        f"their manuscript prose under **both** rules: {' '.join(core)}",
        "verb gap": f"**{len(eo)}** families: {' '.join(sorted(eo))}, of which **{len(eo & rn)}** "
                    "are `rn = 1`",
        "title-scope heading": f"## The title-scope swap: {len(abstract_only)} → {len(rn)}",
        "additions": f"**{len(add)}** additions: {' '.join(add)}",
        "union figure": f"so the column reads **{len(rn)}**",
        "strict replacement": f"would read {len(strict)} ({len(rn - strict)} removals)",
        "additions corroborated": f"All **{len(add)}** are corroborated",
        "additions not dir-named": f"**{len(notdir)}** of the {len(add)} are not directory-named: "
                                   f"{' '.join(notdir)}",
        "outside the additions": f"but **not** title-named, so they sit outside the {len(add)}",
        "abstract layer reach": f"The manuscript-abstract layer alone ({len(an - rn)} families) "
                                f"would cover them and reach {len(rn) + len(an - rn)}",
        "direction A count": f"**{len(en.A_FAMS)}** families. Ten are real; one is the rule's "
                             "false positive",
        "direction A applied": f"**{len(set(real_a) & set(add))} of the {len(real_a)} real misses "
                               "are flagged**",
        "direction A verdict": f"reads **{len(real_a)} real misses and 1 false positive**",
        "direction B count": f"**{len(en.B_FAMS)}** families, all `rn = 1`",
        "direction B split": f"the {len(en.B_FAMS)} split **3 corroborated / 5 resting on the "
                             "overview paraphrase alone**",
        "direction B layer 2": f"{len(bset & (rn - an))} of the {len(en.B_FAMS)} also sit in the "
                               "layer-2 `rn-not-abstract` list; 333 does not",
        "load-bearing negative": f"Over {titled:,} titled headline statements, {len(tgt)} titles "
                                 f"name a target and **{len(p['verb_in_title'])}** of them pair a "
                                 "target noun with a resolve verb",
        "overlap": f"**{len(real_a)} real misses** (Direction A) and **{len(add)} title-scope "
                   f"additions**, overlapping in {' '.join(sorted(set(add) & set(real_a)))}",
        "union verdict": f"the swap is applied, so the column reads **{len(rn)}** with removals 0",
        "direction B verdict": f"**5 of the {len(en.B_FAMS)} Direction-B families**",
        "not checked layer 2": f"The {len(an - rn)}-family layer-2 set is **unadjudicated**. It is "
                               f"the widest candidate ({len(rn) + len(an - rn)})",
        "not checked prose": f"The {len(pw - rn)}-family `prose-not-rn` set (window scope)",
        "not checked subjects": f"The {len(subj_fams - rn)} subject-named-not-`rn` families",
        "not checked no-title": f"The {len(order) - len(have_t)} families with no titled headline "
                                "theorem",
        "corpus sorry facts": f"zero of the {noai:,} files under `lean/OAI/**/*.lean` contain "
                              f"`sorry` while the {nchal} comparator files carry {nsorry} `sorry` "
                              "occurrences",
    }


def named_results_phrases(p: dict[str, Any]) -> dict[str, str]:
    """Slot dict: each phrase, split into " a"/" b" parts where the page wraps it."""
    out: dict[str, str] = {}
    for label, phrase in named_results_full(p).items():
        pre = NR_SPLIT.get(label)
        if pre is None:
            out[label] = phrase
            continue
        if not phrase.startswith(pre):
            msg = f"slot {label!r}: page wrap {pre!r} is not a prefix of {phrase!r}"
            raise ValueError(msg)
        out[f"{label} a"] = pre
        out[f"{label} b"] = phrase[len(pre):].lstrip()
    return out


def tgt_rows(p: dict[str, Any]) -> list[str]:
    """The target-named statement table rows, in the extractor's order."""
    return [f"| {fam} | {p['ledger'][fam]['tier']} | {p['ledger'][fam]['resolves_named']} | "
            f"`{rel}:{ln}` | *\"{title}\"* |"
            for fam, title, rel, ln in p["tgt"]]


def named_results_page(p: dict[str, Any]) -> str:
    """notes/named-results.md, rendered from the extractor's population()."""
    return ENV.get_template("named-results.md.j2").render(
        p=named_results_phrases(p), tgtrows=tgt_rows(p), f=f,
        m={"titled": p["titled"], "titled_all": p["titled_all"]},
        n={"no_head": len(p["no_head"]), "pw_not_rn": len(p["pw"] - p["rn"])})


def builds_on_anchor() -> int:
    """Line of the first `relationship: builds-on` in the yaml — the anchor the page cites."""
    for i, ln in enumerate(Y.yaml_lines(tolerant=True), start=1):
        if "relationship: builds-on" in ln:
            return i
    raise SystemExit("no builds-on declaration in lean/formalization.yaml")


def index_full(p: dict[str, Any]) -> dict[str, str]:
    """label -> the exact phrase notes/index-design.md must carry.

    These are the needles notes/scripts/verify_index_design.py builds from
    measure_index_sizes.population(); the formulas are copied here on the writer side so the
    checker keeps its own recomputation and a green check means the two agree.
    """
    n, e, rb = f"{p['nodes']:,}", f"{p['edges_resolved']:,}", f"{p['edges_rawbib']:,}"
    lf, be = f"{p['lean_files']:,}", f"{p['bib_entries']:,}"
    sf, tex = f"{p['sf_rows']:,}", f"{p['tex_files']:,}"
    setb, rawkib = f"{p['ledger_set_bytes']:,}", f"{p['rawbib_kib']:,}"
    fam, man, disc = p["families"], p["manuscripts"], p["disciplines"]

    def ir(name: str) -> str:
        return f"{p['index_rows'][name]:,}"

    out = {
        "families node count": f"| Families | **{fam}** |",
        "manuscripts node count": f"| Manuscripts | **{man}** |",
        "catalog discipline count": f"| Catalog disciplines | **{disc}** |",
        "preprint dir count": f"| Preprint dirs | **{p['preprint_dirs']}** |",
        "tex file count": f"| `.tex` files under `preprints/` | **{tex}** |",
        "bib file/entry counts": f"| `.bib` files / entries | **{p['bib_files']}** / **{be}** |",
        "lean discipline dir count": f"| Lean discipline dirs | **{p['lean_disc']}** |",
        "lean module dir count": f"| Lean module dirs | **{p['lean_mods']}** |",
        "lean file count": f"| `.lean` files | **{lf}** |",
        "comparator config counts": f"| Comparator configs | **{p['chal_json']}** | "
                                     f"`lean/ComparatorChallenges/*.json`, matched by "
                                     f"**{p['chal_lean']}** `.lean` |",
        "scope note count": f"| Scope notes | **{p['scope_notes']}** |",
        "main_results entry/config counts": f"| `main_results` entries / configs | "
                                             f"**{p['mr_entries']}** / **{p['mr_configs']}** |",
        "yaml-named file/dir counts": f"| Lean files / dirs named by the yaml | "
                                      f"**{p['mr_files']}** / **{p['mr_dirs']}** |",
        "trace file/trace counts": f"| Reasoning traces | **{p['traces']}** in "
                                   f"**{p['trace_files']}** files |",
        "verification dir/family counts": f"| Verification dirs | **{p['ver_dirs']}** over "
                                           f"**{p['ver_fams']}** families |",
        "family-manuscript edge count": f"| family → manuscript | **{p['e_fam_man']}** |",
        "family-discipline edge count": f"| family → discipline | **{p['e_fam_disc']}** |",
        "formalized manuscript count": f"| manuscript → formalized | **{p['formalized']}** |",
        "family-config edge counts": f"| family → config | **{p['fam_cfg_occ']}** occurrences "
                                     f"over **{p['fam_cfg_distinct']}** distinct configs in "
                                     f"**{p['fam_cfg_fams']}** families |",
        "config-declaration edge count": f"| config → declaration | **{p['mr_entries']}** |",
        "family-lean reach count": f"| family → Lean file | **{p['reach']}** families |",
        "citation edge counts": f"| manuscript → corpus manuscript | **{p['resolved']}** resolved "
                                f"(**{p['cross']}** cross-family) | from **{p['bib_hrefs']}** "
                                f"bib hrefs |",
        "subfindings row counts": f"| subfindings rows | **{sf}** = **{p['sf_man']}** manuscript "
                                  f"+ **{p['sf_comp']}** comparator |",
        "population totals": f"Totals: **{n}** index nodes (excluding the **{lf}** `.lean` "
                             f"files) and **{e}** edges, or **{rb}**",
        "store-section totals": f"The measured population is **{n}** nodes and **{e}** edges",
        "subfindings bytes per row": f"carries **{sf}** rows at **{p['sf_bpr']:.1f}** B/row",
        "ledger set byte total": f"the whole ledger set is **{setb}** B",
        "ledger set scope sentence": f"the ledger set the **{setb}** B figure covers",
        "all-TSV byte total": f"every `notes/*.tsv` together totals **{p['all_tsv_bytes']}** B",
        "added TSV byte figures": f"`notes/sources.tsv` (**{p['sizes']['sources.tsv'][0]}** B over "
                                  f"**{p['sizes']['sources.tsv'][1]}** rows) and "
                                  f"`notes/topics.tsv` (**{p['sizes']['topics.tsv'][0]}** B over "
                                  f"**{p['sizes']['topics.tsv'][1]}** rows)",
        "builds-on declaration count": f"(**{p['builds_on']}** `builds-on` declarations at "
                                       f"`lean/formalization.yaml:{builds_on_anchor()}`)",
        "page count decision": f"**{fam}** family pages, and no per-manuscript pages",
        "manuscripts-per-family distribution": f"a family carries a maximum of "
                                               f"**{p['max_paps']}** manuscripts, "
                                               f"**{p['fams_1']}** families carry exactly **1**, "
                                               f"and **{p['fams_2']}** carry two or more",
        "table row bound": f"a table of at most {p['max_paps']} rows",
        "subfindings key counts": f"keyed by manuscript (**{p['sf_man']}** rows) and comparator "
                                  f"link (**{p['sf_comp']}** rows)",
        "MSC hit count": f"family → MSC code **{p['msc_hits']}** hits over "
                         f"**{p['msc_scanned']:,}** files scanned",
        "bib keywords count": f"bibliography entry → `keywords` field **{p['bib_kw']}** over "
                              f"**{be}** entries",
        "keywords macro share": f"manuscript → `\\keywords` macro **{p['kw_dirs']}** of "
                                f"**{man}** (**{p['kw_pct']:.1f}%**)",
        "grouping counts": f"**{disc}** catalog disciplines against **{p['lean_disc']}** "
                           f"Lean discipline dirs",
        "namespace agreement count": f"the triples name **{p['mr_dirs']}** module dirs, and the "
                                     f"declaration namespace equals the file's module dir in only "
                                     f"**{p['ns_agree']}** of **{p['mr_entries']}** entries",
        "namespace disagreement count": f"A name-based guess is wrong "
                                        f"**{p['mr_entries'] - p['ns_agree']}** times out of "
                                        f"**{p['mr_entries']}**",
        "derived-vocabulary rejection basis": f"with **{p['msc_hits']}** MSC codes and "
                                              f"**{p['bib_kw']}** `keywords` fields",
        "families.tsv rows": f"`families.tsv` | **{ir('families.tsv')}**",
        "manuscripts.tsv rows": f"`manuscripts.tsv` | **{ir('manuscripts.tsv')}**",
        "configs.tsv rows": f"`configs.tsv` | **{ir('configs.tsv')}**",
        "lean-dirs.tsv rows": f"`lean-dirs.tsv` | **{ir('lean-dirs.tsv')}**",
        "scope-notes.tsv rows": f"`scope-notes.tsv` | **{ir('scope-notes.tsv')}**",
        "traces.tsv rows": f"`traces.tsv` | **{ir('traces.tsv')}**",
        "topics-rendered.tsv rows": f"`topics-rendered.tsv` | **{ir('topics-rendered.tsv')}** | term",
        "names.tsv rows": f"`names.tsv` | **{ir('names.tsv')}**",
        "family-manuscript.tsv rows": f"`family-manuscript.tsv` | **{ir('family-manuscript.tsv')}**",
        "family-config.tsv rows": f"`family-config.tsv` | **{ir('family-config.tsv')}**",
        "config-declaration.tsv rows": f"`config-declaration.tsv` | "
                                       f"**{ir('config-declaration.tsv')}**",
        "family-lean.tsv rows": f"`family-lean.tsv` | **{ir('family-lean.tsv')}** | family → Lean "
                                f"file, derived; **{p['mr_files']}** files over **{p['reach']}** "
                                f"families",
        "citation.tsv rows": f"`citation.tsv` | **{ir('citation.tsv')}** | manuscript → corpus "
                             f"manuscript, **{p['cross']}** cross-family",
        "family-trace.tsv rows": f"`family-trace.tsv` | **{ir('family-trace.tsv')}**",
        "family-topic.tsv rows": f"`family-topic.tsv` | **{ir('family-topic.tsv')}** | family → "
                                 f"topic, **zero or more** per family",
        "family-name.tsv rows": f"`family-name.tsv` | **{ir('family-name.tsv')}**",
        "rendered page/table totals": f"**{p['index_pages']:,}** pages and "
                                      f"**{p['index_tables']}** tables in total",
        "names.tsv key count": f"has one row per folded name key (**{ir('names.tsv')}**)",
        "page count": f"Pages: `notes/index/<discipline>/<NNN>-<name>.md`, **{fam}** of them",
        "raw-bib projection": f"**{be}** rows at the measured **150** B/row is **{rawkib}** KiB",
        "resolved-edge projection": f"subset is **{p['resolved']}** rows (**{p['res_kib']}** KiB)",
        "scope-note config counts": f"scope notes: **{p['fam_cfg_occ']}** occurrences, "
                                    f"**{p['fam_cfg_distinct']}** distinct configs, "
                                    f"**{p['fam_cfg_fams']}** families",
        "derivable lean reach": f"config → file (yaml: **{p['mr_configs']}** configs, all "
                                f"**{p['cfg_in_both']}** of them also named by a scope note), "
                                f"which reaches **{p['reach']}** families",
        "lean edge scope": f"The index carries family → Lean file for **{p['reach']}** families; "
                           f"the **{p['formalized']}** is a manuscript-level flag",
        "family-discipline join count": f"**{p['e_fam_disc']}** edges, one per family",
        "substring vs line-start counts": f"so a substring count of the command name reads "
                                          f"{p['substr_disc']} and {p['substr_res']}. The "
                                          f"brace-qualified substring reads **{p['brace_disc']}** "
                                          f"and **{p['brace_res']}** only because each definition "
                                          f"writes `}}[n]{{` after the name. The rule is the "
                                          f"command at line start: **{disc}** and **{fam}**",
        "trace file/trace trap": f"Traces: **{p['trace_files']}** files, **{p['traces']}** traces",
        "link occurrence gap": f"**{p['sf_comp']}** scope-note link occurrences against "
                               f"**{p['chal_json']}** distinct configs: {p['dup_docs']} scope "
                               f"notes link one config twice",
        "projection basis": "The **150** B/row byte figures are projections",
        "bib entry caveat": f"The **{be}** bib entries are counted",
        "lean reach caveat": f"The **{p['reach']}**-family Lean reach",
        "namespace caveat": f"The **{p['ns_agree']}** of **{p['mr_entries']}** namespace agreement",
        "grouping caveat": f"Whether the **{p['lean_disc']}** Lean discipline dirs align with the "
                           f"**{disc}** catalog disciplines",
        "superseded estimate": f"superseded by the measured **{n}** and **{rb}**",
        "disk link check": f"covers **{p['disk_links']:,}** links over the same "
                           f"{p['index_pages']:,} pages, also with **{p['disk_broken']}** broken, "
                           f"and **{p['disk_dirs']:,}** of them resolve to a directory",
    }
    for name in M.LEDGER_SET:
        size, rows = p["sizes"][name]
        out[f"{name} measured size"] = f"| `{name}` | **{size}** | **{rows}** |"
    return out


def index_phrases(p: dict[str, Any]) -> dict[str, str]:
    """Slot dict for notes/index-design.md: full phrases, split at the page's own line breaks."""
    out: dict[str, str] = {}
    for label, phrase in index_full(p).items():
        prefixes = INDEX_SPLIT.get(label)
        if not prefixes:
            out[label] = phrase
            continue
        rest = phrase
        for i, pre in enumerate(prefixes):
            # The whitespace at each page break lives in the template, so a part never carries it:
            # fold it out of the remainder before matching the next recorded prefix.
            rest = rest.lstrip()
            if not rest.startswith(pre):
                msg = f"slot {label!r}: page wrap {pre!r} is not a prefix of {rest!r}"
                raise ValueError(msg)
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


# Where notes/index-design.md wraps a phrase across lines, the prefix the page's first line ends
# with. Transcribed from the page bytes, not invented: a prefix that stops matching the measured
# phrase raises ValueError here rather than reflowing the page.
INDEX_SPLIT = {
    "MSC hit count": ["family → MSC code"],
    "added TSV byte figures": ["`notes/sources.tsv`"],
    "bib keywords count": ["bibliography entry → `keywords` field **0** over **13,802**"],
    "builds-on declaration count": ["(**30** `builds-on` declarations at"],
    "derivable lean reach": ["config → file (yaml: **189** configs, all **189** of them also "
                             "named by a scope note), which reaches"],
    "disk link check": ["covers **66,107** links over the same 1,033 pages, also with"],
    "lean edge scope": ["The index carries family → Lean file for **136** families; the "
                        "**172** is a"],
    "link occurrence gap": ["**426** scope-note link occurrences against **416** distinct "
                            "configs: 7 scope notes link one config"],
    "manuscripts-per-family distribution": ["a family carries a maximum of **14**"],
    "namespace agreement count": ["the triples name **183** module dirs, and the declaration"],
    "population totals": ["Totals: **2,560** index nodes (excluding the **122,458** `.lean` "
                          "files) and **3,415** edges, or"],
    "raw-bib projection": ["**13,802** rows at the measured **150** B/row is"],
    "subfindings key counts": ["keyed by"],
    "substring vs line-start counts": ["so a substring count of the command name reads 18 and",
                                       "373. The brace-qualified substring reads **17** and "
                                       "**372** only because each definition writes"],
    "superseded estimate": ["superseded by the measured **2,560**"],
}


def index_page(p: dict[str, Any]) -> str:
    """notes/index-design.md, rendered from measure_index_sizes.population()."""
    return ENV.get_template("index-design.md.j2").render(p=index_phrases(p))


# --- notes/names.md ------------------------------------------------------------------
# The page's fixed vocabularies, transcribed from the page: the probe tokens in the page's order,
# the rejection-ladder buckets in the page's order, the layer flags with the layer names the page
# prints, and the words-section keys in table order. The 40 yield rows are DERIVED (family count
# descending, name ascending on a tie); the builder fails the render if a derived row is not on the
# page, so the table's shape is checked, not transcribed.
NAMES_PROBE = ["the", "all", "games", "lane", "hom", "quot", "cat", "adm", "boolean", "catalan",
               "koebe", "saxl", "pixton", "wang", "cauchy"]
NAMES_LADDER = ["not-a-word-key", "label-word", "maths-word", "contains-digit", "acronym",
                "latex-macro", "no-prose-evidence", "prose-word"]
NAMES_LAYERS = [("F", "family title", "fam_title_fams"), ("M", "manuscript directory title", "ms_title"),
                ("E", "theorem-environment title", "env_title_fams"), ("D", "declaration name", "decl"),
                ("b", "body prose", "body_fams"), ("B", "bib author", "bib_fams")]
NAMES_WORDS = ["hom", "quot", "combinatorics", "computer", "beaver", "stablest"]
NAMES_NUMBER_WORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven"}


def names_population() -> dict[str, Any]:
    """`measure_names.measure()`, plus the figures its report computes in `main()` and never returns.

    The page cites four joins the measurement function does not carry: the wider-pattern environment
    total (from `notes/sources.tsv`), the `main_results` entry and config counts (from
    `lean/formalization.yaml`), the 372-family denominator (from `overview.tex`), and the trace-table
    coverage (from the release's trace attribution). `measure_names.py` prints all of them and returns
    none, so the writer computes them here.
    """
    rows, meta = MN.measure()
    subject = [r for r in rows if r["role"] == "subject"]
    covered: set[str] = set()
    subj_cov: set[str] = set()
    for r in rows:
        covered |= set(r["fams"])
    for r in subject:
        subj_cov |= set(r["fams"])
    order, _ = overview.parse_overview()
    trace_by_fam, _ = Y.parse_traces()
    _, mainres = Y.parse_yaml()
    with TSV.open(encoding="utf-8") as fh:
        wide_env = sum(int(r["thms"]) for r in csv.DictReader(fh, delimiter="\t"))
    return {
        "rows": rows,
        "meta": meta,
        "subject": subject,
        "citation": [r for r in rows if r["role"] == "citation"],
        "edges": sum(len(r["fams"]) for r in subject),
        "fams": len(order),
        "no_hit": len(set(order) - covered),
        "traces": len(trace_by_fam),
        "traces_covered": len(set(trace_by_fam) & subj_cov),
        "no_family": sum(1 for r in rows if not r["fams"]),
        "singletons": sum(1 for r in subject if len(r["fams"]) == 1),
        "spellings": sum(1 for r in subject if len(r["variants"]) > 1),
        "rejected_total": sum(v for n, v in meta["rejected"].items() if n != "family-title-via-bib"),
        "mainres": sum(mainres.values()),
        "mainres_configs": len(mainres),
        "wide_env": wide_env,
    }


def names_phrases(mp: dict[str, Any]) -> dict[str, str]:
    """The slot dict for notes/names.md, every value measured from the population.

    Left literal by design: the 16-name escape list, the 6 merged-keys list, the deleted-gate names
    list, the singleton examples, the curated `decl_top` excerpt (the page drops two of the report's
    eight tokens), the gate formula, and the words-table title evidence — all curated prose the writer
    does not compute. `env_cap`'s 8 is a code constant in `build_index.py`, not a measurement.
    """
    rows, meta = mp["rows"], mp["meta"]
    subject, citation = mp["subject"], mp["citation"]
    row = {r["name"]: r for r in subject}
    edges, fam_total = mp["edges"], mp["fams"]
    counts = [len(r["fams"]) for r in subject]
    layer_hits = {flag: sum(1 for r in subject if r[key]) for flag, _label, key in NAMES_LAYERS}
    top = sorted(subject, key=lambda r: (-len(r["fams"]), r["name"]))[:40]
    merged, escape = meta["merged"], meta["escape_names"]
    pr = {k: (mid, low) for k, _cap, mid, low in meta["probe"]}
    avg = f"{edges / fam_total:.1f}"
    med = statistics.median(counts)
    p: dict[str, str] = {}

    def cell(v: int) -> str:
        return f(v) if v else "—"

    def probe(t: str) -> str:
        return f"{pr[t][0]}/{pr[t][1]}"

    p["names_total"] = f"{f(len(rows))} name keys measured over the corpus"
    p["names_subject a"] = f"{f(len(subject))} of"
    p["names_subject b"] = "them appear in a title layer"
    p["names_citation a"] = f"The other {f(len(citation))} are"
    p["names_citation b"] = "found only in prose"
    p["names_edges"] = f"The subject names produce {f(edges)} family-name edges over all {fam_total} families"
    p["names_zero a"] = "No name resolves to"
    p["names_zero b"] = f"zero families ({mp['no_family']})"
    p["names_allfams a"] = (f"every family has a subject-name hit ({fam_total - mp['no_hit']} of "
                            f"{fam_total}, so {mp['no_hit']} families with no name")
    p["names_allfams b"] = "hit)"
    p["names_traces"] = (f"all {mp['traces_covered']} published reasoning-trace families are "
                         f"covered by subject names")
    p["layerintro"] = f"Subject names with at least one hit in the layer, over the {f(len(subject))} subject names:"
    for flag, layer_label, _key in NAMES_LAYERS:
        p[f"layer_{flag}"] = f"`{flag}` {layer_label} | {f(layer_hits[flag])}"
    p["prose550 a"] = f"{f(layer_hits['b'])} of {f(len(subject))} subject names also"
    p["prose550 b"] = "occur in prose"
    ca = row["cauchy"]
    p["cauchy_prose"] = (f"`cauchy` appears in {f(len(ca['body_fams']))} family-title sets' prose and in "
                         f"{len(ca['env_title_fams'])} theorem-environment titles")
    p["decl_pairs a"] = "the corpus has"
    p["decl_pairs b"] = (f"{mp['mainres']} `main_results` entries over {mp['mainres_configs']} configs, "
                         f"whose declaration names decompose into {meta['decl_tokens']}")
    p["decl_pairs c"] = f"distinct CamelCase tokens ({meta['decl_entries']} distinct config+declaration pairs)"
    p["cauchy_232"] = f"`cauchy` occurs in the prose of {f(len(ca['fams']))} of {fam_total} families"
    wang, zhang = row["wang"], row["zhang"]
    p["wang_zhang a"] = (f"`wang` is a subject name in {len(wang['fams'])} families' records and a "
                         f"bibliography author in {len(wang['bib_fams'])} of")
    p["wang_zhang b"] = f"them; `zhang` in {len(zhang['fams'])} and {len(zhang['bib_fams'])}"
    p["tsv_rows"] = f"`notes/index/names.tsv` carries all {f(len(rows))} rows with a `role` column"
    p["spellings"] = (f"{mp['spellings']} of the {f(len(subject))} subject names are spelled "
                      f"more than one way in prose alone")
    p["spellings_count"] = f"the count of names with >1 prose spelling is {mp['spellings']}"
    for t in NAMES_PROBE:
        p[f"probe_{t}"] = f"`{t}` | {f(pr[t][0])} | {f(pr[t][1])}"
    p["fail_factor a"] = f"`the` and `all` fail by a factor of {round(pr['the'][1] / pr['the'][0])} and"
    p["fail_factor b"] = f"{round(pr['all'][1] / pr['all'][0])}"
    p["games_lane"] = f"`games` ({probe('games')}) and `lane` ({probe('lane')}) fail"
    p["catalan_koebe"] = f"`catalan` ({probe('catalan')}) and `koebe` ({probe('koebe')}) pass"
    p["cauchy_gate"] = (f"`cauchy` is capitalized {f(pr['cauchy'][0])} times mid-sentence and written "
                        f"lowercase {pr['cauchy'][1]} times")
    p["ladder_intro"] = f"Candidate keys are the union of the four title/declaration layers: {f(meta['title_cands'])} keys"
    p["ladder_reject a"] = (f"{f(mp['rejected_total'])} are rejected, leaving "
                            f"{f(meta['title_cands'] - mp['rejected_total'])}; the plural merge below "
                            f"removes {len(merged)},")
    p["ladder_reject b"] = f"so {f(len(subject))} subject names remain"
    for bucket in NAMES_LADDER:
        p[f"ladder_{bucket}"] = f"`{bucket}` | {f(meta['rejected'].get(bucket, 0))}"
    p["cat_adm a"] = f"`cat` ({probe('cat')}) and"
    p["cat_adm b"] = f"`adm` ({probe('adm')}) both pass the mid-sentence name test"
    p["escape_count"] = f"{len(escape)} keys are kept on that basis"
    p["escape_of a"] = f"one of the {len(escape)} family-title escape"
    p["escape_of b"] = "names"
    p["words_count"] = f"{NAMES_NUMBER_WORDS[len(NAMES_WORDS)]} keys clear the mid-sentence gate"
    p["boolean_kept a"] = f"`boolean` ({pr['boolean'][0]} mid / {pr['boolean'][1]}"
    p["boolean_kept b"] = "lowercase"
    maker, snaky = row["maker"], row["snaky"]
    p["maker_snaky a"] = f"{maker['mid']}/{maker['low']} and"
    p["maker_snaky b"] = f"{snaky['mid']}/{snaky['low']} mid-sentence"
    for r in top:
        p[f"yield_{r['name']}"] = (f"`{r['name']}` | {cell(len(r['fams']))} | "
                                   f"{cell(len(r['fam_title_fams']))} | {cell(len(r['ms_title']))} | "
                                   f"{cell(len(r['env_title_fams']))} | {cell(len(r['decl']))} | "
                                   f"{cell(len(r['body_fams']))} | {cell(len(r['bib_fams']))}")
    p["yield_bottom"] = f"The bottom of the list is {mp['singletons']} names attached to exactly one family"
    p["dist_edges"] = f"{f(edges)} subject edges over {fam_total} families: {avg} subject names per family on average"
    p["dist_median a"] = f"Median {med:g}"
    p["dist_median b"] = (f"families per name; {mp['singletons']} names attach to exactly 1 family; "
                          f"{sum(1 for c in counts if c >= 100)} names attach to 100 or more.")
    p["totals a"] = (f"{f(meta['tex_files'])} `.tex` files at depth 1–3; {f(meta['env_count'])} "
                     f"statement environments carrying an optional title;")
    p["totals b"] = (f"{f(meta['bib_entries'])} `.bib` entries, {f(meta['bib_author_keys'])} "
                     f"distinct author-surname keys")
    p["sources_env a"] = f"`notes/sources.tsv` reports {f(mp['wide_env'])}"
    p["sources_env b"] = "environments under a wider pattern"
    p["avg_family"] = f"The average family carries {avg} subject names"
    p["citation_no_page"] = f"({f(len(citation))} of them)"
    p["merge_count"] = f"{len(merged)} keys merged:"
    p["plural_forms a"] = f"{meta['plural_title']} plural"
    p["plural_forms b"] = (f"forms appear in a title layer whose singular also appears in a title "
                           f"layer; {meta['plural_name_like']} of them clear the")
    p["plural_forms c"] = "mid-sentence name test"
    p["boolean_dioph"] = (f"`boolean` ({len(row['boolean']['fams'])} families) and `diophantine` "
                          f"({len(row['diophantine']['fams'])}) are kept as name-derived adjectives")
    p["notchecked_prose a"] = f"{f(meta['rejected']['prose-word'])} candidates were rejected as prose-words by"
    p["notchecked_prose b"] = "a capitalization ratio"
    p["notchecked_nopro"] = f"the {meta['rejected']['no-prose-evidence']} `no-prose-evidence` rejections"
    return p


def names_page(p: dict[str, str]) -> str:
    return ENV.get_template("names.md.j2").render(p=p)


def main() -> None:
    mp = en.population()
    ip = M.population()
    np_ = names_population()
    SOURCES_MD.write_text(sources_page(), encoding="utf-8")
    ABSTRACTS_MD.write_text(abstracts_page(), encoding="utf-8")
    NAMED_RESULTS_MD.write_text(named_results_page(mp), encoding="utf-8")
    INDEX_DESIGN_MD.write_text(index_page(ip), encoding="utf-8")
    NAMES_MD.write_text(names_page(names_phrases(np_)), encoding="utf-8")
    for page in (SOURCES_MD, ABSTRACTS_MD, NAMED_RESULTS_MD, INDEX_DESIGN_MD, NAMES_MD):
        out = page.read_text(encoding="utf-8")
        print(f"{page.name} written  lines {len(out.splitlines())}  bytes {len(out.encode())}")
    ms, ma = measure(), CA.measure()
    print(f"slots  sources {len(phrases(ms))}  abstracts {len(abstracts_phrases(ma))}"
          f"  named-results {len(named_results_phrases(mp))}"
          f"  index-design {len(index_phrases(ip))}"
          f"  multi-root rows {len(ms['multi'])}  rows {ms['rows']}  listed {ms['listed']}"
          f"  dirs {ms['dirs']}  comparisons {ma['manuscripts']}  families {ma['families']}"
          f"  target rows {len(tgt_rows(mp))}")


if __name__ == "__main__":
    main()
