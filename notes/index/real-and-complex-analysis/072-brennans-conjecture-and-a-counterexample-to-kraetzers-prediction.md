# 072 — Brennan's conjecture and a counterexample to Kraetzer's prediction

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 2 (2 formalized at source level) |
| Scope note | [`lean/docs/072.md`](../../../lean/docs/072.md) |
| Comparator configs | 3 (3 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | counterexample, bound, uniform |
| Topics | [complex-analysis](../topics/complex-analysis.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/) | [paper.pdf](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf) | [build/](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/) | [README.md](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/README.md) | yes | [main.tex](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/main.tex) | — |
| [`Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/) | [paper.pdf](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf) | [build/](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/) | [README.md](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/README.md) | yes | [main.tex](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [Brennan](../../../lean/ComparatorChallenges/Brennan.json) | `OAI.Brennan.main_theorem` | [Main.lean](../../../lean/OAI/Analysis/IntegralMeans/Main.lean) | [`OAI/Analysis/IntegralMeans`](../../../lean/OAI/Analysis/IntegralMeans/) |
| [BrennanSharp](../../../lean/ComparatorChallenges/BrennanSharp.json) | `OAI.Brennan.Sharp.sharp_endpoints` | [SharpEndpoints.lean](../../../lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean) | [`OAI/Analysis/IntegralMeans`](../../../lean/OAI/Analysis/IntegralMeans/) |
| [StrictMeans](../../../lean/ComparatorChallenges/StrictMeans.json) | `OAI.StrictInverseFirstPower.main` | [Main.lean](../../../lean/OAI/Analysis/StrictMeans/Main.lean) | [`OAI/Analysis/StrictMeans`](../../../lean/OAI/Analysis/StrictMeans/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Brennan` | [.json](../../../lean/ComparatorChallenges/Brennan.json) | [.lean](../../../lean/ComparatorChallenges/Brennan.lean) | 1 | 0 | no | yes |
| `BrennanSharp` | [.json](../../../lean/ComparatorChallenges/BrennanSharp.json) | [.lean](../../../lean/ComparatorChallenges/BrennanSharp.lean) | 1 | 0 | no | yes |
| `StrictMeans` | [.json](../../../lean/ComparatorChallenges/StrictMeans.json) | [.lean](../../../lean/ComparatorChallenges/StrictMeans.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Brennan's conjecture: for every conformal bijection $\phi$ from a simply connected plane domain onto the disk, $|\phi'|^s$ is area-integrable for $4/3<s<4$. The sharp universal integral-means identity is $B_{\mathcal S}(t)=|t|-1$ for $t\le-2$. A strict bound $B_b(-1)<1/4$ for bounded univalent functions disproves Kraetzer's prediction at that parameter.

