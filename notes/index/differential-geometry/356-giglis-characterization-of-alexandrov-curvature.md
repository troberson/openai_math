# 356 — Gigli's characterization of Alexandrov curvature

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/356.md`](../../../lean/docs/356.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | classification |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026`](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/) | [main.pdf](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf) | [build/](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/build/) | [README.md](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/README.md) | no | [main.tex](../../../preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/build/main.tex) | — |
| [`Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026`](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/) | [weak-hessian-geodesics.pdf](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf) | [build/](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/build/) | [README.md](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [WeakHessian](../../../lean/ComparatorChallenges/WeakHessian.json) | `OAI.WeakHessian.every_geodesic` | [Main.lean](../../../lean/OAI/Geometry/WeakHessian/Main.lean) | [`OAI/Geometry/WeakHessian`](../../../lean/OAI/Geometry/WeakHessian/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `WeakHessian` | [.json](../../../lean/ComparatorChallenges/WeakHessian.json) | [.lean](../../../lean/ComparatorChallenges/WeakHessian.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Gigli's conjecture: in every integer dimension $n\ge2$, Alexandrov curvature at least $\kappa$ is characterized by the full-support $\operatorname{RCD}((n-1)\kappa,n)$ condition with reference measure $\mathcal H^n$ and distributional sectional curvature at least $\kappa$ in the original global test classes. The RCD condition is unreduced.

