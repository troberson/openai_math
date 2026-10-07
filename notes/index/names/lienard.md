# Name: lienard

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 17 capitalized occurrences, 16 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [143](../dynamical-systems-and-ergodic-theory/143-uniform-limit-cycle-bounds-in-hilberts-sixteenth-problem.md) | Uniform limit-cycle bounds in Hilbert's sixteenth problem | — | — | — | yes | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`two-limit-cycles-for-quintic-lienard-systems-September-24-2026`](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/) | [143](../dynamical-systems-and-ergodic-theory/143-uniform-limit-cycle-bounds-in-hilberts-sixteenth-problem.md) | prose | [two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf](../../../preprints/two-limit-cycles-for-quintic-lienard-systems-September-24-2026/two-limit-cycles-for-quintic-lienard-systems-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [QuinticLienard](../../../lean/ComparatorChallenges/QuinticLienard.json) | `OAI.QuinticLienard.main` | [Main.lean](../../../lean/OAI/Analysis/LienardCycles/Main.lean) | [143](../dynamical-systems-and-ergodic-theory/143-uniform-limit-cycle-bounds-in-hilberts-sixteenth-problem.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `lienard`: accents folded, dash variants unified, possessives stripped, case lowered. `Lienard` · `Lienard's`

