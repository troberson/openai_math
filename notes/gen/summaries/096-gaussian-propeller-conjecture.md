[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 096](../index/convex-and-metric-geometry/096-gaussian-propeller-conjecture.md)

# 096 — The Gaussian propeller conjecture

[Index page](../index/convex-and-metric-geometry/096-gaussian-propeller-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:2370] and the catalog abstract [S2:268] state
the family's claim: the sum of squared Gaussian first moments of any
finite measurable partition is at most $9/(8\pi)$, and in dimension
at least two three planar sectors of angle $2\pi/3$ extended
orthogonally attain the bound. The manuscript's abstract


> We prove the Gaussian propeller conjecture: for every finite measurable
partition of a Euclidean space, the sum of the squared lengths of its
Gaussian first moments is at most $9/(8\pi)$.
For dimension at least two and at least three cells, three planar
sectors of angle $2\pi/3$, extended by an orthogonal Euclidean factor,
attain the bound. [S3:37–42]

## Undergraduate summary

Take a finite measurable partition of Euclidean space into regions
$A_1,\ldots,A_k$. Each region has a Gaussian first moment—the
mean of a standard Gaussian measure restricted to that region
[S3:51]. The propeller functional is the sum of the squared lengths
of those first moments. The conjecture, from Khot and Naor's work on
approximate kernel clustering [S3:62–70], asks for the largest
this sum can be, and proposes that the maximizer for
$d\ge2$, $k\ge3$ is a "propeller": three planar sectors meeting at
$120^\circ$ angles, extended by an orthogonal Euclidean factor. The
answer is the universal bound $9/(8\pi)$ [S3:85–86].

## Graduate summary

**The main theorem** [S3:81–92, `thm:main`]. For all positive
integers $d$ and $k$, every measurable partition
$(A_1,\ldots,A_k)$ of $\mathbb R^d$ satisfies

> **theorem**
For all positive integers $d$ and $k$, every measurable partition
$(A_1,\ldots,A_k)$ of $\mathbb R^d$ satisfies
$$\sum_{i=1}^k\left\|\int_{A_i}x\,d\gamma_d(x)\right\|^2
 \le\frac9{8\pi}.$$
Empty cells are allowed. The constant is sharp whenever $d\ge2$ and
$k\ge3$: three planar sectors of angle $2\pi/3$, multiplied by the
orthogonal complement of their plane, attain equality, with any further
cells empty. [S3:81–92]

Empty cells are allowed, and the constant is sharp whenever $d\ge2$
and $k\ge3$ [S3:88–91].

**How the bound is reached.** Khot–Naor determined the
three-cell value and showed a maximizer can be chosen conical in the
span of its centroids [S3:66–70]. Heilman, Jagannath, and Naor
proved the bound in dimension three, their computer-assisted
argument treating the remaining four-cell conical configurations
through spherical geometry [S3:72–75]. The new estimates show
that an extremizer with five or more active cells cannot exceed
$9/(8\pi)$, closing all remaining dimensions [S3:76–79].

## History of the conjecture

The propeller conjecture arises in Khot and Naor's study of
approximate kernel clustering, where Gaussian first moments govern
approximation quality and Unique Games hardness; their formulation
uses $k$ cells in $\mathbb R^{k-1}$ with unused cells permitted
[S3:64–70]. The dimension-three case was settled by Heilman,
Jagannath, and Naor, whose result the manuscript takes as an
established input [S3:72–75].

**Prior (my training data, not this repo).** I know the Khot–Naor
kernel-clustering framework and the role of Gaussian first moments in
it. The assertion that $9/(8\pi)$ is the universal upper bound for
the sum of squared Gaussian first moments over all finite measurable
partitions in every dimension, with the three-sector propeller as the
maximizer, is, to my knowledge, a conjecture that was open in the
literature I was trained on. I cannot independently verify this
manuscript's argument.

## Consequences

**Universal propeller bound.** The sum of squared Gaussian first
moments of any finite measurable partition in any dimension is at
most $9/(8\pi)$ [S3:81–86].

**Sharpness and the maximizer.** For $d\ge2$, $k\ge3$ the bound is
attained by three planar sectors of angle $2\pi/3$ extended by the
orthogonal complement, with any further cells empty
[S3:88–91].

