# 192 — A counterexample to the Gopalan--Servedio conjecture

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/192.md`](../../../lean/docs/192.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026`](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/) | [Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf) | [build/](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/build/) | [README.md](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/README.md) | no | [main.tex](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SquareRootDegree` | [.json](../../../lean/ComparatorChallenges/SquareRootDegree.json) | [.lean](../../../lean/ComparatorChallenges/SquareRootDegree.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves the proposed square-root bound relating a Boolean function's linear Fourier coefficients to its polynomial degree. For every $C>0$, there is a sign-valued Boolean function $f$ with $\sum_i\widehat f(\{i\})>C\sqrt{\deg(f)}$. Thus its total signed correlation with individual input bits can exceed the proposed bound by an arbitrary factor.

