# 098 — A negative answer to the Lang--Plaut problem

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/098.md`](../../../lean/docs/098.md) |
| Comparator configs | 2 (2 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Topics | [metric-geometry](../topics/metric-geometry.md) · [convex-geometry](../topics/convex-geometry.md) · [functional-analysis](../topics/functional-analysis.md) · [banach-spaces](../topics/banach-spaces.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026`](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/) | [main.pdf](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf) | [build/](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/build/) | [README.md](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/README.md) | yes | [main.tex](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [CompactBanach](../../../lean/ComparatorChallenges/CompactBanach.json) | `OAI.CompactBanach.main` | [CompactBanach.lean](../../../lean/OAI/Geometry/DoublingHilbert/CompactBanach.lean) | [`OAI/Geometry/DoublingHilbert`](../../../lean/OAI/Geometry/DoublingHilbert/) |
| [DoublingHilbert](../../../lean/ComparatorChallenges/DoublingHilbert.json) | `OAI.DoublingHilbert.main` | [Main.lean](../../../lean/OAI/Geometry/DoublingHilbert/Main.lean) | [`OAI/Geometry/DoublingHilbert`](../../../lean/OAI/Geometry/DoublingHilbert/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `CompactBanach` | [.json](../../../lean/ComparatorChallenges/CompactBanach.json) | [.lean](../../../lean/ComparatorChallenges/CompactBanach.lean) | 1 | 0 | no | yes |
| `DoublingHilbert` | [.json](../../../lean/ComparatorChallenges/DoublingHilbert.json) | [.lean](../../../lean/ComparatorChallenges/DoublingHilbert.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Every infinite-dimensional real Banach space contains a compact doubling set that admits no bi-Lipschitz embedding into any finite-dimensional normed space. The doubling constant is universal. This answers the Lang--Plaut problem negatively, even for compact subsets of Hilbert space.

