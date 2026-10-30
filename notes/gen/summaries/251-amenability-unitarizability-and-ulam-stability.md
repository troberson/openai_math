[Notes](../../README.md) / [Summaries](README.md) / [Group theory](../index/disciplines/group-theory.md) / [Family 251](../index/group-theory/251-amenability-unitarizability-and-ulam-stability.md)

# 251 — Amenability, unitarizability, and Ulam stability

[Index page](../index/group-theory/251-amenability-unitarizability-and-ulam-stability.md)

## Original CONTENTS.md summary

[S1:6210] (family entry):

> **251. Amenability, unitarizability, and strong Ulam stability.** Resolves Dixmier's problem for all discrete groups: amenability is equivalent to every uniformly bounded Hilbert-space representation being similar to a unitary representation. For countable discrete groups, amenability is also equivalent to strong Ulam stability: sufficiently accurate unitary approximate representations are uniformly close in operator norm to genuine representations on the same, possibly infinite-dimensional, Hilbert space. ([Lean](../../../lean/docs/251.md))

[S2:591] carries the `\resultentry`, so the release blurb and the overview agree.
The two manuscripts:

**Unitarizability implies amenability** [S3:40, S3:42]:

> We prove that a discrete group is amenable if and only if every
uniformly bounded representation on a complex Hilbert space is similar
to a unitary representation. This resolves Dixmier's unitarizability
problem affirmatively for discrete groups. [S4:1–6]

**Strong Ulam stability characterizes amenability** [S5:37, S5:39]:

> A countable discrete group is amenable if and only if it is strongly Ulam
stable: every sufficiently accurate unitary almost representation, on any
complex Hilbert space, is uniformly close in operator norm to a genuine
representation on the same space. We prove the converse to Kazhdan's
amenable stability theorem, answering the question of Burger, Ozawa, and
Thom. The inclusion of infinite-dimensional Hilbert spaces is essential. [S5:42–49]

## Undergraduate summary

A **representation** of a group is a way of turning the group's
elements into matrices (specifically, invertible operators on a
vector space) that respect the group's multiplication. A
representation is **unitary** if the matrices preserve lengths
(unitary operators); it's **uniformly bounded** if no matrix
in the family stretches vectors by more than a fixed factor.
**Unitarizability** asks: can a uniformly bounded
representation be "untwisted" (conjugated by one fixed
invertible operator) into a unitary one? **Amenability** is a
property of groups measuring whether they admit a "fair
averaging" process. The first result shows these two ideas are
the same: a group is amenable **exactly when** every
uniformly bounded representation is unitarizable
[S4:1–6, S2:591]. The second result gives an equivalent
characterization via **Ulam stability**: a group is amenable
exactly when almost-representations are close to genuine
ones [S5:42–49, S2:591].

## Graduate summary

**Dixmier's problem resolved**
[S4:1–6, S2:591]. A
discrete
group
is
amenable
if
and
only
if
every
uniformly
bounded
representation
on
a
complex
Hilbert
space
is
similar
to
a
unitary
representation.
This
resolves
Dixmier's
unitarizability
problem
affirmatively
for
discrete
groups.
For
every
nonamenable
group
and
every
$`arepsilon>0`$,
there
is
a
nonunitarizable
representation
with
uniform
operator
bound
at
most
$`1+arepsilon`$;
the
Hilbert
space
can
be
chosen
separable
for
countable
groups.

**Strong Ulam stability**
[S5:42–49,
S2:591].
A
countable
discrete
group
is
amenable
if
and
only
if
it
is
strongly
Ulam
stable:
every
sufficiently
accurate
unitary
almost
representation,
on
any
complex
Hilbert
space,
is
uniformly
close
in
operator
norm
to
a
genuine
representation
on
the
same
space.
This
is
the
converse
to
Kazhdan's
amenable
stability
theorem,
answering
a
question
of
Burger,
Ozawa,
and
Thom;
the
inclusion
of
infinite-dimensional
Hilbert
spaces
is
essential.

