# 174 — Deterministic construction of strong thin spanning trees

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/174.md`](../../../lean/docs/174.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | resolution, partial |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-polynomial-time-construction-of-strong-thin-trees-September-23-2026`](../../../preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/) | [paper.pdf](../../../preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/paper.pdf) | [build/](../../../preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/build/) | [README.md](../../../preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-polynomial-time-construction-of-strong-thin-trees-September-23-2026/build/source/main.tex) | — |
| [`The-strong-thin-tree-conjecture-September-23-2026`](../../../preprints/The-strong-thin-tree-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/The-strong-thin-tree-conjecture-September-23-2026/build/) | [README.md](../../../preprints/The-strong-thin-tree-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-strong-thin-tree-conjecture-September-23-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [StrongThinTree](../../../lean/ComparatorChallenges/StrongThinTree.json) | `OAI.StrongThinTree.strongThinTree` | [Main.lean](../../../lean/OAI/Combinatorics/ThinTrees/Main.lean) | [`OAI/Combinatorics/ThinTrees`](../../../lean/OAI/Combinatorics/ThinTrees/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `AlgorithmicThinTrees` | [.json](../../../lean/ComparatorChallenges/AlgorithmicThinTrees.json) | [.lean](../../../lean/ComparatorChallenges/AlgorithmicThinTrees.lean) | 1 | 0 | no | no |
| `StrongThinTree` | [.json](../../../lean/ComparatorChallenges/StrongThinTree.json) | [.lean](../../../lean/ComparatorChallenges/StrongThinTree.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the strong thin-tree conjecture constructively. Every finite loopless $k$-edge-connected multigraph on at least two vertices has a spanning tree containing at most a universal $C/k$ fraction of the edges of every cut. Such a tree can be found deterministically in polynomial time, even with binary-encoded parallel-edge multiplicities.

