# 254 — Classifying spaces and geometric obstructions for Artin groups

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 3 (2 formalized at source level) |
| Scope note | [`lean/docs/254.md`](../../../lean/docs/254.md) |
| Comparator configs | 3 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Topics | [algebraic-topology](../topics/algebraic-topology.md) · [group-theory](../topics/group-theory.md) · [metric-geometry](../topics/metric-geometry.md) · [arithmetic-geometry](../topics/arithmetic-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026`](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/) | [paper.pdf](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/paper.pdf) | [build/](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/build/) | [README.md](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/README.md) | yes | [main.tex](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/build/main.tex) | — |
| [`Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026`](../../../preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/build/) | [README.md](../../../preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Harmonic-heights-and-the-Artin-K-pi-1-conjecture-September-23-2026/build/main.tex) | — |
| [`Parabolic-intersections-in-Artin-groups-September-23-2026`](../../../preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/) | [paper.pdf](../../../preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/paper.pdf) | [build/](../../../preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/build/) | [README.md](../../../preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Parabolic-intersections-in-Artin-groups-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ArtinCAT0](../../../lean/ComparatorChallenges/ArtinCAT0.json) | `OAI.ArtinCAT0.main` | [Main.lean](../../../lean/OAI/GroupTheory/ArtinCAT0/Main.lean) | [`OAI/GroupTheory/ArtinCAT0`](../../../lean/OAI/GroupTheory/ArtinCAT0/) |
| [HarmonicArtin](../../../lean/ComparatorChallenges/HarmonicArtin.json) | `OAI.HarmonicArtin.salvetti_cover_contractible` | [SalvettiCoverContractible.lean](../../../lean/OAI/Topology/ArtinGroups/Realizations/SalvettiCoverContractible.lean) | [`OAI/Topology/ArtinGroups/Realizations`](../../../lean/OAI/Topology/ArtinGroups/Realizations/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ArtinCAT0` | [.json](../../../lean/ComparatorChallenges/ArtinCAT0.json) | [.lean](../../../lean/ComparatorChallenges/ArtinCAT0.lean) | 1 | 0 | no | yes |
| `ArtinParabolicIntersections` | [.json](../../../lean/ComparatorChallenges/ArtinParabolicIntersections.json) | [.lean](../../../lean/ComparatorChallenges/ArtinParabolicIntersections.lean) | 4 | 0 | yes | no |
| `HarmonicArtin` | [.json](../../../lean/ComparatorChallenges/HarmonicArtin.json) | [.lean](../../../lean/ComparatorChallenges/HarmonicArtin.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

The Salvetti complex of every finite-rank Artin group is aspherical, proving the Artin $K(\pi,1)$ conjecture. Arbitrary intersections of its parabolic subgroups are parabolic, proving the Parabolic Intersection Conjecture. An explicit Artin group admits no proper cocompact isometric action on any nonempty proper CAT$(0)$ space.

