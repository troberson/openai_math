# 081 — The David--Semmes Riesz-transform problem in higher codimension

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/081.md`](../../../lean/docs/081.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026`](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/) | [paper.pdf](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf) | [build/](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/) | [README.md](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [RieszQuantitative](../../../lean/ComparatorChallenges/RieszQuantitative.json) | `OAI.RieszRectifiability.quantitative_higher_codimension_riesz_rectifiability` | [Rectifiability.lean](../../../lean/OAI/Analysis/RieszRectifiability/Uniformity/Rectifiability.lean) | [`OAI/Analysis/RieszRectifiability/Uniformity`](../../../lean/OAI/Analysis/RieszRectifiability/Uniformity/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `RieszQuantitative` | [.json](../../../lean/ComparatorChallenges/RieszQuantitative.json) | [.lean](../../../lean/ComparatorChallenges/RieszQuantitative.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the remaining higher-codimension Riesz-transform rectifiability problem: for $d\ge4$ and $2\le n\le d-2$, an $n$-Ahlfors--David regular Radon measure on $\mathbb R^d$ is uniformly $n$-rectifiable whenever its $n$-dimensional Riesz transform is uniformly $L^2$-bounded over all positive hard truncations. The rectifiability bounds depend only on dimension, regularity and operator bounds.

