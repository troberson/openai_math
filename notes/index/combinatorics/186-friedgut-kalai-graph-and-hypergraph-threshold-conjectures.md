# 186 — The Friedgut--Kalai graph and hypergraph threshold conjectures

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | [`lean/docs/186.md`](../../../lean/docs/186.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, partial, uniform |
| Topics | [graph-theory](../topics/graph-theory.md) · [probabilistic-combinatorics](../topics/probabilistic-combinatorics.md) · [random-graphs](../topics/random-graphs.md) · [hypergraphs](../topics/hypergraphs.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026`](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/) | [paper.pdf](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/paper.pdf) | [build/](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/build/) | [README.md](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/README.md) | no | [main.tex](../../../preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/build/main.tex) | — |
| [`A-uniform-influence-bound-for-hypergraph-properties-October-5-2026`](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/) | [hypergraph-influences.pdf](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/hypergraph-influences.pdf) | [build/](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/build/) | [README.md](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/README.md) | no | [main.tex](../../../preprints/A-uniform-influence-bound-for-hypergraph-properties-October-5-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SharpThreshold` | [.json](../../../lean/ComparatorChallenges/SharpThreshold.json) | [.lean](../../../lean/ComparatorChallenges/SharpThreshold.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the Friedgut--Kalai threshold-width conjectures for graphs and fixed-uniformity hypergraphs. For fixed $0<\varepsilon<1/2$, every nontrivial increasing relabeling-invariant property crosses from probability $\varepsilon$ to $1-\varepsilon$ within width $O((\log n)^{-2})$ for graphs and $O_r((\log n)^{-r/(r-1)})$ for $r$-uniform hypergraphs, $r\ge3$. The hypergraph influence bound also applies to nonmonotone properties.

