# 378 — Disproof of the Exponential Time Hypothesis

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/378.md`](../../../../lean/docs/378.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, uniform |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [algorithms](../topics/algorithms.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Exponential-Time-Hypothesis-is-False-October-25-2026`](../../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/) | [paper.pdf](../../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) | [build/](../../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/) | [README.md](../../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/README.md) | yes | [main_full_version.tex](../../../../preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SubexponentialSAT](../../../../lean/ComparatorChallenges/SubexponentialSAT.json) | `OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat` | [Final.lean](../../../../lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean) | [`OAI/Algorithms/SubexponentialSAT/SqrtLogSpace`](../../../../lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/) |

The release ships no manuscript→Lean edge (`notes/development/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SubexponentialSAT` | [.json](../../../../lean/ComparatorChallenges/SubexponentialSAT.json) | [.lean](../../../../lean/ComparatorChallenges/SubexponentialSAT.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For every fixed $k\ge2$, a deterministic algorithm counts the satisfying assignments of a $k$-CNF with $n$ variables and $m$ clauses in time $(n+m)^{O_k(1)}2^{n/(\log n)^{1/2+o(1)}}$. This yields superlinear circuit lower bounds for a language in $\mathsf{E}^{\mathsf{NP}}$ on infinitely many input lengths.

