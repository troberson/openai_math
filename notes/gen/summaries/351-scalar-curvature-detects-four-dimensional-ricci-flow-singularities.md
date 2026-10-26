[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 351](../index/differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md)

# 351 — Scalar curvature detects four-dimensional Ricci-flow singularities

[Index page](../index/differential-geometry/351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md)

## Headline theorem

The counterexample manuscript's main theorem is the flow itself [S7:69–78]:

> There are an integer \(q\ge10\), a time \(T>0\), and a smooth Ricci flow \(g(t)\), \(0\le t<T\), on the closed connected manifold \(M=\mathbb S^2\times\mathbb S^q+1\), with smooth initial metric, such that \[ \sup_{M\times[0,T)}|R_g(t)|<\infty, \qquad \lim_{t\uparrow T}\max_M|\mathrmRm_g(t)|=\infty. \] In particular, \(T\) is the finite maximal existence time of this flow. [S7:69–77]

The manuscript states what the theorem does not say: it refutes the unrestricted all-dimensions formulation, and it draws no dimension-four conclusion [S7:80–84].

The four-dimensional manuscript's extension theorem is the positive half 

> Let \(M\) be a closed connected smooth four-manifold, let \(0<T<\infty\), and let \(g(t)\), \(0\le t<T\), be a smooth Ricci flow with smooth initial metric. If \[ \sup_{M\times[0,T)}|R(g(t))|<\infty, \] then there are \(\varepsilon>0\) and a smooth Ricci flow \(\widetilde g(t)\) on \(M\), \(0\le t<T+\varepsilon\), such that \(\widetilde g(t)=g(t)\) for every \(t<T\). [S20:12–20]

Its corollary is the contrapositive, and it is the dimension-four detection statement 

> If a Ricci flow on a closed smooth four-manifold has finite maximal smooth existence time \(T\), then \[ \limsup_{t\uparrow T}\max_{x\in M}R(g(t))(x)=+\infty. \] [S20:32–36]

The proof of the corollary is short 

> The equation \((\partial_t-\Delta)R=2|\mathrmRic|^2\) and the maximum principle give a scalar lower bound on a finite time interval. A finite upper limit in the assertion would therefore give a uniform absolute bound near \(T\), and smoothness supplies the bound on the remaining compact time interval. The componentwise extension just described contradicts maximality. [S20:40–45]

The companion's abstract states its own result 

> We prove a sequential elliptic inequality for the renormalized Einstein–Hilbert functional on a fixed finite tree of four-dimensional Ricci-flat spaces. As the joining lengths diverge and the scale-neutral weighted Ricci error $M$ tends to zero, the functional satisfies $E=o(M)$. The root end has decay exponent greater than one, and every joined quotient group is nontrivial. We also prove the multivariable path-selection theorem for asymptotic expansions used to obtain this estimate. [S31:9–15]

## Undergraduate summary

The release names three manuscripts, all dated September 24, 2026 [S4:4] [S16:4] [S29:4]. Their bibtex titles are `A closed Ricci flow with bounded scalar curvature and finite-time curvature blowup` [S4:11], `Bounded scalar curvature and smooth extension of four-dimensional Ricci flow` [S16:11], and `Path selection and an elliptic inequality on degenerating Ricci-flat trees` [S29:11]. The PDFs are `paper.pdf` in each root [S5] [S17] [S30].

**Manuscript A** ships `build/paper.tex` (47 lines), six section files, two TikZ figures, and a bibliography of 13 entries [S6] [S7] [S8:1] [S9:1] [S10] [S11] [S12] [S13] [S14] [S15]. The sections are `01-introduction.tex` (147 lines), `02-construction.tex` (154, "The construction used as input [S8:1]" ), `03-geometry.tex` (222, "Geometric identities and profile consequences [S9:1]" ), `04-cap.tex` (247, "Curvature at the radius and cap scales [S10:1]" ), `05-reaction.tex` (261, "A dimension-explicit Ricci reaction bound [S11:1]" ), `06-barriers.tex` (320, "Comparison and the scalar-curvature bound [S12:1]" ). The introduction's organization paragraph names Sections `sec:construction`, `sec:geometry`, `sec:cap`, `sec:reaction`, `sec:barriers`, and the build tree defines all five [S7:129–138]. The figures are `scales.tex` (20 lines) [S13] and `drift-cylinder.tex` (18) [S14]. The bibliography's Wang entry is the dimension-three theorem the introduction cites [S15:88–96]:

