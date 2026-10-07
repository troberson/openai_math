# Name: kalton

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 44 capitalized occurrences, 17 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [324](../functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md) | Lipschitz equivalence without linear isomorphism | — | — | — | — | yes | yes |
| [330](../functional-analysis/330-a-negative-answer-to-kaltons-lipschitz-free-approximation-question.md) | A negative answer to Kalton's Lipschitz-free approximation question | yes | — | — | — | yes | — |
| [332](../functional-analysis/332-metric-markov-cotype-two-for-1.md) | Metric Markov cotype two for $\ell_1$ | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026`](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/) | [324](../functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md) | prose | [paper.pdf](../../../preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf) |
| [`Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026`](../../../preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/) | [330](../functional-analysis/330-a-negative-answer-to-kaltons-lipschitz-free-approximation-question.md) | prose | [main.pdf](../../../preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/main.pdf) |
| [`Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026`](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/) | [324](../functional-analysis/324-lipschitz-equivalence-without-linear-isomorphism.md) | prose | [paper.pdf](../../../preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf) |
| [`Metric-Markov-Cotype-Two-of-l1-October-5-2026`](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/) | [332](../functional-analysis/332-metric-markov-cotype-two-for-1.md) | prose | [l1-markov-cotype.pdf](../../../preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `kalton`: accents folded, dash variants unified, possessives stripped, case lowered. `Kalton` · `Kalton's`

