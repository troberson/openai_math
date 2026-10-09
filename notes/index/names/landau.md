# Name: landau

10 families · subject name · 1 carried by a title or a declaration · 10 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 43 capitalized occurrences, 41 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 10 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [003](../number-theory/003-quasi-riemann-hypothesis.md) | The quasi-Riemann hypothesis | — | yes | — | — | yes | — |
| [013](../number-theory/013-ostmanns-inverse-goldbach-conjecture.md) | Ostmann's inverse Goldbach conjecture | — | — | — | — | yes | — |
| [090](../convex-and-metric-geometry/090-universal-optimality-of-the-triangular-lattice.md) | Universal optimality of the triangular lattice | — | — | — | — | yes | — |
| [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | The sharp distortion of edit distance into $\ell_1$ | — | — | — | — | yes | — |
| [121](../theoretical-computer-science/121-almost-linear-expected-time-approximation-of-edit-distance.md) | Almost-linear expected-time approximation of edit distance | — | — | — | — | yes | yes |
| [215](../probability-and-statistical-mechanics/215-massive-continuum-limits-and-exact-mass-asymptotics-for-planar-o-n-models.md) | Massive continuum limits and exact mass asymptotics for planar $O(n)$ models | — | — | — | — | yes | yes |
| [232](../probability-and-statistical-mechanics/232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md) | Gaussian fields and SLE interfaces for Lipschitz heights | — | — | — | — | yes | — |
| [265](../mathematical-physics/265-two-dimensional-gapped-area-law.md) | The two-dimensional gapped area law | — | — | — | — | yes | yes |
| [269](../mathematical-physics/269-laughlin-gap-and-stability-under-scalar-disorder.md) | The Laughlin gap and stability under scalar disorder | — | — | — | — | yes | — |
| [363](../partial-differential-equations/363-boltzmann-nonuniqueness-with-exact-local-conservation.md) | Boltzmann nonuniqueness with exact local conservation | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026`](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/) | [269](../mathematical-physics/269-laughlin-gap-and-stability-under-scalar-disorder.md) | prose | [A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf](../../../preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf) |
| [`A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026`](../../../preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/) | [265](../mathematical-physics/265-two-dimensional-gapped-area-law.md) | prose | [paper.pdf](../../../preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf) |
| [`An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026`](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/) | [121](../theoretical-computer-science/121-almost-linear-expected-time-approximation-of-edit-distance.md) | prose | [paper.pdf](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf) |
| [`Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026`](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/) | [215](../probability-and-statistical-mechanics/215-massive-continuum-limits-and-exact-mass-asymptotics-for-planar-o-n-models.md) | prose | [paper.pdf](../../../preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf) |
| [`Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026`](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/) | [099](../convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md) | prose | [paper.pdf](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf) |
| [`Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026`](../../../preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/) | [363](../partial-differential-equations/363-boltzmann-nonuniqueness-with-exact-local-conservation.md) | prose | [paper.pdf](../../../preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/paper.pdf) |
| [`Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026`](../../../preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/) | [363](../partial-differential-equations/363-boltzmann-nonuniqueness-with-exact-local-conservation.md) | prose | [paper.pdf](../../../preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf) |
| [`The-Quasi-Riemann-Hypothesis-October-5-2026`](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/) | [003](../number-theory/003-quasi-riemann-hypothesis.md) | prose | [paper2.pdf](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) |
| [`Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026`](../../../preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/) | [090](../convex-and-metric-geometry/090-universal-optimality-of-the-triangular-lattice.md) | prose | [paper.pdf](../../../preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf) |
| [`Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026`](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/) | [269](../mathematical-physics/269-laughlin-gap-and-stability-under-scalar-disorder.md) | prose | [uniform-stability-spherical-laughlin-gap.pdf](../../../preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/uniform-stability-spherical-laughlin-gap.pdf) |
| [`Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026`](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/) | [003](../number-theory/003-quasi-riemann-hypothesis.md) | prose + title | [paper.pdf](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) |
| [`Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026`](../../../preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026/) | [232](../probability-and-statistical-mechanics/232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md) | prose | [paper.pdf](../../../preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026/paper.pdf) |
| [`Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026`](../../../preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026/) | — | prose | — |
| [`the-additive-indecomposability-of-the-primes-September-24-2026`](../../../preprints/the-additive-indecomposability-of-the-primes-September-24-2026/) | [013](../number-theory/013-ostmanns-inverse-goldbach-conjecture.md) | prose | [paper.pdf](../../../preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `landau`: accents folded, dash variants unified, possessives stripped, case lowered. `Landau` · `Landau's`

