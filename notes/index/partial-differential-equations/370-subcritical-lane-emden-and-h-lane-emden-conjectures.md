# 370 — The subcritical Lane--Emden and H\'enon--Lane--Emden conjectures

|  |  |
|---|---|
| Discipline | [Partial differential equations](../disciplines/partial-differential-equations.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/370.md`](../../../lean/docs/370.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026`](../../../preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/) | [paper.pdf](../../../preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf) | [build/](../../../preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/build/) | [README.md](../../../preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/README.md) | yes | [main.tex](../../../preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [HenonEmden](../../../lean/ComparatorChallenges/HenonEmden.json) | `OAI.HenonLaneEmden.main_nonexistence` | [Main.lean](../../../lean/OAI/Analysis/HenonEmden/Main.lean) | [`OAI/Analysis/HenonEmden`](../../../lean/OAI/Analysis/HenonEmden/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HenonEmden` | [.json](../../../lean/ComparatorChallenges/HenonEmden.json) | [.lean](../../../lean/ComparatorChallenges/HenonEmden.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the subcritical Lane--Emden conjecture and its weighted H\'enon extension. For $n\ge2$, $p,q>0$ and real $A,B$, the system $-\Delta u=|x|^A v^p$, $-\Delta v=|x|^B u^q$ has no positive entire solution when $(n+A)/(p+1)+(n+B)/(q+1)>n-2$, with solutions continuous at the origin and classical elsewhere. No symmetry or growth assumption is needed. Known radial existence gives the exact existence criterion for $n\ge3$ and $A,B>-2$.

