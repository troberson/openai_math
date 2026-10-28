[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 092](../index/convex-and-metric-geometry/092-optimal-order-of-convex-body-covering-density.md)

# 092 — The optimal order of convex-body covering density

[Index page](../index/convex-and-metric-geometry/092-optimal-order-of-convex-body-covering-density.md)

## Original CONTENTS.md summary

The release's blurb [S1:2279] and the catalog abstract [S2:260] state
the family's claim: the optimal worst-case covering density is
$\Theta(n\log n)$, for both lattice and unrestricted translative
coverings. The family ships two manuscripts. The single-lattice
manuscript's abstract 

> Every convex body in $\mathbb R^n$, $n\ge2$, admits a covering by translates
along one full-rank lattice with density at most $Cn\log n$, for an absolute
constant $C$. No symmetry or boundary regularity is assumed. [S3:73–77]

## Undergraduate summary

To cover a convex body $K$ in $\mathbb R^n$ by translates means
finding a set of points $X$ such that $K+X$ fills the entire space.
The *density* of a covering measures how many translates are needed per
unit volume. The classical question is: how dense must a covering be,
in the worst case over all convex bodies?

Rogers proved in 1957 that every convex body in dimension $n\ge3$
has a periodic covering of density at most
$n\log n+n\log\log n+5n$ [S6:63–70]. The two manuscripts here
close the loop: one proves the matching upper bound with a *single*
lattice (no cosets) [S4:16–24], and the other constructs
centrally symmetric bodies that *require* density
$c\,n\log n$, matching Rogers' order from below
[S6:49–56]. Together they show the optimal order is
$\Theta(n\log n)$.

## Graduate summary

**The single-lattice bound** [S4:16–24, `thm:main`]. There is an
absolute constant $C>0$ such that, for every integer $n\ge2$ and every
convex body $K\subset\mathbb R^n$, one full-rank lattice $\Lambda$
satisfies

> **Theorem 1.1**
There is an absolute constant $C>0$ such that, for every integer
$n\ge2$ and every convex body $K\subset\mathbb R^n$, one full-rank lattice
$\Lambda$ satisfies
$$K+\Lambda=\mathbb R^n,\qquad
 \frac{\mathrm{vol}_n(K)}{\det\Lambda}\le Cn\log n.$$
No symmetry or boundary regularity is assumed. [S4:16–24]

No symmetry or boundary regularity is assumed; the covering is exact
[K$+$\Lambda$=\mathbb R^n$].

**The translative lower bound** [S6:49–56, `thm:main`]. There
are absolute constants $c>0$ and $n_0$ such that, for every $n\ge n_0$,
some centrally symmetric convex body $K_n\subset\mathbb R^n$
satisfies $\theta_T(K_n)>c\,n\log n$:

> **theorem**
There are absolute constants $c>0$ and $n_0$ such that, for every integer
$n\ge n_0$, some centrally symmetric convex body $K_n\subset\mathbb R^n$
satisfies
$$\theta_T(K_n)>c n\log n.$$ [S6:49–56]

This disproves the existence of a universal *linear* upper bound
[S6:58–61].

**The density definitions.** The translative covering density
$\theta_T(K)$ is the infimum, over all locally finite arrangements
$X$ with $K+X=\mathbb R^n$, of the asymptotic translate count per unit
volume [S6:5–14]. The periodization principle
$\theta_T(K)=\theta_{\mathrm{per}}(K)$ reduces the unrestricted
infimum to periodic coverings [S6:41–44].

## History of the conjecture

Rogers' 1957 upper bound [S6:63–70] gave the first
$O(n\log n)$ estimate. Fejes T\H{o}th sharpened the lower-order term
to $n(\log n+\log\log n+1+o(1))$ using $O(\log n)$ cosets
[S6:79–83]. On the lower-bound side, Coxeter, Few and Rogers gave
an order-$n$ obstruction for equal Euclidean balls, and D\H{u}mer gave
the upper bound $(1/2+o(1))n\log n$ for balls; the gap for bodies that
may also be chosen remained [S6:84–90]. The construction here
builds on the random-slab and Poisson-witness method of Li and Liu
[S6:92–98].

**Prior (my training data, not this repo).** I know Rogers' covering
bound, the Fejes T\H{o}th refinement, and the
Coxeter–Few–Rogers / D\H{u}mer results for Euclidean
balls. A proof that the optimal worst-case covering density over all
convex bodies is exactly $\Theta(n\log n)$, with a single-lattice
upper bound and a centrally symmetric lower-bound construction, is, to
my knowledge, not established in the literature I was trained on. I
cannot independently verify these 2026 manuscripts' arguments.

## Consequences

**$\Theta(n\log n)$ optimal order.** The supremum of covering
density over convex bodies in dimension $n$ is $\Theta(n\log n)$,
for both lattice and unrestricted translative coverings, over all
convex bodies and over centrally symmetric bodies
[S4:16–24, S6:49–56].

**Single-lattice suffices.** The upper bound is attained by a single
full-rank lattice, not a finite union of cosets [S4:16–24].

