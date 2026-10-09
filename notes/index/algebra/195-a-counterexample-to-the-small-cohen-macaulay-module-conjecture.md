# 195 — A counterexample to the small Cohen--Macaulay module conjecture

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/195.md`](../../../lean/docs/195.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [surfaces](../topics/surfaces.md) · [commutative-algebra](../topics/commutative-algebra.md) · [noncommutative-algebra](../topics/noncommutative-algebra.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026`](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/) | [paper.pdf](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/paper.pdf) | [build/](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/) | [README.md](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SurfaceConeCandidateSupport](../../../lean/ComparatorChallenges/SurfaceConeCandidateSupport.json) | `OAI.SmallCM.candidate_ring_properties` | [CandidateRing.lean](../../../lean/OAI/AlgebraicGeometry/SurfaceCones/CandidateRing.lean) | [`OAI/AlgebraicGeometry/SurfaceCones`](../../../lean/OAI/AlgebraicGeometry/SurfaceCones/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SurfaceConeCandidateSupport` | [.json](../../../lean/ComparatorChallenges/SurfaceConeCandidateSupport.json) | [.lean](../../../lean/ComparatorChallenges/SurfaceConeCandidateSupport.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a three-dimensional complete Noetherian normal local domain over $\mathbb C$ with no nonzero finitely generated maximal Cohen--Macaulay module. A three-dimensional local domain essentially of finite type over $\mathbb C$ has the same property, disproving the domain form of the small Cohen--Macaulay module conjecture.

