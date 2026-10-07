# 033 — Campana's orbifold Iitaka conjecture and logarithmic subadditivity

|  |  |
|---|---|
| Discipline | [Algebraic and complex geometry](../disciplines/algebraic-and-complex-geometry.md) |
| Tier | T2 |
| Manuscripts | 5 (0 formalized at source level) |
| Scope note | [`lean/docs/033.md`](../../../lean/docs/033.md) |
| Comparator configs | 1 (0 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 12 in · 9 out |
| Claim shapes | bound |
| Topics | [algebraic-geometry](../topics/algebraic-geometry.md) · [manifolds](../topics/manifolds.md) · [operator-algebras](../topics/operator-algebras.md) · [complex-geometry](../topics/complex-geometry.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026`](../../../preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/) | [paper.pdf](../../../preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf) | [build/](../../../preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/build/) | [README.md](../../../preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/README.md) | no | [paper.tex](../../../preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/build/paper.tex) | — |
| [`Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026`](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/) | [paper.pdf](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf) | [build/](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/build/) | [README.md](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/README.md) | no | [main.tex](../../../preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/build/main.tex) | — |
| [`Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026`](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/) | [paper.pdf](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf) | [build/](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/build/) | [README.md](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/README.md) | no | [main.tex](../../../preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/build/main.tex) | — |
| [`Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026`](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/) | [paper.pdf](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf) | [build/](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/build/) | [README.md](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/README.md) | no | [main.tex](../../../preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/build/main.tex) | — |
| [`The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026`](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/) | [paper.pdf](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf) | [build/](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/build/) | [README.md](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/README.md) | no | [main.tex](../../../preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/build/main.tex) | — |

## Lean

No `main_results` declaration reaches this family: its scope note links 1 comparator config, none of them in `main_results`.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `LogKodairaFiberNegative` | [.json](../../../lean/ComparatorChallenges/LogKodairaFiberNegative.json) | [.lean](../../../lean/ComparatorChallenges/LogKodairaFiberNegative.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Proves Campana's orbifold Iitaka subadditivity conjecture for smooth Fujiki-class-$\mathcal C$ manifolds with rational simple-normal-crossing boundaries. For projective fibrations $f:U\to V$ of smooth complex quasi-projective varieties with connected fibers, general fiber $F$, and $\bar\kappa(V)\ge0$, proves Popa's inequality $\bar\kappa(U)\ge\kappa(F)+\max\{\bar\kappa(V),\operatorname{Var}(f)\}$, where variation measures the whole geometric generic fiber.

