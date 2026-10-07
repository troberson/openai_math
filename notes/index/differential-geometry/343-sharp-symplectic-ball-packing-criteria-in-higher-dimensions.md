# 343 — Sharp symplectic ball-packing criteria in higher dimensions

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/343.md`](../../../lean/docs/343.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026`](../../../preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/) | [paper.pdf](../../../preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/paper.pdf) | [build/](../../../preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/build/) | [README.md](../../../preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/README.md) | no | [main.tex](../../../preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BallPacking` | [.json](../../../lean/ComparatorChallenges/BallPacking.json) | [.lean](../../../lean/ComparatorChallenges/BallPacking.lean) | 1 | 0 | no | no |
| `BallPackingNecessity` | [.json](../../../lean/ComparatorChallenges/BallPackingNecessity.json) | [.lean](../../../lean/ComparatorChallenges/BallPackingNecessity.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the Siegel--Yao conjecture for arbitrary capacities in every dimension $2n\ge6$. Finitely many closed symplectic balls of capacities $R_1,\ldots,R_k$ embed disjointly into an open ball of capacity $R$ exactly when $\sum_iR_i^n<R^n$ and $R_i+R_j<R$ for every distinct pair $i,j$.

