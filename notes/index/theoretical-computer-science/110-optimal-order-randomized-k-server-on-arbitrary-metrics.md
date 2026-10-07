# 110 — Optimal-order randomized $k$-server on arbitrary metrics

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | [`lean/docs/110.md`](../../../lean/docs/110.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026`](../../../preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/) | [Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf](../../../preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026.pdf) | [build/](../../../preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/build/) | [README.md](../../../preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/README.md) | no | [common.tex](../../../preprints/Squared-logarithmic-randomized-k-server-on-arbitrary-metrics-September-24-2026/build/source/latex/common.tex) | — |
| [`Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026`](../../../preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/) | [Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf](../../../preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026.pdf) | [build/](../../../preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/build/) | [README.md](../../../preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/README.md) | no | [main.tex](../../../preprints/Uniform-computation-of-the-squared-logarithmic-k-server-bound-September-24-2026/build/source/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `KServer` | [.json](../../../lean/ComparatorChallenges/KServer.json) | [.lean](../../../lean/ComparatorChallenges/KServer.lean) | 1 | 9 | no | no |
| `UniformKServer` | [.json](../../../lean/ComparatorChallenges/UniformKServer.json) | [.lean](../../../lean/ComparatorChallenges/UniformKServer.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Establishes a randomized competitive ratio $O(\log^2(k+1))$ for $k$-server on every metric space, matching the worst-case lower-bound order. One policy serves every finite oblivious request sequence, including on infinite unbounded metrics. On finite rational metrics, a uniform implementation has polynomial preprocessing and per-request bit cost in the input length and $\log(t+1)$ at request $t$, with a finite instance-dependent additive movement constant.

