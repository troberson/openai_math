# Name: saxl

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 29 capitalized occurrences, 21 of them mid-sentence, 9 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | Saxl's conjecture and universal tensor squares | yes | — | yes | yes | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026`](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/) | [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | prose | [paper.pdf](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/paper.pdf) |
| [`Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026`](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/) | [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | prose | [main.pdf](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [Saxl](../../../lean/ComparatorChallenges/Saxl.json) | `OAI.Saxl.saxl_conjecture` | [Main.lean](../../../lean/OAI/RepresentationTheory/Saxl/Main.lean) | [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) |

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | Saxl's conjecture |

## Spelling variants

Every form below normalizes to the key `saxl`: accents folded, dash variants unified, possessives stripped, case lowered. `Saxl` · `Saxl's`

