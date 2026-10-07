# 244 — The partition principle does not imply choice

|  |  |
|---|---|
| Discipline | [Mathematical logic](../disciplines/mathematical-logic.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/244.md`](../../../lean/docs/244.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample, conditional |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Partition-Principle-does-not-imply-Choice-September-24-2026`](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/) | [partition-principle-without-choice.pdf](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/partition-principle-without-choice.pdf) | [build/](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/) | [README.md](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/README.md) | yes | [main.tex](../../../preprints/The-Partition-Principle-does-not-imply-Choice-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PartitionPrinciple](../../../lean/ComparatorChallenges/PartitionPrinciple.json) | `OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice` | [Separation.lean](../../../lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean) | [`OAI/SetTheory/PartitionPrinciple/Models`](../../../lean/OAI/SetTheory/PartitionPrinciple/Models/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PartitionConsistency` | [.json](../../../lean/ComparatorChallenges/PartitionConsistency.json) | [.lean](../../../lean/ComparatorChallenges/PartitionConsistency.lean) | 1 | 0 | no | no |
| `PartitionPrinciple` | [.json](../../../lean/ComparatorChallenges/PartitionPrinciple.json) | [.lean](../../../lean/ComparatorChallenges/PartitionPrinciple.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Assuming ZF is consistent, constructs a model in which every surjective image of a set injects into that set, yet the axiom of choice fails. Choice for ordinal-indexed families still holds. From any countable transitive model of ZFC, a separate construction gives a transitive symmetric extension with these properties and no new countable sequences of ground-model elements.

