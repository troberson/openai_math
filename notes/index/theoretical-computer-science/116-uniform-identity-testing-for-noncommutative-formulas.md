# 116 — Uniform identity testing for noncommutative formulas

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/116.md`](../../../lean/docs/116.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | bound, classification |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026`](../../../preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/) | [One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf](../../../preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026.pdf) | [build/](../../../preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/) | [README.md](../../../preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/README.md) | no | [paper.tex](../../../preprints/One-Rational-Matrix-Hitting-Point-for-Noncommutative-Formulas-September-24-2026/build/paper.tex) | — |
| [`Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026`](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/) | [Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026.pdf) | [build/](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/build/) | [README.md](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Polynomial-Hitting-Lists-for-Noncommutative-Rational-Formulas-September-24-2026/build/main.tex) | — |
| [`Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026`](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/) | [uniform-matrix-hitting-points-positive-characteristic.pdf](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/uniform-matrix-hitting-points-positive-characteristic.pdf) | [build/](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/) | [README.md](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/README.md) | no | [main.tex](../../../preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [RationalHitting](../../../lean/ComparatorChallenges/RationalHitting.json) | `OAI.RationalHitting.main` | [Main.lean](../../../lean/OAI/Computability/RationalHitting/Main.lean) | [`OAI/Computability/RationalHitting`](../../../lean/OAI/Computability/RationalHitting/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FormulaHitting` | [.json](../../../lean/ComparatorChallenges/FormulaHitting.json) | [.lean](../../../lean/ComparatorChallenges/FormulaHitting.lean) | 1 | 0 | no | no |
| `RationalHitting` | [.json](../../../lean/ComparatorChallenges/RationalHitting.json) | [.lean](../../../lean/ComparatorChallenges/RationalHitting.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For each characteristic, constructs in deterministic polynomial bit time a polynomial-dimensional matrix tuple detecting every nonzero division-free noncommutative formula of bounded size over any field of that characteristic. Rational formulas over $\mathbb Q$ also admit polynomial-size hitting lists whenever they have a defined rational-matrix evaluation.

