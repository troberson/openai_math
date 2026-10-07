# Name: weiss

10 families · subject name · 1 carried by a title or a declaration · 10 by prose · 5 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 26 capitalized occurrences, 17 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 0 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 0 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 1 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 10 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 5 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | Torus-packet equidistribution in prime, quartic, and sextic degrees | — | — | — | — | yes | yes |
| [080](../real-and-complex-analysis/080-sobolev-endpoint-in-carlesons-schr-odinger-convergence-problem.md) | The Sobolev endpoint in Carleson's Schr\"odinger convergence problem | — | — | — | — | yes | — |
| [092](../convex-and-metric-geometry/092-optimal-order-of-convex-body-covering-density.md) | The optimal order of convex-body covering density | — | — | — | — | yes | — |
| [152](../dynamical-systems-and-ergodic-theory/152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md) | Zero entropy does not guarantee a smooth positive-volume model | — | — | — | — | yes | yes |
| [197](../algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) | Nonsofic groups and group-ring counterexamples | — | — | — | — | yes | yes |
| [217](../probability-and-statistical-mechanics/217-low-temperature-sherrington-kirkpatrick-fluctuation-law.md) | The low-temperature Sherrington--Kirkpatrick fluctuation law | — | — | yes | — | yes | — |
| [227](../probability-and-statistical-mechanics/227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) | The dynamical phase transition in the Sherrington--Kirkpatrick model | — | — | — | — | yes | — |
| [302](../operator-algebras/302-phillips-toms-formula-for-minimal-integer-actions.md) | The Phillips--Toms formula for minimal integer actions | — | — | — | — | yes | yes |
| [304](../topology/304-hilbert-smith-conjecture-in-every-dimension.md) | The Hilbert--Smith conjecture in every dimension | — | — | — | — | yes | yes |
| [367](../partial-differential-equations/367-critical-dimension-for-the-one-phase-bernoulli-problem.md) | The critical dimension for the one-phase Bernoulli problem | — | — | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026`](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/) | [197](../algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) | prose | [paper.pdf](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf) |
| [`A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026`](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/) | [197](../algebra/197-nonsofic-groups-and-group-ring-counterexamples.md) | prose | [paper.pdf](../../../preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf) |
| [`A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026`](../../../preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/) | [152](../dynamical-systems-and-ergodic-theory/152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md) | prose | [paper.pdf](../../../preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/paper.pdf) |
| [`A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026`](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/) | [092](../convex-and-metric-geometry/092-optimal-order-of-convex-body-covering-density.md) | prose | [paper.pdf](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/paper.pdf) |
| [`Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026`](../../../preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/) | [080](../real-and-complex-analysis/080-sobolev-endpoint-in-carlesons-schr-odinger-convergence-problem.md) | prose | [paper.pdf](../../../preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/paper.pdf) |
| [`Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026`](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/) | [015](../number-theory/015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) | prose | [quartic-torus-packets.pdf](../../../preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf) |
| [`Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026`](../../../preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/) | [302](../operator-algebras/302-phillips-toms-formula-for-minimal-integer-actions.md) | prose | [paper.pdf](../../../preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/paper.pdf) |
| [`Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026`](../../../preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/) | [227](../probability-and-statistical-mechanics/227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) | prose | [paper.pdf](../../../preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/paper.pdf) |
| [`The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026`](../../../preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/) | [304](../topology/304-hilbert-smith-conjecture-in-every-dimension.md) | prose | [paper.pdf](../../../preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/paper.pdf) |
| [`The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026`](../../../preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/) | [367](../partial-differential-equations/367-critical-dimension-for-the-one-phase-bernoulli-problem.md) | prose | [The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf](../../../preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf) |
| [`The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026`](../../../preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/) | [217](../probability-and-statistical-mechanics/217-low-temperature-sherrington-kirkpatrick-fluctuation-law.md) | prose | [The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf](../../../preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

Up to 8 of the statement-environment titles that carry the name, verbatim with accents folded.

| Family | Environment title |
|---|---|
| [217](../probability-and-statistical-mechanics/217-low-temperature-sherrington-kirkpatrick-fluctuation-law.md) | SK--Curie--Weiss fluctuations below unit coupling |

## Spelling variants

Every form below normalizes to the key `weiss`: accents folded, dash variants unified, possessives stripped, case lowered. `Weiss` · `Weiss's`