> \bibitem{Wang2012}
> B.~Wang,
> \emph{On the conditions to extend Ricci flow (II)},
> Int. Math. Res. Not. IMRN 2012, no. 14, 3192--3223.

**Manuscript B** ships `build/paper.tex` (28 lines), a `build/preamble.tex` (48 lines), six section files, two figures, and a 440-line `build/sources/references.bib` [S18] [S19:48] [S20] [S21:1] [S22:1] [S23:1] [S24:1] [S25:1] [S26] [S27] [S28]. Its preamble's pdf subject is "Bounded scalar curvature, Ricci flow, and Ricci-flat bubble trees [S19:48]" [S19:46–48]. The section files are `01-introduction.tex` (200 lines), `02-static-input.tex` (158, "The static input and its normalization [S21:1]" ), `04-geometry.tex` (1,432, "Small-scale geometry and the outermost scale [S22:1]" ), `05-parabolic.tex` (806, "Concentration estimates for the Ricci equation [S23:1]" ), `06-collar.tex` (863, "An exterior extension determined by a fixed collar [S24:1]" ), `07-contradiction.tex` (813, "Functional change and the contradiction [S25:1]" ) — the numbering skips `03`. The introduction's proof-structure paragraph names Sections `sec:geometry`, `sec:parabolic`, `sec:collar`, `sec:contradiction`, and names `sec:static-input` when it records the companion's input [S20:160–185] [S20:125–131]. The figures are `buffered-intervals.tex` (35 lines) [S26] and `overview.tex` (21) [S27].

**Manuscript C** ships `build/paper.tex` (34 lines), a `build/preamble.tex` (80 lines), seven section files, one figure, and a 146-line `build/references.bib` [S31:9–15] [S32:80] [S33] [S34] [S35:1] [S36:1] [S37:1] [S38:1] [S39:1] [S40] [S41]. Its preamble's pdf subject is "Quasianalytic path selection, Ricci-flat bubble trees, and a renormalized Einstein-Hilbert functional [S32:80]" [S32:78–80]. Its sections are `01-introduction.tex` (193 lines), `02-tree.tex` (156, "Tree geometry and the renormalized functional [S34:1]" ), `03-path.tex` (1,320, "Selection of paths at several exponential ends [S35:1]" ), `04-family.tex` (572, "Augmented inverses and the analytic family [S36:1]" ), `05-tails.tex` (213, "Tail expansions and prescribed growth [S37:1]" ), `06-length.tex` (166, "Expansion in one length [S38:1]" ), `07-observables.tex` (307, "Scalar expansions and the tree inequality [S39:1]" ). The introduction's organization paragraph names `sec:elliptic`, `sec:path`, `sec:family`, `ell:tail-calculus`, `ell:length-expansion`, `ell:scalar-calculus`, and the build tree defines all six [S33:176–184]. The figure is `tree-scales.tex` (21 lines) [S40].

## Graduate summary

The counterexample is a doubly warped ansatz with two coupled positive scale functions [S7:94–102]:

> \[
> ds^2+\phi(s,t)^2g_{\Sp^2}+r(s,t)^2g_{\Sp^q},
> \]

The construction separates two scales. With `δ = T − t`, the parabolic scale is `√δ` and the cap scale is `θ = δ^σ` with `σ > 1/2`, so the cap is strictly smaller than the parabolic scale [S7:104–111]. Stolarski's Proposition 5.3 supplies the scalar-sign obstruction, the curvature point-picking, and the Ricci reaction bound whose leading coefficient is `2q`; the reaction estimate `|Ric| ≤ C r^{-e}` holds for `0 < e < 1` [S7:113–127]. The construction input fixes the parameters, the cap scale, and the discrete exponent set [S8:26–30], and the geometry section proves the strict cone gap `r ≤ (1 − κ)θ` [S9:116–119].

