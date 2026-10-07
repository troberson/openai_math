# Name: viana

4 families · subject name · 1 carried by a title or a declaration · 3 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 8 capitalized occurrences, 5 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [151](../dynamical-systems-and-ergodic-theory/151-a-c-1-counterexample-to-shubs-entropy-conjecture.md) | A $C^1$ counterexample to Shub’s entropy conjecture | — | — | — | — | yes | yes |
| [183](../combinatorics/183-power-savings-for-planar-halving-lines-and-k-sets.md) | Power savings for planar halving lines and $k$-sets | — | — | — | — | — | yes |
| [221](../probability-and-statistical-mechanics/221-m-parisi-formula-for-diluted-spin-glasses.md) | The M\'ezard--Parisi formula for diluted spin glasses | — | — | yes | — | yes | yes |
| [349](../differential-geometry/349-solomon-yau-least-volume-conjecture.md) | The Solomon--Yau least-volume conjecture | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026`](../../../preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/) | [151](../dynamical-systems-and-ergodic-theory/151-a-c-1-counterexample-to-shubs-entropy-conjecture.md) | prose | [article.pdf](../../../preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/article.pdf) |
| [`The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026`](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/) | [221](../probability-and-statistical-mechanics/221-m-parisi-formula-for-diluted-spin-glasses.md) | prose | [paper.pdf](../../../preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf) |
| [`The-Solomon-Yau-least-volume-theorem-September-23-2026`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/) | [349](../differential-geometry/349-solomon-yau-least-volume-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [221](../probability-and-statistical-mechanics/221-m-parisi-formula-for-diluted-spin-glasses.md) | Viana--Bray and diluted even-spin models |

## Spelling variants

Every form below normalizes to the key `viana`: accents folded, dash variants unified, possessives stripped, case lowered. `Viana` · `Viana's`

