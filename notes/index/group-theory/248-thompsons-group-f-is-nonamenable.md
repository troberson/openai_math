# 248 — Thompson's group $F$ is nonamenable

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/248.md`](../../../lean/docs/248.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 2 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Thompsons-group-F-is-nonamenable-September-23-2026`](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/) | [paper.pdf](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf) | [build/](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/build/) | [README.md](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ThompsonNonamenability](../../../lean/ComparatorChallenges/ThompsonNonamenability.json) | `OAI.ThompsonNonamenability.thompson_F_nonamenable_composition` | [Main.lean](../../../lean/OAI/GroupTheory/Thompson/Main.lean) | [`OAI/GroupTheory/Thompson`](../../../lean/OAI/GroupTheory/Thompson/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ThompsonNonamenability` | [.json](../../../lean/ComparatorChallenges/ThompsonNonamenability.json) | [.lean](../../../lean/ComparatorChallenges/ThompsonNonamenability.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that Thompson's group $F$, the group of dyadic piecewise linear homeomorphisms of the interval, is nonamenable, resolving its longstanding amenability problem.

