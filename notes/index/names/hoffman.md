# Name: hoffman

5 families · subject name · 1 carried by a title or a declaration · 4 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 22 capitalized occurrences, 12 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [066](../algebraic-and-complex-geometry/066-bounded-klt-complements-for-fano-contractions.md) | Bounded klt complements for Fano contractions | — | — | — | — | yes | — |
| [212](../probability-and-statistical-mechanics/212-no-bigeodesics-and-smooth-limit-shapes-in-planar-first-passage-percolation.md) | No bigeodesics and smooth limit shapes in planar first-passage percolation | — | — | yes | — | yes | yes |
| [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | Sharp singularity rates for symmetric sign matrices | — | — | — | — | yes | — |
| [266](../mathematical-physics/266-exactly-three-mutually-unbiased-bases-in-dimension-six.md) | Exactly three mutually unbiased bases in dimension six | — | — | — | — | — | yes |
| [354](../differential-geometry/354-isoperimetric-regions-in-the-cubic-three-torus.md) | Isoperimetric regions in the cubic three-torus | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`No-bigeodesics-in-planar-first-passage-percolation-September-24-2026`](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/) | [212](../probability-and-statistical-mechanics/212-no-bigeodesics-and-smooth-limit-shapes-in-planar-first-passage-percolation.md) | prose | [main.pdf](../../../preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf) |
| [`Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026`](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/) | [212](../probability-and-statistical-mechanics/212-no-bigeodesics-and-smooth-limit-shapes-in-planar-first-passage-percolation.md) | prose | [main.pdf](../../../preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf) |
| [`The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026`](../../../preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/) | [354](../differential-geometry/354-isoperimetric-regions-in-the-cubic-three-torus.md) | prose | [article.pdf](../../../preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/article.pdf) |
| [`The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026`](../../../preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/) | [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | prose | [symmetric-bernoulli-singularity.pdf](../../../preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/symmetric-bernoulli-singularity.pdf) |
| [`The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026`](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/) | [239](../probability-and-statistical-mechanics/239-sharp-singularity-rates-for-symmetric-sign-matrices.md) | prose | [biased-symmetric-sign-singularity.pdf](../../../preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/biased-symmetric-sign-singularity.pdf) |
| [`Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026`](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/) | [066](../algebraic-and-complex-geometry/066-bounded-klt-complements-for-fano-contractions.md) | prose | [Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf](../../../preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [212](../probability-and-statistical-mechanics/212-no-bigeodesics-and-smooth-limit-shapes-in-planar-first-passage-percolation.md) | Ahlberg--Hoffman and the shape theorem |

## Spelling variants

Every form below normalizes to the key `hoffman`: accents folded, dash variants unified, possessives stripped, case lowered. `Hoffman` · `Hoffman's`

