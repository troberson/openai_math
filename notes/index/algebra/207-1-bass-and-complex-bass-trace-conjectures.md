# 207 — The $\ell^1$-Bass and complex Bass trace conjectures

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/207.md`](../../../lean/docs/207.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 1 out |
| Claim shapes | resolution, classification, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026`](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/) | [The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf) | [build/](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/build/) | [README.md](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/README.md) | yes | [main.tex](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/build/main.tex) | — |
| [`The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026`](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/) | [l1-bass-conjecture.pdf](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/l1-bass-conjecture.pdf) | [build/](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/build/) | [README.md](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/README.md) | no | [main.tex](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BassTrace](../../../lean/ComparatorChallenges/BassTrace.json) | `OAI.BassTrace.RightProjective.bassTraceModules_vanishing_and_support` | [Main.lean](../../../lean/OAI/RingTheory/BassTrace/Main.lean) | [`OAI/RingTheory/BassTrace`](../../../lean/OAI/RingTheory/BassTrace/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BassTorsionFree` | [.json](../../../lean/ComparatorChallenges/BassTorsionFree.json) | [.lean](../../../lean/ComparatorChallenges/BassTorsionFree.lean) | 1 | 0 | no | no |
| `BassTrace` | [.json](../../../lean/ComparatorChallenges/BassTrace.json) | [.lean](../../../lean/ComparatorChallenges/BassTrace.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the $\ell^1$-Bass conjecture for every discrete group: Hattori--Stallings traces of idempotent matrices over $\ell^1(G)$ are supported on finitely many finite-order conjugacy classes. The algebraic companion proves the integral Bass trace conjecture and Kaplansky's idempotent conjecture for torsion-free groups over every commutative unital characteristic-zero domain.

