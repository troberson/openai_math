# 358 — A three-manifold with no conjugate points and no nonpositively curved metric

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/358.md`](../../../lean/docs/358.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [manifolds](../topics/manifolds.md) · [riemannian-geometry](../topics/riemannian-geometry.md) · [metric-geometry](../topics/metric-geometry.md) · [differential-geometry](../topics/differential-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026`](../../../preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/) | [paper.pdf](../../../preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/paper.pdf) | [build/](../../../preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/build/) | [README.md](../../../preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [ConjugatePoints](../../../lean/ComparatorChallenges/ConjugatePoints.json) | `OAI.ThreeManifold.main_theorem` | [ThreeManifold.lean](../../../lean/OAI/Geometry/ConjugatePoints/ThreeManifold.lean) | [`OAI/Geometry/ConjugatePoints`](../../../lean/OAI/Geometry/ConjugatePoints/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ConjugatePoints` | [.json](../../../lean/ComparatorChallenges/ConjugatePoints.json) | [.lean](../../../lean/ComparatorChallenges/ConjugatePoints.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a closed connected orientable smooth three-manifold that admits a metric without conjugate points but no metric of nonpositive sectional curvature. This answers negatively, already in dimension three, whether the first metric-existence property implies the second.