## History of the conjecture

**Dixmier's unitarizability problem** (1950s) asked whether
amenability of a discrete group is equivalent to the
unitarizability of all its uniformly bounded
representations. The amenability-implying-unitarizable
direction was known (amenable groups have invariant means
that average a representation to a unitary one); the
converse — that a nonunitarizable uniformly bounded
representation witnesses nonamenability — was the open
direction. The first manuscript [S4:1–6] proves the full
equivalence, with an effective nonunitarizable witness of
arbitrarily small excess over the unitary bound. The
**strong Ulam stability** result [S5:42–49] is
independent work answering a question of Burger, Ozawa, and
Thom: Ulam stability with approximation on the same,
possibly infinite-dimensional, Hilbert space characterizes
amenability.

**Prior (my training data, not this repo).** Amenability,
unitarizability of representations, Ulam stability, and
Kazhdan's amenable stability theorem are standard in
operator algebra and representation theory. The full
resolution of Dixmier's problem for discrete groups, with
the effective $`1+arepsilon`$ witness, and the strong Ulam
stability characterization (including the infinite-
dimensional case) are the novel contributions. I cannot
confirm these independently from training alone.

## Consequences

- **Dixmier's problem resolved**
  [S4:1–6]: amenability of a discrete group is
  equivalent to the unitarizability of all its uniformly
  bounded Hilbert-space representations; every nonamenable
  group carries a nonunitarizable representation of bound
  at most $`1+arepsilon`$.
- **Strong Ulam stability characterizes amenability**
  [S5:42–49]: for countable discrete groups, amenability
  is equivalent to strong Ulam stability on the same,
  possibly infinite-dimensional, Hilbert space.

## Section skeleton

Two
manuscripts.
[S3]
(title
[S3:40],
date
[S3:42])
—
`main.tex`
under
`build/`
with
`sections/`
(abstract
in
`sections/introduction.tex`).
[S5:42–49]
(title
[S5:37],
date
[S5:39])
—
`strong-ulam-stability.tex`
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
two
comparator
stubs
[S7]
[S8],
and
one
`main_results`
entry
[S10].
The
scope
note
[S6:9–11]
states
the
target:
Dixmier's
unitarizability
problem
—
a
discrete
group
is
amenable
exactly
when
every
uniformly
bounded
Hilbert-space
representation
is
similar
to
a
unitary
one
—
established
for
every
discrete
group,
with
a
nonunitarizable
representation
of
uniform
bound
at
most
$`1+arepsilon`$
for
every
nonamenable
group
and
every
$`arepsilon>0`$.
The
Hilbert
space
can
be
chosen
separable
for
countable
groups;
a
separable
witness
with
uniform
bound
$`101`$
is
recorded
separately
[S6:11].
The
strong
Ulam
stability
manuscript
is
**not**
in
the
formalization's
source
list.

The
`main_results`
entry
[S10:1203–1205]
names
`OAI.Dixmier.current_main_theorem`
in
`lean/OAI/Analysis/Unitarizability/AllDiscrete.lean`.
In
the
source,
the
theorem
`current_main_theorem`
is
stated
and
closed
at
[S9:12].
`grep`
finds
**zero**
`sorry`
in
the
whole
`lean/OAI/Analysis/Unitarizability/`
tree.

