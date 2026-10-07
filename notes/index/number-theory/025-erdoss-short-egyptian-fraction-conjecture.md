# 025 — Erd\H{o}s’s short Egyptian-fraction conjecture

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/025.md`](../../../lean/docs/025.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution |
| Topics | [diophantine-equations](../topics/diophantine-equations.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Short-Egyptian-fractions-September-25-2026`](../../../preprints/Short-Egyptian-fractions-September-25-2026/) | [Short-Egyptian-fractions-September-25-2026.pdf](../../../preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) | [build/](../../../preprints/Short-Egyptian-fractions-September-25-2026/build/) | [README.md](../../../preprints/Short-Egyptian-fractions-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Short-Egyptian-fractions-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [EgyptianFractions](../../../lean/ComparatorChallenges/EgyptianFractions.json) | `OAI.Problem337.counting_double_log_order` | [Main.lean](../../../lean/OAI/NumberTheory/EgyptianFractions/Main.lean) | [`OAI/NumberTheory/EgyptianFractions`](../../../lean/OAI/NumberTheory/EgyptianFractions/) |
| [EgyptianFractions](../../../lean/ComparatorChallenges/EgyptianFractions.json) | `OAI.Problem337.main_double_log_order` | [Main.lean](../../../lean/OAI/NumberTheory/EgyptianFractions/Main.lean) | [`OAI/NumberTheory/EgyptianFractions`](../../../lean/OAI/NumberTheory/EgyptianFractions/) |
| [EgyptianFractions](../../../lean/ComparatorChallenges/EgyptianFractions.json) | `OAI.Problem337.prescribed_denominator_corollary` | [Main.lean](../../../lean/OAI/NumberTheory/EgyptianFractions/Main.lean) | [`OAI/NumberTheory/EgyptianFractions`](../../../lean/OAI/NumberTheory/EgyptianFractions/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `EgyptianFractions` | [.json](../../../lean/ComparatorChallenges/EgyptianFractions.json) | [.lean](../../../lean/ComparatorChallenges/EgyptianFractions.lean) | 9 | 0 | no | yes |
| `ShortEgyptianFractions` | [.json](../../../lean/ComparatorChallenges/ShortEgyptianFractions.json) | [.lean](../../../lean/ComparatorChallenges/ShortEgyptianFractions.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Every rational $a/b$ with $1\le a<b$ is a sum of $O(\log\log b)$ distinct positive unit fractions. The worst-case minimum number of terms has the same order, resolving Erd\H{o}s’s conjecture on short Egyptian fractions.

