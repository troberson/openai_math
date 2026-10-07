# 236 — The factor-of-IID threshold for free Ising states on trees

|  |  |
|---|---|
| Discipline | [Probability and statistical mechanics](../disciplines/probability-and-statistical-mechanics.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/236.md`](../../../lean/docs/236.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution |
| Topics | [statistical-mechanics](../topics/statistical-mechanics.md) · [condensed-matter](../topics/condensed-matter.md) · [probability](../topics/probability.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026`](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/) | [article.pdf](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/article.pdf) | [build/](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/) | [README.md](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/README.md) | yes | [main.tex](../../../preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [FreeIsing](../../../lean/ComparatorChallenges/FreeIsing.json) | `OAI.Problem367.free_ising_factor_iff_threshold` | [Main.lean](../../../lean/OAI/Probability/FreeIsing/Main.lean) | [`OAI/Probability/FreeIsing`](../../../lean/OAI/Probability/FreeIsing/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FreeIsing` | [.json](../../../lean/ComparatorChallenges/FreeIsing.json) | [.lean](../../../lean/ComparatorChallenges/FreeIsing.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Determines when the free zero-field ferromagnetic Ising state on the infinite $d$-regular tree is a factor of independent vertex labels: exactly when $\tanh\beta\le(d-1)^{-1/2}$, including equality, for $d\ge3$ and $\beta\ge0$. The construction uses no root and is almost surely equivariant for each fixed tree automorphism, resolving the ferromagnetic case of Lyons's question.

