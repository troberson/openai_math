# Name: ryser

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 1 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 14 capitalized occurrences, 11 of them mid-sentence, 10 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 1 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | Counterexamples to Ryser's covering and Gy\'arf\'as's tree-cover conjectures | yes | — | — | yes | yes | — |
| [179](../combinatorics/179-circulant-hadamard-conjecture.md) | The circulant Hadamard conjecture | — | — | — | — | yes | yes |
| [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | Saxl's conjecture and universal tensor squares | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026`](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/) | [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | prose | [paper.pdf](../../../preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf) |
| [`A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026`](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/) | [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | prose | [paper.pdf](../../../preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/paper.pdf) |
| [`Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026`](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/) | [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) | prose | [paper.pdf](../../../preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf) |
| [`The-circulant-Hadamard-conjecture-September-23-2026`](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/) | [179](../combinatorics/179-circulant-hadamard-conjecture.md) | prose | [paper.pdf](../../../preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [RyserCovering](../../../lean/ComparatorChallenges/RyserCovering.json) | `OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank` | [Main.lean](../../../lean/OAI/Combinatorics/Ryser/Construction/Main.lean) | [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) |
| [RyserOddExtensions](../../../lean/ComparatorChallenges/RyserOddExtensions.json) | `OAI.RyserOdd.eventualOddFailures_and_infinite` | [OddExtensions.lean](../../../lean/OAI/Combinatorics/Ryser/OddExtensions.lean) | [162](../combinatorics/162-counterexamples-to-rysers-covering-and-gy-tree-cover-conjectures.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `ryser`: accents folded, dash variants unified, possessives stripped, case lowered. `Ryser's` · `Ryser`

