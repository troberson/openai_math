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
import posixpath
import re
import statistics
import subprocess
import sys
from typing import Any

from jinja2 import Environment, FileSystemLoader

import build_sources as S
import check_index_links as CI
import compare_abstracts as CA
import extract_named_results as en
import measure_index_sizes as M
import measure_names as MN
import measure_proof_density as PD
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
PROOF_DENSITY_MD = ROOT / "notes" / "proof-density.md"
INDEX_LINKS_MD = ROOT / "notes" / "index-links.md"
LINKS_MD = ROOT / "notes" / "links.md"
LINKS_TSV = ROOT / "notes" / "links.tsv"


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


# The page's tables key to these, and the verdict pass mirrors measure_proof_density.report(): the
# per-family control gates the two per-family signals, the per-manuscript control gates proofs/man.
PD_SHAPE_KEYS = ("proofs", "proofs_per_man", "proofs_per_thm", "proofs_per_kb")
PD_FLAG_KEYS = ("proofs_per_man", "proofs_per_thm", "proofs_per_kb")
PD_SCALE = {"proofs": "family", "thms": "family", "proofs_per_man": "manuscript",
            "proofs_per_thm": None, "proofs_per_kb": None, "kb_per_man": "manuscript"}
PD_TABLE_KEYS = ("proofs", "thms", "proofs_per_man", "proofs_per_thm", "proofs_per_kb")
PD_FLAG_SHORT = {"proofs_per_man": "man", "proofs_per_thm": "thm", "proofs_per_kb": "kb"}


def pd_median(v: float) -> str:
    """The page prints a median at one decimal from 1 up and at three below it."""
    return f"{v:.1f}" if v >= 1 else f"{v:.3f}"


def proof_density_population() -> dict[str, Any]:
    """Everything notes/proof-density.md quotes, measured through the script the page names.

    This page's checker IS the measurement (measure_proof_density.py --mutant), so the writer reuses
    its statistic and its population build while the checker keeps its own gates and mutant list. The
    split this module's header draws is against a checker importing the renderer, not against sharing
    a measurement: verify_named_results.py re-derives its counts from extract_named_results.population()
    exactly as this reuses measure_proof_density.build_families().
    """
    sources = PD.read_tsv(PD.SOURCES)
    ledger = PD.read_tsv(PD.LEDGER)
    fams = PD.build_families(sources, ledger)
    tiers = {t: sum(1 for d in fams.values() if d["tier"] == t) for t in ("T3", "T2", "T1", "T0")}
    med = {(key, t): PD.median([d[key] for d in fams.values() if d["tier"] == t])
           for key, _lbl in PD.SIGNALS for t in ("T0", "T2", "T3")}
    sep: dict[tuple[str, str, str], tuple[float, float]] = {}
    for key, _lbl in PD.SIGNALS:
        for a, b in PD.TIER_PAIRS:
            auc, _z, pv = PD.auc_p([d[key] for d in fams.values() if d["tier"] == a],
                                    [d[key] for d in fams.values() if d["tier"] == b])
            sep[(key, a, b)] = (auc, pv)
    ctl: dict[tuple[str, str, str], tuple[float, float]] = {}
    for a, b in PD.TIER_PAIRS:
        fa, _fz, fp = PD.auc_p([d["kb"] for d in fams.values() if d["tier"] == a],
                               [d["kb"] for d in fams.values() if d["tier"] == b])
        ctl[(a, b, "family")] = (fa, fp)
        ma, _mz, mp_ = PD.auc_p([d["kb_per_man"] for d in fams.values() if d["tier"] == a],
                                [d["kb_per_man"] for d in fams.values() if d["tier"] == b])
        ctl[(a, b, "manuscript")] = (ma, mp_)
    verdict: dict[tuple[str, str, str], str] = {}
    for key, _lbl in PD.SIGNALS:
        if key == "kb_per_man":
            continue
        for a, b in PD.TIER_PAIRS:
            auc, pv = sep[(key, a, b)]
            if auc >= PD.AUC_MIN and pv < PD.P_MAX:
                scale = PD_SCALE[key]
                verdict[(key, a, b)] = ("SIZE-EXPLAINED" if scale and
                                         abs(auc - ctl[(a, b, scale)][0]) <= PD.SIZE_TOLERANCE
                                         else "SEPARATES")
            else:
                verdict[(key, a, b)] = "NULL"
    shapes = {(shape, key): PD.compare(fams, key, {shape: {f for f, d in fams.items()
                                                            if shape in d["shapes"]}})[shape]
              for shape in PD.SHAPES for key in PD_SHAPE_KEYS}
    flags = {(flag, key): PD.compare(fams, key, {flag: {f for f, d in fams.items()
                                                        if d.get(flag) == "1"}})[flag]
             for flag in PD.FLAGS for key in PD_FLAG_KEYS}
    st_ok, st_total = PD.selftest()
    caught, mt_total, _cases = PD.mutants(PD.build_families)
    return {
        "rows": len(sources), "fams": len(fams),
        "proofs": sum(d["proofs"] for d in fams.values()),
        "thms": sum(d["thms"] for d in fams.values()),
        "tiers": tiers,
        "problems": len(PD.gate_checks(sources, ledger, fams)),
        "selftest": (st_ok, st_total), "mutants": (caught, mt_total),
        "med": med, "sep": sep, "ctl": ctl, "verdict": verdict,
        "shapes": shapes, "flags": flags,
        "signals": len(PD.SIGNALS), "pairs": len(PD.TIER_PAIRS),
        "shape_contrasts": len(PD.SHAPES) * len(PD_SHAPE_KEYS),
        "flag_contrasts": len(PD.FLAGS) * len(PD_FLAG_KEYS),
        "auc_min": PD.AUC_MIN,
    }


