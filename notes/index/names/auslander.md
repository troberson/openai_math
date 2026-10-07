# Name: auslander

4 families · subject name · 1 carried by a title or a declaration · 4 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 26 capitalized occurrences, 24 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [035](../algebraic-and-complex-geometry/035-threefold-log-abundance-in-numerical-dimension-one-in-characteristic-p-3.md) | Threefold log abundance in numerical dimension one in characteristic $p>3$ | — | — | — | — | yes | — |
| [195](../algebra/195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md) | A counterexample to the small Cohen--Macaulay module conjecture | — | — | — | — | yes | — |
| [199](../algebra/199-counterexamples-to-conjectures-of-auslander-reiten-tachikawa-and-nakayama.md) | Counterexamples to conjectures of Auslander--Reiten, Tachikawa, and Nakayama | yes | yes | — | — | yes | yes |
| [208](../algebra/208-finite-benson-etingof-ostrik-conjecture.md) | The finite Benson--Etingof--Ostrik conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026`](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/) | [195](../algebra/195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md) | prose | [paper.pdf](../../../preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/paper.pdf) |
| [`A-counterexample-to-Tachikawas-second-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/) | [199](../algebra/199-counterexamples-to-conjectures-of-auslander-reiten-tachikawa-and-nakayama.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf) |
| [`Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026`](../../../preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/) | [035](../algebraic-and-complex-geometry/035-threefold-log-abundance-in-numerical-dimension-one-in-characteristic-p-3.md) | prose | [paper.pdf](../../../preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/paper.pdf) |
| [`An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026`](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/) | [199](../algebra/199-counterexamples-to-conjectures-of-auslander-reiten-tachikawa-and-nakayama.md) | prose + title | [paper.pdf](../../../preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf) |
| [`Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026`](../../../preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/) | [208](../algebra/208-finite-benson-etingof-ostrik-conjecture.md) | prose | [paper.pdf](../../../preprints/Fiber-functors-for-finite-symmetric-tensor-categories-in-positive-characteristic-September-24-2026/paper.pdf) |
| [`Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026`](../../../preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/) | [035](../algebraic-and-complex-geometry/035-threefold-log-abundance-in-numerical-dimension-one-in-characteristic-p-3.md) | prose | [paper.pdf](../../../preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `auslander`: accents folded, dash variants unified, possessives stripped, case lowered. `Auslander` · `Auslander's`

