# 183 — Power savings for planar halving lines and $k$-sets

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/183.md`](../../../lean/docs/183.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound |
| Topics | [discrete-geometry](../topics/discrete-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-power-saving-for-planar-halving-lines-September-25-2026`](../../../preprints/A-power-saving-for-planar-halving-lines-September-25-2026/) | [main.pdf](../../../preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf) | [build/](../../../preprints/A-power-saving-for-planar-halving-lines-September-25-2026/build/) | [README.md](../../../preprints/A-power-saving-for-planar-halving-lines-September-25-2026/README.md) | no | [main.tex](../../../preprints/A-power-saving-for-planar-halving-lines-September-25-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HalvingLines` | [.json](../../../lean/ComparatorChallenges/HalvingLines.json) | [.lean](../../../lean/ComparatorChallenges/HalvingLines.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Improves the planar halving-line bound to $O(n^{4/3-\varepsilon})$ for sets with no three collinear and an absolute $\varepsilon>0$. More generally, an $n$-point set with no three collinear has $O(n(k+1)^{1/3-\varepsilon_0})$ strictly separable $k$-subsets for $1\le k\le n/2$, with an absolute $\varepsilon_0>0$. The constants and positive exponents are nonquantitative.

