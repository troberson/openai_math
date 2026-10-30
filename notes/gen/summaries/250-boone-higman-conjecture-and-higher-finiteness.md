[Notes](../../README.md) / [Summaries](README.md) / [Group theory](../index/disciplines/group-theory.md) / [Family 250](../index/group-theory/250-boone-higman-conjecture-and-higher-finiteness.md)

# 250 — The Boone–Higman conjecture and higher finiteness

[Index page](../index/group-theory/250-boone-higman-conjecture-and-higher-finiteness.md)

## Original CONTENTS.md summary

[S1:6176] (family entry):

> **250. Boone–Higman embeddings with higher finiteness.** A finitely generated group has decidable word problem exactly when it embeds in a finitely presented simple group, proving the Boone–Higman conjecture. The target can have type $`F_\infty`$: a classifying space with finitely many cells in each dimension. A single group of type $`F_\infty`$ can also contain every finitely presented group. ([Lean](../../../lean/docs/250.md))

[S2:589] carries the `\resultentry`, so the release blurb and the overview agree.
The three manuscripts:

**Finite algebraic envelopes and the Boone–Higman conjecture** [S3:33, S3:35]:

> We prove the Boone–Higman conjecture. A finitely generated group has
decidable word problem if and only if it embeds in a finitely presented
simple group. [S3:38–42]

**Simple $`F_\infty`$ overgroups** [S4:39–41, S4:42]:

> Every finitely generated group with decidable word problem embeds in a
simple group of type $`F_\infty`$. This resolves the higher-finiteness
strengthening of the Boone–Higman conjecture. [S4:45–49]

**Universal $`F_\infty`$ group** [S5:34, S5:36]:

> We construct a single group of type $`F_\infty`$ containing every finitely
presented group. Its finitely generated subgroups, up to isomorphism, are
exactly the finitely generated recursively presented groups. This answers
the $`F_\infty`$ form of the higher-dimensional Higman embedding question. [S5:50–55]

## Undergraduate summary

The **word problem** for a group asks: given a string of generators,
does it represent the identity? A group has a **decidable** word
problem if there's an algorithm that always answers yes/no in
finite time. The **Boone–Higman conjecture** (1970s) asked:
is a finitely generated group's word problem decidable **if and
only if** the group can be embedded in a finitely presented
simple group? The first manuscript proves this equivalence
[S3:39–41, S2:589]. The second and third manuscripts
strengthen the target: the simple overgroup can have a
**nicer** classifying space (type $`F_\infty`$, meaning finitely
many cells in each dimension) [S4:46–48], and a **single**
group of type $`F_\infty`$ can contain every finitely presented
group [S5:51–54].

## Graduate summary

**Boone–Higman equivalence**
[S3:39–41, S2:589]. A
finitely
generated
group
has
a
decidable
word
problem
for
a
finite
generating
set
if
and
only
if
it
embeds
by
an
injective
homomorphism
into
a
finitely
presented
simple
group.

**Simple
$`F_\infty`$
overgroups**
[S4:46–48,
S2:589].
Every
finitely
generated
group
with
decidable
word
problem
embeds
in
a
simple
group
of
type
$`F_\infty`$:
a
classifying
CW
complex
with
finitely
many
cells
in
each
dimension.
No
additional
finiteness
property
of
the
original
group
is
assumed.

**Universal
$`F_\infty`$
group**
[S5:51–54,
S2:589].
There
exists
a
single
group
$`H`$
of
type
$`F_\infty`$
containing
every
finitely
presented
group.
Its
finitely
generated
subgroups,
up
to
isomorphism,
are
exactly
the
finitely
generated
recursively
presented
groups.
The
group
$`H`$
is
fixed
before
the
embedded
groups
are
chosen.

## History of the conjecture

The
**Boone–Higman
conjecture**
(1970s)
connected
the
computability
of
the
word
problem
with
the
existence
of
a
finitely
presented
simple
overgroup.
The
forward
direction
(undecidable
word
problem
implies
no
embedding
into
a
finitely
presented
simple
group)
was
known
from
Boone
and
Higman.
The
converse
(decidable
word
problem
implies
embedding)
was
the
open
direction.
The
first
manuscript
[S3:39–41]
proves
the
full
equivalence.
The
**higher-finiteness
strengthening**
[S4:46–48]
upgrades
the
target
from
finitely
presented
simple
to
type
$`F_\infty`$
simple,
which
guarantees
a
better-behaved
classifying
space.
The
**universal
group**
[S5:51–54]
goes
further:
one
fixed
group
of
type
$`F_\infty`$
contains
every
finitely
presented
group,
answering
the
$`F_\infty`$
form
of
the
higher-dimensional
Higman
embedding
question.

**Prior
(my
training
data,
not
this
repo).**
The
Boone–Higman
conjecture,
the
Higman
embedding
theorem,
and
the
general
framework
of
finitely
presented
simple
groups
and
type
$`F_\infty`$
groups
are
standard.
The
proof
of
the
full
equivalence,
the
$`F_\infty`$
strengthening,
and
the
universal
group
construction
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
  Boone–Higman
  conjecture
  resolved**
  [S3:39–41]:
  decidable
  word
  problem
  for
  a
  finitely
  generated
  group
  is
  equivalent
  to
  embeddability
  into
  a
  finitely
  presented
  simple
  group.
- **The
  $`F_\infty`$
  strengthening**
  [S4:46–48]:
  the
  simple
  overgroup
  can
  be
  chosen
  of
  type
  $`F_\infty`$.
- **The
  universal
  group**
  [S5:51–54]:
  a
  single
  group
  of
  type
  $`F_\infty`$
  contains
  every
  finitely
  presented
  group,
  with
  its
  finitely
  generated
  subgroups
  exactly
  the
  finitely
  generated
  recursively
  presented
  groups.