**No universal linear bound.** There is no absolute $C$ with
$\theta_T(K)\le Cn$ for every convex body in every dimension, even
with central symmetry [S6:58–61].

## Section skeleton

Two manuscripts:

- **single-lattice** [S3:73–77] (title [S3:68], date [S3:70]) — seven
  `.tex` files under `build/` (overview [S4:16–24], preliminaries, sampler,
  blocks, hierarchy, final, references); one figure
  (`figures/suffix-tree.tex`); a thebibliography block in
  `references.tex`.
- **translative** [S5:29–34] (title [S5:24], date [S5:26]) — ten
  `sections/` files (introduction [S6:49–56], construction, localization,
  caps, blocks, poisson, targets, conclusion, encoding,
  periodization); two figures (`figures/residual-cap.tex`,
  `figures/self-matching.tex`); a 12-entry `references.bib` [S12].

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S7:10–12]. The formalization covers two
statements: the single-lattice covering bound (every convex body admits
a single-lattice covering of density $\le Cn\log n$) and the optimal
order of the covering-density suprema (both translative and lattice,
over all and centrally symmetric bodies, are $\Theta(n\log n)$).
The scope note links both manuscripts [S7:5–6] and names two
comparators [S7:16–19]. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library
has not been built here.

**Two comparator stubs, each with a `sorry`.** The single-lattice
bound 

```lean
theorem single_lattice_covering :
    ∃ C : ℝ, 0 < C ∧ ∀ (n : ℕ), 2 ≤ n →
      ∀ (K : Set (Space n)), IsConvexBody K →
        ∃ (L : Submodule ℤ (Space n)) (_ : DiscreteTopology L),
          IsZLattice ℝ L ∧ LatticeCovers K L ∧
            (volume K).toReal / ZLattice.covolume L ≤ C * (n : ℝ) * Real.log (n : ℝ) := by sorry
```
[S8:20–25]

The optimal-order statement 

```lean
def OptimalOrder : Prop :=
  ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∃ n₀ : ℕ, ∀ n : ℕ, n₀ ≤ n →
    orderBounds c C n (translativeSup n) ∧
    orderBounds c C n (symmetricTranslativeSup n) ∧
    orderBounds c C n (latticeSup n) ∧
    orderBounds c C n (symmetricLatticeSup n)

end CoveringOrder

/-- Translative and lattice covering densities over all convex bodies and over
centrally symmetric convex bodies have the same asymptotic order. -/
theorem CoveringOrder.optimal_order : CoveringOrder.OptimalOrder := by
  sorry
```
[S9:102–114]

**The registered entry point.** The `main_results` entry names
`OAI.SingleLatticeCovering.single_lattice_covering` in
`OAI/Geometry/LatticeCovering/Main.lean`, proved at line 25


```lean
theorem single_lattice_covering :
    ∃ C : ℝ, 0 < C ∧ ∀ (n : ℕ), 2 ≤ n →
      ∀ (K : Set (Space n)), IsConvexBody K →
        ∃ (L : Submodule ℤ (Space n)) (_ : DiscreteTopology L),
          IsZLattice ℝ L ∧ LatticeCovers K L ∧
            (volume K).toReal / ZLattice.covolume L ≤ C * (n : ℝ) * Real.log (n : ℝ) := by
  obtain ⟨C,hC,h⟩ := Assembly.eventual_single_lattice_covering
  obtain ⟨C',hC',h'⟩ := FiniteDimensions.absorb_finitely_many_dimensions ⟨C,h⟩
  exact ⟨C',hC',fun n hn K hK => h' n hn K hK.1 hK.2.1 hK.2.2⟩
```
[S10:25–33]

The proof closes by composing `Assembly.eventual_single_lattice_covering`
with `FiniteDimensions.absorb_finitely_many_dimensions`. The
`main_results` entry links the config
`ComparatorChallenges/SingleLatticeCovering.json` to the declaration.

**The optimal-order statement is proven in the OAI tree but not in
`main_results`.** The `CoveringDensity.json` config is **absent** from
`formalization.yaml`, so the optimal-order statement is unregistered.
Nevertheless, the OAI `CoveringDensity/Main.lean` proves
`optimal_order` at line 79 [S11:79–100], composing the
`TranslativeCovering.main` lower bound with
`uniform_lattice_density_upper`:

