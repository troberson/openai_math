# 088 — Petty's projection-volume conjecture and simplex counterexamples

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/088.md`](../../../lean/docs/088.md) |
| Comparator configs | 3 (3 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound |
| Topics | [convex-geometry](../topics/convex-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026`](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/) | [paper.pdf](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf) | [build/](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/) | [README.md](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/main.tex) | — |
| [`Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026`](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/) | [paper.pdf](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf) | [build/](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/) | [README.md](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PettyProjectionVolume](../../../lean/ComparatorChallenges/PettyProjectionVolume.json) | `OAI.PettyProjection.petty_projection_volume` | [Main.lean](../../../lean/OAI/Geometry/ProjectionBodies/Main.lean) | [`OAI/Geometry/ProjectionBodies`](../../../lean/OAI/Geometry/ProjectionBodies/) |
| [ProjectionCounterexample](../../../lean/ComparatorChallenges/ProjectionCounterexample.json) | `OAI.ProjectionCounterexample.universal_simplex_upper_bound_false` | [Counterexample.lean](../../../lean/OAI/Geometry/ProjectionBody/Counterexample.lean) | [`OAI/Geometry/ProjectionBody`](../../../lean/OAI/Geometry/ProjectionBody/) |
| [ProjectionVolume](../../../lean/ComparatorChallenges/ProjectionVolume.json) | `OAI.Paper092.product_counterexample` | [ProductCounterexample.lean](../../../lean/OAI/Geometry/ProjectionVolume/ProductCounterexample.lean) | [`OAI/Geometry/ProjectionVolume`](../../../lean/OAI/Geometry/ProjectionVolume/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PettyProjectionVolume` | [.json](../../../lean/ComparatorChallenges/PettyProjectionVolume.json) | [.lean](../../../lean/ComparatorChallenges/PettyProjectionVolume.lean) | 1 | 0 | no | yes |
| `ProjectionCounterexample` | [.json](../../../lean/ComparatorChallenges/ProjectionCounterexample.json) | [.lean](../../../lean/ComparatorChallenges/ProjectionCounterexample.lean) | 1 | 0 | no | yes |
| `ProjectionVolume` | [.json](../../../lean/ComparatorChallenges/ProjectionVolume.json) | [.lean](../../../lean/ComparatorChallenges/ProjectionVolume.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Petty's projection-volume conjecture in the remaining dimensions $n\ge4$: ellipsoids uniquely minimize projection-body volume at fixed body volume. Also establishes the full Lutwak--Petty projection inequalities. In contrast, products of simplices exceed Brannen's proposed simplex maximum for normalized projection-body volume by an exponential factor in every sufficiently large dimension.

