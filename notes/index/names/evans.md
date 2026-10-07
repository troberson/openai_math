# Name: evans

12 families · subject name · 1 carried by a title or a declaration · 10 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 28 capitalized occurrences, 15 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 10 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [085](../real-and-complex-analysis/085-endpoint-regularity-of-the-planar-centered-maximal-function.md) | Endpoint regularity of the planar centered maximal function | — | — | — | — | — | yes |
| [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) | The logarithmic Brunn--Minkowski conjecture | — | — | — | — | yes | — |
| [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | The higher-dimensional Erd\H{o}s distinct-distances conjecture | — | — | — | — | yes | — |
| [167](../combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md) | Pinned distances and a power saving for planar unit distances | — | — | — | — | — | yes |
| [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | Eisenbud--Green--Harris and lex-plus-powers in characteristic zero | — | — | — | — | yes | — |
| [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | Sharp three- and four-state reconstruction thresholds | — | — | — | — | yes | yes |
| [236](../probability-and-statistical-mechanics/236-factor-of-iid-threshold-for-free-ising-states-on-trees.md) | The factor-of-IID threshold for free Ising states on trees | — | — | — | — | yes | yes |
| [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | The three-quarter diameter exponent for honeycomb walks | — | — | — | — | yes | — |
| [338](../differential-geometry/338-yaus-uniformization-conjecture.md) | Yau's uniformization conjecture | — | — | — | — | yes | — |
| [350](../differential-geometry/350-yaus-nodal-conjecture-surfaces-and-counterexamples.md) | Yau's nodal conjecture: surfaces and counterexamples | — | — | — | — | yes | yes |
| [368](../partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md) | The three-dimensional Ball--Evans approximation problem | yes | — | — | — | yes | — |
| [377](../partial-differential-equations/377-interior-c-1-regularity-for-infinity-harmonic-functions.md) | Interior $C^{1,\alpha}$ regularity for infinity-harmonic functions | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026`](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/) | [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | prose | [four-state-capacity.pdf](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf) |
| [`Cylinder-loop-weights-and-planar-nesting-September-26-2026`](../../../preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/) | [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | prose | [main.pdf](../../../preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/main.pdf) |
| [`Marked-polygon-correlations-and-one-arc-bounds-September-26-2026`](../../../preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026/) | [237](../probability-and-statistical-mechanics/237-three-quarter-diameter-exponent-for-honeycomb-walks.md) | prose | [main.pdf](../../../preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026/main.pdf) |
| [`Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026`](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/) | [350](../differential-geometry/350-yaus-nodal-conjecture-surfaces-and-counterexamples.md) | prose | [paper.pdf](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf) |
| [`Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/) | [368](../partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md) | prose | [main.pdf](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf) |
| [`Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/) | [368](../partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md) | prose | [main.pdf](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf) |
| [`The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026`](../../../preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/) | [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | prose | [paper.pdf](../../../preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/paper.pdf) |
| [`The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026`](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/) | [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | prose | [four-state-potts.pdf](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf) |
| [`The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026`](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/) | [229](../probability-and-statistical-mechanics/229-sharp-three-and-four-state-reconstruction-thresholds.md) | prose | [paper.pdf](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf) |
| [`The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/) | [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | prose | [paper.pdf](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf) |
| [`The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026`](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/) | [091](../convex-and-metric-geometry/091-logarithmic-brunn-minkowski-conjecture.md) | prose | [paper.pdf](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf) |
| [`The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026`](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/) | [236](../probability-and-statistical-mechanics/236-factor-of-iid-threshold-for-free-ising-states-on-trees.md) | prose | [article.pdf](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/article.pdf) |
| [`Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026`](../../../preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/) | [377](../partial-differential-equations/377-interior-c-1-regularity-for-infinity-harmonic-functions.md) | prose | [interior-c1-infinity-harmonic.pdf](../../../preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf) |
| [`Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026`](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/) | [338](../differential-geometry/338-yaus-uniformization-conjecture.md) | prose | [paper.pdf](../../../preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Evans`. The normalized key is `evans`.

