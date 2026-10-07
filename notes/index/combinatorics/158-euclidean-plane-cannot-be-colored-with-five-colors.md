# 158 — The Euclidean plane cannot be colored with five colors

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/158.md`](../../../lean/docs/158.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [graph-coloring](../topics/graph-coloring.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Euclidean-plane-is-not-five-colorable-September-23-2026`](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/) | [paper.pdf](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) | [build/](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/build/) | [README.md](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [EuclideanFiveColor](../../../lean/ComparatorChallenges/EuclideanFiveColor.json) | `OAI.EuclideanFiveColor.no_proper_five_coloring` | [Five.lean](../../../lean/OAI/Geometry/PlaneColoring/Five.lean) | [`OAI/Geometry/PlaneColoring`](../../../lean/OAI/Geometry/PlaneColoring/) |
| [PlaneColoring](../../../lean/ComparatorChallenges/PlaneColoring.json) | `OAI.Problem160.properColoring_seven` | [Seven.lean](../../../lean/OAI/Geometry/PlaneColoring/Seven.lean) | [`OAI/Geometry/PlaneColoring`](../../../lean/OAI/Geometry/PlaneColoring/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `EuclideanFiveColor` | [.json](../../../lean/ComparatorChallenges/EuclideanFiveColor.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanFiveColor.lean) | 1 | 1 | no | yes |
| `PlaneColoring` | [.json](../../../lean/ComparatorChallenges/PlaneColoring.json) | [.lean](../../../lean/ComparatorChallenges/PlaneColoring.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that every five-coloring of the Euclidean plane has a monochromatic pair at distance one, with no restriction on the color classes. This advances the Hadwiger--Nelson problem: together with the classical seven-coloring, only six and seven remain possible chromatic numbers of the plane.

