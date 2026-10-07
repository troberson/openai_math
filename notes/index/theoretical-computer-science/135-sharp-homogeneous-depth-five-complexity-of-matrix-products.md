# 135 — Sharp homogeneous depth-five complexity of matrix products

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/135.md`](../../../lean/docs/135.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, classification |
| Topics | [complexity-theory](../topics/complexity-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026`](../../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/) | [Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf](../../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026.pdf) | [build/](../../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/build/) | [README.md](../../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/README.md) | no | [paper.tex](../../../preprints/Homogeneous-depth-five-lower-bounds-for-iterated-matrix-multiplication-September-25-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DepthFive` | [.json](../../../lean/ComparatorChallenges/DepthFive.json) | [.lean](../../../lean/ComparatorChallenges/DepthFive.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Over every characteristic-zero field, the $(1,1)$ entry of a product of $n$ independent $n\times n$ variable matrices requires $n^{\Theta(\sqrt n)}$ gates in homogeneous depth-five sum--product circuits. This sharp bound allows shared gates and bottom linear forms involving all variables.

