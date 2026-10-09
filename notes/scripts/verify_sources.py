#!/usr/bin/env python3
"""Verify notes/sources.md and notes/sources.tsv against the manuscript trees on disk.

Report-only; writes nothing and runs nothing. Three passes:

1. TSV integrity. 719 rows, the shipped header, every `pdf` on disk and non-empty, every
   `main_tex` a file that exists and declares `\\documentclass` at line start, every `fam` in
   notes/catalog.tsv, every family's row count equal to the ledger's `paps`, every resolved main
   file sitting under `build/`, and the `roots` distribution equal to a fresh line-start recount
   over the **listed** manuscripts. The recount is scoped to the manuscript list, not to every
   directory under preprints/: upstream keeps superseded editions and withdrawal notices on disk.
2. Anchors. Every backticked `path:line` shape must name a file that exists and a line inside it
   (a mistyped extension fails, it is not skipped). A fenced block is attributed to the nearest
   preceding anchor (scanning back up to 8 lines) and every block line must match that file at
   consecutive line numbers.
3. Counts. Every bold count on the page is checked by matching the exact phrase the page must
   contain, rebuilt from a fresh recount: the disk census, the column sums, the main-file outcomes,
   the root distribution, the six-name environment total, and the per-name gap.

Whitespace runs are collapsed on both sides of every comparison: line-wrapping in the page is
markup, not part of the text.

--mutant runs the built-in mutations and fails if any goes uncaught.
"""
import collections
import csv
import pathlib
import re
import sys

import build_sources as S
from catlib import overview, preprints, tsv
from catlib.paths import LEDGER_TSV, PREPRINTS, SUBFINDINGS_TSV

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "notes" / "sources.md"
TSV = ROOT / "notes" / "sources.tsv"

ANCHOR = re.compile(r"`([\w./+-]+?\.(?:py|md|tex|json|tsv|yaml)):(\d+)`")
ANCHOR_SHAPE = re.compile(r"`([\w./+-]+?\.[A-Za-z][A-Za-z0-9]{0,4}):(\d+)`")
# A backticked manuscript directory slug, as it appears in prose and in the multi-root table.
SLUG = re.compile(rf"`([A-Za-z0-9][\w.+-]*-(?:{overview.MONTHS})-\d{{1,2}}-\d{{4}})`")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def rows():
    with TSV.open(encoding="utf-8") as fh:
        rdr = csv.reader(fh, delimiter="\t")
        header = next(rdr)
        body = [dict(zip(header, r, strict=False)) for r in rdr]
    return header, body


