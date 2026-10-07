# 179 — The circulant Hadamard conjecture

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/179.md`](../../../lean/docs/179.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, partial |
| Topics | [enumerative-combinatorics](../topics/enumerative-combinatorics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-circulant-Hadamard-conjecture-September-23-2026`](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/build/) | [README.md](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CirculantHadamard](../../../lean/ComparatorChallenges/CirculantHadamard.json) | `OAI.CirculantHadamard.exists_iff_order_one_or_four` | [Main.lean](../../../lean/OAI/LinearAlgebra/CirculantHadamard/Main.lean) | [`OAI/LinearAlgebra/CirculantHadamard`](../../../lean/OAI/LinearAlgebra/CirculantHadamard/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CirculantHadamard` | [.json](../../../lean/ComparatorChallenges/CirculantHadamard.json) | [.lean](../../../lean/ComparatorChallenges/CirculantHadamard.lean) | 1 | 0 | no | yes |
| `EvenBarker` | [.json](../../../lean/ComparatorChallenges/EvenBarker.json) | [.lean](../../../lean/ComparatorChallenges/EvenBarker.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that real circulant Hadamard matrices exist exactly in orders $1$ and $4$, resolving the circulant Hadamard conjecture. Together with classical Barker-sequence results, this shows that binary sequences whose nontrivial aperiodic autocorrelations have magnitude at most $1$ exist at lengths $n>1$ exactly when $n\in\{2,3,4,5,7,11,13\}$.

