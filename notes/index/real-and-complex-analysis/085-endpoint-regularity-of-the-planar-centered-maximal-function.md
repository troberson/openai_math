# 085 — Endpoint regularity of the planar centered maximal function

|  |  |
|---|---|
| Discipline | [Real and complex analysis](../disciplines/real-and-complex-analysis.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/085.md`](../../../lean/docs/085.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026`](../../../preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/) | [article.pdf](../../../preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/article.pdf) | [build/](../../../preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/build/) | [README.md](../../../preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/README.md) | yes | [main.tex](../../../preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SignedFiniteBand](../../../lean/ComparatorChallenges/SignedFiniteBand.json) | `OAI.SignedDisk.CenteredDiskEndpoint.main_signed_finite_band` | [Main.lean](../../../lean/OAI/Analysis/SignedDisk/Main.lean) | [`OAI/Analysis/SignedDisk`](../../../lean/OAI/Analysis/SignedDisk/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DiskMaximal` | [.json](../../../lean/ComparatorChallenges/DiskMaximal.json) | [.lean](../../../lean/ComparatorChallenges/DiskMaximal.lean) | 1 | 0 | no | no |
| `SignedFiniteBand` | [.json](../../../lean/ComparatorChallenges/SignedFiniteBand.json) | [.lean](../../../lean/ComparatorChallenges/SignedFiniteBand.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Resolves the planar centered-disk case of the Haj{\l}asz--Onninen maximal-function regularity problem. For every real $f\in W^{1,1}(\mathbb R^2)$, the centered disk maximal function satisfies $\|\nabla Mf\|_1\le C\|\nabla f\|_1$ with an absolute constant. It belongs locally to $W^{1,1}$ and has a globally integrable weak gradient.

