# 212 — No bigeodesics and smooth limit shapes in planar first-passage percolation

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/212.md`](../../../lean/docs/212.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`No-bigeodesics-in-planar-first-passage-percolation-September-24-2026`](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/) | [main.pdf](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf) | [build/](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/) | [README.md](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/README.md) | no | [main.tex](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/main.tex) | — |
| [`Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026`](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/) | [main.pdf](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf) | [build/](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/) | [README.md](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PlanarFirstPassage](../../../lean/ComparatorChallenges/PlanarFirstPassage.json) | `OAI.PlanarFPP.manuscriptMain` | [BoundaryCurve.lean](../../../lean/OAI/Probability/FirstPassage/BoundaryCurve.lean) | [`OAI/Probability/FirstPassage`](../../../lean/OAI/Probability/FirstPassage/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GammaPassage` | [.json](../../../lean/ComparatorChallenges/GammaPassage.json) | [.lean](../../../lean/ComparatorChallenges/GammaPassage.lean) | 1 | 0 | no | no |
| `PlanarFirstPassage` | [.json](../../../lean/ComparatorChallenges/PlanarFirstPassage.json) | [.lean](../../../lean/ComparatorChallenges/PlanarFirstPassage.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that planar first-passage percolation has no doubly infinite geodesic for iid nonnegative nonatomic edge weights when the minimum of four weights has finite second moment. For exponential weights, the limit shape is strictly convex with $C^1$ boundary. Differentiability also holds for every Gamma law with positive shape and rate.

