# Name: fontaine

8 families · subject name · 2 carried by a title or a declaration · 8 by prose · 6 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 49 capitalized occurrences, 40 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 8 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 6 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [001](../number-theory/001-milnes-rationality-conjecture.md) | Milne's rationality conjecture | — | — | — | — | yes | — |
| [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | The full Birch--Swinnerton-Dyer formula in Selmer coranks zero and one | — | — | — | — | yes | yes |
| [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | Hilbert's tenth problem over $\mathbb Q$ | — | — | — | — | yes | yes |
| [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | Fontaine--Mazur modularity at the prime $2$ and $2$-adic pro-modularity | yes | yes | — | — | yes | yes |
| [030](../number-theory/030-modularity-over-imaginary-quadratic-fields.md) | Modularity over imaginary quadratic fields | — | — | — | — | yes | — |
| [311](../topology/311-chais-invariant-ideal-conjecture.md) | Chai's invariant-ideal conjecture | — | — | yes | — | yes | yes |
| [313](../topology/313-finite-generation-for-the-k-n-local-sphere.md) | Finite generation for the $K(n)$-local sphere | — | — | — | — | yes | yes |
| [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | Chromatic splitting: counterexamples and filtrations | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026`](../../../preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/A-rational-obstruction-to-strong-chromatic-splitting-at-height-three-September-25-2026/paper.pdf) |
| [`Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026`](../../../preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/paper.pdf) |
| [`Filtered-chromatic-splitting-at-generic-primes-September-25-2026`](../../../preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/paper.pdf) |
| [`Finite-generation-for-the-Kn-local-sphere-September-24-2026`](../../../preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/) | [313](../topology/313-finite-generation-for-the-k-n-local-sphere.md) | prose | [Finite-generation-for-the-Kn-local-sphere-September-24-2026.pdf](../../../preprints/Finite-generation-for-the-Kn-local-sphere-September-24-2026/Finite-generation-for-the-Kn-local-sphere-September-24-2026.pdf) |
| [`Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026`](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/) | [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | prose + title | [paper.pdf](../../../preprints/Fontaine-Mazur-modularity-at-the-prime-2-September-23-2026/paper.pdf) |
| [`Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026`](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/) | [004](../number-theory/004-hilberts-tenth-problem-over-q.md) | prose | [main.pdf](../../../preprints/Hilberts-tenth-problem-over-the-rational-numbers-September-24-2026/main.pdf) |
| [`Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026`](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/) | [001](../number-theory/001-milnes-rationality-conjecture.md) | prose | [paper.pdf](../../../preprints/Milnes-rationality-conjecture-for-abelian-varieties-September-23-2026/paper.pdf) |
| [`Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026`](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/) | [030](../number-theory/030-modularity-over-imaginary-quadratic-fields.md) | prose | [paper.pdf](../../../preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026/paper.pdf) |
| [`Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026`](../../../preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/) | [311](../topology/311-chais-invariant-ideal-conjecture.md) | prose | [paper.pdf](../../../preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/paper.pdf) |
| [`The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026`](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/) | [010](../number-theory/010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) | prose | [two-adic-hecke.pdf](../../../preprints/The-Dimension-of-the-Two-Adic-Hecke-Algebra-at-Odd-Level-October-5-2026/two-adic-hecke.pdf) |
| [`The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026`](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/) | [002](../number-theory/002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) | prose | [main.pdf](../../../preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-September-24-2026/main.pdf) |
| [`The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026`](../../../preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/) | [318](../topology/318-chromatic-splitting-counterexamples-and-filtrations.md) | prose | [paper.pdf](../../../preprints/The-height-three-chromatic-overlap-an-explicit-filtration-and-its-attachments-September-27-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [311](../topology/311-chais-invariant-ideal-conjecture.md) | Fargues--Fontaine |
| [311](../topology/311-chais-invariant-ideal-conjecture.md) | Fargues--Fontaine and Le Bras |

## Spelling variants

Every form below normalizes to the key `fontaine`: accents folded, dash variants unified, possessives stripped, case lowered. `Fontaine` · `Fontaine's`

