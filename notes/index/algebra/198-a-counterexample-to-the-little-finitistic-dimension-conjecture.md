# 198 — A counterexample to the little finitistic-dimension conjecture

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/198.md`](../../../lean/docs/198.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, counterexample |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [commutative-algebra](../topics/commutative-algebra.md) · [category-theory](../topics/category-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-algebra-of-infinite-little-finitistic-dimension-September-23-2026`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/) | [paper.pdf](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/paper.pdf) | [build/](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/) | [README.md](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [FinitisticAsymmetry](../../../lean/ComparatorChallenges/FinitisticAsymmetry.json) | `OAI.LittleFinitistic.extreme_left_right_asymmetry` | [Main.lean](../../../lean/OAI/Algebra/FinitisticAsymmetry/Main.lean) | [`OAI/Algebra/FinitisticAsymmetry`](../../../lean/OAI/Algebra/FinitisticAsymmetry/) |
| [LittleFinitistic](../../../lean/ComparatorChallenges/LittleFinitistic.json) | `OAI.LittleFinitistic.Main.exists_counterexample` | [Main.lean](../../../lean/OAI/Algebra/Finitistic/Main.lean) | [`OAI/Algebra/Finitistic`](../../../lean/OAI/Algebra/Finitistic/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FinitisticAsymmetry` | [.json](../../../lean/ComparatorChallenges/FinitisticAsymmetry.json) | [.lean](../../../lean/ComparatorChallenges/FinitisticAsymmetry.lean) | 1 | 0 | no | yes |
| `LittleFinitistic` | [.json](../../../lean/ComparatorChallenges/LittleFinitistic.json) | [.lean](../../../lean/ComparatorChallenges/LittleFinitistic.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a finite-dimensional complex algebra whose finite-dimensional modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension conjecture.

