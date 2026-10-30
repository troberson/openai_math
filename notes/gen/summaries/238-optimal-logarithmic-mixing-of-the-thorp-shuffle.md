[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 238](../index/probability-and-statistical-mechanics/238-optimal-logarithmic-mixing-of-the-thorp-shuffle.md)

# 238 — Optimal logarithmic mixing of the Thorp shuffle

[Index page](../index/probability-and-statistical-mechanics/238-optimal-logarithmic-mixing-of-the-thorp-shuffle.md)

## Original CONTENTS.md summary

[S1:5847] (family entry):

> **238. Optimal logarithmic mixing of the Thorp shuffle.** Proves that the Thorp shuffle randomizes $`N=2^d`$ labeled cards in $`\Theta(\log N)`$ physical shuffles, settling its optimal mixing order for power-of-two deck sizes. Convergence is in total variation from the worst initial ordering and concerns the entire permutation, not just individual card positions. ([Lean](../../../lean/docs/238.md))

[S2:561] carries the `\resultentry`, so the release blurb and the overview agree.
The family ships twelve manuscripts; the main paper:

**Optimal-order mixing** [S3:22, S3:24]:

> We prove that the Thorp shuffle on $`2^d`$ cards mixes in $`\Theta(d)`$ complete shuffles. The full permutation law after $`1600d`$ shuffles converges to uniform in total variation as $`d\to\infty`$, uniformly over the initial deck, while a support count gives a lower bound of $`2d-O(1)`$. [S3:27–29]

The remaining eleven build the random coordinate frames, partial-permutation
Fourier bounds, deterministic-sweep information, revealed-switching
permutations, routing and representation contraction, row–column symmetry,
random-subspace trace smoothing, compatibility entropy, signed tensor
densities, conditional sweeps and analytic transfer, and the strict
four-row permanent inequality.

## Undergraduate summary

The **Thorp shuffle** is the way a dealer shuffles a deck: cut the
deck in half, then interleave the two halves one card at a time,
choosing randomly which half each card comes from. **Mixing**
means the shuffle randomizes the deck: after enough shuffles, the
ordering looks essentially uniform. The result proves that
$`\Theta(\log N)`$ physical shuffles suffice to randomize a deck
of $`N=2^d`$ cards, and that $`\Omega(\log N)`$ are
necessary — the Thorp shuffle mixes in
logarithmically many shuffles, which is
**optimal** [S3:27–29, S2:561].

## Graduate summary

**Optimal-order mixing**
[S3:27–29, S2:561]. The Thorp shuffle
on $`2^d`$ cards mixes in
$`\Theta(d)`$ complete
shuffles.
The
full
permutation
law
after
1600d
shuffles
converges
to
uniform
in
total
variation
as
$`d\to\infty`$,
uniformly
over
the
initial
deck,
while
a
support
count
gives
a
lower
bound
of
$`2d-O(1)`$.

## History of the conjecture

The **Thorp shuffle** (also called
the
Faro
shuffle)
was
studied
extensively
in
the
1990s,
and
the
mixing
time
for
individual
cards
or
small
sets
of
cards
was
known.
The
**full-permutation**
mixing
time
—
when
the
entire
ordering
becomes
uniform
—
was
open
for
power-of-two
deck
sizes.
The
result
[S3:27–29]
settles
it:
$`\Theta(\log N)`$
physical
shuffles,
with
a
$`2d-O(1)`$
lower
bound
and
a
$`1600d`$
upper
bound.
The
eleven
supporting
manuscripts
build
the
representation-theoretic
and
Fourier-analytic
machinery:
routing
density
estimates,
spectral
bounds,
signed
moments,
compatibility
entropy,
and
the
strict
four-row
permanent
inequality.

**Prior
(my
training
data,
not
this
repo).**
The
Thorp
shuffle,
the
Faro
shuffle,
and
the
general
framework
of
mixing
times
for
card
shuffles
are
well-known.
The
full-permutation
$`\Theta(\log N)`$
mixing
result
for
power-of-two
decks
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

- **The optimal mixing order**
  [S3:27–29]: the Thorp shuffle
  on $`2^d`$
  cards mixes
  in
  $`\Theta(d)
  =
  \Theta(\log N)`$
  physical
  shuffles,
  for
  the
  full
  permutation
  in
  total
  variation.
- **The upper bound**
  [S3:28]:
  1600d
  shuffles
  suffices.
- **The lower bound**
  [S3:29]:
  $`2d -
  O(1)`$
  shuffles
  are
  necessary.

## Section skeleton

Twelve manuscripts.
[S3:27–29]
(title
[S3:22],
date
[S3:24])
—
`main.tex`
under
`build/`
(the
main
paper,
shipping
as
`paper.pdf`).
The
remaining
eleven
cover
random
coordinate
frames,
partial
permutation
Fourier
bounds,
deterministic
sweep
information,
revealed
switching
permutations,
routing
and
representation
contraction,
row-column
symmetry
and
sweep
contraction,
random
subspace
tests
and
trace
smoothing,
compatibility
entropy
and
spectrum,
signed
tensor
densities
and
diagram
budgets,
conditional
sweeps
and
analytic
transfer,
and
the
strict
four-row
permanent
inequality.
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
thirteen
comparator
stubs,
and
four
`main_results`
entries
[S13].
The
scope
note
[S4:18–61]
states
the
main
target
—
optimal-order
mixing
of
the
Thorp
shuffle
on
$`2^d`$
cards
—
and
nine
routing
estimates,
the
weighted
compatibility
theorem,
the
binary
sweep
contraction,
the
conditional
sweep
moment,
the
signed
tensor
density
estimates,
the
compatibility
entropy
bound,
and
the
strict
four-row
permanent
inequality.
The
paper's
asymptotic
product
conclusion,
the
changed
later
statements,
and
the
full
$`L^2`$
and
total-variation
mixing
conclusion
are
outside
the
selected
estimates.

