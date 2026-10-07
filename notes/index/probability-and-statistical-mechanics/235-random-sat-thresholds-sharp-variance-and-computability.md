# 235 — Random-SAT thresholds, sharp variance and computability

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T2 |
| Manuscripts | 4 (0 formalized at source level) |
| Scope note | [`lean/docs/235.md`](../../../lean/docs/235.md) |
| Comparator configs | 4 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 6 in · 6 out |
| Claim shapes | resolution, bound, uniform |
| Topics | [computability](../topics/computability.md) · [disordered-systems](../topics/disordered-systems.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026`](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/) | [article.pdf](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/article.pdf) | [build/](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/build/) | [README.md](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/README.md) | no | [paper.tex](../../../preprints/A-Limiting-Satisfiability-Threshold-for-Every-Fixed-Clause-Size-September-25-2026/build/source/paper.tex) | — |
| [`Computing-the-Random-3-SAT-Threshold-September-27-2026`](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/) | [article.pdf](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf) | [build/](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/build/) | [README.md](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/README.md) | no | [paper.tex](../../../preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/build/paper.tex) | — |
| [`Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026`](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/) | [linear-variance-of-the-random-3-sat-hitting-time.pdf](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/linear-variance-of-the-random-3-sat-hitting-time.pdf) | [build/](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/build/) | [README.md](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/README.md) | no | [main.tex](../../../preprints/Linear-Variance-of-the-Random-3-SAT-Hitting-Time-October-5-2026/build/source/main.tex) | — |
| [`Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026`](../../../preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/) | [article.pdf](../../../preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/article.pdf) | [build/](../../../preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/build/) | [README.md](../../../preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/README.md) | no | [paper.tex](../../../preprints/Variance-of-the-Random-k-SAT-Hitting-Time-September-27-2026/build/source/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 4 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FixedClauseThreshold` | [.json](../../../lean/ComparatorChallenges/FixedClauseThreshold.json) | [.lean](../../../lean/ComparatorChallenges/FixedClauseThreshold.lean) | 1 | 0 | no | no |
| `SATComputability` | [.json](../../../lean/ComparatorChallenges/SATComputability.json) | [.lean](../../../lean/ComparatorChallenges/SATComputability.lean) | 1 | 0 | no | no |
| `SATSharpness` | [.json](../../../lean/ComparatorChallenges/SATSharpness.json) | [.lean](../../../lean/ComparatorChallenges/SATSharpness.lean) | 1 | 0 | no | no |
| `SATVariance` | [.json](../../../lean/ComparatorChallenges/SATVariance.json) | [.lean](../../../lean/ComparatorChallenges/SATVariance.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For random $k$-SAT with independent uniformly signed proper clauses sampled with replacement, proves finite positive limiting thresholds and hitting-time variance $\Theta_k(n)$ for every fixed $k\ge3$, and computability of the 3-SAT threshold. We credit Gaia Carenini with priority for resolving the threshold-existence conjecture in her concurrent \href{https://eccc.weizmann.ac.il/report/2026/229/}{ECCC TR26-229}, made public October 5, 2026; this family supplies another proof and the sharper variance and computability results.

