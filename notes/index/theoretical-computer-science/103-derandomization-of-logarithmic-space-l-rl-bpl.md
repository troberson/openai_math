# 103 — Derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/103.md`](../../../lean/docs/103.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [computability](../topics/computability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026`](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/) | [paper.pdf](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/paper.pdf) | [build/](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/) | [README.md](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Exact-Derandomization-of-Logarithmic-Space-L-equals-RL-equals-BPL-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [LogspaceEquality](../../../lean/ComparatorChallenges/LogspaceEquality.json) | `OAI.ExactDerandomization.exact_logarithmic_space_derandomization` | [Equality.lean](../../../lean/OAI/Computability/Logspace/Equality.lean) | [`OAI/Computability/Logspace`](../../../lean/OAI/Computability/Logspace/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `LogspaceEquality` | [.json](../../../lean/ComparatorChallenges/LogspaceEquality.json) | [.lean](../../../lean/ComparatorChallenges/LogspaceEquality.lean) | 1 | 20 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves $\mathsf L=\mathsf{RL}=\mathsf{BPL}$, resolving derandomization for bounded-error logarithmic-space computation. An effective compiler converts each randomized polynomial-time logarithmic-space machine deciding a language with one-sided or two-sided error into a deterministic logarithmic-space decider with explicit polynomial running-time bounds.

