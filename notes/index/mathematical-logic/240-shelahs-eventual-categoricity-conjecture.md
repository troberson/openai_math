# 240 — Shelah's eventual categoricity conjecture

|  |  |
|---|---|
| Discipline | [Mathematical logic](../disciplines/mathematical-logic.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/240.md`](../../../lean/docs/240.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | bound, uniform, conditional |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026`](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/) | [paper.pdf](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/paper.pdf) | [build/](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/) | [README.md](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/paper.tex) | — |
| [`Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026`](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/) | [paper.pdf](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/paper.pdf) | [build/](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/build/) | [README.md](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/README.md) | no | [main.tex](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CHObstruction](../../../lean/ComparatorChallenges/CHObstruction.json) | `OAI.CHObstruction.main` | [Main.lean](../../../lean/OAI/ModelTheory/Categoricity/Main.lean) | [`OAI/ModelTheory/Categoricity`](../../../lean/OAI/ModelTheory/Categoricity/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CHObstruction` | [.json](../../../lean/ComparatorChallenges/CHObstruction.json) | [.lean](../../../lean/ComparatorChallenges/CHObstruction.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Shelah's eventual categoricity conjecture in ZFC: for each bound on the L\"owenheim--Skolem number, a uniform threshold makes categoricity of an abstract elementary class in one cardinal above that threshold imply categoricity throughout the same tail. Categoricity means uniqueness up to isomorphism at a given cardinality. Under the continuum hypothesis, a proposed specific Hanf threshold need not suffice.