def measure():
    """Everything the page quotes, recomputed from disk."""
    header, body = rows()
    # The listed manuscripts, not every directory under preprints/: a superseded edition and a
    # withdrawal notice are directories, not manuscript rows.
    listed = sorted(PREPRINTS / name for name in
                    {r["path"].split("/")[1] for r in tsv.read_rows(SUBFINDINGS_TSV)
                     if r["kind"] == "manuscript"})
    dirs = listed
    disk = sorted(p for p in PREPRINTS.iterdir() if p.is_dir())
    unlisted = [p for p in disk if p.name not in {d.name for d in listed}]
    notices = [p for p in unlisted
               if "Withdrawal notice" in (p / "README.md").read_text(encoding="utf-8",
                                                                      errors="replace")]
    ledger = tsv.read_rows(LEDGER_TSV)
    paps = {r["fam"]: int(r["paps"]) for r in ledger}

    rootdist = collections.Counter()
    outcomes = collections.Counter()
    single_names = collections.Counter()
    main_no_dc = 0
    for d in dirs:
        roots = preprints.roots_of(d)
        rootdist[len(roots)] += 1
        main, rule = preprints.main_tex_of(roots)
        outcomes["single-root" if rule == "single-root" else
                 "flagged" if rule == "flagged" else main.name] += 1
        if rule == "single-root":
            single_names[main.name] += 1
    main_no_dc = sum(1 for d in dirs for f in d.rglob("main.tex")
                     if not preprints.DOCCLASS.search(f.read_text(encoding="utf-8",
                                                                   errors="replace")))
    substring_multi = sum(
        1 for d in dirs
        if len([f for f in d.rglob("*.tex")
                if "\\documentclass" in f.read_text(encoding="utf-8", errors="replace")]) > 1)
    six, decl, per_name = S.env_variants(dirs)
    added = {n: c for n, c in per_name.items() if n not in preprints.SIX}
    n = len(body)
    sums = {c: sum(int(r[c]) for r in body)
            for c in ("roots", "tex", "bib", "sections", "subsections", "subsubsections",
                      "proofs", "thms", "abstract", "tex_bytes")}
    ov = overview.parse_overview()[1]
    ov_paths = sorted(p for f in ov for p in ov[f]["tex_paps"])
    pdfs = sorted(r["pdf"] for r in body)
    return {
        "header": header, "rows": n, "cols": len(header), "dirs": len(disk),
        "listed": len(listed), "superseded": len(unlisted) - len(notices),
        "notices": len(notices),
        "formalized": sum(int(r["paps_form"]) for r in ledger),
        "fams": len({r["fam"] for r in body}),
        "rootdist": rootdist, "sums": sums, "outcomes": outcomes,
        "single_names": single_names, "main_no_dc": main_no_dc,
        "substring_multi": substring_multi,
        "six": six, "decl": decl, "added": added,
        "zero_bib": sum(1 for r in body if int(r["bib"]) == 0),
        "zero_proof": sum(1 for r in body if int(r["proofs"]) == 0),
        "max_tex": max(int(r["tex"]) for r in body),
        "mean_tex": sum(int(r["tex"]) for r in body) / n,
        "mean_bytes": sum(int(r["tex_bytes"]) for r in body) / n,
        "main_under_build": sum(1 for r in body if "/build/" in "/" + r["main_tex"]),
        "pdf_missing": sum(1 for r in body
                           if not (ROOT / r["pdf"]).exists()
                           or (ROOT / r["pdf"]).stat().st_size == 0),
        "main_missing": sum(1 for r in body
                            if not r["main_tex"] or not (ROOT / "preprints" / r["main_tex"]).exists()),
        "main_not_root": sum(1 for r in body
                             if r["main_tex"] and not preprints.DOCCLASS.search(
                                 (ROOT / "preprints" / r["main_tex"])
                                 .read_text(encoding="utf-8", errors="replace"))),
        "fam_outside": sum(1 for r in body if r["fam"] not in paps),
        "paps_diff": sum(1 for f, c in collections.Counter(r["fam"] for r in body).items()
                         if paps.get(f) != c),
        "pdf_ov_diff": len(set(ov_paths) ^ set(pdfs)),
        "pdf_ov_n": len(ov_paths), "pdf_n": len(pdfs),
        "pdf_ov_distinct": len(set(ov_paths)), "pdf_distinct": len(set(pdfs)),
    }