The
two
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
(unitarizability
for
all
discrete
groups),
[S8]
(separable
nonunitarizable
witnesses).
Only
the
unitarizability
target
has
a
`main_results`
registration;
the
strong
Ulam
stability
result
has
no
formalization
at
all.
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
`fam=251`
[S11]
records
the
tier
and
the
counts:
`tier=T3`,
`paps=2`,
`paps_form=1`,
`chal=2`,
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
unitarizability
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
Dixmier
equivalence
with
the
$`1+arepsilon`$
witness.
The
strong
Ulam
stability
manuscript
has
no
formalization
—
no
scope-note
source
entry
and
no
OAI
tree.
The
two
comparator
stubs
name
the
unitarizability
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
`resolution|bound|uniform`,
and
`resolves_named=1`
—
the
blurb
names
Dixmier's
problem
with
"Resolves".

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6210] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 251 at [S2:591] |
| S3 | [`preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/build/main.tex`](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/build/main.tex) | 58 | manuscript 1 of 2 (unitarizability); title [S3:40], date [S3:42] |
| S4 | [`preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/build/sections/introduction.tex`](../../../preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/build/sections/introduction.tex) | 209 | the M1 abstract, lines 1–6 |
| S5 | [`preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/build/strong-ulam-stability.tex`](../../../preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/build/strong-ulam-stability.tex) | 1346 | manuscript 2 of 2 (strong Ulam stability); title [S5:37], date [S5:39], abstract [S5:42–49] |
| S6 | [`lean/docs/251.md`](../../../lean/docs/251.md) | 18 | scope note — the formalization's Scope at [S6:9–11] and its two comparator links at [S6:17–18] |
| S7 | [`lean/ComparatorChallenges/DixmierAllDiscrete.lean`](../../../lean/ComparatorChallenges/DixmierAllDiscrete.lean) | 49 | comparator stub — the unitarizability target with its `sorry` |
| S8 | [`lean/ComparatorChallenges/Dixmier.lean`](../../../lean/ComparatorChallenges/Dixmier.lean) | 51 | comparator stub — the separable nonunitarizable witness target with its `sorry` |
| S9 | [`lean/OAI/Analysis/Unitarizability/AllDiscrete.lean`](../../../lean/OAI/Analysis/Unitarizability/AllDiscrete.lean) | 29 | the formalized file — `current_main_theorem` at [S9:12] |
| S10 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming `OAI.Dixmier.current_main_theorem`, at [S10:1203–1205] |
| S11 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=251`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- A. Alpeev, _Lamplighters over non-amenable groups are not strongly Ulam stable_, arXiv:2009.11738 (2020), version 3, 2023.
- M. Burger, N. Ozawa, and A. Thom, _On Ulam stability_, Israel J. Math. **193** (2013), 109–129. doi:10.1007/s11856-012-0050-z.
- H. Furstenberg, _Boundary theory and stochastic processes on homogeneous spaces_, in _Harmonic Analysis on Homogeneous Spaces_, Proc. Sympos. Pure Math. **26**, Amer. Math. Soc., Providence, RI, 1973, 193–229.
- L. Glebsky, A. Lubotzky, N. Monod, and B. Rangarajan, _Asymptotic cohomology and uniform stability for lattices in semisimple groups_, arXiv:2301.00476, version 4 (2023).
- D. Kazhdan, _On $`\varepsilon`$-representations_, Israel J. Math. **43** (1982), no. 4, 315–323. doi:10.1007/BF02761236.
- M. Kalantar and M. Kennedy, _Boundaries of reduced $`C^*`$-algebras of discrete groups_, J. reine angew. Math. **727** (2017), 247–267. doi:10.1515/crelle-2014-0111.
- S. Bravyi and A. Kitaev, _Fermionic quantum computation_, Ann. Physics **298** (2002), no. 1, 210–226. doi:10.1006/aphy.2002.6254.
- F. Fournier-Facio and B. Rangarajan, _Ulam stability of lamplighters and Thompson groups_, Math. Ann. **389** (2024), 2469–2497. doi:10.1007/s00208-023-02708-5.
- Y. Lyubarskii and R. Vershynin, _Uncertainty principles and vector quantization_, IEEE Trans. Inform. Theory **56** (2010), no. 7, 3491–3501. doi:10.1109/TIT.2010.2048458.
- P. Jordan and E. Wigner, _Über das Paulische Äquivalenzverbot_, Z. Phys. **47** (1928), 631–651. doi:10.1007/BF01331938.
