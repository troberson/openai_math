# Name: ford

13 families · subject name · 2 carried by a title or a declaration · 9 by prose · 11 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 51 capitalized occurrences, 31 of them mid-sentence, 13 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 9 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 11 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [003](../number-theory/003-quasi-riemann-hypothesis.md) | The quasi-Riemann hypothesis | — | — | — | — | yes | — |
| [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | The Ford--Konyagin--Luca conjecture on prime predecessors | yes | — | — | — | yes | yes |
| [012](../number-theory/012-independent-largest-prime-factors-of-consecutive-integers.md) | Independent largest prime factors of consecutive integers | — | — | — | — | yes | yes |
| [013](../number-theory/013-ostmanns-inverse-goldbach-conjecture.md) | Ostmann's inverse Goldbach conjecture | — | — | — | — | — | yes |
| [021](../number-theory/021-a-quadratic-bound-for-jacobsthals-function.md) | A quadratic bound for Jacobsthal's function | — | — | — | — | yes | yes |
| [024](../number-theory/024-an-asymptotic-formula-for-the-number-of-totients.md) | An asymptotic formula for the number of totients | — | — | yes | — | yes | yes |
| [026](../number-theory/026-positive-lower-density-of-large-prime-gaps.md) | Positive lower density of large prime gaps | — | — | — | — | yes | yes |
| [029](../number-theory/029-artins-primitive-root-conjecture-infinitude-for-every-base.md) | Artin's primitive root conjecture: infinitude for every base | — | — | — | — | yes | — |
| [113](../theoretical-computer-science/113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md) | Approximate counting and the perfect-matching entropy conjecture | — | — | — | — | yes | yes |
| [120](../theoretical-computer-science/120-almost-linear-time-exact-matching-in-general-graphs.md) | Almost-linear-time exact matching in general graphs | — | — | — | — | — | yes |
| [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures | — | — | — | — | yes | yes |
| [180](../combinatorics/180-barnettes-hamiltonian-cycle-conjecture.md) | Barnette's Hamiltonian-cycle conjecture | — | — | — | — | — | yes |
| [211](../probability-and-statistical-mechanics/211-geometry-diffusion-and-spectra-of-random-planar-maps.md) | Geometry, diffusion, and spectra of random planar maps | — | — | — | — | — | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Hadwigers-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf) |
| [`A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/) | [157](../combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) | prose | [paper.pdf](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf) |
| [`A-quadratic-bound-for-Jacobsthals-function-September-25-2026`](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/) | [021](../number-theory/021-a-quadratic-bound-for-jacobsthals-function.md) | prose | [paper.pdf](../../../preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf) |
| [`An-asymptotic-formula-for-the-number-of-totients-September-25-2026`](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/) | [024](../number-theory/024-an-asymptotic-formula-for-the-number-of-totients.md) | prose | [An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf](../../../preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf) |
| [`Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026`](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/) | [113](../theoretical-computer-science/113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md) | prose | [main.pdf](../../../preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf) |
| [`Positive-lower-density-of-large-prime-gaps-September-25-2026`](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/) | [026](../number-theory/026-positive-lower-density-of-large-prime-gaps.md) | prose | [main.pdf](../../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf) |
| [`Primitive-roots-for-every-admissible-integer-base-October-4-2026`](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/) | [029](../number-theory/029-artins-primitive-root-conjecture-infinitude-for-every-base.md) | prose | [primitive-roots-all-integer-bases.pdf](../../../preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf) |
| [`The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026`](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf) |
| [`The-Quasi-Riemann-Hypothesis-October-5-2026`](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/) | [003](../number-theory/003-quasi-riemann-hypothesis.md) | prose | [paper2.pdf](../../../preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf) |
| [`The-joint-Dickman-law-for-consecutive-integers-September-24-2026`](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/) | [012](../number-theory/012-independent-largest-prime-factors-of-consecutive-integers.md) | prose | [paper.pdf](../../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf) |
| [`Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [024](../number-theory/024-an-asymptotic-formula-for-the-number-of-totients.md) | Ford's inverse-fiber propagation |

## Spelling variants

Every form below normalizes to the key `ford`: accents folded, dash variants unified, possessives stripped, case lowered. `Ford` · `Ford's`

