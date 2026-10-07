# Name: thompson

8 families · subject name · 1 carried by a title or a declaration · 8 by prose · 4 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 38 capitalized occurrences, 30 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 8 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 4 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | Saxl's conjecture and universal tensor squares | — | — | — | — | yes | — |
| [248](../group-theory/248-thompsons-group-f-is-nonamenable.md) | Thompson's group $F$ is nonamenable | yes | — | — | yes | yes | yes |
| [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | The Boone--Higman conjecture and higher finiteness | — | — | — | — | yes | yes |
| [251](../group-theory/251-amenability-unitarizability-and-ulam-stability.md) | Amenability, unitarizability, and Ulam stability | — | — | — | — | yes | — |
| [253](../group-theory/253-an-infinite-finitely-presented-simple-amenable-group.md) | An infinite finitely presented simple amenable group | — | — | — | — | yes | — |
| [256](../group-theory/256-howies-conjecture-on-equations-over-groups.md) | Howie's conjecture on equations over groups | — | — | — | — | yes | — |
| [261](../mathematical-physics/261-localization-and-delocalization-in-the-anderson-model.md) | Localization and delocalization in the Anderson model | — | — | — | — | yes | yes |
| [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | Bloch's law and spontaneous ferromagnetic order | — | — | — | — | yes | yes |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026`](../../../preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/) | [261](../mathematical-physics/261-localization-and-delocalization-in-the-anderson-model.md) | prose | [paper.pdf](../../../preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf) |
| [`An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026`](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/) | [253](../group-theory/253-an-infinite-finitely-presented-simple-amenable-group.md) | prose | [paper.pdf](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf) |
| [`Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026`](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/paper.pdf) |
| [`Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026`](../../../preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/) | [256](../group-theory/256-howies-conjecture-on-equations-over-groups.md) | prose | [nonsingular-systems-over-arbitrary-groups.pdf](../../../preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf) |
| [`Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026`](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/) | [250](../group-theory/250-boone-higman-conjecture-and-higher-finiteness.md) | prose | [paper.pdf](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/paper.pdf) |
| [`Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026`](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/) | [251](../group-theory/251-amenability-unitarizability-and-ulam-stability.md) | prose | [strong-ulam-stability.pdf](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf) |
| [`The-Kervaire-Theorem-for-Groups-September-24-2026`](../../../preprints/The-Kervaire-Theorem-for-Groups-September-24-2026/) | [256](../group-theory/256-howies-conjecture-on-equations-over-groups.md) | prose | [The-Kervaire-Theorem-for-Groups-September-24-2026.pdf](../../../preprints/The-Kervaire-Theorem-for-Groups-September-24-2026/The-Kervaire-Theorem-for-Groups-September-24-2026.pdf) |
| [`The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026`](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/) | [271](../mathematical-physics/271-blochs-law-and-spontaneous-ferromagnetic-order.md) | prose | [spherical-magnetization.pdf](../../../preprints/The-spherical-magnetization-law-for-the-three-dimensional-quantum-Heisenberg-ferromagnet-October-5-2026/spherical-magnetization.pdf) |
| [`Thompsons-group-F-is-nonamenable-September-23-2026`](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/) | [248](../group-theory/248-thompsons-group-f-is-nonamenable.md) | prose | [paper.pdf](../../../preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf) |
| [`Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026`](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/) | [205](../algebra/205-saxls-conjecture-and-universal-tensor-squares.md) | prose | [main.pdf](../../../preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/main.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [ThompsonNonamenability](../../../lean/ComparatorChallenges/ThompsonNonamenability.json) | `OAI.ThompsonNonamenability.thompson_F_nonamenable_composition` | [Main.lean](../../../lean/OAI/GroupTheory/Thompson/Main.lean) | [248](../group-theory/248-thompsons-group-f-is-nonamenable.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

Every form below normalizes to the key `thompson`: accents folded, dash variants unified, possessives stripped, case lowered. `Thompson` · `Thompson's`

