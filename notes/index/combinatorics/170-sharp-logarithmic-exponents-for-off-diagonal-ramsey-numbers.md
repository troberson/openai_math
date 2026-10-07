# 170 — Sharp logarithmic exponents for off-diagonal Ramsey numbers

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | [`lean/docs/170.md`](../../../lean/docs/170.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 3 in · 1 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026`](../../../preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/) | [paper.pdf](../../../preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/paper.pdf) | [build/](../../../preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/build/) | [README.md](../../../preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/README.md) | no | [main.tex](../../../preprints/Sharp-Logarithmic-Exponents-for-Fixed-Off-Diagonal-Ramsey-Numbers-September-24-2026/build/main.tex) | — |
| [`The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026`](../../../preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/) | [paper.pdf](../../../preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/paper.pdf) | [build/](../../../preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/build/) | [README.md](../../../preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/README.md) | no | [paper.tex](../../../preprints/The-Sharp-Logarithmic-Exponent-of-r-5-t-September-24-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `RamseyFive` | [.json](../../../lean/ComparatorChallenges/RamseyFive.json) | [.lean](../../../lean/ComparatorChallenges/RamseyFive.lean) | 1 | 0 | no | no |
| `SharpLogRamsey` | [.json](../../../lean/ComparatorChallenges/SharpLogRamsey.json) | [.lean](../../../lean/ComparatorChallenges/SharpLogRamsey.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For every fixed integer $s\ge5$, proves $r(s,t)=t^{s-1}/(\log t)^{s-2+o(1)}$ as $t\to\infty$, determining the logarithmic exponent and matching the classical upper bound at that scale. Here $r(s,t)$ is the least number of vertices forcing an $s$-clique or a $t$-vertex independent set.

