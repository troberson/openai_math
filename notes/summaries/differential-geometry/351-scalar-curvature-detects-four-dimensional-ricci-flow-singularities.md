# 351 — Scalar curvature detects four-dimensional Ricci-flow singularities (Differential geometry, 3 manuscripts, tier T0)

The ledger records `paps` 3, `paps_form` 0, tier T0, `chal` 0, `mainres` 0, `scope_note` 0, `verification` 0, `inputs` 0, `covmd` 0, no trace, no companion edge, and a broad counterexample flag [S3:347]. The claim-shape column is `counterexample|bound|uniform`, the conditional flag is 0, and the resolves-named flag is 1. Nothing in the release formalizes any of the three manuscripts, so no Lean or comparator statement names them.

The blurb is the release's own summary [S1:8533]:

> 351. Scalar curvature and finite-time Ricci-flow singularities. Proves that a smooth Ricci flow on a closed four-manifold extends past any finite time at which scalar curvature remains uniformly bounded. A higher-dimensional counterexample has bounded scalar curvature but unbounded full curvature at its finite maximal time, disproving the unrestricted scalar-curvature extension conjecture.

## Undergraduate summary

A Ricci flow is a one-parameter family of metrics evolving by `∂t g = −2 Ric(g)`. Two curvature quantities matter here. The **full curvature tensor** `Rm` records every component of curvature. The **scalar curvature** `R` is a single number at each point, obtained by contracting the Ricci tensor — it keeps much less information than `Rm`.

Hamilton's 1995 theorem states the necessity: a smooth Ricci flow on a closed manifold can fail to extend past a finite time `T` only if its full curvature becomes unbounded [S7:16–17]. The natural converse in a weaker form asks whether bounded *scalar* curvature is enough to force extension.

The introduction attributes the all-dimensions conjecture to Bamler, page 756, and to Šešum [S7:18–24]. Wang's dimension-three result is the restriction the introduction states: bounded scalar curvature in dimension three forces the full curvature to be bounded, and the introduction adds the display `limsup (T − t)² max |Rm| > 0` [S7:26–38].

Family 351 splits the question in two. The first manuscript **disproves** the unrestricted conjecture: in sufficiently high dimension it builds a smooth Ricci flow on the closed manifold `S² × S^{q+1}` with `q ≥ 10` whose scalar curvature stays uniformly bounded while the full curvature tensor blows up at a finite maximal time [S7:69–78]. The second manuscript proves the opposite in real dimension four: bounded scalar curvature on a closed smooth four-manifold does imply smooth extension [S20:12–20], and the corollary is that a four-dimensional flow with finite maximal existence time must have scalar curvature tending to infinity [S20:32–36]. The third manuscript supplies the static input the four-dimensional proof consumes: a sequential elliptic inequality for degenerating Ricci-flat trees [S34:136–141].

So the scalar curvature detects a four-dimensional singularity, and it does not detect one in high dimension. The dimension is the dividing line.

## Graduate summary

The counterexample is a doubly warped ansatz with two coupled positive scale functions [S7:94–102]:

> \[
> ds^2+\phi(s,t)^2g_{\Sp^2}+r(s,t)^2g_{\Sp^q},
> \]

The construction separates two scales. With `δ = T − t`, the parabolic scale is `√δ` and the cap scale is `θ = δ^σ` with `σ > 1/2`, so the cap is strictly smaller than the parabolic scale [S7:104–111]. Stolarski's Proposition 5.3 supplies the scalar-sign obstruction, the curvature point-picking, and the Ricci reaction bound whose leading coefficient is `2q`; the reaction estimate `|Ric| ≤ C r^{-e}` holds for `0 < e < 1` [S7:113–127]. The construction input fixes the parameters, the cap scale, and the discrete exponent set [S8:26–30], and the geometry section proves the strict cone gap `r ≤ (1 − κ)θ` [S9:116–119].

The cap proposition is what decouples the two curvatures [S10:4–9]:

> For every flow with the choices made above, and \(q\) sufficiently large,
> there is a constant \(C\), allowed to depend on that flow, such that
> \begin{equation}\label{eq:full-curvature}
> (r^2+\theta^2)|\Rm|\le C
> \end{equation}
> on \(M\times[0,T)\).

