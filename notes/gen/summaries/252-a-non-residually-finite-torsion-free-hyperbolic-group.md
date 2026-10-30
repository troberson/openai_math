[Notes](../../README.md) / [Summaries](README.md) / [Group theory](../index/disciplines/group-theory.md) / [Family 252](../index/group-theory/252-a-non-residually-finite-torsion-free-hyperbolic-group.md)

# 252 — A non-residually-finite torsion-free hyperbolic group

[Index page](../index/group-theory/252-a-non-residually-finite-torsion-free-hyperbolic-group.md)

## Original CONTENTS.md summary

[S1:6235] (family entry):

> **252. A torsion-free hyperbolic group that is neither residually finite nor linear over any field.** Constructs a torsion-free word-hyperbolic group that is not residually finite, answering the residual-finiteness question negatively. One fixed nonidentity element is killed by every finite-dimensional linear representation over every commutative field, so the group is not linear over any such field. ([Lean](../../../lean/docs/252.md))

[S2:593] carries the `\resultentry`, so the release blurb and the overview agree. The single manuscript:

**A torsion-free hyperbolic group that is not residually finite** [S3:42, S3:44]:

> "We construct a torsion-free word-hyperbolic group that is not residually finite, answering the residual-finiteness question for hyperbolic groups negatively." [S3:49]

## Undergraduate summary

A group is **residually finite** if, for every element that is
not the identity, there is some finite quotient of the group
where that element is still visible (not collapsed to the
identity). Intuitively, the group's elements are "separated"
by its finite approximations. Many familiar groups are
residually finite, and it was a long-standing open question
whether **every** hyperbolic group (a broad geometric class
of groups) must be. The answer is **no** — the result
constructs a torsion-free hyperbolic group that is **not**
residually finite [S3:49, S2:593].

## Graduate summary

**Non-residually-finite torsion-free hyperbolic group**
[S3:49, S2:593]. There
exists
a
torsion-free
word-hyperbolic
group
$`G`$
that
is
not
residually
finite:
some
nonidentity
element
of
$`G`$
lies
in
the
kernel
of
every
homomorphism
from
$`G`$
to
a
finite
group.
The
group
is
torsion-free
(no
nontrivial
element
has
finite
order)
and
is
word-hyperbolic
in
the
sense
of
Gromov.

The
CONTENTS.md
entry
adds
a
second
conclusion:
one
fixed
nonidentity
element
is
killed
by
every
finite-dimensional
linear
representation
over
every
commutative
field,
so
the
group
is
not
linear
over
any
such
field
[S1:6235, S2:593].

## History of the conjecture

The
**residual
finiteness
question
for
hyperbolic
groups**
asked
whether
Gromov
hyperbolicity
forces
residual
finiteness.
Residual
finiteness
is
known
for
many
families
of
hyperbolic
groups
(surface
groups,
free
and
free
product
groups,
small
cancellation
groups),
but
a
general
answer
was
open.
The
result
[S3:49]
answers
it
negatively
with
an
explicit
torsion-free
example.
Because
every
finite-dimensional
linear
group
is
residually
finite
over
its
characteristic-
zero
case
and
the
constructed
group
kills
a
fixed
element
under
every
finite-dimensional
representation
[S1:6235],
the
same
construction
also
gives
a
torsion-free
hyperbolic
group
that
is
not
linear
over
any
commutative
field.

**Prior
(my
training
data,
not
this
repo).**
Residual
finiteness,
Gromov
hyperbolicity,
and
the
finiteness
properties
of
hyperbolic
groups
are
standard
in
geometric
group
theory.
The
explicit
torsion-free
hyperbolic
group
that
is
neither
residually
finite
nor
linear
over
any
field
is
the
novel
contribution.
I
cannot
confirm
this
independently
from
training
alone.

## Consequences

- **The
  residual-finiteness
  question
  answered
  negatively**
  [S3:49]:
  a
  torsion-free
  word-hyperbolic
  group
  that
  is
  not
  residually
  finite
  exists.
- **Nonlinearity
  over
  every
  field**
  [S1:6235, S2:593]:
  the
  constructed
  group
  is
  not
  linear
  over
  any
  commutative
  field,
  since
  one
  fixed
  nonidentity
  element
  is
  killed
  by
  every
  finite-dimensional
  representation.

## Section skeleton

One
manuscript:
[S3:48–50]
(title
[S3:42],
date
[S3:44])
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
T3
with
one
scope
note
[S4],
one
comparator
stub
[S5],
and
one
`main_results`
entry
[S7].
The
scope
note
[S4:9]
states
the
target:
a
negative
answer
to
the
residual-finiteness
question
for
hyperbolic
groups,
by
constructing
a
torsion-free
word-hyperbolic
group
that
is
not
residually
finite.
The
note
is
explicit
that
"Nonlinearity
over
every
field
is
not
a
separate
conclusion
of
the
statement
linked
below"
[S4:11]
—
the
formalization
covers
only
the
non-residual-finiteness
claim,
not
the
nonlinearity
over
fields
that
the
CONTENTS.md
blurb
also
states.

The
`main_results`
entry
[S7:1747–1749]
names
`OAI.Release075.main`
in
`lean/OAI/GroupTheory/Hyperbolic/Main.lean`.
In
the
source,
the
theorem
`main`
is
stated
at
[S6:7],
asserting
the
existence
of
a
torsion-free
word-hyperbolic
group
that
is
not
residually
finite.
`grep`
finds
**zero**
`sorry`
in
the
whole
`lean/OAI/GroupTheory/Hyperbolic/`
tree.

The
one
comparator
stub
[S5]
states
the
non-residually-finite
target
and
ends
in
`sorry`.
The
proved
copy
lives
under
`lean/OAI/`.
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
exists,
lives
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
proof.

## Coverage

The
ledger
row
`fam=252`
[S8]
records
the
tier
and
the
counts:
`tier=T3`,
`paps=1`,
`paps_form=1`,
`chal=1`,
`mainres=1`,
`scope_note=1`,
`verification=0`,
`trace=`.
The
`paps_form=1`
against
`paps=1`
is
the
coverage
signature:
the
single
manuscript
is
named
as
a
formalization
source,
and
the
single
`main_results`
entry
over
that
config
reaches
the
non-residual-finiteness
claim.
The
nonlinearity-over-fields
conclusion
carried
by
the
blurb
is
outside
the
formalized
statement,
per
the
scope
note
[S4:11].
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
empty
with
`counterex_broad=1`,
and
`resolves_named=1`
—
the
blurb
names
the
residual-finiteness
question
with
"answering".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6235] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 252 at [S2:593] |
| S3 | [`preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/build/paper.tex`](../../../preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026/build/paper.tex) | 105 | manuscript 1 of 1; title [S3:42], date [S3:44], abstract [S3:49] |
| S4 | [`lean/docs/252.md`](../../../lean/docs/252.md) | 17 | scope note — the formalization's Scope at [S4:9] and its one comparator link at [S4:17] |
| S5 | [`lean/ComparatorChallenges/TorsionFreeHyperbolic.lean`](../../../lean/ComparatorChallenges/TorsionFreeHyperbolic.lean) | 43 | comparator stub — the non-residually-finite target with its `sorry` |
| S6 | [`lean/OAI/GroupTheory/Hyperbolic/Main.lean`](../../../lean/OAI/GroupTheory/Hyperbolic/Main.lean) | 20 | the formalized file — `main` at [S6:7] |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.Release075.main`, at [S7:1747–1749] |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=252`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
