[Notes](../../README.md) / [Summaries](README.md) / [Topology](../index/disciplines/topology.md) / [Family 307](../index/topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md)

# 307 — Failure of rational injectivity for maximal coarse assembly

[Index page](../index/topology/307-failure-of-rational-injectivity-for-maximal-coarse-assembly.md)

## Original CONTENTS.md summary

[S1:7587] (family entry):

> **307. Failure of rational injectivity for maximal coarse assembly.** Constructs a uniformly discrete bounded-geometry space whose maximal coarse assembly map is not rationally injective. The example is a coarse disjoint union of finite connected graphs of uniformly bounded degree, with an infinite-order kernel class. A companion gives the analogous failure for reduced coarse assembly, disproving the rational coarse Novikov conjecture. ([Lean](../../../lean/docs/307.md))

[S2:710] carries the `\resultentry` with both manuscripts [S3:3, S3:5, S4:30, S4:32]. The two abstracts:

> We construct a uniformly discrete bounded-geometry space whose maximal coarse
assembly map has an infinite-order element in its kernel. The space is a coarse
disjoint union of finite connected graphs of uniformly bounded degree, so
maximal coarse assembly need not be rationally injective even for such graph
unions. [S3:8–14]

> We disprove the coarse Novikov conjecture: ordinary coarse assembly need not
be rationally injective for uniformly discrete spaces of bounded geometry.
We construct a coarse disjoint union of finite graphs of uniformly bounded
degree and an infinite-order class in its degree-one coarse K-homology whose
image under ordinary coarse assembly in the K-theory of the reduced, locally
compact Roe algebra vanishes. [S4:35–42]

## Undergraduate summary

A **coarse assembly map** is a bridge between the large-scale geometry of a
space and the $`K`$-theory of an algebra encoding that geometry. For a
uniformly discrete space of bounded geometry (think: a graph whose vertices
have a fixed maximum number of neighbors), the map sends coarse
$`K`$-homology classes into the $`K`$-theory of a Roe algebra.

The **coarse Novikov conjecture** predicted that this map should be
**rationally injective** — meaning no nonzero class should vanish after
tensoring with $`\mathbb{Q}`$. Both manuscripts show this is **false**.

Manuscript 2 [S4:35–42] gives the counterexample for **ordinary** coarse
assembly: a coarse disjoint union of finite connected graphs of uniformly
bounded degree, carrying an infinite-order class in its degree-one coarse
$`K`$-homology whose image vanishes in $`K`$-theory of the reduced, locally
compact Roe algebra. The class survives tensoring with $`\mathbb{Q}`$, so
rational injectivity fails.

Manuscript 1 [S3:8–14] extends the failure to **maximal** coarse
assembly — the variant that maps into the maximal Roe algebra. The same
graph-union construction produces an infinite-order element in the kernel
of the maximal assembly map.

## Graduate summary

**Ordinary coarse assembly counterexample (Manuscript 2, formalized)**
[S4:35–42, S2:710].
There exists a uniformly discrete bounded-geometry space $`X`$ — a coarse
disjoint union of finite connected graphs of uniformly bounded degree —
and a class $`[v] \in K_1^{\mathrm{coarse}}(X)`$ of infinite order such
that its image under ordinary coarse assembly
$`\mu: K_1^{\mathrm{coarse}}(X) \to K_1(C^*(X))`$ vanishes, where
$`C^*(X)`$ is the reduced locally compact Roe algebra. Since $`[v]`$ has
infinite order, $`[v] \otimes \mathbb{Q} \neq 0`$, so $`\mu`$ is not
rationally injective.

**Maximal coarse assembly counterexample (Manuscript 1)** [S3:8–14,
S2:710].
The same construction yields a class in the kernel of the maximal coarse
assembly map
$`\mu_{\mathrm{max}}: K_1^{\mathrm{coarse}}(X) \to K_1(C^*_{\max}(X))`$
of infinite order, so maximal coarse assembly is also not rationally
injective for uniformly discrete bounded-geometry graph unions.

**The formalization target.** The release selects the ordinary
coarse-assembly counterexample (Manuscript 2) as its comparator statement
[S5:9] — an infinite-order class in degree-one coarse $`K`$-homology whose
image under ordinary coarse assembly into the reduced locally compact Roe
algebra vanishes — with the non-vanishing after $`\mathbb{Q}`$-tensoring as
the rational-injectivity failure [S5:9].

## History of the conjecture

The coarse Novikov conjecture is the large-scale-geometry analogue of the
classical Novikov conjecture, adapted from the setting of group actions
to the setting of metric spaces. It predicts that the coarse assembly
map should be rationally injective for uniformly discrete spaces of
bounded geometry — the metric counterpart of the topologically
controlled setting where the classical conjecture lives.

