# Name: gallai

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 4 capitalized occurrences, 4 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [181](../combinatorics/181-erdos-gallai-cycle-decomposition-conjecture.md) | The Erd\H{o}s--Gallai cycle-decomposition conjecture | yes | — | — | yes | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026`](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/) | [181](../combinatorics/181-erdos-gallai-cycle-decomposition-conjecture.md) | prose | [main.pdf](../../../preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [CycleDecomposition](../../../lean/ComparatorChallenges/CycleDecomposition.json) | `OAI.ErdosGallai.erdos_gallai` | [Main.lean](../../../lean/OAI/Combinatorics/CycleDecomposition/Main.lean) | [181](../combinatorics/181-erdos-gallai-cycle-decomposition-conjecture.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Gallai`. The normalized key is `gallai`.

