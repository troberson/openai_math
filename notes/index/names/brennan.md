# Name: brennan

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 14 capitalized occurrences, 10 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [072](../real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) | Brennan's conjecture and a counterexample to Kraetzer's prediction | yes | — | yes | yes | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026`](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/) | [072](../real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) | prose | [paper.pdf](../../../preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf) |
| [`Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026`](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/) | [072](../real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) | prose | [paper.pdf](../../../preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [Brennan](../../../lean/ComparatorChallenges/Brennan.json) | `OAI.Brennan.main_theorem` | [Main.lean](../../../lean/OAI/Analysis/IntegralMeans/Main.lean) | [072](../real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) |
| [BrennanSharp](../../../lean/ComparatorChallenges/BrennanSharp.json) | `OAI.Brennan.Sharp.sharp_endpoints` | [SharpEndpoints.lean](../../../lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean) | [072](../real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) |

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [072](../real-and-complex-analysis/072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) | Brennan's conjecture and inverse-square means |

## Spelling variants

Every form below normalizes to the key `brennan`: accents folded, dash variants unified, possessives stripped, case lowered. `Brennan's` · `Brennan`

