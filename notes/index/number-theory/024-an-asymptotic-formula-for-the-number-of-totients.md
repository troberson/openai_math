# 024 — An asymptotic formula for the number of totients

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/024.md`](../../../lean/docs/024.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 1 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-asymptotic-formula-for-the-number-of-totients-September-25-2026`](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/) | [An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf) | [build/](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/) | [README.md](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/README.md) | no | [main.tex](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/build/source/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TotientAsymptotic` | [.json](../../../lean/ComparatorChallenges/TotientAsymptotic.json) | [.lean](../../../lean/ComparatorChallenges/TotientAsymptotic.lean) | 4 | 0 | no | no |
| `TotientCompanionZero` | [.json](../../../lean/ComparatorChallenges/TotientCompanionZero.json) | [.lean](../../../lean/ComparatorChallenges/TotientCompanionZero.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives an asymptotic equivalent for the number $V(x)$ of distinct totient values up to $x$, with a positive bounded phase-dependent factor determined by convergent arithmetic approximations. In particular, $V(cx)/V(x)\to c$ for every fixed $c>0$, answering Erd\H{o}s and Hall’s scaling question.

