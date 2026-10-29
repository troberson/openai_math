[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 261](../index/mathematical-physics/261-localization-and-delocalization-in-the-anderson-model.md)

# 261 — Localization and delocalization in the Anderson model

[Index page](../index/mathematical-physics/261-localization-and-delocalization-in-the-anderson-model.md)

## Original CONTENTS.md summary

[S1:6527] (family entry):

> **261. Localization and delocalization in the Anderson model.** Resolves the predicted spectral contrast for the lattice Anderson model with independent uniform site potentials. In dimension two, every positive disorder strength gives almost surely pure-point spectrum. In every fixed dimension $`d \geq 3`$, sufficiently weak positive disorder gives purely absolutely continuous spectrum on a fixed open interval with nonzero spectral weight. ([Lean](../../../lean/docs/261.md))

[S2:613] carries the `\resultentry`, so the release blurb and the overview agree.
The two manuscripts:

**Pure-point spectrum, two-dimensional Anderson model** [S3:45, S3:47]:

> 1

**Absolutely continuous spectrum, weak disorder, $`d \geq 3`$** [S4:35, S4:37]:

> 2

## Undergraduate summary

The **Anderson model** describes a wave (an electron) moving through
a disordered material: you place a random energy at each point of a
lattice (the "disorder") and ask how the wave propagates. The
**spectrum** of the model tells you which energy levels are
available. **Localization** means the wave gets trapped near where
it started (the spectrum is "pure-point" — isolated energy
levels). **Delocalization** means the wave spreads out freely
(the spectrum is "absolutely continuous" — a smooth band of
energies). The two manuscripts prove the predicted contrast
[S1:6527, S2:613]: in **two** dimensions, the spectrum is
pure-point (localized) at **every** positive disorder strength
[S3:51–55]; in **three or more** dimensions, weak disorder
gives absolutely continuous spectrum (delocalized) on a fixed
energy interval [S4:41–47].

## Graduate summary

**Pure-point spectrum in two dimensions**
[S3:51–55, S2:613]. For
each
fixed
positive
disorder
strength
$`h>0`$,
the
nearest-neighbor
Anderson
operator
on
$`\mathbb Z^2`$
with
independent
uniform
site
potentials
on
$`[-h,h]`$
almost
surely
has
pure-point
spectral
type
throughout
its
spectrum.
This
resolves
the
pure-point
assertion
of
the
two-dimensional
Anderson
localization
conjecture
for
the
uniform
single-site
law.

**Absolutely
continuous
spectrum
for
weak
disorder,
$`d \geq 3`$**
[S4:41–47,
S2:613].
For
each
fixed
dimension
$`d \geq 3`$
and
each
fixed
sufficiently
small
positive
disorder
strength,
the
Anderson
operator
on
$`\mathbb Z^d`$
with
independent
uniform
site
potentials
almost
surely
has
purely
absolutely
continuous
spectrum
with
nonzero
weight
on
an
open
energy
interval.
The
interval
may
depend
on
$`d`$
but
is
independent
of
the
disorder
strength.
This
settles
the
purely
absolutely
continuous
energy-range
question
in
Simon's
Problem
1
for
this
model.

## History of the conjecture

The
**Anderson
localization
conjecture**
(Anderson,
1958)
predicted
a
dimension-dependent
contrast
in
the
spectrum
of
disordered
lattice
models:
strong
disorder
or
low
dimension
favors
localization
(pure-point
spectrum),
weak
disorder
or
high
dimension
favors
delocalization
(absolutely
continuous
spectrum).
The
two-dimensional
case
—
the
borderline
dimension
—
was
open
for
the
uniform
single-site
law,
and
the
first
manuscript
[S3:51–55]
resolves
the
pure-point
assertion
there.
The
high-dimensional
absolute
continuity
for
weak
disorder
was
the
content
of
Simon's
Problem
1
in
its
energy-range
form,
and
the
second
manuscript
[S4:41–47]
settles
it
for
every
fixed
$`d \geq 3`$.

**Prior
(my
training
data,
not
this
repo).**
The
Anderson
model,
the
localization/delocalization
contrast,
pure-point
and
absolutely
continuous
spectral
types,
and
Simon's
Problem
1
are
standard
in
random
matrix
and
disordered
systems
theory.
The
full
two-dimensional
pure-point
result
for
the
uniform
single-site
law
at
every
positive
disorder
strength,
and
the
high-dimensional
absolute
continuity
for
weak
disorder
settling
Simon's
Problem
1,
are
the
novel
contributions.
I
cannot
confirm
these
independently
from
training
alone.

## Consequences

- **The
  two-dimensional
  pure-point
  assertion
  resolved**
  [S3:51–55, S2:613]:
  every
  positive
  disorder
  strength
  gives
  almost
  surely
  pure-point
  spectrum
  for
  the
  uniform
  single-site
  law
  on
  $`\mathbb Z^2`$.
