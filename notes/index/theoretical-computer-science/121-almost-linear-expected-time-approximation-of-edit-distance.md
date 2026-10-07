# 121 — Almost-linear expected-time approximation of edit distance

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/121.md`](../../../lean/docs/121.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 1 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026`](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/) | [paper.pdf](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/paper.pdf) | [build/](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/build/) | [README.md](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/README.md) | no | [paper.tex](../../../preprints/An-Almost-Linear-Approximation-Scheme-for-Edit-Distance-September-24-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `EditApproximation` | [.json](../../../lean/ComparatorChallenges/EditApproximation.json) | [.lean](../../../lean/ComparatorChallenges/EditApproximation.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For every fixed rational $\varepsilon\in(0,1)$, gives a randomized $(1+\varepsilon)$ approximation to unit-cost edit distance in worst-case expected time $N^{1+o(1)}$, with success probability at least $2/3$. The strings have total length $N$ and polynomially bounded integer symbols. This is an asymptotic guarantee at fixed accuracy.

