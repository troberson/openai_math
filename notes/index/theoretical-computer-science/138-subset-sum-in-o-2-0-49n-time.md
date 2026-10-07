# 138 — Subset Sum in $O(2^{0.49n})$ time

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T0 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | — |
| Comparator configs | 0 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026`](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/) | [paper.pdf](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf) | [build/](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/) | [README.md](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/README.md) | no | [main.tex](../../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/main.tex) | — |
| [`Subset-Sum-in-Time-2-power-0-49n-October-4-2026`](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/) | [subset-sum.pdf](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf) | [build/](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/) | [README.md](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/README.md) | no | [main.tex](../../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family, and no scope note links a comparator config.

## Comparator configs

No scope note links a comparator config for this family.

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives a uniform randomized classical algorithm for worst-case Subset Sum in ordinary $O(2^{0.49n})$ word-RAM time on polynomial-bit inputs, where $n$ counts the integers. The time bound holds on every execution and success probability is at least $2/3$ on every input. Inputs may repeat positive integers; words have $O(n+b)$ bits for maximum input bit length $b$.

