[Notes](../../README.md) / [Summaries](README.md) / [Group theory](../index/disciplines/group-theory.md) / [Family 253](../index/group-theory/253-an-infinite-finitely-presented-simple-amenable-group.md)

# 253 — An infinite finitely presented simple amenable group

[Index page](../index/group-theory/253-an-infinite-finitely-presented-simple-amenable-group.md)

## Original CONTENTS.md summary

[S1:6251] (family entry):

> **253. An infinite finitely presented simple amenable group.** Constructs an infinite finitely presented simple amenable group, answering the longstanding question of whether these properties can occur simultaneously. ([Lean](../../../lean/docs/253.md))

[S2:595] carries the `\resultentry`, so the release blurb and the overview agree. The single manuscript:

**An infinite finitely presented simple amenable group** [S3:35, S3:37]:

> "We construct an infinite finitely presented simple amenable group, giving a positive answer to the finite-presentation existence question for simple amenable groups." [S3:41]

## Undergraduate summary

Three properties of groups were long thought to be in tension. A
group is **simple** if it has no nontrivial quotients (no
normal subgroups other than itself and the trivial one). It
is **amenable** if it admits a "fair averaging" process
(informally, it has no wild paradoxical decompositions). And
it is **finitely presented** if it can be described by a
finite list of generators and relations. Infinite finitely
presented groups were known to be simple, and amenable groups
were known to be abundant, but it was an open question
whether a group could be **all three at once**: infinite,
finitely presented, simple, and amenable. The answer is
**yes** — the result constructs such a group
[S3:41, S2:595].

## Graduate summary

**Infinite finitely presented simple amenable group**
[S3:41, S2:595]. There
exists
a
group
$`G`$
that
is
infinite,
finitely
presented,
simple,
and
amenable.
This
gives
a
positive
answer
to
the
finite-presentation
existence
question
for
simple
amenable
groups:
the
three
properties
(infiniteness,
finite
presentation,
simplicity)
together
with
amenability
are
not
mutually
exclusive.

The
formalized
statement
expresses
amenability
by
the
**Følner
condition**:
for
every
finite
subset
$`F`$
of
$`G`$
and
every
$`arepsilon>0`$,
there
is
a
nonempty
finite
subset
$`A`$
of
$`G`$
such
that
$`|Af \setminus A| / |A| < arepsilon`$
for
every
$`f \in F`$.

## History of the conjecture

The
question
of
whether
an
infinite
finitely
presented
simple
amenable
group
exists
was
a
longstanding
open
problem
at
the
intersection
of
geometric
group
theory
and
operator
algebra.
Tarski
(1952)
produced
the
first
infinite
finitely
presented
simple
groups,
but
those
were
nonamenable
(they
contained
a
free
subgroup).
Amenable
groups
like
$`\mathbb Z`$
or
nilpotent
groups
are
never
simple
in
the
finitely
presented
setting
they
arise
in.
The
result
[S3:41]
closes
the
gap
with
an
explicit
construction:
a
single
group
simultaneously
infinite,
finitely
presented,
simple,
and
amenable,
with
amenability
certified
by
the
Følner
condition.

**Prior
(my
training
data,
not
this
repo).**
Infinite
finitely
presented
simple
groups
(Tarski),
amenability,
the
Følner
condition,
and
the
tension
between
simplicity
and
amenability
are
standard.
The
first
construction
of
an
infinite
finitely
presented
simple
amenable
group
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
  existence
  question
  answered
  affirmatively**
  [S3:41]:
  an
  infinite,
  finitely
  presented,
  simple,
  amenable
  group
  exists,
  so
  the
  three
  structural
  properties
  together
  with
  amenability
  are
  compatible.
- **Amenability
  by
  Følner
  condition**
  [S3:41, S4:9]:
  the
  constructed
  group's
  amenability
  is
  certified
  via
  the
  Følner
  condition,
  the
  standard
  criterion
  for
  countable
  groups.

## Section skeleton

One
manuscript:
[S3]
(title
[S3:35],
date
[S3:37])
—
`main.tex`
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
there
is
one
group
that
is
infinite,
finitely
presented,
simple,
and
amenable,
with
amenability
expressed
by
the
Følner
condition.
The
note
excludes
the
paper's
later
general
claims
about
central
kernels
and
enlargements
across
families
[S4:11].

The
`main_results`
entry
[S7:1639–1641]
names
`OAI.SimpleAmenable.main`
in
`lean/OAI/GroupTheory/SimpleAmenable/Main.lean`.
In
the
source,
the
theorem
`main`
is
stated
and
closed
at
[S6:102],
asserting
the
existence
of
a
group
with
the
four
required
properties.
`grep`
finds
**zero**
`sorry`
in
the
whole
`lean/OAI/GroupTheory/SimpleAmenable/`
tree.

The
one
comparator
stub
[S5]
states
the
simple
amenable
group
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
`fam=253`
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
full
existence
claim
(infinite,
finitely
presented,
simple,
amenable
by
Følner).
The
comparator
stub
names
the
same
target,
and
the
proved
copy
lives
under
`lean/OAI/`.
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
empty,
and
`resolves_named=1`
—
the
blurb
names
the
existence
question
with
"answering".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6251] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 253 at [S2:595] |
| S3 | [`preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/build/main.tex`](../../../preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/build/main.tex) | 58 | manuscript 1 of 1; title [S3:35], date [S3:37], abstract [S3:41] |
| S4 | [`lean/docs/253.md`](../../../lean/docs/253.md) | 17 | scope note — the formalization's Scope at [S4:9] and its one comparator link at [S4:17] |
| S5 | [`lean/ComparatorChallenges/SimpleAmenable.lean`](../../../lean/ComparatorChallenges/SimpleAmenable.lean) | 21 | comparator stub — the simple amenable group target with its `sorry` |
| S6 | [`lean/OAI/GroupTheory/SimpleAmenable/Main.lean`](../../../lean/OAI/GroupTheory/SimpleAmenable/Main.lean) | 116 | the formalized file — `main` at [S6:102] |
| S7 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.SimpleAmenable.main`, at [S7:1639–1641] |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=253`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
