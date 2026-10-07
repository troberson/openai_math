# Name: mendel

4 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 8 capitalized occurrences, 3 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [094](../convex-and-metric-geometry/094-subpolynomial-dimension-reduction-in-l-p.md) | Subpolynomial dimension reduction in $L_p$ | — | — | — | — | yes | — |
| [110](../theoretical-computer-science/110-optimal-order-randomized-k-server-on-arbitrary-metrics.md) | Optimal-order randomized $k$-server on arbitrary metrics | — | — | — | — | — | yes |
| [327](../functional-analysis/327-markov-type-characterizes-superreflexivity.md) | Markov type characterizes superreflexivity | — | — | — | — | yes | — |
| [332](../functional-analysis/332-metric-markov-cotype-two-for-1.md) | Metric Markov cotype two for $\ell_1$ | — | — | yes | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Metric-Markov-Cotype-Two-of-l1-October-5-2026`](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/) | [332](../functional-analysis/332-metric-markov-cotype-two-for-1.md) | prose | [l1-markov-cotype.pdf](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf) |
| [`Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026`](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/) | [327](../functional-analysis/327-markov-type-characterizes-superreflexivity.md) | prose | [paper.pdf](../../../preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf) |
| [`Subpolynomial-dimension-reduction-in-Lp-September-23-2026`](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/) | [094](../convex-and-metric-geometry/094-subpolynomial-dimension-reduction-in-l-p.md) | prose | [paper.pdf](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [332](../functional-analysis/332-metric-markov-cotype-two-for-1.md) | Mendel--Naor |

## Spelling variants

One surface form in prose: `Mendel`. The normalized key is `mendel`.

