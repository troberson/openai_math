# Name: anosov

3 families · subject name · 1 carried by a title or a declaration · 3 by prose · 2 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 7 capitalized occurrences, 6 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 3 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 2 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [144](../dynamical-systems-and-ergodic-theory/144-banachs-simple-lebesgue-spectrum-problem.md) | Banach's simple Lebesgue-spectrum problem | — | — | — | — | yes | yes |
| [146](../dynamical-systems-and-ergodic-theory/146-sinais-positive-entropy-conjecture-for-the-standard-map.md) | Sinai's positive-entropy conjecture for the standard map | — | — | — | — | yes | — |
| [339](../differential-geometry/339-katoks-entropy-rigidity-conjecture.md) | Katok's entropy rigidity conjecture | — | — | yes | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026`](../../../preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/) | [144](../dynamical-systems-and-ergodic-theory/144-banachs-simple-lebesgue-spectrum-problem.md) | prose | [paper.pdf](../../../preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf) |
| [`Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026`](../../../preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/) | [339](../differential-geometry/339-katoks-entropy-rigidity-conjecture.md) | prose | [paper.pdf](../../../preprints/Entropy-equality-and-local-symmetry-in-negative-curvature-September-23-2026/paper.pdf) |
| [`Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026`](../../../preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/) | [146](../dynamical-systems-and-ergodic-theory/146-sinais-positive-entropy-conjecture-for-the-standard-map.md) | prose | [paper.pdf](../../../preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [339](../differential-geometry/339-katoks-entropy-rigidity-conjecture.md) | Smoothness of the Anosov splitting |

## Spelling variants

Every form below normalizes to the key `anosov`: accents folded, dash variants unified, possessives stripped, case lowered. `Anosov` · `Anosov's`

