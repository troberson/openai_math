# 327 — Markov type characterizes superreflexivity

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/327.md`](../../../lean/docs/327.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | classification, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026`](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/) | [paper.pdf](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf) | [build/](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/build/) | [README.md](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [MarkovType](../../../lean/ComparatorChallenges/MarkovType.json) | `OAI.MarkovSuperreflexivity.hasNontrivialMarkovType_iff_hasEquivalentUCNorm` | [Main.lean](../../../lean/OAI/Analysis/MarkovType/Main.lean) | [`OAI/Analysis/MarkovType`](../../../lean/OAI/Analysis/MarkovType/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MarkovType` | [.json](../../../lean/ComparatorChallenges/MarkovType.json) | [.lean](../../../lean/ComparatorChallenges/MarkovType.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that every real Banach space with Markov type $p$ for some $p>1$ admits an equivalent uniformly convex norm, answering Naor's renorming question. Together with the known converse, this characterizes superreflexivity by nontrivial Markov type.