The cap proposition is what decouples the two curvatures 

> For every flow with the choices made above, and \(q\) sufficiently large, there is a constant \(C\), allowed to depend on that flow, such that $$\label{eq:full-curvature} (r^2+\theta^2)|\mathrm{Rm}|\le C$$ on \(M\times[0,T)\). [S10:4–9]

The reaction proposition bounds the reaction quotient at the pole and at the cap 

> At late times on \(0<r\le\frac18\sqrt\delta\), the reaction quotient \[ c(x,t)=\frac{2\langle\mathrmRm(\mathrmRic),\mathrmRic\rangle}{|\mathrmRic|^2} \quadwhere |\mathrmRic|>0 \] satisfies both bounds $$\label{eq:reaction-two} c\le\frac{2(q-1)+C\sqrt q}{r^2},\qquad c\le\frac{C_*}{\theta^2}.$$ [S11:210–219]

The three barrier propositions fix the parameters in order and control the pole, the interior, and the geometric exterior [S12:71–73] [S12:158–159] [S12:225–226].

The rate corollary is the quantitative form, with `d_q = (q + 1 − √((q + 1)(q − 7)))/2` 

> For every sufficiently large integer \(q\), set \[ d_q=\frac{q+1-\sqrt(q+1)(q-7)}2. \] For every sufficiently large even integer \(k\), with the threshold allowed to depend on \(q\), there is a smooth Ricci flow on \(\mathbb S^2\times\mathbb S^q+1\) with finite maximal time \(T\), uniformly bounded scalar curvature, and constants \(0<c\le C<\infty\) such that \[ c(T-t)^-2k/d_q\le\max_M|\mathrmRm|(\cdot,t) \le C(T-t)^-2k/d_q \] for all sufficiently late times. In particular, one fixed dimension admits such flows with an unbounded discrete set of power-law Type-II curvature exponents. The flow, \(T\), and the constants may depend on \(q\) and \(k\). [S12:284–299]

The four-dimensional paper runs the other way. It models the spatial geometry near `T` as a tree of Ricci-flat ALE pieces with an outermost scale `a(t)` [S20:100–105], and studies a renormalized Einstein–Hilbert functional whose differential is the integral pairing with the Einstein tensor `½ R g − Ric` [S20:109–123]. The degeneration-tree theorem makes the tree precise [S22:31–60], the buffered-interval proposition selects time intervals on which the outermost scale changes by a fixed factor [S22:1270–1282], the exterior Ricci proposition is the parabolic input [S23:334–336], the collar extension theorem extends the flow across the collar [S24:82–108], and the final contradiction shows the energy must vanish [S25:476].

The companion paper is the static half. It fixes a tree of Ricci-flat ALE model spaces, selects a path through the tree, and proves the tree inequality 

> Fix a finite rooted tree with the end identifications and order-$20$ metric bounds of Section  . Let $(g_j,L^{(j)},M_j)$ satisfy the compact vertex convergence, the same uniform half-end and root-end bounds, and Equation   through order $10$, with every $L_e^{(j)}\to\infty$ and $M_j\to0$. Then, in physical root units, $$E(g_j)=o(M_j). \label{ell:little-oh}$$ For an index with $M_j=0$, the assertion means $E(g_j)=0$. The little-oh is taken for this fixed tree; it does not assert a power exponent uniform over different trees. [S34:136–141]

Its path-selection theorem realizes finite sign conditions and finite prescribed limits along a real analytic path, with every actual coordinate eventually monotone or constant [S35:67–79], and its corollary gives the finite variation the elliptic argument consumes [S35:90–97].

## History of the conjecture