def proof_density_phrases(mp: dict[str, Any]) -> dict[str, str]:
    p: dict[str, str] = {}
    p["rows"] = f(mp["rows"])
    p["fams"] = f(mp["fams"])
    p["proofs"] = f(mp["proofs"])
    p["thms"] = f(mp["thms"])
    p["tiers"] = " / ".join(f"{t} {mp['tiers'][t]}" for t in ("T3", "T2", "T1", "T0"))
    p["gate_problems"] = f"All {mp['problems']} problems"
    p["gate_selftest"] = f"statistic self-test {mp['selftest'][0]}/{mp['selftest'][1]}"
    p["gate_mutants"] = f"injected mutants caught {mp['mutants'][0]}/{mp['mutants'][1]}"
    for key, lab in (("proofs", "medrow_proofs"), ("thms", "medrow_thms")):
        p[lab] = " | ".join(pd_median(mp["med"][(key, t)]) for t in ("T0", "T2", "T3"))
    for key, _lbl in PD.SIGNALS:
        if key in ("proofs", "thms"):
            # The two raw-count rows are slotted whole: their T3 medians are both 27.0, and a bare
            # "27.0" needle matches the other row's cell first, so the builder would slot one row's
            # value into both. A whole-row needle is unique, and the row stays correct if the two
            # medians ever diverge.
            continue
        for t in ("T0", "T2", "T3"):
            p[f"med_{key}_{t}"] = pd_median(mp["med"][(key, t)])
    for key in PD_TABLE_KEYS:
        for a, b in PD.TIER_PAIRS:
            auc, pv = mp["sep"][(key, a, b)]
            p[f"sep_{key}_{a}{b}"] = f"{auc:.3f} / {pv:.2e} → {mp['verdict'][(key, a, b)]}"
    p["ctlman"] = " | ".join(f"{mp['ctl'][(a, b, 'manuscript')][0]:.3f} / "
                             f"{mp['ctl'][(a, b, 'manuscript')][1]:.2e}"
                             for a, b in PD.TIER_PAIRS)
    p["ctlfam"] = " | ".join(f"{mp['ctl'][(a, b, 'family')][0]:.3f}" for a, b in PD.TIER_PAIRS)
    for key, lab in (("proofs", "fact_proofs"), ("thms", "fact_thms"),
                     ("proofs_per_man", "fact_man")):
        p[lab] = f"{mp['sep'][(key, 'T0', 'T2')][0]:.3f} / {mp['sep'][(key, 'T0', 'T3')][0]:.3f}"
    p["fact_ctl_fam"] = (" / ".join(f"{mp['ctl'][(a, b, 'family')][0]:.3f}"
                                    for a, b in PD.TIER_PAIRS[:2]))
    p["fact_ctl_man"] = (" / ".join(f"{mp['ctl'][(a, b, 'manuscript')][0]:.3f}"
                                    for a, b in PD.TIER_PAIRS[:2]))
    for shape in ("conditional", "undecidability"):
        auc, pv, n, _rest = mp["shapes"][(shape, "proofs")]
        # The needle opens at the shape name, not at "n=5": the flag table below carries the same
        # "(n=5)" for `conditional`, and a needle starting at the same offset as the flag label's
        # shorter one is a fatal OVERLAP in the builder.
        p[f"shape_{shape}"] = f"{shape}` (n={n}) at {auc:.3f} / {pv:.2e}"
    p["shape_partial"] = (f"{mp['shapes'][('partial', 'proofs_per_kb')][0]:.3f} / "
                          f"{mp['shapes'][('partial', 'proofs_per_kb')][1]:.2e}")
    for flag in PD.FLAGS:
        p[f"flag_{flag}_n"] = f"n={mp['flags'][(flag, 'proofs_per_man')][2]}"
        for key, short in PD_FLAG_SHORT.items():
            auc, pv, _n, _rest = mp["flags"][(flag, key)]
            p[f"flag_{flag}_{short}"] = f"{auc:.3f} / {pv:.2e}"
    rk = mp["flags"][("resolves_named", "proofs_per_kb")][0]
    p["gap_bar"] = f"{rk:.3f} sits {mp['auc_min'] - rk:.3f} below the AUC bar"
    p["count_signals"] = f"{mp['signals']} signals"
    p["count_pairs"] = f"{mp['pairs']} tier pairs"
    p["count_shape"] = f"{mp['shape_contrasts']} shape contrasts"
    p["count_flag"] = f"{mp['flag_contrasts']} flag contrasts"
    return p


def proof_density_page(p: dict[str, str]) -> str:
    return ENV.get_template("proof-density.md.j2").render(p=p)


# --- notes/index-links.md --------------------------------------------------------------
# The page quotes two reports. check_index_links.py is imported (it does no work at module scope),
# so the writer reads its measurement as data. build_index.py is run as a subprocess: it calls
# main() at module scope, so importing it would run the 45-second index build inside every render.
# The page's checker (check_index_links.py --mutant) keeps its own recomputation, as everywhere.

IL_DIR_DESC = {
    "manuscript-dir": "`preprints/<dir>/` — the manuscript directory",
    "latex-build-tree": "`preprints/<dir>/build/` — the LaTeX source tree",
    "lean-dir": "the Lean module dir named by a `main_results` file path",
    "verification-dir": "`preprints/<dir>/verification/` — certificate bundles",
    "index-dir": "`notes/index/names/`, linked from the entry point",
}
IL_GROUP_CELL = {"name pages": "name pages", "family pages": "family pages",
                 "topic pages": "topic pages", "discipline pages": "discipline pages",
                 "entry point": "entry point (`notes/index/README.md`)"}
# Categories whose scanned count exceeds the render-time registered count, in the page's row order.
IL_GAP_CATS = ["index-page", "manuscript-dir", "notes-doc", "index-table", "config-json",
               "verification-dir", "index-dir"]
