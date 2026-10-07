# 290 — Connes' bicentralizer conjecture and relative bicentralizers

|  |  |
|---|---|
| Discipline | [Operator algebras](../disciplines/operator-algebras.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/290.md`](../../../lean/docs/290.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Bounded-recovery-for-modular-spectral-averages-September-23-2026`](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/) | [Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf) | [build/](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/build/) | [README.md](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/build/paper.tex) | — |
| [`Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026`](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/) | [Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf) | [build/](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/build/) | [README.md](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/README.md) | no | [paper.tex](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [BoundedRecovery](../../../lean/ComparatorChallenges/BoundedRecovery.json) | `OAI.BoundedRecovery.bounded_recovery` | [Recovery.lean](../../../lean/OAI/Analysis/ModularRecovery/Recovery.lean) | [`OAI/Analysis/ModularRecovery`](../../../lean/OAI/Analysis/ModularRecovery/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `BoundedRecovery` | [.json](../../../lean/ComparatorChallenges/BoundedRecovery.json) | [.lean](../../../lean/ComparatorChallenges/BoundedRecovery.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Connes' bicentralizer conjecture for every type $\mathrm{III}_1$ factor with separable predual and every faithful normal state. More generally, for every inclusion $N\subset M$ of von Neumann algebras with separable preduals admitting a faithful normal conditional expectation, constructs an amenable expected subalgebra $P\subset N$ with $P'\cap c(M)=N'\cap c(M)$, resolving the relative bicentralizer conjecture.

