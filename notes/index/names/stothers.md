# Name: stothers

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 14 capitalized occurrences, 8 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [047](../algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md) | Complex counterexamples to cancellation and affine fibrations | — | — | yes | — | yes | — |
| [107](../theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md) | Matrix multiplication with exponent at most $9/4$ | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/) | [047](../algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md) | prose | [paper.pdf](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf) |
| [`Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026`](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/) | [107](../theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md) | prose | [Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf](../../../preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026.pdf) |
| [`Matrix-Multiplication-Nine-Fourths-October-2-2026`](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/) | [107](../theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md) | prose | [paper.pdf](../../../preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf) |
| [`Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026`](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/) | [107](../theoretical-computer-science/107-matrix-multiplication-with-exponent-at-most-9-4.md) | prose | [Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf](../../../preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [047](../algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md) | Mason--Stothers polynomial \(abc\) |

## Spelling variants

One surface form in prose: `Stothers`. The normalized key is `stothers`.

