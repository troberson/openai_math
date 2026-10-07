# 107 — Matrix multiplication with exponent at most $9/4$

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 3 (3 formalized at source level) |
| Scope note | [`lean/docs/107.md`](../../../lean/docs/107.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 2 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, classification |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026`](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/) | [Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf) | [build/](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/build/) | [README.md](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/build/main.tex) | [verification/](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/verification/) |
| [`Matrix-Multiplication-Nine-Fourths-October-2-2026`](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/) | [paper.pdf](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf) | [build/](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/) | [README.md](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/README.md) | yes | [paper.tex](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/build/paper.tex) | — |
| [`Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026`](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/) | [Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf) | [build/](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/build/) | [README.md](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/build/main.tex) | [verification/](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/verification/) |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [MatrixFields](../../../lean/ComparatorChallenges/MatrixFields.json) | `OAI.MatrixAllFields.MatrixMultiplication.AllFieldMain.omega_lt_source_constant` | [AllFieldsBound.lean](../../../lean/OAI/LinearAlgebra/MatrixFields/Conclusions/AllFieldsBound.lean) | [`OAI/LinearAlgebra/MatrixFields/Conclusions`](../../../lean/OAI/LinearAlgebra/MatrixFields/Conclusions/) |
| [MatrixMultiplication](../../../lean/ComparatorChallenges/MatrixMultiplication.json) | `OAI.MatrixMultiplication.complex_alpha_gt_93_div_200` | [Main.lean](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean) | [`OAI/LinearAlgebra/MatrixMultiplication`](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/) |
| [MatrixMultiplication](../../../lean/ComparatorChallenges/MatrixMultiplication.json) | `OAI.MatrixMultiplication.complex_omega_le_nine_quarters` | [Main.lean](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean) | [`OAI/LinearAlgebra/MatrixMultiplication`](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/) |
| [MatrixMultiplication](../../../lean/ComparatorChallenges/MatrixMultiplication.json) | `OAI.MatrixMultiplication.complex_rectangular_omega_lt_523_div_250` | [Main.lean](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean) | [`OAI/LinearAlgebra/MatrixMultiplication`](../../../lean/OAI/LinearAlgebra/MatrixMultiplication/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MatrixFields` | [.json](../../../lean/ComparatorChallenges/MatrixFields.json) | [.lean](../../../lean/ComparatorChallenges/MatrixFields.lean) | 1 | 0 | no | yes |
| `MatrixMultiplication` | [.json](../../../lean/ComparatorChallenges/MatrixMultiplication.json) | [.lean](../../../lean/ComparatorChallenges/MatrixMultiplication.lean) | 3 | 0 | no | yes |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026` | [verification/](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/verification/) | no | no |
| `Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026` | [verification/](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves $\omega\le9/4$ over $\mathbb C$, giving $O_\varepsilon(n^{9/4+\varepsilon})$ arithmetic operations for square matrix multiplication. In characteristic zero, some inner dimension $n^a$ with $a>0.465$ permits $n^{2+o(1)}$ rectangular multiplication. Further square bounds give $\omega<2.258$ outside finitely many positive characteristics and $\omega<2.371054886006746$ over every fixed field.

