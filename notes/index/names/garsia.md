# Name: garsia

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 22 capitalized occurrences, 13 of them mid-sentence, 3 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [148](../dynamical-systems-and-ergodic-theory/148-dimension-formula-for-self-similar-measures-on-the-line.md) | The dimension formula for self-similar measures on the line | — | — | — | — | yes | yes |
| [153](../dynamical-systems-and-ergodic-theory/153-arithmetic-classification-of-bernoulli-convolutions.md) | Arithmetic classification of Bernoulli convolutions | — | — | yes | — | yes | yes |
| [169](../combinatorics/169-shareshian-wachs-e-positivity-conjecture.md) | The Shareshian--Wachs $e$-positivity conjecture | — | — | — | — | yes | yes |
| [220](../probability-and-statistical-mechanics/220-directional-zero-one-laws-and-ballisticity-in-random-environments.md) | Directional zero--one laws and ballisticity in random environments | — | — | — | — | yes | yes |
| [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | The three-quarter diameter exponent for honeycomb walks | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026`](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/) | [220](../probability-and-statistical-mechanics/220-directional-zero-one-laws-and-ballisticity-in-random-environments.md) | prose | [directional-zero-one-finite-range.pdf](../../../preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/directional-zero-one-finite-range.pdf) |
| [`A-directional-zero-one-law-under-strict-ellipticity-September-23-2026`](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/) | [220](../probability-and-statistical-mechanics/220-directional-zero-one-laws-and-ballisticity-in-random-environments.md) | prose | [paper.pdf](../../../preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf) |
| [`Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026`](../../../preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/) | [153](../dynamical-systems-and-ergodic-theory/153-arithmetic-classification-of-bernoulli-convolutions.md) | prose | [paper.pdf](../../../preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/paper.pdf) |
| [`Directional-transience-implies-ballisticity-September-23-2026`](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/) | [220](../probability-and-statistical-mechanics/220-directional-zero-one-laws-and-ballisticity-in-random-environments.md) | prose | [paper.pdf](../../../preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf) |
| [`Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026`](../../../preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/) | [169](../combinatorics/169-shareshian-wachs-e-positivity-conjecture.md) | prose | [paper.pdf](../../../preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf) |
| [`Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026`](../../../preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/) | [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | prose | [main.pdf](../../../preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/main.pdf) |
| [`The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026`](../../../preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/) | [148](../dynamical-systems-and-ergodic-theory/148-dimension-formula-for-self-similar-measures-on-the-line.md) | prose | [main.pdf](../../../preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [153](../dynamical-systems-and-ergodic-theory/153-arithmetic-classification-of-bernoulli-convolutions.md) | Garsia parameters, \citeGarsia1962 |
| [153](../dynamical-systems-and-ergodic-theory/153-arithmetic-classification-of-bernoulli-convolutions.md) | Garsia parameters, \citeGarsia1962 |

## Spelling variants

Every form below normalizes to the key `garsia`: accents folded, dash variants unified, possessives stripped, case lowered. `Garsia` · `Garsia's`

