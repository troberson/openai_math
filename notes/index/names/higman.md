# Name: higman

5 families · subject name · 1 carried by a title or a declaration · 4 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 40 capitalized occurrences, 29 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [196](../algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md) | A counterexample to Kaplansky's zero-divisor conjecture | — | — | — | — | yes | yes |
| [197](../algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) | Nonsofic groups and group-ring counterexamples | — | — | — | — | — | yes |
| [202](../algebra/202-blockwise-alperin-weight-conjecture.md) | The blockwise Alperin weight conjecture | — | — | — | — | yes | yes |
| [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | The Boone--Higman conjecture and higher finiteness | yes | yes | — | — | yes | yes |
| [253](../group-theory/253-an-infinite-finitely-presented-simple-amenable-group.md) | An infinite finitely presented simple amenable group | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026`](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/) | [196](../algebra/196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf) |
| [`A-universal-group-of-type-F-infinity-September-23-2026`](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/paper.pdf) |
| [`An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026`](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/) | [253](../group-theory/253-an-infinite-finitely-presented-simple-amenable-group.md) | prose | [paper.pdf](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf) |
| [`Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026`](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose + title | [paper.pdf](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf) |
| [`Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026`](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/paper.pdf) |
| [`The-Blockwise-Alperin-Weight-Conjecture-September-23-2026`](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/) | [202](../algebra/202-blockwise-alperin-weight-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Blockwise-Alperin-Weight-Conjecture-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `higman`: accents folded, dash variants unified, possessives stripped, case lowered. `Higman` · `Higman's`

