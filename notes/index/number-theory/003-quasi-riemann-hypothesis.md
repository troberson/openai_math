# 003 — The quasi-Riemann hypothesis

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T3 |
| Manuscripts | 3 (2 formalized at source level) |
| Scope note | [`lean/docs/003.md`](../../../lean/docs/003.md) |
| Comparator configs | 4 (4 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 2 in · 0 out |
| Claim shapes | resolution, uniform |
| Topics | [representation-theory](../topics/representation-theory.md) · [analytic-number-theory](../topics/analytic-number-theory.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-Quasi-Riemann-Hypothesis-October-5-2026`](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/) | [paper2.pdf](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) | [build/](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/) | [README.md](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/README.md) | no | [paper2.tex](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex) | — |
| [`The-Quasi-Riemann-Hypothesis-September-30-2026`](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/) | [paper.pdf](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) | [build/](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/) | [README.md](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/README.md) | yes | [paper.tex](../../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex) | — |
| [`Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026`](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/) | [paper.pdf](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) | [build/](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/) | [README.md](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/README.md) | yes | [paper.tex](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [DirichletSevenEighths](../../../lean/ComparatorChallenges/DirichletSevenEighths.json) | `OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re` | [Nonvanishing.lean](../../../lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean) | [`OAI/NumberTheory/DirichletL`](../../../lean/OAI/NumberTheory/DirichletL/) |
| [HeckeSevenEighths](../../../lean/ComparatorChallenges/HeckeSevenEighths.json) | `OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re` | [Nonvanishing.lean](../../../lean/OAI/NumberTheory/DirichletL/Hecke/Nonvanishing.lean) | [`OAI/NumberTheory/DirichletL/Hecke`](../../../lean/OAI/NumberTheory/DirichletL/Hecke/) |
| [QuasiRiemannHypothesis](../../../lean/ComparatorChallenges/QuasiRiemannHypothesis.json) | `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re` | [Nonvanishing.lean](../../../lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean) | [`OAI/NumberTheory/DirichletL`](../../../lean/OAI/NumberTheory/DirichletL/) |
| [SiegelZeros](../../../lean/ComparatorChallenges/SiegelZeros.json) | `OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap` | [Theorem.lean](../../../lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean) | [`OAI/NumberTheory/SiegelZeros/Conclusions`](../../../lean/OAI/NumberTheory/SiegelZeros/Conclusions/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `DirichletSevenEighths` | [.json](../../../lean/ComparatorChallenges/DirichletSevenEighths.json) | [.lean](../../../lean/ComparatorChallenges/DirichletSevenEighths.lean) | 1 | 0 | no | yes |
| `HeckeSevenEighths` | [.json](../../../lean/ComparatorChallenges/HeckeSevenEighths.json) | [.lean](../../../lean/ComparatorChallenges/HeckeSevenEighths.lean) | 1 | 0 | no | yes |
| `QuasiRiemannHypothesis` | [.json](../../../lean/ComparatorChallenges/QuasiRiemannHypothesis.json) | [.lean](../../../lean/ComparatorChallenges/QuasiRiemannHypothesis.lean) | 1 | 0 | no | yes |
| `SiegelZeros` | [.json](../../../lean/ComparatorChallenges/SiegelZeros.json) | [.lean](../../../lean/ComparatorChallenges/SiegelZeros.lean) | 2 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves that every Dirichlet $L$-function, including $\zeta(s)$, is zero-free in $\Re s>7/8$, resolving the quasi-Riemann hypothesis. The same half-plane is zero-free for every finite-order Hecke $L$-function over $\mathbb Q(\sqrt{-3})$. A companion gives a different proof of the zero-free half-plane $\Re s>11/12$.

