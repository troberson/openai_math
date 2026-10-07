# 250 — The Boone--Higman conjecture and higher finiteness

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/250.md`](../../../lean/docs/250.md) |
| Comparator configs | 3 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 1 out |
| Claim shapes | — |
| Topics | [algebraic-topology](../topics/algebraic-topology.md) · [group-theory](../topics/group-theory.md) · [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-universal-group-of-type-F-infinity-September-23-2026`](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/) | [paper.pdf](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf) | [build/](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/build/) | [README.md](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/build/main.tex) | — |
| [`Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026`](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/build/) | [README.md](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/build/paper.tex) | — |
| [`Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026`](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/) | [paper.pdf](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/paper.pdf) | [build/](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/build/) | [README.md](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/README.md) | no | [main.tex](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [UniversalFInfinity](../../../lean/ComparatorChallenges/UniversalFInfinity.json) | `OAI.UniversalFInfinity.universal_group_of_type_FInfinity` | [Main.lean](../../../lean/OAI/GroupTheory/UniversalGroup/Main.lean) | [`OAI/GroupTheory/UniversalGroup`](../../../lean/OAI/GroupTheory/UniversalGroup/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BooneHigman` | [.json](../../../lean/ComparatorChallenges/BooneHigman.json) | [.lean](../../../lean/ComparatorChallenges/BooneHigman.lean) | 1 | 0 | no | no |
| `SimpleOvergroups` | [.json](../../../lean/ComparatorChallenges/SimpleOvergroups.json) | [.lean](../../../lean/ComparatorChallenges/SimpleOvergroups.lean) | 1 | 0 | no | no |
| `UniversalFInfinity` | [.json](../../../lean/ComparatorChallenges/UniversalFInfinity.json) | [.lean](../../../lean/ComparatorChallenges/UniversalFInfinity.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

A finitely generated group has decidable word problem exactly when it embeds in a finitely presented simple group, proving the Boone--Higman conjecture. The target can have type $F_\infty$: a classifying space with finitely many cells in each dimension. A single group of type $F_\infty$ can also contain every finitely presented group.

