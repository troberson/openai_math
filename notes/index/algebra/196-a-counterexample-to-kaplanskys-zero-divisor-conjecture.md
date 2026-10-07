# 196 — A counterexample to Kaplansky's zero-divisor conjecture

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/196.md`](../../../lean/docs/196.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026`](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/) | [paper.pdf](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf) | [build/](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/) | [README.md](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TorsionFreeZeroDivisors](../../../lean/ComparatorChallenges/TorsionFreeZeroDivisors.json) | `OAI.TorsionFreeZeroDivisors.main` | [Main.lean](../../../lean/OAI/Algebra/GroupRing/Main.lean) | [`OAI/Algebra/GroupRing`](../../../lean/OAI/Algebra/GroupRing/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TorsionFreeZeroDivisors` | [.json](../../../lean/ComparatorChallenges/TorsionFreeZeroDivisors.json) | [.lean](../../../lean/ComparatorChallenges/TorsionFreeZeroDivisors.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a finitely presented torsion-free group $G$ whose group algebra $\mathbb F_2[G]$ has nonzero zero divisors, disproving Kaplansky's zero-divisor conjecture. The group has a finite two-dimensional classifying space.

