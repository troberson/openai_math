# Name: matomaki

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 12 capitalized occurrences, 7 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [007](../number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md) | Two-point Chowla and the corrected binary Elliott conjecture | — | — | yes | — | yes | yes |
| [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | The Ford--Konyagin--Luca conjecture on prime predecessors | — | — | — | — | yes | yes |
| [012](../number-theory/012-independent-largest-prime-factors-of-consecutive-integers.md) | Independent largest prime factors of consecutive integers | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026`](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/) | [007](../number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md) | prose | [final.pdf](../../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf) |
| [`The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) |
| [`The-joint-Dickman-law-for-consecutive-integers-September-24-2026`](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/) | [012](../number-theory/012-independent-largest-prime-factors-of-consecutive-integers.md) | prose | [paper.pdf](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) |
| [`Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [007](../number-theory/007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md) | Matomaki--Radziwi\l\l--Tao,
\citeMRT15, Theorem~1.3 |

## Spelling variants

One surface form in prose: `Matomaki`. The normalized key is `matomaki`.

