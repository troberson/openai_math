# 229 — Sharp three- and four-state reconstruction thresholds

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T2 |
| Manuscripts | 3 (0 formalized at source level) |
| Scope note | [`lean/docs/229.md`](../../../lean/docs/229.md) |
| Comparator configs | 2 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 2 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | — |
| Topics | [statistical-mechanics](../topics/statistical-mechanics.md) · [condensed-matter](../topics/condensed-matter.md) · [potential-theory](../topics/potential-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026`](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/) | [four-state-capacity.pdf](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf) | [build/](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/build/) | [README.md](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/README.md) | no | [main.tex](../../../preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/build/main.tex) | — |
| [`The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026`](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/) | [four-state-potts.pdf](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf) | [build/](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/build/) | [README.md](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/README.md) | no | [main.tex](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/build/main.tex) | [verification/](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/verification/) |
| [`The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026`](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/) | [paper.pdf](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf) | [build/](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/build/) | [README.md](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/README.md) | no | [main.tex](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/build/main.tex) | [verification/](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/verification/) |

## Lean

No `main_results` declaration reaches this family: its scope note links 2 comparator configs, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `ThreeStateSupercritical` | [.json](../../../lean/ComparatorChallenges/ThreeStateSupercritical.json) | [.lean](../../../lean/ComparatorChallenges/ThreeStateSupercritical.lean) | 2 | 0 | no | no |
| `ThreeStateTreeClauses` | [.json](../../../lean/ComparatorChallenges/ThreeStateTreeClauses.json) | [.lean](../../../lean/ComparatorChallenges/ThreeStateTreeClauses.lean) | 2 | 0 | no | no |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026` | [verification/](../../../preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/verification/) | no | no |
| `The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026` | [verification/](../../../preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves the exact reconstruction threshold $d\lambda^2>1$, with nonreconstruction at equality, for three-state symmetric and four-state ferromagnetic broadcasting on regular trees ($d\ge2$) and observed Poisson trees (mean $d>1$ and $d>0$, respectively), with Poisson advantage averaged without conditioning on survival. The three-state theorem allows both signs of $\lambda$ and gives the exact weak-recovery threshold for the symmetric three-community stochastic block model.