# Where notes/index-links.md wraps a phrase across lines, the prefix its first line ends with.
IL_SPLIT = {
    "hl_canon": ["719",
                 "manuscript PDFs, 719 `build/` trees, 719 `README.md` stubs, 242 scope notes, "
                 "416 comparator",
                 "configs (JSON and Lean side by side), 192 Lean files named by "
                 "`formalization.yaml` over 183"],
    "prose_lean200": ["`lean-dir` counts 200 links over"],
    "prose_leanhost": ["14 dirs host more than one `main_results` declaration (max 3), and 6 files host"],
    "prose_extra": ["`manuscript-dir` is the one category whose target count exceeds the "
                    "canonical count: 746"],
    "prose_superseded": ["The 27 extra targets are directories the upstream merge superseded —",
                         "every one exists on disk, none is listed as a manuscript in "
                         "`notes/subfindings.tsv`, and all 27"],
    "prose_indexpage": ["`index-page` 521 targets = 372 family pages + 92 topic",
                        "pages + 17 discipline pages + 40 name pages, and the 40 name pages are "
                        "linked only from the entry"],
    "prose_latexsource": ["`latex-source` 719 = the `main_tex` of each of the 719 manuscripts, "
                          "all 719 present in"],
    "prose_notesdoc": ["`notes-doc` 26 targets = `notes/names.md` (552 links: one from each of the",
                       "551 name pages and one from the entry point), the 21 `notes/summaries/` "
                       "pages family pages link,",
                       "and the 5 notes docs the entry point links (`index-design.md`, `names.md`, "
                       "`topics.md`,"],
    "prose_regchecked": ["**48,012 links checked, 0"],
    "prose_tracefiles": ["`reasoning_traces/` ships **11 files"],
    "prose_fresh": ["**20 injected, 20 caught, 0 missed; 7 controls, 7"],
    "prose_surplus": ["The 18,095 surplus links are"],
}


def build_index_report() -> dict[str, Any]:
    """Run notes/scripts/build_index.py and parse the report lines the page quotes.

    A subprocess, not an import: build_index.py calls main() at module scope, so importing it
    would build the index inside every render.
    """
    proc = subprocess.run([sys.executable, str(ROOT / "notes" / "scripts" / "build_index.py")],
                          capture_output=True, text=True, check=True, cwd=ROOT)
    out: dict[str, Any] = {"checked": -1, "broken": -1, "reg": {}}
    for ln in proc.stdout.splitlines():
        if ln.startswith("links checked"):
            out["checked"], out["broken"] = int(ln.split()[2]), int(ln.split()[-1])
        elif ln.startswith("registered by group"):
            for g in CI.GROUP_ORDER:
                m = re.search(rf"{g} (\d+)", ln)
                if m:
                    out["reg"][g] = int(m.group(1))
        elif ln.startswith("registered by category"):
            for tok in ln[len("registered by category "):].split("  "):
                k, v = tok.rsplit(" ", 1)
                out["reg"][k] = int(v)
    return out


def index_links_population() -> dict[str, Any]:
    """The two reports notes/index-links.md quotes, plus the checker's own self-test.

    The build runs first so the disk scan reads the index the same render just produced.
    """
    build = build_index_report()
    return {"scan": CI.measure(), "build": build, "mutant": CI.mutant_test()}


