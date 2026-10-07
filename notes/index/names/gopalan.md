# Name: gopalan

4 families · subject name · 1 carried by a title or a declaration · 4 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 6 capitalized occurrences, 3 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | The Unique Games Conjecture and optimal approximation thresholds | — | — | — | — | yes | yes |
| [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | Approximate counting of common integer polymatroid bases | — | — | — | — | yes | yes |
| [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | Sampling and counting contingency tables with arbitrary margins | — | — | — | — | yes | yes |
| [192](../combinatorics/192-a-counterexample-to-the-gopalan-servedio-conjecture.md) | A counterexample to the Gopalan--Servedio conjecture | yes | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026`](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/) | [115](../theoretical-computer-science/115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) | prose | [main.pdf](../../../preprints/An-FPRAS-for-Cell-Bounded-Contingency-Tables-September-24-2026/main.pdf) |
| [`An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026`](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/) | [114](../theoretical-computer-science/114-approximate-counting-of-common-integer-polymatroid-bases.md) | prose | [polymatroid-fpras.pdf](../../../preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf) |
| [`The-Unique-Games-Theorem-September-23-2026`](../../../preprints/The-Unique-Games-Theorem-September-23-2026/) | [102](../theoretical-computer-science/102-unique-games-conjecture-and-optimal-approximation-thresholds.md) | prose | [paper.pdf](../../../preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf) |
| [`Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026`](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/) | [192](../combinatorics/192-a-counterexample-to-the-gopalan-servedio-conjecture.md) | prose | [Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf](../../../preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Gopalan`. The normalized key is `gopalan`.