```lean
theorem optimal_order : OptimalOrder := by
  obtain ⟨c, hc, n₀, hlower⟩ := TranslativeCovering.main
  obtain ⟨C, hC, hupper⟩ := uniform_lattice_density_upper
  refine ⟨c, C, hc, hC, max n₀ 2, ?_⟩
  intro n hn
  have hn₀ : n₀ ≤ n := (le_max_left _ _).trans hn
  have hn₂ : 2 ≤ n := (le_max_right _ _).trans hn
  obtain ⟨K, hK, hsym, hlow⟩ := hlower n hn₀
  let B : Body n := ⟨K, hK⟩
  let S : SymmetricBody n := ⟨B, hsym⟩
  have t_upper (A : Body n) :
      TranslativeCovering.thetaT A.val ≤
        ENNReal.ofReal (C * (n : ℝ) * Real.log (n : ℝ)) :=
    (thetaT_le_thetaL A.property).trans (hupper n hn₂ A.val A.property)
  have l_upper (A : Body n) :
      thetaL A.val ≤ ENNReal.ofReal (C * (n : ℝ) * Real.log (n : ℝ)) :=
    hupper n hn₂ A.val A.property
  have tl : ENNReal.ofReal (c * (n : ℝ) * Real.log (n : ℝ)) ≤
      TranslativeCovering.thetaT K := hlow.le
  have ll : ENNReal.ofReal (c * (n : ℝ) * Real.log (n : ℝ)) ≤ thetaL K :=
    tl.trans (thetaT_le_thetaL hK)
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
```
[S11:79–100]

The OAI `LatticeCovering` tree is 41 files over 25,913 lines with zero
`sorry`; the `CoveringDensity` tree is 3 files over 306 lines; the
`TranslativeCovering` tree is 100 files over 13,879 lines.

## Coverage

T3: the family is partially formalized. The ledger row `fam=092`
records `paps 2`, `paps_form 1`, `tier T3`, `chal 2`, `mainres 1`,
`scope_note 1`, `verification 0`, `trace` empty,
`shapes density|partial`, `resolves_named 0`, `summary 1`. The family
ships two LaTeX manuscripts, a scope note covering both, and two
comparator challenges each carrying one `sorry` theorem; the
`main_results` entry registers the single-lattice bound (proven in a
41-file OAI tree), while the optimal-order statement (proven in a
3-file OAI tree with a 100-file dependency) is unregistered. The family
ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 092 at [S1:2279] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{092} at [S2:260] |
| S3 | [`preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/build/main.tex`](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/build/main.tex) | 85 | single-lattice manuscript root; title [S3:68], date [S3:70], abstract [S3:73–77] |
| S4 | [`preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/build/overview.tex`](../../../preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/build/overview.tex) | 126 | single-lattice main theorem [S4:16–24] |
| S5 | [`preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/paper.tex`](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/paper.tex) | 53 | translative manuscript root; title [S5:24], date [S5:26], abstract [S5:29–34] |
| S6 | [`preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/sections/01-introduction.tex) | 183 | translative introduction; the density definition [S6:5–14], the periodization principle [S6:41–44], the main theorem [S6:49–56], the Rogers bound [S6:63–70] |
| S7 | [`lean/docs/092.md`](../../../lean/docs/092.md) | 19 | the formalization scope note: the two scope paragraphs [S7:10–12] and the comparator table [S7:16–19] |
| S8 | [`lean/ComparatorChallenges/SingleLatticeCovering.lean`](../../../lean/ComparatorChallenges/SingleLatticeCovering.lean) | 29 | comparator stub (single-lattice bound): the theorem [S8:20–24] and the `sorry` [S8:25] |
| S9 | [`lean/ComparatorChallenges/CoveringDensity.lean`](../../../lean/ComparatorChallenges/CoveringDensity.lean) | 116 | comparator stub (optimal order): the `OptimalOrder` def [S9:102–107], the open theorem [S9:113], and the `sorry` [S9:114] |
| S10 | [`lean/OAI/Geometry/LatticeCovering/Main.lean`](../../../lean/OAI/Geometry/LatticeCovering/Main.lean) | 42 | the OAI proven `single_lattice_covering` [S10:25–33] |
| S11 | [`lean/OAI/Geometry/CoveringDensity/Main.lean`](../../../lean/OAI/Geometry/CoveringDensity/Main.lean) | 113 | the OAI proven `optimal_order` [S11:79–100] |
| S12 | [`preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/references.bib`](../../../preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/build/references.bib) | 150 | 12-entry BibTeX bibliography of the translative manuscript |

## Bibliography

- Bukh, Boris, Gao, Jun, Liu, Xizhi, Pikhurko, Oleg, Sun, Shumin, Covering large-dimensional Euclidean spaces by random translates of a given convex body (2025)
- Coxeter, H. S. M., Few, L., Rogers, C. A., Covering space with equal spheres (1959)
- Naszódi, Márton, Flavors of Translative Coverings (2018)
- Dumer, Ilya, Covering spheres with spheres (2007)
- Harris, T. E., A lower bound for the critical probability in a certain percolation process (1960)
- Janson, Svante, Warnke, Lutz, The lower tail: Poisson approximation revisited (2016)
- Janson, Svante, Poisson approximation for large deviations (1990)
- Li, Heng, Liu, Xizhi, Nearly Sharp Bounds for Lattice Coverings by Convex Bodies (2026)
- OpenAI, {A single-lattice covering bound of order $n\log n$} (2026)
- Prosanov, Roman, On a Relation Between Packing and Covering Densities of Convex Bodies (2021)
- Rogers, C. A., A note on coverings (1957)
- Fejes Tóth, Gábor, A note on covering by convex bodies (2009)
