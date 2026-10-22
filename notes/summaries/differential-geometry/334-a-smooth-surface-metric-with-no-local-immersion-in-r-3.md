Notes / Summaries / Differential geometry / [Family 334](../../index/differential-geometry/334-a-smooth-surface-metric-with-no-local-immersion-in-r-3.md)

# 334 — A smooth surface metric with no local immersion in $\mathbb R^3$

## Original CONTENTS.md summary

The release's blurb for family 334 [S1:8136]:

> **334. A smooth surface metric with no local isometric immersion in ℝ3.** Constructs a smooth positive-definite metric on $(-1,1)^2$ for which no neighborhood of the origin admits a smooth isometric immersion into ℝ3. This answers the unrestricted smooth local isometric realization problem for surfaces negatively, even after shrinking the neighborhood. ([Lean](../../../lean/docs/334.md))

The catalog abstract in `overview.tex` [S2:766] is the same sentence, and the manuscript's own abstract says the same in the first person [S5:45–50]:

> We construct a smooth positive-definite Riemannian metric on \((-1,1)^2\) that agrees with the Euclidean metric to every order at the origin, yet no neighborhood of the origin admits a smooth isometric immersion into Euclidean three-space. This gives a negative answer to the unrestricted smooth local isometric realization problem for surfaces.

The bibtex key the release ships [S3:9–12]:

