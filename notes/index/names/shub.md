# Name: shub

2 families · subject name · 1 carried by a title or a declaration · 1 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 5 capitalized occurrences, 2 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [151](../dynamical-systems-and-ergodic-theory/151-a-c-1-counterexample-to-shubs-entropy-conjecture.md) | A $C^1$ counterexample to Shub’s entropy conjecture | yes | — | — | — | yes | yes |
| [339](../differential-geometry/339-katoks-entropy-rigidity-conjecture.md) | Katok's entropy rigidity conjecture | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026`](../../../preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/) | [151](../dynamical-systems-and-ergodic-theory/151-a-c-1-counterexample-to-shubs-entropy-conjecture.md) | prose | [article.pdf](../../../preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/article.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `shub`: accents folded, dash variants unified, possessives stripped, case lowered. `Shub's` · `Shub`

