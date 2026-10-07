# 020 — Squarefree quartics and power-free polynomial values

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/020.md`](../../../lean/docs/020.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, density |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026`](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/) | [manuscript.pdf](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf) | [build/](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/) | [README.md](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PowerFreeValues](../../../lean/ComparatorChallenges/PowerFreeValues.json) | `OAI.QuarticPowerFree.allDegrees` | [Main.lean](../../../lean/OAI/NumberTheory/PowerFree/Main.lean) | [`OAI/NumberTheory/PowerFree`](../../../lean/OAI/NumberTheory/PowerFree/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PowerFreeValues` | [.json](../../../lean/ComparatorChallenges/PowerFreeValues.json) | [.lean](../../../lean/ComparatorChallenges/PowerFreeValues.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the squarefree-values conjecture for irreducible integer quartics with no fixed prime-square divisor: squarefree values on positive integers have the predicted positive Euler-product density. More generally, establishes the $(d-2)$-power-free density for irreducible integer polynomials of degrees four through eight under the necessary local condition; together with Browning's higher-degree theorem, this covers every $d\ge4$.