> @misc{OAI:A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026,
>   author = {{OpenAI}},
>   title = {{A Smooth Metric with No Local Isometric Immersion into Three-Space}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

The question is local. Near one point, can a surface carrying a given smooth metric be realized as a smooth surface in ordinary three-dimensional space? The manuscript states the question in coordinates [S5:56–59]:

> The local isometric realization problem asks whether a Riemannian surface \((\Sigma,g)\) can, near each point, be realized as a smooth surface in Euclidean three-space. In local coordinates this means finding a smooth map \(F\) with

The answer given is no. The main result is Theorem A [S5:70–78]:

> \begin{maintheorem}
> There is a \(C^\infty\) positive definite Riemannian metric \(g\) on
> \((-1,1)^2\) such that no open neighborhood \(U\) of the origin admits a
> \(C^\infty\) isometric immersion
> \[
> F:(U,g)\longrightarrow\R^3.
> \]
> In particular, no such neighborhood admits a smooth isometric embedding.
> \end{maintheorem}

Two things make the example sharp. First, the metric is not singular at the base point. It agrees with the Euclidean metric to every order there, so no finite set of derivatives at the origin distinguishes it from the flat plane. The manuscript states this as a corollary [S9:250–261]:

> \begin{corollary}[Euclidean Taylor jet]\label{cor:flat-jet}
> The metric in Theorem~A can be chosen so that, in the coordinates
> \(X,Y\),
> \[
> \partial^\alpha(g_{ij}-\delta_{ij})(0)=0
> \qquad
> \text{for every multi-index }\alpha\in\mathbb N_0^2
> \text{ and }i,j\in\{1,2\}.
> \]
> Thus smooth local isometric realizability is not determined by
> the full Taylor jet of the metric at the base point.
> \end{corollary}

Second, the obstruction is not a curvature sign. The construction uses both signs, and the manuscript states plainly that it leaves the sign-restricted versions open [S5:115–118]:

> In Theorem~A, positive definiteness refers to the metric, not its curvature: the construction uses both signs of curvature. It does not settle the smooth local-realizability problem under either sign restriction \(K\ge0\) or \(K\le0\).

The proof runs through a scalar equation. Any smooth isometric immersion into three-space has a height function in a fixed ambient direction, and that height must satisfy one second-order relation. The manuscript sets out the two tasks [S5:134–143]:

> The proof has two tasks: obstruct a scalar height on an entire fixed square, and construct a metric for which any local immersion would produce such a height on one of those squares. The scalar equation is the Darboux equation. It follows from the Gauss equation because the component of an immersion in a fixed ambient direction has covariant Hessian equal to a scalar multiple of the second fundamental form. We use only this necessary condition for an immersion. The patch argument excludes heights with gradient norm below one, a nonzero diagonal entry of the covariant Hessian, and a mixed entry small relative to that diagonal entry.

So the argument is: find a metric for which the height equation has no solution on a whole square, then build a metric whose every local immersion would produce such a height.

## Graduate summary

The model geometry is a square with a prescribed curvature profile. The background metric has curvature $\kappa(x^2-h(y))$, where $h$ equals 1 near the center, is positive outside, and vanishes at $y=\pm1$ [S6:8–29]. The perturbation set $\mathcal U$ is the set of smooth symmetric tensors supported in $[-1/10,1/10]^2$ whose resulting metric is positive and strongly negative on $[-1/5,1/5]^2$ [S6:24–43].

An admissible height is the class the obstruction targets [S6:52–57]:

> An \emph{admissible height}
> for \(g\) is a function \(z\), smooth on a neighborhood of the closed square \(S\), satisfying throughout~\(S\)
> \begin{equation}\label{eq:admissible}
> H_{xx}H_{yy}-H_{xy}^2=KE,\qquad
> E>0,\qquad H_{yy}\ne0,\qquad \abs q\le1/100.
> \end{equation}

The link from an immersion to that equation is one lemma [S6:62–72]:

> \begin{lemma}[Height equation]\label{lem:height}
> Let \(F\) be a smooth isometric immersion of a surface into \(\R^3\),
> let \(e\) be a fixed ambient unit vector, and set \(z=\langle F,e\rangle\).
> Then
> \[
> \det(\nabla_g^2z)=K\det(g)(1-\abs{dz}_g^2).
> \]
> If \(e\) is normal to the immersed surface at a point \(b\), then
> \(dz(b)=0\) and \(\nabla_g^2z(b)=\II(b)\), with the choice of unit
> normal equal to \(e\) at \(b\).
> \end{lemma}

The manuscript is explicit that it uses only the necessary direction [S6:83–84]:

> Only this necessary equation for a height is used. We do not need the converse reconstruction of an immersion from a Darboux solution.

The analytic obstruction is a category statement [S6:86–91]:

> \begin{proposition}[Patch obstruction]\label{prop:patch}
> The metrics in \(\mathcal U\) admitting no admissible height form
> a residual subset of \(\mathcal U\). In particular, for every
> \(C^\infty\) neighborhood of \(g_0\) in \(\mathcal U\), there is
> a metric in that neighborhood with no admissible height.
> \end{proposition}

The square-wide quantification is what makes this an obstruction rather than a local existence failure [S6:93–94]:

> The whole-square requirement is essential. Every curvature zero in \(S\) of a metric in \(\mathcal U\) is a clean change of sign. Indeed,

Every curvature zero in the square is a clean change of sign, so the pointwise local-existence theorems recalled in the introduction remain compatible with the proposition: they give heights locally, not one height on all of $S$ [S6:93–100].

The cap estimate is the analytic core. A cap is a region with three edges in positive curvature and one artificial edge that may cut through negative curvature [S5:161–172]:

> For the model curvature used here, the main analytic ingredient is a uniform regularity estimate for Darboux heights on a _cap_: a region with three edges in positive curvature and a fourth, artificial edge that may cut through negative curvature. Starting from fixed low-order bounds, the estimate gives all-orders bounds on compact subsets whenever the metric has such bounds there. No high-order data are imposed on the artificial edge. Differentiating the equation produces a transverse drift proportional to the curvature derivative. A directed multiplier uses this drift together with a small tangential term, needed where the transverse curvature derivative vanishes. A weighted elliptic estimate controls the remaining positive-curvature region. This is  .

The proposition itself [S7:41–53]:

> \begin{proposition}[Cap regularity]\label{prop:cap}
> Fix \(-1/4<b_*\le0\), and assume \eqref{eq:low-bounds}.
> Suppose that, for every compact rectangle
> \[
> R\Subset(-2,2)\times(-2,b_*),
> \]
> the ordinary coordinate derivatives of \(g\) of every order have
> uniform bounds on \(\Phi_z(R)\).
> Then the ordinary coordinate derivatives of \(z\) of every order
> also have uniform bounds on \(\Phi_z(R)\).
> The corresponding assertion holds for the upper cap
> \((-2,2)\times(-b_*,2)\).
> \end{proposition}

Two caps supply smooth data on opposite sides of a thin negative-curvature slab; hyperbolic propagation carries that data to the edges of an oscillating perturbation. The strip width is a small parameter times the inverse oscillation frequency, so the forced oscillatory moment is linear in the parameter while the competing spatial terms are quadratic. The manuscript's own summary of the count [S5:174–187]:

> Two caps supply uniformly smooth data on opposite sides of a small negative-curvature slab. Hyperbolic propagation carries these data to the two edges of a thin, oscillating metric perturbation. A finite Taylor comparison for the unperturbed metric isolates the change in the height's transverse derivative caused by the perturbation. Choose the strip width to be a small parameter times the inverse oscillation frequency. The forced oscillatory moment is linear in that parameter, while the leading competing spatial terms are quadratic and the smooth endpoint data contribute a negligible high-frequency moment. Fixing that parameter sufficiently small and then increasing the frequency excludes density, in any nonempty open set, of metrics admitting a height in a fixed bounded class. Baire category then removes those bounds and gives  , the obstruction on a whole square.

The closing lines of the pulse section state the category step [S8:404–406]:

> We have proved that every \(\mathcal A_{M,q_0}\) is nowhere dense. Their countable union contains every metric admitting an admissible height. Baire's theorem now proves  .

The geometric step explains why a squarewide obstruction is enough. The boundary-saddle lemma is the load-bearing piece [S9:166–172]:

> **lemma**


The manuscript describes the accumulation [S5:189–203]:

> The geometric step explains why that squarewise obstruction suffices. For each orientation in a fixed finite net, place shrinking obstructed patches approaching every boundary point of a disk with negative curvature inside and zero curvature on its boundary. The boundary-saddle argument finds a point where any hypothetical graph immersion has a nonzero rank-one second fundamental form. A height in the fixed ambient normal direction at that point has zero differential there. In a frame aligned with the Hessian's kernel, its mixed entry vanishes and its transverse diagonal entry is nonzero. A nearby orientation from the net preserves the required strict inequalities on a sufficiently small full patch. Finally, let such disks and their surrounding patches accumulate at the origin, with amplitudes small enough to preserve smoothness and the Euclidean Taylor jet there.

The assembly is two levels of accumulation, with summable bounds in each derivative order at both levels [S9:3–7]:

> We now turn the whole-patch obstruction into one metric germ. There are two levels of accumulation: obstructed patches approach every boundary point of each negative disk, and the disks approach the origin. Summable bounds in each derivative order will preserve smoothness at both levels.

The final comparison is with the flat metric [S9:286–288]:

> The Euclidean metric itself admits an isometric immersion into \(\mathbb R^3\), whereas the constructed metric does not on any neighborhood of the origin.

The formalization is one declaration. The scope note states what it covers [S11:9]:

> The local isometric-immersion problem asks whether every smooth surface metric can be realized locally in Euclidean three-space. The formalized counterexample is a smooth positive-definite metric on $(-1,1)^2$ for which no neighborhood of the origin admits a smooth isometric immersion into $\mathbb R^3$. The obstruction applies to every smooth candidate map on every such neighborhood.

The release's index names the paper and the one result [S12:172–175] [S12:1325–1327]:

> - comparator_config: ComparatorChallenges/IsometricImmersion.json
>   declaration: OAI.SmoothLocal.Geometry.exists_local_metric_without_local_immersion
>   file: OAI/Geometry/IsometricImmersion/Main.lean

The declaration as it stands under `lean/OAI/` [S15:49–61]:

> theorem exists_local_metric_without_local_immersion :
>     ∃ g : coordinateSquareOpen → Matrix (Fin 2) (Fin 2) ℝ,
>       LocalSmoothPositive coordinateSquareOpen g ∧
>       ∀ U : Opens Coord, ∀ hUS : (U : Set Coord) ⊆ square,
>         (0 : Coord) ∈ U → ∀ F : U → Ambient,
>           ¬ (ContMDiff 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) ∞ F ∧
>             ∀ p : U, ∀ v w : Coord,
>               (inner ℝ : Ambient → Ambient → ℝ) (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p v)
>                 (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p w) =
>                   v ⬝ᵥ (g ⟨p, hUS p.property⟩ *ᵥ w)) := by
>   refine ⟨fun p => counterexampleMetric p, counterexampleMetric_local_smoothPositive, ?_⟩
>   intro U hUS h0 F hF
>   exact counterexampleMetric_no_subtype_isometric_immersion U hUS h0 F hF

The comparator challenge states the same target under its own definitions and ends in `sorry` [S14:46–56]:

> theorem exists_local_metric_without_local_immersion :
>     ∃ g : coordinateSquareOpen → Matrix (Fin 2) (Fin 2) ℝ,
>       LocalSmoothPositive coordinateSquareOpen g ∧
>       ∀ U : Opens Coord, ∀ hUS : (U : Set Coord) ⊆ square,
>         (0 : Coord) ∈ U → ∀ F : U → Ambient,
>           ¬ (ContMDiff 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) ∞ F ∧
>             ∀ p : U, ∀ v w : Coord,
>               (inner ℝ : Ambient → Ambient → ℝ) (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p v)
>                 (mfderiv 𝓘(ℝ, Coord) 𝓘(ℝ, Ambient) F p w) =
>                   v ⬝ᵥ (g ⟨p, hUS p.property⟩ *ᵥ w)) := by
>   sorry

