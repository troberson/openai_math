# 017 — The irrationality exponent of $\pi$ is $2$

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/017.md`](../../../lean/docs/017.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | [irrationality-exponent-of-pi](../../../reasoning_traces/irrationality-exponent-of-pi.pdf) |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Topics | [diophantine-equations](../topics/diophantine-equations.md) |
| Companion families | — |
| Summary page | [017-the-irrationality-exponent-of-pi-is-2.md](../../../notes/summaries/number-theory/017-the-irrationality-exponent-of-pi-is-2.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-irrationality-exponent-of-pi-is-2-September-24-2026`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/) | [paper.pdf](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf) | [build/](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/) | [README.md](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/README.md) | no | [main.tex](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PiExponent` | [.json](../../../lean/ComparatorChallenges/PiExponent.json) | [.lean](../../../lean/ComparatorChallenges/PiExponent.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that the irrationality exponent of $\pi$ is exactly $2$: for every $\varepsilon>0$ and all sufficiently large denominators $q$, every rational $p/q$ satisfies $|\pi-p/q|\ge q^{-2-\varepsilon}$. This also proves convergence of the Flint--Hills series $\sum_{n\ge1}1/(n^3\sin^2 n)$, with angles in radians.

