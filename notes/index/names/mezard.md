# Name: mezard

6 families · subject name · 1 carried by a title or a declaration · 5 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 17 capitalized occurrences, 10 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity | — | — | — | — | — | yes |
| [221](../probability-and-statistical-mechanics/221-m-parisi-formula-for-diluted-spin-glasses.md) | The M\'ezard--Parisi formula for diluted spin glasses | yes | yes | — | — | yes | yes |
| [222](../probability-and-statistical-mechanics/222-perceptron-free-energies-and-microscopic-jamming.md) | Perceptron free energies and microscopic jamming | — | — | — | — | yes | yes |
| [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | Sharp three- and four-state reconstruction thresholds | — | — | — | — | yes | yes |
| [234](../probability-and-statistical-mechanics/234-all-temperature-pressure-for-orthogonally-invariant-ising-spin-glasses.md) | All-temperature pressure for orthogonally invariant Ising spin glasses | — | — | — | — | yes | — |
| [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | Random-SAT thresholds, sharp variance and computability | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026`](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/) | [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | prose | [four-state-capacity.pdf](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf) |
| [`A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026`](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/) | [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | prose | [article.pdf](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/article.pdf) |
| [`All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026`](../../../preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/) | [234](../probability-and-statistical-mechanics/234-all-temperature-pressure-for-orthogonally-invariant-ising-spin-glasses.md) | prose | [paper.pdf](../../../preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/paper.pdf) |
| [`Computing-the-Random-3-SAT-Threshold-September-27-2026`](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/) | [235](../probability-and-statistical-mechanics/235-random-sat-thresholds-sharp-variance-and-computability.md) | prose | [article.pdf](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf) |
| [`The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/) | [221](../probability-and-statistical-mechanics/221-m-parisi-formula-for-diluted-spin-glasses.md) | prose + title | [paper.pdf](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf) |
| [`The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026`](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/) | [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | prose | [four-state-potts.pdf](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf) |
| [`The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026`](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/) | [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | prose | [paper.pdf](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf) |
| [`The-free-energy-of-the-Ising-random-perceptron-September-24-2026`](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/) | [222](../probability-and-statistical-mechanics/222-perceptron-free-energies-and-microscopic-jamming.md) | prose | [The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Mezard`. The normalized key is `mezard`.

