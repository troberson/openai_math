# Name: brunn

6 families · subject name · 1 carried by a title or a declaration · 6 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 26 capitalized occurrences, 20 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 6 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [038](../algebraic-and-complex-geometry/038-fujitas-freeness-conjecture.md) | Fujita's freeness conjecture | — | — | — | — | yes | — |
| [088](../convex-and-metric-geometry/088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md) | Petty's projection-volume conjecture and simplex counterexamples | — | — | — | — | yes | — |
| [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) | The logarithmic Brunn--Minkowski conjecture | yes | yes | yes | yes | yes | — |
| [224](../probability-and-statistical-mechanics/224-critical-and-near-critical-universality-for-voronoi-percolation.md) | Critical and near-critical universality for Voronoi percolation | — | — | — | — | yes | — |
| [227](../probability-and-statistical-mechanics/227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) | The dynamical phase transition in the Sherrington--Kirkpatrick model | — | — | — | — | yes | — |
| [232](../probability-and-statistical-mechanics/232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md) | Gaussian fields and SLE interfaces for Lipschitz heights | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026`](../../../preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/) | [224](../probability-and-statistical-mechanics/224-critical-and-near-critical-universality-for-voronoi-percolation.md) | prose | [voronoi-pivotal-amplitude.pdf](../../../preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/voronoi-pivotal-amplitude.pdf) |
| [`Fujitas-freeness-conjecture-September-23-2026`](../../../preprints/Fujitas-freeness-conjecture-September-23-2026/) | [038](../algebraic-and-complex-geometry/038-fujitas-freeness-conjecture.md) | prose | [Fujitas-freeness-conjecture-September-23-2026.pdf](../../../preprints/Fujitas-freeness-conjecture-September-23-2026/Fujitas-freeness-conjecture-September-23-2026.pdf) |
| [`Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/) | [088](../convex-and-metric-geometry/088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md) | prose | [paper.pdf](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf) |
| [`Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026`](../../../preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/) | [227](../probability-and-statistical-mechanics/227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) | prose | [paper.pdf](../../../preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/paper.pdf) |
| [`The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026`](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/) | [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) | prose + title | [paper.pdf](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf) |
| [`Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026`](../../../preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026/) | [232](../probability-and-statistical-mechanics/232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md) | prose | [paper.pdf](../../../preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [LogBrunnMinkowski](../../../lean/ComparatorChallenges/LogBrunnMinkowski.json) | `OAI.LogBrunnMinkowski.main` | [BrunnMinkowski.lean](../../../lean/OAI/Geometry/LogVolume/BrunnMinkowski.lean) | [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) |

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) | Even logarithmic Brunn--Minkowski inequality |
| [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) | Symmetric $L_p$ Brunn--Minkowski inequality |

## Spelling variants

One surface form in prose: `Brunn`. The normalized key is `brunn`.

