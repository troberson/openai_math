# 027 — Integral density on curve character varieties

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/027.md`](../../../lean/docs/027.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, density, uniform |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [curves](../topics/curves.md) · [surfaces](../topics/surfaces.md) · [arithmetic-geometry](../topics/arithmetic-geometry.md) · [number-fields](../topics/number-fields.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Integral-points-on-character-varieties-of-curves-September-25-2026`](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/) | [paper.pdf](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf) | [build/](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/) | [README.md](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CharacterVarietiesAllSeamsSupport](../../../lean/ComparatorChallenges/CharacterVarietiesAllSeamsSupport.json) | `OAI.IntegralCharacterVarieties.SurfacePresentation.Diagram.producedMarkedValues_allSeams` | [ProducedSolution.lean](../../../lean/OAI/AlgebraicGeometry/CharacterVarieties/Seams/ProducedSolution.lean) | [`OAI/AlgebraicGeometry/CharacterVarieties/Seams`](../../../lean/OAI/AlgebraicGeometry/CharacterVarieties/Seams/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CharacterVarietiesAllSeamsSupport` | [.json](../../../lean/ComparatorChallenges/CharacterVarietiesAllSeamsSupport.json) | [.lean](../../../lean/ComparatorChallenges/CharacterVarietiesAllSeamsSupport.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the determinant-one curve case of Litt's integral-density question. For every smooth connected complex algebraic curve and every rank, integral points become Zariski dense in every component of its $\mathrm{SL}_r$ character variety over the full ring of integers of one number field. Prescribed quasi-unipotent boundary conjugacy classes are allowed, including nonsemisimple classes.

