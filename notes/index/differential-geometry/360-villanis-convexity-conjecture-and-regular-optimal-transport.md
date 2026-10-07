# 360 — Villani’s convexity conjecture and regular optimal transport

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/360.md`](../../../lean/docs/360.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, bound |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026`](../../../preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/) | [paper.pdf](../../../preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf) | [build/](../../../preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/) | [README.md](../../../preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/build/main.tex) | — |
| [`Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026`](../../../preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/) | [paper.pdf](../../../preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf) | [build/](../../../preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/build/) | [README.md](../../../preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/README.md) | yes | [main.tex](../../../preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BiholderTransport](../../../lean/ComparatorChallenges/BiholderTransport.json) | `OAI.WeakMTWTransport.uniform_biHolder_transport` | [Main.lean](../../../lean/OAI/Analysis/BiholderTransport/Main.lean) | [`OAI/Analysis/BiholderTransport`](../../../lean/OAI/Analysis/BiholderTransport/) |
| [WeakMTWGlobalSupport](../../../lean/ComparatorChallenges/WeakMTWGlobalSupport.json) | `OAI.WeakMTWGlobalSupport.current_main_convexity` | [Convexity.lean](../../../lean/OAI/Geometry/WeakMTW/Convexity.lean) | [`OAI/Geometry/WeakMTW`](../../../lean/OAI/Geometry/WeakMTW/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BiholderTransport` | [.json](../../../lean/ComparatorChallenges/BiholderTransport.json) | [.lean](../../../lean/ComparatorChallenges/BiholderTransport.lean) | 1 | 0 | no | yes |
| `WeakMTWGlobalSupport` | [.json](../../../lean/ComparatorChallenges/WeakMTWGlobalSupport.json) | [.lean](../../../lean/ComparatorChallenges/WeakMTWGlobalSupport.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

On every closed connected Riemannian manifold of dimension at least two satisfying weak Ma--Trudinger--Wang curvature, all tangent injectivity domains are convex, resolving Villani’s conjecture in this setting. For squared-distance transport between measurable probability densities bounded above and away from zero, the optimal map and its inverse are H\"older continuous.

