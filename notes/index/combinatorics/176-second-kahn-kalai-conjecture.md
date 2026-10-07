# 176 — The second Kahn--Kalai conjecture

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/176.md`](../../../lean/docs/176.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, density, partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-second-Kahn-Kalai-conjecture-September-24-2026`](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/) | [paper.pdf](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf) | [build/](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/build/) | [README.md](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/README.md) | yes | [main.tex](../../../preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/build/source/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SecondKahnKalai](../../../lean/ComparatorChallenges/SecondKahnKalai.json) | `OAI.LeanBlast.SecondKahnKalai.secondKahnKalaiBounds` | [Main.lean](../../../lean/OAI/Combinatorics/GraphThreshold/Main.lean) | [`OAI/Combinatorics/GraphThreshold`](../../../lean/OAI/Combinatorics/GraphThreshold/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SecondKahnKalai` | [.json](../../../lean/ComparatorChallenges/SecondKahnKalai.json) | [.lean](../../../lean/ComparatorChallenges/SecondKahnKalai.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the second Kahn--Kalai conjecture: for every finite simple graph $H$ with $h\ge1$ edges and at most $n$ vertices, its appearance threshold in $G(n,p)$ is at most $C p_{\mathrm E}(n,H)(1+\log_2 h)$, with universal $C$. Here $p_{\mathrm E}$ is the least density at which every subgraph of $H$ has expected copy count at least $1/2$.

