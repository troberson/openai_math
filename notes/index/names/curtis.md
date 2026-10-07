# Name: curtis

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 11 capitalized occurrences, 8 of them mid-sentence, 5 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | The Margulis--Platonov conjecture over global fields | — | — | — | — | yes | yes |
| [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | Saxl's conjecture and universal tensor squares | — | — | — | — | yes | — |
| [316](../topology/316-curtiss-conjecture.md) | Curtis’s conjecture | yes | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose | [paper.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf) |
| [`The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026`](../../../preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/) | [316](../topology/316-curtiss-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Stable-Hurewicz-Image-of-the-Sphere-at-Two-September-25-2026/paper.pdf) |
| [`Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026`](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/) | [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | prose | [main.pdf](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `curtis`: accents folded, dash variants unified, possessives stripped, case lowered. `Curtis` · `Curtis's`

