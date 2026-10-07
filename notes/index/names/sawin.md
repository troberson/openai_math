# Name: sawin

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 13 capitalized occurrences, 4 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [003](../number-theory/003-quasi-riemann-hypothesis.md) | The quasi-Riemann hypothesis | — | — | — | — | yes | — |
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | — | — | yes | — | yes | yes |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | The rational Hodge conjecture for CM abelian varieties and products of K3 surfaces | — | — | — | — | yes | — |
| [167](../combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md) | Pinned distances and a power saving for planar unit distances | — | — | — | — | yes | yes |
| [178](../combinatorics/178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md) | Deterministic nonbipartite Ramanujan graphs in every fixed degree | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-power-saving-for-planar-unit-distances-September-23-2026`](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/) | [167](../combinatorics/167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md) | prose | [paper.pdf](../../../preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf) |
| [`Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026`](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | prose | [paper.pdf](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026/paper.pdf) |
| [`Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026`](../../../preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/) | [178](../combinatorics/178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md) | prose | [paper.pdf](../../../preprints/Deterministic-nonbipartite-Ramanujan-graphs-in-every-fixed-degree-September-23-2026/paper.pdf) |
| [`Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [paper.pdf](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf) |
| [`Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026`](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [ramified-ramanujan.pdf](../../../preprints/Temperedness-at-ramified-places-for-globally-generic-exceptional-groups-October-5-2026/ramified-ramanujan.pdf) |
| [`The-Quasi-Riemann-Hypothesis-October-5-2026`](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/) | [003](../number-theory/003-quasi-riemann-hypothesis.md) | prose | [paper2.pdf](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Gan--Harris--Sawin, with Beuzart-Plessis |

## Spelling variants

One surface form in prose: `Sawin`. The normalized key is `sawin`.

