# 182 — Power savings for polynomial-difference-free sets

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 3 (0 formalized at source level) |
| Scope note | [`lean/docs/182.md`](../../../lean/docs/182.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 3 in · 4 out |
| Claim shapes | uniform |
| Topics | [additive-combinatorics](../topics/additive-combinatorics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026`](../../../preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/) | [prime-argument-polynomial-differences.pdf](../../../preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf) | [build/](../../../preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/) | [README.md](../../../preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/README.md) | no | [main.tex](../../../preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/main.tex) | — |
| [`A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026`](../../../preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/) | [power-saving-intersective-polynomial-differences.pdf](../../../preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf) | [build/](../../../preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/) | [README.md](../../../preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/README.md) | no | [main.tex](../../../preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/manuscript/main.tex) | — |
| [`A-power-saving-for-square-difference-free-sets-September-24-2026`](../../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/) | [paper.pdf](../../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf) | [build/](../../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/build/) | [README.md](../../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/README.md) | no | [main.tex](../../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SquareDifference` | [.json](../../../lean/ComparatorChallenges/SquareDifference.json) | [.lean](../../../lean/ComparatorChallenges/SquareDifference.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For every fixed intersective integer polynomial $h$ of degree $k\ge2$ with positive leading coefficient, proves that a subset of $\{1,\ldots,N\}$ avoiding nonzero values $h(1),h(2),\ldots$ as differences has size $O_h(N^{1-c_k})$, with $c_k>0$ depending only on degree. Here intersective means having a root modulo every modulus. For prime arguments, a power saving also holds when $h$ has a unit root modulo every modulus, with exponent allowed to depend on $h$.

