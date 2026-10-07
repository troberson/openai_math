# 021 — A quadratic bound for Jacobsthal's function

|  |  |
|---|---|
| Discipline | [Number theory](../disciplines/number-theory.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/021.md`](../../../lean/docs/021.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | resolution, bound, partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-quadratic-bound-for-Jacobsthals-function-September-25-2026`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/) | [paper.pdf](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) | [build/](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/) | [README.md](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/README.md) | yes | [main.tex](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [Jacobsthal](../../../lean/ComparatorChallenges/Jacobsthal.json) | `OAI.Erdos970.Erdos970Final.erdos_970_quadratic` | [QuadraticBound.lean](../../../lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean) | [`OAI/NumberTheory/Jacobsthal/Conclusions`](../../../lean/OAI/NumberTheory/Jacobsthal/Conclusions/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `Jacobsthal` | [.json](../../../lean/ComparatorChallenges/Jacobsthal.json) | [.lean](../../../lean/ComparatorChallenges/Jacobsthal.lean) | 1 | 0 | no | yes |
| `JacobsthalImproved` | [.json](../../../lean/ComparatorChallenges/JacobsthalImproved.json) | [.lean](../../../lean/ComparatorChallenges/JacobsthalImproved.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Answers Jacobsthal's quadratic-bound question: every interval of $Ck^2$ consecutive integers contains an integer coprime to any prescribed positive integer with at most $k$ distinct prime divisors, for an absolute constant $C$. The bound is uniform over prime sets and interval positions and removes the classical logarithmic loss.

