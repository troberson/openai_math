# The manuscript source surface

Measured 2026-10-08 by `python3 notes/scripts/build_sources.py`, which writes `notes/sources.tsv` —
**719 rows, 14 columns**, one row per manuscript the release lists. The script reads the manuscript
trees as text: no `lake`, `lean`, `lake exe cache get`, or comparator run, no PDF parsing, no `.lean`
file opened. Run it twice and diff: the TSV is byte-identical and the report is identical. Every
count below comes from that report, so quote a number with the rule that yields it.

The row set is the manuscript list, not the directory list. `preprints/` holds **749** directories:
the **719** the release lists, **27** superseded editions upstream keeps beside their replacements,
and **3** withdrawal notices. A superseded directory is not a manuscript row, so the table's counts
describe the listed corpus only.

## The columns

| Column | Rule | Corpus total |
|---|---|---|
| `dir` | `preprints/` directory name — manuscript ownership is the path component after `preprints` | 719 distinct |
| `fam` | Family id, from the manuscript rows of `notes/subfindings.tsv` | 372 distinct |
| `pdf` | Manuscript PDF path, reconciled against `overview.tex` | 719, all on disk, all non-empty |
| `main_tex` | Resolved main file, rule below | 719 filled, **0** empty |
| `roots` | `.tex` files declaring `\documentclass` **at line start** | **724** over 719 dirs: 715 with 1, 3 with 2, 1 with 3 |
| `tex` | All `.tex` files under the dir | **7,705** (max 201, mean 10.72 per dir) |
| `bib` | `.bib` files under the dir | **500**; **225** dirs carry none |
| `sections` | `\section*?{` | **6,019** |
| `subsections` | `\subsection*?{` | **16,297** |
| `subsubsections` | `\subsubsection*?{` | **316** |
| `proofs` | `\begin{proof}` | **20,341**; **1** dir carries none |
| `thms` | Statement environments, rule below | **21,288** |
| `abstract` | Line-start `\begin{abstract}` anywhere in the dir | **719 of 719** |
| `tex_bytes` | Sum of `.tex` file sizes | **127,456,942** (mean 177,270 per dir) |

`abstract` does not discriminate — every manuscript ships one — and is kept because the bead asked
for it. `proofs` and `thms` do: the one zero-`\begin{proof}` dir
(`A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026`)
carries 3 `.tex` files and 1 statement environment, which is the shape `math-hqd.3` is about.

## Main-file resolution

A **root** is a `.tex` file with `\documentclass` at the start of a line. Resolution prefers a root
named `main.tex`, then a root named `paper.tex`, then the single root; a dir with several roots and
no `main.tex`/`paper.tex` is flagged with an empty `main_tex`, never guessed. Outcomes:
**main.tex 494, paper.tex 209, single-root 16, flagged 0.**

The name test is applied to roots, not to files, because **12** `main.tex` files in the corpus
declare no `\documentclass` — companion and build copies — so a bare-name preference would pick a
non-root file.

The 16 single-root dirs resolve to: `preamble.tex` **7**, `manuscript.tex` **2**, `common.tex` **2**,
and **5** singletons (`invariant-sk.tex`, `critical-percolation-z3.tex`,
`positive-eigenvalues-relative-su2-bfss.tex`, `strong-ulam-stability.tex`, `paper2.tex`). The bead's
spec records 17 with `preamble.tex` 8 and 4 singletons; the split never reproduced — one singleton is
counted as a `preamble.tex` there — and the 17 is now 16, because the withdrawn
`Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026` was the dir that
resolved to `build/manuscript.tex`, and its notice ships no `.tex` file at all.

**Every one of the 719 resolved main files sits under a `build/` directory.** The release ships the
manuscript source as a build tree; there is no top-level `.tex` root anywhere in `preprints/`.

The 4 multi-root dirs, with the file each resolves to:

| Roots | Directory | Resolves to |
|---|---|---|
| 3 | `A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026` | `build/main.tex` |
| 2 | `Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026` | `build/main.tex` |
| 2 | `Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026` | `build/main.tex` |
| 2 | `Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026` | `build/main.tex` |

## 715/4 vs 714/5: the line-start rule is load-bearing