The
four
`main_results`
entries
[S13]
name:
`OAI.ThorpNine.main`
in
[S9]
(the
nine
routing
estimates),
`OAI.ThorpCompatibility.weightedCompatibility_main`
in
[S10],
`OAI.binary_sweep_contraction_and_mixing`
in
[S11],
and
`OAI.CoordinateSweeps.conditional_main`
in
[S12].
`grep`
finds
**zero**
`sorry`
in
the
`lean/OAI/Probability/ThorpRouting/`,
`ThorpCompatibility/`,
`BinarySweep/`,
and
`CoordinateSweeps/`
trees.

The
thirteen
comparator
stubs
carry
the
targets,
each
with
one
`sorry`:
[S5]
(ThorpRouting),
[S6]
(ThorpWeightedCompatibility),
[S7]
(BinarySweep),
[S8]
(CoordinateSweeps),
and
nine
remaining
stubs
(CoordinateTrace,
FourRowPermanent,
OccupiedOverlap,
PartialPermutation,
SignedSweepMoment,
SpinAngle,
ThorpFirstReciprocal,
ThorpRemaining,
WeightedSweepMoments).
Only
the
four
`main_results`
targets
have
proved
copies
under
`lean/OAI/`;
the
other
nine
targets
are
stubs
without
a
corresponding
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
`fam=238`
[S14]
records
the
tier
and
the
counts:
`tier=T3`,
`paps=12`,
`paps_form=3`,
`chal=13`,
`mainres=4`,
`scope_note=1`,
`verification=0`,
`trace=`.
The
`paps_form=3`
against
`paps=12`
is
the
coverage
signature:
three
of
the
twelve
manuscripts
are
named
as
formalization
sources,
and
the
four
`main_results`
entries
reach
the
routing
estimates,
weighted
compatibility,
binary
sweep
contraction,
and
conditional
sweep
moment
—
the
full
$`\Theta(\log N)`$
mixing
conclusion
and
the
remaining
nine
targets
have
no
`main_results`
registration.
The
thirteen
comparator
stubs
name
all
thirteen
targets,
but
only
four
have
proved
copies.
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
`resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5847] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 238 at [S2:561] |
| S3 | [`preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex`](../../../preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/build/main.tex) | 601 | manuscript 1 of 12 (optimal-order mixing; the main paper); title [S3:22], date [S3:24], abstract [S3:27–29] |
| S4 | [`lean/docs/238.md`](../../../lean/docs/238.md) | 64 | scope note — the formalization's Scope at [S4:18–61] and its thirteen comparator links at [S4:62–64] |
| S5 | [`lean/ComparatorChallenges/ThorpRouting.lean`](../../../lean/ComparatorChallenges/ThorpRouting.lean) | 2579 | comparator stub — the nine routing estimates target with its `sorry` |
| S6 | [`lean/ComparatorChallenges/ThorpWeightedCompatibility.lean`](../../../lean/ComparatorChallenges/ThorpWeightedCompatibility.lean) | 52 | comparator stub — the weighted compatibility target with its `sorry` |
| S7 | [`lean/ComparatorChallenges/BinarySweep.lean`](../../../lean/ComparatorChallenges/BinarySweep.lean) | 102 | comparator stub — the binary sweep contraction target with its `sorry` |
| S8 | [`lean/ComparatorChallenges/CoordinateSweeps.lean`](../../../lean/ComparatorChallenges/CoordinateSweeps.lean) | 314 | comparator stub — the conditional sweep moment target with its `sorry` |
| S9 | [`lean/OAI/Probability/ThorpRouting/Main.lean`](../../../lean/OAI/Probability/ThorpRouting/Main.lean) | 33 | the formalized file — `ThorpNine.main` proved at [S9:13] |
| S10 | [`lean/OAI/Probability/ThorpCompatibility/Main.lean`](../../../lean/OAI/Probability/ThorpCompatibility/Main.lean) | 132 | the formalized file — `weightedCompatibility_main` proved |
| S11 | [`lean/OAI/Probability/BinarySweep/Main.lean`](../../../lean/OAI/Probability/BinarySweep/Main.lean) | 17 | the formalized file — `binary_sweep_contraction_and_mixing` proved |
| S12 | [`lean/OAI/Probability/CoordinateSweeps/Main.lean`](../../../lean/OAI/Probability/CoordinateSweeps/Main.lean) | 464 | the formalized file — `conditional_main` proved |
| S13 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the four `main_results` entries, at [S13:1735–1741] and the BinarySweep / CoordinateSweeps blocks |
| S14 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=238`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
