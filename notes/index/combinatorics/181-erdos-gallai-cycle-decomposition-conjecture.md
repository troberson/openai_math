# 181 — The Erd\H{o}s--Gallai cycle-decomposition conjecture

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/181.md`](../../../lean/docs/181.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, partial |
| Topics | [graph-theory](../topics/graph-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026`](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/) | [main.pdf](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf) | [build/](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/build/) | [README.md](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CycleDecomposition](../../../lean/ComparatorChallenges/CycleDecomposition.json) | `OAI.ErdosGallai.erdos_gallai` | [Main.lean](../../../lean/OAI/Combinatorics/CycleDecomposition/Main.lean) | [`OAI/Combinatorics/CycleDecomposition`](../../../lean/OAI/Combinatorics/CycleDecomposition/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CycleDecomposition` | [.json](../../../lean/ComparatorChallenges/CycleDecomposition.json) | [.lean](../../../lean/ComparatorChallenges/CycleDecomposition.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that the edges of every finite simple undirected graph on $n$ vertices can be partitioned into at most $Cn$ simple cycles and single edges, for an absolute constant $C$. This resolves the Erd\H{o}s--Gallai cycle-decomposition conjecture, bounding the number of pieces linearly even for dense graphs.

