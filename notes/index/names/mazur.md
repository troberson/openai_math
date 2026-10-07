# Name: mazur

7 families · subject name · 1 carried by a title or a declaration · 6 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 35 capitalized occurrences, 21 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 6 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | — | — | yes | — |
| [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | Hilbert's tenth problem over $\mathbb Q$ | — | — | — | — | yes | yes |
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity | yes | yes | — | — | yes | yes |
| [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | Zilber--Pink in abelian varieties and the Siegel threefold | — | — | — | — | — | yes |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | The Mahler conjectures and symplectic width | — | — | — | — | yes | — |
| [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) | Tingley's sphere-isometry problem | — | — | — | — | yes | — |
| [323](../functional-analysis/323-relative-independence-of-the-separable-quotient-problem.md) | Relative independence of the separable quotient problem | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-positive-solution-to-Tingleys-problem-September-23-2026`](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/) | [322](../functional-analysis/322-tingleys-sphere-isometry-problem.md) | prose | [paper.pdf](../../../preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf) |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [exact-bsd-low-selmer-corank.pdf](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/exact-bsd-low-selmer-corank.pdf) |
| [`Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/) | [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | prose + title | [paper.pdf](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/paper.pdf) |
| [`Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/) | [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | prose | [main.pdf](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf) |
| [`Relative-independence-of-the-separable-quotient-problem-September-23-2026`](../../../preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/) | [323](../functional-analysis/323-relative-independence-of-the-separable-quotient-problem.md) | prose | [paper.pdf](../../../preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf) |
| [`The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/) | [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | prose | [two-adic-hecke.pdf](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf) |
| [`The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026`](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose | [paper.pdf](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) |
| [`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026`](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [paper.pdf](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `mazur`: accents folded, dash variants unified, possessives stripped, case lowered. `Mazur` · `Mazur's`