**Kernel-clustering hardness.** Combined with the separate Unique
Games theorem, the bound yields NP-hardness of improving the loss
factor for identity-target kernel clustering at fixed $k\ge3$ on
rational centered positive-semidefinite inputs [S2:268].

## Section skeleton

One manuscript [S3] (title [S3:31], date [S3:33]) — a 300-line
`main.tex` under `build/` plus six `sections/` files (geometry,
scalars, extremizers, elimination, certificates, kernel-application),
two figures (`figures/propeller.tex`, `figures/residual-triangle.tex`),
and a 10-entry `thebibliography` block in `sources/references.tex`.
Total 1,873 lines. The manuscript ships no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalized result proves the sharp bound
$9/(8\pi)$ for every positive dimension and every positive number of
labelled cells, allowing empty cells and arbitrary masses, with
equality attained by the three-sector propeller in dimension at least
two with at least three cells. The scope note **excludes** the
separate Gaussian-maxima and kernel-clustering consequences
[S4:9]. It names one comparator [S4:13–15]. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library
has not been built here.

**The comparator stub** [S5:32–39] states the bound and the
attainment together, with one `sorry`:

```lean
def AllPartitions : Prop :=
  (∀ (d k : ℕ), 0 < d → 0 < k → ∀ A : Fin k → Set (Space d),
    IsPartition A → value A ≤ 9 / (8 * Real.pi)) ∧
  (∀ (d k : ℕ), 2 ≤ d → 3 ≤ k →
    IsPartition (propeller d k) ∧ value (propeller d k) = 9 / (8 * Real.pi))

theorem all_partitions : AllPartitions := by
  sorry
```
[S5:32–39]

**The registered entry point.** The `main_results` entry names
`OAI.GaussianPropeller.all_partitions` in
`OAI/Probability/GaussianPropeller/Main.lean`, proved at line 78


```lean
theorem all_partitions : AllPartitions := by
  constructor
  · intro d k hd hk A hA
    exact Reduction.all_partition_bound d hd k A hA
  · exact Reduction.propeller_attainment
```
[S6:78–82]

The proof discharges the upper bound by `Reduction.all_partition_bound`
and the attainment by `Reduction.propeller_attainment`. The
`main_results` entry links the config
`ComparatorChallenges/GaussianPropeller.json` to the declaration, so
this is the family's headline bound, registered and proven. The OAI
`GaussianPropeller` tree is 47 files over 11,622 lines with zero
`sorry`. The kernel-clustering NP-hardness consequence is a
manuscript claim not carried by the formalization.

## Coverage

T3: the family is formalized. The ledger row `fam=096` records
`paps 1`, `paps_form 1`, `tier T3`, `chal 1`, `mainres 1`,
`scope_note 1`, `verification 0`, `trace` empty,
`shapes bound|partial`, `resolves_named 1`, `summary 1`. The family
ships one 1,873-line LaTeX manuscript, a scope note, one comparator
challenge carrying one `sorry` theorem, and the registered
`main_results` declaration `OAI.GaussianPropeller.all_partitions`,
the bound-attainment headline, proven in the 47-file `GaussianPropeller` OAI
tree. The scope note excludes the kernel-clustering consequence. The
family ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 096 at [S1:2370] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{096} at [S2:268] |
| S3 | [`preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/main.tex`](../../../preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/main.tex) | 300 | the single manuscript; title [S3:31], date [S3:33], abstract [S3:37–42], the conjecture's origin in Khot–Naor [S3:62–70], the Heilman–Jagannath–Naor input [S3:72–79], and the main theorem [S3:81–92] |
| S4 | [`lean/docs/096.md`](../../../lean/docs/096.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/GaussianPropeller.lean`](../../../lean/ComparatorChallenges/GaussianPropeller.lean) | 43 | comparator stub: the `AllPartitions` def [S5:32–36], the `all_partitions` theorem [S5:38], and the `sorry` [S5:39] |
| S6 | [`lean/OAI/Probability/GaussianPropeller/Main.lean`](../../../lean/OAI/Probability/GaussianPropeller/Main.lean) | 114 | the OAI proven `all_partitions` theorem [S6:78–82] |