The reaction proposition bounds the reaction quotient at the pole and at the cap [S11:210–219]:

> At late times on \(0<r\le\frac18\sqrt\delta\), the reaction quotient
> \[
> c(x,t)=\frac{2\langle\Rm(\Ric),\Ric\rangle}{|\Ric|^2}
> \quad\text{where }|\Ric|>0
> \]
> satisfies both bounds
> \begin{equation}\label{eq:reaction-two}
> c\le\frac{2(q-1)+C\sqrt q}{r^2},\qquad
> c\le\frac{C_*}{\theta^2}.
> \end{equation}

The three barrier propositions fix the parameters in order and control the pole, the interior, and the geometric exterior [S12:71–73] [S12:158–159] [S12:225–226].

The rate corollary is the quantitative form, with `d_q = (q + 1 − √((q + 1)(q − 7)))/2` [S12:284–299]:

> For every sufficiently large integer \(q\), set
> \[
> d_q=\frac{q+1-\sqrt{(q+1)(q-7)}}2.
> \]
> For every sufficiently large even integer \(k\), with the threshold
> allowed to depend on \(q\), there is a smooth Ricci flow on
> \(\Sp^2\times\Sp^{q+1}\) with finite maximal time \(T\), uniformly
> bounded scalar curvature, and constants \(0<c\le C<\infty\) such that
> \[
> c(T-t)^{-2k/d_q}\le\max_M|\Rm|(\cdot,t)
> \le C(T-t)^{-2k/d_q}
> \]
> for all sufficiently late times. In particular, one fixed dimension
> admits such flows with an unbounded discrete set of power-law Type-II
> curvature exponents. The flow, \(T\), and the constants may depend on
> \(q\) and \(k\).

The four-dimensional paper runs the other way. It models the spatial geometry near `T` as a tree of Ricci-flat ALE pieces with an outermost scale `a(t)` [S20:100–105], and studies a renormalized Einstein–Hilbert functional whose differential is the integral pairing with the Einstein tensor `½ R g − Ric` [S20:109–123]. The degeneration-tree theorem makes the tree precise [S22:31–60], the buffered-interval proposition selects time intervals on which the outermost scale changes by a fixed factor [S22:1270–1282], the exterior Ricci proposition is the parabolic input [S23:334–336], the collar extension theorem extends the flow across the collar [S24:82–108], and the final contradiction shows the energy must vanish [S25:476].

The companion paper is the static half. It fixes a tree of Ricci-flat ALE model spaces, selects a path through the tree, and proves the tree inequality [S34:136–141]:

> Fix a finite rooted tree with the end identifications and order-$20$ metric bounds of Section~\ref{ell:setup}. Let $(g_j,L^{(j)},M_j)$ satisfy the compact vertex convergence, the same uniform half-end and root-end bounds, and Equation~\eqref{eq:tree-ricci-error} through order $10$, with every $L_e^{(j)}\to\infty$ and $M_j\to0$. Then, in physical root units,
> \begin{equation}
>                          E(g_j)=o(M_j).
>  \label{ell:little-oh}
> \end{equation}
> For an index with $M_j=0$, the assertion means $E(g_j)=0$. The little-oh is taken for this fixed tree; it does not assert a power exponent uniform over different trees.

Its path-selection theorem realizes finite sign conditions and finite prescribed limits along a real analytic path, with every actual coordinate eventually monotone or constant [S35:67–79], and its corollary gives the finite variation the elliptic argument consumes [S35:90–97].

## Headline theorem

The counterexample manuscript's main theorem is the flow itself [S7:69–78]:

> There are an integer \(q\ge10\), a time \(T>0\), and a smooth Ricci flow \(g(t)\), \(0\le t<T\),
> on the closed connected manifold \(M=\Sp^2\times\Sp^{q+1}\), with smooth initial metric, such that
> \[
> \sup_{M\times[0,T)}|R_{g(t)}|<\infty,
> \qquad
> \lim_{t\uparrow T}\max_M|\Rm_{g(t)}|=\infty.
> \]
> In particular, \(T\) is the finite maximal existence time of this flow.

