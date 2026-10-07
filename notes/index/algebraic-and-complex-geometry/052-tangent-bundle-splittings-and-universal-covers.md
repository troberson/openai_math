# 052 — Tangent-bundle splittings and universal covers

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/052.md`](../../../lean/docs/052.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [manifolds](../topics/manifolds.md) · [complex-geometry](../topics/complex-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026`](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/) | [main.pdf](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/main.pdf) | [build/](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/) | [README.md](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/README.md) | no | [main.tex](../../../preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/main.tex) | — |
| [`Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026`](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/) | [paper.pdf](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf) | [build/](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/) | [README.md](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/README.md) | yes | [main.tex](../../../preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [KahlerSplitting](../../../lean/ComparatorChallenges/KahlerSplitting.json) | `OAI.UniversalCoverSplitting.main` | [Main.lean](../../../lean/OAI/Geometry/KahlerSplitting/Main.lean) | [`OAI/Geometry/KahlerSplitting`](../../../lean/OAI/Geometry/KahlerSplitting/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `KahlerSplitting` | [.json](../../../lean/ComparatorChallenges/KahlerSplitting.json) | [.lean](../../../lean/ComparatorChallenges/KahlerSplitting.lean) | 1 | 0 | no | yes |
| `SplitTangentIntegrability` | [.json](../../../lean/ComparatorChallenges/SplitTangentIntegrability.json) | [.lean](../../../lean/ComparatorChallenges/SplitTangentIntegrability.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

A splitting of the tangent bundle of a compact K\"ahler manifold into two integrable holomorphic subbundles induces a compatible product decomposition of its universal cover, proving the two-summand form of Beauville's splitting conjecture. On smooth rationally connected projective manifolds, both summands are automatically integrable, establishing H\"oring's conjecture and the corresponding product decomposition.

