# 167 — Pinned distances and a power saving for planar unit distances

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/167.md`](../../../lean/docs/167.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Topics | [discrete-geometry](../topics/discrete-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-power-saving-for-planar-unit-distances-September-23-2026`](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/) | [paper.pdf](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf) | [build/](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/build/) | [README.md](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/build/main.tex) | — |
| [`The-weak-pinned-planar-distance-theorem-September-23-2026`](../../../preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/) | [paper.pdf](../../../preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf) | [build/](../../../preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/build/) | [README.md](../../../preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PinnedDistances](../../../lean/ComparatorChallenges/PinnedDistances.json) | `OAI.WeakPinned.main` | [Main.lean](../../../lean/OAI/Geometry/PinnedDistances/Main.lean) | [`OAI/Geometry/PinnedDistances`](../../../lean/OAI/Geometry/PinnedDistances/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PinnedDistances` | [.json](../../../lean/ComparatorChallenges/PinnedDistances.json) | [.lean](../../../lean/ComparatorChallenges/PinnedDistances.lean) | 1 | 0 | no | yes |
| `PlanarUnitDistances` | [.json](../../../lean/ComparatorChallenges/PlanarUnitDistances.json) | [.lean](../../../lean/ComparatorChallenges/PlanarUnitDistances.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the weak pinned Erd\H{o}s distance conjecture: for every fixed $\varepsilon>0$, all but $o(n)$ points of any $n$-point planar set determine at least $n^{1-\varepsilon}$ distinct nonzero distances. A complementary theorem bounds the number of unit-distance pairs by $O(n^{4/3-\delta})$ for an absolute $\delta>0$.

