# Name: pop

7 families · subject name · 1 carried by a title or a declaration · 7 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 58 capitalized occurrences, 25 of them mid-sentence, 26 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 7 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [009](../number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) | Bogomolov--Pop and Milnor $K$-theoretic reconstruction | yes | yes | yes | — | yes | yes |
| [019](../number-theory/019-p-adic-section-conjecture.md) | The $p$-adic section conjecture | — | — | — | — | yes | yes |
| [109](../theoretical-computer-science/109-integer-multiplication-below-n-n.md) | Integer multiplication below $n\log n$ | — | — | — | — | yes | — |
| [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | No infinite critical clusters on quasi-transitive graphs | — | — | — | — | yes | — |
| [242](../mathematical-logic/242-single-fold-diophantine-representations.md) | Single-fold Diophantine representations | — | — | — | — | yes | — |
| [295](../operator-algebras/295-kadison-ringrose-cohomology-conjecture.md) | The Kadison--Ringrose cohomology conjecture | — | — | — | — | yes | yes |
| [300](../operator-algebras/300-popa-vaes-quadratic-strong-operator-paving-conjecture.md) | The Popa--Vaes quadratic strong-operator paving conjecture | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Integer-multiplication-below-n-log-n-September-23-2026`](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/) | [109](../theoretical-computer-science/109-integer-multiplication-below-n-n.md) | prose | [paper.pdf](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf) |
| [`No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026`](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/) | [213](../probability-and-statistical-mechanics/213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) | prose | [paper.pdf](../../../preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf) |
| [`Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026`](../../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/) | [300](../operator-algebras/300-popa-vaes-quadratic-strong-operator-paving-conjecture.md) | prose | [Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf](../../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf) |
| [`Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026`](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/) | [009](../number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) | prose | [mod-ell-bogomolov-pop.pdf](../../../preprints/Reconstruction-of-Function-Fields-from-Mod-ell-Milnor-K-Theory-October-5-2026/mod-ell-bogomolov-pop.pdf) |
| [`Single-fold-Diophantine-representations-September-24-2026`](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/) | [242](../mathematical-logic/242-single-fold-diophantine-representations.md) | prose | [paper.pdf](../../../preprints/Single-fold-Diophantine-representations-September-24-2026/paper.pdf) |
| [`The-Bogomolov-Pop-reconstruction-theorem-September-23-2026`](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/) | [009](../number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) | prose + title | [paper.pdf](../../../preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf) |
| [`The-p-adic-section-conjecture-September-24-2026`](../../../preprints/The-p-adic-section-conjecture-September-24-2026/) | [019](../number-theory/019-p-adic-section-conjecture.md) | prose | [main.pdf](../../../preprints/The-p-adic-section-conjecture-September-24-2026/main.pdf) |
| [`Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026`](../../../preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/) | [295](../operator-algebras/295-kadison-ringrose-cohomology-conjecture.md) | prose | [paper.pdf](../../../preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [009](../number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) | Bogomolov--Pop reconstruction |
| [009](../number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) | Pop's reconstruction theorems |
| [009](../number-theory/009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) | Pop's residual density input |

## Spelling variants

Every form below normalizes to the key `pop`: accents folded, dash variants unified, possessives stripped, case lowered. `Pop` · `Pop's`

