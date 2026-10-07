# Name: song

11 families · subject name · 1 carried by a title or a declaration · 9 by prose · 7 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 30 capitalized occurrences, 16 of them mid-sentence, 7 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 9 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 7 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [037](../algebraic-and-complex-geometry/037-sharp-ordinary-double-point-volume-gap.md) | The sharp ordinary-double-point volume gap | — | — | — | — | yes | — |
| [052](../algebraic-and-complex-geometry/052-tangent-bundle-splittings-and-universal-covers.md) | Tangent-bundle splittings and universal covers | — | — | — | — | yes | — |
| [120](../theoretical-computer-science/120-almost-linear-time-exact-matching-in-general-graphs.md) | Almost-linear-time exact matching in general graphs | — | — | — | — | — | yes |
| [139](../theoretical-computer-science/139-subpolynomial-queries-for-log-concave-sampling.md) | Subpolynomial queries for log-concave sampling | — | — | — | — | — | yes |
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | — | — | — | — | yes | yes |
| [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | Counterexamples to Ryser's covering and Gy\'arf\'as's tree-cover conjectures | — | — | — | — | yes | yes |
| [175](../combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) | Talagrand's conjectures and graph decompositions at expectation thresholds | — | — | — | — | yes | — |
| [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | Conformal universality for weakly interacting and disordered Ising models | — | — | — | — | yes | yes |
| [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | Sharp singularity rates for symmetric sign matrices | — | — | — | — | yes | — |
| [277](../mathematical-physics/277-threshold-repetition-for-entangled-games.md) | Threshold repetition for entangled games | — | — | yes | — | yes | yes |
| [344](../differential-geometry/344-metric-blaschke-conjecture.md) | The metric Blaschke conjecture | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026`](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/) | [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | prose | [paper.pdf](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf) |
| [`A-counterexample-to-Hadwigers-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) |
| [`A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) |
| [`Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026`](../../../preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [paper.pdf](../../../preprints/Buffered-comparison-and-stopping-band-resolution-in-critical-Ising-September-23-2026/paper.pdf) |
| [`Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026`](../../../preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [paper.pdf](../../../preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/paper.pdf) |
| [`Talagrands-discrete-convexity-conjecture-September-23-2026`](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/) | [175](../combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) | prose | [paper.pdf](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf) |
| [`The-metric-Blaschke-theorem-September-23-2026`](../../../preprints/The-metric-Blaschke-theorem-September-23-2026/) | [344](../differential-geometry/344-metric-blaschke-conjecture.md) | prose | [paper.pdf](../../../preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf) |
| [`The-normalized-volume-gap-in-dimension-four-September-24-2026`](../../../preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/) | [037](../algebraic-and-complex-geometry/037-sharp-ordinary-double-point-volume-gap.md) | prose | [paper.pdf](../../../preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/paper.pdf) |
| [`The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026`](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/) | [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | prose | [biased-symmetric-sign-singularity.pdf](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/biased-symmetric-sign-singularity.pdf) |
| [`Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026`](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/) | [277](../mathematical-physics/277-threshold-repetition-for-entangled-games.md) | prose | [paper.pdf](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/paper.pdf) |
| [`Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/) | [052](../algebraic-and-complex-geometry/052-tangent-bundle-splittings-and-universal-covers.md) | prose | [paper.pdf](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [277](../mathematical-physics/277-threshold-repetition-for-entangled-games.md) | Song's conditioning estimate,
  \cite[Definition~4.3 and Lemma~4.4 |

## Spelling variants

Every form below normalizes to the key `song`: accents folded, dash variants unified, possessives stripped, case lowered. `Song` · `Song's`