The scalar-curvature extension question is a refinement of Hamilton's 1995 singularity criterion, stated as a necessity: a flow can fail to extend only if full curvature blows up [S7:16–17]. Wang's 2012 paper on the conditions to extend Ricci flow is the dimension-three restriction the introduction states [S15:88–96] [S7:26–38]. The introduction attributes the all-dimensions conjecture to Bamler, page 756, and to Šešum [S7:18–24]. The Type II literature — Angenent–Knopf's shrinking neck, Gu–Zhu, and the AIK analysis — is the analysis of singularity models the construction is designed to produce [S7:40–51]. Stolarski's 2019 Proposition 5.3 is the scalar-sign obstruction the construction uses [S7:113–127].

The four-dimensional manuscript's history is the extension literature after Hamilton: Šešum's 2005 local curvature bounds, Bamler's compactness, Liu–Simon, and Li–Li [S20:50–72]. The ALE bubble-tree analysis it uses descends from Anderson, Bando, Bando–Kasue–Nakajima, and Cheeger–Tian [S20:86–98]. The companion's method descends from the renormalized ALE functionals of Haslhofer and of Deruelle–Ozuch, the quasianalytic algebras of Speissegger, and the Einstein desingularization work of Biquard and Ozuch [S33:21–35] [S33:94–102] [S33:117–132].

## Consequences

The unrestricted scalar-curvature extension conjecture is false. The counterexample is a closed smooth flow with bounded scalar curvature and a genuine finite maximal time [S7:69–78], so bounded scalar curvature does not control full curvature in high dimension. The rate corollary adds that one fixed dimension admits such flows with an unbounded discrete set of power-law Type-II curvature exponents `2k/d_q`, one flow per sufficiently large even `k` [S12:284–299].

The four-dimensional result closes the question at the other end. Bounded scalar curvature forces extension, and the contrapositive says a four-dimensional flow with finite maximal existence time must have scalar curvature tending to infinity [S20:32–36]. So in dimension four the scalar curvature alone detects the singularity, and the dimension where the conjecture holds is exactly the dimension where the counterexample does not live.

The companion's inequality is the static input the four-dimensional proof consumes: the introduction states that the companion article proves `E = o(M)` on each fixed limiting tree and that Section `sec:static-input` records the complete input, and that the four-dimensional task is to verify those hypotheses for metrics obtained from the flow and compare their functional variation with actual spacetime Ricci energy [S20:125–131]. The tree inequality and the path-selection theorem are the two statements that carry it [S34:136–141] [S35:67–79]. The companion states its conclusion as a little-oh bound taken for a fixed tree, and it does not assert a power exponent uniform over different trees [S34:136–141].

Inside the release, the family is at tier T0 with no formalized manuscript, no scope note, no comparator, no verification bundle, and no reasoning trace [S3:347]. The three manuscripts are 8,750 lines of section text in total, and nothing in `lean/` names them, so no Lean or comparator run can confirm any part of the argument.

## Coverage

