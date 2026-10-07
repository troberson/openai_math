# Name: thomason

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 35 capitalized occurrences, 24 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | — | — | — | — | yes | — |
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | — | — | — | — | yes | yes |
| [193](../algebra/193-serres-intersection-multiplicity-conjecture.md) | Serre's intersection-multiplicity conjecture | — | — | — | — | yes | — |
| [314](../topology/314-chromatic-smith-fixed-point-problem-for-finite-p-groups.md) | The chromatic Smith fixed-point problem for finite $p$-groups | — | — | — | — | yes | — |
| [317](../topology/317-thomason-model-structures-in-every-strict-higher-dimension.md) | Thomason model structures in every strict higher dimension | yes | yes | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Hadwigers-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) |
| [`A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) |
| [`Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026`](../../../preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/) | [314](../topology/314-chromatic-smith-fixed-point-problem-for-finite-p-groups.md) | prose | [Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026.pdf](../../../preprints/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026/Cyclic-Length-and-Chromatic-Fixed-Point-Loss-September-24-2026.pdf) |
| [`Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026`](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [manuscript.pdf](../../../preprints/Global-Arthur-Enhancements-of-Cuspidal-Excursion-Parameters-October-5-2026/manuscript.pdf) |
| [`Positivity-of-Serres-Intersection-Multiplicity-September-23-2026`](../../../preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/) | [193](../algebra/193-serres-intersection-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Positivity-of-Serres-Intersection-Multiplicity-September-23-2026/paper.pdf) |
| [`Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026`](../../../preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/) | [317](../topology/317-thomason-model-structures-in-every-strict-higher-dimension.md) | prose + title | [paper.pdf](../../../preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `thomason`: accents folded, dash variants unified, possessives stripped, case lowered. `Thomason` · `Thomason's`

