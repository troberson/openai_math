# Name: gross

17 families · subject name · 1 carried by a title or a declaration · 17 by prose · 13 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 133 capitalized occurrences, 94 of them mid-sentence, 8 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 17 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 13 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | yes | — | yes | yes |
| [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | Hilbert's tenth problem over $\mathbb Q$ | — | — | — | — | yes | yes |
| [006](../number-theory/006-goldfelds-conjecture.md) | Goldfeld's conjecture | — | — | — | — | yes | yes |
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | — | — | — | — | yes | — |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | The rational Hodge conjecture for CM abelian varieties and products of K3 surfaces | — | — | — | — | yes | yes |
| [053](../algebraic-and-complex-geometry/053-a-counterexample-to-pixtons-original-completeness-conjecture.md) | A counterexample to Pixton's original completeness conjecture | — | — | — | — | yes | — |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | The Mahler conjectures and symplectic width | — | — | — | — | yes | yes |
| [093](../convex-and-metric-geometry/093-dimension-free-logarithmic-sobolev-inequality-for-subgaussian-log-concave-measures.md) | Dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures | — | — | — | — | yes | yes |
| [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | The Courtade--Kumar and Hellinger conjectures | — | — | — | — | yes | yes |
| [169](../combinatorics/169-shareshian-wachs-e-positivity-conjecture.md) | The Shareshian--Wachs $e$-positivity conjecture | — | — | — | — | yes | yes |
| [227](../probability-and-statistical-mechanics/227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) | The dynamical phase transition in the Sherrington--Kirkpatrick model | — | — | — | — | yes | yes |
| [267](../mathematical-physics/267-positive-temperature-bose-einstein-condensation-and-quantum-depletion.md) | Positive-temperature Bose--Einstein condensation and quantum depletion | — | — | — | — | yes | — |
| [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | Counterexamples to Baum--Connes and Kadison--Kaplansky | — | — | — | — | yes | yes |
| [309](../topology/309-kervaire-invariant-problem-at-the-prime-three.md) | The Kervaire invariant problem at the prime three | — | — | — | — | yes | — |
| [311](../topology/311-chais-invariant-ideal-conjecture.md) | Chai's invariant-ideal conjecture | — | — | — | — | yes | yes |
| [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | Chromatic splitting: counterexamples and filtrations | — | — | — | — | yes | yes |
| [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | Donaldson's hypersymplectic deformation conjecture | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/paper.pdf) |
| [`A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf) |
| [`A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026`](../../../preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/) | [267](../mathematical-physics/267-positive-temperature-bose-einstein-condensation-and-quantum-depletion.md) | prose | [paper.pdf](../../../preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf) |
| [`A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026`](../../../preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/) | [093](../convex-and-metric-geometry/093-dimension-free-logarithmic-sobolev-inequality-for-subgaussian-log-concave-measures.md) | prose | [paper.pdf](../../../preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf) |
| [`A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026`](../../../preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/) | [053](../algebraic-and-complex-geometry/053-a-counterexample-to-pixtons-original-completeness-conjecture.md) | prose | [paper.pdf](../../../preprints/A-high-arity-counterexample-to-Pixton-completeness-in-Chow-September-24-2026/paper.pdf) |
| [`A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/) | [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | prose | [paper.pdf](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/paper.pdf) |
| [`A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026`](../../../preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/paper.pdf) |
| [`Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026`](../../../preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/) | [267](../mathematical-physics/267-positive-temperature-bose-einstein-condensation-and-quantum-depletion.md) | prose | [positive-temperature-hard-spheres.pdf](../../../preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/positive-temperature-hard-spheres.pdf) |
| [`Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026`](../../../preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026/paper.pdf) |
| [`Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026`](../../../preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/) | [227](../probability-and-statistical-mechanics/227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) | prose | [paper.pdf](../../../preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/paper.pdf) |
| [`Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026`](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/) | [341](../differential-geometry/341-donaldsons-hypersymplectic-deformation-conjecture.md) | prose | [paper.pdf](../../../preprints/Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-September-23-2026/paper.pdf) |
| [`Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026`](../../../preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/) | [169](../combinatorics/169-shareshian-wachs-e-positivity-conjecture.md) | prose | [paper.pdf](../../../preprints/Elementary-Positivity-of-Chromatic-Quasisymmetric-Functions-September-24-2026/paper.pdf) |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [exact-bsd-low-selmer-corank.pdf](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/exact-bsd-low-selmer-corank.pdf) |
| [`Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026`](../../../preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/paper.pdf) |
| [`Filtered-chromatic-splitting-at-generic-primes-September-25-2026`](../../../preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/paper.pdf) |
| [`Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026`](../../../preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026/) | [006](../number-theory/006-goldfelds-conjecture.md) | prose | [paper.pdf](../../../preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026/paper.pdf) |
| [`Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026`](../../../preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/) | [267](../mathematical-physics/267-positive-temperature-bose-einstein-condensation-and-quantum-depletion.md) | prose | [paper.pdf](../../../preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf) |
| [`Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026`](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/) | [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | prose | [main.pdf](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf) |
| [`Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026`](../../../preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/) | [267](../mathematical-physics/267-positive-temperature-bose-einstein-condensation-and-quantum-depletion.md) | prose | [Quantum-Depletion-in-the-Dilute-Hard-Sphere-Bose-Gas.pdf](../../../preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/Quantum-Depletion-in-the-Dilute-Hard-Sphere-Bose-Gas.pdf) |
| [`Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026`](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/) | [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | prose | [main.pdf](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf) |
| [`Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026`](../../../preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/) | [311](../topology/311-chais-invariant-ideal-conjecture.md) | prose | [paper.pdf](../../../preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/paper.pdf) |
| [`Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026`](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose | [paper.pdf](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf) |
| [`Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [ramified-ramanujan.pdf](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf) |
| [`The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026`](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/) | [309](../topology/309-kervaire-invariant-problem-at-the-prime-three.md) | prose | [paper.pdf](../../../preprints/The-Kervaire-Invariant-Problem-at-the-Prime-Three-September-24-2026/paper.pdf) |
| [`The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026`](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [main.pdf](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/main.pdf) |
| [`The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | prose | [paper.pdf](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-September-30-2026/paper.pdf) |
| [`The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026`](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose | [paper.pdf](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) |
| [`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026`](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [paper.pdf](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | Split Gross--Zagier normalization |
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | Split Gross--Zagier formula |

## Spelling variants

Every form below normalizes to the key `gross`: accents folded, dash variants unified, possessives stripped, case lowered. `Gross` · `Gross's`

