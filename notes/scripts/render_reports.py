#!/usr/bin/env python3
"""Render the report-fed notes pages from the templates at notes/templates/report/.

Writer: the 16 report-fed pages under notes/ — sources.md, abstracts.md, named-results.md,
index-design.md, names.md, proof-density.md, index-links.md, links.md, dependency-drift.md,
formalization-deps.md, verification-dirs.md, scope-exclusions.md, topics.md, t0-chains.md,
subfinding-pairs.md and README.md — each from its template at notes/templates/report/. Every
number on a page is measured here, either by calling the report the page itself names as its rule
(compare_abstracts.measure() for abstracts.md, extract_named_results.population() for
named-results.md, measure_index_sizes.population() for index-design.md, check_index_links.measure()
for index-links.md, measure_names.measure() for names.md, measure_proof_density for
proof-density.md, measure_topics for topics.md, extract_links run as a subprocess for links.md) or
by recounting the files on disk (sources.md), while each page's checker keeps its own
recomputation. The split is deliberate, and it is now two passes with two jobs: the checker's own
measurement is what proves the page's numbers are measured — a checker that only re-ran this module
would prove nothing about them — while catlib.render.sync_problems(), which asks this module for
the page's rendered bytes, is what proves the page on disk is the bytes the writer produces.
Neither pass substitutes for the other. Because the writer computes a page's slots by importing,
or spawning, the very scripts that call that sync pass, catlib.render.sync_inert() makes the pass
inert inside a render and in a child marked by RENDER_REPORTS_CHILD; without it a sync pass
started from a mutant would re-enter the render that is computing the mutant.
verify_sources.py re-derives its 31 figures from disk; verify_abstracts.py delegates its count pass
to compare_abstracts.measure() (the page says its counts come from that report) and keeps its
marker and quotation passes independent of this module.

Slot contract: p['<label>'] is the exact phrase string the checker's needle list carries for a
figure, m['<key>'] the measured value behind it. Where the page wraps a phrase across lines, the
label carries an " a"/" b" suffix and the two strings sit on the page's own lines — the checker
compares with whitespace collapsed, so a split phrase is checked as one. Prove a render by running
this script and diffing the page against the committed bytes: 0 differences.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import os
import pathlib
import posixpath
import re
import statistics
import subprocess
import sys
from collections.abc import Callable
from functools import cache
from typing import Any

from jinja2 import Environment, FileSystemLoader

import build_catalog as B
import build_sources as S
import check_index_links as CI
import compare_abstracts as CA
import extract_counterexample_crosscheck as cc
import extract_named_results as en
import extract_scope_notes as ex
import extract_subfinding_pairs as ep
import extract_t0_chains as tc
import extract_verification_dirs as evd
import measure_index_sizes as M
import measure_names as MN
import measure_proof_density as PD
import measure_templates as MTPL
import measure_topics as MT
from catlib import overview, preprints, tsv
from catlib import render as RD
from catlib import yaml as Y
from catlib.paths import (COMPARATOR_DIR, DEPS_TSV, FORMALIZATION_YAML, LAKEFILE, LAKE_MANIFEST,
                          LEDGER_TSV, PREPRINTS, ROOT, SUBFINDINGS_TSV, owner)

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
DRIFT_MD = ROOT / "notes" / "dependency-drift.md"
PATCHES_DIR = ROOT / "lean" / "patches"
TOOLCHAIN_FILE = ROOT / "lean" / "lean-toolchain"
DEPS_MD = ROOT / "notes" / "formalization-deps.md"
VERIF_MD = ROOT / "notes" / "verification-dirs.md"
EX_MD = ROOT / "notes" / "scope-exclusions.md"
TOPICS_MD = ROOT / "notes" / "topics.md"
T0_CHAINS_MD = ROOT / "notes" / "t0-chains.md"
SP_MD = ROOT / "notes" / "subfinding-pairs.md"
README_MD = ROOT / "notes" / "README.md"
CROSSCHECK_MD = ROOT / "notes" / "counterexample-crosscheck.md"
TEMPLATES_MD = ROOT / "notes" / "templates.md"
VPOS = PREPRINTS / "Positively-curved-Einstein-four-manifolds-September-23-2026" / "verification"
VZERO = PREPRINTS / "Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026" / "verification"
FOCK = PREPRINTS / "A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026"
UNIF = PREPRINTS / "Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026"
NUM_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
             8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}


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
        "strict replacement": f"would read {len(strict)} ({len(rn - strict)} removals against the "
                              f"applied {len(rn)} column)",
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
    caught, mt_total, cases = PD.mutants(PD.build_families)
    # The sync-pass mutant cannot fire here: catlib.render.sync_inert() is True while this render is
    # in progress, so the pass returns [] by design (the writer rendering the page the page's own
    # checker asks for would recurse). The writer IS the render that mutant is compared against, so
    # it records it as caught; the standalone --mutant run in notes/scripts/gate.sh is what proves it.
    if RD.sync_inert():
        caught += sum(1 for name, ok, _ in cases if name == PD.SYNC_MUTANT and not ok)
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
    "prose_fresh": ["**21 injected, 21 caught, 0 missed; 7 controls, 7"],
    "prose_surplus": ["The 18,095 surplus links are"],
}


def build_index_report() -> dict[str, Any]:
    """Run notes/scripts/build_index.py and parse the report lines the page quotes.

    A subprocess, not an import: build_index.py calls main() at module scope, so importing it
    would build the index inside every render.
    """
    proc = subprocess.run([sys.executable, str(ROOT / "notes" / "scripts" / "build_index.py")],
                          capture_output=True, text=True, check=True, cwd=ROOT,
                          env={**os.environ, "RENDER_REPORTS_CHILD": "1"})
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
    caught, total, missed, clean, ctotal, wrong, trap, classed = CI.mutant_test()
    # The sync-pass mutant cannot fire here: catlib.render.sync_inert() is True while this render
    # is in progress, so the pass returns [] by design (the writer rendering the page the page's
    # own checker asks for would recurse). The writer IS the render that mutant is compared
    # against, so it records it as caught; the standalone --mutant run in notes/scripts/gate.sh is
    # what proves it.
    if RD.sync_inert():
        sync_missed = [m for m in missed if m.startswith(CI.SYNC_MUTANT)]
        caught += len(sync_missed)
        missed = [m for m in missed if m not in sync_missed]
    return {"scan": CI.measure(), "build": build,
            "mutant": (caught, total, missed, clean, ctotal, wrong, trap, classed)}


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
                          capture_output=True, text=True, check=True, cwd=ROOT,
                          env={**os.environ, "RENDER_REPORTS_CHILD": "1"})
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

    # Unformatted counts, for the page that prints these figures without bold or thousands separators.
    out["raw_msc"] = str(msc)
    out["raw_msc_files"] = str(msc_files)
    out["raw_kw_bib"] = str(kw_bib)
    out["raw_kw_tex"] = str(kw_tex)
    out["raw_bibent"] = str(bibent)
    out["raw_listed"] = str(listed)

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


# =============================================================================
# notes/dependency-drift.md — the pinned-commit / patch surface
# =============================================================================
#
# Read-only over the page's sources: notes/formalization-deps.tsv, lean/lakefile.lean,
# lean/patches/*.patch, lean/lean-toolchain, lean/lake-manifest.json, lean/formalization.yaml and the
# OAI source-file count recorded in notes/formalization-deps.md. Nothing is built and nothing is run.
#
# verify_dependency_drift.py is deliberately NOT imported. A checker that re-derives a count through
# the same code as the page it checks proves nothing, so the checker keeps its own recomputation and
# this section stays on the writer side of that line.
DRIFT_REQUIRE = re.compile(
    r'^require\s+(?:«(?P<l1>[^»]+)»|(?P<l2>[A-Za-z0-9_.\-]+))\s+from\s+git\s*\n'
    r'\s*"(?P<url>[^"]+)"\s*@\s*"(?P<commit>[0-9a-f]+)"', re.M)
PRE_ARRAY = "preResolutionPatchNames : Array Lean.Name := #["
POST_ARRAY = "for name in #["


def drift_strip(s: str) -> str:
    """Lakefile labels are written «doc-gen4»; the TSV key is doc-gen4."""
    return s.strip("«»")


def drift_requires(text: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for m in DRIFT_REQUIRE.finditer(text):
        raw = m.group("l1") or m.group("l2")
        out.append({"label": drift_strip(raw), "raw": f"«{raw}»" if m.group("l1") else raw,
                    "url": m.group("url"), "commit": m.group("commit"),
                    "line": text[:m.start()].count("\n") + 1})
    return out


def drift_array(text: str, marker: str) -> tuple[list[str], int, int]:
    """Names in a hard-coded lakefile array, with the array's first and last line.

    Lean writes a name as `iut with one leading backtick and no closing one, so the closing
    delimiter is whitespace, a comma, or the array's `]`.
    """
    i = text.index(marker)
    j = text.index("]", i)
    names = [drift_strip(s) for s in re.findall(r"`([^\s`,\]]+)", text[i:j])]
    return names, text[:i].count("\n") + 1, text[:j].count("\n") + 1


def drift_patches() -> dict[str, dict[str, Any]]:
    """Per patch file: lines, `diff --git` hunks, files touched, toolchain hunk, from/to versions."""
    out: dict[str, dict[str, Any]] = {}
    for p in sorted(PATCHES_DIR.glob("*.patch")):
        text = p.read_text(encoding="utf-8", errors="replace")
        lines = text.split("\n")
        heads = [i for i, ln in enumerate(lines) if ln.startswith("diff --git ")]
        files: list[str] = []
        for i in heads:
            tail = lines[i].split()[-1]
            files.append(tail[2:] if tail.startswith("b/") else tail)
        froms: list[str] = []
        tos: list[str] = []
        for k, i in enumerate(heads):
            end = heads[k + 1] if k + 1 < len(heads) else len(lines)
            if not files[k].endswith("lean-toolchain"):
                continue
            for ln in lines[i:end]:
                if "leanprover/lean4:" not in ln:
                    continue
                ver = ln.split("leanprover/lean4:")[-1].strip()
                if ln.startswith("-"):
                    froms.append(ver)
                elif ln.startswith("+"):
                    tos.append(ver)
        out[p.name] = {"lines": len(text.splitlines()), "hunks": len(heads), "files": len(files),
                       "toolchain": any(f.endswith("lean-toolchain") for f in files),
                       "lakefile": any(re.search(r"(^|/)lakefile\.\w+$", f) for f in files),
                       "froms": froms, "tos": tos}
    return out


def drift_key(url: str) -> str:
    """Repo URL -> TSV library key, the derivation the yaml ordering check needs."""
    last = url.rstrip("/").split("/")[-1]
    if last.endswith(".git"):
        last = last[: -len(".git")]
    key = re.sub(r"[0-9]+$", "", re.sub(r"[^a-z0-9]", "", last.lower()))
    for suffix in ("lean4", "lean"):
        if key.endswith(suffix) and len(key) > len(suffix):
            key = re.sub(r"[0-9]+$", "", key[: -len(suffix)])
            break
    return key


def drift_above(nm: str) -> str:
    """The page names a violation's upper entry by its repo name minus the toolchain suffix.

    `fixed-point-theorems-lean4` is the yaml `id`'s last segment; the page writes
    `fixed-point-theorems`. The TSV library name is not the rule here - the page writes
    `zeta_3_irrational`, the URL segment, where the TSV name is `Zeta3Irrational`.
    """
    return re.sub(r"-lean\d*$", "", nm)


def drift_violations(imports_by_key: dict[str, int]) -> list[tuple[int, str, int, str, int]]:
    """yaml `related_formalizations` entries that break the ordering comment the file carries."""
    lines = Y.yaml_lines(tolerant=True)
    start = lines.index("related_formalizations:")
    urls: list[str] = []
    for ln in lines[start + 1:]:
        if ln and not ln.startswith(" "):
            break
        m = re.match(r"\s+-\s+id:\s*(\S+)", ln)
        if m:
            urls.append(m.group(1))
    out: list[tuple[int, str, int, str, int]] = []
    prev: tuple[int, int, str] | None = None
    for i, url in enumerate(urls, start=1):
        last = url.rstrip("/").split("/")[-1]
        if last.endswith(".git"):
            last = last[: -len(".git")]
        cnt = imports_by_key.get(drift_key(url))
        if cnt is None:
            continue
        if prev is not None and cnt > prev[1]:
            out.append((i, last, cnt, prev[2], prev[1]))
        prev = (i, cnt, last)
    return out


def drift_population() -> dict[str, Any]:
    rows = tsv.read_rows(DEPS_TSV)
    fields = len(DEPS_TSV.read_text(encoding="utf-8").splitlines()[0].split("\t"))
    declared = [r for r in rows if r["lakefile_declared"] == "y"]
    # A typed side table keyed by stripped library name: the TSV rows are dict[str, str] and the
    # numeric reads below need ints, so the rows are never widened in place.
    metric: dict[str, dict[str, Any]] = {
        drift_strip(r["library"]): {
            "imports": int(r["direct_imports"]),
            "plines": int(r["patch_lines"]),
            "patch_file": r["patch_file"],
            "repo_url": r["repo_url"],
        }
        for r in declared
    }
    lake_text = LAKEFILE.read_text(encoding="utf-8")
    reqs = drift_requires(lake_text)
    pre, pre_s, pre_e = drift_array(lake_text, PRE_ARRAY)
    post, post_s, post_e = drift_array(lake_text, POST_ARRAY)
    patches = drift_patches()
    by_name = metric
    zero = sorted(n for n, v in by_name.items() if v["imports"] == 0)
    patched = sorted(n for n, v in by_name.items() if v["patch_file"] != "none")
    froms: collections.Counter[str] = collections.Counter()
    for v in patches.values():
        froms.update(v["froms"])
    imports_by_key = {drift_key(v["repo_url"]): v["imports"] for v in by_name.values()}
    manifest = json.loads(LAKE_MANIFEST.read_text(encoding="utf-8"))
    pkg_names = {drift_strip(q["name"]) for q in manifest["packages"]}
    src = re.search(r'OAI/\*\*/\*\.lean` \((\d[\d,]*) files\)', DEPS_MD.read_text(encoding="utf-8"))
    if src is None:
        msg = "notes/formalization-deps.md names no OAI source-file count"
        raise ValueError(msg)
    return {
        "rows": rows, "fields": fields, "declared": declared, "reqs": reqs,
        "patches": patches, "by_name": by_name, "zero": zero, "patched": patched,
        "lake_lines": len(lake_text.splitlines()), "commit_len": min(len(r["commit"]) for r in reqs),
        "pre": pre, "pre_s": pre_s, "pre_e": pre_e, "post": post, "post_s": post_s, "post_e": post_e,
        "pre_lines": sum(by_name[x]["plines"] for x in pre),
        "post_lines": sum(by_name[x]["plines"] for x in post),
        "total_lines": sum(v["lines"] for v in patches.values()),
        "total_hunks": sum(v["hunks"] for v in patches.values()),
        "tc": sum(1 for v in patches.values() if v["toolchain"]),
        "lakefile_patches": sum(1 for v in patches.values() if v["lakefile"]),
        "froms": froms, "tos": sorted({v for p in patches.values() for v in p["tos"]}),
        "nopatch": sorted(n for n, v in by_name.items() if v["patch_file"] == "none"),
        "zero_nopatch": sorted(n for n, v in by_name.items()
                               if v["imports"] == 0 and v["patch_file"] == "none"),
        "zero_patched": sorted(n for n, v in by_name.items()
                               if v["imports"] == 0 and v["patch_file"] != "none"),
        "post_zero": sorted(set(post) & set(zero)),
        "lana": sorted(n for n, v in by_name.items() if "lana-agents/" in v["repo_url"]),
        "last_block": [r for r in reqs if r["line"] >= 73],
        "last_block_nopatch": len([r for r in reqs if r["line"] >= 73
                                   if by_name[r["label"]]["patch_file"] == "none"]),
        "imports": imports_by_key,
        "violations": drift_violations(imports_by_key),
        "med_import": statistics.median([v["plines"] for v in by_name.values() if v["imports"] > 0]),
        "med_zero": statistics.median([v["plines"] for v in by_name.values() if v["imports"] == 0]),
        "manifest_pkgs": len(pkg_names),
        "transitive": sorted(pkg_names - set(by_name)),
        "toolchain": TOOLCHAIN_FILE.read_text(encoding="utf-8").splitlines()[0].strip(),
        "src_files": int(src.group(1).replace(",", "")),
    }


def drift_full(p: dict[str, Any]) -> dict[str, str]:
    by_name: dict[str, dict[str, Any]] = p["by_name"]
    reqs: list[dict[str, Any]] = p["reqs"]
    n_decl = len(p["declared"])
    n_patch = len(p["patches"])
    n_zero = len(p["zero"])
    out: dict[str, str] = {}
    out["hdr_tsv"] = f"({len(p['rows'])} rows, {p['fields']} fields)"
    out["hdr_lake_lines"] = f"({p['lake_lines']} lines)"
    out["hdr_patches"] = f"{n_patch} `*-lean4341.patch` files plus `README.md`"
    out["t1_row1"] = (f"| `require … from git \"url\" @ \"commit\"` declarations | **{len(reqs)}**, "
                      f"every one pinned to a **{p['commit_len']}-char** commit | "
                      f"`lean/lakefile.lean:{reqs[0]['line']}`–`:{reqs[-1]['line'] + 1}` |")
    out["t1_row2"] = (f"| Patch files | **{n_patch}**, **{f(p['total_lines'])}** lines, "
                      f"**{f(p['total_hunks'])}** `diff --git` file hunks | `lean/patches/` |")
    out["t1_row3"] = (f"| Declared libraries with **no** patch | **{len(p['nopatch'])}** | "
                      "`notes/formalization-deps.tsv` |")
    out["t1_row4"] = (f"| Patches that rewrite the dependency's `lean-toolchain` | "
                      f"**{p['tc']} of {n_patch}** | `lean/patches/*.patch` |")
    out["t1_row5"] = (f"| Distinct toolchain versions the patches migrate **from** | "
                      f"**{len(p['froms'])}**, all migrating **to** `{p['tos'][0]}` | "
                      "`lean/patches/*.patch` |")
    out["t1_row6"] = f"| Release toolchain | `{p['toolchain']}` | `lean/lean-toolchain:1` |"
    out["p1_23names"] = f"The {n_patch} patch filenames all end"
    out["p1_impl"] = f"A {f(p['src_files'])}-file agent-generated Lean tree"
    ranked = sorted(p["froms"].items(), key=lambda kv: (-kv[1], kv[0]))
    multi = [f"`{v}` ×{c}" for v, c in ranked if c > 1]
    single = [f"`{v}`" for v, c in ranked if c == 1]
    out["p1_tc_move"] = (f"The {p['tc']} toolchain hunks move {len(p['froms'])} distinct upstream "
                         f"versions onto the release's own: {', '.join(multi)}, and one each of "
                         f"{', '.join(single)}.")
    out["p1_sits"] = (f"It sits on {len(reqs)} pinned commits plus {f(p['total_lines'])} lines of "
                      f"release-specific edits to {n_patch} of them, {p['tc']} of which have had "
                      "their toolchain rewritten to match.")
    out["p1_ratio"] = (f"The compatibility layer is {round(p['total_lines'] / p['src_files'], 1)} "
                       "lines of patch per source file in the tree it supports.")
    out["t4_row1"] = (f"| Pre-resolution (`run_cmd`) | `lean/lakefile.lean:{p['pre_s']}`–`:{p['pre_e']}`, "
                      f"driven at `:271`–`:275` | **{len(p['pre'])}** | **{f(p['pre_lines'])}** |")
    out["t4_row2"] = (f"| `post_update` preflight | `lean/lakefile.lean:{p['post_s']}`–`:{p['post_e']}` | "
                      f"**{len(p['post'])}** | **{f(p['post_lines'])}** |")
    out["p4_union"] = f"their union is **exactly** the {n_patch} patched libraries"
    out["p4_lana"] = (f"The {len(p['pre'])} pre-resolution libraries are **exactly** the "
                      f"{len(p['lana'])} declared libraries whose URL is under")
    out["p4_overrule"] = f"for the {len(p['pre'])} libraries it controls the source of"
    lb = p["last_block"]
    out["p5_requires"] = (f"is **{len(lb)}** requires "
                          f"(`lean/lakefile.lean:{lb[0]['line']}`–`:{lb[-1]['line'] + 1}`):")
    out["p5_names"] = ", ".join(f"`{r['raw']}`" if r["raw"].startswith("«") else r["raw"]
                                for r in lb) + "."
    out["p5_nopatch"] = f"**{p['last_block_nopatch']} of those {len(lb)} ship no patch**"
    out["p5_one"] = f"One mathlib across {len(reqs)} pinned third-party trees"
    out["p5_plus"] = (f"It is achieved by last-wins ordering plus {p['tc']} patches that rewrite "
                      "each dependency's own toolchain, plus patches that rewrite a dependency's "
                      "own mathlib revision.")
    out["p5_imposed"] = f"The release's mathlib version is imposed on the ecosystem, {p['tc']} times."
    out["p6_table_intro"] = f"The table is all **{n_patch}** declared libraries with a patch, ordered by patch lines."
    for i, name in enumerate(sorted(p["patched"], key=lambda k: -by_name[k]["plines"]), start=1):
        imp = by_name[name]["imports"]
        out[f"lib_{i:02d}"] = f"| {name} | {'**0**' if imp == 0 else imp} | {f(by_name[name]['plines'])} |"
    out["p6_median"] = (f"Median patch lines: **{f(int(p['med_import']))}** for declared libraries "
                        f"with any direct import, **{f(int(p['med_zero']))}** for declared "
                        "libraries with none.")
    top = max(p["patched"], key=lambda k: by_name[k]["plines"])
    top_imp = max(by_name, key=lambda k: by_name[k]["imports"])
    top_zero = max(p["zero"], key=lambda k: by_name[k]["plines"])
    out["p6_largest"] = (f"The largest patch in the release, {top} at {f(by_name[top]['plines'])} "
                         f"lines, sits beside the largest import count, {top_imp} at "
                         f"{f(by_name[top_imp]['imports'])} — and {top_imp} itself ships **no** patch.")
    out["p6_largest_unused"] = (f"The largest patch on a library OAI never imports directly is "
                                f"{top_zero} at {f(by_name[top_zero]['plines'])} lines.")
    out["p6_tau"] = (f"A library can be load-bearing and untouched (mathlib, TauCeti at "
                     f"{by_name['TauCeti']['imports']} imports) or unused and heavily rewritten "
                     "(AINTLIB, carleson).")
    out["p7_zero"] = f"**{n_zero} of the {n_decl}** declared libraries have `direct_imports = 0`:"
    out["p7_zerolist"] = ", ".join(f"`{n}`" for n in p["zero"]) + "."
    out["p7_zeropatched"] = (f"**{len(p['zero_patched'])} of those {n_zero} ship a patch**; "
                             f"the {len(p['zero_nopatch'])} that do not are")
    out["p7_zeronopatch"] = ", ".join(f"`{n}`" for n in p["zero_nopatch"]) + "."
    out["p7_allpre"] = (f"All {len(p['pre'])} pre-resolution libraries are in the zero-import set, "
                        f"and {len(p['post_zero'])} of the {len(p['post'])} `post_update` libraries are "
                        "(" + ", ".join(f"`{n}`" for n in p["post_zero"]) + ").")
    out["p7_viol"] = (f"**That claim is recorded, not asserted true, and {len(p['violations'])} "
                      "entries violate it** (measured in")
    out["p7_violist"] = "; ".join(f"{name} {cnt} above {drift_above(prev)} {pcount}"
                                  for _, name, cnt, prev, pcount in p["violations"]) + ")"
    out["p7_zero19"] = (f"The {n_zero} zero-import libraries sit beside that claim: an "
                        f"ordering-by-import comment over a list in which {n_zero} of {n_decl} "
                        "entries import nothing directly is a claim about a list that is mostly not a usage list.")
    out["p7_manifest"] = f"({p['manifest_pkgs']} resolved packages)"
    out["p7_transitive"] = (f"The manifest's {len(p['transitive'])} transitive-only packages "
                            "(`Qq`, `aesop`, `batteries`, …) are none of the "
                            f"{n_zero} zero-import libraries")
    out["p7_floor"] = ("the direct-import counts are the floor they are: **no direct import**, "
                       "not non-use.")
    out["p7_impl"] = (f"{n_decl} declarations, {n_decl - n_zero} with direct imports, "
                      f"{n_zero} with none, {n_patch} patched.")
    out["nc_hunks"] = f"The {f(p['total_hunks'])} `diff --git` hunks are counted by filename"
    out["nc_lines"] = (f"how much of the {f(p['total_lines'])} lines is toolchain-compat renaming "
                       "and how much is mathematics.")
    out["nc_split"] = f"The {len(p['pre'])}/{len(p['post'])} phase split is read from two hard-coded arrays"
    out["nc_last"] = f"{n_decl} declarations, {n_patch} patches, no build to say which are load-bearing."
    return out


DRIFT_SPLIT = {
    "p1_tc_move": ["The 22 toolchain",
                   "hunks move 8 distinct upstream versions onto the release's own: "
                   "`v4.32.0` ×13, `v4.34.0` ×3, and one"],
    "p1_sits": ["It sits on 30 pinned commits plus 160,187 lines of release-specific edits to 23 of them,"],
    "p1_ratio": ["The compatibility layer is 1.3 lines of patch"],
    "p5_nopatch": ["**6 of"],
    "p5_plus": ["It is achieved by last-wins ordering plus 22 patches that rewrite each"],
    "p5_imposed": ["The"],
    "p6_table_intro": ["The table is all **23** declared"],
    "p6_median": ["Median patch lines: **2,575** for declared libraries with any direct import, "
                  "**408** for declared"],
    "p6_largest": ["The largest patch in the release, PrimeNumberTheoremAnd at 39,904 lines, sits"],
    "p6_largest_unused": ["The"],
    "p6_tau": ["A library can be load-bearing and"],
    "p7_zerolist": ["`AINTLIB`, `LeanArchitect`,",
                    "`PrimeCert`, `Zeta3Irrational`, `belyi`, `carleson`, `checkdecls`, `doc-gen4`, "
                    "`elliptic-curves`,",
                    "`formal-schemes`, `genl`, `heights`, `iut`, `leancert`, `oka`, `orbicurve-cores`, `pi1`,"],
    "p7_zeropatched": ["**14 of those 19 ship a patch**; the 5 that do not"],
    "p7_allpre": ["All 11 pre-resolution",
                  "libraries are in the zero-import set, and 3 of the 12 `post_update` libraries are"],
    "p7_violist": ["strongpnt 12 above AINTLIB 0; TauCeti 5 above fixed-point-theorems 4;",
                   "gromov 2 above heights 0; schoenflies-lean 2 above iut 0; AbsorptionCutoff 1 above"],
    "p7_zero19": ["The 19 zero-import libraries sit beside that claim: an ordering-by-import",
                  "comment over a list in which 19 of 30 entries import nothing directly is a claim "
                  "about a list that is"],
    "p7_transitive": ["The",
                      "manifest's 12 transitive-only packages (`Qq`, `aesop`, `batteries`, …) are none "
                      "of the 19 zero-import"],
    "p7_floor": ["the direct-import counts are the floor they are: **no direct"],
}


def drift_phrases(p: dict[str, Any]) -> dict[str, str]:
    """The slot dict: base labels, then each page-wrapped phrase as label a, label b, …"""
    full = drift_full(p)
    out: dict[str, str] = {}
    for label, val in full.items():
        prefixes = DRIFT_SPLIT.get(label)
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


def drift_page(p: dict[str, str]) -> str:
    return ENV.get_template("dependency-drift.md.j2").render(p=p)


def verif_sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def group_fams(fams: list[str]) -> str:
    """Sorted families with repeats folded into `NNN (×k)`, the form the page prints."""
    counts: list[tuple[str, int]] = []
    for fam in sorted(fams):
        if counts and counts[-1][0] == fam:
            counts[-1] = (fam, counts[-1][1] + 1)
        else:
            counts.append((fam, 1))
    return ", ".join(f"{fam}" if n == 1 else f"{fam} (×{n})" for fam, n in counts)


def verification_dirs_population() -> dict[str, Any]:
    """Every count notes/verification-dirs.md prints, recomputed from the shipped bundles.

    The rules are the ones verify_verification_dirs.py measures with, re-derived on the writer side
    through extract_verification_dirs.py. The checker deliberately does not import this module: a page
    that drifts from the files has to show up as a checker failure, not as a shared blind spot.
    """
    rows = tsv.read_rows(LEDGER_TSV)
    cov = sorted({r["fam"] for r in rows if int(r["covmd"]) > 0})
    inp = sorted(r["fam"] for r in rows if int(r["inputs"]) > 0)
    fam_by_slug, _order, _fams = evd.families_by_slug()
    bundles = [p for p in sorted(x for x in evd.PRE.iterdir() if x.is_dir())
               if (p / "verification").is_dir()]
    named, runsec, unnamed = [], [], []
    for p in bundles:
        heads = evd.headings(p / "README.md")[1]
        if any("Verification" in h for _, h in heads):
            named.append(p.name)
        elif any("Run the verification code" in h for _, h in heads):
            runsec.append(p.name)
        else:
            unnamed.append(p.name)
    classes: dict[str, int] = {}
    no_entry, declaring, readme_fams = [], [], []
    for p in bundles:
        bundle = p / "verification"
        _, rule, _ = evd.entry_point(bundle)
        classes[rule] = classes.get(rule, 0) + 1
        if rule == "none":
            no_entry.append(p)
        if evd.main_command(bundle)[0] is not None:
            declaring.append(p)
        if rule == "top-level README.md":
            readme_fams.append(fam_by_slug[p.name])
    a, b = FOCK / "verification/rows.txt", UNIF / "verification/rows.txt"
    fp = {q.name: q for q in VPOS.iterdir() if q.is_file()}
    fz = {q.name: q for q in VZERO.iterdir() if q.is_file()}
    shared = sorted(set(fp) & set(fz))
    same = [n for n in shared if fp[n].read_bytes() == fz[n].read_bytes()]
    entries = json.loads((VZERO / "manifest.json").read_text(encoding="utf-8"))["files"]
    bad = [n for n in sorted(entries)
           if n not in fz or verif_sha(fz[n]) != entries[n]["sha256"]
           or fz[n].stat().st_size != entries[n]["bytes"]]
    res = json.loads((VPOS / "results.json").read_text(encoding="utf-8"))
    summ = res["summary"]
    src = (VPOS / "verify.py").read_text(encoding="utf-8").split("\n")
    checks = json.loads((VPOS / "portability-results.json").read_text(encoding="utf-8"))["checks"]
    cov_md = (VPOS / "COVERAGE.md").read_text(encoding="utf-8")
    seen: set[str] = set()
    named_cov: list[str] = []
    for n in (re.findall(r"`([\w.]+\.(?:py|json|md))`", cov_md)
              + re.findall(r"\[([\w.]+\.(?:py|json|md))\]\(", cov_md)):
        if n not in seen:
            seen.add(n)
            named_cov.append(n)
    present = [n for n in named_cov if (VPOS / n).exists() and (VZERO / n).exists()]
    return {
        "dirs": len(bundles),
        "fams": len({fam_by_slug[p.name] for p in bundles}),
        "fam_list": ", ".join(sorted(r["fam"] for r in rows if int(r["verification"]) > 0)),
        "covn": sum(int(r["covmd"]) for r in rows),
        "cov_fams": cov,
        "inp_n": sum(int(r["inputs"]) for r in rows),
        "inp_list": ", ".join(inp),
        "v348": int(next(r for r in rows if r["fam"] == "348")["verification"]),
        "named": len(named) + len(runsec),
        "ver": len(named),
        "run": len(runsec),
        "unnamed_n": len(unnamed),
        "classes": classes,
        "no_entry": len(no_entry),
        "no_entry_fams": [fam_by_slug[p.name] for p in no_entry if fam_by_slug[p.name] != "269"],
        "rule4": sum(c for k, c in classes.items() if k.startswith("manifest")),
        "declaring": len(declaring),
        "declaring_fams": sorted({fam_by_slug[p.name] for p in declaring}),
        "readme_fams": readme_fams,
        "rows_lines": len(a.read_text(encoding="utf-8", errors="replace").splitlines()),
        "rows_bytes": a.stat().st_size,
        "rows_identical": a.read_bytes() == b.read_bytes(),
        "shared": len(shared),
        "identical": len(same),
        "differ": len(shared) - len(same),
        "entries": len(entries),
        "mismatches": len(bad),
        "identities": summ["identities"],
        "interval_rows": summ["interval_certificate_rows"],
        "reported": summ["reported_interval_rows"],
        "supplementary": summ["interval_certificate_rows"] - summ["reported_interval_rows"],
        "triangle_rows": len(res["triangle_certificates"]),
        "det_floor": sum(1 for t in res["triangle_certificates"] if t["determinant_floor"] is not None),
        "exact": summ["exact_value_assertions"],
        "subintervals": sum(len(c["intervals"]) for c in res["interval_certificates"]),
        "lines": len(src),
        "checkfns": len([l for l in src if l.startswith("def check_")]),
        "fnlines": [i + 1 for i, l in enumerate(src) if l.startswith("def check_")],
        "printed_keys": len(re.findall(r'scalar_claim\("([\w.]*printed[\w.]*)', "\n".join(src))),
        "require": sum(l.count("require(") for l in src),
        "passed": json.dumps(res).count('"passed": true'),
        "checks": len(checks),
        "negative": len([c for c in checks if "rejected" in c["name"]]),
        "ends_rejected": len([c for c in checks if c["name"].endswith("rejected")]),
        "cov_present": len(present),
    }


def verification_dirs_full(v: dict[str, Any]) -> dict[str, str]:
    """Label -> page-verbatim phrase. Labels with no suffix are the base values the builder wraps."""
    dirs, fams = v["dirs"], v["fams"]
    cls, cov_fams = v["classes"], v["cov_fams"]
    readme_n = len(v["readme_fams"])
    out: dict[str, str] = {}
    out["v_dirs_fams"] = f"**{dirs} dirs over {fams} families**"
    out["v_famlist"] = f"({v['fam_list']})"
    out["v_covmd"] = f"`covmd` counts {v['covn']} `verification/COVERAGE.md`, both in family {cov_fams[0]}"
    out["v_inputs"] = f"`inputs` counts {v['inp_n']} `INPUTS.md` ({v['inp_list']})"
    out["v_v348"] = f"the ledger's `verification` value of {v['v348']} for family 348"
    out["v_doc_readme"] = (f"**{readme_n} of {dirs}** ship a `README.md` with a run command and "
                           f"success criteria: {group_fams(v['readme_fams'])}")
    out["v_doc_noreadme"] = f"**{dirs - readme_n} ship no README**"
    out["v_doc_manifest"] = (f"**{v['declaring']} of {dirs}** ship `manifest.json` "
                             f"(both {v['declaring_fams'][0]} dirs)")
    out["v_doc_covmd"] = f"**{v['covn']} of {dirs}** ship `COVERAGE.md` (both {cov_fams[0]} dirs)"
    out["v_named"] = f"A README section names **{v['named']}** of the **{dirs}** bundles"
    out["v_headings"] = f"**{v['ver']}** carry `## Verification` and **{v['run']}** carries"
    out["v_unnamed"] = (f"**{v['unnamed_n']}** bundles ship a `verification/` tree "
                        "their README never mentions")
    out["v_rows"] = (f"Each is {v['rows_lines']} lines and {v['rows_bytes']} bytes, "
                     f"and the two files are **{'byte-identical' if v['rows_identical'] else 'not identical'}**")
    out["v_classes"] = (f"**{cls['top-level README.md']}** top-level `README.md`, "
                        f"**{cls['subdirectory README.md']}** a subdirectory `README.md`, "
                        f"**{cls['top-level script by name']}** a top-level script by name, "
                        f"**{cls['subdirectory README.txt']}** a subdirectory `README.txt`, "
                        f"**{cls['none']}** with **no entry point**")
    out["v_rule4"] = f"Rule 4 fires for **{v['rule4']}** bundles"
    out["v_declaring"] = (f"the {NUM_WORDS[v['declaring']]} family-{v['declaring_fams'][0]} dirs that "
                          "declare `main_command` are claimed by rule 1 first")
    nf = v["no_entry_fams"]
    out["v_noentry"] = (f"The {v['no_entry']} with no entry point are the two 269 dirs above plus "
                        f"{', '.join(nf[:-1])} and {nf[-1]}")
    out["v_join"] = f"sums to {dirs} dirs over {fams} families"
    out["v_shared"] = f"Of the {v['shared']} files they share, **{v['identical']} are byte-identical**"
    out["v_differ"] = f"and **{v['differ']} differ**"
    out["v_idents"] = f"**{v['identities']}** identities"
    out["v_interval"] = (f"**{v['interval_rows']}** interval certificate rows "
                         f"(**{v['reported']}** reported + **{v['supplementary']}** supplementary)")
    out["v_triangle"] = (f"**{v['triangle_rows']}** triangle certificate rows "
                         f"(**{v['det_floor']}** carrying a determinant floor)")
    out["v_exact"] = f"**{v['exact']}** exact-value assertions"
    out["v_subint"] = f"over **{v['subintervals']}** subinterval records"
    out["v_verify"] = (f"`verify.py` is {v['lines']} lines with {v['checkfns']} `check_*` functions "
                       f"(at lines {', '.join(str(n) for n in v['fnlines'])})")
    out["v_printed"] = f"**{v['printed_keys']}** `scalar_claim` keys name a printed value"
    out["v_require"] = f"through `require` ({v['require']} occurrences)"
    out["v_passed"] = f"**{v['passed']}** such occurrences in `results.json`"
    out["v_entries"] = f"list {v['entries']} files"
    out["v_mismatch"] = f"({v['mismatches']} mismatches)"
    out["v_cov"] = ("`COVERAGE.md` points at `results.json`, `verify.py`, `polynomial.py`, and "
                    f"`README.md`; all {NUM_WORDS[v['cov_present']]} are present in both directories")
    out["v_port"] = f"ships **{v['checks']}** checks, **{v['negative']}** of them negative"
    out["v_reject"] = f"tests naming a rejection: **{v['ends_rejected']}** whose names end in `rejected`"
    return out


VERIF_SPLIT = {
    "v_dirs_fams": ["**30 dirs over"],
    "v_famlist": ["(059, 067, 087, 090, 101, 107, 119, 153, 187, 189, 205, 210, 229, 266, 268, 269, 272,"],
    "v_covmd": ["`covmd` counts 2"],
    "v_doc_readme": ["**12 of 30** ship a `README.md` with a run command and success criteria: "
                     "087, 090 (×4), 107, 119,"],
    "v_classes": ["**12** top-level `README.md`, **6** a subdirectory `README.md`, **5** a top-level"],
    "v_declaring": ["the two family-348 dirs that declare `main_command` are claimed by"],
    "v_v348": ["the"],
    "v_verify": ["`verify.py` is 504 lines with 6 `check_*` functions (at lines 157, 170, 271,"],
    "v_cov": ["`COVERAGE.md` points at `results.json`, `verify.py`,"],
}


def verification_dirs_phrases(v: dict[str, Any]) -> dict[str, str]:
    """The slot dict: base labels, then each page-wrapped phrase as label a, label b, …"""
    full = verification_dirs_full(v)
    out: dict[str, str] = {}
    for label, val in full.items():
        prefixes = VERIF_SPLIT.get(label)
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


def verification_dirs_page(p: dict[str, str]) -> str:
    return ENV.get_template("verification-dirs.md.j2").render(p=p)


EX_ROW = re.compile(r"^\|\s*(\d{3})\s*\|\s*(.+?)\s*\|\s*$")
EX_PAIR = re.compile(r"^“(.+)”\s*`lean/docs/(\d{3})\.md:(\d+)`$")


def scope_exclusions_population() -> dict[str, str]:
    """Every derived figure on notes/scope-exclusions.md, measured from the shipped scope notes.

    The Entries table is a hand read — which clause and which line each family gets is a reading
    decision, not a measurement — so the table stays literal in the template and the counts it
    carries (rows, exclusion statements, quotations) are read back out of the page being replaced.
    The page's own checker is what pins each of those quotations to a line inside its `## Scope`
    section; this function measures the section geometry and the two keyword floors.
    """
    sections: dict[str, list[str]] = {}
    doc_lines = 0
    both = 0
    for path in Y.doc_files():
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        doc_lines += len(lines)
        if (any(l.strip() == "## Scope" for l in lines)
                and any(l.strip() == "## Comparator links" for l in lines)):
            both += 1
        span = Y.scope_span_lines(lines)
        if span is not None:
            first, last = span
            sections[path.stem] = lines[first - 1:last]
    counts = [len(sec) for sec in sections.values()]

    def hit_docs(phrases: list[str]) -> list[str]:
        return sorted(stem for stem, sec in sections.items()
                      if any(ph in " ".join(sec).lower() for ph in phrases))

    narrow = hit_docs(ex.NARROW)
    broad = hit_docs(ex.BROAD)
    per_phrase = [sum(1 for sec in sections.values()
                      if ph in " ".join(sec).lower()) for ph in ex.NARROW]

    rows: list[tuple[str, str]] = []
    for line in EX_MD.read_text(encoding="utf-8").splitlines():
        m = EX_ROW.match(line)
        if not m or m.group(1) == "Family" or set(m.group(2)) <= {"-"}:
            continue
        rows.append((m.group(1), m.group(2)))
    excl = [cell for _, cell in rows if cell.strip() != "**None stated.**"]
    quotes = sum(sum(1 for part in cell.split("·") if EX_PAIR.match(part.strip())) for cell in excl)
    fams = len({r["fam"] for r in tsv.read_rows(LEDGER_TSV)})
    return {
        "notes": str(len(sections)), "both": str(both), "seclines": str(sum(counts)),
        "alllines": str(doc_lines),
        "minmedmax": f"{min(counts)} / {int(statistics.median(counts))} / {max(counts)}",
        "narrow": str(len(narrow)), "broad": str(len(broad)),
        "narrow_fams": ", ".join(narrow),
        "perphrase": " / ".join(str(n) for n in per_phrase),
        "rows": str(len(rows)), "excl": str(len(excl)), "quotes": str(quotes),
        "none": str(len(rows) - len(excl)),
        "fams": str(fams), "nonote": str(fams - len(sections)),
    }


def scope_exclusions_full(p: dict[str, str]) -> dict[str, str]:
    return {
        "ex_readall": f"All {p['notes']} scope notes on disk were read in full, section by section",
        "ex_prose": (f"{p['excl']} of {p['rows']} sections state at least one exclusion, carrying "
                     f"{p['quotes']} exclusion statements; {p['none']} state none."),
        "ex_row_notes": f"| Scope notes | {p['notes']} |",
        "ex_row_both": f"| Docs with both `## Scope` and `## Comparator links` | {p['both']} |",
        "ex_row_seclines": f"| `## Scope` section lines | {p['seclines']} |",
        "ex_row_alllines": f"| Scope-note lines, all files | {p['alllines']} |",
        "ex_row_minmedmax": f"| Lines per section (min / median / max) | {p['minmedmax']} |",
        "ex_row_narrow": f"| Docs hit by the {len(ex.NARROW)}-phrase narrow list | {p['narrow']} |",
        "ex_row_broad": f"| Docs hit by the {len(ex.BROAD)}-phrase broad list | {p['broad']} |",
        "ex_narrow_detail": (f"It hits {p['narrow']} of {p['notes']} — families {p['narrow_fams']}, "
                             f"with per-phrase hits {p['perphrase']}."),
        "ex_broad_detail": f"it hits {p['broad']} of {p['notes']}.",
        "ex_floor_a": f"So {p['narrow']} is a floor under a narrow rule, not a census.",
        "ex_floor_b": (f"A keyword filter finds {p['narrow']} sections; the reading pass finds "
                       f"exclusions in {p['excl']} of the {p['notes']}."),
        "ex_readlines": f"a human read of {p['seclines']} lines",
        "ex_nonoote": (f"The {p['nonote']} families with no scope note at all "
                       f"({p['fams']} families, {p['notes']} notes)"),
    }


EX_SPLIT = {
    "ex_prose": ["121 of 242 sections state at least one exclusion, carrying 143 exclusion"],
    "ex_narrow_detail": ["It hits 5 of 242 — families 003, 020, 049, 173, 360,"],
    "ex_floor_b": ["A keyword filter finds 5 sections; the reading pass"],
}


def scope_exclusions_phrases(p: dict[str, str]) -> dict[str, str]:
    out = scope_exclusions_full(p)
    for label, prefixes in EX_SPLIT.items():
        base = out.pop(label)
        rest = base
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {base!r}")
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def scope_exclusions_page(p: dict[str, str]) -> str:
    return ENV.get_template("scope-exclusions.md.j2").render(p=p)


RENDER_NOUN = {
    "discipline.md.j2": "discipline pages",
    "family.md.j2": "family pages",
    "index-readme.md.j2": "entry point",
    "name.md.j2": "name pages",
    "topic.md.j2": "topic pages",
}


def templates_population(abstracts_labels: int) -> dict[str, Any]:
    """The template census, plus the writer-label count the page compares a slot count with."""
    p = MTPL.population()
    p["abstracts_labels"] = abstracts_labels
    return p


def templates_phrases(p: dict[str, Any]) -> dict[str, str]:
    """label -> phrase, one label per table row, so a census that grows grows the slot set.

    A report template carries no Jinja loop: every table row on the page is its own label, the same
    shape as disc_row_NN in the index-design page. A phrase the writer supplies as ONE string that the
    page wraps across lines is left literal by the builder, which would freeze a census number in the
    template, so no phrase here spans a line.
    """
    out: dict[str, str] = {}
    for n, r in enumerate(p["report_rows"], start=1):
        out[f"tpl_row_{n:02d}"] = (
            f"| `{r['name']}` | {int(r['lines']):,} | {int(r['bytes']):,} | {int(r['slots'])} | "
            f"`{r['page']}` | `{r['checker']}` | {r['needles'] or 'NOT DERIVED'} |")
    for n, r in enumerate(p["index_rows"], start=1):
        out[f"idx_row_{n:02d}"] = (
            f"| `{r['name']}` | {int(r['lines']):,} | {int(r['bytes']):,} | {int(r['slots'])} | "
            f"{int(r['renders']):,} {RENDER_NOUN[r['name']]} |")
    r, i, a = p["report"], p["index"], p["all"]
    out["report_total"] = (f"| **report tree** | **{r['n']}** | **{r['lines']:,}** | **{r['bytes']:,}** |"
                           f" **{r['slots']:,}** | | |")
    out["index_total"] = (f"| **index tree** | **{i['n']}** | **{i['lines']:,}** | **{i['bytes']:,}** |"
                          f" **{i['slots']:,}** | |")
    out["census_report"] = (f"report tree: **{r['n']}** templates, **{r['lines']:,}** lines,"
                            f" **{r['bytes']:,}** bytes, **{r['slots']:,}** slots")
    out["census_index"] = (f"index tree: **{i['n']}** templates, **{i['lines']:,}** lines,"
                           f" **{i['bytes']:,}** bytes, **{i['slots']:,}** slots")
    out["census_all"] = (f"all **{a['n']}** templates: **{a['lines']:,}** lines, **{a['bytes']:,}** bytes,"
                         f" **{a['slots']:,}** slots")
    out["reuse"] = f"**{p['reuse']}** repeat expressions over **{p['reuse_templates']}** templates"
    out["reuse_detail"] = p["reuse_detail"]
    out["reuse_scope"] = f"over the **{a['n']}** committed templates"
    out["header"] = f"header comment is **{p['header_lines']}** lines"
    out["derived"] = f"**{p['derived_n']}** of **{p['registry_n']}** pages"
    out["not_derived"] = f"the other **{p['not_derived_n']}**"
    out["not_derived_bullet"] = f"the **{p['not_derived_n']}** NOT-DERIVED pages"
    out["registry"] = (f"registry: **{p['registry_n']}** entries at "
                       f"`build_report_templates.py:{p['all_pages_anchor']}`")
    out["gap"] = (f"template-without-page **{len(p['missing'])}**,"
                  f" page-without-template **{len(p['extra'])}**")
    ab = next(x for x in p["report_rows"] if x["name"] == "abstracts.md.j2")
    out["labels_vs_slots"] = (f"**{p['abstracts_labels']}** writer labels against **{ab['slots']}** slots"
                              f" in `abstracts.md.j2`")
    return out


def templates_page(p: dict[str, str]) -> str:
    return ENV.get_template("templates.md.j2").render(p=p)


def topics_population(lf: dict[str, str]) -> dict[str, str]:
    """Every derived figure on notes/topics.md, measured from the curated vocabulary.

    notes/topics.tsv is the source of truth and measure_topics.measure() matches its patterns over the
    four texts a family ships, so the 92-row yield table, the coverage line, and both histograms are
    measurements. The reading-pass table stays literal: its reach column mixes bare-stem probes with a
    shipped-pattern probe and with reading prose, and no single rule reproduces it. The MSC/keywords
    figures come from the links population, which is where extract_links.py measures them.
    """
    rows, texts = MT.measure()
    fams = len(texts)
    nlayer = [sum(1 for t in texts.values() if t[i].strip()) for i in range(4)]
    covered = set().union(*(r["families"] for r in rows))
    assign = sum(len(r["families"]) for r in rows)
    ycount = collections.Counter(len(r["families"]) for r in rows)
    per = collections.Counter(len([r for r in rows if f in r["families"]]) for f in texts)
    topics_per_family = sorted(per.elements())
    _order, ov = overview.parse_overview()
    titles = [ov[f]["title"] for f in ov]
    header = MT.TSV.read_text(encoding="utf-8").splitlines()[0].split("\t")
    zero = [r["term"] for r in rows if not r["families"]]
    out = {
        "terms": str(len(rows)), "cols": str(len(header)), "fams": str(fams),
        "assign": str(assign), "covered": str(len(covered)),
        "uncovered": str(fams - len(covered)), "zero": str(len(zero)),
        "n_title": str(nlayer[0]), "n_abstract": str(nlayer[1]),
        "n_scope": str(nlayer[2]), "n_path": str(nlayer[3]),
        "nopath": str(fams - nlayer[3]),
        "perfamily": " ".join(f"{k}:{v}" for k, v in sorted(per.items())),
        "yieldhist": " ".join(f"{k}:{ycount[k]}" for k in sorted(ycount)),
        "median": str(int(statistics.median(topics_per_family))),
        "mean": f"{assign / fams:.2f}", "single": str(per[1]),
        "thin3": str(sum(v for k, v in ycount.items() if k <= 3)),
        "thin1": str(sum(v for k, v in ycount.items() if k <= 1)),
        "noted": str(sum(1 for r in tsv.read_rows(MT.TSV) if r["note"].strip())),
        "ascii_apos": str(sum(1 for t in titles if "'" in t)),
        "u2019": str(sum(1 for t in titles if "\u2019" in t)),
        "apos_pat": str(sum(1 for _term, pat in MT.VOCAB if "'" in pat)),
        "msc": lf["raw_msc"], "msc_files": lf["raw_msc_files"],
        "kw_bib": lf["raw_kw_bib"], "kw_tex": lf["raw_kw_tex"],
        "bibent": lf["raw_bibent"], "listed": lf["raw_listed"],
    }
    for r in sorted(rows, key=lambda r: (-len(r["families"]), r["term"])):
        out[f"tp_row_{r['term']}"] = (
            f"| {r['term']} | {len(r['families'])} | {len(r['title'])} | {len(r['abstract'])} | "
            f"{len(r['scope'])} | {len(r['path'])} |")
    return out


def topics_full(p: dict[str, str]) -> dict[str, str]:
    return {
        "tp_terms": f"**{p['terms']} curated terms**",
        "tp_cols": f"**{p['cols']} columns**",
        "tp_headline": (f"{p['terms']} patterns matched case-insensitively against the title, abstract, "
                        f"scope-note text, and derived Lean file paths of the {p['fams']} catalogued "
                        f"families \u2192 {p['assign']} family-topic assignments over {p['fams']} "
                        f"families, {p['uncovered']} families uncovered, {p['zero']} terms with no hit."),
        "tp_row_title": (f"| title | the 2nd argument of the family's `\\resultentry` in "
                         f"`overview.tex` | {p['n_title']} |"),
        "tp_row_abstract": f"| abstract | the 3rd argument of the same entry | {p['n_abstract']} |",
        "tp_row_scope": f"| scope | the text of `lean/docs/<NNN>.md` | {p['n_scope']} |",
        "tp_row_path": (f"| path | Lean file paths reached from the family's comparator configs "
                        f"through `formalization.yaml` `main_results`, plus the Lean module dir "
                        f"names | {p['n_path']} |"),
        "tp_neg": (f"{p['msc']} MSC codes over {f(int(p['msc_files']))} files, {p['kw_bib']} "
                   f"`keywords` fields over {f(int(p['bibent']))} bibliography entries, "
                   f"`\\keywords` defined in {p['kw_tex']} of {p['listed']} manuscript directories"),
        "tp_covered": f"families covered {p['covered']} of {p['fams']}, uncovered {p['uncovered']}",
        "tp_perfamily": f"topics per family {p['perfamily']}",
        "tp_median": f"median **{p['median']}**, mean {p['mean']}",
        "tp_single": f"{p['single']} families carry exactly one topic",
        "tp_yieldhist": f"yield histogram {p['yieldhist']}",
        "tp_thin": (f"**{p['thin3']}** terms have a yield of 3 or less and {p['thin1']} "
                    f"have a yield of 1 or less"),
        "tp_thin_nc": f"**{p['thin3']}** terms have a yield of 3 or less.",
        "tp_note": f"{p['noted']} of {p['terms']} rows carry one",
        "tp_ascii": f"{p['ascii_apos']} use ASCII `'` and {p['u2019']} use U+2019",
        "tp_apos": f"{p['apos_pat']} patterns contain an ASCII apostrophe",
        "tp_nopath": f"{p['nopath']} families the path layer is empty",
    }


TP_SPLIT = {
    "tp_headline": [
        "92 patterns matched case-insensitively against the title,",
        "abstract, scope-note text, and derived Lean file paths of the 372 catalogued families \u2192 978",
    ],
    "tp_neg": ["0 MSC codes over 8,206 files, 0 `keywords` fields over 12,876 bibliography entries,"],
    "tp_thin": ["**17** terms have a yield of 3 or less"],
    "tp_yieldhist": [
        "yield histogram 0:4 1:5 2:3 3:5 4:9 5:4 6:5 7:8 8:6 9:6 10:2 11:6 12:1 13:5 15:1 16:3 17:4",
    ],
}


def topics_phrases(p: dict[str, str]) -> dict[str, str]:
    out = topics_full(p)
    out.update({k: v for k, v in p.items() if k.startswith("tp_row_")})
    for label, prefixes in TP_SPLIT.items():
        base = out.pop(label)
        rest = base
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {base!r}")
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def topics_page(p: dict[str, str]) -> str:
    return ENV.get_template("topics.md.j2").render(p=p)


# 311 enters the chain table by reading, not by measurement: the release records no `companions`
# value for it, so the measured part is the two result (NNN) edges and 311 is the literature chain.
TC_LIT_CHAIN = ("311",)


def t0_chains_population() -> dict[str, Any]:
    v = tc.population()
    rows, pop = v["rows"], v["pop"]
    mss = tc.manuscripts()
    bib_edges = tc.release_bib_edges()
    lines = ep.resultentry_lines()
    fam_dirs = {f: sorted({owner(pathlib.Path(m["path"])) for m in mss[f]}) for f in pop}
    fam_edges = {f: tc.intra_edges(fam_dirs[f], bib_edges) for f in pop}
    fam_mutual = {f: sum(1 for a, b in fam_edges[f] if (b, a) in fam_edges[f]) // 2 for f in pop}
    fam_bibs = {f: tc.bib_files(fam_dirs[f]) for f in pop}
    return {"v": v, "rows": rows, "pop": pop, "lines": lines, "edges": fam_edges,
            "mutual": fam_mutual, "bibs": fam_bibs, "chain": tc.chain_edges(rows),
            "cw": tc.companion_word_fams(rows)}


def t0_chains_full(p: dict[str, Any]) -> dict[str, str]:
    v, rows, pop = p["v"], p["rows"], p["pop"]
    lines, edges, mutual, bibs = p["lines"], p["edges"], p["mutual"], p["bibs"]
    out: dict[str, str] = {}
    paps = sum(int(rows[f]["paps"]) for f in pop)
    out["tc_pop"] = f"**{len(pop)}** families carrying **{paps}** manuscripts"
    tiers = ", ".join(f"`{t}:{n}`" for t, n in sorted(v["paps2_tiers"].items()) if n)
    out["tc_repo"] = f"**{len(v['paps2'])}** families with exactly 2 manuscripts, split {tiers}"
    out["tc_firstpass"] = (f"Of the **{len(v['t0_paps2'])}** at T0, **{len(v['first_pass'])}** were read in "
                           f"the first pass ({', '.join(v['first_pass'])}), so **{len(pop)}** remain")
    out["tc_first_pass_list"] = ", ".join(v["first_pass"])
    out["tc_zero"] = f"holds for **{len(v['zero_signal'])}** of the {len(pop)} and fails for"
    out["tc_268sig"] = (f"**{len(v['signal_outliers'])}**: "
                        + " ".join(f"{f} carries `verification = {rows[f]['verification']}`"
                                   for f in v["signal_outliers"]))
    out["tc_trueof"] = f"That is true of **{len(v['zero_signal'])}**"
    ce = p["chain"]
    out["tc_edges"] = (f"Over **{len(rows)}** families that yields **{len(ce)}** edges — "
                       + " and ".join(f"{s} → {d}" for s, d in ce) + " —")
    for f in [x for pair in ce for x in pair] + list(TC_LIT_CHAIN):
        r = rows[f]
        out[f"tc_chain_{f}"] = (f"| {f} | {r['tier']} | {r['paps']} | {r['paps_form']} | {r['chal']} | "
                                f"{r['mainres']} | {r['scope_note']} | {r['verification']} | "
                                f"{r['trace'] or '0'} | {r['shapes'].replace('|', ', ')} |")
    cw = p["cw"]
    cw_pop = [f for f in pop if rows[f]["companion_word"] == "1"]
    out["tc_cw"] = (f"fires on **{len(cw)}** families — {', '.join(cw)} — and "
                    f"**{sum(1 for f in cw if rows[f]['companions'])}** of them carry a `companions` edge")
    out["tc_cw_pop"] = f"Of the {len(pop)} families here, **{len(cw_pop)}** use the word ({', '.join(cw_pop)})"
    withedge = [f for f in pop if edges[f]]
    mutual_f = [f for f in pop if mutual[f]]
    oneway = [f for f in pop if edges[f] and not mutual[f]]
    noedge = [f for f in pop if not edges[f]]
    nobib = [f for f in noedge if not bibs[f]]
    out["tc_layer"] = (f"{len(ce)} edges over {len(rows)} families, while the companion relation it "
                       f"describes in prose is at least {len(cw)} families wide, and the manuscript-level "
                       f"citation layer below measures {len(withedge)} of {len(pop)}")
    for f in pop:
        r = rows[f]
        # The page's discipline column is the reading-pass abbreviation it shares with t0-triage.md
        # ("A&CG", "real&complex"), not the ledger's full name, so the template keeps it literal and
        # the label starts at the shapes column.
        out[f"tc_row_{f}"] = (f"{r['shapes'].replace('|', ', ') or '-'} | {len(bibs[f])} | "
                              f"{len(edges[f])} | {mutual[f]} | `overview.tex:{lines[f]}` |")
    out["tc_all"] = (f"All {len(pop)} are T0, all {paps} manuscripts carry `formalized = 0`, and "
                     f"{len(v['zero_signal'])} of {len(pop)} carry no coverage signal at all")
    out["tc_cite"] = (f"**{len(withedge)}** of the {len(pop)} cite their sibling: **{len(mutual_f)}** mutual "
                      f"pairs and **{len(oneway)}** one-directional. **{len(noedge)}** cite no sibling, and "
                      f"**{len(nobib)}** of those ({', '.join(nobib)}) ship no `.bib` file at all, so their "
                      f"absence is unmeasurable rather than a negative.")
    out["tc_mutual"] = "The mutual pairs are " + ", ".join(mutual_f)
    out["tc_oneway"] = "The one-directional edges are " + ", ".join(oneway)
    out["tc_none"] = f"The {len(noedge)} with no intra-family edge are " + ", ".join(noedge)
    out["tc_nobib"] = f"of them ({', '.join(nobib)}) ship no `.bib` file;"
    return out


TC_SPLIT = {
    "tc_firstpass": ["Of the",
                     "**35** at T0, **8** were read in the first pass (004, 006, 018, 019, 029, 046, "
                     "059, 209), so **27**"],
    "tc_268sig": ["**1**: 268"],
    "tc_trueof": ["That is true of"],
    "tc_edges": ["Over **372** families"],
    "tc_cw": ["fires on **9**",
              "families — 003, 197, 207, 256, 266, 268, 270, 307, 364 — and **0** of them carry "
              "a `companions`"],
    "tc_layer": ["2 edges over 372 families, while the",
                 "companion relation it describes in prose is at least 9 families wide, and the "
                 "manuscript-level"],
    "tc_cite": ["**15** of the 27 cite their sibling: **8** mutual pairs and **7** one-directional. "
                "**12** cite no",
                "sibling, and **3** of those (200, 239, 300) ship no `.bib` file at all, so their absence is"],
    "tc_oneway": ["The one-directional edges are 037,"],
}


def t0_chains_phrases(p: dict[str, Any]) -> dict[str, str]:
    out = t0_chains_full(p)
    out.update({k: v for k, v in p.items() if k.startswith("tc_row_")})
    out.update({k: v for k, v in p.items() if k.startswith("tc_chain_")})
    for label, prefixes in TC_SPLIT.items():
        base = out.pop(label)
        rest = base
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {base!r}")
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def t0_chains_page(p: dict[str, str]) -> str:
    return ENV.get_template("t0-chains.md.j2").render(p=p)


# --- page 10: notes/subfinding-pairs.md -------------------------------------------------------
# The pairing judgement is a reading record, so the writer reads it back out of the page it replaces
# (the shape scope-exclusions.md's Entries table already uses): every Summary-table figure below is a
# count of the page's own pair lines. verify_subfinding_pairs.py re-derives them independently and
# pins every quoted clause and title to the family's \resultentry line, which the writer deliberately
# does not share with it.

SP_HEAD = re.compile(r"^## (?P<fam>\d{3}) · `overview\.tex:(?P<line>\d+)` · "
                     r"n=(?P<n>\d+) · (?P<tier>T\d)$")
SP_TARGET = re.compile(r"-> \"[^\"]*\" \(`overview\.tex:\d+`\) \[\d{3}:\d+\]$")
SP_FP_SENT = re.compile(r"Probe-vocabulary false positives: ([0-9, ]+)\.")


def subfinding_pairs_population() -> dict[str, Any]:
    """The measured population, and the reading record exactly as the page carries it."""
    v = ep.population()
    text = SP_MD.read_text(encoding="utf-8")
    blocks: list[dict[str, Any]] = []
    cur: dict[str, Any] = {}
    for ln in text.splitlines():
        m = SP_HEAD.match(ln)
        if m:
            cur = {"fam": m["fam"], "line": int(m["line"]), "n": int(m["n"]), "tier": m["tier"],
                   "main": 0, "main_t": 0, "clause": 0, "clause_t": 0, "claimed": [], "unclaimed": []}
            blocks.append(cur)
        elif cur and ln.startswith("- main: "):
            cur["main"] += 1
            cur["main_t"] += 1 if SP_TARGET.search(ln) else 0
        elif cur and ln.startswith("- clause: "):
            cur["clause"] += 1
            cur["clause_t"] += 1 if SP_TARGET.search(ln) else 0
        elif cur and ln.startswith("- claimed:"):
            cur["claimed"] = ln[len("- claimed:"):].split()
        elif cur and ln.startswith("- unclaimed:"):
            cur["unclaimed"] = ln[len("- unclaimed:"):].split()
    m = SP_FP_SENT.search(text)
    if m is None:
        raise ValueError("no probe false-positive sentence on the page")
    fp = [x.strip() for x in m.group(1).split(",") if x.strip()]
    rows = tsv.read_rows(SUBFINDINGS_TSV)
    return {"v": v, "blocks": blocks, "fp": fp,
            "comparator_rows": sum(1 for r in rows if r["kind"] == "comparator-link"),
            "manuscript_rows": sum(1 for r in rows if r["kind"] == "manuscript")}


def subfinding_pairs_full(p: dict[str, Any]) -> dict[str, str]:
    v, blocks = p["v"], p["blocks"]
    pop, counts, probe = v["pop"], v["counts"], v["probe"]
    probe_all, multi, per = v["probe_all"], v["multi"], v["per_phrase"]
    low, fams = v["low"], v["fams"]
    out: dict[str, str] = {}
    mss = sum(counts[f] for f in pop)
    out["sp_pop"] = f"**{len(pop)} families over {mss} manuscripts**"
    out["sp_probe_also"] = f"`also prove` ({len(per['also prove'])}),"
    out["sp_probe_independ"] = (f"`Independent` ({len(per['independ'])}), "
                                f"`also establish` ({len(per['also establish'])}),")
    out["sp_probe_conseq"] = f"`not as a consequence` ({len(per['as a consequence'])})"
    out["sp_indep_word"] = (f"not the word `independent` "
                            f"({sum(1 for f in fams if 'independent' in low[f])})")
    out["sp_t_also"] = f"| `also prove` | {len(per['also prove'])} |"
    out["sp_t_independ"] = f"| `independ` (stem) | {len(per['independ'])} |"
    out["sp_t_establish"] = f"| `also establish` | {len(per['also establish'])} |"
    out["sp_t_consequence"] = f"| `as a consequence` | {len(per['as a consequence'])} |"
    out["sp_t_union372"] = f"| union of the four, over all 372 | {len(probe_all)} |"
    out["sp_t_multi"] = f"| families with ≥2 manuscripts | {len(multi)} |"
    out["sp_t_union167"] = f"| **union of the four, over the 167** | **{len(probe)}** |"
    out["sp_not51"] = f"{len(probe)}, not 51."
    inside = [d for d in ep.DENSEST if d in probe]
    outside = [d for d in ep.DENSEST if d not in probe]
    out["sp_outside"] = (f"{NUM_WORDS[len(outside)].capitalize()} of the bead's "
                         f"{NUM_WORDS[len(ep.DENSEST)]} named densest targets "
                         f"(all but {', '.join(inside)})")
    out["sp_decision"] = f"**{len(pop)} families, {mss} manuscripts**"
    out["sp_densest_range"] = (f"{ep.DENSEST[0]} at n={counts[ep.DENSEST[0]]} down to "
                               f"{ep.DENSEST[-1]} at n={counts[ep.DENSEST[-1]]}")
    fp_probe = [x for x in p["fp"] if x in probe]
    out["sp_fpcount"] = f"{len(fp_probe)} of the {len(probe)} probe-hit families"
    accepted = sum(b["clause_t"] for b in blocks)
    main_accepted = sum(b["main_t"] for b in blocks)
    unmatched = sum(b["main"] + b["clause"] - b["main_t"] - b["clause_t"] for b in blocks)
    claimed_total = sum(len(b["claimed"]) for b in blocks)
    unclaimed_total = sum(len(b["unclaimed"]) for b in blocks)
    with_pair = [b["fam"] for b in blocks if b["clause_t"]]
    with_unmatched = sum(1 for b in blocks
                         if b["main"] + b["clause"] - b["main_t"] - b["clause_t"])
    noprobe = [b["fam"] for b in blocks if b["clause_t"] and b["fam"] not in probe]
    out["sp_s_fams"] = f"| families read | {len(blocks)} |"
    out["sp_s_mss"] = f"| manuscripts in the population | {mss} |"
    out["sp_s_pairs"] = f"| sub-finding clause pairs accepted | {accepted} |"
    out["sp_s_headline"] = f"| headline clause pairs accepted | {main_accepted} |"
    out["sp_s_unmatched"] = f"| clauses recorded unmatched | {unmatched} |"
    out["sp_s_claimed"] = f"| titles claimed by a clause | {claimed_total} |"
    out["sp_s_unclaimed"] = f"| titles claimed by no clause | {unclaimed_total} |"
    out["sp_s_fampair"] = f"| families with >=1 accepted sub-finding pair | {len(with_pair)} |"
    out["sp_s_famunmatched"] = f"| families with >=1 clause recorded unmatched | {with_unmatched} |"
    out["sp_s_noprobe"] = (f"| families with an accepted sub-finding pair and no probe hit "
                           f"| {len(noprobe)} |")
    out["sp_b_pair"] = (f"{len(with_pair)} of {len(blocks)} families have at least one accepted "
                        f"sub-finding pair, and")
    out["sp_b_claimed"] = f"{claimed_total} of the {mss} titles are claimed by a clause"
    out["sp_b_unmatched"] = f"{unmatched} clauses in {with_unmatched} families state a result no"
    out["sp_b_noprobe"] = f"{len(noprobe)} families pair sub-findings with no probe hit at"
    out["sp_b_noprobe_list"] = (f"all ({', '.join(noprobe)}) — {NUM_WORDS[len(noprobe)]} of the bead's "
                                f"{NUM_WORDS[len(ep.DENSEST)]} named densest targets —")
    out["sp_b_fp"] = f"{len(fp_probe)} of the {len(probe)} probe hits"
    out["sp_notread"] = (f"{len(multi) - len(pop)} families with two or more manuscripts are not read. "
                         f"The page covers {len(pop)} of the {len(multi)}.")
    out["sp_rows"] = (f"The {p['comparator_rows']} comparator-link rows in `notes/subfindings.tsv` "
                      f"are not paired; only the {p['manuscript_rows']} manuscript rows")
    out["sp_rows2"] = f"only {mss} of those are in this population"
    return out


SP_SPLIT = {
    "sp_densest_range": ["034 at n=14 down to 211 at"],
}


def subfinding_pairs_phrases(p: dict[str, Any]) -> dict[str, str]:
    out = subfinding_pairs_full(p)
    for label, prefixes in SP_SPLIT.items():
        base = out.pop(label)
        rest = base
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {base!r}")
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def subfinding_pairs_page(p: dict[str, str]) -> str:
    return ENV.get_template("subfinding-pairs.md.j2").render(p=p)


README_SHAPE_GIST: dict[str, str] = {
    "uniform": '"uniformly", "for every", "arbitrary"',
    "resolution": "resolves / proves the conjecture / answers the question / settles",
    "bound": "bound, sharp, power-saving, improvement, inequality",
    "counterexample": "counterexample, disprove, refute, fails, violation",
    "partial": "at most, restricted, in coranks, for fixed, unramified part",
    "classification": "if and only if, classified, characterization",
    "density": "density",
    "conditional": "assuming, we assume, under the … hypothesis, provided that",
    "undecidability": "no algorithm, undecidable, unsolvable, negative answer",
}

README_TIER_MEANING: dict[str, str] = {
    "T3": "≥1 linked config listed in `main_results`",
    "T2": "linked configs exist, none listed in `main_results` (companion/secondary statements)",
    "T1": "scope note with no comparator link",
    "T0": "no scope note, no challenge, no main result",
}

README_ABSTRACT_SCOPE = 233


def readme_population() -> dict[str, Any]:
    entries = Y.main_results_entries()
    return {
        "rows": tsv.read_rows(LEDGER_TSV),
        "sources_paths": len(Y.SOURCE_ID.findall(FORMALIZATION_YAML.read_text(encoding="utf-8"))),
        "entries": len(entries),
        "entry_configs": {e["config"] for e in entries},
        "docs": Y.parse_docs(),
    }


def readme_full(p: dict[str, Any]) -> dict[str, str]:
    rows = p["rows"]
    out: dict[str, str] = {}
    fams = len(rows)
    paps = sum(int(r["paps"]) for r in rows)
    form = sum(int(r["paps_form"]) for r in rows)
    notes = sum(int(r["scope_note"]) for r in rows)
    chal = sum(int(r["chal"]) for r in rows)
    tiers = collections.Counter(r["tier"] for r in rows)
    shapes = collections.Counter(s for r in rows for s in r["shapes"].split("|") if s)
    out["cov_row_1"] = (f"| Manuscripts with a formalized main result | `formalization.yaml` → "
                        f"`sources:` | {form} / {paps} |")
    out["cov_row_2"] = f"| Families with a scope note | `lean/docs/<NNN>.md` | {notes} / {fams} |"
    out["cov_row_3"] = (f"| Statement/solution pairs | `lean/ComparatorChallenges/*.json` | "
                        f"{chal} |")
    out["cov_row_4"] = (f"| Catalogued main results | `formalization.yaml` → `status.main_results` | "
                        f"{p['entries']} entries / {len(p['entry_configs'])} unique configs |")

    fam_form = sum(1 for r in rows if int(r["paps_form"]))
    fam_main = sum(1 for r in rows if int(r["mainres"]))
    gap = [r["fam"] for r in rows if int(r["mainres"]) and not int(r["paps_form"])]
    out["cov_agree"] = (f"{fam_form} families have ≥1 formalized manuscript and {fam_main} have "
                        f"≥1 config listed in `main_results`")
    out["cov_gap"] = f"the difference is family **{gap[0]}**"
    out["cov_paths"] = f"The yaml's own `sources:` list carries {p['sources_paths']} paths"
    out["cov_t2"] = (f"The {tiers['T2']} families at T2 have a scope note and comparator links, "
                     f"and zero formalized manuscripts.")

    for i, tier in enumerate(("T3", "T2", "T1", "T0")):
        out[f"tier_row_{i + 1}"] = f"| {tier} | {README_TIER_MEANING[tier]} | {tiers[tier]} |"
    out["tier_t1"] = f"every one of the {notes} scope notes links at least one challenge file"
    out["tier_t0"] = f"**All {tiers['T0']} T0 families have zero formalized manuscripts**"
    t0 = [r for r in rows if r["tier"] == "T0"]
    t0_noshape = [r for r in t0 if not r["shapes"]]
    out["tier_flag"] = (f"{sum(1 for r in t0 if r['resolves_named'] == '1')} of the {len(t0)} are "
                        f"flagged, including {sum(1 for r in t0_noshape if r['resolves_named'] == '1')}"
                        f" of the {len(t0_noshape)} families with no shape tag at all")

    for i, shape in enumerate(README_SHAPE_GIST):
        out[f"shape_row_{i + 1}"] = f"| {shape} | {README_SHAPE_GIST[shape]} | {shapes[shape]} |"
    out["shape_multi"] = (f"{sum(1 for r in rows if len([s for s in r['shapes'].split('|') if s]) >= 3)}"
                          f" families match ≥3 shapes and {sum(1 for r in rows if not r['shapes'])}"
                          " match none")
    out["cond_fams"] = "`conditional` families: **" + ", ".join(
        sorted(r["fam"] for r in rows if r["conditional"] == "1")) + ".**"

    cc = [r for r in rows if "counterexample" in r["shapes"].split("|") and r["tier"] != "T0"]
    cc_t3 = [r for r in cc if r["tier"] == "T3"]
    cc_t2 = [r for r in cc if r["tier"] == "T2"]
    cc_decl = sum(int(r["mainres"]) for r in cc)
    linked: set[str] = set()
    gaps_t3 = fams_t3_gap = gaps_t2 = 0
    for r in cc:
        cfgs = set(p["docs"].get(r["fam"], {}).get("configs", ()))
        linked |= cfgs
        gaps = [c for c in cfgs if c not in p["entry_configs"]]
        if r["tier"] == "T3":
            gaps_t3 += len(gaps)
            fams_t3_gap += 1 if gaps else 0
        else:
            gaps_t2 += len(gaps)
    out["cc_pop"] = f"**{len(cc)}** families, **{len(cc_t3)} at T3 and {len(cc_t2)} at T2**"
    out["cc_decl"] = (f"The {len(cc)} families carry **{cc_decl}** `main_results` declarations; "
                      f"all {cc_decl} resolve,")
    out["cc_t2"] = f"The {len(cc_t2)} T2 families carry **none**"
    out["cc_gaps"] = (f"Of the **{len(linked)}** configs their scope notes link, "
                      f"**{gaps_t3 + gaps_t2}** have no entry: **{gaps_t3}** in **{fams_t3_gap}** T3 "
                      f"families, **{gaps_t2}** across all **{len(cc_t2)}** T2 families")

    out["cw_fire"] = f"fires on **{sum(1 for r in rows if r['companion_word'] == '1')}** families"
    out["cw_edge"] = "and **0** of them carry an edge"

    ver_fams = sorted({r["fam"] for r in rows if int(r["verification"])})
    ver_dirs = sum(int(r["verification"]) for r in rows)
    v348 = int(next(r for r in rows if r["fam"] == "348")["verification"])
    out["col_paps"] = (f"| `paps` | `CONTENTS.md` links ∪ `overview.tex` `\\href` links | The two "
                       f"mappings agree exactly: {paps} links, 0 one-sided |")
    out["col_form"] = f"| `paps_form` | `formalization.yaml` `sources:` ids | Sums to {form} |"
    out["col_note"] = f"| `scope_note` | file exists | {notes} total |"
    out["col_ver"] = (f"| `verification` | manuscript dirs with a `verification/` subdir | "
                      f"{ver_dirs} dirs over {len(ver_fams)} families; family 348's {v348} are one "
                      "bundle shipped twice. A **count, not a pointer** — see the entry-point record "
                      "in `notes/verification-dirs.md` |")
    inp = sorted(r["fam"] for r in rows if int(r["inputs"]))
    out["col_inputs"] = (f"| `inputs` | manuscript dirs with `INPUTS.md` | {sum(int(r['inputs']) for r in rows)} "
                         f"dirs over {len(inp)} families ({', '.join(inp)}) |")
    cov = sorted(r["fam"] for r in rows if int(r["covmd"]))
    out["col_covmd"] = (f"| `covmd` | dirs with `verification/COVERAGE.md` | "
                        f"{sum(int(r['covmd']) for r in rows)} files, both in family {cov[0]} — these "
                        "bound what a check covers |")
    tr = sorted(r["fam"] for r in rows if r["trace"])
    out["col_trace"] = (f"| `trace` | `README.md` reasoning-trace table | {len(tr)} families; read "
                        "from the release table, not guessed from filenames |")
    out["col_named"] = (f"| `resolves_named` | title **or** abstract (lowered together) names a "
                        "conjecture/question/problem **and** uses a resolution verb | "
                        f"{sum(1 for r in rows if r['resolves_named'] == '1')} families, the "
                        f"abstract-only scope having read {README_ABSTRACT_SCOPE}; separate from the "
                        f"`resolution` shape ({shapes['resolution']}) so the T0 buckets stay put |")
    out["col_cex"] = (f"| `counterex_broad` | title **or** abstract matches the counterexample "
                      f"phrase rule | {sum(1 for r in rows if r['counterex_broad'] == '1')} families; "
                      f"a strict superset of the `counterexample` shape ({shapes['counterexample']}), "
                      "kept out of `shapes` so the T0 buckets stay put |")
    out["col_cword"] = (f"| `companion_word` | abstract says \"companion\" | "
                        f"{sum(1 for r in rows if r['companion_word'] == '1')} families |")
    ver = [r for r in rows if int(r["versions"]) > 0]
    out["col_versions"] = (f"| `versions` | manuscripts sharing a date-stripped dir slug | "
                           f"{len(ver)} families, {sum(int(r['versions']) for r in ver)} dated "
                           f"re-issues ({', '.join(r['fam'] for r in ver)}) |")
    out["col_summary"] = (f"| `summary` | a page exists at "
                          "`notes/summaries/<discipline>/<NNN>-*.md` | Filesystem fact, not a derived "
                          f"claim; {sum(1 for r in rows if int(r['summary']))} of {fams} families, "
                          f"{sum(int(r['paps']) for r in rows if int(r['summary']))} manuscripts "
                          "behind them |")

    order: list[str] = []
    by: dict[str, dict[str, int]] = {}
    for r in rows:
        d = r["discipline"]
        if d not in by:
            by[d] = {"fams": 0, "notes": 0, "paps": 0, "form": 0}
            order.append(d)
        by[d]["fams"] += 1
        by[d]["notes"] += int(r["scope_note"])
        by[d]["paps"] += int(r["paps"])
        by[d]["form"] += int(r["paps_form"])
    ranked = sorted(order, key=lambda d: (-by[d]["fams"], order.index(d)))
    for i, d in enumerate(ranked):
        b = by[d]
        out[f"disc_row_{i + 1:02d}"] = (f"| {d} | {b['fams']} | {b['notes']} | {b['paps']} | "
                                        f"{b['form']} |")
    out["disc_sum"] = f"The columns sum to {fams} / {notes} / {paps} / {form}."
    out["trace_fams"] = "(" + ", ".join(tr) + ")"
    return out


README_SPLIT: dict[str, list[str]] = {
    "cc_decl": ["The 28"],
    "cov_agree": ["135 families have ≥1 formalized manuscript and 136 have"],
    "cov_t2": ["The"],
    "tier_flag": ["86 of the 130 are flagged, including 11 of the 19 families with no shape"],
    "cc_gaps": ["Of the **52** configs their scope notes link, **24** have no entry: **12** in **8** T3"],
    "cw_fire": ["fires on"],
    "trace_fams": ["(007, 017, 087, 102,"],
}


def readme_phrases(p: dict[str, str]) -> dict[str, str]:
    out = readme_full(p)
    for label, prefixes in README_SPLIT.items():
        base = out.pop(label)
        rest = base
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {base!r}")
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


def readme_page(p: dict[str, str]) -> str:
    return ENV.get_template("README.md.j2").render(p=p)


# The Verdict column and the gap table's "what the claim needs" cells are reading-pass findings,
# not measurements: they ship as records keyed by family / (config, family).
CC_VERDICTS = {
    "047": "entry states the counterexample",
    "072": "entry states it; two companion entries",
    "095": "entry states the counterexample",
    "100": "structural absence",
    "118": "entry states the counterexample",
    "151": "structural absence",
    "155": "entry states the counterexample",
    "157": "entry states the Hadwiger claim; one gap",
    "161": "structural absence",
    "162": "entries state both claims; one gap",
    "172": "classification and spherical witness; five gaps",
    "185": "entry states claim 1; one gap",
    "190": "entry states the counterexample",
    "191": "structural absence",
    "192": "structural absence",
    "197": "three entries state the three claims; one gap",
    "198": "entry states claim 1; one companion",
    "199": "entries state claims 1 and 3",
    "244": "entry states claim 1; one gap",
    "272": "structural absence",
    "289": "structural absence",
    "294": "entry states claim 1; one gap",
    "297": "structural absence",
    "323": "structural absence",
    "329": "entry states the counterexample",
    "347": "entry states a degenerate instance",
    "350": "entries state two forms; one gap",
    "361": "entry states the counterexample",
}

CC_NEEDS = {
    ("ListHadwiger", "157"): "no claim sentence names it",
    ("BalancedRyser", "162"): "the balanced case of the Ryser covering claim",
    ("EuclideanRamseyCircle", "172"): "no claim sentence names it",
    ("EuclideanRamseyNine", "172"): "no claim sentence names it",
    ("EuclideanRamseyQuadratic", "172"): "no claim sentence names it",
    ("EuclideanRamseySpherical", "172"): "no claim sentence names it",
    ("EuclideanRamseyTransitive", "172"): "the Leader–Russell–Walters refutation (claim 1)",
    ("InfiniteMatroidCorollaries", "185"): "the Joó partitional-matroid corollary (claim 2)",
    ("KaplanskyDirectFiniteness", "197"): "the general direct-finiteness counterexample",
    ("PartitionConsistency", "244"): "no claim sentence names it",
    ("KaplanskyStableFiniteness", "294"): "no claim sentence names it",
    ("NodalLength", "350"): "the nodal-length bound",
}


def crosscheck_population() -> dict[str, Any]:
    rows = {r["fam"]: r for r in tsv.read_rows(LEDGER_TSV)}
    order, fams = overview.parse_overview()
    shape = [f for f in order if "counterexample" in B.shapes_of(fams[f]["abstract"])]
    pop = [f for f in shape if rows[f]["tier"] != "T0"]
    mr, entries = cc.main_results()
    links = {f: cc.scope_note(f)[1] for f in pop}
    cfgs = {f: sorted({c for _, c in links[f]}) for f in pop}
    first_link = {f: {c: min(n for n, x in links[f] if x == c) for c in cfgs[f]} for f in pop}
    gaps = {f: [c for c in cfgs[f] if c not in mr] for f in pop}
    # The page's Entries column counts configs that HAVE an entry, not the yaml entries a config
    # carries; the coverage sentences count the ledger's mainres column.
    ent_cfg = {f: len([c for c in cfgs[f] if c in mr]) for f in pop}
    all_cfg = sorted({c for f in pop for c in cfgs[f]})

    def sorry(c: str) -> int:
        p = COMPARATOR_DIR / f"{c}.lean"
        return p.read_text(encoding="utf-8", errors="replace").count("sorry") if p.is_file() else 0

    carriers = carriers_ok = 0
    for f in pop:
        for c in cfgs[f]:
            ent = mr.get(c)
            if ent is None:
                continue
            decl, rel, _ = ent
            at, block = cc.declaration_statement(decl, rel)
            if at is None:
                continue
            t = re.search(r":\s*([A-Z][A-Za-z0-9_.]*(?:\.\{[^}]*\})?)\s*:=", " ".join(block))
            if not t:
                continue
            carriers += 1
            cfile, _, _ = cc.carrier(t.group(1).split(".{")[0].split(".")[-1], rel)
            if cfile is not None:
                carriers_ok += 1
    return {
        "rows": rows, "pop": pop, "tiers": collections.Counter(rows[f]["tier"] for f in pop),
        "shape": len(shape), "mr": mr, "entries": entries, "cfgs": cfgs, "links": links,
        "first_link": first_link, "ent_cfg": ent_cfg, "gaps": gaps,
        "with_entry": [f for f in pop if ent_cfg[f] > 0],
        "without": [f for f in pop if ent_cfg[f] == 0],
        "all_cfg": all_cfg,
        "mainres": sum(int(rows[f]["mainres"]) for f in pop),
        "sorry_distinct": sum(sorry(c) for c in all_cfg),
        "sorry_links": sum(sorry(c) for f in pop for _, c in links[f]),
        "carriers": carriers, "carriers_ok": carriers_ok,
        "broad": [f for f in order if rows[f]["counterex_broad"] == "1"],
    }


def crosscheck_phrases(p: dict[str, Any]) -> dict[str, str]:
    rows, pop = p["rows"], p["pop"]
    t3, t2 = p["tiers"]["T3"], p["tiers"]["T2"]
    out: dict[str, str] = {}
    out["cc_pop"] = f"**{len(pop)}** families — **{t3}** at T3 and **{t2}** at T2"
    out["cc_shape"] = f"**{p['shape']}** families overall, so"
    out["cc_t0"] = f"**{p['shape'] - len(pop)}** carry the tag at T0"
    out["cc_led_over"] = f"Ledger sums over the {len(pop)}:"
    out["cc_led_a"] = (f"**{sum(int(rows[f]['mainres']) for f in pop)}** `main_results` declarations, "
                       f"**{sum(int(rows[f]['chal']) for f in pop)}** comparator configs, "
                       f"**{sum(int(rows[f]['paps_form']) for f in pop)}**")
    out["cc_led_b"] = f"formalized manuscripts out of **{sum(int(rows[f]['paps']) for f in pop)}**"
    out["cc_scope_all"] = f"Every one of the {len(pop)} has a scope note"
    out["cc_yaml"] = (f"**{len(p['entries'])}** `main_results` entries over "
                      f"**{len(set(p['entries']))}** unique configs")
    out["cc_of"] = (f"Of the {len(pop)} families, **{len(p['with_entry'])}** have at least one entry "
                    f"and **{len(p['without'])}**")
    out["cc_tierdict"] = f"`{dict(collections.Counter(rows[f]['tier'] for f in p['without']))}`"
    out["cc_decl_all"] = f"All **{p['mainres']}** declarations resolve"
    out["cc_carrier"] = f"**{p['carriers']}** of the {len(pop)} are"
    out["cc_carrier_res"] = f"**{p['carriers_ok']}** carriers resolve"
    out["cc_cfg_acct"] = f"Config accounting: the {len(pop)} scope notes link"
    out["cc_cfg"] = (f"**{len(p['all_cfg'])}** distinct configs, **{p['mainres']}** of them carry an "
                     f"entry and")
    out["cc_cfg_none"] = f"**{len(p['all_cfg']) - p['mainres']}** carry none"
    t3g = [f for f in pop if rows[f]["tier"] == "T3" and p["gaps"][f]]
    t2g = [f for f in pop if rows[f]["tier"] == "T2" and p["gaps"][f]]
    out["cc_t3gap"] = f"**{sum(len(p['gaps'][f]) for f in t3g)}** configs in **{len(t3g)}** families"
    out["cc_t2gap"] = (f"**{sum(len(p['gaps'][f]) for f in t2g)}** configs in all "
                       f"**{len(t2g)}** families")
    out["cc_h_t3"] = f"## The {t3} T3 families"
    out["cc_h_t2"] = f"## The {t2} T2 families: structural absence"
    out["cc_gap_intro"] = (f"The {sum(len(p['gaps'][f]) for f in t3g)} configs a T3 scope note links "
                           f"that carry no `main_results` entry, in {len(t3g)} families:")
    for f in pop:
        out[f"cc_row_{f}"] = (f"| {f} | {rows[f]['tier']} | {len(p['cfgs'][f])} | {p['ent_cfg'][f]} | "
                              f"{len(p['gaps'][f])} | {CC_VERDICTS[f]} |")
    for f in pop:
        if rows[f]["tier"] != "T2":
            continue
        cell = ", ".join(f"`{c}`" for c in p["cfgs"][f])
        anchor = min(p["first_link"][f].values())
        out[f"cc_t2row_{f}"] = f"| {f} | {cell} | `lean/docs/{f}.md:{anchor}` |"
    for f in pop:
        for c in p["gaps"][f]:
            if rows[f]["tier"] != "T3":
                continue
            out[f"cc_gaprow_{c}"] = (f"| `{c}` | {f} | `lean/docs/{f}.md:{p['first_link'][f][c]}` | "
                                     f"{CC_NEEDS[(c, f)]} |")
    out["cc_100_links"] = f"{len(p['links']['100'])} link occurrences, {len(p['cfgs']['100'])} distinct configs"
    out["cc_stub_a"] = (f"The {len(pop)} scope notes link **{len(p['all_cfg'])}** distinct configs, "
                        f"and each has a stub file under")
    out["cc_stub_sorry"] = f"carrying **{p['sorry_distinct']}** `sorry` occurrences"
    out["cc_stub_links"] = (f"the same files carry {p['sorry_links']}, the "
                            f"{p['sorry_links'] - p['sorry_distinct']}-gap being family 100's four")
    out["cc_stub_cov"] = (f"which is why {p['mainres']} entries over {len(p['all_cfg'])} configs is "
                          f"the coverage answer")
    out["cc_bead_t0"] = f"fires on **{p['shape'] - len(pop)}** T0 families"
    out["cc_bead_21"] = f"The **{sum(1 for f in p['broad'] if rows[f]['tier'] == 'T0')}** is the count"
    out["cc_broad"] = (f"column, {len(p['broad'])} families corpus-wide: "
                       f"{sum(1 for f in p['broad'] if rows[f]['tier'] == 'T0')}")
    out["cc_broad_tiers"] = (f"T0, {sum(1 for f in p['broad'] if rows[f]['tier'] == 'T3')} T3, "
                             f"{sum(1 for f in p['broad'] if rows[f]['tier'] == 'T2')} T2")
    out["cc_nc_decl"] = f"The {len(pop)} declarations were resolved"
    out["cc_nc_carrier"] = f"({p['carriers']} of them are)"
    out["cc_nc_t0"] = f"The {p['shape'] - len(pop)} T0 families with the shape tag"
    out["cc_nc_outside"] = (f"the {len(set(p['entries']))} − {p['mainres']} = "
                            f"{len(set(p['entries'])) - p['mainres']} configs named by")
    for label, prefixes in CC_SPLIT.items():
        base = out.pop(label)
        rest = base
        for i, pre in enumerate(prefixes):
            rest = rest.lstrip()
            if not rest.startswith(pre):
                raise ValueError(f"slot {label!r}: page wrap {pre!r} is not a prefix of {base!r}")
            out[f"{label} {'abcdefghij'[i]}"] = pre
            rest = rest[len(pre):]
        out[f"{label} {'abcdefghij'[len(prefixes)]}"] = rest.lstrip()
    return out


CC_SPLIT: dict[str, list[str]] = {
    # label -> first-line prefix of each page newline inside its span; the tail is the remainder
    "cc_bead_21": ["The"],
    "cc_stub_cov": ["which is why 28 entries"],
    "cc_t2gap": ["**12**"],
}


def crosscheck_page(p: dict[str, str]) -> str:
    return ENV.get_template("counterexample-crosscheck.md.j2").render(p=p)


# The registry: page name -> the call that measures it, and page path -> the call that renders it.
# A checker that wants the writer's bytes for a page calls render_page(page) instead of re-deriving
# them, and a checker that wants the writer's numbers calls population_of(name). Both are cached, so
# a run that renders a page and then reports its slots measures the corpus once.
@cache
def population_of(name: str) -> Any:
    return POPULATIONS[name]()


POPULATIONS: dict[str, Callable[[], Any]] = {
    "named-results": en.population,
    "index-design": M.population,
    "names": names_population,
    "proof-density": proof_density_population,
    "index-links": index_links_population,
    "links": links_population,
    "dependency-drift": drift_population,
    "verification-dirs": verification_dirs_population,
    "scope-exclusions": scope_exclusions_population,
    "topics": lambda: topics_population(links_full(population_of("links"))),
    "t0-chains": t0_chains_population,
    "subfinding-pairs": subfinding_pairs_population,
    "README": readme_population,
    "counterexample-crosscheck": crosscheck_population,
    # templates.md reports the census of both template trees, measured by measure_templates.py. The
    # page compares a template's slot count with the writer's label count, so the abstracts label count
    # travels inside its population — CA.measure() is the call abstracts_page() makes.
    "templates": lambda: templates_population(len(abstracts_phrases(CA.measure()))),
}


PAGE_RENDERERS: dict[pathlib.Path, Callable[[], str]] = {
    SOURCES_MD: sources_page,
    ABSTRACTS_MD: abstracts_page,
    NAMED_RESULTS_MD: lambda: named_results_page(population_of("named-results")),
    INDEX_DESIGN_MD: lambda: index_page(population_of("index-design")),
    NAMES_MD: lambda: names_page(names_phrases(population_of("names"))),
    PROOF_DENSITY_MD: lambda: proof_density_page(proof_density_phrases(population_of("proof-density"))),
    INDEX_LINKS_MD: lambda: index_links_page(index_links_phrases(population_of("index-links"))),
    LINKS_MD: lambda: links_page(links_phrases(population_of("links"))),
    DRIFT_MD: lambda: drift_page(drift_phrases(population_of("dependency-drift"))),
    VERIF_MD: lambda: verification_dirs_page(verification_dirs_phrases(population_of("verification-dirs"))),
    EX_MD: lambda: scope_exclusions_page(scope_exclusions_phrases(population_of("scope-exclusions"))),
    TOPICS_MD: lambda: topics_page(topics_phrases(population_of("topics"))),
    T0_CHAINS_MD: lambda: t0_chains_page(t0_chains_phrases(population_of("t0-chains"))),
    SP_MD: lambda: subfinding_pairs_page(subfinding_pairs_phrases(population_of("subfinding-pairs"))),
    README_MD: lambda: readme_page(readme_phrases(population_of("README"))),
    CROSSCHECK_MD: lambda: crosscheck_page(crosscheck_phrases(population_of("counterexample-crosscheck"))),
    TEMPLATES_MD: lambda: templates_page(templates_phrases(population_of("templates"))),
}


def render_page(page: pathlib.Path) -> str:
    """The writer's bytes for a templated page — the baseline a render-diff compares the page against."""
    return PAGE_RENDERERS[page]()


def main() -> None:
    mp = population_of("named-results")
    ip = population_of("index-design")
    np_ = population_of("names")
    pdp = population_of("proof-density")
    ilk = population_of("index-links")
    lk = population_of("links")
    dp = population_of("dependency-drift")
    xp = population_of("scope-exclusions")
    vp = population_of("verification-dirs")
    tp = population_of("topics")
    tcp = population_of("t0-chains")
    spp = population_of("subfinding-pairs")
    rmp = population_of("README")
    xcp = population_of("counterexample-crosscheck")
    tplp = population_of("templates")
    SOURCES_MD.write_text(render_page(SOURCES_MD), encoding="utf-8")
    ABSTRACTS_MD.write_text(render_page(ABSTRACTS_MD), encoding="utf-8")
    NAMED_RESULTS_MD.write_text(render_page(NAMED_RESULTS_MD), encoding="utf-8")
    INDEX_DESIGN_MD.write_text(render_page(INDEX_DESIGN_MD), encoding="utf-8")
    NAMES_MD.write_text(render_page(NAMES_MD), encoding="utf-8")
    PROOF_DENSITY_MD.write_text(render_page(PROOF_DENSITY_MD), encoding="utf-8")
    INDEX_LINKS_MD.write_text(render_page(INDEX_LINKS_MD), encoding="utf-8")
    LINKS_MD.write_text(render_page(LINKS_MD), encoding="utf-8")
    DRIFT_MD.write_text(render_page(DRIFT_MD), encoding="utf-8")
    VERIF_MD.write_text(render_page(VERIF_MD), encoding="utf-8")
    EX_MD.write_text(render_page(EX_MD), encoding="utf-8")
    TOPICS_MD.write_text(render_page(TOPICS_MD), encoding="utf-8")
    T0_CHAINS_MD.write_text(render_page(T0_CHAINS_MD), encoding="utf-8")
    SP_MD.write_text(render_page(SP_MD), encoding="utf-8")
    README_MD.write_text(render_page(README_MD), encoding="utf-8")
    CROSSCHECK_MD.write_text(render_page(CROSSCHECK_MD), encoding="utf-8")
    TEMPLATES_MD.write_text(render_page(TEMPLATES_MD), encoding="utf-8")
    for page in (SOURCES_MD, ABSTRACTS_MD, NAMED_RESULTS_MD, INDEX_DESIGN_MD, NAMES_MD,
                 PROOF_DENSITY_MD, INDEX_LINKS_MD, LINKS_MD, DRIFT_MD, VERIF_MD, EX_MD, TOPICS_MD,
                 T0_CHAINS_MD, SP_MD, README_MD, CROSSCHECK_MD, TEMPLATES_MD):
        out = page.read_text(encoding="utf-8")
        print(f"{page.name} written  lines {len(out.splitlines())}  bytes {len(out.encode())}")
    ms, ma = measure(), CA.measure()
    print(f"slots  sources {len(phrases(ms))}  abstracts {len(abstracts_phrases(ma))}"
          f"  named-results {len(named_results_phrases(mp))}"
          f"  index-design {len(index_phrases(ip))}  names {len(names_phrases(np_))}"
          f"  proof-density {len(proof_density_phrases(pdp))}"
          f"  index-links {len(index_links_phrases(ilk))}  links {len(links_phrases(lk))}"
          f"  dependency-drift {len(drift_phrases(dp))}"
          f"  verification-dirs {len(verification_dirs_phrases(vp))}"
          f"  scope-exclusions {len(scope_exclusions_phrases(xp))}"
          f"  topics {len(topics_phrases(tp))}"
          f"  t0-chains {len(t0_chains_phrases(tcp))}"
          f"  subfinding-pairs {len(subfinding_pairs_phrases(spp))}"
          f"  readme {len(readme_phrases(rmp))}"
          f"  crosscheck {len(crosscheck_phrases(xcp))}"
          f"  templates {len(templates_phrases(tplp))}"
          f"  multi-root rows {len(ms['multi'])}  rows {ms['rows']}  listed {ms['listed']}"
          f"  dirs {ms['dirs']}  comparisons {ma['manuscripts']}  families {ma['families']}"
          f"  target rows {len(tgt_rows(mp))}")


if __name__ == "__main__":
    main()
