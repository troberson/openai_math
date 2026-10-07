# Name: chatterji

2 families · subject name · 1 carried by a title or a declaration · 1 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 5 capitalized occurrences, 3 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [139](../theoretical-computer-science/139-subpolynomial-queries-for-log-concave-sampling.md) | Subpolynomial queries for log-concave sampling | — | — | — | — | — | yes |
| [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | The $\ell^1$-Bass and complex Bass trace conjectures | — | — | yes | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026`](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/) | [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | prose | [The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf) |
| [`The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026`](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/) | [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | prose | [l1-bass-conjecture.pdf](../../../preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/l1-bass-conjecture.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | Berrick--Chatterji--Mislin consequences |

## Spelling variants

One surface form in prose: `Chatterji`. The normalized key is `chatterji`.

