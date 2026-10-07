# Name: rordam

5 families · subject name · 1 carried by a title or a declaration · 4 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 20 capitalized occurrences, 5 of them mid-sentence, 1 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 1 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 4 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [291](../operator-algebras/291-toms-winter-and-equivariant-jiang-su-stability.md) | Toms--Winter and equivariant Jiang--Su stability | — | — | — | — | yes | — |
| [294](../operator-algebras/294-a-counterexample-to-kaplanskys-quasitrace-conjecture.md) | A counterexample to Kaplansky's quasitrace conjecture | — | — | — | — | yes | — |
| [299](../operator-algebras/299-kirchberg-r-rdam-character-criterion.md) | The Kirchberg--R\o rdam character criterion | — | yes | — | yes | — | — |
| [302](../operator-algebras/302-phillips-toms-formula-for-minimal-integer-actions.md) | The Phillips--Toms formula for minimal integer actions | — | — | — | — | yes | — |
| [303](../operator-algebras/303-from-ordinary-to-strong-pure-infiniteness.md) | From ordinary to strong pure infiniteness | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026`](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/) | [294](../operator-algebras/294-a-counterexample-to-kaplanskys-quasitrace-conjecture.md) | prose | [paper.pdf](../../../preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026/paper.pdf) |
| [`Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026`](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/) | [291](../operator-algebras/291-toms-winter-and-equivariant-jiang-su-stability.md) | prose | [paper.pdf](../../../preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf) |
| [`Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026`](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/) | [291](../operator-algebras/291-toms-winter-and-equivariant-jiang-su-stability.md) | prose | [paper.pdf](../../../preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf) |
| [`Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026`](../../../preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/) | [302](../operator-algebras/302-phillips-toms-formula-for-minimal-integer-actions.md) | prose | [paper.pdf](../../../preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/paper.pdf) |
| [`The-Kirchberg-Rordam-character-criterion-September-25-2026`](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/) | [299](../operator-algebras/299-kirchberg-r-rdam-character-criterion.md) | title | [paper.pdf](../../../preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf) |
| [`Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026`](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/) | [291](../operator-algebras/291-toms-winter-and-equivariant-jiang-su-stability.md) | prose | [paper.pdf](../../../preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf) |
| [`Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026`](../../../preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/) | [303](../operator-algebras/303-from-ordinary-to-strong-pure-infiniteness.md) | prose | [paper.pdf](../../../preprints/Weak-pure-infiniteness-and-O-infinity-absorption-September-25-2026/paper.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

| Config | Declaration | File | Family |
|---|---|---|---|
| [CharacterCriterion](../../../lean/ComparatorChallenges/CharacterCriterion.json) | `OAI.KirchbergRordam.character_criterion` | [Main.lean](../../../lean/OAI/Analysis/CharacterCriterion/Main.lean) | [299](../operator-algebras/299-kirchberg-r-rdam-character-criterion.md) |

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Rordam`. The normalized key is `rordam`.

