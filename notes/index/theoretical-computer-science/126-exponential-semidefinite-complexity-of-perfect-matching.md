# 126 — Exponential semidefinite complexity of perfect matching

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/126.md`](../../../lean/docs/126.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026`](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/) | [shifted-matching-psd.pdf](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf) | [build/](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/) | [README.md](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/README.md) | no | [main.tex](../../../preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/source/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `MatchingAffineLift` | [.json](../../../lean/ComparatorChallenges/MatchingAffineLift.json) | [.lean](../../../lean/ComparatorChallenges/MatchingAffineLift.lean) | 1 | 0 | no | no |
| `MatchingPSD` | [.json](../../../lean/ComparatorChallenges/MatchingPSD.json) | [.lean](../../../lean/ComparatorChallenges/MatchingPSD.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that every exact semidefinite lift of the perfect matching polytope has exponential size, answering Rothvoss's polynomial-size lift question negatively. The bound holds even for the positive semidefinite rank of its odd-cut slack matrix after any fixed shift $0<\rho<1$, allowing arbitrary real positive semidefinite factors.

