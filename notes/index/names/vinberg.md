# Name: vinberg

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 23 capitalized occurrences, 21 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [046](../algebraic-and-complex-geometry/046-counterexamples-to-shafarevich-holomorphic-convexity.md) | Counterexamples to Shafarevich holomorphic convexity | — | — | — | — | yes | yes |
| [069](../algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md) | Quantum geometric Langlands at irrational level | — | — | yes | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026`](../../../preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/) | [046](../algebraic-and-complex-geometry/046-counterexamples-to-shafarevich-holomorphic-convexity.md) | prose | [paper.pdf](../../../preprints/A-surface-counterexample-to-Shafarevich-holomorphic-convexity-September-23-2026/paper.pdf) |
| [`Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026`](../../../preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/) | [069](../algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md) | prose | [quantum-langlands.pdf](../../../preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [069](../algebraic-and-complex-geometry/069-quantum-geometric-langlands-at-irrational-level.md) | Finite Vinberg comparison |

## Spelling variants

One surface form in prose: `Vinberg`. The normalized key is `vinberg`.

