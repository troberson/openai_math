# 172 — Classification of finite Euclidean Ramsey configurations

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/172.md`](../../../lean/docs/172.md) |
| Comparator configs | 7 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, counterexample, classification |
| Topics | [algebraic-topology](../topics/algebraic-topology.md) · [graph-coloring](../topics/graph-coloring.md) · [ramsey-theory](../topics/ramsey-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026`](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/) | [paper.pdf](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf) | [build/](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/build/) | [README.md](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [EuclideanRamsey](../../../lean/ComparatorChallenges/EuclideanRamsey.json) | `OAI.EuclideanRamsey.classification` | [Main.lean](../../../lean/OAI/Combinatorics/EuclideanRamsey/Main.lean) | [`OAI/Combinatorics/EuclideanRamsey`](../../../lean/OAI/Combinatorics/EuclideanRamsey/) |
| [GrahamSpherical](../../../lean/ComparatorChallenges/GrahamSpherical.json) | `OAI.GrahamSpherical.full_main` | [Main.lean](../../../lean/OAI/Combinatorics/SphericalRamsey/Main.lean) | [`OAI/Combinatorics/SphericalRamsey`](../../../lean/OAI/Combinatorics/SphericalRamsey/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `EuclideanRamsey` | [.json](../../../lean/ComparatorChallenges/EuclideanRamsey.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanRamsey.lean) | 1 | 0 | no | yes |
| `EuclideanRamseyCircle` | [.json](../../../lean/ComparatorChallenges/EuclideanRamseyCircle.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanRamseyCircle.lean) | 1 | 0 | no | no |
| `EuclideanRamseyNine` | [.json](../../../lean/ComparatorChallenges/EuclideanRamseyNine.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanRamseyNine.lean) | 1 | 0 | no | no |
| `EuclideanRamseyQuadratic` | [.json](../../../lean/ComparatorChallenges/EuclideanRamseyQuadratic.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanRamseyQuadratic.lean) | 1 | 0 | no | no |
| `EuclideanRamseySpherical` | [.json](../../../lean/ComparatorChallenges/EuclideanRamseySpherical.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanRamseySpherical.lean) | 1 | 0 | no | no |
| `EuclideanRamseyTransitive` | [.json](../../../lean/ComparatorChallenges/EuclideanRamseyTransitive.json) | [.lean](../../../lean/ComparatorChallenges/EuclideanRamseyTransitive.lean) | 1 | 0 | no | no |
| `GrahamSpherical` | [.json](../../../lean/ComparatorChallenges/GrahamSpherical.json) | [.lean](../../../lean/ComparatorChallenges/GrahamSpherical.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Classifies finite point configurations that occur monochromatically, at their original scale, in every finite coloring of sufficiently high-dimensional Euclidean space. The characterization is an algebraic condition over the coordinate field. It also disproves the Leader--Russell--Walters conjecture that every such configuration is a subset of a finite transitive set.