The counterexample here uses a coarse disjoint union of finite graphs,
which is a natural bounded-geometry space: each component is finite
hence discrete, and the degree bound gives the coarse control. The
infinite-order class lives in the degree-one coarse $`K`$-homology and
maps to zero in the Roe algebra $`K`$-theory — the rational injectivity
failure follows because the class does not become zero after
$`\mathbb{Q}`$-tensoring. The maximal-assembly variant shows the failure
is not an artifact of the reduced versus maximal Roe algebra
distinction.

**Prior (my training data, not this repo).** The coarse Novikov
conjecture is a well-studied open problem in coarse geometry, with
partial results for spaces with coarse property $`A`$ and for spaces
admitting a uniform embedding into a Hilbert space. A counterexample
using graph unions of uniformly bounded degree, with an explicit
infinite-order kernel class for both the ordinary and maximal assembly
maps, is the novel contribution claimed here; I cannot verify the
coarse-geometric $`K`$-homology constructions independently from training
alone.

## Consequences

- **The coarse Novikov conjecture is disproved** [S4:35–42, S2:710]:
  ordinary coarse assembly is not rationally injective for uniformly
  discrete bounded-geometry spaces. This is the named counterexample the
  ledger's `counterex_broad` and `resolves_named` flags record.
- **Maximal coarse assembly also fails rational injectivity** [S3:8–14,
  S2:710]: the same graph-union construction produces an infinite-order
  kernel element for the maximal assembly map, so the failure is not
  specific to the reduced Roe algebra.
- **The counterexample is a graph union of uniformly bounded degree**
  [S4:37–40, S3:10–12]: the space is a coarse disjoint union of finite
  connected graphs, a class with strong coarse geometric control, so
  the failure occurs even in this well-behaved setting.
- **The kernel class has infinite order** [S4:38–42, S5:9]: the failing
  class survives $`\mathbb{Q}`$-tensoring, so rational injectivity — the
  weakest injectivity statement — is the property that genuinely fails.

## Section skeleton

Two manuscripts. Manuscript 1 [S3:8–14]: root `build/main.tex` (22
lines), sections under `build/sections/`. Manuscript 2 [S4:35–42]: root
`build/main.tex` (56 lines), sections under `build/sections/`. No
verification bundle.

## Comparison with the formalized statement

The release formalizes this family at tier **T2** with a scope note [S5:9]
and one comparator stub [S6]. There is **no** `main_results` entry, and
no proved OAI tree. The T2 shape is "scope note and comparator stubs
exist, but no `main_results` entry and no proved OAI tree."

The scope note [S5:9] selects the ordinary coarse-assembly
counterexample: a coarse disjoint union of finite connected graphs with
uniformly bounded degree, whose degree-one coarse $`K`$-homology contains
an infinite-order class whose image under ordinary coarse assembly into
the reduced locally compact Roe algebra vanishes, and which remains
nonzero after $`\mathbb{Q}`$-tensoring [S5:9].

The single comparator stub carries 1 `sorry`:
`CoarseAssembly.lean` (6648 lines) with
`theorem bounded_geometry_graph_counterexample_unconditional` at
[S6:6629] and the `sorry` at [S6:6641]. No proved copy exists under
`lean/OAI/`. The reading is of source text only.

## Coverage

The ledger row `fam=307` [S7] records the tier and the counts:
`tier=T2`, `paps=2`, `paps_form=0`, `chal=1`, `mainres=0`,
`scope_note=1`, `scope_chars=536`, `verification=0`, `trace=`. The T2
shape is "scope note and comparator stub exist, with no `main_results`
entry." The single comparator stub carries 1 `sorry`. The shape flags
are `shapes=bound|uniform`, `counterex_broad=1`, `resolves_named=1`,
`covmd=1` — a bound/counterexample family recording the failure of
rational injectivity for the coarse assembly maps, with a coverage
document in the manuscript directory.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7587] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 307 at [S2:710] |
| S3 | [`preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/build/main.tex`](../../../preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/build/main.tex) | 22 | manuscript 1 (maximal coarse assembly); title [S3:3], date [S3:5], abstract [S3:8–14] |
| S4 | [`preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/build/main.tex`](../../../preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/build/main.tex) | 56 | manuscript 2 (coarse Novikov conjecture, formalized); title [S4:30], date [S4:32], abstract [S4:35–42] |
| S5 | [`lean/docs/307.md`](../../../lean/docs/307.md) | 15 | scope note — Scope at [S5:9] and the comparator link `CoarseAssembly.lean` |
| S6 | [`lean/ComparatorChallenges/CoarseAssembly.lean`](../../../lean/ComparatorChallenges/CoarseAssembly.lean) | 6648 | comparator stub (formalized target) — 6648 lines, 1 `sorry` |
| S7 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=307`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
