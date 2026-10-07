# 253 — An infinite finitely presented simple amenable group

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/253.md`](../../../lean/docs/253.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [group-theory](../topics/group-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026`](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/) | [paper.pdf](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf) | [build/](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/build/) | [README.md](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/README.md) | yes | [main.tex](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SimpleAmenable](../../../lean/ComparatorChallenges/SimpleAmenable.json) | `OAI.SimpleAmenable.main` | [Main.lean](../../../lean/OAI/GroupTheory/SimpleAmenable/Main.lean) | [`OAI/GroupTheory/SimpleAmenable`](../../../lean/OAI/GroupTheory/SimpleAmenable/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SimpleAmenable` | [.json](../../../lean/ComparatorChallenges/SimpleAmenable.json) | [.lean](../../../lean/ComparatorChallenges/SimpleAmenable.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs an infinite finitely presented simple amenable group, answering the longstanding question of whether these properties can occur simultaneously.

