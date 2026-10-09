# Name: fricke

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 40 capitalized occurrences, 36 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | yes | — | yes | — |
| [006](../number-theory/006-goldfelds-conjecture.md) | Goldfeld's conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/) | — | prose | — |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [exact-bsd-low-selmer-corank.pdf](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf) |
| [`The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026`](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [main.pdf](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf) |
| [`The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026`](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/) | — | prose | — |
| [`The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026`](../../../preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026/) | [006](../number-theory/006-goldfelds-conjecture.md) | prose | [paper.pdf](../../../preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026/paper.pdf) |
| [`The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-September-23-2026`](../../../preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-September-23-2026/) | — | prose | — |
| [`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026`](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [paper.pdf](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/paper.pdf) |
| [`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026`](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/) | — | prose | — |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | Horizontal integrality and Fricke invariance |
| — | Horizontal integrality and Fricke invariance |

## Spelling variants

One surface form in prose: `Fricke`. The normalized key is `fricke`.

