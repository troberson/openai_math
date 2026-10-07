# 092 — The optimal order of convex-body covering density

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/092.md`](../../../lean/docs/092.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | density, partial |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026`](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/) | [paper.pdf](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/paper.pdf) | [build/](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/build/) | [README.md](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/build/main.tex) | — |
| [`Translative-covering-densities-of-order-n-log-n-September-23-2026`](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/) | [paper.pdf](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/paper.pdf) | [build/](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/) | [README.md](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SingleLatticeCovering](../../../lean/ComparatorChallenges/SingleLatticeCovering.json) | `OAI.SingleLatticeCovering.single_lattice_covering` | [Main.lean](../../../lean/OAI/Geometry/LatticeCovering/Main.lean) | [`OAI/Geometry/LatticeCovering`](../../../lean/OAI/Geometry/LatticeCovering/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CoveringDensity` | [.json](../../../lean/ComparatorChallenges/CoveringDensity.json) | [.lean](../../../lean/ComparatorChallenges/CoveringDensity.lean) | 1 | 0 | no | no |
| `SingleLatticeCovering` | [.json](../../../lean/ComparatorChallenges/SingleLatticeCovering.json) | [.lean](../../../lean/ComparatorChallenges/SingleLatticeCovering.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines the optimal worst-case covering density as $\Theta(n\log n)$, for both lattice and unrestricted translative coverings. Every convex body in $\mathbb R^n$, $n\ge2$, admits a lattice covering of density at most $Cn\log n$; centrally symmetric examples in every sufficiently large dimension require at least $cn\log n$ even without the lattice restriction, for absolute $c,C>0$.