The comparator configuration names the challenge module, the solution module, the theorem name, and the permitted axioms [S13:1–14]:

> {
>   "challenge_module": "ComparatorChallenges.IsometricImmersion",
>   "solution_module": "OAI.Geometry.IsometricImmersion.Main",
>   "theorem_names": [
>     "OAI.SmoothLocal.Geometry.exists_local_metric_without_local_immersion"
>   ],
>   "definition_names": [],
>   "permitted_axioms": [
>     "propext",
>     "Quot.sound",
>     "Classical.choice"
>   ],
>   "enable_nanoda": false
> }

The ledger records the family as one manuscript at tier T3, formalized, with one scope note, one comparator challenge, and one `main_results` entry; the claim-shape column is empty, and the broad counterexample flag is set [S16:330].

## History of the conjecture

The manuscript places its result inside a literature that had settled the analytic local problem for nondegenerate curvature [S5:89–101]:

> The analytic local problem is settled by the classical Janet--Cartan theorem~ . For smooth metrics, nonzero Gaussian curvature leads to elliptic or hyperbolic equations and smooth local existence; zeros of curvature introduce degeneracy and changes of type. Lin's foundational work treated nonnegative curvature and a clean change of sign with finite differentiability estimates~ . Here a clean change of sign means \(K(p)=0\) and \(dK(p)\ne0\). Smooth local existence under this condition was established by Nakamura and Maeda~ ; see also the regularity comparison in \cite[p.~320]{NY2008}. More complicated zero sets have been treated under finite-order and geometric restrictions, including transverse curves and cusps~\cite[Theorem~1.1]{HanKhuri2010}\cite[Theorem~1.1]{Lin2015}.

