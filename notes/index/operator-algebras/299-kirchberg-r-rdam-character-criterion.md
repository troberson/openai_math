# 299 — The Kirchberg--R\o rdam character criterion

|  |  |
|---|---|
| Discipline | [Operator algebras](../disciplines/operator-algebras.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/299.md`](../../../lean/docs/299.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Topics | [operator-algebras](../topics/operator-algebras.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Kirchberg-Rordam-character-criterion-September-25-2026`](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/) | [paper.pdf](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf) | [build/](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/build/) | [README.md](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CharacterCriterion](../../../lean/ComparatorChallenges/CharacterCriterion.json) | `OAI.KirchbergRordam.character_criterion` | [Main.lean](../../../lean/OAI/Analysis/CharacterCriterion/Main.lean) | [`OAI/Analysis/CharacterCriterion`](../../../lean/OAI/Analysis/CharacterCriterion/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CharacterCriterion` | [.json](../../../lean/ComparatorChallenges/CharacterCriterion.json) | [.lean](../../../lean/ComparatorChallenges/CharacterCriterion.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

A nonzero unital separable complex $C^*$-algebra is Jiang--Su stable exactly when its norm central-sequence algebra has no characters, for every free ultrafilter. This answers the Kirchberg--R\o rdam character question. Also, the infinite minimal tensor power of every such algebra without characters is Jiang--Su stable, answering the Dadarlat--Toms question.

