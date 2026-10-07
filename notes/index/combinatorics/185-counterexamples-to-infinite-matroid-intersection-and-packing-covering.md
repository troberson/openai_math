# 185 — Counterexamples to infinite matroid intersection and packing/covering

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/185.md`](../../../lean/docs/185.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026`](../../../preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/) | [paper.pdf](../../../preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf) | [build/](../../../preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/build/) | [README.md](../../../preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [InfiniteMatroid](../../../lean/ComparatorChallenges/InfiniteMatroid.json) | `OAI.InfiniteMatroidCounterexample.main` | [Main.lean](../../../lean/OAI/Combinatorics/InfiniteMatroid/Main.lean) | [`OAI/Combinatorics/InfiniteMatroid`](../../../lean/OAI/Combinatorics/InfiniteMatroid/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `InfiniteMatroid` | [.json](../../../lean/ComparatorChallenges/InfiniteMatroid.json) | [.lean](../../../lean/ComparatorChallenges/InfiniteMatroid.lean) | 1 | 0 | no | yes |
| `InfiniteMatroidCorollaries` | [.json](../../../lean/ComparatorChallenges/InfiniteMatroidCorollaries.json) | [.lean](../../../lean/ComparatorChallenges/InfiniteMatroidCorollaries.lean) | 2 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves the unrestricted infinite matroid intersection and packing/covering conjectures in ZFC, using two self-dual partitional matroids on a countably infinite ground set. The same examples answer Jo\'o’s partitional-matroid question negatively. They are neither finitary nor cofinitary, so Nash-Williams’ original finitary conjecture remains outside the result.

