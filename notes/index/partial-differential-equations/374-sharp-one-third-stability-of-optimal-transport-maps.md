# 374 — Sharp one-third stability of optimal transport maps

|  |  |
|---|---|
| Discipline | [Partial differential equations](../disciplines/partial-differential-equations.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/374.md`](../../../lean/docs/374.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, uniform |
| Topics | [convex-geometry](../topics/convex-geometry.md) · [optimal-transport](../topics/optimal-transport.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026`](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/) | [article.pdf](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/article.pdf) | [build/](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/) | [README.md](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/README.md) | no | [main.tex](../../../preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/build/source/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Brenier` | [.json](../../../lean/ComparatorChallenges/Brenier.json) | [.lean](../../../lean/ComparatorChallenges/Brenier.lean) | 2 | 12 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For uniform source measure $\rho$ on a compact convex body with interior in dimension at least two, quadratic optimal transport maps satisfy $\|T_\mu-T_\nu\|_{L^2(\rho)}\le C W_2(\mu,\nu)^{1/3}$ uniformly over targets in a fixed compact set. The exponent is sharp, even for three-atom targets, disproving Letrouit's conjectured square-root bound.

