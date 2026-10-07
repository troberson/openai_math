# 113 — Approximate counting and the perfect-matching entropy conjecture

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/113.md`](../../../lean/docs/113.md) |
| Comparator configs | 6 (3 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, bound, uniform |
| Topics | [graph-theory](../topics/graph-theory.md) · [algorithms](../topics/algorithms.md) · [computability](../topics/computability.md) · [convex-geometry](../topics/convex-geometry.md) · [dynamical-systems](../topics/dynamical-systems.md) · [information-theory](../topics/information-theory.md) · [sampling-and-counting](../topics/sampling-and-counting.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026`](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/) | [main.pdf](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf) | [build/](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/build/) | [README.md](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/build/main.tex) | — |
| [`Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026`](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/) | [main.pdf](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf) | [build/](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/) | [README.md](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BinaryMatching](../../../lean/ComparatorChallenges/BinaryMatching.json) | `OAI.BinaryMatching.deterministic_approximate_counting` | [BinarySolve.lean](../../../lean/OAI/Computability/MatchingCount/BinarySolve.lean) | [`OAI/Computability/MatchingCount`](../../../lean/OAI/Computability/MatchingCount/) |
| [MatchingEntropy](../../../lean/ComparatorChallenges/MatchingEntropy.json) | `OAI.MatchingEntropy.entropy_main` | [Main.lean](../../../lean/OAI/Combinatorics/PerfectMatching/Main.lean) | [`OAI/Combinatorics/PerfectMatching`](../../../lean/OAI/Combinatorics/PerfectMatching/) |
| [SingletonLoopMatching](../../../lean/ComparatorChallenges/SingletonLoopMatching.json) | `OAI.LoopMatching.fullEndpoint` | [Main.lean](../../../lean/OAI/Computability/LoopMatching/Main.lean) | [`OAI/Computability/LoopMatching`](../../../lean/OAI/Computability/LoopMatching/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BinaryMatching` | [.json](../../../lean/ComparatorChallenges/BinaryMatching.json) | [.lean](../../../lean/ComparatorChallenges/BinaryMatching.lean) | 1 | 0 | no | yes |
| `MatchingEntropy` | [.json](../../../lean/ComparatorChallenges/MatchingEntropy.json) | [.lean](../../../lean/ComparatorChallenges/MatchingEntropy.lean) | 1 | 0 | no | yes |
| `MatchingEntropyBounds` | [.json](../../../lean/ComparatorChallenges/MatchingEntropyBounds.json) | [.lean](../../../lean/ComparatorChallenges/MatchingEntropyBounds.lean) | 1 | 0 | no | no |
| `MatchingFPRAS` | [.json](../../../lean/ComparatorChallenges/MatchingFPRAS.json) | [.lean](../../../lean/ComparatorChallenges/MatchingFPRAS.lean) | 1 | 0 | no | no |
| `SingletonLoopMatching` | [.json](../../../lean/ComparatorChallenges/SingletonLoopMatching.json) | [.lean](../../../lean/ComparatorChallenges/SingletonLoopMatching.lean) | 1 | 0 | no | yes |
| `TriangleFace` | [.json](../../../lean/ComparatorChallenges/TriangleFace.json) | [.lean](../../../lean/ComparatorChallenges/TriangleFace.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives a fully polynomial randomized approximation scheme for counting perfect matchings in arbitrary finite simple graphs, with exact detection of zero counts. Also proves the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant, bounding the maximum entropy of a matching law at every feasible edge-marginal vector in a loopless labelled multigraph, including boundary points.

