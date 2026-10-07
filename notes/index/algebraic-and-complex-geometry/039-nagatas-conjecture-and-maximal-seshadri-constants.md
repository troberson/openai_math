# 039 — Nagata's conjecture and maximal Seshadri constants

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 4 (2 formalized at source level) |
| Scope note | [`lean/docs/039.md`](../../../lean/docs/039.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 4 out |
| Claim shapes | bound, classification, uniform |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [curves](../topics/curves.md) · [partial-differential-equations](../topics/partial-differential-equations.md) · [surfaces](../topics/surfaces.md) · [abelian-varieties](../topics/abelian-varieties.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026`](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/) | [main.pdf](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/main.pdf) | [build/](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/build/) | [README.md](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/README.md) | no | [main.tex](../../../preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/build/main.tex) | — |
| [`Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026`](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/) | [main.pdf](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/main.pdf) | [build/](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/) | [README.md](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/README.md) | yes | [preamble.tex](../../../preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/preamble.tex) | — |
| [`Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026`](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/) | [seshadri-positive-characteristic.pdf](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/seshadri-positive-characteristic.pdf) | [build/](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/build/) | [README.md](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/README.md) | no | [main.tex](../../../preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/build/build/main.tex) | — |
| [`Nagatas-Conjecture-for-Plane-Curves-September-23-2026`](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/) | [main.pdf](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/main.pdf) | [build/](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/build/) | [README.md](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [MaximalSeshadriConstants](../../../lean/ComparatorChallenges/MaximalSeshadriConstants.json) | `OAI.MaximalSeshadri.Geometry.maximalSeshadriConstants` | [Main.lean](../../../lean/OAI/AlgebraicGeometry/Seshadri/Main.lean) | [`OAI/AlgebraicGeometry/Seshadri`](../../../lean/OAI/AlgebraicGeometry/Seshadri/) |
| [Nagata](../../../lean/ComparatorChallenges/Nagata.json) | `OAI.Nagata.nagata_conjecture` | [Nagata.lean](../../../lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean) | [`OAI/AlgebraicGeometry/PlaneCurves`](../../../lean/OAI/AlgebraicGeometry/PlaneCurves/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MaximalSeshadriConstants` | [.json](../../../lean/ComparatorChallenges/MaximalSeshadriConstants.json) | [.lean](../../../lean/ComparatorChallenges/MaximalSeshadriConstants.lean) | 1 | 0 | no | yes |
| `Nagata` | [.json](../../../lean/ComparatorChallenges/Nagata.json) | [.lean](../../../lean/ComparatorChallenges/Nagata.lean) | 3 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Nagata's strict inequality $\sum_i m_i<d\sqrt r$ for every nonzero effective plane curve of degree $d$ through $r\ge10$ very general complex points, with arbitrary multiplicities $m_i$. It also proves maximal multipoint Seshadri constants $(L^n/r)^{1/n}$ for every smooth polarized projective variety of dimension $n\ge2$ and all sufficiently large $r$: at very general points over $\mathbb C$, and at the geometric generic tuple over any algebraically closed field of positive characteristic.

