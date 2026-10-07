# 243 — Choiceless counting does not capture polynomial time

|  |  |
|---|---|
| Discipline | [Mathematical logic](../disciplines/mathematical-logic.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/243.md`](../../../lean/docs/243.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | uniform |
| Topics | [computability](../topics/computability.md) · [logic](../topics/logic.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026`](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/) | [paper.pdf](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/paper.pdf) | [build/](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/) | [README.md](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Choiceless-polynomial-time-with-counting-does-not-capture-polynomial-time-September-23-2026/build/main.tex) | — |
| [`Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026`](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/) | [paper.pdf](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/paper.pdf) | [build/](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/) | [README.md](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/README.md) | no | [main.tex](../../../preprints/Witnessed-symmetric-choice-is-strictly-stronger-than-choiceless-polynomial-time-with-counting-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ChoicelessPolynomialTime](../../../lean/ComparatorChallenges/ChoicelessPolynomialTime.json) | `OAI.CPTSeparation.main` | [Separation.lean](../../../lean/OAI/ModelTheory/Choiceless/Separation.lean) | [`OAI/ModelTheory/Choiceless`](../../../lean/OAI/ModelTheory/Choiceless/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ChoicelessPolynomialTime` | [.json](../../../lean/ComparatorChallenges/ChoicelessPolynomialTime.json) | [.lean](../../../lean/ComparatorChallenges/ChoicelessPolynomialTime.lean) | 1 | 0 | no | yes |
| `WitnessedChoice` | [.json](../../../lean/ComparatorChallenges/WitnessedChoice.json) | [.lean](../../../lean/ComparatorChallenges/WitnessedChoice.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Confirms the Blass--Gurevich--Shelah noncapture conjecture: consistency of a linear system over $\mathbb F_3$ defines a polynomial-time query on unordered finite structures that choiceless polynomial time with counting cannot express. A separate result shows that adding witnessed symmetric choice strictly increases expressive power. Both separations hold for the full counting formalism, allowing hereditarily finite sets of arbitrary finite rank.

