# Name: courtade

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 14 capitalized occurrences, 10 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | The Courtade--Kumar and Hellinger conjectures | yes | — | yes | yes | yes | yes |
| [139](../theoretical-computer-science/139-subpolynomial-queries-for-log-concave-sampling.md) | Subpolynomial queries for log-concave sampling | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026`](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/) | [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | prose | [main.pdf](../../../preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf) |
| [`Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026`](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/) | [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | prose | [main.pdf](../../../preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf) |
| [`Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026`](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/) | [139](../theoretical-computer-science/139-subpolynomial-queries-for-log-concave-sampling.md) | prose | [article.pdf](../../../preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/article.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [CourtadeKumar](../../../lean/ComparatorChallenges/CourtadeKumar.json) | `OAI.LeanBlast.CourtadeKumar.courtadeKumarAndAttainment` | [Main.lean](../../../lean/OAI/InformationTheory/BooleanNoise/Main.lean) | [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) |

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [119](../theoretical-computer-science/119-courtade-kumar-and-hellinger-conjectures.md) | Courtade--Kumar bound |

## Spelling variants

One surface form in prose: `Courtade`. The normalized key is `courtade`.