- **Simon's
  Problem
  1
  settled**
  [S4:41–47]:
  in
  every
  fixed
  dimension
  $`d \geq 3`$,
  sufficiently
  weak
  positive
  disorder
  gives
  purely
  absolutely
  continuous
  spectrum
  with
  nonzero
  weight
  on
  a
  fixed
  open
  energy
  interval.

## Section skeleton

Two
manuscripts.
[S3]
(title
[S3:45],
date
[S3:47])
—
`paper.tex`
under
`build/`.
[S4]
(title
[S4:35],
date
[S4:37])
—
`paper.tex`
under
`build/`.
The
family
ships
no
`verification/`
bundle.

## Comparison with the formalized statement

The
release
formalises
this
family
at
tier
T2
with
one
scope
note
[S5]
and
one
comparator
stub
[S6],
but
no
`main_results`
entry
[S7].
The
scope
note
links
**only
the
pure-point
manuscript**
[S3]
[S5:5];
the
absolutely
continuous
manuscript
[S4]
is
outside
the
formalization.
The
recorded
scope
[S5:9]
is
a
**supporting
spectral
statement**:
for
every
disorder
strength
$`h>0`$
with
independent
site
potentials
uniform
on
$`[-h,h]`$,
it
constructs
the
bounded
self-adjoint
operator
almost
surely
and
identifies
its
spectrum
as
the
real
interval
$`[-4-h,4+h]`$.
The
scope
note
is
explicit
that
the
selected
statement
"identifies
the
spectral
set"
but
"does
not
assert
the
pure-point
spectral
type
claimed
in
the
accompanying
paper"
[S5:11]
—
the
formalization
proves
the
spectrum
is
the
interval
$`[-4-h,4+h]`$,
not
that
it
is
pure-point.

The
comparator
stub
[S6]
states
`anderson_spectrum_ae`
([S6:26])
and
ends
in
`sorry`.
There
is
no
`main_results`
entry
naming
this
family
[S7],
so
there
is
no
registered
proved
declaration
and
no
OAI
tree
reachable
through
the
yaml.
A
comparator
stub
is
a
target
the
release
set
itself;
the
proved
version,
where
it
exists
and
is
registered,
would
live
under
`lean/OAI/`.
The
reading
is
of
source
text
only
—
no
`lake`
or
`lean`
run
elaborates
the
library.

## Coverage

The
ledger
row
`fam=261`
[S8]
records
the
tier
and
the
counts:
`tier=T2`,
`paps=2`,
`paps_form=0`,
`chal=1`,
`mainres=0`,
`scope_note=1`,
`verification=0`,
`trace=`.
The
`paps_form=0`
against
`paps=2`
is
the
coverage
signature:
the
scope
note
links
only
the
pure-point
manuscript
[S5:5],
and
no
`main_results`
entry
registers
a
proved
declaration
for
either
manuscript,
so
the
formalization
stops
at
the
scope
note
and
the
comparator
stub.
The
absolutely
continuous
manuscript
[S4]
is
entirely
unformalized,
and
even
for
the
linked
pure-point
manuscript
[S3]
the
formalized
statement
is
only
the
supporting
spectral
set
$`[-4-h,4+h]`$
[S5:9],
not
the
pure-point
assertion
[S5:11].
The
single
comparator
stub
[S6]
carries
one
`sorry`.
There
is
no
verification
bundle
and
no
reasoning
trace.
The
shape
flags
are
`resolution|uniform`,
and
`resolves_named=0`
—
the
blurb
states
the
resolution
without
naming
a
conjecture
in
the
resolve
form
the
ledger
flags.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6527] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 261 at [S2:613] |
| S3 | [`preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/paper.tex`](../../../preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/paper.tex) | 69 | manuscript 1 of 2 (pure-point, the one the scope note links); title [S3:45], date [S3:47], abstract [S3:51–55] |
| S4 | [`preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex`](../../../preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/paper.tex) | 61 | manuscript 2 of 2 (absolutely continuous); title [S4:35], date [S4:37], abstract [S4:41–47] |
| S5 | [`lean/docs/261.md`](../../../lean/docs/261.md) | 17 | scope note — links only the pure-point manuscript [S5:5], states the supporting spectral-set scope at [S5:9], notes the pure-point exclusion at [S5:11], and its one comparator link at [S5:17] |
| S6 | [`lean/ComparatorChallenges/PlanarAndersonSpectrum.lean`](../../../lean/ComparatorChallenges/PlanarAndersonSpectrum.lean) | 35 | comparator stub — `anderson_spectrum_ae` at [S6:26] with its `sorry` |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | no `main_results` entry names this family — the yaml carries no Anderson reference |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=261`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
