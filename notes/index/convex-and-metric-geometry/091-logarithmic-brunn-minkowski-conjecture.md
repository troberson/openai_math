# 091 — The logarithmic Brunn--Minkowski conjecture

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/091.md`](../../../lean/docs/091.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound |
| Topics | [convex-geometry](../topics/convex-geometry.md) · [measure-theory](../topics/measure-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026`](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/) | [README.md](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [LogBrunnMinkowski](../../../lean/ComparatorChallenges/LogBrunnMinkowski.json) | `OAI.LogBrunnMinkowski.main` | [BrunnMinkowski.lean](../../../lean/OAI/Geometry/LogVolume/BrunnMinkowski.lean) | [`OAI/Geometry/LogVolume`](../../../lean/OAI/Geometry/LogVolume/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `LogBrunnMinkowski` | [.json](../../../lean/ComparatorChallenges/LogBrunnMinkowski.json) | [.lean](../../../lean/ComparatorChallenges/LogBrunnMinkowski.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the logarithmic Brunn--Minkowski inequality for origin-symmetric convex bodies in every dimension, and the scalar-dilation B-conjecture for all even log-concave Radon measures. For Lebesgue volume it also proves the additive $L_p$ Brunn--Minkowski inequality for full-dimensional origin-symmetric convex bodies throughout $0<p<1$.

