# 325 — The complete Crouzeix conjecture

|  |  |
|---|---|
| Discipline | [Functional analysis](../disciplines/functional-analysis.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/325.md`](../../../lean/docs/325.md) |
| Comparator configs | 5 (3 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, uniform |
| Topics | [functional-analysis](../topics/functional-analysis.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026`](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/) | [paper.pdf](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf) | [build/](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/) | [README.md](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/README.md) | yes | [main.tex](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/build/main.tex) | — |
| [`The-complete-Crouzeix-theorem-September-23-2026`](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/) | [paper.pdf](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/paper.pdf) | [build/](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/build/) | [README.md](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CompleteCrouzeix](../../../lean/ComparatorChallenges/CompleteCrouzeix.json) | `OAI.CompleteCrouzeix.main` | [Main.lean](../../../lean/OAI/Analysis/NumericalRange/Main.lean) | [`OAI/Analysis/NumericalRange`](../../../lean/OAI/Analysis/NumericalRange/) |
| [DirectCrouzeix](../../../lean/ComparatorChallenges/DirectCrouzeix.json) | `OAI.DirectCrouzeix.complete_crouzeix` | [CompleteBound.lean](../../../lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean) | [`OAI/Analysis/DirectCrouzeix`](../../../lean/OAI/Analysis/DirectCrouzeix/) |
| [StructuralCrouzeix](../../../lean/ComparatorChallenges/StructuralCrouzeix.json) | `OAI.StructuralCrouzeixReference.challenge` | [Endpoint.lean](../../../lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean) | [`OAI/Analysis/StructuralCrouzeix`](../../../lean/OAI/Analysis/StructuralCrouzeix/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CompleteCrouzeix` | [.json](../../../lean/ComparatorChallenges/CompleteCrouzeix.json) | [.lean](../../../lean/ComparatorChallenges/CompleteCrouzeix.lean) | 1 | 0 | no | yes |
| `CrouzeixHilbert` | [.json](../../../lean/ComparatorChallenges/CrouzeixHilbert.json) | [.lean](../../../lean/ComparatorChallenges/CrouzeixHilbert.lean) | 1 | 0 | no | no |
| `DirectCrouzeix` | [.json](../../../lean/ComparatorChallenges/DirectCrouzeix.json) | [.lean](../../../lean/ComparatorChallenges/DirectCrouzeix.lean) | 2 | 0 | no | yes |
| `HilbertCrouzeix` | [.json](../../../lean/ComparatorChallenges/HilbertCrouzeix.json) | [.lean](../../../lean/ComparatorChallenges/HilbertCrouzeix.lean) | 4 | 0 | no | no |
| `StructuralCrouzeix` | [.json](../../../lean/ComparatorChallenges/StructuralCrouzeix.json) | [.lean](../../../lean/ComparatorChallenges/StructuralCrouzeix.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the complete Crouzeix conjecture: for every bounded operator $A$ on a complex Hilbert space and every finite matrix-valued polynomial $P$, one has $\lVert P[A]\rVert\le2\sup_{z\in W(A)}\lVert P(z)\rVert$, where $W(A)$ is the numerical range. The constant $2$ is sharp, independent of the matrix size, and valid in infinite dimensions.

