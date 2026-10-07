# Name: lang

11 families · subject name · 1 carried by a title or a declaration · 11 by prose · 6 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 68 capitalized occurrences, 42 of them mid-sentence, 3 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 11 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 6 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | — | — | yes | — |
| [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | Hilbert's tenth problem over $\mathbb Q$ | — | — | — | — | yes | — |
| [006](../number-theory/006-goldfelds-conjecture.md) | Goldfeld's conjecture | — | — | — | — | yes | yes |
| [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | Restricted geometric Langlands, generic Ramanujan and Arthur parameters | — | — | — | — | yes | yes |
| [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | Zilber--Pink in abelian varieties and the Siegel threefold | — | — | — | — | yes | — |
| [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | The Margulis--Platonov conjecture over global fields | — | — | — | — | yes | yes |
| [027](../number-theory/027-integral-density-on-curve-character-varieties.md) | Integral density on curve character varieties | — | — | — | — | yes | yes |
| [098](../convex-and-metric-geometry/098-a-negative-answer-to-the-lang-plaut-problem.md) | A negative answer to the Lang--Plaut problem | yes | — | — | — | yes | — |
| [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | Donovan's conjecture over fields and discrete valuation rings | — | — | — | — | yes | — |
| [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | Finite lattice representation: counterexamples and undecidability | — | — | — | — | yes | yes |
| [337](../differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md) | Cartan--Hadamard isoperimetry and CAT$(0)$ fillings | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026`](../../../preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/) | [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | prose | [paper.pdf](../../../preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/paper.pdf) |
| [`A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026`](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/) | [098](../convex-and-metric-geometry/098-a-negative-answer-to-the-lang-plaut-problem.md) | prose | [main.pdf](../../../preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf) |
| [`A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026`](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/) | [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | prose | [paper.pdf](../../../preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/paper.pdf) |
| [`Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026`](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/) | [203](../algebra/203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) | prose | [main.pdf](../../../preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/main.pdf) |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [exact-bsd-low-selmer-corank.pdf](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/exact-bsd-low-selmer-corank.pdf) |
| [`Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026`](../../../preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/) | [206](../algebra/206-finite-lattice-representation-counterexamples-and-undecidability.md) | prose | [paper.pdf](../../../preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf) |
| [`Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026`](../../../preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026/) | [006](../number-theory/006-goldfelds-conjecture.md) | prose | [paper.pdf](../../../preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026/paper.pdf) |
| [`Integral-points-on-character-varieties-of-curves-September-25-2026`](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/) | [027](../number-theory/027-integral-density-on-curve-character-varieties.md) | prose | [paper.pdf](../../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf) |
| [`Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026`](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/) | [014](../number-theory/014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) | prose | [paper.pdf](../../../preprints/Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026/paper.pdf) |
| [`Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026`](../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/) | [337](../differential-geometry/337-cartan-hadamard-isoperimetry-and-cat-0-fillings.md) | prose | [paper.pdf](../../../preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf) |
| [`The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026`](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/) | [016](../number-theory/016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) | prose | [paper.pdf](../../../preprints/The-E-times-CM-Component-of-Zilber-Pink-for-Curves-in-A2-September-24-2026/paper.pdf) |
| [`The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose | [margulis-platonov-global-function-fields.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-global-function-fields-October-5-2026/margulis-platonov-global-function-fields.pdf) |
| [`The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026`](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/) | [018](../number-theory/018-margulis-platonov-conjecture-over-global-fields.md) | prose | [paper.pdf](../../../preprints/The-Margulis-Platonov-conjecture-over-number-fields-September-23-2026/paper.pdf) |
| [`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026`](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [paper.pdf](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `lang`: accents folded, dash variants unified, possessives stripped, case lowered. `Lang` · `Lang's`

