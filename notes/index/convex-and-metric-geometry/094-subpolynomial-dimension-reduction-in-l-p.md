# 094 — Subpolynomial dimension reduction in $L_p$

|  |  |
|---|---|
| Discipline | [Convex and metric geometry](../disciplines/convex-and-metric-geometry.md) |
| Tier | T3 |
| Manuscripts | 1 (1 formalized at source level) |
| Scope note | [`lean/docs/094.md`](../../../lean/docs/094.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 0 in · 0 out |
| Claim shapes | partial, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Subpolynomial-dimension-reduction-in-Lp-September-23-2026`](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/) | [paper.pdf](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf) | [build/](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/build/) | [README.md](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/README.md) | yes | [paper.tex](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [SubpolynomialLp](../../../lean/ComparatorChallenges/SubpolynomialLp.json) | `OAI.SubpolynomialLp.source_main` | [Main.lean](../../../lean/OAI/Analysis/LpDimension/Main.lean) | [`OAI/Analysis/LpDimension`](../../../lean/OAI/Analysis/LpDimension/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `SubpolynomialLp` | [.json](../../../lean/ComparatorChallenges/SubpolynomialLp.json) | [.lean](../../../lean/ComparatorChallenges/SubpolynomialLp.lean) | 1 | 0 | no | yes |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

For every fixed $1<p<\infty$ and distortion $D>1$, every $n$-point subset of real $L_p$ embeds into $\ell_p^d$ with distortion at most $D$ and dimension $d=n^{o(1)}$, answering Naor's sublinear-dimension question for $p\ne2$. In contrast, exact embeddings require worst-case dimension $\Theta(n^2)$ when $p\ne2$.

