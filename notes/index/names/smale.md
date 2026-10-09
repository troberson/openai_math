# Name: smale

10 families · subject name · 2 carried by a title or a declaration · 10 by prose · 7 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 55 capitalized occurrences, 27 of them mid-sentence, 6 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 2 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 10 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 7 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Counterexamples to Zariski's multiplicity conjecture | — | — | yes | — | yes | yes |
| [090](../convex-and-metric-geometry/090-universal-optimality-of-the-triangular-lattice.md) | Universal optimality of the triangular lattice | — | — | — | — | yes | — |
| [152](../dynamical-systems-and-ergodic-theory/152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md) | Zero entropy does not guarantee a smooth positive-volume model | — | — | — | — | yes | yes |
| [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | Spacetime Penrose inequalities and rigidity | — | — | — | — | yes | yes |
| [306](../topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) | The purely cosmetic surgery conjecture for knots in $S^3$ | — | — | — | — | yes | yes |
| [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | Donaldson's hypersymplectic deformation conjecture | — | — | — | — | yes | yes |
| [344](../differential-geometry/344-metric-blaschke-conjecture.md) | The metric Blaschke conjecture | — | — | — | — | yes | — |
| [345](../differential-geometry/345-infinitely-many-closed-geodesics-on-spheres-and-three-manifolds.md) | Infinitely many closed geodesics on spheres and three-manifolds | — | — | — | — | yes | — |
| [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | Counterexamples to strong forms of Arnold's fixed-point conjecture | — | — | yes | — | yes | yes |
| [368](../partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md) | The three-dimensional Ball--Evans approximation problem | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026`](../../../preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/) | [152](../dynamical-systems-and-ergodic-theory/152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md) | prose | [paper.pdf](../../../preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/paper.pdf) |
| [`Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/) | [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/paper.pdf) |
| [`Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/) | [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | prose | [paper.pdf](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026/paper.pdf) |
| [`Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/) | — | prose | — |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [paper.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [hamiltonian-fixed-points-below-stable-morse-number.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf) |
| [`Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026`](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/) | [345](../differential-geometry/345-infinitely-many-closed-geodesics-on-spheres-and-three-manifolds.md) | prose | [paper.pdf](../../../preprints/Infinitely-many-closed-geodesic-images-on-every-Riemannian-sphere-September-24-2026/paper.pdf) |
| [`Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026`](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/) | [306](../topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) | prose | [paper.pdf](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/paper.pdf) |
| [`Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf) |
| [`Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/) | [368](../partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md) | prose | [main.pdf](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf) |
| [`Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026`](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/) | [368](../partial-differential-equations/368-three-dimensional-ball-evans-approximation-problem.md) | prose | [main.pdf](../../../preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf) |
| [`The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026`](../../../preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/) | [260](../mathematical-physics/260-spacetime-penrose-inequalities-and-rigidity.md) | prose | [paper.pdf](../../../preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/paper.pdf) |
| [`The-metric-Blaschke-theorem-September-23-2026`](../../../preprints/The-metric-Blaschke-theorem-September-23-2026/) | [344](../differential-geometry/344-metric-blaschke-conjecture.md) | prose | [paper.pdf](../../../preprints/The-metric-Blaschke-theorem-September-23-2026/paper.pdf) |
| [`Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026`](../../../preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/) | [090](../convex-and-metric-geometry/090-universal-optimality-of-the-triangular-lattice.md) | prose | [paper.pdf](../../../preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Smale and Levine |
| [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | Smale |
| [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | Smale |
| [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | Smale |

## Spelling variants

Every form below normalizes to the key `smale`: accents folded, dash variants unified, possessives stripped, case lowered. `Smale` · `Smale's`

