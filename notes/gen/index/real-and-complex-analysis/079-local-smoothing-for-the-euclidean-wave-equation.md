# 079 — Local smoothing for the Euclidean wave equation

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/079.md`](../../../../lean/docs/079.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 4 out |
| Claim shapes | bound |
| Topics | [harmonic-analysis](../topics/harmonic-analysis.md) · [partial-differential-equations](../topics/partial-differential-equations.md) · [quantum-theory](../topics/quantum-theory.md) · [fractal-geometry](../topics/fractal-geometry.md) |
| Companion families | — |
| Summary page | [079-local-smoothing-for-the-euclidean-wave-equation.md](../../../../notes/gen/summaries/079-local-smoothing-for-the-euclidean-wave-equation.md) |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026`](../../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/) | [paper.pdf](../../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf) | [build/](../../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/) | [README.md](../../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/README.md) | no | [main.tex](../../../../preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/build/main.tex) | — |
| [`Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026`](../../../../preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/) | [paper.pdf](../../../../preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf) | [build/](../../../../preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/build/) | [README.md](../../../../preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/README.md) | yes | [paper.tex](../../../../preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [LocalSmoothing](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | `OAI.Analysis.Fourier.LocalSmoothing.Comparator.bochner_riesz` | [Comparator.lean](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean) | [`OAI/Analysis/Fourier/LocalSmoothing`](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/) |
| [LocalSmoothing](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | `OAI.Analysis.Fourier.LocalSmoothing.Comparator.euclidean_local_smoothing` | [Comparator.lean](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean) | [`OAI/Analysis/Fourier/LocalSmoothing`](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/) |
| [LocalSmoothing](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | `OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya` | [Comparator.lean](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean) | [`OAI/Analysis/Fourier/LocalSmoothing`](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/) |
| [LocalSmoothing](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | `OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya_maximal` | [Comparator.lean](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean) | [`OAI/Analysis/Fourier/LocalSmoothing`](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/) |
| [LocalSmoothing](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | `OAI.Analysis.Fourier.LocalSmoothing.Comparator.spherical_restriction` | [Comparator.lean](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean) | [`OAI/Analysis/Fourier/LocalSmoothing`](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/) |
| [LocalSmoothing](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | `OAI.Analysis.Fourier.LocalSmoothing.Comparator.stein_square` | [Comparator.lean](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean) | [`OAI/Analysis/Fourier/LocalSmoothing`](../../../../lean/OAI/Analysis/Fourier/LocalSmoothing/) |

The release ships no manuscript→Lean edge (`notes/development/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `LocalSmoothing` | [.json](../../../../lean/ComparatorChallenges/LocalSmoothing.json) | [.lean](../../../../lean/ComparatorChallenges/LocalSmoothing.lean) | 6 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Sogge's local smoothing conjecture in every spatial dimension $n\ge2$, with arbitrarily small loss above the sharp Sobolev threshold. The wave estimate yields the Bochner--Riesz conjecture and, for $2\le p<\infty$, maximal bounds for these means and sharp bounds for Stein's square function. It also gives Fourier restriction throughout the interior of the conjectured range for the sphere, compact paraboloid, and truncated cone, and local smoothing for the Schrödinger equation. The Kakeya and Nikodym maximal conjectures follow. In particular, every Euclidean Kakeya set has full Hausdorff dimension.

