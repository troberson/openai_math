# 293 — A counterexample to the hyperinvariant-subspace problem

|  |  |
|---|---|
| Discipline | [Operator algebras](../disciplines/operator-algebras.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/293.md`](../../../lean/docs/293.md) |
| Comparator configs | 6 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | — |
| Topics | [operator-algebras](../topics/operator-algebras.md) · [functional-analysis](../topics/functional-analysis.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Backward-intertwiners-and-a-transitive-commutant-September-27-2026`](../../../preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/) | [paper.pdf](../../../preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf) | [build/](../../../preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/) | [README.md](../../../preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/README.md) | yes | [paper.tex](../../../preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/paper.tex) | — |
| [`Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026`](../../../preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/) | [paper.pdf](../../../preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf) | [build/](../../../preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/build/) | [README.md](../../../preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/README.md) | no | [paper.tex](../../../preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BackwardIntertwiners](../../../lean/ComparatorChallenges/BackwardIntertwiners.json) | `OAI.BackwardIntertwiners.direct_algebra_corollary` | [AlgebraCorollary.lean](../../../lean/OAI/Analysis/BackwardIntertwiners/AlgebraCorollary.lean) | [`OAI/Analysis/BackwardIntertwiners`](../../../lean/OAI/Analysis/BackwardIntertwiners/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BackwardIntertwiners` | [.json](../../../lean/ComparatorChallenges/BackwardIntertwiners.json) | [.lean](../../../lean/ComparatorChallenges/BackwardIntertwiners.lean) | 1 | 0 | no | yes |
| `ContinuousCircleWeight` | [.json](../../../lean/ComparatorChallenges/ContinuousCircleWeight.json) | [.lean](../../../lean/ComparatorChallenges/ContinuousCircleWeight.lean) | 1 | 0 | no | no |
| `FiniteFactor` | [.json](../../../lean/ComparatorChallenges/FiniteFactor.json) | [.lean](../../../lean/ComparatorChallenges/FiniteFactor.lean) | 1 | 0 | no | no |
| `HyperinvariantSubspaces` | [.json](../../../lean/ComparatorChallenges/HyperinvariantSubspaces.json) | [.lean](../../../lean/ComparatorChallenges/HyperinvariantSubspaces.lean) | 1 | 0 | no | no |
| `IrrationalRotation` | [.json](../../../lean/ComparatorChallenges/IrrationalRotation.json) | [.lean](../../../lean/ComparatorChallenges/IrrationalRotation.lean) | 2 | 0 | no | no |
| `ProductBrown` | [.json](../../../lean/ComparatorChallenges/ProductBrown.json) | [.lean](../../../lean/ComparatorChallenges/ProductBrown.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a nonzero norm-quasinilpotent operator on every infinite-dimensional separable complex Hilbert space with no nonzero proper closed subspace invariant under every commuting operator. The construction also gives operators with no nontrivial invariant projection in the hyperfinite type $\mathrm{II}_1$ factor.

