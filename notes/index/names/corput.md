# Name: corput

5 families · subject name · 1 carried by a title or a declaration · 5 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 8 capitalized occurrences, 6 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 5 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | The Ford--Konyagin--Luca conjecture on prime predecessors | — | — | — | — | yes | — |
| [025](../number-theory/025-erdoss-short-egyptian-fraction-conjecture.md) | Erd\H{o}s’s short Egyptian-fraction conjecture | — | — | — | — | yes | — |
| [145](../dynamical-systems-and-ergodic-theory/145-rokhlins-multiple-mixing-problem.md) | Rokhlin's multiple-mixing problem | — | — | — | — | yes | — |
| [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | Pointwise multiple ergodic averages for mixing transformations | — | — | yes | — | yes | — |
| [158](../combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md) | The Euclidean plane cannot be colored with five colors | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026`](../../../preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/) | [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | prose | [multiple-ergodic-averages.pdf](../../../preprints/Pointwise-Multiple-Ergodic-Averages-for-Mixing-Transformations-October-4-2026/multiple-ergodic-averages.pdf) |
| [`Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026`](../../../preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/) | [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | prose | [fourfold-ergodic-averages.pdf](../../../preprints/Pointwise-convergence-of-fourfold-ergodic-averages-for-mixing-transformations-October-4-2026/fourfold-ergodic-averages.pdf) |
| [`Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026`](../../../preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/) | [145](../dynamical-systems-and-ergodic-theory/145-rokhlins-multiple-mixing-problem.md) | prose | [paper.pdf](../../../preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf) |
| [`Short-Egyptian-fractions-September-25-2026`](../../../preprints/Short-Egyptian-fractions-September-25-2026/) | [025](../number-theory/025-erdoss-short-egyptian-fraction-conjecture.md) | prose | [Short-Egyptian-fractions-September-25-2026.pdf](../../../preprints/Short-Egyptian-fractions-September-25-2026/Short-Egyptian-fractions-September-25-2026.pdf) |
| [`The-Euclidean-plane-is-not-five-colorable-September-23-2026`](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/) | [158](../combinatorics/158-euclidean-plane-cannot-be-colored-with-five-colors.md) | prose | [paper.pdf](../../../preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) |
| [`Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026`](../../../preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/) | [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | prose | [triple-ergodic-distinct-slopes.pdf](../../../preprints/Triple-ergodic-averages-with-distinct-integer-slopes-October-4-2026/triple-ergodic-distinct-slopes.pdf) |
| [`Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026`](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/) | [011](../number-theory/011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) | prose | [paper.pdf](../../../preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [154](../dynamical-systems-and-ergodic-theory/154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) | The Hilbert space van der Corput criterion |

## Spelling variants

One surface form in prose: `Corput`. The normalized key is `corput`.

