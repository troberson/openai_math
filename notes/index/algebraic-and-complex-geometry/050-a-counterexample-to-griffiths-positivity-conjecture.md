# 050 — A counterexample to Griffiths' positivity conjecture

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/050.md`](../../../lean/docs/050.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [surfaces](../topics/surfaces.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026`](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/) | [paper.pdf](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf) | [build/](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/) | [README.md](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [QuadricBundles](../../../lean/ComparatorChallenges/QuadricBundles.json) | `OAI.QuadricCounterexample.main_theorem` | [Main.lean](../../../lean/OAI/Geometry/QuadricBundles/Main.lean) | [`OAI/Geometry/QuadricBundles`](../../../lean/OAI/Geometry/QuadricBundles/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `QuadricBundles` | [.json](../../../lean/ComparatorChallenges/QuadricBundles.json) | [.lean](../../../lean/ComparatorChallenges/QuadricBundles.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs ample rank-two bundles on $\mathbb P^1\times\mathbb P^1$ with no smooth Hermitian metric of strictly Griffiths-positive curvature, disproving Griffiths' positivity conjecture already on the quadric surface.