The release records 3 manuscripts for this family and 0 formalized paths, 0 comparator challenges, 0 `main_results` entries, 0 scope notes, 0 verification bundles, 0 inputs, and no reasoning trace [S3:347]. The overview entry is the family's only release-level statement [S2:800]. The three manuscript abstracts are the release's own claims [S1:8542] [S1:8551] [S1:8560].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | Release blurb, three manuscript links, three manuscript abstracts |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 351's `\resultentry`, at line 800 |
| S3 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 373 | Reading ledger row for family 351 |
| S4 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/README.md`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/README.md) | 17 | Manuscript A README: date, bibtex key |
| S5 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf) | 6262 | Manuscript A PDF |
| S6 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/paper.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/paper.tex) | 47 | Manuscript A preamble, theorem environments, section order |
| S7 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/01-introduction.tex) | 147 | Abstract, main theorem, the doubly warped ansatz, the two scales, the organization |
| S8 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/02-construction.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/02-construction.tex) | 154 | The construction input proposition |
| S9 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/03-geometry.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/03-geometry.tex) | 222 | The warping identities and the strict cone gap |
| S10 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/04-cap.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/04-cap.tex) | 247 | The full-curvature proposition at the radius and cap scales |
| S11 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/05-reaction.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/05-reaction.tex) | 261 | The dimension-explicit reaction proposition |
| S12 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/06-barriers.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/sections/06-barriers.tex) | 320 | The three barrier propositions and the rate corollary |
| S13 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/figures/scales.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/figures/scales.tex) | 20 | The two-scale figure |
| S14 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/figures/drift-cylinder.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/figures/drift-cylinder.tex) | 18 | The drift-cylinder figure |
| S15 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/references/bibliography.tex`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/build/references/bibliography.tex) | 96 | Manuscript A bibliography, 13 entries |
| S16 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/README.md`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/README.md) | 17 | Manuscript B README: date, bibtex key |
| S17 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf) | 19424 | Manuscript B PDF |
| S18 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/paper.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/paper.tex) | 28 | Manuscript B preamble, theorem environments, section order |
| S19 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/preamble.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/preamble.tex) | 48 | Manuscript B preamble and pdf metadata |
| S20 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/01-introduction.tex) | 200 | Extension theorem, scalar-blowup corollary, the degeneration tree, the functional, the proof structure |
| S21 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/02-static-input.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/02-static-input.tex) | 158 | The static input and its normalization |
| S22 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/04-geometry.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/04-geometry.tex) | 1432 | The degeneration-tree theorem and the buffered-interval proposition |
| S23 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/05-parabolic.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/05-parabolic.tex) | 806 | The exterior Ricci proposition |
| S24 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/06-collar.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/06-collar.tex) | 863 | The collar extension theorem |
| S25 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/07-contradiction.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/07-contradiction.tex) | 813 | The functional-smallness proposition and the final contradiction |
| S26 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/buffered-intervals.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/buffered-intervals.tex) | 35 | The buffered-intervals figure |
| S27 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/overview.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/overview.tex) | 21 | The overview figure |
| S28 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sources/references.bib`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sources/references.bib) | 440 | Manuscript B bibliography |
| S29 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/README.md`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/README.md) | 17 | Manuscript C README: date, bibtex key |
| S30 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf) | 15438 | Manuscript C PDF |
| S31 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/paper.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/paper.tex) | 34 | Manuscript C preamble, abstract, theorem environments, section order |
| S32 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/preamble.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/preamble.tex) | 80 | Manuscript C preamble and pdf metadata |
| S33 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/01-introduction.tex) | 193 | The tree, the functional, the prior work, the path selection, the organization |
| S34 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/02-tree.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/02-tree.tex) | 156 | The tree inequality |
| S35 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/03-path.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/03-path.tex) | 1320 | The path-selection theorem and the variation corollary |
| S36 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/04-family.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/04-family.tex) | 572 | The inverses, gauge, analytic family, and comparison |
| S37 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/05-tails.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/05-tails.tex) | 213 | The tail expansions and prescribed growth |
| S38 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/06-length.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/06-length.tex) | 166 | The expansion in one length |
| S39 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/07-observables.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/07-observables.tex) | 307 | The scalar expansions that complete the theorem |
| S40 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/figures/tree-scales.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/figures/tree-scales.tex) | 21 | The tree-scales figure |
| S41 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/references.bib`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/references.bib) | 146 | Manuscript C bibliography |

## Bibliography

