# 073 — The Falconer distance conjecture

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/073.md`](../../../lean/docs/073.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 1 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026`](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/) | [paper.pdf](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf) | [build/](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/build/) | [README.md](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PlanarFalconer](../../../lean/ComparatorChallenges/PlanarFalconer.json) | `OAI.PlanarFalconer.mainTarget_proved` | [Main.lean](../../../lean/OAI/MeasureTheory/Falconer/Main.lean) | [`OAI/MeasureTheory/Falconer`](../../../lean/OAI/MeasureTheory/Falconer/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FalconerAllDimensions` | [.json](../../../lean/ComparatorChallenges/FalconerAllDimensions.json) | [.lean](../../../lean/ComparatorChallenges/FalconerAllDimensions.lean) | 1 | 0 | no | no |
| `PlanarFalconer` | [.json](../../../lean/ComparatorChallenges/PlanarFalconer.json) | [.lean](../../../lean/ComparatorChallenges/PlanarFalconer.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the Falconer distance conjecture in every dimension $d\ge2$: every compact set $E\subset\mathbb R^d$ with Hausdorff dimension greater than $d/2$ determines a set of Euclidean distances of positive Lebesgue measure.

