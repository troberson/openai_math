# 096 — The Gaussian propeller conjecture

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/096.md`](../../../lean/docs/096.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | bound, partial |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [computability](../topics/computability.md) · [convex-geometry](../topics/convex-geometry.md) · [measure-theory](../topics/measure-theory.md) · [convex-optimization](../topics/convex-optimization.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026`](../../../preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/) | [main.pdf](../../../preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/main.pdf) | [build/](../../../preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/) | [README.md](../../../preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/README.md) | yes | [main.tex](../../../preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [GaussianPropeller](../../../lean/ComparatorChallenges/GaussianPropeller.json) | `OAI.GaussianPropeller.all_partitions` | [Main.lean](../../../lean/OAI/Probability/GaussianPropeller/Main.lean) | [`OAI/Probability/GaussianPropeller`](../../../lean/OAI/Probability/GaussianPropeller/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GaussianPropeller` | [.json](../../../lean/ComparatorChallenges/GaussianPropeller.json) | [.lean](../../../lean/ComparatorChallenges/GaussianPropeller.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that the sum of squared Gaussian first moments of any finite measurable partition is at most $9/(8\pi)$. In dimension at least two, three planar sectors of angle $2\pi/3$, extended orthogonally, attain the bound. Combined with the separate Unique Games theorem, this proves NP-hardness of improving the loss factor $(8\pi/9)(1-1/k)$ for identity-target kernel clustering with fixed $k\ge3$ on rational centered positive semidefinite inputs.

