# Name: howe

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 19 capitalized occurrences, 14 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | The Margulis--Platonov conjecture over global fields | — | — | — | — | yes | yes |
| [210](../algebra/210-foulkes-conjecture-for-sixth-powers-and-quadratic-stabilization.md) | Foulkes’ conjecture for sixth powers and quadratic stabilization | — | yes | — | — | yes | — |
| [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | Arithmetic rigidity of lattice von Neumann algebras | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026`](../../../preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/) | [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | prose | [paper.pdf](../../../preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/paper.pdf) |
| [`Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026`](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/) | [210](../algebra/210-foulkes-conjecture-for-sixth-powers-and-quadratic-stabilization.md) | prose | [main.pdf](../../../preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/main.pdf) |
| [`Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026`](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/) | [210](../algebra/210-foulkes-conjecture-for-sixth-powers-and-quadratic-stabilization.md) | prose + title | [paper.pdf](../../../preprints/Quadratic-Stabilization-of-the-Canonical-Foulkes-Howe-Map-September-25-2026/paper.pdf) |
| [`The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose | [margulis-platonov-global-function-fields.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/margulis-platonov-global-function-fields.pdf) |
| [`The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose | [paper.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Howe`. The normalized key is `howe`.

