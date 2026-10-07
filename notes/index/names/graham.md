# Name: graham

15 families · subject name · 1 carried by a title or a declaration · 11 by prose · 10 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 19 capitalized occurrences, 10 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 11 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 10 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [025](../number-theory/025-erdoss-short-egyptian-fraction-conjecture.md) | Erd\H{o}s’s short Egyptian-fraction conjecture | — | — | — | — | yes | yes |
| [037](../algebraic-and-complex-geometry/037-sharp-ordinary-double-point-volume-gap.md) | The sharp ordinary-double-point volume gap | — | — | — | — | — | yes |
| [053](../algebraic-and-complex-geometry/053-a-counterexample-to-pixtons-original-completeness-conjecture.md) | A counterexample to Pixton's original completeness conjecture | — | — | — | — | yes | — |
| [113](../theoretical-computer-science/113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md) | Approximate counting and the perfect-matching entropy conjecture | — | — | — | — | — | yes |
| [124](../theoretical-computer-science/124-polynomial-time-scheduling-on-three-identical-machines.md) | Polynomial-time scheduling on three identical machines | — | — | — | — | yes | yes |
| [138](../theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md) | Subset Sum in $O(2^{0.49n})$ time | — | — | — | — | yes | — |
| [140](../theoretical-computer-science/140-memory-sample-lower-bounds-for-noiseless-gaussian-regression.md) | Memory--sample lower bounds for noiseless Gaussian regression | — | — | — | — | yes | yes |
| [161](../combinatorics/161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) | Counterexamples to Sidorenko's conjecture and the forcing conjecture | — | — | — | — | yes | yes |
| [164](../combinatorics/164-hindmans-finite-sums-and-products-conjecture.md) | Hindman's finite sums and products conjecture | — | — | — | — | yes | — |
| [171](../combinatorics/171-hypercube-ramsey-conjecture.md) | The hypercube Ramsey conjecture | — | — | — | — | yes | — |
| [172](../combinatorics/172-classification-of-finite-euclidean-ramsey-configurations.md) | Classification of finite Euclidean Ramsey configurations | — | — | — | yes | yes | yes |
| [188](../combinatorics/188-sharp-constant-in-random-triangle-removal.md) | The sharp constant in random triangle removal | — | — | — | — | yes | yes |
| [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | Finite lattice representation: counterexamples and undecidability | — | — | — | — | — | yes |
| [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | No infinite critical clusters on quasi-transitive graphs | — | — | — | — | — | yes |
| [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | The Boone--Higman conjecture and higher finiteness | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026`](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/) | [138](../theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md) | prose | [paper.pdf](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf) |
| [`A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026`](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/) | [172](../combinatorics/172-classification-of-finite-euclidean-ramsey-configurations.md) | prose | [paper.pdf](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf) |
| [`A-counterexample-to-Sidorenkos-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/) | [161](../combinatorics/161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf) |
| [`A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026`](../../../preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/) | [053](../algebraic-and-complex-geometry/053-a-counterexample-to-pixtons-original-completeness-conjecture.md) | prose | [paper.pdf](../../../preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/paper.pdf) |
| [`A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026`](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/) | [124](../theoretical-computer-science/124-polynomial-time-scheduling-on-three-identical-machines.md) | prose | [paper.pdf](../../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) |
| [`A-universal-group-of-type-F-infinity-September-23-2026`](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf) |
| [`Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026`](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/) | [140](../theoretical-computer-science/140-memory-sample-lower-bounds-for-noiseless-gaussian-regression.md) | prose | [paper.pdf](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/paper.pdf) |
| [`Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026`](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/) | [164](../combinatorics/164-hindmans-finite-sums-and-products-conjecture.md) | prose | [paper.pdf](../../../preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf) |
| [`Short-Egyptian-fractions-September-25-2026`](../../../preprints/Short-Egyptian-fractions-September-25-2026/) | [025](../number-theory/025-erdoss-short-egyptian-fraction-conjecture.md) | prose | [Short-Egyptian-fractions-September-25-2026.pdf](../../../preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) |
| [`Subset-Sum-in-Time-2-power-0-49n-October-4-2026`](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/) | [138](../theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md) | prose | [subset-sum.pdf](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf) |
| [`The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026`](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/) | [188](../combinatorics/188-sharp-constant-in-random-triangle-removal.md) | prose | [The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf) |
| [`The-hypercube-Ramsey-number-has-linear-order-September-23-2026`](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/) | [171](../combinatorics/171-hypercube-ramsey-conjecture.md) | prose | [paper.pdf](../../../preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [GrahamSpherical](../../../lean/ComparatorChallenges/GrahamSpherical.json) | `OAI.GrahamSpherical.full_main` | [Main.lean](../../../lean/OAI/Combinatorics/SphericalRamsey/Main.lean) | [172](../combinatorics/172-classification-of-finite-euclidean-ramsey-configurations.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Graham`. The normalized key is `graham`.

