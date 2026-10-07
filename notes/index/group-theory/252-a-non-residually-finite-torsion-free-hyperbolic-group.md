# 252 — A non-residually-finite torsion-free hyperbolic group

|  |  |
|---|---|
| Discipline | [Group theory](../disciplines/group-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/252.md`](../../../lean/docs/252.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [group-theory](../topics/group-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026`](../../../preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/) | [paper.pdf](../../../preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/paper.pdf) | [build/](../../../preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/build/) | [README.md](../../../preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [TorsionFreeHyperbolic](../../../lean/ComparatorChallenges/TorsionFreeHyperbolic.json) | `OAI.Release075.main` | [Main.lean](../../../lean/OAI/GroupTheory/Hyperbolic/Main.lean) | [`OAI/GroupTheory/Hyperbolic`](../../../lean/OAI/GroupTheory/Hyperbolic/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TorsionFreeHyperbolic` | [.json](../../../lean/ComparatorChallenges/TorsionFreeHyperbolic.json) | [.lean](../../../lean/ComparatorChallenges/TorsionFreeHyperbolic.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a torsion-free word-hyperbolic group that is not residually finite, answering the residual-finiteness question negatively. One fixed nonidentity element is killed by every finite-dimensional linear representation over every commutative field, so the group is not linear over any such field.

