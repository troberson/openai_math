# 210 — Foulkes’ conjecture for sixth powers and quadratic stabilization

|  |  |
|---|---|
| Discipline | [Algebra](../disciplines/algebra.md) |
| Tier | T3 |
| Manuscripts | 2 (1 formalized at source level) |
| Scope note | [`lean/docs/210.md`](../../../lean/docs/210.md) |
| Comparator configs | 1 (1 with a `main_results` declaration) |
| Reasoning trace | — |
| Verification bundles | 1 |
| Cited by / cites | 1 in · 1 out |
| Claim shapes | resolution, uniform |
| Companion families | — |
| Summary page | — |

## Manuscripts

| Dir | PDF | LaTeX tree | README | Formalized | Main file | Verification |
|---|---|---|---|---|---|---|
| [`Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026`](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/) | [main.pdf](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf) | [build/](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/build/) | [README.md](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/README.md) | no | [main.tex](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/build/main.tex) | [verification/](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/verification/) |
| [`Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026`](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/) | [paper.pdf](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/paper.pdf) | [build/](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/build/) | [README.md](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/README.md) | yes | [paper.tex](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/build/paper.tex) | — |

## Lean

| Config | Declaration | File | Module dir |
|---|---|---|---|
| [FoulkesHowe](../../../lean/ComparatorChallenges/FoulkesHowe.json) | `OAI.Problem346.canonical_foulkes_howe_surjective` | [Stabilization.lean](../../../lean/OAI/RepresentationTheory/FoulkesHowe/Stabilization.lean) | [`OAI/RepresentationTheory/FoulkesHowe`](../../../lean/OAI/RepresentationTheory/FoulkesHowe/) |

The release ships no manuscript→Lean edge (`notes/index-design.md`): `sources:` and `main_results:` are two flat lists that nothing joins, so the table above is a family-level link and the formalized count above is a manuscript-level flag.

## Comparator configs

| Config | Statement | Solution | Theorems | Definitions | nanoda | In `main_results` |
|---|---|---|---|---|---|---|
| `FoulkesHowe` | [.json](../../../lean/ComparatorChallenges/FoulkesHowe.json) | [.lean](../../../lean/ComparatorChallenges/FoulkesHowe.lean) | 1 | 0 | no | yes |

## Verification bundles

| Dir | Bundle | INPUTS.md | COVERAGE.md |
|---|---|---|---|
| `Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026` | [verification/](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/verification/) | no | no |

## Abstract (`overview.tex`, verbatim)

Proves the sixth case of Foulkes’ conjecture: $\operatorname{Sym}^6(\operatorname{Sym}^bV)$ embeds equivariantly in $\operatorname{Sym}^b(\operatorname{Sym}^6V)$ for every $b\ge6$ and finite-dimensional complex $V$. More generally, the canonical multiplication map $\operatorname{Sym}^b(\operatorname{Sym}^aV)\to\operatorname{Sym}^a(\operatorname{Sym}^bV)$ is surjective for $a\ge2$ and $b\ge a(a-1)$, giving dimension-independent quadratic stabilization.

