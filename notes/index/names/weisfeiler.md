# Name: weisfeiler

4 families · subject name · 1 carried by a title or a declaration · 3 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 64 capitalized occurrences, 53 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | Zilber--Pink in abelian varieties and the Siegel threefold | — | — | — | — | — | yes |
| [047](../algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md) | Complex counterexamples to cancellation and affine fibrations | — | — | — | — | yes | — |
| [133](../theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md) | The complexity of Weisfeiler--Leman refinement | yes | yes | yes | — | yes | yes |
| [161](../combinatorics/161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) | Counterexamples to Sidorenko's conjecture and the forcing conjecture | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Sidorenkos-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/) | [161](../combinatorics/161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf) |
| [`An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/) | [047](../algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md) | prose | [paper.pdf](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf) |
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

One surface form in prose: `Weisfeiler`. The normalized key is `weisfeiler`.