The manuscript states what the theorem does not say: it refutes the unrestricted all-dimensions formulation, and it draws no dimension-four conclusion [S7:80–84].

The four-dimensional manuscript's extension theorem is the positive half [S20:12–20]:

> Let \(M\) be a closed connected smooth four-manifold, let
> \(0<T<\infty\), and let \(g(t)\), \(0\le t<T\), be a smooth Ricci
> flow with smooth initial metric. If
> \[
>  \sup_{M\times[0,T)}|R(g(t))|<\infty,
> \]
> then there are \(\varepsilon>0\) and a smooth Ricci flow
> \(\widetilde g(t)\) on \(M\), \(0\le t<T+\varepsilon\), such that
> \(\widetilde g(t)=g(t)\) for every \(t<T\).

Its corollary is the contrapositive, and it is the dimension-four detection statement [S20:32–36]:

> If a Ricci flow on a closed smooth four-manifold has finite maximal
> smooth existence time \(T\), then
> \[
>  \limsup_{t\uparrow T}\max_{x\in M}R(g(t))(x)=+\infty.
> \]

The proof of the corollary is short [S20:40–45]:

> The equation \((\partial_t-\Delta)R=2|\Ric|^2\) and the maximum
> principle give a scalar lower bound on a finite time interval. A finite
> upper limit in the assertion would therefore give a uniform absolute
> bound near \(T\), and smoothness supplies the bound on the remaining
> compact time interval. The componentwise extension just described
> contradicts maximality.

The companion's abstract states its own result [S31:9–15]:

> We prove a sequential elliptic inequality for the renormalized
> Einstein--Hilbert functional on a fixed finite tree of four-dimensional
> Ricci-flat spaces. As the joining lengths diverge and the scale-neutral
> weighted Ricci error $M$ tends to zero, the functional satisfies $E=o(M)$.
> The root end has decay exponent greater than one, and every joined quotient
> group is nontrivial. We also prove the multivariable path-selection theorem
> for asymptotic expansions used to obtain this estimate.

## Three manuscripts

The release names three manuscripts, all dated September 24, 2026 [S4:4] [S16:4] [S29:4]. Their bibtex titles are `A closed Ricci flow with bounded scalar curvature and finite-time curvature blowup` [S4:11], `Bounded scalar curvature and smooth extension of four-dimensional Ricci flow` [S16:11], and `Path selection and an elliptic inequality on degenerating Ricci-flat trees` [S29:11]. The PDFs are `paper.pdf` in each root [S5] [S17] [S30].

**Manuscript A** ships `build/paper.tex` (47 lines), six section files, two TikZ figures, and a bibliography of 13 entries [S6] [S7] [S8] [S9] [S10] [S11] [S12] [S13] [S14] [S15]. The sections are `01-introduction.tex` (147 lines), `02-construction.tex` (154, "The construction used as input" [S8:1]), `03-geometry.tex` (222, "Geometric identities and profile consequences" [S9:1]), `04-cap.tex` (247, "Curvature at the radius and cap scales" [S10:1]), `05-reaction.tex` (261, "A dimension-explicit Ricci reaction bound" [S11:1]), `06-barriers.tex` (320, "Comparison and the scalar-curvature bound" [S12:1]). The introduction's organization paragraph names Sections `sec:construction`, `sec:geometry`, `sec:cap`, `sec:reaction`, `sec:barriers`, and the build tree defines all five [S7:129–138]. The figures are `scales.tex` (20 lines) [S13] and `drift-cylinder.tex` (18) [S14]. The bibliography's Wang entry is the dimension-three theorem the introduction cites [S15:88–96]:

> \bibitem{Wang2012}
> B.~Wang,
> \emph{On the conditions to extend Ricci flow (II)},
> Int. Math. Res. Not. IMRN 2012, no. 14, 3192--3223.