The bibliography carries these entries: Janet 1926 [S10:163–172], Cartan 1927 [S10:174–183], Lin 1985 [S10:1–10], Lin 1986 [S10:12–21], Nakamura–Maeda 1989 [S10:23–32], Han–Khuri 2010 [S10:124–137], and Lin 2015 [S10:139–153]. The two questions the manuscript cites as the source of the problem are Yau's discussion at page 236 [S10:185–195] and Ghomi's survey, Section 1.5, Problem 1.9 [S10:155–161].

The regularity ladder is the part of the history the manuscript is careful about [S5:103–118]:

> The regularity distinction is essential. Existence at every finite differentiability order, on neighborhoods allowed to shrink with that order, does not by itself give one smooth map on a fixed neighborhood. At the other end of the scale, Nash--Kuiper flexibility gives \(C^1\) local isometric realizations in three-space~ . That regularity does not impose the second-order compatibility used for smooth immersions. Pogorelov constructed a \(C^{2,1}\) metric with no local \(C^2\) realization~\cite[paragraph~7]{Pogorelov1971}. The published refinement by Nadirashvili and Yuan achieves \(K\ge0\) with the same input and output regularities~\cite[Theorem~1.1]{NY2008}. In Theorem~A, positive definiteness refers to the metric, not its curvature: the construction uses both signs of curvature. It does not settle the smooth local-realizability problem under either sign restriction \(K\ge0\) or \(K\le0\).

Pogorelov's example is the nearest predecessor: a $C^{2,1}$ metric with no local $C^2$ realization, cited at paragraph 7 of the 1971 paper [S10:79–89]. The manuscript's result is at the smooth end of that scale.

The manuscript records a disagreement in the literature and declines to adjudicate it [S5:120–131]:

