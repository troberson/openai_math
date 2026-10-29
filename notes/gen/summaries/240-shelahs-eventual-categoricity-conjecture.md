[Notes](../../README.md) / [Summaries](README.md) / [Mathematical logic](../index/disciplines/mathematical-logic.md) / [Family 240](../index/mathematical-logic/240-shelahs-eventual-categoricity-conjecture.md)

# 240 — Shelah's eventual categoricity conjecture

[Index page](../index/mathematical-logic/240-shelahs-eventual-categoricity-conjecture.md)

## Original CONTENTS.md summary

[S1:5989] (family entry):

> **240. Shelah's eventual categoricity and the prescribed-threshold obstruction.** Proves Shelah's eventual categoricity conjecture in ZFC: for each bound on the L\"owenheim--Skolem number, a uniform threshold makes categoricity of an abstract elementary class in one cardinal above that threshold imply categoricity throughout the same tail. Categoricity means uniqueness up to isomorphism at a given cardinality. Under the continuum hypothesis, a proposed specific Hanf threshold need not suffice. ([Lean](../../../lean/docs/240.md))

[S2:567] carries the `\resultentry`, so the release blurb and the overview agree.
The two manuscripts:

**Eventual categoricity in ZFC** [S3:59, S3:61]:

> 1

**CH obstruction** [S4:3, S4:5]:

> 2

## Undergraduate summary

An **abstract elementary class** (AEC) is a collection of structures
with a notion of "partial isomorphism" that generalizes elementary
embeddings. **Categoricity** in a cardinal $`\kappa`$ means
there is exactly one structure of size $`\kappa`$ (up to
isomorphism) in the class. **Shelah's eventual
categoricity conjecture** asks: if an AEC is categorical
in one sufficiently large cardinal, is it categorical in
**all** larger cardinals? The answer is **yes**, proved
in ZFC (the standard axioms of set theory)
[S3:64–70, S2:565]. The companion
result shows that a
**specific**
proposed
threshold
is
not
enough
under
the
continuum
hypothesis
[S5:1–7, S2:565].

## Graduate summary

**Eventual categoricity in ZFC**
[S3:64–70, S2:565]. For each bound
$`\kappa_0`$ on the
L\"owenheim--Skolem
number,
there
is
a
uniform
threshold
$`\kappa_1
>
\kappa_0`$
such
that
if
an
AEC
is
categorical
in
some
$`\kappa
\geq
\kappa_1`$,
it
is
categorical
in
every
$`\lambda
\geq
\kappa`$.
The
threshold
depends
only
on
$`\kappa_0`$,
not
on
the
class.

**CH
obstruction**
[S5:1–7,
S2:565].
Assuming
CH,
there
is
an
AEC
in
a
countable
relational
language
with
L\"owenheim--Skolem
number
$`\aleph_0`$
that
is
categorical
in
every
sufficiently
large
cardinal
but
has
at
least
two
nonisomorphic
models
of
cardinality
$`\beth_{\omega_2}`$.
Thus
categoricity
does
not
transfer
down
to
the
proposed
bound
$`\beth_{(2^{\aleph_0})^+}`$,
which
equals
$`\beth_{\omega_2}`$
under
CH.

## History of the conjecture

**Shelah's
eventual
categoricity
conjecture**
(1980s)
asked
whether
categoricity
in
one
large
cardinal
implies
categoricity
in
all
larger
cardinals
for
AECs.
The
result
[S3:64–70]
proves
it
in
ZFC,
with
a
uniform
threshold
depending
only
on
the
L\"owenheim--Skolem
number.
The
**CH
obstruction**
[S5:1–7]
shows
that
the
specific
Hanf
threshold
$`\beth_{(2^{\aleph_0})^+}`$
proposed
in
earlier
work
is
not
sufficient:
under
CH,
an
AEC
can
be
eventually
categorical
but
not
categorical
at
that
specific
cardinal.
This
separates
the
general
existence
theorem
from
any
specific
bound.

**Prior
(my
training
data,
not
this
repo).**
AECs,
the
L\"owenheim--Skolem
number,
categoricity,
and
Shelah's
conjecture
are
standard
model
theory.
The
ZFC
proof
of
eventual
categoricity
with
a
uniform
threshold,
and
the
CH
obstruction
to
the
specific
Hanf
bound,
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

