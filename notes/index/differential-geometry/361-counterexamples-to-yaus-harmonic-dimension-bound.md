# 361 — Counterexamples to Yau's harmonic dimension bound

|  |  |
|---|---|
| Discipline | [Differential geometry](../disciplines/differential-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/361.md`](../../../lean/docs/361.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | counterexample, bound, partial, uniform |
| Topics | [manifolds](../topics/manifolds.md) · [riemannian-geometry](../topics/riemannian-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026`](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/) | [paper.pdf](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/paper.pdf) | [build/](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/build/) | [README.md](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/README.md) | no | [paper.tex](../../../preprints/A-Three-Dimensional-Counterexample-to-Integer-Degree-Harmonic-Dimension-Comparison-September-26-2026/build/paper.tex) | — |
| [`A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026`](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/) | [paper.pdf](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/paper.pdf) | [build/](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/build/) | [README.md](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/build/paper.tex) | [verification/](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/verification/) |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [HarmonicGrowth](../../../lean/ComparatorChallenges/HarmonicGrowth.json) | `OAI.HarmonicCounterexample.main` | [Main.lean](../../../lean/OAI/Geometry/HarmonicGrowth/Main.lean) | [`OAI/Geometry/HarmonicGrowth`](../../../lean/OAI/Geometry/HarmonicGrowth/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HarmonicGrowth` | [.json](../../../lean/ComparatorChallenges/HarmonicGrowth.json) | [.lean](../../../lean/ComparatorChallenges/HarmonicGrowth.lean) | 1 | 0 | no | yes |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026` | [verification/](../../../preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Disproves Yau's proposed Euclidean dimension bound for harmonic functions of integer growth on manifolds with nonnegative Ricci curvature. For every sufficiently large integer $k$, a complete smooth metric on $\mathbb R^3$ has at least $(k+2)^2$ independent harmonic functions of growth at most $k$, exceeding the Euclidean count $(k+1)^2$. The metric may depend on $k$.