> An earlier preprint of Nadirashvili and Yuan~\cite[Theorem~1.1]{NY2002} states a stronger counterexample: a smooth metric with \(K\le0\) and no \(C^3\) isometric embedding on any neighborhood of the distinguished point. Their later published paper, however, explicitly leaves the arbitrary smooth-metric question open~\cite[p.~320]{NY2008}, as does the subsequent discussion in \cite[p.~650]{HanKhuri2010}. The earlier preprint and these later accounts therefore give different statuses for the unrestricted smooth question. We leave this discrepancy unresolved. We do not use the preprint's nonsolvability assertion; the construction below supplies its own analytic obstruction.

The 2002 preprint is in the bibliography as an arXiv entry [S10:102–111], the 2008 paper as a published article [S10:91–100]. The two analytic debts the manuscript names are the boundary-saddle argument in the 2002 preprint's Section 2, Step 3, and Khuri's high-frequency integral testing for general Monge–Ampère equations, together with Khuri's own open construction of a nonsolvable curvature profile [S5:145–159]:

> Two earlier approaches supply important parts of this strategy. The geometric construction uses the boundary-saddle argument of Nadirashvili and Yuan~\cite[Section~2, Step~3]{NY2002}: a negatively curved disk cannot be a graph whose second fundamental form vanishes along its entire boundary. On the analytic side, Khuri's counterexamples for general Monge--Amp\`ere equations use high-frequency integral testing~ . His work on the Darboux equation develops solution-dependent flow coordinates and a prescribed-curvature construction, while leaving open the construction of the required nonsolvable curvature profile~\cite[Theorem~1 and the following discussion]{Khuri2009}. The distinction matters here: the Darboux coefficients come from one metric, so a nonsolvable general Monge--Amp\`ere equation does not by itself give an isometric-immersion obstruction. We perturb the metric itself and estimate the resulting Darboux forcing.

The Khuri entries are the 2007 counterexamples paper [S10:55–64] and the 2009 Darboux paper [S10:113–122].

**Prior (my training data, not this repo).** The local isometric embedding problem for surfaces is classical: the Janet–Cartan theorem gives analytic local realization, and the degenerate cases — where the Gaussian curvature vanishes — are the hard ones. Lin, Nakamura–Maeda, Han–Khuri, and Lin's later work on cusp domains are the standard names for the finite-regularity results, and Pogorelov's example is the standard counterexample at low regularity. Nash's and Kuiper's $C^1$ flexibility sits at the opposite end. The literature I recall treats the smooth, unrestricted case as open, which is consistent with the manuscript's own framing [S5:65–67] and with the discrepancy it records [S5:120–131]. The prior is a training-data recollection at an early-2025 cutoff, self-rated, and the repo supplies only the manuscript's citations.

## Consequences

The direct consequence is the one the release states: the unrestricted smooth local realization problem for surfaces has a negative answer, and shrinking the neighborhood does not rescue it [S1:8136] [S2:766]. The manuscript's own framing names the two sources it answers [S5:65–67].

The second consequence is about what smooth data determine. The constructed metric has the Euclidean Taylor jet at the origin, so the full jet at a point does not decide local smooth realizability [S9:250–261]. A negative answer at that level is stronger than a singularity example: the metric is flat to every order at the point where the obstruction is located.

The third is what the result does not settle. The construction uses both signs of curvature, so the sign-restricted problems ($K\ge0$ and $K\le0$) remain open, as the manuscript states [S5:115–118]. The manuscript also declines to use the 2002 preprint's stronger assertion, so the $K\le0$ smooth case is not resolved by this paper [S5:130–131].

Inside the release, the formalization is one declaration, `OAI.SmoothLocal.Geometry.exists_local_metric_without_local_immersion`, over one file [S12:1325–1327] [S15:49–61]. The comparator challenge for the family is a stub with one `sorry` [S14:46–56], and the release's review status for the formalization is `unchecked`. The scope note describes the formalized counterexample as the metric and the obstruction over every neighborhood of the origin [S11:9]; the Darboux lemma, the cap estimate, the Baire argument, the boundary-saddle lemma, and the accumulation construction are not formalized, and the scope note names no exclusion. The manuscript ships no verification bundle, no reasoning trace, and no second manuscript [S16:330].

