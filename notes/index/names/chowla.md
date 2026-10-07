# Name: chowla

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 5 capitalized occurrences, 5 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [007](../number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md) | Two-point Chowla and the corrected binary Elliott conjecture | yes | — | — | — | yes | yes |
| [028](../number-theory/028-gaussian-moat-conjecture.md) | The Gaussian moat conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026`](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/) | [028](../number-theory/028-gaussian-moat-conjecture.md) | prose | [paper.pdf](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf) |
| [`Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/) | [007](../number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md) | prose | [final.pdf](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `chowla`: accents folded, dash variants unified, possessives stripped, case lowered. `Chowla` · `Chowla's`

