# 095 — Hyperbolicity cones without semidefinite lifts

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/095.md`](../../../lean/docs/095.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, counterexample |
| Topics | [convex-optimization](../topics/convex-optimization.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026`](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/) | [nonspectrahedral-hyperbolicity-cone.pdf](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/nonspectrahedral-hyperbolicity-cone.pdf) | [build/](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/build/) | [README.md](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-Nonspectrahedral-Hyperbolicity-Cone-September-24-2026/build/main.tex) | — |
| [`An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026`](../../../preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/) | [Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone.pdf](../../../preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone.pdf) | [build/](../../../preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/build/) | [README.md](../../../preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/README.md) | no | [main.tex](../../../preprints/An-Exact-Semidefinite-Lift-of-a-Nonspectrahedral-Hyperbolicity-Cone-October-5-2026/build/main.tex) | — |
| [`Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026`](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/) | [nonliftable-hyperbolicity.pdf](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/nonliftable-hyperbolicity.pdf) | [build/](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/build/) | [README.md](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/README.md) | no | [main.tex](../../../preprints/Hyperbolicity-Cones-Without-Semidefinite-Lifts-October-5-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [HyperbolicCones](../../../lean/ComparatorChallenges/HyperbolicCones.json) | `OAI.Paper256.main_result` | [Main.lean](../../../lean/OAI/Analysis/HyperbolicCones/Main.lean) | [`OAI/Analysis/HyperbolicCones`](../../../lean/OAI/Analysis/HyperbolicCones/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HyperbolicCones` | [.json](../../../lean/ComparatorChallenges/HyperbolicCones.json) | [.lean](../../../lean/ComparatorChallenges/HyperbolicCones.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves the Projected Lax conjecture: some hyperbolicity cones are not spectrahedral shadows. The examples admit no exact finite affine semidefinite lift, regardless of the number of auxiliary variables or the real coefficients used. This also disproves the generalized Lax conjecture that every hyperbolicity cone is spectrahedral.

