# Name: eisenbud

8 families · subject name · 1 carried by a title or a declaration · 3 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 38 capitalized occurrences, 26 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [020](../number-theory/020-squarefree-quartics-and-power-free-polynomial-values.md) | Squarefree quartics and power-free polynomial values | — | — | — | — | — | yes |
| [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | The rational Hodge conjecture for CM abelian varieties and products of K3 surfaces | — | — | — | — | yes | — |
| [059](../algebraic-and-complex-geometry/059-counterexamples-to-zariskis-multiplicity-conjecture.md) | Counterexamples to Zariski's multiplicity conjecture | — | — | — | — | — | yes |
| [067](../algebraic-and-complex-geometry/067-campana-peternell-conjecture-in-dimension-six.md) | The Campana--Peternell conjecture in dimension six | — | — | — | — | — | yes |
| [194](../algebra/194-lechs-multiplicity-conjecture.md) | Lech's multiplicity conjecture | — | — | — | — | yes | — |
| [195](../algebra/195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md) | A counterexample to the small Cohen--Macaulay module conjecture | — | — | — | — | — | yes |
| [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | Eisenbud--Green--Harris and lex-plus-powers in characteristic zero | yes | yes | yes | — | yes | — |
| [359](../differential-geometry/359-negative-k-ahler-curvature-without-bounded-holomorphic-coordinates.md) | Negative K\"ahler curvature without bounded holomorphic coordinates | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026`](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026/) | [032](../algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties-and-products-of-k3-surfaces.md) | prose | [paper.pdf](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-September-30-2026/paper.pdf) |
| [`Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026`](../../../preprints/Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026/) | [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | prose + title | [paper.pdf](../../../preprints/Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026/paper.pdf) |
| [`Lechs-multiplicity-conjecture-September-23-2026`](../../../preprints/Lechs-multiplicity-conjecture-September-23-2026/) | [194](../algebra/194-lechs-multiplicity-conjecture.md) | prose | [paper.pdf](../../../preprints/Lechs-multiplicity-conjecture-September-23-2026/paper.pdf) |
| [`The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026`](../../../preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/) | [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | prose | [paper.pdf](../../../preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | Artinian Eisenbud--Green--Harris |
| [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | Eisenbud--Green--Harris in characteristic zero |
| [200](../algebra/200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) | Eisenbud--Green--Harris and lex-plus-powers in characteristic zero |

## Spelling variants

One surface form in prose: `Eisenbud`. The normalized key is `eisenbud`.