**Manuscript B** ships `build/paper.tex` (28 lines), a `build/preamble.tex` (48 lines), six section files, two figures, and a 440-line `build/sources/references.bib` [S18] [S19] [S20] [S21] [S22] [S23] [S24] [S25] [S26] [S27] [S28]. Its preamble's pdf subject is "Bounded scalar curvature, Ricci flow, and Ricci-flat bubble trees" [S19:46–48]. The section files are `01-introduction.tex` (200 lines), `02-static-input.tex` (158, "The static input and its normalization" [S21:1]), `04-geometry.tex` (1,432, "Small-scale geometry and the outermost scale" [S22:1]), `05-parabolic.tex` (806, "Concentration estimates for the Ricci equation" [S23:1]), `06-collar.tex` (863, "An exterior extension determined by a fixed collar" [S24:1]), `07-contradiction.tex` (813, "Functional change and the contradiction" [S25:1]) — the numbering skips `03`. The introduction's proof-structure paragraph names Sections `sec:geometry`, `sec:parabolic`, `sec:collar`, `sec:contradiction`, and names `sec:static-input` when it records the companion's input [S20:160–185] [S20:125–131]. The figures are `buffered-intervals.tex` (35 lines) [S26] and `overview.tex` (21) [S27].

**Manuscript C** ships `build/paper.tex` (34 lines), a `build/preamble.tex` (80 lines), seven section files, one figure, and a 146-line `build/references.bib` [S31] [S32] [S33] [S34] [S35] [S36] [S37] [S38] [S39] [S40] [S41]. Its preamble's pdf subject is "Quasianalytic path selection, Ricci-flat bubble trees, and a renormalized Einstein-Hilbert functional" [S32:78–80]. Its sections are `01-introduction.tex` (193 lines), `02-tree.tex` (156, "Tree geometry and the renormalized functional" [S34:1]), `03-path.tex` (1,320, "Selection of paths at several exponential ends" [S35:1]), `04-family.tex` (572, "Augmented inverses and the analytic family" [S36:1]), `05-tails.tex` (213, "Tail expansions and prescribed growth" [S37:1]), `06-length.tex` (166, "Expansion in one length" [S38:1]), `07-observables.tex` (307, "Scalar expansions and the tree inequality" [S39:1]). The introduction's organization paragraph names `sec:elliptic`, `sec:path`, `sec:family`, `ell:tail-calculus`, `ell:length-expansion`, `ell:scalar-calculus`, and the build tree defines all six [S33:176–184]. The figure is `tree-scales.tex` (21 lines) [S40].

## Prior work

The counterexample manuscript's introduction names the literature it stands on. The necessity of unbounded full curvature is Hamilton's theorem [S7:16–17]. The scalar-curvature conjecture is attributed to Bamler, page 756, and to Šešum [S7:18–24]. Wang's dimension-three theorem is the restriction the introduction states [S7:26–38]. Type II singularity analysis is Angenent–Knopf's shrinking neck, Gu–Zhu, and the AIK analysis [S7:40–51]. The scalar-sign obstruction and the Ricci reaction bound come from Stolarski's Proposition 5.3, with Bohm's maximum-principle machinery [S7:53–66]. The bibliography carries 13 entries, including Hamilton 1995, Angenent–Knopf 2004, Bamler 2018, Bohm 1999, Cao–Zhu 2006, Gu–Zhu 2008, AIK 2015, Krylov 2006, Ladyzhenskaya–Solonnikov–Ural'tseva 1968, Šešum 2005, Shi 1989, Stolarski 2019, and Wang 2012 [S15:1–96].

The four-dimensional manuscript's prior work is the extension literature: Hamilton, Šešum, Bamler, Liu–Simon, Li–Li, and the Kähler–Ricci work of Zhang [S20:50–72]. The Type I literature is Enders–Müller–Topping on global Type I and Buzano–Di Matteo on local Type I [S20:73–84]. The ALE compactness background is Anderson, Bando, Bando–Kasue–Nakajima, and Cheeger–Tian [S20:86–98]. The collar construction uses the classical compatibility between metric strains and linearized curvature, together with Korn control modulo rigid motions, citing Khavkine 2017 and Ciarlet–Ciarlet 2005 [S20:152–154]. Its bibliography is 440 lines [S28].

