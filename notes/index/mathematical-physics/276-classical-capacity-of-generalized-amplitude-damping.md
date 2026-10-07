# 276 — The classical capacity of generalized amplitude damping

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/276.md`](../../../lean/docs/276.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026`](../../../preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/) | [paper.pdf](../../../preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf) | [build/](../../../preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/build/) | [README.md](../../../preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [AmplitudeDamping](../../../lean/ComparatorChallenges/AmplitudeDamping.json) | `OAI.GAD.main` | [Main.lean](../../../lean/OAI/InformationTheory/AmplitudeDamping/Main.lean) | [`OAI/InformationTheory/AmplitudeDamping`](../../../lean/OAI/InformationTheory/AmplitudeDamping/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `AmplitudeDamping` | [.json](../../../lean/ComparatorChallenges/AmplitudeDamping.json) | [.lean](../../../lean/ComparatorChallenges/AmplitudeDamping.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines the unassisted classical capacity of every qubit generalized amplitude-damping channel, including all damping and thermal parameters. An explicit one-variable optimization gives the capacity, attained by independent two-state signal ensembles with collective decoding. Holevo capacity, minimum output entropy and regularized classical capacity are additive when tensoring with any finite-dimensional quantum channel.

