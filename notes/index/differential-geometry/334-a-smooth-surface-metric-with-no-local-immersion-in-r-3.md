# 334 — A smooth surface metric with no local immersion in $\mathbb R^3$

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/334.md`](../../../lean/docs/334.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026`](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/) | [paper.pdf](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/paper.pdf) | [build/](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/) | [README.md](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [IsometricImmersion](../../../lean/ComparatorChallenges/IsometricImmersion.json) | `OAI.SmoothLocal.Geometry.exists_local_metric_without_local_immersion` | [Main.lean](../../../lean/OAI/Geometry/IsometricImmersion/Main.lean) | [`OAI/Geometry/IsometricImmersion`](../../../lean/OAI/Geometry/IsometricImmersion/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `IsometricImmersion` | [.json](../../../lean/ComparatorChallenges/IsometricImmersion.json) | [.lean](../../../lean/ComparatorChallenges/IsometricImmersion.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a smooth positive-definite metric on $(-1,1)^2$ for which no neighborhood of the origin admits a smooth isometric immersion into $\mathbb R^3$. This answers the unrestricted smooth local isometric realization problem for surfaces negatively, even after shrinking the neighborhood.

