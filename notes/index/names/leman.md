# Name: leman

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 59 capitalized occurrences, 55 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 2 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | The complexity of Weisfeiler--Leman refinement | yes | yes | yes | — | yes | yes |
| [161](../combinatorics/161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) | Counterexamples to Sidorenko's conjecture and the forcing conjecture | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Sidorenkos-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/) | [161](../combinatorics/161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf) |
| [`Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026`](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose + title | [paper.pdf](../../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) |
| [`The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026`](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose + title | [paper.pdf](../../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/paper.pdf) |
| [`Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026`](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose + title | [paper.pdf](../../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf) |
| [`Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026`](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/) | [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | prose + title | [paper.pdf](../../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | Joint-update Weisfeiler--Leman refinement |

## Spelling variants

Every form below normalizes to the key `leman`: accents folded, dash variants unified, possessives stripped, case lowered. `Leman` · `Leman's`

