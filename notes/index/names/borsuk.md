# Name: borsuk

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 9 capitalized occurrences, 7 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [156](../combinatorics/156-borsuks-conjecture-fails-in-dimension-nine.md) | Borsuk's conjecture fails in dimension nine | yes | — | — | yes | yes | yes |
| [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | The higher-dimensional Erd\H{o}s distinct-distances conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026`](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/) | [156](../combinatorics/156-borsuks-conjecture-fails-in-dimension-nine.md) | prose | [paper.pdf](../../../preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf) |
| [`The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026`](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/) | [166](../combinatorics/166-higher-dimensional-erdos-distinct-distances-conjecture.md) | prose | [paper.pdf](../../../preprints/The-higher-dimensional-Erdos-distinct-distances-conjecture-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [BorsukNine](../../../lean/ComparatorChallenges/BorsukNine.json) | `OAI.BorsukNine.main_theorem` | [Counterexample.lean](../../../lean/OAI/Geometry/Borsuk/Counterexample.lean) | [156](../combinatorics/156-borsuks-conjecture-fails-in-dimension-nine.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `borsuk`: accents folded, dash variants unified, possessives stripped, case lowered. `Borsuk's` · `Borsuk`

