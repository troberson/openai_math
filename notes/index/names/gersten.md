# Name: gersten

4 families · subject name · 2 carried by a title or a declaration · 4 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 21 capitalized occurrences, 12 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 2 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [209](../algebra/209-integral-counterexamples-to-gerstens-conjecture.md) | Integral counterexamples to Gersten’s conjecture | yes | yes | — | — | yes | yes |
| [254](../group-theory/254-classifying-spaces-and-geometric-obstructions-for-artin-groups.md) | Classifying spaces and geometric obstructions for Artin groups | — | — | — | — | yes | — |
| [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | Gersten's conjecture for one-relator groups | yes | — | — | — | yes | yes |
| [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | Counterexamples to Baum--Connes and Kadison--Kaplansky | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf) |
| [`An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026`](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/) | [254](../group-theory/254-classifying-spaces-and-geometric-obstructions-for-artin-groups.md) | prose | [paper.pdf](../../../preprints/An-Artin-group-with-no-geometric-CAT-0-action-September-23-2026/paper.pdf) |
| [`An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026`](../../../preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/) | [209](../algebra/209-integral-counterexamples-to-gerstens-conjecture.md) | prose | [An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026.pdf](../../../preprints/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026/An-Integral-Counterexample-to-Gerstens-Conjecture-September-25-2026.pdf) |
| [`An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026`](../../../preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/) | [209](../algebra/209-integral-counterexamples-to-gerstens-conjecture.md) | prose + title | [paper.pdf](../../../preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/paper.pdf) |
| [`Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026`](../../../preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/) | [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | prose | [paper.pdf](../../../preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `gersten`: accents folded, dash variants unified, possessives stripped, case lowered. `Gersten` · `Gersten's`