What has not been checked: no Lean or comparator run was performed, so nothing here proves the formalized declaration elaborates, and the carrier under `lean/OAI/Geometry/IsometricImmersion/` was not read beyond `Main.lean`; the manuscript's four section files were read at the statement level, not line by line across all 1,284 lines, so a proof step inside `caps.tex`, `pulse.tex`, or `assembly.tex` can be mis-stated here; the manuscript's own NY2002 discrepancy is recorded as unresolved by the manuscript and is not adjudicated; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 19 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `CONTENTS.md` | 9142 | Release blurb, manuscript link, manuscript abstract |
| S2 | `overview.tex` | 859 | Family 334's `\resultentry`, at line 766 |
| S3 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/README.md` | 17 | Manuscript README and bibtex key |
| S4 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/paper.pdf` | 12181 | Manuscript PDF |
| S5 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/main.tex` | 228 | Abstract, Theorem A, introduction, conventions, include list |
| S6 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/model.tex` | 105 | Model patch, admissible height, height lemma, patch obstruction |
| S7 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/caps.tex` | 484 | Cap regularity estimate |
| S8 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/pulse.tex` | 406 | Oscillatory pulse and the Baire argument |
| S9 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/assembly.tex` | 289 | Disk accumulation, boundary-saddle lemma, Taylor-jet corollary |
| S10 | `preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/references.bib` | 195 | Bibliography |
| S11 | `lean/docs/334.md` | 15 | Scope note |
| S12 | `lean/formalization.yaml` | 1783 | Release index of papers and results |
| S13 | `lean/ComparatorChallenges/IsometricImmersion.json` | 14 | Comparator configuration |
| S14 | `lean/ComparatorChallenges/IsometricImmersion.lean` | 62 | Comparator challenge stub |
| S15 | `lean/OAI/Geometry/IsometricImmersion/Main.lean` | 67 | Formalized declaration |
| S16 | `notes/tables/catalog.tsv` | 373 | Reading ledger row for family 334 |

## Links

- [S1](../../../CONTENTS.md)
- [S2](../../../overview.tex)
- [S3](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/README.md)
- [S4](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/paper.pdf)
- [S5](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/main.tex)
- [S6](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/model.tex)
- [S7](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/caps.tex)
- [S8](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/pulse.tex)
- [S9](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/sections/assembly.tex)
- [S10](../../../preprints/A-Smooth-Metric-with-No-Local-Isometric-Immersion-into-Three-Space-September-24-2026/build/references.bib)
- [S11](../../../lean/docs/334.md)
- [S12](../../../lean/formalization.yaml)
- [S13](../../../lean/ComparatorChallenges/IsometricImmersion.json)
- [S14](../../../lean/ComparatorChallenges/IsometricImmersion.lean)
- [S15](../../../lean/OAI/Geometry/IsometricImmersion/Main.lean)
- [S16](../../../notes/tables/catalog.tsv)

## Bibliography

**17 entries** from `references.bib`:
- Lin, Chang-Shou. *The local isometric embedding in {$\mathbb{R}^3$} of 2-dimensional {Riemannian} manifolds with nonnegative curvature*. (1985) [Lin1985]
- Lin, Chang-Shou. *The local isometric embedding in {$\mathbb{R}^3$} of two-dimensional {Riemannian} manifolds with {Gaussian} curvature changing sign cleanly*. (1986) [Lin1986]
- Nakamura, Gen, Maeda, Yoshiaki. *Local smooth isometric embeddings of low-dimensional {Riemannian} manifolds into {Euclidean} spaces*. (1989) [NakamuraMaeda1989]
- Nash, John. *{$C^1$} isometric imbeddings*. (1954) [Nash1954]
- Kuiper, Nicolaas H.. *On {$C^1$}-isometric imbeddings. {I}*. (1955) [Kuiper1955]
- Khuri, Marcus A.. *Counterexamples to the Local Solvability of {Monge--Amp\`ere} Equations in the Plane*. (2007) [Khuri2007Counterexamples]
- Schoen, Richard, Yau, Shing-Tung. *Lectures on Differential Geometry*. (1994) [Yau]
- Pogorelov, A. V.. *An example of a two-dimensional {Riemannian} metric admitting no local realization in {$E^3$}*. (1971) [Pogorelov1971]
- Nadirashvili, Nikolai, Yuan, Yu. *Improving {Pogorelov}'s isometric embedding counterexample*. (2008) [NY2008]
- Nadirashvili, Nikolai, Yuan, Yu. *Counterexamples for Local Isometric Embedding*. (2002) [NY2002]
- … and 7 more