- **Eventual
  categoricity
  in
  ZFC**
  [S3:64–70]:
  categoricity
  in
  one
  sufficiently
  large
  cardinal
  implies
  categoricity
  in
  all
  larger
  cardinals,
  with
  a
  uniform
  threshold
  depending
  only
  on
  the
  L\"owenheim--Skolem
  number.
- **The
  CH
  obstruction**
  [S5:1–7]:
  the
  specific
  Hanf
  threshold
  $`\beth_{(2^{\aleph_0})^+}`$
  is
  not
  sufficient
  under
  CH;
  the
  prescribed-threshold
  form
  of
  Shelah's
  conjecture
  is
  not
  provable
  in
  ZFC.

## Section skeleton

Two
manuscripts.
[S3]
(title
[S3:59],
date
[S3:61])
—
`main.tex`
under
`build/`.
[S4]
(title
[S4:3],
date
[S4:5])
—
`paper.tex`
under
`build/`
with
`sections/`
(abstract
in
`sections/00-introduction.tex`).
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
one
comparator
stub
[S7],
and
one
`main_results`
entry
[S9].
The
scope
note
[S6:9]
states
the
target:
under
CH,
an
AEC
in
a
countable
relational
language
with
L\"owenheim--Skolem
number
$`\aleph_0`$
has
two
nonisomorphic
models
at
$`\beth_{\omega_2} = h(\aleph_0)`$
but
is
categorical
in
every
cardinal
at
least
$`\beth_{(2^{\aleph_1})^+}`$.
The
later
canonical-point
obstruction
and
the
separate
eventual-categoricity
theorem
are
not
included
[S6:11].

The
`main_results`
entry
[S9:1071–1073]
names
`OAI.CHObstruction.main`
in
`lean/OAI/ModelTheory/Categoricity/Main.lean`.
The
source
carries
the
full
construction:
the
Data
structure,
the
tail
threshold,
the
object
and
tail
theorems,
and
the
base/cardinal
comparisons
[S8].
`grep`
finds
**zero**
`sorry`
in
the
whole
`lean/OAI/ModelTheory/Categoricity/`
tree.

The
one
comparator
stub
[S7]
states
the
CH
obstruction
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
`fam=240`
[S10]
records
the
tier
and
the
counts:
`tier=T3`,
`paps=2`,
`paps_form=1`,
`chal=1`,
`mainres=1`,
`scope_note=1`,
`verification=0`,
`trace=`.
The
`paps_form=1`
against
`paps=2`
is
the
coverage
signature:
one
of
the
two
manuscripts
is
named
as
a
formalization
source
(the
CH
obstruction),
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
CH
obstruction
construction
—
the
eventual
categoricity
theorem
itself
is
outside
the
formalization.
The
comparator
stub
names
the
CH
obstruction
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
`resolution`,
and
`resolves_named=1`
—
the
blurb
names
Shelah's
conjecture
with
"Proves".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5989] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 240 at [S2:567] |
| S3 | [`preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/build/main.tex`](../../../preprints/Eventual-Categoricity-for-Abstract-Elementary-Classes-September-24-2026/build/main.tex) | 89 | manuscript 1 of 2 (eventual categoricity in ZFC); title [S3:59], date [S3:61], abstract [S3:64–70] |
| S4 | [`preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/paper.tex`](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/paper.tex) | 20 | manuscript 2 of 2 (CH obstruction); title [S4:3], date [S4:5] |
| S5 | [`preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/sections/00-introduction.tex`](../../../preprints/A-CH-Obstruction-to-a-Prescribed-Categoricity-Threshold-September-24-2026/build/sections/00-introduction.tex) | 204 | the M2 abstract, lines 1–7 |
| S6 | [`lean/docs/240.md`](../../../lean/docs/240.md) | 17 | scope note — the formalization's Scope at [S6:9–11] and its one comparator link at [S6:17] |
| S7 | [`lean/ComparatorChallenges/CHObstruction.lean`](../../../lean/ComparatorChallenges/CHObstruction.lean) | 107 | comparator stub — the CH obstruction target with its `sorry` |
| S8 | [`lean/OAI/ModelTheory/Categoricity/Main.lean`](../../../lean/OAI/ModelTheory/Categoricity/Main.lean) | 270 | the formalized file — the CH obstruction construction proved |
| S9 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.CHObstruction.main`, at [S9:1071–1073] |
| S10 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=240`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
