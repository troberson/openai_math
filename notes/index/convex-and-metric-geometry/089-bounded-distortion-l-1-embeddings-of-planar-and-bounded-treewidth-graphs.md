# 089 — Bounded-distortion $L_1$ embeddings of planar and bounded-treewidth graphs

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/089.md`](../../../lean/docs/089.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026`](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/) | [paper.pdf](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf) | [build/](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/) | [README.md](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/README.md) | yes | [main.tex](../../../preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/build/main.tex) | — |
| [`Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026`](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/) | [paper.pdf](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf) | [build/](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/) | [README.md](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BoundedTreewidthL1](../../../lean/ComparatorChallenges/BoundedTreewidthL1.json) | `OAI.BoundedTreewidthL1.main_theorem` | [Main.lean](../../../lean/OAI/Combinatorics/TreewidthL1/Main.lean) | [`OAI/Combinatorics/TreewidthL1`](../../../lean/OAI/Combinatorics/TreewidthL1/) |
| [PlanarL1](../../../lean/ComparatorChallenges/PlanarL1.json) | `OAI.PlanarL1.planar_graph_metrics_embed_L1` | [Embedding.lean](../../../lean/OAI/Combinatorics/PlanarL1/Embedding.lean) | [`OAI/Combinatorics/PlanarL1`](../../../lean/OAI/Combinatorics/PlanarL1/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BoundedTreewidthL1` | [.json](../../../lean/ComparatorChallenges/BoundedTreewidthL1.json) | [.lean](../../../lean/ComparatorChallenges/BoundedTreewidthL1.lean) | 1 | 0 | no | yes |
| `PlanarL1` | [.json](../../../lean/ComparatorChallenges/PlanarL1.json) | [.lean](../../../lean/ComparatorChallenges/PlanarL1.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the planar and bounded-treewidth cases of the Gupta--Newman--Rabinovich--Sinclair conjecture. Shortest-path metrics of finite connected graphs with arbitrary positive edge lengths embed into real $L_1$ with universal distortion for planar graphs, and distortion depending only on treewidth for bounded-treewidth graphs. The corresponding multicommodity flow--cut gaps are uniformly bounded.

