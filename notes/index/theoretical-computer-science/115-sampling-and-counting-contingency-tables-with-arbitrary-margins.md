# 115 — Sampling and counting contingency tables with arbitrary margins

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 2 (0 formalized at source level) |
| Scope note | [`lean/docs/115.md`](../../../lean/docs/115.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | bound, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026`](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/) | [main.pdf](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf) | [build/](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/build/) | [README.md](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/README.md) | no | [main.tex](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/build/main.tex) | — |
| [`Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026`](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/) | [main.pdf](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/main.pdf) | [build/](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/build/) | [README.md](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/README.md) | no | [main.tex](../../../preprints/Exact-Uniform-Sampling-of-Contingency-Tables-with-Arbitrary-Margins-September-24-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ContingencyTables` | [.json](../../../lean/ComparatorChallenges/ContingencyTables.json) | [.lean](../../../lean/ComparatorChallenges/ContingencyTables.lean) | 3 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For nonnegative integer matrices with prescribed row and column sums, gives exact uniform sampling in expected polynomial bit time and almost-uniform sampling in worst-case polynomial bit time. The dimensions and binary-encoded margins are unrestricted. Also gives a fully polynomial randomized approximation scheme for counting such tables with arbitrary individual cell bounds, including structural zeros, with polynomial cost on every execution.

