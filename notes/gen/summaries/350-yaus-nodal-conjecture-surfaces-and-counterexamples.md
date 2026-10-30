[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 350](../index/differential-geometry/350-yaus-nodal-conjecture-surfaces-and-counterexamples.md)

# 350 — Yau's nodal conjecture: surfaces and counterexamples

[Index page](../index/differential-geometry/350-yaus-nodal-conjecture-surfaces-and-counterexamples.md)

## Original CONTENTS.md summary

[S1:8508] (family entry):

> **350. Yau's nodal bounds: surfaces and higher dimensions.** Proves the sharp $`C\sqrt\lambda`$ upper bound for nodal length on every fixed smooth closed surface, completing Yau's conjecture there. The upper bound fails for fixed smooth metrics in dimensions three and four, including metrics on $`S^3`$ arbitrarily close to round. In dimension five, nodal measure can grow faster than $`\lambda^{1/2+\varepsilon_0}`$ for some fixed $`\varepsilon_0>0`$, ruling out even arbitrarily small power losses.

[S2:800] carries the `\resultentry` with three manuscripts.
Manuscript 1 [S3] (the sharp surface bound), manuscript 2 [S4]
(dimension-3–4 smooth counterexamples), manuscript 3 [S5] (the
dimension-5 power-law violation). The scope note [S6:9] states the
formalized surface result:

> Yau's nodal-set conjecture predicts nodal size of order $`\sqrt\lambda`$ for Laplace eigenfunctions of eigenvalue $`\lambda`$. The formalization proves the upper bound on every fixed smooth closed connected Riemannian surface: there is a surface-dependent constant $`C`$ such that the one-dimensional Hausdorff measure of the zero set of every nonzero real eigenfunction with $`\lambda>0`$ is at most $`C\sqrt\lambda`$. The known lower bound is not part of this selected statement. [S6:9]

## Undergraduate summary

When you pluck a drum, the spots that do not vibrate — the places
where the surface is perfectly still — form a set of **nodal lines**
(for a two-dimensional drum) or, in higher dimensions, nodal
surfaces. As the tone rises (the drum vibrates at a higher
**frequency**, which mathematicians write as a larger eigenvalue
$`\lambda`$), a natural question is: how much nodal area appears?

**Yau's conjecture** (1978) guessed the precise rule: the nodal
area of an eigenfunction of eigenvalue $`\lambda`$ should grow like
$`\sqrt\lambda`$ — no faster, no slower. This is a "sandwich": the
lower bound (at least $`\lambda^{1/4}`$, known since the 1950s–60s for
surfaces) and the upper bound (at most $`C\sqrt\lambda`$).

The three papers here answer the two halves of the sandwich
separately, and the answers are in tension. On **surfaces** (2
dimensions), the upper bound is **true**: the nodal length is at
most $`C\sqrt\lambda`$, completing Yau's conjecture there. But in
**dimensions three and four**, the upper bound is **false** — there
are smooth metrics (one on the 3-sphere, arbitrarily close to round,
and one on $`S^2\times T^2`$) for which the nodal area grows faster
than $`\sqrt\lambda`$. In **dimension five**, the failure is even
sharper: the nodal "volume" can grow faster than
$`\lambda^{1/2+\varepsilon_0}`$ for a fixed positive $`\varepsilon_0`$,
so even a tiny power of headroom is impossible.

## Graduate summary

**Main theorem 1 (surface bound, manuscript 1)** [S3:9–14, S2:800].
On a fixed smooth closed connected Riemannian surface, a nonzero
real Laplace eigenfunction with eigenvalue $`\lambda>0`$ has nodal
length (one-dimensional Hausdorff measure of its zero set) at most
$`C \sqrt{\lambda}`$ for a surface-dependent constant $`C`$. Together
with the known lower bound, this proves Yau's conjecture in this
setting.

**Main theorem 2 (dimensions 3–4, manuscript 2)** [S4:51–54, S2:800].
There is a smooth metric on the three-sphere, arbitrarily close to
the round metric in the smooth topology, and a smooth metric on
$`S^2 \times T^2`$, for which sequences of exact real Laplace
eigenfunctions have unbounded nodal measure divided by the square
root of the eigenvalue. Each sequence belongs to one **fixed**
metric. Thus the upper-bound part of Yau's nodal conjecture fails
for smooth metrics in dimensions three and four.

**Main theorem 3 (dimension 5, manuscript 3)** [S5:74–80, S2:800].
There is a smooth Riemannian metric on $`S^4 \times S^1`$ and a
sequence of real Laplace eigenfunctions whose nodal four-volume grows
faster than $`\lambda^{1/2+\epsilon_0}`$ for one fixed
$`\epsilon_0 > 0`$. This disproves the smooth upper-bound assertion in
Yau's nodal-set conjecture and the proposed bound with an
arbitrarily small positive power loss.

