# Name: zarankiewicz

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 5 capitalized occurrences, 4 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [165](../combinatorics/165-exact-crossing-numbers-of-complete-and-complete-bipartite-graphs.md) | Exact crossing numbers of complete and complete bipartite graphs | — | — | — | yes | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`The-crossing-number-of-complete-bipartite-graphs-September-23-2026`](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/) | [165](../combinatorics/165-exact-crossing-numbers-of-complete-and-complete-bipartite-graphs.md) | prose | [paper.pdf](../../../preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [BipartiteCrossing](../../../lean/ComparatorChallenges/BipartiteCrossing.json) | `OAI.Zarankiewicz.mainTarget_proof` | [Main.lean](../../../lean/OAI/Combinatorics/Crossing/Main.lean) | [165](../combinatorics/165-exact-crossing-numbers-of-complete-and-complete-bipartite-graphs.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Zarankiewicz`. The normalized key is `zarankiewicz`.

