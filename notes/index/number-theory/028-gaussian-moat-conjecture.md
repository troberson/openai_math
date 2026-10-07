# 028 — The Gaussian moat conjecture

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/028.md`](../../../lean/docs/028.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026`](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/) | [paper.pdf](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf) | [build/](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/) | [README.md](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/README.md) | yes | [main.tex](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [GaussianMoat](../../../lean/ComparatorChallenges/GaussianMoat.json) | `OAI.GaussianMoat.fullMain` | [Main.lean](../../../lean/OAI/NumberTheory/GaussianMoat/Main.lean) | [`OAI/NumberTheory/GaussianMoat`](../../../lean/OAI/NumberTheory/GaussianMoat/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GaussianMoat` | [.json](../../../lean/ComparatorChallenges/GaussianMoat.json) | [.lean](../../../lean/ComparatorChallenges/GaussianMoat.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves the Gaussian moat conjecture: no infinite walk through distinct Gaussian primes can have uniformly bounded steps. More strongly, for every distance bound $D$, the graph joining Gaussian primes at distance at most $D$ has uniformly bounded finite component sizes, depending only on $D$, including primes on the coordinate axes.

