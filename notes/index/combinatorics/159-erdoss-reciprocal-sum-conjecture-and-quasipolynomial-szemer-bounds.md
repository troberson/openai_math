# 159 — Erd\H{o}s's reciprocal-sum conjecture and quasipolynomial Szemer\'edi bounds

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/159.md`](../../../lean/docs/159.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | [quasipolynomial-arithmetic-progressions](../../../reasoning_traces/quasipolynomial-arithmetic-progressions.pdf) |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | partial |
| Companion families | — |
| Summary page | [159-quasipolynomial-bounds-for-arithmetic-progressions.md](../../../notes/summaries/combinatorics/159-quasipolynomial-bounds-for-arithmetic-progressions.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026`](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/) | [paper.pdf](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf) | [build/](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/) | [README.md](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/README.md) | no | [main.tex](../../../preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ErdosReciprocal` | [.json](../../../lean/ComparatorChallenges/ErdosReciprocal.json) | [.lean](../../../lean/ComparatorChallenges/ErdosReciprocal.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Erd\H{o}s's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. Quantitatively, for each fixed $k\ge3$, every subset of $\{1,\ldots,N\}$ with no nonconstant $k$-term progression has size at most $C_kN\exp[-c_k(\log N)^{\varepsilon_k}]$, with positive constants depending only on $k$.

