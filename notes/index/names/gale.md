# Name: gale

3 families · subject name · 1 carried by a title or a declaration · 2 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 37 capitalized occurrences, 29 of them mid-sentence, 10 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md) | The rational Hodge conjecture for CM abelian varieties | — | yes | yes | — | yes | — |
| [120](../theoretical-computer-science/120-almost-linear-time-exact-matching-in-general-graphs.md) | Almost-linear-time exact matching in general graphs | — | — | — | — | yes | yes |
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026`](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md) | prose + title | [paper.pdf](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf) |
| [`Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026`](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026/) | — | prose | — |
| [`Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026`](../../../preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/) | [120](../theoretical-computer-science/120-almost-linear-time-exact-matching-in-general-graphs.md) | prose | [main.pdf](../../../preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md) | Perfect Gale tensor |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md) | Gale cohomology supply |
| — | Perfect Gale tensor |
| — | Gale cohomology supply |

## Spelling variants

One surface form in prose: `Gale`. The normalized key is `gale`.

