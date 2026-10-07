# Name: kahn

10 families · subject name · 1 carried by a title or a declaration · 10 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 49 capitalized occurrences, 26 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 10 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [040](../algebraic-and-complex-geometry/040-blochs-conjecture-for-complex-surfaces.md) | Bloch's conjecture for complex surfaces | — | — | — | — | yes | — |
| [156](../combinatorics/156-borsuks-conjecture-fails-in-dimension-nine.md) | Borsuk's conjecture fails in dimension nine | — | — | — | — | yes | yes |
| [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | Counterexamples to Ryser's covering and Gy\'arf\'as's tree-cover conjectures | — | — | — | — | yes | yes |
| [175](../combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) | Talagrand's conjectures and graph decompositions at expectation thresholds | — | — | — | — | yes | yes |
| [176](../combinatorics/176-second-kahn-kalai-conjecture.md) | The second Kahn--Kalai conjecture | yes | yes | — | yes | yes | — |
| [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | The Friedgut--Kalai graph and hypergraph threshold conjectures | — | — | — | — | yes | — |
| [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | No infinite critical clusters on quasi-transitive graphs | — | — | — | — | yes | yes |
| [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | Conformal universality for weakly interacting and disordered Ising models | — | — | — | — | yes | — |
| [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | Sharp singularity rates for symmetric sign matrices | — | — | — | — | yes | — |
| [246](../group-theory/246-cannons-conjecture.md) | Cannon's conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026`](../../../preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/) | [246](../group-theory/246-cannons-conjecture.md) | prose | [paper.pdf](../../../preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/paper.pdf) |
| [`A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026`](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/) | [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | prose | [paper.pdf](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf) |
| [`A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026`](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/) | [156](../combinatorics/156-borsuks-conjecture-fails-in-dimension-nine.md) | prose | [paper.pdf](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf) |
| [`A-uniform-influence-bound-for-hypergraph-properties-October-5-2026`](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/) | [186](../combinatorics/186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) | prose | [hypergraph-influences.pdf](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) |
| [`Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026`](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/) | [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | prose | [paper.pdf](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf) |
| [`Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026`](../../../preprints/Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026/) | [040](../algebraic-and-complex-geometry/040-blochs-conjecture-for-complex-surfaces.md) | prose | [paper.pdf](../../../preprints/Blochs-Conjecture-for-Surfaces-with-pg-equals-q-equals-0-September-24-2026/paper.pdf) |
| [`Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026`](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/) | [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | prose | [paper.pdf](../../../preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf) |
| [`Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026`](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/) | [175](../combinatorics/175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) | prose | [graph-threshold-decompositions.pdf](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/graph-threshold-decompositions.pdf) |
| [`Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026`](../../../preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/) | [218](../probability-and-statistical-mechanics/218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) | prose | [critical-relative-second-moment-weak-random-bond-ising.pdf](../../../preprints/Logarithmic-Relative-Fluctuations-in-the-Weakly-Disordered-Planar-Ising-Model-October-5-2026/critical-relative-second-moment-weak-random-bond-ising.pdf) |
| [`No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026`](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/) | [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | prose | [paper.pdf](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf) |
| [`The-second-Kahn-Kalai-conjecture-September-24-2026`](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/) | [176](../combinatorics/176-second-kahn-kalai-conjecture.md) | prose + title | [paper.pdf](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf) |
| [`The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026`](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/) | [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | prose | [biased-symmetric-sign-singularity.pdf](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/biased-symmetric-sign-singularity.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [SecondKahnKalai](../../../lean/ComparatorChallenges/SecondKahnKalai.json) | `OAI.LeanBlast.SecondKahnKalai.secondKahnKalaiBounds` | [Main.lean](../../../lean/OAI/Combinatorics/GraphThreshold/Main.lean) | [176](../combinatorics/176-second-kahn-kalai-conjecture.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Kahn`. The normalized key is `kahn`.

