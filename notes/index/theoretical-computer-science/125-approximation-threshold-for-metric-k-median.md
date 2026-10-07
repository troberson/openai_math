# 125 — The approximation threshold for metric $k$-median

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/125.md`](../../../lean/docs/125.md) |
| Comparator configs | 4 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | uniform, conditional |
| Topics | [algorithms](../topics/algorithms.md) · [combinatorial-optimization](../topics/combinatorial-optimization.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026`](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/) | [paper.pdf](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/paper.pdf) | [build/](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/build/) | [README.md](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Single-Exponential-Recovery-and-Bounded-Price-Strictness-for-Metric-k-Median-September-24-2026/build/paper.tex) | — |
| [`The-Approximation-Threshold-for-Metric-k-Median-September-24-2026`](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/) | [main.pdf](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/main.pdf) | [build/](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/) | [README.md](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/README.md) | no | [main.tex](../../../preprints/The-Approximation-Threshold-for-Metric-k-Median-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [KMedianRecovery](../../../lean/ComparatorChallenges/KMedianRecovery.json) | `OAI.MetricKMedianRecovery.global_application` | [Main.lean](../../../lean/OAI/Combinatorics/KMedianRecovery/Main.lean) | [`OAI/Combinatorics/KMedianRecovery`](../../../lean/OAI/Combinatorics/KMedianRecovery/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `KMedianRecovery` | [.json](../../../lean/ComparatorChallenges/KMedianRecovery.json) | [.lean](../../../lean/ComparatorChallenges/KMedianRecovery.lean) | 1 | 0 | no | yes |
| `KMedianRefinedRecovery` | [.json](../../../lean/ComparatorChallenges/KMedianRefinedRecovery.json) | [.lean](../../../lean/ComparatorChallenges/KMedianRefinedRecovery.lean) | 1 | 0 | no | no |
| `KMedianThreshold` | [.json](../../../lean/ComparatorChallenges/KMedianThreshold.json) | [.lean](../../../lean/ComparatorChallenges/KMedianThreshold.lean) | 1 | 0 | no | no |
| `MetricKMedian` | [.json](../../../lean/ComparatorChallenges/MetricKMedian.json) | [.lean](../../../lean/ComparatorChallenges/MetricKMedian.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives a deterministic polynomial-time $(1+2/e+\varepsilon)$-approximation for finite rational metric $k$-median with specified candidate facilities, for every fixed $\varepsilon>0$. Assuming $P\ne NP$, the optimal infimum approximation factor is $1+2/e$.

