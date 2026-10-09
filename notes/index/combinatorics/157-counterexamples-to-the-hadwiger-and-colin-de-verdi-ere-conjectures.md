# 157 — Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures

|  |  |
|---|---|
| Discipline | [Combinatorics](../disciplines/combinatorics.md) |
| Tier | T3 |
| Manuscripts | 3 (1 formalized at source level) |
| Scope note | [`lean/docs/157.md`](../../../lean/docs/157.md) |
| Comparator configs | 2 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 0 |
| Cited by / cites | 4 in · 4 out |
| Claim shapes | counterexample, bound, partial |
| Topics | [graph-theory](../topics/graph-theory.md) · [graph-coloring](../topics/graph-coloring.md) |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`A-counterexample-to-Hadwigers-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/README.md) | yes | [main.tex](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/main.tex) | — |
| [`A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/) | [paper.pdf](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/paper.pdf) | [build/](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/build/) | [README.md](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/build/main.tex) | — |
| [`A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/) | [paper.pdf](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) | [build/](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/build/) | [README.md](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/README.md) | no | [main.tex](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/build/main.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [HadwigerCounterexample](../../../lean/ComparatorChallenges/HadwigerCounterexample.json) | `OAI.HadwigerCounterexample.not_hadwiger_conjecture` | [Main.lean](../../../lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean) | [`OAI/Combinatorics/HadwigerCounterexample`](../../../lean/OAI/Combinatorics/HadwigerCounterexample/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `HadwigerCounterexample` | [.json](../../../lean/ComparatorChallenges/HadwigerCounterexample.json) | [.lean](../../../lean/ComparatorChallenges/HadwigerCounterexample.lean) | 2 | 0 | no | yes |
| `ListHadwiger` | [.json](../../../lean/ComparatorChallenges/ListHadwiger.json) | [.lean](../../../lean/ComparatorChallenges/ListHadwiger.lean) | 1 | 0 | no | no |

## Verification bundles

No `verification/` bundle ships with this family's manuscripts.

## Abstract (`overview.tex`, verbatim)

Disproves Hadwiger's conjecture even for fractional coloring: arbitrarily large finite simple graphs with independence number at most two satisfy $\chi_f(G)>h(G)$, where $h(G)$ is the largest clique-minor order. Also disproves the fractional Colin de Verdi\`ere chromatic bound $\chi_f(G)\le\mu(G)+1$. In the positive direction, every finite nonempty graph satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$ for a universal constant $C$.

