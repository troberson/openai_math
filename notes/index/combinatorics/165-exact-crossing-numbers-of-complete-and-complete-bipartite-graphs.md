# 165 — Exact crossing numbers of complete and complete bipartite graphs

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/165.md`](../../../lean/docs/165.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-crossing-number-of-complete-bipartite-graphs-September-23-2026`](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/) | [paper.pdf](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/paper.pdf) | [build/](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/build/) | [README.md](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/build/paper.tex) | — |
| [`The-crossing-number-of-complete-graphs-September-23-2026`](../../../preprints/The-crossing-number-of-complete-graphs-September-23-2026/) | [paper.pdf](../../../preprints/The-crossing-number-of-complete-graphs-September-23-2026/paper.pdf) | [build/](../../../preprints/The-crossing-number-of-complete-graphs-September-23-2026/build/) | [README.md](../../../preprints/The-crossing-number-of-complete-graphs-September-23-2026/README.md) | yes | [main.tex](../../../preprints/The-crossing-number-of-complete-graphs-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BipartiteCrossing](../../../lean/ComparatorChallenges/BipartiteCrossing.json) | `OAI.Zarankiewicz.mainTarget_proof` | [Main.lean](../../../lean/OAI/Combinatorics/Crossing/Main.lean) | [`OAI/Combinatorics/Crossing`](../../../lean/OAI/Combinatorics/Crossing/) |
| [CompleteCrossing](../../../lean/ComparatorChallenges/CompleteCrossing.json) | `OAI.Paper170.complete_graph_crossing_number` | [Main.lean](../../../lean/OAI/Combinatorics/CompleteCrossing/Main.lean) | [`OAI/Combinatorics/CompleteCrossing`](../../../lean/OAI/Combinatorics/CompleteCrossing/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BipartiteCrossing` | [.json](../../../lean/ComparatorChallenges/BipartiteCrossing.json) | [.lean](../../../lean/ComparatorChallenges/BipartiteCrossing.lean) | 1 | 0 | no | yes |
| `CompleteCrossing` | [.json](../../../lean/ComparatorChallenges/CompleteCrossing.json) | [.lean](../../../lean/ComparatorChallenges/CompleteCrossing.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the Harary--Hill conjecture and Tur\'an's brickyard problem in the Zarankiewicz formulation, determining the crossing numbers of every complete and complete bipartite graph. The result proves the optimality of the classical drawings among all plane drawings with continuous edge arcs.

