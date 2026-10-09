# 066 — Bounded klt complements for Fano contractions

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/066.md`](../../../lean/docs/066.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 4 out |
| Claim shapes | bound, classification |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [disordered-systems](../topics/disordered-systems.md) · [commutative-algebra](../topics/commutative-algebra.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Bounded-klt-complements-for-Fano-contractions-September-25-2026`](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/) | [Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf) | [build/](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/) | [README.md](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/README.md) | no | [main.tex](../../../preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/build/main.tex) | — |
| [`Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026`](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/) | [Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf) | [build/](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/build/) | [README.md](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CartierChartCompactnessSupport](../../../lean/ComparatorChallenges/CartierChartCompactnessSupport.json) | `OAI.CartierSections.isCompact_closedChartFieldRetraction_cone` | [ChartCompactness.lean](../../../lean/OAI/AlgebraicGeometry/CartierSections/ChartCompactness.lean) | [`OAI/AlgebraicGeometry/CartierSections`](../../../lean/OAI/AlgebraicGeometry/CartierSections/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CartierChartCompactnessSupport` | [.json](../../../lean/ComparatorChallenges/CartierChartCompactnessSupport.json) | [.lean](../../../lean/ComparatorChallenges/CartierChartCompactnessSupport.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the finite-rational-coefficient form of Shokurov’s bounded-klt-complement conjecture for $\epsilon$-lc complex Fano-type pairs with nef anti-log-canonical divisor. For $\epsilon$-lc Fano contractions over any algebraically closed characteristic-zero field, it gives klt complements near every base point, with index bounded only by dimension and positive rational $\epsilon$.