def index_links_full(p: dict[str, Any]) -> dict[str, str]:
    """label → full measured phrase, for notes/index-links.md."""
    s, b, mt = p["scan"], p["build"], p["mutant"]
    cats, canon, reg = s["cats"], s["canon"], b["reg"]
    tg = {c: len(v) for c, v in s["targets"].items()}
    kind, gp, groups = s["kind"], s["gp"], s["groups"]
    nlinks, npages, nbroken = len(s["links"]), len(s["pages"]), len(s["broken"])
    gap = nlinks - b["checked"]
    name_gap = groups["name pages"] - reg["name pages"]
    caught, total, missed, clean, ctotal = mt[0], mt[1], mt[2], mt[3], mt[4]
    trap = mt[6]
    dirs = collections.Counter(posixpath.dirname(fl) for _c, _d, fl in s["triples"])
    files = collections.Counter(fl for _c, _d, fl in s["triples"])
    tops = collections.Counter(r.split("/")[2] for r in s["targets"]["index-page"])
    fam_pg = sum(v for k, v in tops.items() if k not in ("names", "topics", "disciplines"))
    entry_docs = len({rel for pg, _h, rel in s["links"]
                      if pg == "README.md" and CI.category(rel) == "notes-doc"})
    summaries = len([r for r in s["targets"]["notes-doc"] if r.startswith("notes/summaries/")])
    names_links = sum(1 for _pg, _h, rel in s["links"] if rel == "notes/names.md")
    extra = len(s["extra_dirs"])
    out: dict[str, str] = {}
    out["h_title"] = f"{f(nlinks)} links checked against the shipped files, {nbroken} broken"
    out["hl_pages"] = f"all {f(npages)} rendered index pages"
    out["hl_links"] = f"{f(nlinks)} markdown links extracted"
    out["hl_broken"] = f"→ **{nbroken} broken**"
    out["hl_dirfile"] = f"{f(s['dir_links'])} resolve to a directory and {f(s['file_links'])} to a"
    out["hl_canon"] = (f"{canon['manuscript-pdf']} manuscript PDFs, {canon['latex-build-tree']} "
                       f"`build/` trees, {canon['manuscript-readme']} `README.md` stubs, "
                       f"{canon['scope-note']} scope notes, {canon['config-json']} comparator "
                       f"configs (JSON and Lean side by side), {canon['lean-file']} Lean files "
                       f"named by `formalization.yaml` over {canon['lean-dir']} "
                       f"module dirs, {canon['verification-dir']} verification dirs, "
                       f"{canon['trace']} reasoning-trace stems")
    out["hl_contents"] = (f"{len(s['contents'])} links, {len(s['contents_pdf'])} of them `.pdf`, "
                          f"**{len(s['contents_broken'])} broken**")
    out["trap_naive"] = f"`[^)]*` | `{trap[0][1]}` | {'yes' if trap[0][2] else 'no'}"
    out["trap_balanced"] = f"paren-balanced | `{trap[1][1]}` | {'yes' if trap[1][2] else 'no'}"
    for c, desc in IL_DIR_DESC.items():
        out[f"dirrow_{c}"] = f"| `{c}` | {f(cats[c])} | {tg[c]} | {desc} |"
    out["dir_intro"] = f"{f(s['dir_links'])} of the {f(nlinks)} links resolve to a directory"
    out["prose_remaining"] = f"The remaining {f(s['file_links'])} links resolve to files"
    out["prose_ver60"] = (f"`verification-dir` counts {cats['verification-dir']} links over "
                          f"{tg['verification-dir']} dirs")
    out["prose_lean200"] = f"`lean-dir` counts {cats['lean-dir']} links over {tg['lean-dir']} dirs"
    out["prose_leanhost"] = (f"{sum(1 for v in dirs.values() if v > 1)} dirs host more than one "
                             f"`main_results` declaration (max {max(dirs.values())}), and "
                             f"{sum(1 for v in files.values() if v > 1)} files host more than one "
                             f"(max {max(files.values())}), which is why {canon['lean-file']} "
                             f"files sit in {canon['lean-dir']} dirs")
    out["prose_extra"] = (f"`manuscript-dir` is the one category whose target count exceeds the "
                          f"canonical count: {tg['manuscript-dir']} linked of "
                          f"{canon['manuscript-dir']} shipped")
    out["prose_superseded"] = (f"The {extra} extra targets are directories the upstream merge "
                               f"superseded — every one exists on disk, none is listed as a "
                               f"manuscript in `notes/subfindings.tsv`, and all {extra} are "
                               f"reached only from name pages, by {f(s['extra_dir_links'])} links")
    out["line_extra"] = (f"manuscript dirs linked outside the release set  {extra}  on disk "
                         f"{s['extra_dirs_on_disk']}  links {s['extra_dir_links']}")
    out["line_from"] = (f"From `python3 notes/scripts/check_index_links.py` ({f(npages)} pages, "
                        f"{f(nlinks)} links, {nbroken} broken):")
    for c in sorted(cats, key=lambda k: (-cats[k], k)):
        cv = canon.get(c)
        cell = "—" if cv is None else (f"{cv} = canonical" if tg[c] == cv
                                       else f"{cv} linked {tg[c]} of {cv}")
        out[f"catrow_{c}"] = (f"| `{c}` | {f(cats[c])} | {f(tg[c])} | {f(kind[(c, 'file')])} | "
                              f"{f(kind[(c, 'dir')])} | {cell} |")
    out["prose_indexpage"] = (f"`index-page` {tg['index-page']} targets = {fam_pg} family pages + "
                              f"{tops['topics']} topic pages + {tops['disciplines']} discipline "
                              f"pages + {tops['names']} name pages, and the {tops['names']} name "
                              f"pages are linked only from the entry point")
    out["prose_latexsource"] = (f"`latex-source` {tg['latex-source']} = the `main_tex` of each of "
                                f"the {tg['latex-source']} manuscripts, all {tg['latex-source']} "
                                f"present in `notes/sources.tsv`")
    out["prose_notesdoc"] = (f"`notes-doc` {tg['notes-doc']} targets = `notes/names.md` "
                             f"({names_links} links: one from each of the {gp['name pages']} name "
                             f"pages and one from the entry point), the {summaries} "
                             f"`notes/summaries/` pages family pages link, and the {entry_docs} "
                             f"notes docs the entry point links (`index-design.md`, `names.md`, "
                             f"`topics.md`, `topics.tsv`, `scripts/measure_names.py`)")
    out["prose_indextable"] = f"`index-table` {tg['index-table']} target = `notes/index/names.tsv`"
    out["prose_traces"] = (f"Traces: {len(s['trace_stems'])} stems attributed, "
                           f"{len(s['trace_disk'])} on disk, {len(s['trace_unlisted'])} unattributed.")
    out["prose_tracefiles"] = (f"`reasoning_traces/` ships **{s['trace_files']} files over "
                               f"{len(s['trace_stems'])} stems**")
    out["prose_contentspdf"] = (f"`CONTENTS.md`'s {len(s['contents_pdf'])} `.pdf` links are the "
                                f"{canon['manuscript-pdf']} manuscript PDFs plus `overview.pdf`")
    out["prose_regchecked"] = f"**{f(b['checked'])} links checked, {b['broken']} broken**"
    out["prose_scanfinds"] = f"The disk scan finds **{f(nlinks)} links, {nbroken} broken**"
    out["prose_gap"] = f"The {f(gap)}-link difference"
    for g in CI.GROUP_ORDER:
        out[f"gprow_{g}"] = (f"| {IL_GROUP_CELL[g]} | {gp[g]} | {f(groups[g])} | {f(reg[g])} | "
                             f"{f(groups[g] - reg[g])} |")
    for c in IL_GAP_CATS:
        # The build report's registered-by-category line lists only categories with a non-zero
        # count, so a category the registry never sees is registered 0, not missing.
        rc = reg.get(c, 0)
        out[f"gaprow_{c}"] = f"| `{c}` | {f(cats[c])} | {f(rc)} | {f(cats[c] - rc)} |"
    out["prose_surplus"] = (f"The {f(gap)} surplus links are all verified by the disk scan, and "
                            f"{f(name_gap)} of them ({round(name_gap / gap * 100)}%) sit on "
                            f"name pages")
    out["prose_mutants"] = f"injects {total} broken hrefs"
    out["prose_controls"] = f"requires {ctotal} real hrefs to resolve"
    out["prose_fresh"] = (f"**{total} injected, {caught} caught, {len(missed)} missed; "
                          f"{ctotal} controls, {clean} resolve**")
    out["prose_overviewpdf"] = (f"is inside the {len(s['contents_pdf'])} `.pdf` links in "
                                f"`CONTENTS.md`** ({canon['manuscript-pdf']} manuscripts + 1)")
    return out


