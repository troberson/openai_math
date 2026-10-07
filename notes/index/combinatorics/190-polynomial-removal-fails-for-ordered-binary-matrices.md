# 190 — Polynomial removal fails for ordered binary matrices

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/190.md`](../../../lean/docs/190.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample, bound, density |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026`](../../../preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/) | [paper.pdf](../../../preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf) | [build/](../../../preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/build/) | [README.md](../../../preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [MatrixRemoval](../../../lean/ComparatorChallenges/MatrixRemoval.json) | `OAI.Problem348.no_polynomial_removal_bound` | [Main.lean](../../../lean/OAI/Combinatorics/MatrixRemoval/Main.lean) | [`OAI/Combinatorics/MatrixRemoval`](../../../lean/OAI/Combinatorics/MatrixRemoval/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MatrixRemoval` | [.json](../../../lean/ComparatorChallenges/MatrixRemoval.json) | [.lean](../../../lean/ComparatorChallenges/MatrixRemoval.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves polynomial ordered binary matrix removal with one fixed $66\times66$ zero--one pattern. Matrices can require many binary-entry changes to become pattern-free while their copy density is smaller than every proposed polynomial bound in that distance. Copies preserve row and column orders and match both zeros and ones.

