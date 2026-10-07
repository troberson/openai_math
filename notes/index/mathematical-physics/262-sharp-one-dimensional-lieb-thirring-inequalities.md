# 262 — Sharp one-dimensional Lieb--Thirring inequalities

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/262.md`](../../../lean/docs/262.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026`](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/) | [sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf) | [build/](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/build/) | [README.md](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/README.md) | no | [main.tex](../../../preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/build/main.tex) | — |
| [`Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026`](../../../preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/) | [paper.pdf](../../../preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf) | [build/](../../../preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/build/) | [README.md](../../../preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/build/main.tex) | — |
| [`Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026`](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/) | [sharp-matrix-lieb-thirring.pdf](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf) | [build/](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/build/) | [README.md](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/README.md) | no | [main.tex](../../../preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [LiebThirring](../../../lean/ComparatorChallenges/LiebThirring.json) | `OAI.SharpLiebThirring.sharp_lieb_thirring` | [Main.lean](../../../lean/OAI/Analysis/LiebThirring/Main.lean) | [`OAI/Analysis/LiebThirring`](../../../lean/OAI/Analysis/LiebThirring/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `LiebThirring` | [.json](../../../lean/ComparatorChallenges/LiebThirring.json) | [.lean](../../../lean/ComparatorChallenges/LiebThirring.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the sharp one-dimensional Lieb--Thirring inequality for $1/2<\gamma<3/2$ and arbitrary finite-matrix potentials $W\ge0$ with $\int\operatorname{tr}(W^{\gamma+1/2})<\infty$: the optimal constant is the scalar one-bound-state value, independent of matrix size. All equality cases are direct sums, in one constant unitary basis, of scalar $\operatorname{sech}^2$ solitons with independent scales and centers, and zero channels.

