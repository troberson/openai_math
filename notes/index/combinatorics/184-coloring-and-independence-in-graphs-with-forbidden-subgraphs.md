# 184 — Coloring and independence in graphs with forbidden subgraphs

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/184.md`](../../../lean/docs/184.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 2 out |
| Claim shapes | resolution, partial |
| Topics | [graph-theory](../topics/graph-theory.md) · [graph-coloring](../topics/graph-coloring.md) · [extremal-combinatorics](../topics/extremal-combinatorics.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026`](../../../preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/) | [paper.pdf](../../../preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/paper.pdf) | [build/](../../../preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/build/) | [README.md](../../../preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/README.md) | yes | [main.tex](../../../preprints/A-Logarithmic-Independence-Bound-for-Clique-Free-Graphs-September-25-2026/build/main.tex) | — |
| [`Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026`](../../../preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/) | [correspondence-coloring-forbidden-clique.pdf](../../../preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf) | [build/](../../../preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/build/) | [README.md](../../../preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/README.md) | no | [main.tex](../../../preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CliqueFreeLog](../../../lean/ComparatorChallenges/CliqueFreeLog.json) | `OAI.CliqueFreeLog.logarithmic_independence_bound` | [Main.lean](../../../lean/OAI/Combinatorics/CliqueFree/Main.lean) | [`OAI/Combinatorics/CliqueFree`](../../../lean/OAI/Combinatorics/CliqueFree/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CliqueFreeLog` | [.json](../../../lean/ComparatorChallenges/CliqueFreeLog.json) | [.lean](../../../lean/ComparatorChallenges/CliqueFreeLog.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the Alon--Krivelevich--Sudakov coloring conjecture in correspondence-coloring form: graphs avoiding any fixed subgraph $F$ need $O_F(\Delta/\log\Delta)$ colors when their maximum degree $\Delta$ is sufficiently large. Also proves the Ajtai--Erd\H{o}s--Koml\'os--Szemer\'edi independence conjecture: for fixed $r\ge4$, every $n$-vertex $K_r$-free graph of average degree $d\ge2$ has an independent set of size $\Omega_r(n\log d/d)$.

