# Name: emerton

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 20 capitalized occurrences, 9 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity | — | — | yes | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/) | [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | prose | [paper.pdf](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026/paper.pdf) |
| [`Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/) | — | prose | — |
| [`The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/) | [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | prose | [two-adic-hecke.pdf](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Emerton |

## Spelling variants

Every form below normalizes to the key `emerton`: accents folded, dash variants unified, possessives stripped, case lowered. `Emerton` · `Emerton's`

