# Name: konyagin

5 families · subject name · 1 carried by a title or a declaration · 4 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 13 capitalized occurrences, 8 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | The Ford--Konyagin--Luca conjecture on prime predecessors | yes | — | — | — | yes | yes |
| [013](../number-theory/013-ostmanns-inverse-goldbach-conjecture.md) | Ostmann's inverse Goldbach conjecture | — | — | — | — | — | yes |
| [021](../number-theory/021-a-quadratic-bound-for-jacobsthals-function.md) | A quadratic bound for Jacobsthal's function | — | — | — | — | yes | yes |
| [025](../number-theory/025-erdoss-short-egyptian-fraction-conjecture.md) | Erd\H{o}s’s short Egyptian-fraction conjecture | — | — | — | — | yes | yes |
| [026](../number-theory/026-positive-lower-density-of-large-prime-gaps.md) | Positive lower density of large prime gaps | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-quadratic-bound-for-Jacobsthals-function-September-25-2026`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/) | [021](../number-theory/021-a-quadratic-bound-for-jacobsthals-function.md) | prose | [paper.pdf](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) |
| [`Positive-lower-density-of-large-prime-gaps-September-25-2026`](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/) | [026](../number-theory/026-positive-lower-density-of-large-prime-gaps.md) | prose | [main.pdf](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf) |
| [`Short-Egyptian-fractions-September-25-2026`](../../../preprints/Short-Egyptian-fractions-September-25-2026/) | [025](../number-theory/025-erdoss-short-egyptian-fraction-conjecture.md) | prose | [Short-Egyptian-fractions-September-25-2026.pdf](../../../preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) |
| [`The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Konyagin`. The normalized key is `konyagin`.

