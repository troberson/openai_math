# 122 — Superpolynomial lower bounds and quasipolynomial reconstruction from deletion traces

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 3 (0 formalized at source level) |
| Scope note | [`lean/docs/122.md`](../../../lean/docs/122.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | bound, partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026`](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/) | [paper.pdf](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/paper.pdf) | [build/](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/build/) | [README.md](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/README.md) | no | [main.tex](../../../preprints/A-latest-anchor-induction-with-spectrally-compact-masks-for-worst-case-trace-reconstruction-October-5-2026/build/main.tex) | — |
| [`Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026`](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/) | [uniform-trace-reconstruction.pdf](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/uniform-trace-reconstruction.pdf) | [build/](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/build/) | [README.md](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/README.md) | no | [main.tex](../../../preprints/Uniform-quasipolynomial-time-trace-reconstruction-October-5-2026/build/manuscript/main.tex) | — |
| [`quantitative-lower-bounds-for-trace-reconstruction-September-24-2026`](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/) | [paper.pdf](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf) | [build/](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/) | [README.md](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/README.md) | no | [main.tex](../../../preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `TraceReconstruction` | [.json](../../../lean/ComparatorChallenges/TraceReconstruction.json) | [.lean](../../../lean/ComparatorChallenges/TraceReconstruction.lean) | 3 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

At every fixed deletion probability in $(0,1)$, reconstructing an arbitrary length-$n$ binary string requires $n^{\Omega(\log\log n)}$ independent traces, ruling out polynomial-sample reconstruction. A uniform decoder achieves quasipolynomial sample and running-time bounds for known fixed rational retention probabilities. When the deletion probability is at most $n^{-\varepsilon}$ for fixed $\varepsilon>0$, both bounds become polynomial in the input and parameter encoding.

