# Name: luck

8 families · subject name · 1 carried by a title or a declaration · 7 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 33 capitalized occurrences, 12 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 7 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [060](../algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md) | The Global Spherical Shell conjecture | — | — | — | — | yes | — |
| [197](../algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) | Nonsofic groups and group-ring counterexamples | — | — | — | — | yes | yes |
| [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | The $\ell^1$-Bass and complex Bass trace conjectures | — | — | — | — | — | yes |
| [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | Gersten's conjecture for one-relator groups | — | — | — | — | yes | — |
| [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | Counterexamples to Baum--Connes and Kadison--Kaplansky | — | — | yes | — | yes | yes |
| [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | Counterexamples to disk embedding and Wall's manifold conjecture | — | — | — | — | yes | — |
| [315](../topology/315-four-dimensional-singer-conjecture.md) | The four-dimensional Singer conjecture | — | — | — | — | yes | yes |
| [320](../topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md) | A four-dimensional counterexample to Borel rigidity | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026`](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/) | [197](../algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) | prose | [paper.pdf](../../../preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf) |
| [`A-PD4-group-without-an-aspherical-manifold-model-September-24-2026`](../../../preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/) | [305](../topology/305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) | prose | [paper.pdf](../../../preprints/A-PD4-group-without-an-aspherical-manifold-model-September-24-2026/paper.pdf) |
| [`A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf) |
| [`An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026`](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/paper.pdf) |
| [`Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026`](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/) | [060](../algebraic-and-complex-geometry/060-global-spherical-shell-conjecture.md) | prose | [paper.pdf](../../../preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/paper.pdf) |
| [`Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026`](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/) | [320](../topology/320-a-four-dimensional-counterexample-to-borel-rigidity.md) | prose | [paper.pdf](../../../preprints/Nonhomeomorphic-closed-aspherical-four-manifolds-with-the-same-homotopy-type-October-4-2026/paper.pdf) |
| [`The-Singer-conjecture-in-dimension-four-September-25-2026`](../../../preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/) | [315](../topology/315-four-dimensional-singer-conjecture.md) | prose | [paper.pdf](../../../preprints/The-Singer-conjecture-in-dimension-four-September-25-2026/paper.pdf) |
| [`Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026`](../../../preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/) | [258](../group-theory/258-gerstens-conjecture-for-one-relator-groups.md) | prose | [paper.pdf](../../../preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | Luck |

## Spelling variants

Every form below normalizes to the key `luck`: accents folded, dash variants unified, possessives stripped, case lowered. `Luck` · `Luck's`

