# 214 — The Benjamini--Schramm nonuniqueness conjecture

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/214.md`](../../../lean/docs/214.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | resolution, bound |
| Topics | [graph-theory](../topics/graph-theory.md) · [group-theory](../topics/group-theory.md) · [planar-maps-and-lattice-models](../topics/planar-maps-and-lattice-models.md) · [percolation](../topics/percolation.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026`](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/) | [paper.pdf](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf) | [build/](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/) | [README.md](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/README.md) | no | [main.tex](../../../preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BenjaminiSchramm` | [.json](../../../lean/ComparatorChallenges/BenjaminiSchramm.json) | [.lean](../../../lean/ComparatorChallenges/BenjaminiSchramm.lean) | 3 | 0 | no | no |
| `CayleyPercolation` | [.json](../../../lean/ComparatorChallenges/CayleyPercolation.json) | [.lean](../../../lean/ComparatorChallenges/CayleyPercolation.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves $p_c<p_u$ for Bernoulli bond percolation on every infinite connected locally finite nonamenable quasi-transitive graph, resolving the Benjamini--Schramm nonuniqueness conjecture. Thus there is a nonempty range of probabilities with infinitely many infinite clusters. A stronger operator bound also establishes the critical triangle condition.