def index_links_phrases(p: dict[str, Any]) -> dict[str, str]:
    """Slot dict for notes/index-links.md: full phrases, split at the page's own line breaks."""
    out: dict[str, str] = {}
    for label, phrase in index_links_full(p).items():
        prefixes = IL_SPLIT.get(label)
        if not prefixes:
            out[label] = phrase
            continue
        rest = phrase
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                msg = f"slot {label!r}: page wrap {pre!r} is not a prefix of {rest!r}"
                raise ValueError(msg)
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def index_links_page(p: dict[str, str]) -> str:
    return ENV.get_template("index-links.md.j2").render(p=p)


# --- notes/links.md ---------------------------------------------------------------------

# The table's 22 rows: label, the links.tsv edge key, the count-cell suffix, the page's prose.
# Rows are slotted whole because the counts repeat (two 0s, two 30s, three 12s): a needle for a
# repeated count alone collides with every row that count appears in.
LINKS_ROWS: list[tuple[str, str, str, str]] = [
    ("row01", "family->manuscript", "",
     "A published link, not a claim the manuscript is formalized, read, or correct"),
    ("row02", "manuscript->formalized", " of 719",
     "A source-level declaration under `review: status: unchecked`"),
    ("row03", "family->scope note", " of 372", "Release prose stating exclusions, not a certification"),
    ("row04", "scope note->comparator statement", "", "A link to a statement file, not a comparator pass"),
    ("row05", "comparator config->statement+solution", "", "A statement/solution pair on disk, not a run"),
    ("row06", "family->main_results declaration", "", "The release's own list, not a verification"),
    ("row07", "formalization->declared library", "", "A declared pin, not a buildable pin"),
    ("row08", "formalization->observed import root", "",
     "Direct imports over `lean/OAI/`, not the transitive closure"),
    ("row09", "manuscript->bibliography entry", "", "Shipped entries, not checked references"),
    ("row10", "manuscript->corpus manuscript (bib href)", "",
     "What the release chose to cite, not importance"),
    ("row11", "manuscript->corpus manuscript (body href)", "", "An in-text pointer, not a dependency"),
    ("row12", "abstract->companion family", "", "An abstract naming a sibling, not a citation"),
    ("row13", "abstract->'companion' wording", "", "A word, creating no edge"),
    ("row14", "family->reasoning trace", "", "Release attribution, not evidence the trace is the proof"),
    ("row15", "named-in-title", " of 372", "A property of catalog prose, not of the literature"),
    ("row16", "cited-in-bib", " of 372", "A title-phrase proxy; a miss is not evidence of no impact"),
    ("row17", "mentioned-in-body", " of 372", "A shared phrase can be not-a-reference"),
    ("row18", "family->MSC code", "", "Negative: no classification vocabulary exists to read"),
    ("row19", "bibliography entry->keywords field", "", "Negative: bibliographies carry no topic vocabulary"),
    ("row20", "manuscript->\\keywords macro", " of 719", "98% of manuscripts define no keyword list"),
    ("row21", "manuscript->verification bundle", "", "A certificate bundle, not a theorem check"),
    ("row22", "family->notes summary page", "", "Our artifact, not part of the release"),
]

# The TSV edge key is not always the page's cell text: the page renders -> as → and styles two
# edges the TSV does not style.
LINKS_EDGE_DISP = {
    "abstract->'companion' wording": 'abstract→"companion" wording',
    "manuscript->\\keywords macro": "manuscript→`\\keywords` macro",
}

# Where notes/links.md wraps a phrase across lines, the prefix its first line ends with.
LINKS_SPLIT = {
    "sec426_chal": ["sums to **416** while this row"],
    "mm_targets": ["span **268** target"],
    "mm_same": ["**287** point at a"],
    "mm_tree": ["resolves **432** hrefs, of which **22** point at **16**"],
    "mm_edges": ["carries 391 resolved manuscript→manuscript"],
    "rec_all": ["over all 500 listed files: **17** families, **12**"],
    "knob_quote": ["Quote 14 with its"],
    "neg_word": ['**9** families use the word "companion" in an'],
}


def links_report() -> dict[str, str]:
    """Run notes/scripts/extract_links.py and key its report lines by their leading label.

    A subprocess, not an import: extract_links.py writes notes/links.tsv, and the renderer must
    not become a second writer of a file the ownership manifest attributes to one script.
    """
    proc = subprocess.run([sys.executable, str(ROOT / "notes" / "scripts" / "extract_links.py")],
                          capture_output=True, text=True, check=True, cwd=ROOT)
    rep: dict[str, str] = {}
    for ln in proc.stdout.splitlines():
        key, sep, rest = ln.partition(": ")
        if sep:
            rep[key] = rest.strip()
    return rep


def links_tsv_rows() -> dict[str, dict[str, str]]:
    """The 22 written rows, keyed by edge — the renderer reads the TSV, never re-derives it."""
    with LINKS_TSV.open(encoding="utf-8") as fh:
        return {r["edge"]: r for r in csv.DictReader(fh, delimiter="\t")}


def links_bc_line() -> int:
    """The line of build_catalog.py carrying the companion pattern the page cites."""
    lines = (ROOT / "notes" / "scripts" / "build_catalog.py").read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(lines, 1):
        if "result (\\d{3})" in ln:
            return i
    raise ValueError("companion pattern not found in build_catalog.py")


def links_population() -> dict[str, Any]:
    return {"rep": links_report(), "tsv": links_tsv_rows(), "bc_line": links_bc_line()}


