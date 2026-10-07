# 106 — Hardness of coloring three-colorable graphs

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/106.md`](../../../lean/docs/106.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026`](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/) | [Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026.pdf) | [build/](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/) | [README.md](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [IndependentSets](../../../lean/ComparatorChallenges/IndependentSets.json) | `OAI.LargeIndependentSets.mainTheoremReal` | [Main.lean](../../../lean/OAI/Combinatorics/IndependentSets/Main.lean) | [`OAI/Combinatorics/IndependentSets`](../../../lean/OAI/Combinatorics/IndependentSets/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `IndependentSets` | [.json](../../../lean/ComparatorChallenges/IndependentSets.json) | [.lean](../../../lean/ComparatorChallenges/IndependentSets.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

It is NP-hard to color a three-colorable graph using any fixed number $c\ge3$ of colors. More strongly, for every fixed $0<\delta<1/3$, a deterministic polynomial-time reduction from $3$SAT produces simple unweighted graphs that are three-colorable in the satisfiable case and have no independent set of size $\delta n$ otherwise, where $n$ is the number of vertices.

