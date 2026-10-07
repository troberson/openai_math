# 242 — Single-fold Diophantine representations

|  |  |
|---|---|
| Discipline | [Mathematical logic](../disciplines/mathematical-logic.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/242.md`](../../../lean/docs/242.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, undecidability |
| Topics | [computability](../topics/computability.md) · [diophantine-equations](../topics/diophantine-equations.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Single-fold-Diophantine-representations-September-24-2026`](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/) | [paper.pdf](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/paper.pdf) | [build/](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/build/) | [README.md](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SingleFold](../../../lean/ComparatorChallenges/SingleFold.json) | `OAI.SingleFold.main` | [Main.lean](../../../lean/OAI/NumberTheory/SingleFold/Main.lean) | [`OAI/NumberTheory/SingleFold`](../../../lean/OAI/NumberTheory/SingleFold/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SingleFold` | [.json](../../../lean/ComparatorChallenges/SingleFold.json) | [.lean](../../../lean/ComparatorChallenges/SingleFold.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Every recursively enumerable set of tuples of natural numbers has a Diophantine representation with exactly one auxiliary solution for each member and none for nonmembers. This proves the single-fold conjecture and hence the finite-fold conjecture. Diophantine solvability over the nonnegative integers remains undecidable even with an at-most-one-solution promise.