The companion's prior work is the renormalization and desingularization literature. Haslhofer's renormalized Perelman functional treats relative energies near steady solitons; Deruelle and Ozuch subtract the mass contribution in their analytic ALE functional and discuss the corresponding renormalized Hilbert–Einstein expression, with a weighted Łojasiewicz inequality near a fixed Ricci-flat ALE background that holds without an integrability hypothesis [S33:21–35]. The path-selection method's ancestry is the quasianalytic asymptotic algebras of Speissegger and of Galal, Kaiser, and Speissegger [S33:94–102]. The elliptic reduction's predecessors are Biquard's Eguchi–Hanson gluing construction modulo a finite-dimensional obstruction space, Ozuch's uniform inverse estimates for desingularization trees, and Ozuch's treatment of potentially nonintegrable Einstein deformations — the introduction states this is methodological motivation, not an invocation of that paper's results for the tree inequality proved here [S33:117–132]. The DeTurck–Kazdan coordinate method is the classical setting of the gauge cancellation [S33:106–115]. Its bibliography is 146 lines [S41].

## History

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

| ID | File | Lines | What it carries |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | Release blurb, three manuscript links, three manuscript abstracts |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 351's `\resultentry`, at line 800 |
| S3 | [`notes/tables/catalog.tsv`](../../../notes/tables/catalog.tsv) | 373 | Reading ledger row for family 351 |
| S4 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/README.md`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/README.md) | 17 | Manuscript A README: date, bibtex key |
| S5 | [`preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf`](../../../preprints/A-closed-Ricci-flow-with-bounded-scalar-curvature-and-finite-time-curvature-blowup-September-24-2026/paper.pdf) | — | Manuscript A PDF |
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
| S17 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/paper.pdf) | — | Manuscript B PDF |
| S18 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/paper.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/paper.tex) | 28 | Manuscript B preamble, theorem environments, section order |
| S19 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/preamble.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/preamble.tex) | 48 | Manuscript B preamble and pdf metadata |
| S20 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/01-introduction.tex) | 200 | Extension theorem, scalar-blowup corollary, the degeneration tree, the functional, the proof structure |
| S21 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/02-static-input.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/02-static-input.tex) | 158 | The static input and its normalization |
| S22 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/04-geometry.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/04-geometry.tex) | 1,432 | The degeneration-tree theorem and the buffered-interval proposition |
| S23 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/05-parabolic.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/05-parabolic.tex) | 806 | The exterior Ricci proposition |
| S24 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/06-collar.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/06-collar.tex) | 863 | The collar extension theorem |
| S25 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/07-contradiction.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sections/07-contradiction.tex) | 813 | The functional-smallness proposition and the final contradiction |
| S26 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/buffered-intervals.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/buffered-intervals.tex) | 35 | The buffered-intervals figure |
| S27 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/overview.tex`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/figures/overview.tex) | 21 | The overview figure |
| S28 | [`preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sources/references.bib`](../../../preprints/Bounded-scalar-curvature-and-smooth-extension-of-four-dimensional-Ricci-flow-September-24-2026/build/sources/references.bib) | 440 | Manuscript B bibliography |
| S29 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/README.md`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/README.md) | 17 | Manuscript C README: date, bibtex key |
| S30 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf) | — | Manuscript C PDF |
| S31 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/paper.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/paper.tex) | 34 | Manuscript C preamble, abstract, theorem environments, section order |
| S32 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/preamble.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/preamble.tex) | 80 | Manuscript C preamble and pdf metadata |
| S33 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/01-introduction.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/01-introduction.tex) | 193 | The tree, the functional, the prior work, the path selection, the organization |
| S34 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/02-tree.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/02-tree.tex) | 156 | The tree inequality |
| S35 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/03-path.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/03-path.tex) | 1,320 | The path-selection theorem and the variation corollary |
| S36 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/04-family.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/04-family.tex) | 572 | The inverses, gauge, analytic family, and comparison |
| S37 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/05-tails.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/05-tails.tex) | 213 | The tail expansions and prescribed growth |
| S38 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/06-length.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/06-length.tex) | 166 | The expansion in one length |
| S39 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/07-observables.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/sections/07-observables.tex) | 307 | The scalar expansions that complete the theorem |
| S40 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/figures/tree-scales.tex`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/figures/tree-scales.tex) | 21 | The tree-scales figure |
| S41 | [`preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/references.bib`](../../../preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/build/references.bib) | 146 | Manuscript C bibliography |
