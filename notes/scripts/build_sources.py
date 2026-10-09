#!/usr/bin/env python3
"""Write notes/sources.tsv: the LaTeX source surface of each of the 719 listed manuscripts.

Reads the manuscript trees as text. Runs nothing, parses no PDF, opens no Lean file. The row set is
the manuscript list from notes/subfindings.tsv, not a walk of preprints/: upstream keeps superseded
editions beside their replacements and a withdrawal notice beside its replacement, so a directory
walk is 749 dirs, not 719 manuscripts.

Rules stated where they matter:

- A root is a `.tex` file with `\\documentclass` **at the start of a line**. The line-start rule
  gives 715 dirs with exactly one root and 4 with two; a substring count of `\\documentclass`
  reads 714 and 5, because one dir has a file that mentions the command in prose
  (Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026).
- Main-file resolution prefers a file named `main.tex` **that declares `\\documentclass`**, then
  `paper.tex`, then the single root. 12 `main.tex` files in the corpus declare no documentclass
  (companion and build copies), so preferring the bare name would pick a non-root file.
  Multi-root dirs with no `main.tex`/`paper.tex` are flagged with an empty `main_tex`, not guessed.
- `thms` counts `\\begin{X}` for X declared by `\\newtheorem` in the same dir, minus the
  non-statement names (definition, remark, example, notation, convention, procedure, construction,
  scope, abstract). Every theorem-like env used in the corpus is locally declared, so this agrees
  with the union of declared names and a fixed standard list to the occurrence — 21,288 both ways.
  The six-name list the epic quotes (theorem, lemma, proposition, corollary, claim, conjecture)
  reads 21,203; the 85 gap is names the declared rule counts that the six omit (assumption 22,
  foundation 13, hypothesis 8, auxproposition 8, auxlemma 7, standinginput 5, maintheorem 4,
  externalinput 4, companionresults 3, unnumberedproposition 3, verification 2, principle 2,
  maincorollary 2, thm 1, question 1). Quote the count with its rule.
- `abstract` is a line-start `\\begin{abstract}` anywhere in the dir. All 719 listed dirs have one,
  so the column does not discriminate; it is kept because the bead asked for it.
- Manuscript ownership is the path component after `preprints`, never `parts[-2]`. Family and PDF
  path come from the manuscript rows of notes/subfindings.tsv, which is itself derived from
  overview.tex.

The LaTeX joins live in catlib/preprints.py; the TSV reader and writer in catlib/tsv.py.
"""
import collections
import pathlib

from catlib import overview, preprints, text, tsv
from catlib.paths import LEDGER_TSV, PREPRINTS, ROOT, SOURCES_TSV, SUBFINDINGS_TSV, read_text
from catlib.preprints import DOCCLASS, SIX

OUT = SOURCES_TSV

COLUMNS = ["dir", "fam", "pdf", "main_tex", "roots", "tex", "bib", "sections", "subsections",
           "subsubsections", "proofs", "thms", "abstract", "tex_bytes"]


def row_for(d, fam, pdf):
    tex_files = preprints.tex_files(d)
    ts = preprints.texts(tex_files)
    declared = preprints.declared_envs(ts)
    counts = preprints.env_counts(ts, declared)
    roots = preprints.roots_of(d)
    main, _ = preprints.main_tex_of(roots)
    return {
        "dir": d.name,
        "fam": fam,
        "pdf": pdf,
        "main_tex": "" if main is None else str(main.relative_to(PREPRINTS)),
        "roots": len(roots),
        "tex": len(tex_files),
        "bib": len(list(d.rglob("*.bib"))),
        "sections": counts["sections"],
        "subsections": counts["subsections"],
        "subsubsections": counts["subsubsections"],
        "proofs": counts["proofs"],
        "thms": counts["thms"],
        "abstract": counts["abstract"],
        "tex_bytes": sum(f.stat().st_size for f in tex_files),
    }


def build():
    subs = [r for r in tsv.read_rows(SUBFINDINGS_TSV) if r["kind"] == "manuscript"]
    by_slug = {r["path"].split("/")[1]: r for r in subs}
    # The listed manuscripts, not every directory under preprints/: upstream keeps a superseded
    # edition of a revised manuscript on disk beside its replacement, and a withdrawn manuscript's
    # directory ships only a README and the archived PDF, so a directory walk is not the
    # manuscript list.
    dirs = sorted(PREPRINTS / name for name in by_slug)
    rows = [row_for(d, by_slug[d.name]["fam"], "preprints/" + d.name + "/" +
                    pathlib.PurePosixPath(by_slug[d.name]["path"]).name)
            for d in dirs]
    return rows, subs, dirs


def env_variants(dirs):
    """(six-name total, declared-rule total, per-name counts under the declared rule)."""
    six = 0
    per_name = collections.Counter()
    for d in dirs:
        ts = preprints.texts(preprints.tex_files(d))
        declared = preprints.declared_envs(ts)
        six += preprints.six_count(ts)
        per_name.update(preprints.per_name_counts(ts, declared))
    return six, sum(per_name.values()), per_name


def write(rows):
    tsv.write_csv(OUT, COLUMNS, rows)


