# 058 — The Koll\'ar--Pardon universal-cover conjecture

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/058.md`](../../../lean/docs/058.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 2 out |
| Claim shapes | resolution, bound |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026`](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/) | [paper.pdf](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/paper.pdf) | [build/](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/build/) | [README.md](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/README.md) | no | [main.tex](../../../preprints/Semialgebraic-universal-covers-of-normal-projective-varieties-September-24-2026/build/main.tex) | — |
| [`Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026`](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/) | [paper.pdf](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/paper.pdf) | [build/](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/) | [README.md](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/README.md) | yes | [paper.tex](../../../preprints/Symmetry-of-semialgebraic-bounded-domains-with-compact-quotient-September-24-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SymmetricDomains](../../../lean/ComparatorChallenges/SymmetricDomains.json) | `OAI.Release061.main` | [Main.lean](../../../lean/OAI/Analysis/SymmetricDomains/Main.lean) | [`OAI/Analysis/SymmetricDomains`](../../../lean/OAI/Analysis/SymmetricDomains/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SymmetricDomains` | [.json](../../../lean/ComparatorChallenges/SymmetricDomains.json) | [.lean](../../../lean/ComparatorChallenges/SymmetricDomains.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the Koll\'ar--Pardon conjecture: the semialgebraic universal covers of connected normal projective complex varieties are exactly products $D\times\mathbb C^m\times F$, with $D$ bounded symmetric and $F$ simply connected, normal, and projective. A universal cover is quasi-projective exactly when the bounded symmetric factor is absent. In particular, a smooth projective variety covered by $\mathbb C^n$ has a finite \textnormal{étale} cover by an abelian variety.

