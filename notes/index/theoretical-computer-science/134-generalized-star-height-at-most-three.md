# 134 — Generalized star height at most three

|  |  |
|---|---|
| Discipline | [Theoretical computer science](../disciplines/theoretical-computer-science.md) |
| Tier | T2 |
| Manuscripts | 3 (0 formalized at source level) |
| Scope note | [`lean/docs/134.md`](../../../lean/docs/134.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 4 out |
| Claim shapes | resolution, bound, partial, uniform |
| Topics | [complexity-theory](../topics/complexity-theory.md) · [formal-languages](../topics/formal-languages.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026`](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/) | [Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf) | [build/](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/) | [README.md](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/README.md) | no | [paper.tex](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/paper.tex) | — |
| [`Generalized-Star-Height-at-Most-Four-September-25-2026`](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/) | [Generalized-Star-Height-at-Most-Four-September-25-2026.pdf](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf) | [build/](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/) | [README.md](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/README.md) | no | [main.tex](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/main.tex) | — |
| [`Generalized-Star-Height-at-Most-Three-September-25-2026`](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/) | [article.pdf](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf) | [build/](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/) | [README.md](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/README.md) | no | [paper.tex](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/paper.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `GeneralizedStarHeight` | [.json](../../../lean/ComparatorChallenges/GeneralizedStarHeight.json) | [.lean](../../../lean/ComparatorChallenges/GeneralizedStarHeight.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Every regular language over a finite alphabet has a generalized regular expression with at most three nested Kleene stars, allowing union, concatenation and complement over the same alphabet. This establishes an absolute bound independent of automaton size, resolving the uniform-boundedness version of the generalized star-height problem.

