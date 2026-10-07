# Name: crouzeix

2 families · subject name · 1 carried by a title or a declaration · 1 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 50 capitalized occurrences, 31 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [183](../combinatorics/183-power-savings-for-planar-halving-lines-and-k-sets.md) | Power savings for planar halving lines and $k$-sets | — | — | — | — | — | yes |
| [325](../functional-analysis/325-complete-crouzeix-conjecture.md) | The complete Crouzeix conjecture | yes | yes | — | yes | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026`](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/) | [325](../functional-analysis/325-complete-crouzeix-conjecture.md) | prose + title | [paper.pdf](../../../preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf) |
| [`The-complete-Crouzeix-theorem-September-23-2026`](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/) | [325](../functional-analysis/325-complete-crouzeix-conjecture.md) | prose + title | [paper.pdf](../../../preprints/The-complete-Crouzeix-theorem-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [CompleteCrouzeix](../../../lean/ComparatorChallenges/CompleteCrouzeix.json) | `OAI.CompleteCrouzeix.main` | [Main.lean](../../../lean/OAI/Analysis/NumericalRange/Main.lean) | [325](../functional-analysis/325-complete-crouzeix-conjecture.md) |
| [DirectCrouzeix](../../../lean/ComparatorChallenges/DirectCrouzeix.json) | `OAI.DirectCrouzeix.complete_crouzeix` | [CompleteBound.lean](../../../lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean) | [325](../functional-analysis/325-complete-crouzeix-conjecture.md) |
| [StructuralCrouzeix](../../../lean/ComparatorChallenges/StructuralCrouzeix.json) | `OAI.StructuralCrouzeixReference.challenge` | [Endpoint.lean](../../../lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean) | [325](../functional-analysis/325-complete-crouzeix-conjecture.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `crouzeix`: accents folded, dash variants unified, possessives stripped, case lowered. `Crouzeix` · `Crouzeix's`

