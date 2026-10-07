# 140 — Memory--sample lower bounds for noiseless Gaussian regression

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T3 |
| Manuscripts | 6 (5 formalized at source level) |
| Scope note | [`lean/docs/140.md`](../../../lean/docs/140.md) |
| Comparator configs | 8 (5 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 4 out |
| Claim shapes | partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026`](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/) | [paper.pdf](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/paper.pdf) | [build/](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/build/) | [README.md](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/README.md) | no | [main.tex](../../../preprints/Localization-costs-and-information-growth-for-exact-Gaussian-observations-September-27-2026/build/main.tex) | — |
| [`Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026`](../../../preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/) | [paper.pdf](../../../preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf) | [build/](../../../preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/) | [README.md](../../../preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/README.md) | yes | [main.tex](../../../preprints/Memory-and-precision-in-noiseless-Gaussian-regression-September-27-2026/build/main.tex) | — |
| [`Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026`](../../../preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/) | [paper.pdf](../../../preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/paper.pdf) | [build/](../../../preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/build/) | [README.md](../../../preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/README.md) | yes | [main.tex](../../../preprints/Posterior-replicas-and-conditional-information-in-Gaussian-regression-September-27-2026/build/main.tex) | — |
| [`Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026`](../../../preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/) | [paper.pdf](../../../preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/paper.pdf) | [build/](../../../preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/build/) | [README.md](../../../preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/README.md) | yes | [main.tex](../../../preprints/Projection-moments-positive-cap-domination-and-Riesz-estimates-on-the-sphere-September-27-2026/build/main.tex) | — |
| [`Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026`](../../../preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/) | [paper.pdf](../../../preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/paper.pdf) | [build/](../../../preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/build/) | [README.md](../../../preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/README.md) | yes | [main.tex](../../../preprints/Replacing-Gaussian-observations-in-memory-constrained-inference-September-27-2026/build/main.tex) | — |
| [`Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026`](../../../preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/) | [paper.pdf](../../../preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/paper.pdf) | [build/](../../../preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/build/) | [README.md](../../../preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/README.md) | yes | [main.tex](../../../preprints/Subsphere-methods-for-memory-sample-lower-bounds-in-noiseless-Gaussian-regression-September-27-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [GaussianReplacement](../../../lean/ComparatorChallenges/GaussianReplacement.json) | `OAI.CurrentProjection.fiberBlockMain` | [FiberBlock.lean](../../../lean/OAI/Probability/GaussianReplacement/FiberBlock.lean) | [`OAI/Probability/GaussianReplacement`](../../../lean/OAI/Probability/GaussianReplacement/) |
| [GaussianReplacement](../../../lean/ComparatorChallenges/GaussianReplacement.json) | `OAI.CurrentProjection.hybridBlockMain` | [Hybrid.lean](../../../lean/OAI/Probability/GaussianReplacement/Hybrid.lean) | [`OAI/Probability/GaussianReplacement`](../../../lean/OAI/Probability/GaussianReplacement/) |
| [MemoryPrecision](../../../lean/ComparatorChallenges/MemoryPrecision.json) | `OAI.MemoryPrecision.main` | [Main.lean](../../../lean/OAI/Probability/MemoryPrecision/Main.lean) | [`OAI/Probability/MemoryPrecision`](../../../lean/OAI/Probability/MemoryPrecision/) |
| [PosteriorReplicas](../../../lean/ComparatorChallenges/PosteriorReplicas.json) | `OAI.PosteriorReplicas.source_main` | [Main.lean](../../../lean/OAI/Probability/PosteriorReplicas/Main.lean) | [`OAI/Probability/PosteriorReplicas`](../../../lean/OAI/Probability/PosteriorReplicas/) |
| [ProjectionMoments](../../../lean/ComparatorChallenges/ProjectionMoments.json) | `OAI.ProjectionMoments.main` | [Main.lean](../../../lean/OAI/Probability/ProjectionMoments/Main.lean) | [`OAI/Probability/ProjectionMoments`](../../../lean/OAI/Probability/ProjectionMoments/) |
| [SubsphereCurrent](../../../lean/ComparatorChallenges/SubsphereCurrent.json) | `OAI.SubsphereCurrent.full_current_main_scope` | [Main.lean](../../../lean/OAI/Probability/Subsphere/Main.lean) | [`OAI/Probability/Subsphere`](../../../lean/OAI/Probability/Subsphere/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GaussianFiniteEntropy` | [.json](../../../lean/ComparatorChallenges/GaussianFiniteEntropy.json) | [.lean](../../../lean/ComparatorChallenges/GaussianFiniteEntropy.lean) | 1 | 0 | no | no |
| `GaussianInformation` | [.json](../../../lean/ComparatorChallenges/GaussianInformation.json) | [.lean](../../../lean/ComparatorChallenges/GaussianInformation.lean) | 4 | 0 | no | no |
| `GaussianReplacement` | [.json](../../../lean/ComparatorChallenges/GaussianReplacement.json) | [.lean](../../../lean/ComparatorChallenges/GaussianReplacement.lean) | 11 | 0 | no | yes |
| `MemoryPrecision` | [.json](../../../lean/ComparatorChallenges/MemoryPrecision.json) | [.lean](../../../lean/ComparatorChallenges/MemoryPrecision.lean) | 1 | 0 | no | yes |
| `NoiselessRegression` | [.json](../../../lean/ComparatorChallenges/NoiselessRegression.json) | [.lean](../../../lean/ComparatorChallenges/NoiselessRegression.lean) | 1 | 0 | no | no |
| `PosteriorReplicas` | [.json](../../../lean/ComparatorChallenges/PosteriorReplicas.json) | [.lean](../../../lean/ComparatorChallenges/PosteriorReplicas.lean) | 1 | 0 | no | yes |
| `ProjectionMoments` | [.json](../../../lean/ComparatorChallenges/ProjectionMoments.json) | [.lean](../../../lean/ComparatorChallenges/ProjectionMoments.lean) | 1 | 0 | no | yes |
| `SubsphereCurrent` | [.json](../../../lean/ComparatorChallenges/SubsphereCurrent.json) | [.lean](../../../lean/ComparatorChallenges/SubsphereCurrent.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For fixed $A>0$, a one-pass learner with $Ad^2$ persistent bits needs $\Omega_A(d\log(1/\epsilon))$ noiseless Gaussian samples to recover a unit vector to angular error $0<\epsilon\le1/10$ with probability $2/3$, uniformly in accuracy for large $d$. Computation and randomized updates are unrestricted, but output uses only the terminal state, stopping index and fresh randomness.

