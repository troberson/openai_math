# Name: connes

11 families · subject name · 2 carried by a title or a declaration · 10 by prose · 7 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 79 capitalized occurrences, 55 of them mid-sentence, 2 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 2 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 10 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 7 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | The $\ell^1$-Bass and complex Bass trace conjectures | — | — | — | — | yes | yes |
| [256](../group-theory/256-howies-conjecture-on-equations-over-groups.md) | Howie's conjecture on equations over groups | — | — | — | — | yes | — |
| [280](../mathematical-physics/280-strong-locality-for-strongly-rational-unitary-vertex-operator-algebras.md) | Strong locality for strongly rational unitary vertex operator algebras | — | — | — | — | yes | — |
| [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | Counterexamples to Baum--Connes and Kadison--Kaplansky | yes | yes | — | — | yes | yes |
| [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | Arithmetic rigidity of lattice von Neumann algebras | — | — | — | — | yes | yes |
| [287](../operator-algebras/287-all-nonabelian-free-group-factors-are-isomorphic.md) | All nonabelian free group factors are isomorphic | — | — | — | — | — | yes |
| [290](../operator-algebras/290-connes-bicentralizer-conjecture-and-relative-bicentralizers.md) | Connes' bicentralizer conjecture and relative bicentralizers | yes | — | — | — | yes | yes |
| [291](../operator-algebras/291-toms-winter-and-equivariant-jiang-su-stability.md) | Toms--Winter and equivariant Jiang--Su stability | — | — | — | — | yes | yes |
| [292](../operator-algebras/292-a-counterexample-to-kirchbergs-norm-ultrapower-embedding-problem.md) | A counterexample to Kirchberg's norm-ultrapower embedding problem | — | — | — | — | yes | — |
| [301](../operator-algebras/301-classification-by-trace-cones-after-razak-jacelon-stabilization.md) | Classification by trace cones after Razak--Jacelon stabilization | — | — | — | — | yes | yes |
| [307](../topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md) | Failure of rational injectivity for maximal coarse assembly | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose + title | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026/paper.pdf) |
| [`A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026`](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose | [paper.pdf](../../../preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026/paper.pdf) |
| [`A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/) | [307](../topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf) |
| [`An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026`](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/) | [285](../operator-algebras/285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) | prose + title | [paper.pdf](../../../preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026/paper.pdf) |
| [`An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026`](../../../preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/) | [292](../operator-algebras/292-a-counterexample-to-kirchbergs-norm-ultrapower-embedding-problem.md) | prose | [paper.pdf](../../../preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026/paper.pdf) |
| [`Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026`](../../../preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/) | [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | prose | [paper.pdf](../../../preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/paper.pdf) |
| [`Bounded-recovery-for-modular-spectral-averages-September-23-2026`](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/) | [290](../operator-algebras/290-connes-bicentralizer-conjecture-and-relative-bicentralizers.md) | prose | [Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf](../../../preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf) |
| [`Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026`](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/) | [290](../operator-algebras/290-connes-bicentralizer-conjecture-and-relative-bicentralizers.md) | prose | [Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf](../../../preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf) |
| [`Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026`](../../../preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/) | [307](../topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md) | prose | [paper.pdf](../../../preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf) |
| [`Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026`](../../../preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/) | [256](../group-theory/256-howies-conjecture-on-equations-over-groups.md) | prose | [nonsingular-systems-over-arbitrary-groups.pdf](../../../preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf) |
| [`Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026`](../../../preprints/Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026/) | [280](../mathematical-physics/280-strong-locality-for-strongly-rational-unitary-vertex-operator-algebras.md) | prose | [paper.pdf](../../../preprints/Strongly-rational-unitary-vertex-operator-algebras-and-conformal-nets-September-25-2026/paper.pdf) |
| [`The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026`](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/) | [207](../algebra/207-1-bass-and-complex-bass-trace-conjectures.md) | prose | [The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf](../../../preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf) |
| [`The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026`](../../../preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/) | [286](../operator-algebras/286-arithmetic-rigidity-of-lattice-von-neumann-algebras.md) | prose | [paper.pdf](../../../preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/paper.pdf) |
| [`The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026`](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/) | [301](../operator-algebras/301-classification-by-trace-cones-after-razak-jacelon-stabilization.md) | prose | [The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf](../../../preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf) |
| [`Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026`](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/) | [291](../operator-algebras/291-toms-winter-and-equivariant-jiang-su-stability.md) | prose | [paper.pdf](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `connes`: accents folded, dash variants unified, possessives stripped, case lowered. `Connes` · `Connes's`

