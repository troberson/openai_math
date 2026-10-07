# 117 — Uniform sparsest cut: hardness and semidefinite gaps

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/117.md`](../../../lean/docs/117.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026`](../../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/) | [Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf](../../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf) | [build/](../../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/build/) | [README.md](../../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/README.md) | no | [main.tex](../../../preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/build/source/main.tex) | — |
| [`Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026`](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/) | [Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf) | [build/](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/build/) | [README.md](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [UniformSparsestCut](../../../lean/ComparatorChallenges/UniformSparsestCut.json) | `OAI.UniformSparsestCut.mainGap` | [Main.lean](../../../lean/OAI/Combinatorics/SparsestCut/Main.lean) | [`OAI/Combinatorics/SparsestCut`](../../../lean/OAI/Combinatorics/SparsestCut/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `UniformSparsestCut` | [.json](../../../lean/ComparatorChallenges/UniformSparsestCut.json) | [.lean](../../../lean/ComparatorChallenges/UniformSparsestCut.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that approximating Uniform Sparsest Cut within any fixed constant factor is NP-hard, even with nonnegative rational capacities and unit demands. The Goemans--Linial semidefinite relaxation also has integrality gaps of order at least $\sqrt{\log n}/(\log\log n)^3$, approaching the square-root-logarithmic upper bound.

