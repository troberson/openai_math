[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 278](../index/mathematical-physics/278-failure-of-kohn-sham-ensemble-representation.md)

# 278 — Failure of Kohn–Sham ensemble representation

[Index page](../index/mathematical-physics/278-failure-of-kohn-sham-ensemble-representation.md)

## Original CONTENTS.md summary

[S1:6988] (family entry):

> **278. Failure of Kohn–Sham ensemble representation.** Constructs a three-electron Coulomb molecule with two equal positive-integer-charge nuclei whose absolute ground-state density has no noninteracting ground-state ensemble representation by a single real spin-independent local potential in $`L^{3/2}(\mathbb R^3)+L^\infty(\mathbb R^3)`$. This disproves Kohn–Sham ensemble representability for that potential class; the required nuclear charge is specified nonnumerically.

[S2:647] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript:

**A Coulomb ground-state density without Kohn--Sham ensemble representation** [S3:80–81, S3:82]:

> We construct a finite three-electron Coulomb molecule whose spin-summed
ground-state density cannot be reproduced by any ground-state ensemble
of noninteracting electrons in a single real, spin-independent local
potential in $`L^{3/2}(\mathbf R^3)+L^\infty(\mathbf R^3)`$.
The molecule has two equal positive integer nuclear charges,
specified by an exact finite nonnumerical formula. [S3:83–90]

## Undergraduate summary

**Density functional theory** (DFT) is the workhorse method for computing
the energy of molecules and materials: instead of tracking every
electron, it works from the **electron density** — how the
electrons' charge is spread through space. The central promise of
**Kohn--Sham theory** is that this real, interacting many-electron
density should be reproducible from a *noninteracting* model: a set of
independent electrons moved by a single local potential. This paper
show that promise **fails**: it builds an explicit three-electron
molecule (two identically charged nuclei) whose true ground-state
density **cannot** be reproduced by any such noninteracting model, at
least within the standard class of "nice" potentials [S3:84–89].
The offending nuclear charge is given as an exact formula rather than
a decimal — the counterexample is explicit but not a number you
can just plug in.

## Graduate summary

**A density without Kohn--Sham ensemble representation**
[S3:84–89, S2:647].
There
exists
a
finite
three-electron
Coulomb
molecule
with
two
equal
positive-integer
nuclear
charges,
specified
by
an
exact
finite
nonnumerical
formula,
whose
spin-summed
absolute
ground-state
density
is
not
the
density
of
any
ground-state
ensemble
of
noninteracting
spinful
electrons
in
a
single
real,
spin-independent
local
potential
in
$`L^{3/2}(\mathbb R^3)+L^\infty(\mathbb R^3)`$
[S3:84–89].
The
statement
is
a
negation
over
the
ensemble:
no
probability
mixture
of
noninteracting
ground
states,
no
matter
how
the
weights
are
chosen,
reproduces
the
interacting
density.
The
result
therefore
disproves
Kohn–Sham
ensemble
representability
for
that
potential
class,
for
three-electron
Coulomb
molecules
[S1:6988].

## History of the conjecture

The
Kohn–Sham
theorem
(1965)
guaranteed
that,
for
a
given
interacting
ground-state
density,
there
is
a
noninteracting
potential
reproducing
it
—
but
the
potential
was
shown
to
exist
without
any
regularity
class,
and
later
work
left
open
whether
the
reproducing
potential
can
be
**local**
and
in
a
natural
function
space.
The
question
broadened
from
pure
ground
states
to
**ensembles**
(probability
mixtures),
where
representability
had
been
expected
to
be
more
flexible.
This
manuscript
[S3:84–89]
answers
both
at
once:
an
explicit
three-electron
Coulomb
system
whose
density
resists
every
ensemble
reproduction
by
a
single
spin-independent
local
potential
in
$`L^{3/2}+L^\infty`$,
with
the
charge
given
by
a
closed
nonnumerical
expression
rather
than
a
floored
decimal.

**Prior
(my
training
data,
not
this
repo).**
Kohn–Sham
theory,
the
representability
question,
ensemble
DFT,
and
the
pathologies
of
reproducing
potentials
are
standard
in
density
functional
theory.
The
specific
counterexample
—
a
three-electron,
two-equal-charge
Coulomb
molecule
whose
spin-summed
density
has
no
noninteracting
ensemble
representation
in
the
$`L^{3/2}+L^\infty`$
class,
with
a
nonnumerically
specified
charge
—
is
the
novel
contribution.
I
cannot
confirm
it
independently
from
training
alone.

## Consequences

- **No
  ensemble
  representation**
  [S3:84–89, S2:647]:
  the
  absolute
  ground-state
  density
  of
  the
  constructed
  three-electron
  Coulomb
  molecule
  is
  not
  reproduced
  by
  any
  ground-state
  ensemble
  of
  noninteracting
  electrons
  in
  a
  single
  real
  spin-independent
  local
  potential
  in
  $`L^{3/2}(\mathbb R^3)+L^\infty(\mathbb R^3)`$.
- **Disproof
  for
  the
  potential
  class**
  [S1:6988]:
  Kohn–Sham
  ensemble
  representability
  fails
  for
  that
  potential
  class,
  with
  the
  charge
  fixed
  by
  an
  exact
  nonnumerical
  formula.

## Section skeleton

One
manuscript.
[S3:83–90]
(title
[S3:80–81],
date
[S3:83])
—
`main.tex`
under
`build/`,
with
sections
under
`build/sections/`
(the
Coulomb
setup,
the
channels,
the
angle
spectrum,
the
ensemble
obstruction,
the
plane
obstruction,
the
parameters,
and
the
functional
consequence).
The
family
ships
no
`verification/`
bundle.

## Comparison with the formalized statement

The
release
does
**not**
formalize
this
family.
There
is
no
scope
note
under
`lean/docs/`,
no
comparator
challenge
stub
under
`lean/ComparatorChallenges/`,
and
no
`main_results`
entry
in
`lean/formalization.yaml`
naming
it,
so
no
Lean
statement
—
proved
or
otherwise
—
corresponds
to
the
density
constructed
in
[S3:84–89].
The
ledger
records
`scope_note=0`,
`chal=0`,
and
`mainres=0`
[S4].
The
formalization
gap
is
total:
the
counterexample
exists
only
as
the
manuscript's
LaTeX,
and
nothing
in
the
release
has
stated
it
in
Lean.

## Coverage

The
ledger
row
`fam=278`
[S4]
records
the
tier
and
the
counts:
`tier=T0`,
`paps=1`,
`paps_form=0`,
`chal=0`,
`mainres=0`,
`scope_note=0`,
`verification=0`,
`trace=`.
The
whole
row
is
the
coverage
signature:
no
scope
note,
no
comparator,
no
`main_results`
entry,
and
no
verification
bundle,
so
the
family
sits
entirely
outside
the
release's
checking
workflow.
The
shape
flags
are
`counterexample|density`,
`counterex_broad=1`,
and
`resolves_named=0`
—
the
blurb
states
a
constructed
counterexample
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
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6988] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 278 at [S2:647] |
| S3 | [`preprints/A-Coulomb-Ground-State-Density-without-Kohn-Sham-Ensemble-Representation-September-25-2026/build/main.tex`](../../../preprints/A-Coulomb-Ground-State-Density-without-Kohn-Sham-Ensemble-Representation-September-25-2026/build/main.tex) | 344 | manuscript (single); title [S3:80–81], date [S3:83], abstract [S3:84–89] |
| S4 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=278`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
