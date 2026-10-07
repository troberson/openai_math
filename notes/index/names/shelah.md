# Name: shelah

6 families · subject name · 1 carried by a title or a declaration · 5 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 42 capitalized occurrences, 21 of them mid-sentence, 3 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) | Superexponential van der Waerden numbers | — | — | — | — | yes | yes |
| [172](../combinatorics/172-classification-of-finite-euclidean-ramsey-configurations.md) | Classification of finite Euclidean Ramsey configurations | — | — | — | — | yes | yes |
| [240](../mathematical-logic/240-shelahs-eventual-categoricity-conjecture.md) | Shelah's eventual categoricity conjecture | yes | — | — | — | yes | yes |
| [241](../mathematical-logic/241-rigidity-of-the-turing-degrees.md) | Rigidity of the Turing degrees | — | — | — | — | yes | — |
| [243](../mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md) | Choiceless counting does not capture polynomial time | — | — | — | — | yes | yes |
| [323](../functional-analysis/323-relative-independence-of-the-separable-quotient-problem.md) | Relative independence of the separable quotient problem | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026`](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/) | [240](../mathematical-logic/240-shelahs-eventual-categoricity-conjecture.md) | prose | [paper.pdf](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/paper.pdf) |
| [`A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026`](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/) | [172](../combinatorics/172-classification-of-finite-euclidean-ramsey-configurations.md) | prose | [paper.pdf](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf) |
| [`Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/) | [243](../mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md) | prose | [paper.pdf](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/paper.pdf) |
| [`Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026`](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/) | [240](../mathematical-logic/240-shelahs-eventual-categoricity-conjecture.md) | prose | [paper.pdf](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/paper.pdf) |
| [`Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026`](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/) | [160](../combinatorics/160-superexponential-van-der-waerden-numbers.md) | prose | [paper.pdf](../../../preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf) |
| [`Rigidity-of-the-Turing-degrees-September-24-2026`](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/) | [241](../mathematical-logic/241-rigidity-of-the-turing-degrees.md) | prose | [paper.pdf](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/paper.pdf) |
| [`Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/) | [243](../mathematical-logic/243-choiceless-counting-does-not-capture-polynomial-time.md) | prose | [paper.pdf](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `shelah`: accents folded, dash variants unified, possessives stripped, case lowered. `Shelah` · `Shelah's`