def report(rows, subs, dirs):
    ledger = tsv.read_rows(LEDGER_TSV)
    fams = {r["fam"] for r in ledger}
    paps = {r["fam"]: int(r["paps"]) for r in ledger}
    slugs = [r["path"].split("/")[1] for r in subs]

    disk = sorted(p for p in PREPRINTS.iterdir() if p.is_dir())
    listed = {d.name for d in dirs}
    unlisted = [d.name for d in disk if d.name not in listed]
    notices = [n for n in unlisted
               if "Withdrawal notice" in read_text(PREPRINTS / n / "README.md")]
    extra = [s for s in slugs if s not in {d.name for d in disk}]
    pdf_diff = sum(1 for r in rows
                   if not (ROOT / r["pdf"]).exists()
                   or (ROOT / r["pdf"]).stat().st_size == 0)
    fam_diff = [r["fam"] for r in rows if r["fam"] not in fams]
    per_fam = {f: sum(1 for r in rows if r["fam"] == f) for f in {r["fam"] for r in rows}}
    paps_diff = [f for f, n in per_fam.items() if paps.get(f) != n]

    outcomes = {"name-main": 0, "name-paper": 0, "single-root": 0, "flagged": 0}
    single_names = collections.Counter()
    multi = []
    for d in dirs:
        roots = preprints.roots_of(d)
        main, rule = preprints.main_tex_of(roots)
        if rule == "single-root":
            outcomes["single-root"] += 1
            single_names[main.name] += 1
        elif rule == "flagged":
            outcomes["flagged"] += 1
        elif main.name == "main.tex":
            outcomes["name-main"] += 1
        else:
            outcomes["name-paper"] += 1
        if len(roots) > 1:
            multi.append(d.name)
    substring_multi = sum(
        1 for d in dirs
        if len([f for f in d.rglob("*.tex")
                if "\\documentclass" in read_text(f)]) > 1)
    main_no_dc = [str(f.relative_to(PREPRINTS)) for d in dirs for f in d.rglob("main.tex")
                  if not DOCCLASS.search(read_text(f))]
    pdf_per_dir = {len(list(d.glob("*.pdf"))) for d in dirs}

    # Independent check: the release's own manuscript list, parsed from overview.tex with the
    # paren-aware manuscript-path rule, not from the subfindings rows this table's pdf column is
    # derived from.
    _, ov_fams = overview.parse_overview()
    ov_paths = sorted(p for f in ov_fams for p in ov_fams[f]["tex_paps"])
    mine = sorted(r["pdf"] for r in rows)
    ov_only = sorted(set(ov_paths) - set(mine))
    mine_only = sorted(set(mine) - set(ov_paths))
    by_fam = {}
    for r in rows:
        by_fam.setdefault(r["fam"], set()).add(r["pdf"])
    fam_path_diff = [f for f in ov_fams
                     if ov_fams[f]["tex_paps"] and by_fam.get(f, set()) != set(ov_fams[f]["tex_paps"])]

    print(f"rows written                     {len(rows)}")
    print(f"listed manuscript dirs           {len(dirs)}")
    print(f"preprint dirs on disk            {len(disk)}  unlisted {len(unlisted)} = "
          f"{len(unlisted) - len(notices)} superseded + {len(notices)} withdrawal notices")
    print(f"subfindings slugs not on disk    {len(extra)} {extra[:3]}")
    print(f"empty/missing PDF files          {pdf_diff}")
    print(f"fams outside the ledger          {len(fam_diff)} {fam_diff[:3]}")
    print(f"per-family row count vs ledger paps, differences  {len(paps_diff)} {paps_diff[:3]}")
    print(f"overview.tex PAP paths {len(ov_paths)} ({len(set(ov_paths))} distinct)  "
          f"sources.tsv pdf {len(mine)} ({len(set(mine))} distinct)")
    print(f"paths in overview.tex not in sources.tsv  {len(ov_only)} {ov_only[:3]}")
    print(f"paths in sources.tsv not in overview.tex  {len(mine_only)} {mine_only[:3]}")
    print(f"families whose path set differs from overview.tex  {len(fam_path_diff)} "
          f"{fam_path_diff[:3]}")
    print(f"main-file rule: main.tex {outcomes['name-main']}  paper.tex {outcomes['name-paper']}"
          f"  single-root {outcomes['single-root']}  flagged {outcomes['flagged']}")
    print(f"single-root file names  {text.fmt_counter(single_names)}")
    print(f"multi-root dirs (line-start rule) {len(multi)}: {multi}")
    print(f"multi-root dirs (substring rule)  {substring_multi}")
    print(f"main.tex files with no \\documentclass  {len(main_no_dc)}")
    print(f"top-level PDFs per dir (set of counts) {sorted(pdf_per_dir)}")
    for c in ("tex", "bib", "sections", "subsections", "subsubsections", "proofs", "thms",
              "abstract", "tex_bytes"):
        print(f"sum {c:16} {sum(int(r[c]) for r in rows)}")
    six, decl, per_name = env_variants(dirs)
    added = {n: c for n, c in per_name.items() if n not in SIX}
    print(f"thms rule (declared minus non-statement) {decl}  = sum of thms column "
          f"{sum(int(r['thms']) for r in rows)}")
    print(f"six-name list (theorem/lemma/proposition/corollary/claim/conjecture) {six}"
          f"  gap {decl - six}")
    print(f"names the declared rule adds: {text.fmt_counter(added)}")
    print(f"dirs with main_tex empty         {sum(1 for r in rows if not r['main_tex'])}")
    print(f"dirs with an abstract            {sum(int(r['abstract']) for r in rows)} of {len(rows)}")


def main():
    rows, subs, dirs = build()
    write(rows)
    report(rows, subs, dirs)


if __name__ == "__main__":
    main()