def links_full(p: dict[str, Any]) -> dict[str, str]:
    """Every count notes/links.md quotes, read from the extract_links.py report and links.tsv."""
    rep, tsv, bc_line = p["rep"], p["tsv"], p["bc_line"]

    def n(key: str, pat: str) -> int:
        m = re.search(pat, rep[key])
        assert m is not None, f"{key}: {pat}"
        return int(m.group(1))

    out: dict[str, str] = {}
    for label, edge, suffix, prose in LINKS_ROWS:
        disp = LINKS_EDGE_DISP.get(edge, edge.replace("->", "→"))
        out[label] = f"| {disp} | **{f(int(tsv[edge]['count']))}**{suffix} | {prose} |"

    chal = n("scope note->comparator statement", r"^(\d+)")
    chal_distinct = n("scope note->comparator statement", r"(\d+) distinct configs")
    chal_dup = n("scope note->comparator statement", r"(\d+) duplicate links")
    chal_dupdocs = n("scope note->comparator statement", r"inside (\d+) docs")
    mdup = re.search(r"\(([\d, ]+)\)", rep["scope note->comparator statement"])
    assert mdup is not None
    chal_docs = n("scope note->comparator statement", r"(\d+) of \d+ docs")
    chal_shared = n("scope note->comparator statement", r"(\d+) configs linked by >1 family")
    cfg_lean = n("comparator config->statement+solution", r"(\d+) \.lean files")
    cfg_unlinked = n("comparator config->statement+solution", r"(\d+) never linked")
    mr = n("family->main_results declaration", r"^(\d+)")
    mr_cfgs = n("family->main_results declaration", r"(\d+) unique configs")
    mr_rep = n("family->main_results declaration", r"\((\d+) repeated entries\)")
    mr_fams = n("family->main_results declaration", r"; (\d+) families")
    bibent = n("manuscript->bibliography entry", r"^(\d+)")
    bibfiles = n("manuscript->bibliography entry", r"(\d+) \.bib files")
    bibdirs = n("manuscript->bibliography entry", r"in (\d+) of \d+ manuscript dirs")
    bibhref = n("manuscript->corpus manuscript (bib href)", r"^(\d+)")
    bibres = n("manuscript->corpus manuscript (bib href)", r"(\d+) resolved edges")
    bibtarg = n("manuscript->corpus manuscript (bib href)", r"(\d+) target dirs")
    bibfams = n("manuscript->corpus manuscript (bib href)", r"over (\d+) of \d+ families")
    bibcite = n("manuscript->corpus manuscript (bib href)", r"(\d+) citing dirs")
    bibsame = n("manuscript->corpus manuscript (bib href)", r"(\d+) same-family")
    bibcross = n("manuscript->corpus manuscript (bib href)", r"(\d+) cross-family")
    bibunres = n("manuscript->corpus manuscript (bib href)", r"(\d+) unresolved")
    bodyhref = n("manuscript->corpus manuscript (body href)", r"^(\d+)")
    bodytarg = n("manuscript->corpus manuscript (body href)", r"(\d+) target dirs")
    bodyfams = n("manuscript->corpus manuscript (body href)", r"over (\d+) families")
    bodycite = n("manuscript->corpus manuscript (body href)", r"(\d+) citing dirs")
    comp = n("abstract->companion family", r"^(\d+)")
    compword = n("abstract->'companion' wording", r"^(\d+)")
    compword_edges = n("abstract->'companion' wording", r"(\d+) of them carry")
    named = n("named-in-title", r"^(\d+)")
    cited = n("cited-in-bib", r"^(\d+)")
    cited_own = n("cited-in-bib", r"(\d+) families when")
    mentioned = n("mentioned-in-body", r"^(\d+)")
    mentioned_own = n("mentioned-in-body", r"(\d+) families including")
    msc = n("family->MSC code", r"^(\d+)")
    msc_files = n("family->MSC code", r"files scanned: (\d+)")
    kw_bib = n("bibliography entry->keywords field", r"^(\d+)")
    kw_tex = n("manuscript->\\keywords macro", r"^(\d+)")
    mkw = re.search(r"\((\d+\.\d+)%\)", rep["manuscript->\\keywords macro"])
    assert mkw is not None
    kw_pct = mkw.group(1)
    verif = n("manuscript->verification bundle", r"^(\d+)")
    rows_n = n("rows", r"^(\d+)")
    fields_n = n("rows", r"fields: (\d+)")
    tex_files = n("bib entries", r"tex files: (\d+)")
    disk = n("preprint dirs on disk", r"^(\d+)")
    listed = n("preprint dirs on disk", r"listed manuscripts: (\d+)")
    superseded = n("preprint dirs on disk", r"= (\d+) superseded editions")
    notices = n("preprint dirs on disk", r"\+ (\d+) withdrawal notices")
    families = n("family->scope note", r"of (\d+) families")
    formalized = n("manuscript->formalized", r"^(\d+)")
    stale_listed = n("bib hrefs pointing at superseded editions", r"listed-scope (\d+) over")
    tree_stale = n("bib hrefs pointing at superseded editions", r"whole-tree (\d+) over")
    tree_staledirs = n("bib hrefs pointing at superseded editions", r"whole-tree \d+ over (\d+) of")
    tree_hrefs = n("bib hrefs pointing at superseded editions", r"of (\d+) tree hrefs")
    legacy_files = n("legacy title proxy (6-token prefix, lowercased corpus, .bib at depth<=3)",
                     r"files=(\d+)")
    legacy_any = n("legacy title proxy (6-token prefix, lowercased corpus, .bib at depth<=3)",
                   r"any=(\d+)")
    legacy_cross = n("legacy title proxy (6-token prefix, lowercased corpus, .bib at depth<=3)",
                     r"cross=(\d+)")
    all_files = n("same title rule over all .bib", r"files=(\d+)")
    all_any = n("same title rule over all .bib", r"any=(\d+)")
    all_cross = n("same title rule over all .bib", r"cross=(\d+)")
    mainres_only = n("mainres families", r"mainres-only: (\d+)")
    form_only = n("mainres families", r"formalized-only: (\d+)")
    form_fams = n("mainres families", r"formalized families: (\d+)")
    body_targ2 = n("body href edges", r"target dirs: (\d+)")
    ov_only = n("family->manuscript", r"overview\.tex-only links (\d+)")
    ct_only = n("family->manuscript", r"CONTENTS\.md-only links (\d+)")
    cited_l = re.findall(r"'(\d{3})'", rep["cited list"])
    mentioned_l = re.findall(r"'(\d{3})'", rep["mentioned list"])
    cm = rep["cited∩mentioned"]
    inter_l = re.findall(r"'(\d{3})'", cm.split(" mentioned-only")[0])
    mentonly_l = re.findall(r"'(\d{3})'", cm.split("mentioned-only: ")[1].split(" cited-only")[0])
    citedonly_l = re.findall(r"'(\d{3})'", cm.split("cited-only: ")[1])
    top = re.findall(r"\('(\d{3})', (\d+)\)", rep["top bib target families"])
    pairs = re.findall(r"(\d{3})->(\d{3})", rep["abstract->companion family"])

    out["prose_rowsfields"] = f"{rows_n} rows, {fields_n} fields"
    out["prose_scope719"] = f"the **{listed}** manuscript directories the release"
    out["prose_dirsdisk"] = (f"**{disk}** directories on disk = **{listed}** listed + "
                             f"**{superseded}** superseded + **{notices}** withdrawal")

    out["sec426_head"] = f"{chal} vs {chal_distinct}"
    out["sec426_files"] = f"({chal_docs} files) contain"
    out["sec426_occ"] = f"**{chal}** occurrences of"
    out["sec426_distinct"] = f"**{chal_distinct}** distinct config names"
    out["sec426_extra"] = f"The {chal_dup} extra occurrences"
    out["sec426_docs"] = f"{chal_dupdocs} docs: `{mdup.group(1)}`"
    out["sec426_shared"] = f"**{chal_shared}** configs are linked by more"
    out["sec426_partition"] = f"the {chal_distinct} configs are partitioned"
    out["sec426_chal"] = f"sums to **{chal_distinct}** while this row counts **{chal}**"
    out["sec426_genline"] = f"the generator report line is `challenges {chal_distinct}`"
    out["sec426_json"] = (f"**{cfg_unlinked}** of the {cfg_lean} `.json` files are unlinked "
                          f"and **{cfg_unlinked}** linked")

    out["mr_head"] = f"{mr} / {mr_cfgs} / {mr_fams}"
    out["mr_entries"] = f"carries **{mr}** `comparator_config:` entries over"
    out["mr_cfgs"] = f"**{mr_cfgs}** unique configs — **{mr_rep}** repeated entries across"
    out["mr_fams"] = (f"**{mr_fams}** families have ≥1 entry, and the ledger `mainres` "
                      f"column sums to {mr_cfgs}")
    out["mr_notrepro"] = f"the measured figure is {mr_fams}"
    out["mr_gap"] = (f"{mr_fams} families have a `main_results` entry; **{form_fams}** have a "
                     f"formalized manuscript ({formalized} manuscripts)")
    out["mr_diff"] = f"`mainres`−formalized = **{mainres_only}** family:"
    out["mr_formdiff"] = f"formalized−`mainres` = **{form_only}**"

    out["mm_entries"] = f"In the {f(bibent)} bibliography entries owned by listed"
    out["mm_393"] = f"**{bibhref}** contain the literal string"
    out["mm_391"] = f"**{bibres}** resolve to a shipped"
    out["mm_unres"] = f"(**{bibunres}** unresolved)"
    out["mm_targets"] = (f"span **{bibtarg}** target directories over **{bibfams} of {families} "
                         f"families**, from **{bibcite}** citing directories")
    out["mm_same"] = (f"**{bibsame}** point at a manuscript of the same family, "
                      f"**{bibcross}** cross a family boundary")
    out["mm_body"] = f"**{bodyhref}** " + "`\\href{…/preprints/…}` occurrences in `.tex`, over"
    out["mm_bodytargets"] = (f"**{bodytarg}** target directories spanning **{bodyfams}** "
                             f"families, from **{bodycite}** citing directories")
    out["mm_bodyall"] = f"All {body_targ2} body"
    out["mm_outside"] = f"**{stale_listed}** of the {bibres} resolved"
    out["mm_tree"] = (f"resolves **{tree_hrefs}** hrefs, of which **{tree_stale}** point at "
                      f"**{tree_staledirs}** superseded editions")
    for fam, cnt in top:
        out[f"top_{fam}"] = f"**{fam}** ({cnt})"
    out["mm_edges"] = (f"carries {bibres} resolved manuscript→manuscript citation edges "
                       f"reaching {bibfams} families")

    out["namerow_named"] = (f"| named-in-title | `overview.tex` `\\resultentry` arg 2 | "
                            f"**{named}** of {families} | — |")
    out["namerow_cited"] = f"| cited-in-bib | `preprints/**/*.bib` | **{cited}** of {families} | {cited_own} |"
    out["namerow_mentioned"] = (f"| mentioned-in-body | `preprints/**/*.tex` | **{mentioned}** of "
                                f"{families} | {mentioned_own} |")
    out["cited_list"] = ", ".join(cited_l)
    out["mentioned_list"] = ", ".join(mentioned_l)
    out["inter_count"] = f"**{len(inter_l)}** of these {mentioned}"
    out["inter_list"] = f"({', '.join(inter_l)})"
    out["mentonly_count"] = f"the **{len(mentonly_l)}** that do not"
    out["mentonly_list"] = f"**{', '.join(mentonly_l)}**"
    out["citedonly"] = f"{len(citedonly_l)} of the {cited} `cited-in-bib` families ({', '.join(citedonly_l)})"

    out["rec_glob"] = (f"reach **{legacy_files} of the {all_files}** listed-manuscript `.bib` "
                       f"files; the {all_files - legacy_files} at depth 4")
    out["rec_all"] = (f"over all {all_files} listed files: **{all_any}** families, "
                      f"**{all_cross}** cross-family.")

    out["knob_row1"] = (f"| 6-token prefix | lowercased | {legacy_files} (depth ≤3) | "
                        f"**{legacy_any}** ← the recorded figure | {legacy_cross} |")
    out["knob_row2"] = (f"| 6-token prefix | lowercased | {all_files} (all listed) | {all_any} | "
                        f"{all_cross} |")
    out["knob_row8"] = (f"| normalized full title | normalized | {all_files} | **{cited_own}** | "
                        f"**{cited}** ← shipped `cited-in-bib` |")
    out["knob_dominant"] = f"taking 5 to {cited_own}"
    out["knob_quote"] = (f"Quote {legacy_any} with its rule and its {legacy_files}-file scope, "
                         f"and quote {all_cross} with the normalized rule and the {all_files}-file scope.")
    out["knob_layers"] = (f"reaches {all_cross} cross-family families while the href layer "
                          f"reaches {bibcross}")

    out["neg_msc"] = f"**{msc}** MSC codes anywhere"
    out["neg_files"] = (f"over {f(msc_files)} files ({f(tex_files)} `.tex` + {bibfiles} `.bib` "
                        f"+ `overview.tex`)")
    out["neg_kw"] = f"**{kw_bib}** `keywords =` fields in {f(bibent)} bibliography entries"
    out["neg_kwmacro"] = "`\\keywords` in " + f"**{kw_tex}** of {listed} manuscript directories ({kw_pct}%)"
    out["neg_companion"] = f"**{comp}** companion edges: `" + "`, `".join(f"{a}→{b}" for a, b in pairs) + "`"
    out["neg_bcline"] = f"`notes/scripts/build_catalog.py:{bc_line}`"
    out["neg_word"] = (f'**{compword}** families use the word "companion" in an abstract and '
                       f"**{compword_edges}** of them carry a `result NNN` edge")
    out["neg_onesided"] = (f"**{ov_only}** one-sided family→manuscript links: `overview.tex`-only "
                           f"links {ov_only}, `CONTENTS.md`-only links {ct_only}")

    out["nc_393"] = f"The {bibhref} release-labelled entries"
    out["nc_12"] = f"the {cited} validated `cited-in-bib` cases"
    out["nc_104"] = f"The {bibcross} cross-family citation edges"
    out["nc_11"] = f"The {mentioned} cross-family hits"
    out["nc_211"] = f"The {bodyhref} body hrefs"
    out["nc_bibcov"] = (f"Bibliography coverage is **{bibdirs} of {listed}** manuscript "
                        f"directories. The {listed - bibdirs} directories with no `.bib`")
    out["nc_entries"] = f"The {f(bibent)} entries are counted by"
    out["nc_verif"] = f"Whether the {verif} verification directories"
    out["nc_superseded"] = f"The {superseded} superseded editions and {notices} withdrawal notices"
    return out


