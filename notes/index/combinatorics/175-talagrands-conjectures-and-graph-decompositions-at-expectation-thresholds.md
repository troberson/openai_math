# 175 — Talagrand's conjectures and graph decompositions at expectation thresholds

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 3 (2 formalized at source level) |
| Scope note | [`lean/docs/175.md`](../../../lean/docs/175.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, bound, partial |
| Topics | [graph-theory](../topics/graph-theory.md) · [probabilistic-combinatorics](../topics/probabilistic-combinatorics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026`](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/) | [graph-threshold-decompositions.pdf](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/graph-threshold-decompositions.pdf) | [build/](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/build/) | [README.md](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/README.md) | no | [main.tex](../../../preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026/build/main.tex) | — |
| [`Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026`](../../../preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/) | [paper.pdf](../../../preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/paper.pdf) | [build/](../../../preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/build/) | [README.md](../../../preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Integral-and-fractional-expectation-thresholds-are-equivalent-September-23-2026/build/source/main.tex) | — |
| [`Talagrands-discrete-convexity-conjecture-September-23-2026`](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/build/) | [README.md](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Talagrands-discrete-convexity-conjecture-September-23-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TalagrandDiscreteConvexity](../../../lean/ComparatorChallenges/TalagrandDiscreteConvexity.json) | `OAI.TalagrandDiscreteConvexity.talagrand_discrete_convexity` | [Main.lean](../../../lean/OAI/Combinatorics/DiscreteConvexity/Main.lean) | [`OAI/Combinatorics/DiscreteConvexity`](../../../lean/OAI/Combinatorics/DiscreteConvexity/) |
| [TalagrandExpectationThreshold](../../../lean/ComparatorChallenges/TalagrandExpectationThreshold.json) | `OAI.TalagrandThreshold.talagrand_expectation_threshold_equivalence` | [Main.lean](../../../lean/OAI/Combinatorics/ExpectationThreshold/Main.lean) | [`OAI/Combinatorics/ExpectationThreshold`](../../../lean/OAI/Combinatorics/ExpectationThreshold/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TalagrandDiscreteConvexity` | [.json](../../../lean/ComparatorChallenges/TalagrandDiscreteConvexity.json) | [.lean](../../../lean/ComparatorChallenges/TalagrandDiscreteConvexity.lean) | 1 | 0 | no | yes |
| `TalagrandExpectationThreshold` | [.json](../../../lean/ComparatorChallenges/TalagrandExpectationThreshold.json) | [.lean](../../../lean/ComparatorChallenges/TalagrandExpectationThreshold.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that integral and fractional expectation thresholds differ by at most a universal factor, and resolves Talagrand's discrete-convexity conjecture. An application proves the Ascoli--He--Park--Talagrand graph-decomposition conjecture: every graph's edges split into a universally bounded number of fixed pieces, each with containment threshold at most a universal constant times the original graph's integral expectation threshold. The pieces' embeddings need not agree on shared vertices.

