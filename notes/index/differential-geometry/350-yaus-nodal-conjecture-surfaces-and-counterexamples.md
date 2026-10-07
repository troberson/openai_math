# 350 — Yau's nodal conjecture: surfaces and counterexamples

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 3 (2 formalized at source level) |
| Scope note | [`lean/docs/350.md`](../../../lean/docs/350.md) |
| Comparator configs | 3 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | counterexample, bound, partial |
| Topics | [riemannian-geometry](../topics/riemannian-geometry.md) · [curves](../topics/curves.md) · [spectral-theory](../topics/spectral-theory.md) · [surfaces](../topics/surfaces.md) · [fractal-geometry](../topics/fractal-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026`](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/) | [paper.pdf](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf) | [build/](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/build/) | [README.md](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/build/main.tex) | — |
| [`Sharp-nodal-length-on-smooth-surfaces-September-23-2026`](../../../preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/) | [paper.pdf](../../../preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/paper.pdf) | [build/](../../../preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/build/) | [README.md](../../../preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/build/paper.tex) | — |
| [`Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026`](../../../preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/) | [paper.pdf](../../../preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf) | [build/](../../../preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/build/) | [README.md](../../../preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SmoothYau](../../../lean/ComparatorChallenges/SmoothYau.json) | `OAI.YauCounterexamples.sphere_three` | [ThreeSphere.lean](../../../lean/OAI/Geometry/SmoothYau/SphereMetric/ThreeSphere.lean) | [`OAI/Geometry/SmoothYau/SphereMetric`](../../../lean/OAI/Geometry/SmoothYau/SphereMetric/) |
| [SmoothYau](../../../lean/ComparatorChallenges/SmoothYau.json) | `OAI.YauCounterexamples.sphere_two_torus_two` | [SphereProduct.lean](../../../lean/OAI/Geometry/SmoothYau/ProductMetric/SphereProduct.lean) | [`OAI/Geometry/SmoothYau/ProductMetric`](../../../lean/OAI/Geometry/SmoothYau/ProductMetric/) |
| [YauCounterexample](../../../lean/ComparatorChallenges/YauCounterexample.json) | `OAI.Yau.Target.yau_nodal_set_upper_bound_counterexample` | [Main.lean](../../../lean/OAI/Geometry/NodalSets/Main.lean) | [`OAI/Geometry/NodalSets`](../../../lean/OAI/Geometry/NodalSets/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `NodalLength` | [.json](../../../lean/ComparatorChallenges/NodalLength.json) | [.lean](../../../lean/ComparatorChallenges/NodalLength.lean) | 1 | 0 | no | no |
| `SmoothYau` | [.json](../../../lean/ComparatorChallenges/SmoothYau.json) | [.lean](../../../lean/ComparatorChallenges/SmoothYau.lean) | 2 | 0 | no | yes |
| `YauCounterexample` | [.json](../../../lean/ComparatorChallenges/YauCounterexample.json) | [.lean](../../../lean/ComparatorChallenges/YauCounterexample.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the sharp $C\sqrt\lambda$ upper bound for nodal length on every fixed smooth closed surface, completing Yau's conjecture there. The upper bound fails for fixed smooth metrics in dimensions three and four, including metrics on $S^3$ arbitrarily close to round. In dimension five, nodal measure can grow faster than $\lambda^{1/2+\varepsilon_0}$ for some fixed $\varepsilon_0>0$, ruling out even arbitrarily small power losses.

