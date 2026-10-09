# Name: navier

1 families · subject name · 1 carried by a title or a declaration · 1 by prose · 0 by bibliography author

A name page exists because a **title** layer (a family title in `overview.tex`, a manuscript directory name, the optional title of a statement environment) or a `main_results` **declaration** name carries this name. Those hits make it a subject. The prose and bibliography columns are listed as citation evidence: a body paragraph that mentions a name says the manuscript cites it, not that the result is about it. A name that never reaches a title layer has no page — it is a row in [`../names.tsv`](../names.tsv) with `role = citation`.

Prose counts: 41 capitalized occurrences, 41 of them mid-sentence, 0 lowercase. The mid-sentence count is what separates a surname from an English word; the rule and its measurements live in [`notes/names.md`](../../names.md).

## Provenance by source

| Source | Layer | Families | What a hit means here |
|---|---|---|---|
| `F` — Family title | title | 1 | The release named the family after it — the strongest subject evidence there is. |
| `M` — Manuscript title | title | 1 | A manuscript directory is named after it, so a manuscript takes it as its subject. |
| `E` — Theorem title | title | 0 | A statement environment carries it in its optional title, so a theorem is named for it. |
| `D` — Declaration | declaration | 0 | A `main_results` declaration name contains it, so a formalized statement is named for it. |
| `b` — Body prose | body | 1 | A capitalized occurrence in manuscript prose — a citation, not a statement of subject. |
| `B` — Bib author | body | 0 | An author surname in a shipped `.bib` — a citation, not a statement of subject. |

## Families

| Family | Title | F | M | E | D | b | B |
|---|---|---|---|---|---|---|---|
| [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | Universal computation in forced Navier--Stokes flows | yes | yes | — | — | yes | — |

## Manuscripts

| Dir | Family | Where the name appears | PDF |
|---|---|---|---|
| [`A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026`](../../../preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/manuscript.pdf) |
| [`Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026`](../../../preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose + title | [manuscript.pdf](../../../preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) |
| [`Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026`](../../../preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/manuscript.pdf) |
| [`Geometric-Programs-for-Solenoidal-Forcing-September-27-2026`](../../../preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/manuscript.pdf) |
| [`Incompressible-Box-Transport-and-Finite-Computation-October-6-2026`](../../../preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/manuscript.pdf) |
| [`Incompressible-Box-Transport-and-Finite-Computation-September-27-2026`](../../../preprints/Incompressible-Box-Transport-and-Finite-Computation-September-27-2026/) | — | prose | — |
| [`Prefix-Instructions-and-Incompressible-Flows-September-27-2026`](../../../preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/manuscript.pdf) |
| [`Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026`](../../../preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose | [manuscript.pdf](../../../preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf) |
| [`Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026`](../../../preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose + title | [manuscript.pdf](../../../preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) |
| [`Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026`](../../../preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/) | [376](../partial-differential-equations/376-universal-computation-in-forced-navier-stokes-flows.md) | prose + title | [manuscript.pdf](../../../preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/manuscript.pdf) |

`title` means the name is in the manuscript directory name; `prose` means it appears capitalized in that manuscript's body text with its bibliography stripped. A `prose`-only row is a citation.

## Lean declarations

No `main_results` declaration name contains this name.

## Theorem-environment titles

No statement environment carries this name in its optional title.

## Spelling variants

One surface form in prose: `Navier`. The normalized key is `navier`.

