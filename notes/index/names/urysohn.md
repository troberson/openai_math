# Name: urysohn

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 11 capitalized occurrences, 11 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | Spectral scalar curvature and codimension-two width | — | yes | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026`](../../../preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/) | [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | prose | [paper.pdf](../../../preprints/Positive-scalar-curvature-and-uniform-codimension-two-width-September-23-2026/paper.pdf) |
| [`Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026`](../../../preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/) | [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | prose + title | [spectral-urysohn-three-manifolds.pdf](../../../preprints/Spectral-scalar-curvature-and-Urysohn-width-in-dimension-three-October-5-2026/spectral-urysohn-three-manifolds.pdf) |
| [`Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026`](../../../preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/) | [336](../differential-geometry/336-spectral-scalar-curvature-and-codimension-two-width.md) | prose + title | [main.pdf](../../../preprints/Spectral-scalar-curvature-and-uniform-Urysohn-width-October-5-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Urysohn`. The normalized key is `urysohn`.

