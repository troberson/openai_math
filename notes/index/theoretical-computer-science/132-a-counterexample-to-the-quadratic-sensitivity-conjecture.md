# 132 — A counterexample to the quadratic sensitivity conjecture

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/132.md`](../../../lean/docs/132.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026`](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/) | [paper.pdf](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf) | [build/](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/) | [README.md](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SensitivitySeparation](../../../lean/ComparatorChallenges/SensitivitySeparation.json) | `OAI.Paper320.quantitative_separation` | [Separation.lean](../../../lean/OAI/Combinatorics/Sensitivity/Separation.lean) | [`OAI/Combinatorics/Sensitivity`](../../../lean/OAI/Combinatorics/Sensitivity/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SensitivitySeparation` | [.json](../../../lean/ComparatorChallenges/SensitivitySeparation.json) | [.lean](../../../lean/ComparatorChallenges/SensitivitySeparation.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs total Boolean functions with block sensitivity $\operatorname{bs}(f)\ge s(f)^\alpha$ for a fixed $\alpha>2$, disproving the quadratic strengthening of the Sensitivity Conjecture. Here $s(f)$ counts influential individual-bit flips, while block sensitivity allows disjoint groups of bits to change together.

