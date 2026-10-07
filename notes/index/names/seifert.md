# Name: seifert

4 families · subject name · 1 carried by a title or a declaration · 4 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 102 capitalized occurrences, 96 of them mid-sentence, 7 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Counterexamples to Zariski's multiplicity conjecture | — | — | yes | — | yes | — |
| [066](../algebraic-and-complex-geometry/066-bounded-klt-complements-for-fano-contractions.md) | Bounded klt complements for Fano contractions | — | — | — | — | yes | — |
| [306](../topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) | The purely cosmetic surgery conjecture for knots in $S^3$ | — | — | — | — | yes | — |
| [315](../topology/315-four-dimensional-singer-conjecture.md) | The four-dimensional Singer conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/) | [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/paper.pdf) |
| [`Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/) | [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/paper.pdf) |
| [`Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026`](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/) | [306](../topology/306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) | prose | [paper.pdf](../../../preprints/Purely-Cosmetic-Surgery-on-Knots-in-the-Three-Sphere-September-23-2026/paper.pdf) |
| [`The-Singer-conjecture-in-dimension-four-September-25-2026`](../../../preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/) | [315](../topology/315-four-dimensional-singer-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/paper.pdf) |
| [`Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026`](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/) | [066](../algebraic-and-complex-geometry/066-bounded-klt-complements-for-fano-contractions.md) | prose | [Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Integral Seifert congruence |
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Real Seifert forms from the spectrum |

## Spelling variants

One surface form in prose: `Seifert`. The normalized key is `seifert`.

