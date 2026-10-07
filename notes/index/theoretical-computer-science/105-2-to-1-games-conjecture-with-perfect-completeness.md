# 105 — The 2-to-1 Games Conjecture with perfect completeness

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/105.md`](../../../lean/docs/105.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 1 out |
| Claim shapes | partial, uniform |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Perfect-completeness-for-2-to-1-games-September-23-2026`](../../../preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/) | [paper.pdf](../../../preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/paper.pdf) | [build/](../../../preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/build/) | [README.md](../../../preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Perfect-completeness-for-2-to-1-games-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [PerfectCompleteness](../../../lean/ComparatorChallenges/PerfectCompleteness.json) | `OAI.PerfectCompleteness.Theorem11.exists_reduction` | [Theorem11.lean](../../../lean/OAI/Computability/PerfectCompleteness/Theorem11.lean) | [`OAI/Computability/PerfectCompleteness`](../../../lean/OAI/Computability/PerfectCompleteness/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `PerfectCompleteness` | [.json](../../../lean/ComparatorChallenges/PerfectCompleteness.json) | [.lean](../../../lean/ComparatorChallenges/PerfectCompleteness.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Khot's 2-to-1 Games Conjecture with perfect completeness: for every fixed rational $\delta\in(0,1)$, it is NP-hard to distinguish satisfiable games from games whose optimum is at most $\delta$, on explicit unweighted instances. The alphabet depends only on $\delta$, and every right-hand label has exactly two preimages under each constraint map.

