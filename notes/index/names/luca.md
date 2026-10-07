# Name: luca

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 5 capitalized occurrences, 4 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | The Ford--Konyagin--Luca conjecture on prime predecessors | yes | — | — | — | yes | yes |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | The rational Hodge conjecture for CM abelian varieties and products of K3 surfaces | — | — | — | — | yes | — |
| [038](../algebraic-and-complex-geometry/038-fujitas-freeness-conjecture.md) | Fujita's freeness conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026`](../../../preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | prose | [paper.pdf](../../../preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf) |
| [`Fujitas-freeness-conjecture-September-23-2026`](../../../preprints/Fujitas-freeness-conjecture-September-23-2026/) | [038](../algebraic-and-complex-geometry/038-fujitas-freeness-conjecture.md) | prose | [Fujitas-freeness-conjecture-September-23-2026.pdf](../../../preprints/Fujitas-freeness-conjecture-September-23-2026/Fujitas-freeness-conjecture-September-23-2026.pdf) |
| [`The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Luca`. The normalized key is `luca`.

