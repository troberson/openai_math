# The manuscript source surface

Measured 2026-10-07 by `python3 notes/scripts/build_sources.py`, which writes `notes/sources.tsv` —
**722 rows, 14 columns**, one row per manuscript. The script reads the manuscript trees as text: no
`lake`, `lean`, `lake exe cache get`, or comparator run, no PDF parsing, no `.lean` file opened. Run
it twice and diff: the TSV is byte-identical and the report is identical. Every count below comes
from that report, so quote a number with the rule that yields it.

## The columns

| Column | Rule | Corpus total |
|---|---|---|
| `dir` | `preprints/` directory name — manuscript ownership is the path component after `preprints` | 722 distinct |
| `fam` | Family id, from the manuscript rows of `notes/subfindings.tsv` | 372 distinct |
| `pdf` | Manuscript PDF path, reconciled against `overview.tex` | 722, all on disk, all non-empty |
| `main_tex` | Resolved main file, rule below | 722 filled, **0** empty |
| `roots` | `.tex` files declaring `\documentclass` **at line start** | **727** over 722 dirs: 718 with 1, 3 with 2, 1 with 3 |
| `tex` | All `.tex` files under the dir | **7,729** (max 201, mean 10.70 per dir) |
| `bib` | `.bib` files under the dir | **501**; **227** dirs carry none |
| `sections` | `\section*?{` | **6,047** |
| `subsections` | `\subsection*?{` | **16,411** |
| `subsubsections` | `\subsubsection*?{` | **314** |
| `proofs` | `\begin{proof}` | **20,449**; **1** dir carries none |
| `thms` | Statement environments, rule below | **21,402** |
| `abstract` | Line-start `\begin{abstract}` anywhere in the dir | **722 of 722** |
| `tex_bytes` | Sum of `.tex` file sizes | **127,982,216** (mean 177,261 per dir) |

`abstract` does not discriminate — every manuscript ships one — and is kept because the bead asked
for it. `proofs` and `thms` do: the one zero-`\begin{proof}` dir
(`A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026`)
carries 3 `.tex` files and 1 statement environment, which is the shape `math-hqd.3` is about.

## Main-file resolution

A **root** is a `.tex` file with `\documentclass` at the start of a line. Resolution prefers a root
named `main.tex`, then a root named `paper.tex`, then the single root; a dir with several roots and
no `main.tex`/`paper.tex` is flagged with an empty `main_tex`, never guessed. Outcomes:
**main.tex 495, paper.tex 210, single-root 17, flagged 0.**

The name test is applied to roots, not to files, because **12** `main.tex` files in the corpus
declare no `\documentclass` — companion and build copies — so a bare-name preference would pick a
non-root file.

The 17 single-root dirs resolve to: `preamble.tex` **7**, `manuscript.tex` **3**, `common.tex` **2**,
and **5** singletons (`invariant-sk.tex`, `critical-percolation-z3.tex`,
`positive-eigenvalues-relative-su2-bfss.tex`, `strong-ulam-stability.tex`, `paper2.tex`). The bead's
spec records the same 17 with `preamble.tex` 8 and 4 singletons; the 17 reproduces, the split does
not — one singleton is counted as a `preamble.tex` there.

**Every one of the 722 resolved main files sits under a `build/` directory.** The release ships the
manuscript source as a build tree; there is no top-level `.tex` root anywhere in `preprints/`.

The 4 multi-root dirs, with the file each resolves to:

| Roots | Directory | Resolves to |
|---|---|---|
| 3 | `A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026` | `build/main.tex` |
| 2 | `Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026` | `build/main.tex` |
| 2 | `Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026` | `build/main.tex` |
| 2 | `Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-5-2026` | `build/main.tex` |

## 718/4 vs 717/5: the line-start rule is load-bearing

The bead's spec measures **717** dirs with exactly one `\documentclass` file and **5** with two or
three. That is a substring count of the command name. Requiring the command at line start reads
**718** and **4**. The rules differ in exactly one directory,
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
**all 722** directories under either rule (0 differences), because the name preference fires before
the root count matters.

## 21,402 and 21,317: two honest counts of the same thing

`thms` counts `\begin{X}` for X declared by `\newtheorem` **in the same directory**, minus the names
that state nothing (`definition`, `remark`, `example`, `notation`, `convention`, `procedure`,
`construction`, `scope`, `abstract`). Every theorem-like environment used in the corpus is locally
declared, so this agrees with the union of declared names and a fixed standard list to the
occurrence — 21,402 both ways.

The epic quotes **21,317** for "theorem/lemma/proposition/corollary/claim/conjecture environments".
That is the six-name list, and it reproduces exactly, corpus-wide and restricted to declared names.
The 85 gap is names the declared rule counts that the six omit: `assumption` 22, `foundation` 13,
`auxproposition` 8, `hypothesis` 8, `auxlemma` 7, `standinginput` 5, `externalinput` 4,
`maintheorem` 4, `companionresults` 3, `unnumberedproposition` 3, `maincorollary` 2, `principle` 2,
`verification` 2, `question` 1, `thm` 1. The TSV column carries the declared-rule figure.

## Reconciliation, all zero

The report's reconciliation lines, from the run that wrote the shipped TSV:

- rows written **722**, preprint dirs **722**;
- dirs with no `subfindings.tsv` manuscript row **0**; subfindings slugs not on disk **0**;
- empty or missing PDF files **0**;
- families outside `notes/catalog.tsv` **0**; per-family row count vs ledger `paps` differences **0**;
- `overview.tex` manuscript paths (the paren-aware `PAP` regex) **722** distinct vs `sources.tsv`
  `pdf` **722** distinct; paths in one and not the other **0** and **0**; families whose path set
  differs from `overview.tex` **0**.

The `pdf` column is derived from `notes/subfindings.tsv`, so the last three lines are the
independent check: they re-parse the release's own list out of `overview.tex` with
`build_catalog.parse_overview()` rather than trusting the table's own source.

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
  `notes/catalog.tsv` at **162** of 722 manuscripts, at source level under
  `lean/formalization.yaml` `review: status: unchecked`.
