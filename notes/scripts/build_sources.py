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
"""
import collections
import csv
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_catalog as B  # for the paren-aware manuscript-path regex

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRE = ROOT / "preprints"
OUT = ROOT / "notes" / "sources.tsv"
SUBF = ROOT / "notes" / "subfindings.tsv"
LEDGER = ROOT / "notes" / "catalog.tsv"

COLUMNS = ["dir", "fam", "pdf", "main_tex", "roots", "tex", "bib", "sections", "subsections",
           "subsubsections", "proofs", "thms", "abstract", "tex_bytes"]

# Environments declared by \newtheorem that state nothing.
NON_STATEMENT = {"definition", "remark", "example", "notation", "convention", "procedure",
                 "construction", "scope", "abstract"}

# The six-name list the epic quotes, kept so the report prints the figure the bead's prose uses.
SIX = {"theorem", "lemma", "proposition", "corollary", "claim", "conjecture"}

DOCCLASS = re.compile(r"^\s*\\documentclass", re.M)
ABSTRACT = re.compile(r"^\s*\\begin\{abstract\}", re.M)
BEGIN = re.compile(r"\\begin\{([A-Za-z*]+)\}")
NEWTHEOREM = re.compile(r"\\newtheorem\*?\{([A-Za-z]+)\}")


def tsv(path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def fmt(counter):
    """Counter -> 'name n, name n, ...' sorted by count desc, then name."""
    return ", ".join(f"{n} {c}" for n, c in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])))


def roots_of(d):
    """`.tex` files under `d` that declare `\\documentclass` at the start of a line."""
    out = [f for f in d.rglob("*.tex")
           if DOCCLASS.search(f.read_text(encoding="utf-8", errors="replace"))]
    return sorted(out, key=lambda f: (len(f.relative_to(d).parts), str(f.relative_to(d))))


def main_tex_of(roots):
    """Prefer main.tex, then paper.tex, then the single root; flag, never guess, the rest."""
    for name in ("main.tex", "paper.tex"):
        hits = [f for f in roots if f.name == name]
        if hits:
            return hits[0], "name"
    if len(roots) == 1:
        return roots[0], "single-root"
    return None, "flagged"


def row_for(d, fam, pdf):
    tex_files = sorted(d.rglob("*.tex"))
    texts = [f.read_text(encoding="utf-8", errors="replace") for f in tex_files]
    declared = set()
    for t in texts:
        declared.update(NEWTHEOREM.findall(t))
    declared -= NON_STATEMENT
    thms = proofs = 0
    sections = subsections = subsub = 0
    abstract = 0
    for t in texts:
        proofs += len(re.findall(r"\\begin\{proof\}", t))
        thms += len([m for m in BEGIN.findall(t) if m in declared])
        sections += len(re.findall(r"\\section\*?\{", t))
        subsections += len(re.findall(r"\\subsection\*?\{", t))
        subsub += len(re.findall(r"\\subsubsection\*?\{", t))
        if ABSTRACT.search(t):
            abstract = 1
    roots = roots_of(d)
    main, _ = main_tex_of(roots)
    return {
        "dir": d.name,
        "fam": fam,
        "pdf": pdf,
        "main_tex": "" if main is None else str(main.relative_to(PRE)),
        "roots": len(roots),
        "tex": len(tex_files),
        "bib": len(list(d.rglob("*.bib"))),
        "sections": sections,
        "subsections": subsections,
        "subsubsections": subsub,
        "proofs": proofs,
        "thms": thms,
        "abstract": abstract,
        "tex_bytes": sum(f.stat().st_size for f in tex_files),
    }


def build():
    subs = [r for r in tsv(SUBF) if r["kind"] == "manuscript"]
    by_slug = {r["path"].split("/")[1]: r for r in subs}
    # The listed manuscripts, not every directory under preprints/: upstream keeps a superseded
    # edition of a revised manuscript on disk beside its replacement, and a withdrawn manuscript's
    # directory ships only a README and the archived PDF, so a directory walk is not the
    # manuscript list.
    dirs = sorted(PRE / name for name in by_slug)
    rows = [row_for(d, by_slug[d.name]["fam"], "preprints/" + d.name + "/" +
                    pathlib.PurePosixPath(by_slug[d.name]["path"]).name)
            for d in dirs]
    return rows, subs, dirs


def env_variants(dirs):
    """(six-name total, declared-rule total, per-name counts under the declared rule)."""
    six = 0
    per_name = collections.Counter()
    for d in dirs:
        texts = [f.read_text(encoding="utf-8", errors="replace") for f in d.rglob("*.tex")]
        declared = set()
        for t in texts:
            declared.update(NEWTHEOREM.findall(t))
        declared -= NON_STATEMENT
        for t in texts:
            found = BEGIN.findall(t)
            six += sum(1 for m in found if m in SIX)
            per_name.update(m for m in found if m in declared)
    return six, sum(per_name.values()), per_name


def write(rows):
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in COLUMNS])


def report(rows, subs, dirs):
    ledger = tsv(LEDGER)
    fams = {r["fam"] for r in ledger}
    paps = {r["fam"]: int(r["paps"]) for r in ledger}
    slugs = [r["path"].split("/")[1] for r in subs]

    disk = sorted(p for p in PRE.iterdir() if p.is_dir())
    listed = {d.name for d in dirs}
    unlisted = [d.name for d in disk if d.name not in listed]
    notices = [n for n in unlisted
               if "Withdrawal notice" in (PRE / n / "README.md").read_text(encoding="utf-8",
                                                                           errors="replace")]
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
        roots = roots_of(d)
        main, rule = main_tex_of(roots)
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
                if "\\documentclass" in f.read_text(encoding="utf-8", errors="replace")]) > 1)
    main_no_dc = [str(f.relative_to(PRE)) for d in dirs for f in d.rglob("main.tex")
                  if not DOCCLASS.search(f.read_text(encoding="utf-8", errors="replace"))]
    pdf_per_dir = {len(list(d.glob("*.pdf"))) for d in dirs}

    # Independent check: the release's own manuscript list, parsed from overview.tex with the
    # paren-aware PAP regex, not from the subfindings rows this table's pdf column is derived from.
    _, ov_fams = B.parse_overview()
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
    print(f"single-root file names  {fmt(single_names)}")
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
    print(f"names the declared rule adds: {fmt(added)}")
    print(f"dirs with main_tex empty         {sum(1 for r in rows if not r['main_tex'])}")
    print(f"dirs with an abstract            {sum(int(r['abstract']) for r in rows)} of {len(rows)}")


def main():
    rows, subs, dirs = build()
    write(rows)
    report(rows, subs, dirs)


if __name__ == "__main__":
    main()
