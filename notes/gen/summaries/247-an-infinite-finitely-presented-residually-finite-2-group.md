[Notes](../../README.md) / [Summaries](README.md) / [Group theory](../index/disciplines/group-theory.md) / [Family 247](../index/group-theory/247-an-infinite-finitely-presented-residually-finite-2-group.md)

# 247 — An infinite finitely presented residually finite $2$-group

[Index page](../index/group-theory/247-an-infinite-finitely-presented-residually-finite-2-group.md)

## Original CONTENTS.md summary

[S1:6119] (family entry):

> **247. An infinite finitely presented periodic group and a residually finite 2-group.** Constructs an infinite group with an ordinary finite presentation in which every element has finite order, answering the finitely presented Burnside question negatively. A second manuscript proves that the infinite Steinberg group from the first is residually finite, with a finite-index subgroup whose elements all have finite 2-power order. ([Lean](../../../lean/docs/247.md))

[S2:583] carries the `\resultentry`, so the release blurb and the overview agree.
The two manuscripts:

**Infinite finitely presented periodic group** [S3:43, S3:45]:

> We construct an infinite group with an ordinary finite presentation in
which every element has finite order, answering the finitely presented
Burnside question negatively. We also construct an infinite-dimensional
finitely presented nonunital nil associative algebra over $`\mathbb F_2`$ that is
Jacobson radical but not nilpotent. Its unitization is finitely presented,
algebraic, and infinite-dimensional. These algebras answer the finitely
presented nil- and radical-algebra nilpotence questions and the
finite-presentation version of Kurosh's algebraic finiteness question
negatively. [S3:49–59]

**Residually finite 2-group** [S4:38, S4:40]:

> We prove that the infinite, ordinarily finitely presented periodic
Steinberg group $`\Gamma=\mathrm{St}_{12}(R)`$ of a companion paper is residually
finite. Its finite-index subgroup
$`G=\ker(\Gamma\to\mathrm{St}_{12}(\mathbb F_2))`$ is infinite, ordinarily finitely
presented, and residually finite, and every element of $`G`$ has finite
$`2`$-power order. The orders of its elements are unbounded.
Phases of long words in the companion's graded algebra allow finite
degree truncations to detect all elements of $`\Gamma`$, including the
central kernel. [S4:43–53]

## Undergraduate summary

A **finitely presented group** is a group defined by a finite list
of generators and a finite list of relations. The **Burnside
question** asks: if every element in a finitely presented group
has finite order (meaning each element, raised to some power,
gives the identity), must the group itself be finite? The
answer is **no** — the first manuscript constructs an
infinite finitely presented group where every element has
finite order [S3:49–59, S2:583]. The second manuscript
goes further: it proves that a specific infinite subgroup
is **residually finite** (you can always separate any two
different elements using a finite quotient) and that every
element in it has order a power of 2
[S4:43–53, S2:583].

## Graduate summary

**Infinite finitely presented periodic group**
[S3:49–59, S2:583].
There exists an infinite group with an ordinary finite presentation in
which every element has finite order, answering the finitely presented
Burnside question negatively. The construction also yields an infinite-
dimensional finitely presented nonunital nil associative algebra over
$`\mathbb F_2`$
that is Jacobson radical but not nilpotent.

**Residually finite 2-group**
[S4:43–53, S2:583]. The infinite finitely presented periodic Steinberg
group
$`\Gamma = \mathrm{St}_{12}(R)`$
from the first manuscript is residually finite. Its finite-index
subgroup
$`G = \ker(\Gamma 	o \mathrm{St}_{12}(\mathbb F_2))`$
is infinite, ordinarily finitely presented, residually finite, and every
element of $`G`$ has finite $`2`$-power order, with the orders unbounded.

## History of the conjecture

The **Burnside problem** (1902) originally asked whether a
finitely generated group of bounded exponent is finite.
Magnus (1932) showed the finitely *generated* case has a
negative answer for large exponents. The **finitely presented**
variant — does finite presentation plus periodicity
imply finiteness? — was a more subtle question because
the finite presentation constraint is stronger. The result
[S3:49–59] answers it negatively with an explicit
construction using Steinberg groups over a nil algebra.
The companion [S4:43–53] strengthens the result by
showing the constructed group is residually finite and
that a finite-index subgroup is a 2-group with unbounded
element orders.

**Prior (my training data, not this repo).** The Burnside
problem, its finitely generated resolution by Novikov and
Adyan, and the general framework of finitely presented
groups are standard. The explicit finitely presented periodic
group construction and the residual finiteness of the
2-power-order subgroup are the novel contributions. I
cannot confirm these independently from training alone.

## Consequences

- **The finitely presented
Burnside question answered negatively** [S3:49–59]: an infinite finitely
presented periodic group exists.
- **Residual
finiteness of the 2-group** [S4:43–53]: the finite-index subgroup $`G`$ of
the constructed Steinberg group is residually finite with every element
of finite $`2`$-power order and unbounded orders.

## Section skeleton

Two manuscripts. [S3:49–59] (title [S3:43], date [S3:45]) — `paper.tex` under
`build/` with `sections/`. [S4:43–53] (title [S4:38], date [S4:40]) —
`main.tex` under `build/`. The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T2 with one scope note [S5]
and one comparator stub [S6]. The scope note [S5:9] states the target: a
negative answer to the finitely presented Burnside question by
constructing an infinite finitely presented periodic group, including a
witness realized as a Steinberg group over an algebra of characteristic
two. Periodicity means each element has some finite order; no common
exponent is asserted. The paper's separate nil-algebra and radical-
algebra conclusions are outside the selected statements [S5:9].

There is **no** `main_results` entry and **no** OAI tree: the
formalization is a comparator stub only. The one comparator stub [S6]
states the infinite periodic group target and ends in `sorry`. A
comparator stub is a target the release set itself; the proved version,
where it exists, lives under `lean/OAI/`. Here no proved copy exists.
The reading is of source text only — no `lake` or `lean` run elaborates
the proof.

## Coverage

The ledger row `fam=247` [S7] records the tier and the counts:
`tier=T2`, `paps=2`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `verification=0`, `trace=`. The `paps_form=0` against
`paps=2` is the coverage signature: neither manuscript is named as a
formalization source, and there is no `main_results` entry — the
formalization exists only as a scope note and a comparator stub. There
is no verification bundle and no reasoning trace. The shape flags are
`counterexample`, and `resolves_named=0` — the blurb names the Burnside
question with "answering", a negative answer, not a named-conjecture
resolution.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:6119] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 247 at [S2:583] |
| S3 | [`preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/build/paper.tex`](../../../preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/build/paper.tex) | 312 | manuscript 1 of 2 (infinite finitely presented periodic group); title [S3:43], date [S3:45], abstract [S3:49–59] |
| S4 | [`preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/build/main.tex`](../../../preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/build/main.tex) | 66 | manuscript 2 of 2 (residually finite 2-group); title [S4:38], date [S4:40], abstract [S4:43–53] |
| S5 | [`lean/docs/247.md`](../../../lean/docs/247.md) | 15 | scope note — the formalization's Scope at [S5:9] and its one comparator link at [S5:15] |
| S6 | [`lean/ComparatorChallenges/PeriodicGroup.lean`](../../../lean/ComparatorChallenges/PeriodicGroup.lean) | 56 | comparator stub — the infinite periodic group target with its `sorry` |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=247`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
