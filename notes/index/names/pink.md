# Name: pink

2 families · subject name · 1 carried by a title or a declaration · 2 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 49 capitalized occurrences, 33 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

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
| [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | Zilber--Pink in abelian varieties and the Siegel threefold | yes | yes | yes | — | yes | yes |
| [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | Finite lattice representation: counterexamples and undecidability | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026`](../../../preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/) | [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | prose | [paper.pdf](../../../preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/paper.pdf) |
| [`Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026`](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/) | [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | prose + title | [paper.pdf](../../../preprints/Elliptic-Squares-and-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) |
| [`Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026`](../../../preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/) | [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | prose | [paper.pdf](../../../preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf) |
| [`Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026`](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/) | [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | prose | [paper.pdf](../../../preprints/Quaternionic-Division-Points-on-Curves-in-the-Siegel-Threefold-September-24-2026/paper.pdf) |
| [`The-Abelian-Zilber-Pink-Conjecture-September-24-2026`](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/) | [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | prose + title | [paper.pdf](../../../preprints/The-Abelian-Zilber-Pink-Conjecture-September-24-2026/paper.pdf) |
| [`The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/) | [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | prose + title | [paper.pdf](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | Zilber--Pink for curves in $\A_2$ |

## Spelling variants

Every form below normalizes to the key `pink`: accents folded, dash variants unified, possessives stripped, case lowered. `Pink` · `Pink's`

