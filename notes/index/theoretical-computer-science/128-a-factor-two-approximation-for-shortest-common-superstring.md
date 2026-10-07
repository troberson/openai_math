# 128 — A factor-two approximation for shortest common superstring

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/128.md`](../../../lean/docs/128.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | partial, uniform |
| Topics | [algorithms](../topics/algorithms.md) · [computability](../topics/computability.md) · [combinatorial-optimization](../topics/combinatorial-optimization.md) · [coding-theory](../topics/coding-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026`](../../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/) | [paper.pdf](../../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf) | [build/](../../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/) | [README.md](../../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [Superstring](../../../lean/ComparatorChallenges/Superstring.json) | `OAI.Superstring.main` | [Main.lean](../../../lean/OAI/Computability/Superstring/Main.lean) | [`OAI/Computability/Superstring`](../../../lean/OAI/Computability/Superstring/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Superstring` | [.json](../../../lean/ComparatorChallenges/Superstring.json) | [.lean](../../../lean/ComparatorChallenges/Superstring.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Gives a deterministic polynomial-time algorithm constructing a common superstring of length at most twice the optimum for every finite family of explicitly represented strings. The running time is polynomial in the full encoded input length, including symbol labels.