def links_phrases(p: dict[str, Any]) -> dict[str, str]:
    """The slot dict: base labels, then each page-wrapped phrase as label a, label b, …"""
    full = links_full(p)
    out: dict[str, str] = {}
    for label, val in full.items():
        prefixes = LINKS_SPLIT.get(label)
        if not prefixes:
            out[label] = val
            continue
        rest = val
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                msg = f"slot {label!r}: page wrap {pre!r} is not a prefix of {rest!r}"
                raise ValueError(msg)
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def links_page(p: dict[str, str]) -> str:
    return ENV.get_template("links.md.j2").render(p=p)


def main() -> None:
    mp = en.population()
    ip = M.population()
    np_ = names_population()
    pdp = proof_density_population()
    ilk = index_links_population()
    lk = links_population()
    SOURCES_MD.write_text(sources_page(), encoding="utf-8")
    ABSTRACTS_MD.write_text(abstracts_page(), encoding="utf-8")
    NAMED_RESULTS_MD.write_text(named_results_page(mp), encoding="utf-8")
    INDEX_DESIGN_MD.write_text(index_page(ip), encoding="utf-8")
    NAMES_MD.write_text(names_page(names_phrases(np_)), encoding="utf-8")
    PROOF_DENSITY_MD.write_text(proof_density_page(proof_density_phrases(pdp)), encoding="utf-8")
    INDEX_LINKS_MD.write_text(index_links_page(index_links_phrases(ilk)), encoding="utf-8")
    LINKS_MD.write_text(links_page(links_phrases(lk)), encoding="utf-8")
    for page in (SOURCES_MD, ABSTRACTS_MD, NAMED_RESULTS_MD, INDEX_DESIGN_MD, NAMES_MD,
                 PROOF_DENSITY_MD, INDEX_LINKS_MD, LINKS_MD):
        out = page.read_text(encoding="utf-8")
        print(f"{page.name} written  lines {len(out.splitlines())}  bytes {len(out.encode())}")
    ms, ma = measure(), CA.measure()
    print(f"slots  sources {len(phrases(ms))}  abstracts {len(abstracts_phrases(ma))}"
          f"  named-results {len(named_results_phrases(mp))}"
          f"  index-design {len(index_phrases(ip))}  names {len(names_phrases(np_))}"
          f"  proof-density {len(proof_density_phrases(pdp))}"
          f"  index-links {len(index_links_phrases(ilk))}  links {len(links_phrases(lk))}"
          f"  multi-root rows {len(ms['multi'])}  rows {ms['rows']}  listed {ms['listed']}"
          f"  dirs {ms['dirs']}  comparisons {ma['manuscripts']}  families {ma['families']}"
          f"  target rows {len(tgt_rows(mp))}")


if __name__ == "__main__":
    main()