- Anderson, Michael T., Ricci curvature bounds and Einstein metrics on compact manifolds (1989)
- S. Angenent, J. Isenberg, and D. Knopf, _Degenerate neckpinches in Ricci flow_, J. Reine Angew. Math. **709** (2015), 81–117. arXiv:1208.4312v1.
- R. H. Bamler, _Convergence of Ricci flows with bounded scalar curvature_, Ann. of Math. (2) **188** (2018), no. 3, 753–831. doi:10.4007/annals.2018.188.3.2.
- Bamler, Richard H., Zhang, Qi S., Heat kernel and curvature bounds in Ricci flows with bounded scalar curvature (2017)
- Bamler, Richard H., Zhang, Qi S., Heat kernel and curvature bounds in Ricci flows with bounded scalar curvature—Part II (2019)
- Bamler, Richard H., Convergence of Ricci flows with bounded scalar curvature (2018)
- Bamler, Richard H., Zhang, Qi S., Heat kernel and curvature bounds in Ricci flows with bounded scalar curvature (2017)
- Bamler, Richard H., Zhang, Qi S., Heat kernel and curvature bounds in Ricci flows with bounded scalar curvature—Part II (2019)
- Bamler, Richard H., Convergence of Ricci flows with bounded scalar curvature (2018)
- Bando, Shigetoshi, Bubbling out of Einstein manifolds (1990)
- Bando, Shigetoshi, Correction and addition: Bubbling out of Einstein manifolds (1990)
- Bando, Shigetoshi, Kasue, Atsushi, Nakajima, Hiraku, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth (1989)
- Bartnik, Robert, The mass of an asymptotically flat manifold (1986)
- Biquard, Olivier, Désingularisation de métriques d'Einstein. I (2013)
- Buzano, Reto, Di Matteo, Gianmichele, A Local Singularity Analysis for the Ricci Flow and its Applications to Ricci Flows with Bounded Scalar Curvature—Part II (2026)
- C. Böhm, _Non-compact cohomogeneity one Einstein manifolds_, Bull. Soc. Math. France **127** (1999), no. 1, 135–177. doi:10.24033/bsmf.2345.
- Cheeger, Jeff, Tian, Gang, Curvature and injectivity radius estimates for Einstein 4-manifolds (2006)
- Cheeger, Jeff, Gromov, Mikhail, Taylor, Michael, Finite propagation speed, kernel estimates for functions of the Laplace operator, and the geometry of complete Riemannian manifolds (1982)
- Chern, Shiing-Shen, A Simple Intrinsic Proof of the Gauss–Bonnet Formula for Closed Riemannian Manifolds (1944)
- Chiarenza, Filippo, Frasca, Michele, Longo, Placido, Interior $W^{2,p}$ estimates for non divergence elliptic equations with discontinuous coefficients (1991)
- Chiarenza, Filippo, Frasca, Michele, Longo, Placido, $W^{2,p}$-solvability of the Dirichlet problem for nondivergence elliptic equations with VMO coefficients (1993)
- Ciarlet, Philippe G., Ciarlet, Jr., Patrick, Another approach to linearized elasticity and a new proof of Korn's inequality (2005)
- Deruelle, Alix, Kröncke, Klaus, Stability of ALE Ricci-flat manifolds under Ricci flow (2021)
- Deruelle, Alix, Ozuch, Tristan, A Łojasiewicz inequality for ALE metrics (2025)
- Deruelle, Alix, Ozuch, Tristan, A Łojasiewicz inequality for ALE metrics (2025)
- DeTurck, Dennis M., Kazdan, Jerry L., Some regularity theorems in Riemannian geometry (1981)
- DeTurck, Dennis M., Kazdan, Jerry L., Some regularity theorems in Riemannian geometry (1981)
- Enders, Joerg, Müller, Reto, Topping, Peter M., On type-I singularities in Ricci flow (2011)
- Galal, Zeinab, Kaiser, Tobias, Speissegger, Patrick, Ilyashenko algebras based on transserial asymptotic expansions (2020)
- Galal, Zeinab, Kaiser, Tobias, Speissegger, Patrick, Ilyashenko algebras based on transserial asymptotic expansions (2020)
- Gilbarg, David, Trudinger, Neil S., Elliptic Partial Differential Equations of Second Order (2001)
- R. S. Hamilton, _The formation of singularities in the Ricci flow_, Surveys in Differential Geometry, Vol. II (Cambridge, MA, 1993), International Press, Cambridge, MA, 1995, 7–136. Full text.
- Hamilton, Richard S., Three-manifolds with positive Ricci curvature (1982)
- Hardy, G. H., Littlewood, J. E., A maximal theorem with function-theoretic applications (1930)
- Haslhofer, Robert, A renormalized Perelman-functional and a lower bound for the ADM-mass (2011)
- Khavkine, Igor, The Calabi complex and Killing sheaf cohomology (2017)
- S. Angenent and D. Knopf, _An example of neckpinching for Ricci flow on $S^{n+1}$_, Math. Res. Lett. **11** (2004), no. 4, 493–518. Author's text; corrigendum.
- N. V. Krylov, _Parabolic equations with VMO coefficients in spaces with mixed norms_, arXiv:math/0610955v1, 2006. Theorem numbering refers to this version. Published as _Parabolic equations with VMO coefficients in Sobolev spaces with mixed norms_, J. Funct. Anal. **250** (2007), no. 2, 521–558. doi:10.1016/j.jfa.2007.04.003.
- O. A. Ladyzhenskaya, V. A. Solonnikov, and N. N. Ural'tseva, _Linear and Quasi-linear Equations of Parabolic Type_, Translations of Mathematical Monographs, vol. 23, American Mathematical Society, Providence, RI, 1968; corrected reprint, 1988. doi:10.1090/mmono/023.
- Li, Chuanhuan, Li, Yi, Long-time existence of some geometric flows with bounded scalar curvature (2026)
- Liu, Jiawei, Simon, Miles, Volume estimates and convergence results for solutions to Ricci flow with $L^p$ bounded scalar curvature (2026)
- Lockhart, Robert B., McOwen, Robert C., Elliptic differential operators on noncompact manifolds (1985)
- OpenAI, Path selection and an elliptic inequality on degenerating Ricci-flat trees (2026)
- Ozuch, Tristan, Noncollapsed degeneration of Einstein 4-manifolds II (2022)
- Ozuch, Tristan, Integrability of Einstein deformations and desingularizations (2021)
- Perelman, Grisha, The entropy formula for the Ricci flow and its geometric applications (2002)
- Perrucci, Daniel, Roy, Marie-Françoise, Elementary recursive quantifier elimination based on Thom encoding and sign determination (2017)
- W.-X. Shi, _Deforming the metric on complete Riemannian manifolds_, J. Differential Geom. **30** (1989), no. 1, 223–301. doi:10.4310/jdg/1214443292.
- Shi, Wan-Xiong, Deforming the metric on complete Riemannian manifolds (1989)
- Simon, Miles, Extending four dimensional Ricci flows with bounded scalar curvature (2020)
- Simon, Miles, Some integral curvature estimates for the Ricci flow in four dimensions (2020)
- Speissegger, Patrick, Quasianalytic Ilyashenko algebras (2018)
- Speissegger, Patrick, Quasianalytic Ilyashenko algebras (2018)
- M. Stolarski, _Curvature Blow-up in Doubly-warped Product Metrics Evolving by Ricci Flow_, arXiv:1905.00087v1, 2019. All numbered source references in this paper use this version. Published in Mem. Amer. Math. Soc. **295** (2024), no. 1470. doi:10.1090/memo/1470.
- Šešum, Nataša, Curvature tensor under the Ricci flow (2005)
- B. Wang, _On the conditions to extend Ricci flow (II)_, Int. Math. Res. Not. IMRN **2012**, no. 14, 3192–3223. doi:10.1093/imrn/rnr141. arXiv:1107.5107v1; theorem numbering refers to this preprint version.
- Wang, Bing, On the conditions to extend Ricci flow (2008)
- Zhang, Zhou, Scalar curvature behavior for finite-time singularity of Kähler–Ricci flow (2010)
- H.-D. Cao and X.-P. Zhu, _A complete proof of the Poincaré and geometrization conjectures—application of the Hamilton–Perelman theory of the Ricci flow_, Asian J. Math. **10** (2006), no. 2, 165–492. Full text.
- H.-L. Gu and X.-P. Zhu, _The existence of Type II singularities for the Ricci flow on $S^{n+1}$_, Comm. Anal. Geom. **16** (2008), no. 3, 467–494. arXiv:0707.0033v1.
- N. Šešum, _Curvature tensor under the Ricci flow_, Amer. J. Math. **127** (2005), no. 6, 1315–1324. doi:10.1353/ajm.2005.0042.
