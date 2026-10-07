# 156 — Borsuk's conjecture fails in dimension nine

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/156.md`](../../../lean/docs/156.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | — |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026`](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/) | [paper.pdf](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf) | [build/](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/build/) | [README.md](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BorsukNine](../../../lean/ComparatorChallenges/BorsukNine.json) | `OAI.BorsukNine.main_theorem` | [Counterexample.lean](../../../lean/OAI/Geometry/Borsuk/Counterexample.lean) | [`OAI/Geometry/Borsuk`](../../../lean/OAI/Geometry/Borsuk/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BorsukNine` | [.json](../../../lean/ComparatorChallenges/BorsukNine.json) | [.lean](../../../lean/ComparatorChallenges/BorsukNine.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Constructs a compact subset of $\mathbb R^9$ that cannot be covered by ten sets of strictly smaller diameter, disproving Borsuk's covering assertion already in dimension nine. The example consists of rank-one orthogonal projectors onto lines in $\mathbb R^4$, with the Frobenius metric.

