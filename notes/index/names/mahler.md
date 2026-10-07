# Name: mahler

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 3 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 44 capitalized occurrences, 27 of them mid-sentence, 27 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 3 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | — | — | yes | — |
| [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | Torus-packet equidistribution in prime, quartic, and sextic degrees | — | — | — | — | yes | yes |
| [017](../number-theory/017-irrationality-exponent-of-is-2.md) | The irrationality exponent of $\pi$ is $2$ | — | — | — | — | yes | yes |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | The Mahler conjectures and symplectic width | yes | yes | yes | yes | yes | yes |
| [101](../convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md) | The sharp simplex conjecture for isotropic constants | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026`](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/) | [101](../convex-and-metric-geometry/101-sharp-simplex-conjecture-for-isotropic-constants.md) | prose | [isotropic-simplex.pdf](../../../preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf) |
| [`Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026`](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [paper.pdf](../../../preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf) |
| [`Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026`](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [quartic-torus-packets.pdf](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf) |
| [`Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026`](../../../preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [primitive-sextic-torus-packets.pdf](../../../preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf) |
| [`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026`](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [exact-bsd-low-selmer-corank.pdf](../../../preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/exact-bsd-low-selmer-corank.pdf) |
| [`Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026`](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose | [paper.pdf](../../../preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf) |
| [`The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026`](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose + title | [paper.pdf](../../../preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/paper.pdf) |
| [`The-irrationality-exponent-of-pi-is-2-September-24-2026`](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/) | [017](../number-theory/017-irrationality-exponent-of-is-2.md) | prose | [paper.pdf](../../../preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf) |
| [`The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026`](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | prose + title | [paper.pdf](../../../preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) |
| [`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026`](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [paper.pdf](../../../preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [MahlerConjecture](../../../lean/ComparatorChallenges/MahlerConjecture.json) | `OAI.SymmetricMahler.symmetric_mahler` | [MainTheorem.lean](../../../lean/OAI/Analysis/Mahler/MainTheorem.lean) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) |
| [SymmetricMahlerEquality](../../../lean/ComparatorChallenges/SymmetricMahlerEquality.json) | `OAI.SymmetricMahler.symmetric_mahler_equality` | [Classification.lean](../../../lean/OAI/Analysis/Mahler/Classification.lean) | [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) |

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | Symmetric Mahler inequality |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | General Mahler conjecture |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | Functional Mahler inequality |
| [087](../convex-and-metric-geometry/087-mahler-conjectures-and-symplectic-width.md) | Even functional Mahler inequality |

## Spelling variants

Every form below normalizes to the key `mahler`: accents folded, dash variants unified, possessives stripped, case lowered. `Mahler` · `Mahler's`

