# 277 — Threshold repetition for entangled games

|  |  |
|---|---|
| Discipline | [Mathematical physics](../disciplines/mathematical-physics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/277.md`](../../../lean/docs/277.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026`](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/) | [paper.pdf](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/paper.pdf) | [build/](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/build/) | [README.md](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [EntangledGames](../../../lean/ComparatorChallenges/EntangledGames.json) | `OAI.ThresholdParallelRepetition.threshold_parallel_repetition` | [Main.lean](../../../lean/OAI/Probability/EntangledGames/Main.lean) | [`OAI/Probability/EntangledGames`](../../../lean/OAI/Probability/EntangledGames/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `EntangledGames` | [.json](../../../lean/ComparatorChallenges/EntangledGames.json) | [.lean](../../../lean/ComparatorChallenges/EntangledGames.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves exponential threshold repetition for every finite two-player one-round game: if its entangled value is $v<1$, the probability of winning at least a fraction $v+\delta$ of $k$ independent repetitions decays exponentially in $k$, for $0<\delta<1-v$. Arbitrary joint finite-dimensional entangled strategies and correlated question distributions are allowed.

