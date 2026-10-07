# 188 — The sharp constant in random triangle removal

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/188.md`](../../../lean/docs/188.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026`](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/) | [The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf) | [build/](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/build/) | [README.md](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/README.md) | no | [paper.tex](../../../preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TriangleRemoval` | [.json](../../../lean/ComparatorChallenges/TriangleRemoval.json) | [.lean](../../../lean/ComparatorChallenges/TriangleRemoval.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Starting from the complete graph on $n$ vertices, repeatedly delete a uniformly chosen remaining triangle. The terminal edge count is asymptotic to $n^{3/2}/(2\sqrt2)$, with mean-square convergence after normalization by $n^{3/2}$. This proves the triangle case of the Joos--K\"uhn sharp-constant conjecture.

