# 291 — Toms--Winter and equivariant Jiang--Su stability

|  |  |
|---|---|
| Discipline | [Operator algebras](../disciplines/operator-algebras.md) |
| Tier | T3 |
| Manuscripts | 4 (1 formalized at source level) |
| Scope note | [`lean/docs/291.md`](../../../lean/docs/291.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026`](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/) | [paper.pdf](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf) | [build/](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/build/) | [README.md](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/build/paper.tex) | — |
| [`Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026`](../../../preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/) | [paper.pdf](../../../preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf) | [build/](../../../preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/build/) | [README.md](../../../preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/README.md) | no | [paper.tex](../../../preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/build/paper.tex) | — |
| [`Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026`](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/) | [paper.pdf](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf) | [build/](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/build/) | [README.md](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/build/paper.tex) | — |
| [`Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026`](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/) | [paper.pdf](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf) | [build/](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/) | [README.md](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [UniformGamma](../../../lean/ComparatorChallenges/UniformGamma.json) | `OAI.ComparatorModel.CurrentMain.main` | [Challenge.lean](../../../lean/OAI/Analysis/TracialSplitting/Challenge.lean) | [`OAI/Analysis/TracialSplitting`](../../../lean/OAI/Analysis/TracialSplitting/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `UniformGamma` | [.json](../../../lean/ComparatorChallenges/UniformGamma.json) | [.lean](../../../lean/ComparatorChallenges/UniformGamma.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves equivariant Jiang--Su stability for every countable discrete amenable group action on a simple separable unital infinite-dimensional nuclear stably finite Jiang--Su-stable $C^*$-algebra, resolving this case of Szab\'o's conjecture without restrictions on trace dynamics. The family also proves the unital Toms--Winter conjecture, equating strict comparison, finite nuclear dimension and Jiang--Su stability in the simple separable unital infinite-dimensional nuclear setting.