The bead's spec measures 717 dirs with exactly one `\documentclass` file and **5** with two or
three. That is a substring count of the command name, over the 722-dir corpus it measured; over the
719 dirs the release lists today the same substring rule reads 714 and 5. Requiring the command at
line start reads **715** and **4**. The rules differ in exactly one directory,
`Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026`, whose second "root" is a bundled
PGF documentation macro file that defines a macro *mentioning* the command — `preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/build/tools/tex/latex/pgf/doc/pgfmanual-en-macros.tex:1177`:

```
\def\extractclass#1#2@{%
\item{{{\ttfamily\char`\\documentclass}#2{\ttfamily\char`\{\declare{#1}\char`\}}}}%
  \index{#1@\protect\texttt{#1} class}%
```

The directory's real root is `preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/build/paper.tex:1`:

```
\documentclass[11pt]{article}
```

The rule changes the multi-root count, not the answer: main-file resolution picks the same file for
**all 719** directories under either rule (0 differences), because the name preference fires before
the root count matters.

## 21,288 and 21,203: two honest counts of the same thing

`thms` counts `\begin{X}` for X declared by `\newtheorem` **in the same directory**, minus the names
that state nothing (`definition`, `remark`, `example`, `notation`, `convention`, `procedure`,
`construction`, `scope`, `abstract`). Every theorem-like environment used in the corpus is locally
declared, so this agrees with the union of declared names and a fixed standard list to the
occurrence — 21,288 both ways.

The epic quotes **21,203** for "theorem/lemma/proposition/corollary/claim/conjecture environments".
That is the six-name list, and it reproduces exactly, corpus-wide and restricted to declared names.
The 85 gap is names the declared rule counts that the six omit: `assumption` 22, `foundation` 13,
`auxproposition` 8, `hypothesis` 8, `auxlemma` 7, `standinginput` 5, `externalinput` 4,
`maintheorem` 4, `companionresults` 3, `unnumberedproposition` 3, `maincorollary` 2, `principle` 2,
`verification` 2, `question` 1, `thm` 1. The TSV column carries the declared-rule figure.

## Reconciliation, all zero

The report's reconciliation lines, from the run that wrote the shipped TSV:

- rows written **719**, listed manuscript dirs **719**, preprint dirs on disk **749**;
- subfindings slugs not on disk **0**;
- empty or missing PDF files **0**;
- families outside `notes/catalog.tsv` **0**; per-family row count vs ledger `paps` differences **0**;
- `overview.tex` manuscript paths (the paren-aware `PAP` regex) **719** distinct vs `sources.tsv`
  `pdf` **719** distinct; paths in one and not the other **0** and **0**; families whose path set
  differs from `overview.tex` **0**.

The `pdf` column is derived from `notes/subfindings.tsv`, so the last three lines are the
independent check: they re-parse the release's own list out of `overview.tex` with
`build_catalog.parse_overview()` rather than trusting the table's own source.

Diffing the 722-row table shipped before the Oct 7 merge against this 719-row table: 30 directories
leave (27 superseded editions, 3 withdrawal notices), 27 arrive (the new date-named editions), and
**0** cells change in the directories present in both. The merge moves directory names; it does not
re-measure a manuscript that stayed put.

## Not checked

- No manuscript was compiled and no `.tex` file was parsed as LaTeX — every count is a regex over
  text. `\begin{proof}` inside a comment, a verbatim block, or a macro definition counts.
- `\newtheorem` declarations are collected per directory, so a declaration in a file the manuscript
  never `\input`s still makes its environment names count.
- `main_tex` is a resolution under a stated rule, not a claim that the file is what the release
  compiled to ship the PDF.
- `tex_bytes` counts `.tex` only: no `.sty`, `.cls`, `.bbl`, image, or `.pdf` bytes are included.
- Bibliography files are counted, not parsed — that is `math-hqd.4`.
- The manuscript abstract text was not compared with the `overview.tex` abstract — that is
  `math-hqd.2`.
- Nothing here says a manuscript is formalized, correct, or read. The formalized flag lives in
  `notes/catalog.tsv` at **172** of 719 manuscripts, at source level under
  `lean/formalization.yaml` `review: status: unchecked`.
