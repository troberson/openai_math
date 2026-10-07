# Name: arnold

9 families · subject name · 2 carried by a title or a declaration · 8 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 75 capitalized occurrences, 50 of them mid-sentence, 4 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 8 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [008](../number-theory/008-deligne-drinfeld-conjecture.md) | The Deligne--Drinfeld conjecture | — | — | — | — | yes | — |
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Counterexamples to Zariski's multiplicity conjecture | — | — | yes | — | yes | — |
| [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs | — | — | — | — | yes | — |
| [104](../theoretical-computer-science/104-quasipolynomial-algorithms-for-mean-payoff-stochastic-and-parity-games.md) | Quasipolynomial algorithms for mean-payoff, stochastic and parity games | — | — | — | — | — | yes |
| [147](../dynamical-systems-and-ergodic-theory/147-near-boundary-birkhoff-conjecture.md) | The near-boundary Birkhoff conjecture | — | — | — | — | yes | yes |
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | — | — | — | — | yes | — |
| [340](../differential-geometry/340-a-counterexample-to-the-nearby-lagrangian-conjecture.md) | A counterexample to the nearby Lagrangian conjecture | — | — | — | — | yes | — |
| [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | Counterexamples to strong forms of Arnold's fixed-point conjecture | yes | yes | — | yes | yes | — |
| [361](../differential-geometry/361-counterexamples-to-yaus-harmonic-dimension-bound.md) | Counterexamples to Yau's harmonic dimension bound | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026`](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/) | [361](../differential-geometry/361-counterexamples-to-yaus-harmonic-dimension-bound.md) | prose | [paper.pdf](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/paper.pdf) |
| [`A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/paper.pdf) |
| [`A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/) | [340](../differential-geometry/340-a-counterexample-to-the-nearby-lagrangian-conjecture.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/paper.pdf) |
| [`A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026`](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose + title | [paper.pdf](../../../preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf) |
| [`A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026`](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose + title | [paper.pdf](../../../preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf) |
| [`Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/) | [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/paper.pdf) |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [paper.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) |
| [`Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026`](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [hamiltonian-fixed-points-below-stable-morse-number.pdf](../../../preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf) |
| [`L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/) | [089](../convex-and-metric-geometry/089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) | prose | [paper.pdf](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf) |
| [`Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026`](../../../preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/) | [147](../dynamical-systems-and-ergodic-theory/147-near-boundary-birkhoff-conjecture.md) | prose | [paper.pdf](../../../preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/paper.pdf) |
| [`Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026`](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) | prose | [sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf](../../../preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf) |
| [`The-Deligne-Drinfeld-conjecture-September-23-2026`](../../../preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/) | [008](../number-theory/008-deligne-drinfeld-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [ArnoldCounterexample](../../../lean/ComparatorChallenges/ArnoldCounterexample.json) | `OAI.ArnoldCounterexample.main` | [Main.lean](../../../lean/OAI/Geometry/Arnold/Main.lean) | [347](../differential-geometry/347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) |

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Negative answer to Arnold's corank problem |

## Spelling variants

Every form below normalizes to the key `arnold`: accents folded, dash variants unified, possessives stripped, case lowered. `Arnold` · `Arnold's`

