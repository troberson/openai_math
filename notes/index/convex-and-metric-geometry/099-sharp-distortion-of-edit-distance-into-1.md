# 099 — The sharp distortion of edit distance into $\ell_1$

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T2 |
| Manuscripts | 3 (0 formalized at source level) |
| Scope note | [`lean/docs/099.md`](../../../lean/docs/099.md) |
| Comparator configs | 4 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 0 out |
| Claim shapes | bound, partial, uniform |
| Topics | [algebraic-topology](../topics/algebraic-topology.md) · [metric-geometry](../topics/metric-geometry.md) · [banach-spaces](../topics/banach-spaces.md) · [coding-theory](../topics/coding-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026`](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/) | [paper.pdf](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/paper.pdf) | [build/](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/build/) | [README.md](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/README.md) | no | [main.tex](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/build/main.tex) | — |
| [`Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026`](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/) | [paper.pdf](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/paper.pdf) | [build/](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/build/) | [README.md](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/README.md) | no | [main.tex](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/build/main.tex) | — |
| [`Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026`](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/) | [paper.pdf](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/paper.pdf) | [build/](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/build/) | [README.md](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/README.md) | no | [main.tex](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 4 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BinaryEditLower` | [.json](../../../lean/ComparatorChallenges/BinaryEditLower.json) | [.lean](../../../lean/ComparatorChallenges/BinaryEditLower.lean) | 1 | 0 | no | no |
| `EditDistance` | [.json](../../../lean/ComparatorChallenges/EditDistance.json) | [.lean](../../../lean/ComparatorChallenges/EditDistance.lean) | 1 | 0 | no | no |
| `FiniteCircle` | [.json](../../../lean/ComparatorChallenges/FiniteCircle.json) | [.lean](../../../lean/ComparatorChallenges/FiniteCircle.lean) | 1 | 0 | no | no |
| `TreeEdit` | [.json](../../../lean/ComparatorChallenges/TreeEdit.json) | [.lean](../../../lean/ComparatorChallenges/TreeEdit.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines the least distortion of embedding edit distance on words of length at most $d$ into real $\ell_1$: it is $\exp(\Theta(\sqrt{\log d\,\log\log d}))$. Insertions, deletions and substitutions have unit cost. The constants are uniform over all finite alphabets with at least two symbols, even when the alphabet grows with $d$; binary words already force the lower bound.