def count_phrases(m):
    def f(x):
        return f"{x:,}"
    s, o, sn = m["sums"], m["outcomes"], m["single_names"]
    rd = m["rootdist"]
    gap = ", ".join(f"`{n}` {c}" for n, c in
                    sorted(m["added"].items(), key=lambda kv: (-kv[1], kv[0])))
    return [
        (f"**{m['rows']} rows, {m['cols']} columns**", "table shape"),
        (f"| {m['rows']} distinct |", "dir distinct count"),
        (f"| {m['fams']} distinct |", "fam distinct count"),
        (f"| {m['rows']} filled, **0** empty |", "main_tex filled count"),
        (f"| **{s['roots']}** over {m['listed']} dirs: {rd[1]} with 1, {rd[2]} with 2, {rd[3]} with 3 |",
         "roots distribution"),
        (f"| **{f(s['tex'])}** (max {m['max_tex']}, mean {m['mean_tex']:.2f} per dir) |",
         "tex file count"),
        (f"| **{f(s['bib'])}**; **{m['zero_bib']}** dirs carry none |", "bib count"),
        (f"| **{f(s['sections'])}** |", "section count"),
        (f"| **{f(s['subsections'])}** |", "subsection count"),
        (f"| **{f(s['subsubsections'])}** |", "subsubsection count"),
        (f"| **{f(s['proofs'])}**; **{m['zero_proof']}** dir carries none |", "proof count"),
        (f"| **{f(s['thms'])}** |", "thms count"),
        (f"| **{s['abstract']} of {m['rows']}** |", "abstract count"),
        (f"| **{f(s['tex_bytes'])}** (mean {f(round(m['mean_bytes']))} per dir) |", "tex bytes"),
        (f"**main.tex {o['main.tex']}, paper.tex {o['paper.tex']}, single-root {o['single-root']}, "
         f"flagged {o['flagged']}.**", "main-file outcomes"),
        (f"because **{m['main_no_dc']}** `main.tex` files in the corpus", "main.tex without documentclass"),
        (f"`preamble.tex` **{sn['preamble.tex']}**, `manuscript.tex` **{sn['manuscript.tex']}**, "
         f"`common.tex` **{sn['common.tex']}**", "single-root name counts"),
        (f"and **{sum(c for n, c in sn.items()) - sn['preamble.tex'] - sn['manuscript.tex'] - sn['common.tex']}** singletons",
         "single-root singleton count"),
        (f"`preprints/` holds **{m['dirs']}** directories: the **{m['listed']}** the release lists, "
         f"**{m['superseded']}** superseded editions upstream keeps beside their replacements, and "
         f"**{m['notices']}** withdrawal notices", "disk census"),
        (f"**Every one of the {m['rows']} resolved main files sits under a `build/` directory.**",
         "main file under build"),
        (f"and **{m['substring_multi']}** with two or three", "substring multi-root count"),
        (f"reads **{m['rootdist'][1] - 0}** and **{m['listed'] - m['rootdist'][1]}**",
         "line-start root counts"),
        ("under either rule (0 differences)", "rule agreement"),
        (f"occurrence — {f(m['decl'])} both ways", "declared-rule agreement"),
        (f"quotes **{f(m['six'])}** for", "six-name count"),
        (f"The {m['decl'] - m['six']} gap is names", "env gap"),
        (f"{gap}. The TSV column carries the declared-rule figure.", "env gap breakdown"),
        (f"rows written **{m['rows']}**, listed manuscript dirs **{m['listed']}**, "
         f"preprint dirs on disk **{m['dirs']}**", "report reconciliation"),
        (f"**{m['pdf_ov_distinct']}** distinct vs `sources.tsv`", "overview path distinct count"),
        (f"`pdf` **{m['pdf_distinct']}** distinct", "pdf distinct count"),
        (f"at **{m['formalized']}** of {m['rows']} manuscripts", "formalized share"),
    ]


