# 108 — A cubic permanent--determinant lower bound

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/108.md`](../../../lean/docs/108.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026`](../../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/) | [A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf](../../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026.pdf) | [build/](../../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/) | [README.md](../../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/README.md) | no | [main.tex](../../../preprints/A-cubic-lower-bound-for-border-determinantal-complexity-of-the-permanent-September-24-2026/build/source/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PermanentCubic` | [.json](../../../lean/ComparatorChallenges/PermanentCubic.json) | [.lean](../../../lean/ComparatorChallenges/PermanentCubic.lean) | 1 | 0 | no | no |
| `SmoothInitialForm` | [.json](../../../lean/ComparatorChallenges/SmoothInitialForm.json) | [.lean](../../../lean/ComparatorChallenges/SmoothInitialForm.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves an $\Omega(n^3)$ lower bound for the border determinantal complexity of the $n\times n$ permanent over $\mathbb C$. Even coefficientwise limits of determinants of affine-linear matrices require matrix size at least $cn^3$, for an absolute $c>0$ and all sufficiently large $n$; the same bound therefore holds for exact representations.

