# 199 — Counterexamples to conjectures of Auslander--Reiten, Tachikawa, and Nakayama

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/199.md`](../../../lean/docs/199.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 3 in · 3 out |
| Claim shapes | resolution, counterexample, classification |
| Topics | [number-fields](../topics/number-fields.md) · [analytic-number-theory](../topics/analytic-number-theory.md) · [commutative-algebra](../topics/commutative-algebra.md) · [galois-theory](../topics/galois-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-counterexample-to-Tachikawas-second-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/build/paper.tex) | — |
| [`An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026`](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/) | [README.md](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [AuslanderReiten](../../../lean/ComparatorChallenges/AuslanderReiten.json) | `OAI.ArExplicit.Statement.main` | [All.lean](../../../lean/OAI/Algebra/AuslanderReiten/All.lean) | [`OAI/Algebra/AuslanderReiten`](../../../lean/OAI/Algebra/AuslanderReiten/) |
| [Tachikawa](../../../lean/ComparatorChallenges/Tachikawa.json) | `OAI.Tachikawa.main_theorem` | [Counterexample.lean](../../../lean/OAI/RingTheory/Tachikawa/Counterexample.lean) | [`OAI/RingTheory/Tachikawa`](../../../lean/OAI/RingTheory/Tachikawa/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `AuslanderReiten` | [.json](../../../lean/ComparatorChallenges/AuslanderReiten.json) | [.lean](../../../lean/ComparatorChallenges/AuslanderReiten.lean) | 1 | 0 | no | yes |
| `Tachikawa` | [.json](../../../lean/ComparatorChallenges/Tachikawa.json) | [.lean](../../../lean/ComparatorChallenges/Tachikawa.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs finite-dimensional algebras over a characteristic-two rational-function field that disprove the Auslander--Reiten and Gorenstein-projective conjectures, and Tachikawa's second conjecture. An associated endomorphism algebra also disproves the classical, generalized and strong Nakayama conjectures, the Auslander--Gorenstein conjecture, and the Wakamatsu tilting conjecture. The counterexamples persist under every extension of the base field.

