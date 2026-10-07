# Name: baumslag

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 29 capitalized occurrences, 26 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | The Boone--Higman conjecture and higher finiteness | — | — | — | — | yes | yes |
| [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | A hyperbolic group with no geometric CAT(0) action | — | — | — | — | yes | yes |
| [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | Gersten's conjecture for one-relator groups | — | yes | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026`](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/) | [257](../group-theory/257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) | prose | [paper.pdf](../../../preprints/A-hyperbolic-group-with-no-geometric-CAT0-action-September-25-2026/paper.pdf) |
| [`A-universal-group-of-type-F-infinity-September-23-2026`](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf) |
| [`Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026`](../../../preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/) | [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | prose + title | [paper.pdf](../../../preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/paper.pdf) |
| [`Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026`](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf) |
| [`Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026`](../../../preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/) | [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | prose | [paper.pdf](../../../preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Baumslag`. The normalized key is `baumslag`.

