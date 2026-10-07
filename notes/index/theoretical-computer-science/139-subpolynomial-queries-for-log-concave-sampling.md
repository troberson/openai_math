# 139 — Subpolynomial queries for log-concave sampling

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/139.md`](../../../lean/docs/139.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | bound, uniform |
| Topics | [convex-geometry](../topics/convex-geometry.md) · [measure-theory](../topics/measure-theory.md) · [sampling-and-counting](../topics/sampling-and-counting.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026`](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/) | [article.pdf](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf) | [build/](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/) | [README.md](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/README.md) | yes | [main.tex](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [LogConcaveQuery](../../../lean/ComparatorChallenges/LogConcaveQuery.json) | `OAI.LogConcaveSampling.exact_source_main` | [Main.lean](../../../lean/OAI/Probability/LogConcave/Main.lean) | [`OAI/Probability/LogConcave`](../../../lean/OAI/Probability/LogConcave/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `LogConcaveQuery` | [.json](../../../lean/ComparatorChallenges/LogConcaveQuery.json) | [.lean](../../../lean/ComparatorChallenges/LogConcaveQuery.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For $C^2$ potentials with a supplied minimizer and $I\preceq\nabla^2V\preceq2I$, proves that sampling within total variation $1/10$ requires only $C_\varepsilon d^\varepsilon$ exact value-and-gradient queries for every fixed $\varepsilon>0$. The bound holds on every run, with unrestricted computation between queries. A logarithmic lower bound also holds, so the optimal power-law exponent in this oracle model is zero.

