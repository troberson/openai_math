# 241 — Rigidity of the Turing degrees

|  |  |
|---|---|
| Discipline | [Mathematical logic](../disciplines/mathematical-logic.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/241.md`](../../../lean/docs/241.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Rigidity-of-the-Turing-degrees-September-24-2026`](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/) | [paper.pdf](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/paper.pdf) | [build/](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/build/) | [README.md](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Rigidity-of-the-Turing-degrees-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [DegreeRigidity](../../../lean/ComparatorChallenges/DegreeRigidity.json) | `OAI.TuringRigidity.ManuscriptMain.rigidity` | [Main.lean](../../../lean/OAI/Computability/DegreeRigidity/Main.lean) | [`OAI/Computability/DegreeRigidity`](../../../lean/OAI/Computability/DegreeRigidity/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DegreeRigidity` | [.json](../../../lean/ComparatorChallenges/DegreeRigidity.json) | [.lean](../../../lean/ComparatorChallenges/DegreeRigidity.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Every order automorphism of the Turing degrees is the identity, resolving their rigidity problem. Thus no nontrivial relabeling of degrees preserves the ordering by relative computability.

