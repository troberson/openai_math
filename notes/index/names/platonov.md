# Name: platonov

3 families · subject name · 1 carried by a title or a declaration · 2 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 39 capitalized occurrences, 32 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | The Margulis--Platonov conjecture over global fields | yes | yes | — | — | yes | yes |
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Counterexamples to Zariski's multiplicity conjecture | — | — | — | — | yes | yes |
| [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | Arithmetic rigidity of lattice von Neumann algebras | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/) | [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/paper.pdf) |
| [`Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026`](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/) | [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/paper.pdf) |
| [`The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose + title | [margulis-platonov-global-function-fields.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/margulis-platonov-global-function-fields.pdf) |
| [`The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose + title | [paper.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `platonov`: accents folded, dash variants unified, possessives stripped, case lowered. `Platonov` · `Platonov's`

