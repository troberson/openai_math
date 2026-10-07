# 257 — A hyperbolic group with no geometric CAT(0) action

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/257.md`](../../../lean/docs/257.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [algebraic-topology](../topics/algebraic-topology.md) · [riemannian-geometry](../topics/riemannian-geometry.md) · [group-theory](../topics/group-theory.md) · [metric-geometry](../topics/metric-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026`](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/) | [paper.pdf](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) | [build/](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/build/) | [README.md](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/README.md) | yes | [main.tex](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [HyperbolicObstruction](../../../lean/ComparatorChallenges/HyperbolicObstruction.json) | `OAI.HyperbolicObstruction.main` | [Main.lean](../../../lean/OAI/Geometry/HyperbolicGroups/Main.lean) | [`OAI/Geometry/HyperbolicGroups`](../../../lean/OAI/Geometry/HyperbolicGroups/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HyperbolicObstruction` | [.json](../../../lean/ComparatorChallenges/HyperbolicObstruction.json) | [.lean](../../../lean/ComparatorChallenges/HyperbolicObstruction.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Answers negatively whether every word-hyperbolic group is a CAT(0) group. Constructs one with a finite classifying space but no proper cocompact isometric action on any proper complete $\operatorname{CAT}(0)$ space, in any dimension.

