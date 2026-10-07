# Name: heilbronn

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 7 capitalized occurrences, 6 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [003](../number-theory/003-quasi-riemann-hypothesis.md) | The quasi-Riemann hypothesis | — | — | — | — | yes | — |
| [191](../combinatorics/191-a-power-improvement-in-the-heilbronn-triangle-problem.md) | A power improvement in the Heilbronn triangle problem | yes | yes | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026`](../../../preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/) | [191](../combinatorics/191-a-power-improvement-in-the-heilbronn-triangle-problem.md) | prose + title | [main.pdf](../../../preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026/main.pdf) |
| [`Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026`](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/) | [003](../number-theory/003-quasi-riemann-hypothesis.md) | prose | [paper.pdf](../../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `heilbronn`: accents folded, dash variants unified, possessives stripped, case lowered. `Heilbronn` · `Heilbronn's`

