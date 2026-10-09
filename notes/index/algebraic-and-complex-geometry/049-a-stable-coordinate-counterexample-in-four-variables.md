# 049 — A stable-coordinate counterexample in four variables

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/049.md`](../../../lean/docs/049.md) |
| Comparator configs | 3 (3 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 1 out |
| Claim shapes | — |
| Topics | [geometric-measure-theory](../topics/geometric-measure-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026`](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/) | [stable-coordinate-four-variables.pdf](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf) | [build/](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/build/) | [README.md](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/README.md) | yes | [main.tex](../../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/build/source/main.tex) | — |
| [`An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026`](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/) | [paper.pdf](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf) | [build/](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/build/) | [README.md](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [AbhyankarSathaye](../../../lean/ComparatorChallenges/AbhyankarSathaye.json) | `OAI.AbhyankarSathaye.exists_noncoordinate_polynomial` | [Counterexample.lean](../../../lean/OAI/AlgebraicGeometry/AbhyankarSathaye/Counterexample.lean) | [`OAI/AlgebraicGeometry/AbhyankarSathaye`](../../../lean/OAI/AlgebraicGeometry/AbhyankarSathaye/) |
| [CommutingDerivations](../../../lean/ComparatorChallenges/CommutingDerivations.json) | `OAI.AbhyankarSathaye.CommutingDerivations.commuting_derivations_with_ordinary_extras` | [OrdinaryExtraMain.lean](../../../lean/OAI/AlgebraicGeometry/CommutingDerivations/OrdinaryExtraMain.lean) | [`OAI/AlgebraicGeometry/CommutingDerivations`](../../../lean/OAI/AlgebraicGeometry/CommutingDerivations/) |
| [StableCoordinateFour](../../../lean/ComparatorChallenges/StableCoordinateFour.json) | `OAI.StableCoordinate.principal_package` | [Principal.lean](../../../lean/OAI/AlgebraicGeometry/StableCoordinate/Principal.lean) | [`OAI/AlgebraicGeometry/StableCoordinate`](../../../lean/OAI/AlgebraicGeometry/StableCoordinate/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `AbhyankarSathaye` | [.json](../../../lean/ComparatorChallenges/AbhyankarSathaye.json) | [.lean](../../../lean/ComparatorChallenges/AbhyankarSathaye.lean) | 1 | 0 | no | yes |
| `CommutingDerivations` | [.json](../../../lean/ComparatorChallenges/CommutingDerivations.json) | [.lean](../../../lean/ComparatorChallenges/CommutingDerivations.lean) | 1 | 0 | no | yes |
| `StableCoordinateFour` | [.json](../../../lean/ComparatorChallenges/StableCoordinateFour.json) | [.lean](../../../lean/ComparatorChallenges/StableCoordinateFour.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a polynomial in four complex variables that is not a coordinate but becomes one after adjoining a single variable, disproving the Stable Coordinate conjecture in four variables. Every fiber is affine three-space, yet none of its embeddings is rectifiable, also disproving the Abhyankar--Sathaye conjecture even when all fibers are affine spaces.

