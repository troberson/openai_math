# 109 — Integer multiplication below $n\log n$

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T0 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | — |
| Comparator configs | 0 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, counterexample |
| Topics | [algorithms](../topics/algorithms.md) · [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Integer-multiplication-below-n-log-n-September-23-2026`](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/) | [paper.pdf](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf) | [build/](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/) | [README.md](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/README.md) | no | [main.tex](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family, and no scope note links a comparator config.

## Comparator configs

No scope note links a comparator config for this family.

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Multiplies two $n$-bit integers exactly at every input length in deterministic worst-case time $O(n(\log n)^{1-\kappa})$, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with finitely many one-dimensional tapes. This disproves the Sch\"onhage--Strassen $n\log n$ optimality conjecture in the ordinary multitape bit model.