## Section skeleton

Three
manuscripts.
[S3:38–42]
(title
[S3:33],
date
[S3:35])
—
`paper.tex`
under
`build/`.
[S4:45–49]
(title
[S4:39–41],
date
[S4:42])
—
`main.tex`
under
`build/`.
[S5:50–55]
(title
[S5:34],
date
[S5:36])
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
[S6],
three
comparator
stubs
[S7]
[S8]
[S9],
and
one
`main_results`
entry
[S11].
The
scope
note
states
three
targets.
The
Boone–Higman
equivalence
[S6:11]:
a
finitely
generated
group
has
a
computable
word
problem
for
a
finite
generating
set
exactly
when
it
embeds
by
an
injective
homomorphism
into
a
finitely
presented
simple
group.
The
higher-finiteness
strengthening
[S6:13]:
every
finitely
generated
group
with
decidable
word
problem
embeds
into
a
nontrivial
simple
group
of
type
$`F_\infty`$.
The
universal
group
[S6:15–17]:
one
group
$`H`$
of
type
$`F_\infty`$
containing
every
finitely
presented
group;
$`H`$
is
fixed
before
the
embedded
groups
are
chosen,
no
word-problem
assumption
is
imposed,
and
the
classifying
space
need
not
be
finite-dimensional
or
have
finitely
many
cells
in
total.
The
paper's
converse
about
recursively
presented
subgroups
is
not
included
[S6:17].

The
`main_results`
entry
[S11:1799–1801]
names
`OAI.UniversalFInfinity.universal_group_of_type_FInfinity`
in
`lean/OAI/GroupTheory/UniversalGroup/Main.lean`.
In
the
source,
the
theorem
`universal_group_of_type_FInfinity`
is
stated
at
[S10:20].
`grep`
finds
**zero**
`sorry`
in
the
whole
`lean/OAI/GroupTheory/UniversalGroup/`
tree.

The
Boone–Higman
equivalence
and
the
simple
$`F_\infty`$
overgroup
targets
have
proved
copies
under
`lean/OAI/GroupTheory/BooneHigman/`
and
`lean/OAI/GroupTheory/SimpleOvergroups/`
respectively
(both
with
**zero**
`sorry`),
but
neither
has
a
`main_results`
registration.
The
three
comparator
stubs
carry
the
targets,
each
with
one
`sorry`:
[S7]
(Boone–Higman
equivalence),
[S8]
(simple
$`F_\infty`$
overgroups),
[S9]
(universal
$`F_\infty`$
group).
Only
the
universal
group
target
has
a
`main_results`
entry.
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
`fam=250`
[S12]
records
the
tier
and
the
counts:
`tier=T3`,
`paps=3`,
`paps_form=1`,
`chal=3`,
`mainres=1`,
`scope_note=1`,
`verification=0`,
`trace=`.
The
`paps_form=1`
against
`paps=3`
is
the
coverage
signature:
one
of
the
three
manuscripts
is
named
as
a
formalization
source
(the
universal
group
paper),
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
universal
$`F_\infty`$
group
construction.
The
Boone–Higman
equivalence
and
the
simple
$`F_\infty`$
overgroup
targets
have
proved
OAI
trees
but
no
`main_results`
registration.
The
three
comparator
stubs
name
all
three
targets;
only
one
has
a
`main_results`
entry.
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
Boone–Higman
conjecture
with
"proving".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6176] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 250 at [S2:589] |
| S3 | [`preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/build/paper.tex`](../../../preprints/Finite-algebraic-envelopes-and-the-Boone-Higman-conjecture-September-23-2026/build/paper.tex) | 60 | manuscript 1 of 3 (Boone-Higman equivalence); title [S3:33], date [S3:35], abstract [S3:39–41] |
| S4 | [`preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/build/main.tex`](../../../preprints/Simple-F-infinity-overgroups-of-groups-with-decidable-word-problem-September-23-2026/build/main.tex) | 62 | manuscript 2 of 3 (simple F-infinity overgroups); title [S4:39–41], date [S4:42], abstract [S4:46–48] |
| S5 | [`preprints/A-universal-group-of-type-F-infinity-September-23-2026/build/main.tex`](../../../preprints/A-universal-group-of-type-F-infinity-September-23-2026/build/main.tex) | 66 | manuscript 3 of 3 (universal F-infinity group); title [S5:34], date [S5:36], abstract [S5:51–54] |
| S6 | [`lean/docs/250.md`](../../../lean/docs/250.md) | 25 | scope note — the Boone-Higman equivalence at [S6:11], the higher-finiteness strengthening at [S6:13], and the universal group at [S6:15–17] |
| S7 | [`lean/ComparatorChallenges/BooneHigman.lean`](../../../lean/ComparatorChallenges/BooneHigman.lean) | 32 | comparator stub — the Boone-Higman equivalence target with its `sorry` |
| S8 | [`lean/ComparatorChallenges/SimpleOvergroups.lean`](../../../lean/ComparatorChallenges/SimpleOvergroups.lean) | 36 | comparator stub — the simple F-infinity overgroup target with its `sorry` |
| S9 | [`lean/ComparatorChallenges/UniversalFInfinity.lean`](../../../lean/ComparatorChallenges/UniversalFInfinity.lean) | 25 | comparator stub — the universal F-infinity group target with its `sorry` |
| S10 | [`lean/OAI/GroupTheory/UniversalGroup/Main.lean`](../../../lean/OAI/GroupTheory/UniversalGroup/Main.lean) | 52 | the formalized file — `universal_group_of_type_FInfinity` at [S10:20] |
| S11 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.UniversalFInfinity.universal_group_of_type_FInfinity`, at [S11:1799–1801] |
| S12 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=250`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