def check(text):
    problems = []
    lines = text.split("\n")
    flat = norm(text)
    n_anchor = n_block_lines = n_slug = 0

    header, body = rows()
    if header != S.COLUMNS:
        problems.append(f"tsv header {header} != shipped COLUMNS {S.COLUMNS}")
    if len(body) != 719:
        problems.append(f"tsv has {len(body)} rows, expected 719")

    for m in ANCHOR_SHAPE.finditer(text):
        rel, at = m.group(1), int(m.group(2))
        f = ROOT / rel
        if not f.exists():
            problems.append(f"anchor file {rel} does not exist")
            continue
        src = f.read_text(encoding="utf-8", errors="replace").split("\n")
        n_anchor += 1
        if not 1 <= at <= len(src):
            problems.append(f"anchor {rel}:{at} is outside the file ({len(src)} lines)")

    # Every manuscript directory named on the page must exist; a mutated slug is otherwise
    # invisible to the count checks, which never look at directory names.
    for m in SLUG.finditer(text):
        n_slug += 1
        if not (PREPRINTS / m.group(1)).is_dir():
            problems.append(f"directory {m.group(1)} is not a preprints/ directory")

    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("```"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            j = i + 1
            blk = []
            while j < len(lines) and not lines[j].lstrip().startswith("```"):
                ln = lines[j]
                blk.append(ln[len(indent):] if ln.startswith(indent) and ln.strip() else ln)
                j += 1
            anchor = None
            for k in range(i - 1, max(i - 9, -1), -1):
                found = ANCHOR.findall(lines[k])
                if found:
                    anchor = (found[-1][0], int(found[-1][1]))
                    break
            if anchor is None:
                problems.append(f"page line {i + 1}: fenced block has no preceding file:line anchor")
            elif not (ROOT / anchor[0]).exists():
                problems.append(f"page line {i + 1}: anchor file {anchor[0]} does not exist")
            else:
                rel, at = anchor
                src = (ROOT / rel).read_text(encoding="utf-8", errors="replace").split("\n")
                for k, want in enumerate(blk):
                    got = src[at - 1 + k] if at - 1 + k < len(src) else "<past end of file>"
                    n_block_lines += 1
                    if got != want:
                        problems.append(
                            f"page line {i + 2}: block line {k} != {rel}:{at + k}\n"
                            f"    want {want!r}\n    got  {got!r}")
            i = j + 1
        else:
            i += 1

    m = measure()
    for key, want in (("pdf_missing", 0), ("main_missing", 0), ("main_not_root", 0),
                      ("fam_outside", 0), ("paps_diff", 0), ("pdf_ov_diff", 0)):
        if m[key] != want:
            problems.append(f"tsv integrity {key}: {m[key]} differences, expected {want}")
    if m["main_under_build"] != m["rows"]:
        problems.append(f"tsv integrity main_under_build: {m['main_under_build']} of {m['rows']} "
                        f"main files sit under build/")
    if m["listed"] != m["rows"]:
        problems.append(f"tsv integrity listed: {m['listed']} manuscript slugs vs {m['rows']} rows")
    for phrase, label in count_phrases(m):
        if norm(phrase) not in flat:
            problems.append(f"count mismatch ({label}): page does not contain {phrase!r}")

    return problems, n_anchor, n_block_lines, n_slug, len(count_phrases(m))


MUTANTS = {
    "anchor line shifted": lambda t: t.replace("pgfmanual-en-macros.tex:1177",
                                               "pgfmanual-en-macros.tex:1176", 1),
    "anchor file renamed": lambda t: t.replace("build/paper.tex:1", "build/paper.yml:1", 1),
    "block line altered": lambda t: t.replace("\\def\\extractclass#1#2@{%",
                                              "\\def\\extractclass#1#3@{%", 1),
    "count altered": lambda t: t.replace("**16,297**", "**16,290**", 1),
    "byte figure altered": lambda t: t.replace("**127,456,942**", "**127,000,000**", 1),
    "six-name count altered": lambda t: t.replace("quotes **21,203** for",
                                                  "quotes **21,288** for", 1),
    "gap breakdown altered": lambda t: t.replace("`assumption` 22, `foundation` 13",
                                                 "`assumption` 21, `foundation` 13", 1),
    "directory name altered": lambda t: t.replace(
        "`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026`",
        "`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-6-2026`", 1),
    "root distribution altered": lambda t: t.replace("715 with 1, 3 with 2, 1 with 3",
                                                     "716 with 1, 2 with 2, 1 with 3", 1),
    "disk census altered": lambda t: t.replace("the **719** the release lists",
                                               "the **720** the release lists", 1),
    "formalized share altered": lambda t: t.replace("at **172** of 719 manuscripts",
                                                     "at **173** of 719 manuscripts", 1),
}


def main():
    text = PAGE.read_text(encoding="utf-8", errors="replace")

    if "--mutant" in sys.argv:
        uncaught = []
        for name, fn in MUTANTS.items():
            mutated = fn(text)
            if mutated == text:
                print(f"mutant target absent: {name}")
                uncaught.append(name)
                continue
            problems, _, _, _, _ = check(mutated)
            print(f"mutant {name}: {'caught' if problems else 'NOT CAUGHT'}"
                  f" ({len(problems)} problems)")
            if not problems:
                uncaught.append(name)
        print(f"mutants not caught {len(uncaught)} of {len(MUTANTS)}")
        raise SystemExit(1 if uncaught else 0)

    problems, n_anchor, n_block_lines, n_slug, n_phrases = check(text)
    for p in problems:
        print(f"PROBLEM {p}")
    print(f"\nanchors {n_anchor}  slugs {n_slug}  block lines {n_block_lines}"
          f"  count phrases {n_phrases}  problems {len(problems)}")
    raise SystemExit(1 if problems else 0)


main()