**The two proved formalizations** [S6:11, S6:13, S10, S11].
The scope note selects three statements, but the release proves only
the two **counterexample** results. The surface upper bound
[S6:9] is stated in the comparator stub `NodalLength.lean`
[S7] but carries **no** `main_results` entry — it is an unproved
challenge. The two proved results are: (a) the dimension-3 and
dimension-4 counterexamples [S6:11, S10:1655–1661], formalized as
the declarations `OAI.YauCounterexamples.sphere_three` and
`OAI.YauCounterexamples.sphere_two_torus_two`; and (b) the
dimension-5 counterexample [S6:13, S10:1819–1821], formalized as
`OAI.Yau.Target.yau_nodal_set_upper_bound_counterexample`. Both
proved results live in OAI trees under `lean/OAI/Geometry/`
carrying 0 `sorry`.

## History of the conjecture

The **Yau nodal-set conjecture** originates with Shing-Tung Yau's
1978 paper "On the geometry of the zero set of eigenfunctions of
Riemannian manifolds," which established the $`\lambda^{1/4}`$ lower
bound for nodal length on surfaces and proposed the
$`O(\sqrt{\lambda})`$ upper bound in all dimensions. The lower bound
has since been sharpened and extended; the upper bound was the open
question.

The surface case ($`n=2`$) is a classical result: the $`C\sqrt{\lambda}`$
upper bound for fixed smooth closed surfaces is well known in the
literature (logarithmic improvements over $`\sqrt{\lambda}`$ are known
for special metrics). Manuscript 1 [S3] presents the clean
sharp-$`C\sqrt{\lambda}`$ form, completing the conjecture in 2D.

The **novel contribution** is the higher-dimensional story. The
disproof of the $`O(\sqrt{\lambda})`$ upper bound in dimensions three
and four [S4] — with a metric on $`S^3`$ arbitrarily close to round —
is the genuinely new result, since round $`S^3`$ itself satisfies the
bound (spherical harmonics have bounded nodal ratio). The
dimension-five power-law violation [S5] sharpens the failure: it is
not merely a logarithmic excess but a positive power of $`\lambda`$.

**Prior (my training data, not this repo).** As of my training
cutoff, the $`O(\sqrt{\lambda})`$ upper bound for nodal sets in
dimensions $`n\ge3`$ is a genuine open problem. The known results are
the sharp 2D bound and the $`\lambda^{1/4}`$-type lower bounds. The
construction of smooth metrics with unbounded nodal ratio (the
"wave packet" or "profile" method used across manuscripts 2 and 3)
is the claimed novelty. I cannot verify the spectral-geometry
construction independently from training alone.

## Consequences

- **Yau's conjecture is completed in 2D** [S3:9–14, S2:800]: the
  sharp $`C\sqrt{\lambda}`$ upper bound holds on every fixed smooth
  closed surface.
- **The upper bound fails in dimensions 3 and 4** [S4:51–54,
  S2:800]: there exist smooth metrics — on $`S^3`$ arbitrarily close
  to round, and on $`S^2\times T^2`$ — for which the nodal-to-
  $`\sqrt{\lambda}`$ ratio is unbounded.
- **The failure in dimension 5 is a power law, not a log** [S5:74–80,
  S2:800]: nodal four-volume grows faster than
  $`\lambda^{1/2+\varepsilon_0}`$ for a fixed $`\varepsilon_0>0`$,
  ruling out the "arbitrarily small power loss" variant of the
  conjecture.
- **The metric is fixed in each counterexample** [S4:51–54, S5:74–80]:
  the failure is not a degeneration of the metric but a property of
  one fixed smooth metric's eigenfunction sequence.
- **The two counterexample results are the only proved
  formalizations** [S10:1655–1661, S10:1819–1821, S11]: the
  positive surface result remains an unproved challenge stub
  [S7].

## Section skeleton

Three manuscripts.
Manuscript 1 [S3] (surface bound, `build/paper.tex`, 22 lines): 6
`input` files: `introduction`, `profiles`, `subdivision`, `descent`,
`persistence`, `length`, plus `bibliography`.
Manuscript 2 [S4] (dimensions 3–4, `build/paper.tex`, 68 lines): two
`\part*` blocks — "The three-sphere construction" with 4 `input`
files (`s3-profiles`, `s3-waves`, `s3-exactification`,
`s3-persistence`) and "The $`S^2\times\mathbb T^2`$ construction" with
additional `input` files. A `sections/introduction` prefix.
Manuscript 3 [S5] (dimension 5, `build/main.tex`, 90 lines): 5
`input` files under `sections/`: `introduction`, `framework`,
`envelopes`, `waves`, `global`, plus a BibTeX `references.bib`.
**No verification bundles.**

## Comparison with the formalized statement

The release formalizes this family at tier **T3** with a scope note
[S6:9], three comparator stubs [S7, S8, S9], **two** `main_results`
configs [S10:1655–1661, S10:1819–1821], and **two** proved OAI trees
[S11]. The T3 shape is "scope note, comparator stubs, `main_results`
entries, and proved OAI tree (0 `sorry`)."

