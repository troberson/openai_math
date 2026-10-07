# 189 — Exact cycle--clique Ramsey numbers

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T2 |
| Manuscripts | 1 (0 formalized at source level) |
| Scope note | [`lean/docs/189.md`](../../../lean/docs/189.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Cycle-clique-Ramsey-numbers-September-25-2026`](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/) | [Cycle-clique-Ramsey-numbers-September-25-2026.pdf](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/Cycle-clique-Ramsey-numbers-September-25-2026.pdf) | [build/](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/build/) | [README.md](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/README.md) | no | [main.tex](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/build/main.tex) | [verification/](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/verification/) |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CycleCliqueRamsey` | [.json](../../../lean/ComparatorChallenges/CycleCliqueRamsey.json) | [.lean](../../../lean/ComparatorChallenges/CycleCliqueRamsey.lean) | 1 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Cycle-clique-Ramsey-numbers-September-25-2026` | [verification/](../../../preprints/Cycle-clique-Ramsey-numbers-September-25-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves the Erd\H{o}s--Faudree--Rousseau--Schelp conjecture: $R(C_m,K_n)=(m-1)(n-1)+1$ for every $m\ge n\ge3$, except $R(C_3,K_3)=6$. This is the exact threshold forcing a red $m$-cycle or a blue $n$-clique in every red--blue coloring of a complete graph.