The formalization is **asymmetric**: the positive surface result is
unproved, while both counterexample results are proved. The surface
statement [S6:9] — the $`C\sqrt{\lambda}`$ upper bound on fixed
smooth closed surfaces — is carried by the comparator stub
`NodalLength.lean` [S7] (62 lines, `def MainStatement` [S7:44],
`theorem Main` [S7:52] with the `sorry` at [S7:56]) and has **no**
`main_results` entry in `formalization.yaml`. The two proved
results are:

(a) **Dimensions 3–4** [S6:11, S10:1655–1661]. The comparator
`SmoothYau.lean` [S8] (149 lines) states two theorems —
`theorem sphere_three` [S8:132] (the $`S^3`$ counterexample, `sorry`
at [S8:137]) and `theorem sphere_two_torus_two` [S8:139] (the
$`S^2\times T^2`$ counterexample, `sorry` at [S8:142]). Both resolve
to proofs under `lean/OAI/Geometry/SmoothYau/` (436 `.lean`
files): `SphereMetric/ThreeSphere.lean` (23 lines) and
`ProductMetric/SphereProduct.lean` (83 lines).

(b) **Dimension 5** [S6:13, S10:1819–1821]. The comparator
`YauCounterexample.lean` [S9] (72 lines) states
`def MainTarget` [S9:54] and
`theorem yau_nodal_set_upper_bound_counterexample` [S9:65]
(`sorry` at [S9:66]). It resolves to `lean/OAI/Geometry/NodalSets/`
(1068 `.lean` files), entry point `Main.lean` (14 lines) which
decomposes the proof into `sphere_iteration_positive_limit` and
`sphere_persistent_limit_implies_main`.

The two OAI trees together carry 1,504 `.lean` files with 0
`sorry`. The reading is of source text only.

## Coverage

The ledger row `fam=350` [S12] records the tier and the counts:
`tier=T3`, `paps=3`, `paps_form=2`, `chal=3`, `mainres=2`,
`scope_note=1`, `scope_chars=1402`, `verification=0`, `trace=`.
The shape flags are `shapes=counterexample|bound|partial`,
`resolves_named=1`, `counterex_broad=1`, `covmd=0` — a
counterexample family (the upper bound is disproved in dimensions 3–5)
that also carries a bound result (the 2D surface bound), with a
named conjecture (Yau's) and a broad counterexample flag. Note
`paps_form=2`: the two counterexample manuscripts appear in
`formalization.yaml`'s `sources:` list [S10], while the surface
manuscript [S3] does not — its result is stated in a comparator stub
[S7] but has no `main_results` entry, so the per-manuscript
formalized flag for the surface paper stays 0. The two comparator
stubs that have proved OAI trees [S8, S9] together carry 3 `sorry`;
the unproved surface stub [S7] carries 1, for 4 `sorry` across all
three.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:8508] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 350 at [S2:800] |
| S3 | [`preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/build/paper.tex`](../../../preprints/Sharp-nodal-length-on-smooth-surfaces-September-23-2026/build/paper.tex) | 21 | the `\documentclass` root (manuscript 1, surface bound) — title [S3:3], date [S3:5], abstract [S3:9–14] |
| S4 | [`preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/build/paper.tex`](../../../preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/build/paper.tex) | 67 | the `\documentclass` root (manuscript 2, dimensions 3–4) — title [S4:45–46], date [S4:48], abstract [S4:51–54] |
| S5 | [`preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/build/main.tex`](../../../preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/build/main.tex) | 89 | the `\documentclass` root (manuscript 3, dimension 5) — title [S5:69–70], date [S5:72], abstract [S5:74–80] |
| S6 | [`lean/docs/350.md`](../../../lean/docs/350.md) | 23 | scope note — Scope at [S6:9, S6:11, S6:13], comparator links at [S6:19–24] |
| S7 | [`lean/ComparatorChallenges/NodalLength.lean`](../../../lean/ComparatorChallenges/NodalLength.lean) | 62 | comparator stub (surface bound) — 62 lines, 1 `sorry`; **no** `main_results` entry |
| S8 | [`lean/ComparatorChallenges/SmoothYau.lean`](../../../lean/ComparatorChallenges/SmoothYau.lean) | 149 | comparator stub (dimensions 3–4) — 149 lines, 2 `sorry`; **two** proved declarations |
| S9 | [`lean/ComparatorChallenges/YauCounterexample.lean`](../../../lean/ComparatorChallenges/YauCounterexample.lean) | 72 | comparator stub (dimension 5) — 72 lines, 1 `sorry`; **one** proved declaration |
| S10 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entries — SmoothYau at [S10:1655–1661], YauCounterexample at [S10:1819–1821] |
| S11 | [`lean/OAI/Geometry/NodalSets/Main.lean`](../../../lean/OAI/Geometry/NodalSets/Main.lean) | 14 | proved OAI tree entry (dimension 5) — 14 lines, 0 `sorry` |
| S12 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=350`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
