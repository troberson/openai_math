[Notes](../../README.md) / [Summaries](../README.md) / [Differential geometry](../../index/disciplines/differential-geometry.md) / [Family 349](../../index/differential-geometry/349-solomon-yau-least-volume-conjecture.md)

# 349 — The Solomon–Yau least-volume conjecture

[Index page](../../index/differential-geometry/349-solomon-yau-least-volume-conjecture.md)

## Original CONTENTS.md summary

The release's blurb for family 349 [S1:8483]:

> 349. The Solomon–Yau least-volume conjecture. Proves the Solomon–Yau least-volume conjecture for minimal hypersurfaces of round spheres. For every m ≥ 2, a closed connected minimal immersion into the unit sphere $S^{m+1}$ with non-totally-geodesic image has volume at least that of the smallest minimal Clifford product, counting covering multiplicity.

The manuscript's abstract [S1:8492]:

> Volume is measured on the domain, including covering multiplicities. The theorem resolves the stated least-volume conjecture positively. The threshold is attained by a Clifford product minimizing \(a_m\).

The catalog abstract in `overview.tex` is the blurb quoted above [S2:796]. The bibtex key the release ships [S3:10–13]:

> @misc{OAI:The-Solomon-Yau-least-volume-theorem-September-23-2026,
>   author = {{OpenAI}},
>   title = {{The Solomon--Yau least-volume theorem}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

The comparison objects are the minimal Clifford products. The introduction names them [S6:4–8]:

> The equator is the least-volume closed minimal hypersurface of a unit round sphere. The next volume level is a subtler question: minimality alone gives no immediate control of topology, curvature, or singular limits of a sequence of hypersurfaces. The natural comparison examples are the minimal Clifford products

The Clifford products are minimal, and the threshold is the minimum over their volumes [S6:15–25]:

> The two factors have opposite principal curvatures, whose weighted sum vanishes; these products are therefore minimal. For each integer \(m\ge2\), set \[ a_m=\min_{1\le k<m}\Vol_m(\mathcal C_{k,m-k}). \] The assertion that \(a_m\) is the first volume level above the equator is the least-volume question in Yau's collection \cite[Problem 31]Yau1994. The modern formulation in \cite[Conjecture 1.12(ii)]GeLi2021 calls it the Solomon–Yau conjecture. We prove this formulation with its full immersion scope.

The theorem is the volume bound [S6:27–34]:

> \begin{theorem}\label{thm:volume}
> Let \(m\ge2\), let \(M^m\) be a closed connected smooth manifold, and let
> \(F:M\to S^{m+1}\) be a smooth minimal immersion into the unit round sphere.
> If \(F(M)\) is not totally geodesic, then
> \[
> \Vol\bigl(M,F^*g_{\mathrm{round}}\bigr)\ge a_m.
> \]
> \end{theorem}

The volume is measured on the domain, which is what makes the covering-multiplicity clause part of the statement [S6:36–38]:

> Volume is measured on the domain, including covering multiplicities.
> The theorem resolves the stated least-volume conjecture positively.
> The threshold is attained by a Clifford product minimizing \(a_m\).

## Graduate summary

The nonembedded case reduces to the embedded one by a counting argument. A point with $q$ preimages forces the domain volume to at least $q|S^m|$, and the Clifford threshold is below twice the sphere volume, so any counterexample must be embedded [S6:72–81]:

> The nonembedded case has a useful independent reduction. A point with \(q\) preimages forces domain volume at least \(q|S^m|\), as proved by Nguyen \cite[Corollary 4.8 and Remark 4.9]Nguyen2023 and by Ge and Li \cite[Theorem 1.2 and Corollary 1.3]GeLi2022. Since \(a_m<2|S^m|\), any counterexample to Theorem   would be embedded. We give the short cone-monotonicity proof in Proposition  , retaining tangent and coincident sheets. The more recent general embedded-hypersurface bounds of Ge and Li \cite[Theorems 1.4 and 1.6]GeLi2026II remain below the sharp Clifford threshold, which their Conjecture 1.3 still poses as the target.

The first construction is a curvature inequality. A two-point maximum compares the normal at one point with every other point, and a smooth upper-test comparison gives the integrated bound [S6:93–106]:

> The first construction controls both signs of the principal curvatures. For a closed embedded non-equatorial minimal hypersurface \(\Sigma^m\), with second fundamental form \(A\), a two-point maximum compares the normal at one point with every other point of \(\Sigma\). The reflection calculation is related to the two-point methods in \cite[Section 2]Brendle2013 and \cite[Section 2]AHLW2015. We prove the required static differential inequality directly, including diagonal contacts and repeated principal curvatures. A smooth upper-test comparison then gives \[ \int_\Sigma |A|^2\ge m|\Sigma|. \] This proves the lower-bound assertion of Perdomo's average-curvature conjecture \cite[Conjecture 1.5]GeLi2021.

Combined with the conformal and spectral mechanism, index $m+3$ forces a Clifford product, so a counterexample must have a further negative area direction [S6:107–111]:

> Combining it with the conformal and spectral mechanism of \cite[Theorem 3.1]Perdomo2004, and keeping track of equality in each spectral inequality, shows that index \(m+3\) forces a Clifford product (Proposition  ). A counterexample must therefore have a further negative direction for area.

The manuscript notes that the curvature and index results appear independently in a recent preprint, and states what its own construction does not need [S6:113–120]:

> The average-curvature inequality and this embedded index classification also appear in Nifa's recent preprint \cite[Theorem 1.1 and Corollary 7.3]Nifa2026, which proves a stronger Schrödinger quadratic-form inequality. His construction uses the sum of two tangent-ball curvatures and a weak supersolution. Here a two-sided maximum and a smooth Poisson comparison suffice for the integrated bound. We give the curvature and index arguments in full, independently of the volume comparison that follows.

The second construction is Lorentzian. Form the Euclidean cone over the hypersurface, take its signed distance function, and regard the graph as a hypersurface in a space with one time coordinate [S6:122–131]:

> The second construction turns that direction into a strict area improvement. Form the Euclidean cone over \(\Sigma\), take its signed distance function, and regard the graph as a hypersurface in a space with one time coordinate. Lorentz boosts preserve the difference between squared spatial length and squared time. Intersecting the transformed graph with the unit spatial sphere produces level sets whose areas are controlled on the fixed source \(\Sigma\). At each closest-point contact, minimality makes a nonnegative Jacobian matrix have fixed trace; its determinant bounds the area of the level. This estimate works even when closest points are not unique.

The boost and level parameters give a family on projective space whose cohomology detects the topology [S6:133–143]:

> The boost parameters and the level parameter give a family on \(\mathbbRP^{m+3}\). Its boundary cycles have area at most \(|\Sigma|\), and its fillings change to their complements around the projective generator. The associated degree-one cohomology class has nonzero \((m+3)\)-rd power. This is the topological detection used in Section  ; it replaces a topology assumption on \(\Sigma\) itself. The original hypersurface is the unique area maximum, with a uniform gap away from its central parameter. Its extra index direction removes that maximum while preserving the detection and the absence of mass concentration (Proposition  ).

Detection forces a uniform area gap above the equator, so the min–max theorem produces varifolds above the equator even after the strict deformation [S6:147–153]:

> Detection forces every such family to contain a boundary of a half-volume region with zero centroid. Spherical isoperimetry and its hemisphere equality case give a uniform area threshold \(\gamma_m>|S^m|\) for these boundaries (Lemma  ). The min–max theorem therefore produces stationary integral varifolds above the equator, even after the strict deformation.

The volume proof is an induction on $m$ whose regularity step is radial splitting of cone tangents [S6:155–162]:

> The volume proof proceeds by induction on \(m\). Assuming only the lower-dimensional volume statements, Section   proves regularity for the subthreshold limits arising both from minimizing sequences and from min–max. The mechanism is radial splitting: tangents at nonzero points of a Euclidean cone split off a line, reducing their classification to a smaller cone dimension. This gives smooth connected links of multiplicity one without applying the unknown dimension-\(m\) volume theorem to those links.

The contradiction is the last step [S6:164–171]:

> Compactness therefore attains a least counterexample of area \(H\), with \(\gamma_m\le H<a_m\). Its index exceeds \(m+3\), so the deformed family has maximum area strictly below \(H\). Min–max produces a varifold of mass in \([\gamma_m,H)\), and the same regularity argument makes it a smooth connected multiplicity-one hypersurface. Its mass is above the equator and below \(H\): it is a smaller counterexample, the desired contradiction. The induction starts at \(m=2\), with no lower-dimensional volume hypothesis.

The organization names seven sections [S6:173–179]:

> Section   establishes the volume normalization and immersion reduction. Section   proves curvature and index rigidity. Section   establishes detection and the precise min–max interface before Section   constructs and deforms the Lorentz-distance family. Section   proves the cone induction and exact attainment, and Section   completes the proof.

**Prior (my training data, not this repo).** As of my early-2025 cutoff, the Solomon–Yau least-volume conjecture is open. I recall the equator as the known least-volume closed minimal hypersurface of the unit sphere, the Clifford torus as the sharp two-dimensional case via the Marques–Neves Willmore theorem, and Cheng–Li–Yau's dimension-dependent volume gap above the equator by heat-kernel comparison. A proof for every hypersurface dimension in the immersion category, using a Lorentzian deformation of the cone and a projective cohomology detection, is not something I recall from the literature. The prior is a training-data recollection, self-rated, and the repo supplies only the manuscript's citations.

## Consequences

The direct consequence is that the least-volume question in Yau's Problem 31 and the conjecture in Ge–Li's formulation are resolved positively, with the full immersion scope, for every $m\ge2$ [S6:27–34] [S6:36–38]. The volume bound is sharp: the threshold $a_m$ is attained by a Clifford product. The two-point curvature inequality also proves the lower-bound assertion of Perdomo's average-curvature conjecture [S6:93–106], and the index classification is a rigidity statement in its own right [S6:107–111].

Inside the release, the family is at tier T0 with no formalized manuscript, no scope note, no comparator, and no verification bundle [S14:345]. The proof is 2,409 lines of section text across seven sections, and nothing in `lean/` names it, so no Lean or comparator run can confirm any part of the argument.

What has not been checked: no Lean, lake, or comparator run was performed, and there is nothing in the release to run for this family; I read only the introduction line by line, so every section-file claim in the machinery paragraphs is a section name the introduction names, not a statement read in the section file — the seven section files carry 177, 585, 401, 757, 442 and 44 lines that I did not read; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 12 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | Release blurb, manuscript link, manuscript abstract |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | Family 349's `\resultentry`, at line 796 |
| S3 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/README.md`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/README.md) | 18 | Manuscript README: date, bibtex key |
| S4 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/paper.pdf`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/paper.pdf) | 13143 | Manuscript PDF |
| S5 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/paper.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/paper.tex) | 83 | Preamble, theorem environments, abstract |
| S6 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/introduction.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/introduction.tex) | 179 | Main theorem, the Clifford threshold, the immersion reduction, the curvature and index steps, the Lorentz family, the induction, the organization |
| S7 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/preliminaries.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/preliminaries.tex) | 177 | Volume normalization and immersion reduction |
| S8 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/index.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/index.tex) | 585 | Curvature and index rigidity |
| S9 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/minmax.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/minmax.tex) | 401 | Detection and the min–max interface |
| S10 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/family.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/family.tex) | 757 | The Lorentz-distance family and its deformation |
| S11 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/cones.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/cones.tex) | 442 | The cone induction and exact attainment |
| S12 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/conclusion.tex`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/sections/conclusion.tex) | 44 | The completed proof |
| S13 | [`preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/references.bib`](../../../preprints/The-Solomon-Yau-least-volume-theorem-September-23-2026/build/references.bib) | 414 | Manuscript bibliography |
| S14 | [`notes/tables/catalog.tsv`](../../../notes/tables/catalog.tsv) | 373 | Reading ledger row for family 349 |

## Bibliography

- Allard, William K., On the first variation of a varifold (1972)
- Andrews, Ben, Han, Xiaoli, Li, Haizhong, Wei, Yong, Non-collapsing for hypersurface flows in the sphere and hyperbolic space (2012)
- Andrews, Ben, Han, Xiaoli, Li, Haizhong, Wei, Yong, Non-collapsing for hypersurface flows in the sphere and hyperbolic space (2015)
- Bernstein, Jacob, Wang, Lu, Lower bounds on density for topologically nontrivial minimal cones up to dimension six (2025)
- Blatt, Simon, On the analyticity of solutions to non-linear elliptic partial differential equations (2024)
- Brendle, Simon, Embedded minimal tori in $S^3$ and the Lawson conjecture (2013)
- Cheng, Siu Yuen, Li, Peter, Yau, Shing-Tung, Heat equations on minimal submanifolds and their applications (1984)
- Cheng, Qing-Ming, Wei, Guoxin, Zeng, Yuting, Area of minimal hypersurfaces (2019)
- Federer, Herbert, Geometric Measure Theory (1969)
- Federer, Herbert, Colloquium lectures on geometric measure theory (1978)
- Ge, Jianquan, Li, Fagui, A lower bound for $L^2$ length of second fundamental form on minimal hypersurfaces (2021)
- Ge, Jianquan, Li, Fagui, Volume gap for minimal submanifolds in spheres (2022)
- Ge, Jianquan, Li, Fagui, Volume gap for minimal submanifolds in spheres, II (2026)
- B{ö}gelein, Verena, Duzaar, Frank, Fusco, Nicola, A quantitative isoperimetric inequality on the sphere (2017)
- Hatcher, Allen, Algebraic Topology (2002)
- Li, Peter, Yau, Shing-Tung, A new conformal invariant and its applications to the Willmore conjecture and the first eigenvalue of compact surfaces (1982)
- Marques, Fernando C., Neves, Andr{é}, Min-max theory and the Willmore conjecture (2014)
- Marques, Fernando C., Neves, Andr{é}, Existence of infinitely many minimal hypersurfaces in positive Ricci curvature (2017)
- Marques, Fernando C., Neves, Andr{é}, Morse index of multiplicity one min-max minimal hypersurfaces (2021)
- Mityagin, Boris S., The Zero Set of a Real Analytic Function (2015)
- Morrey, Jr., Charles B., On the analyticity of the solutions of analytic non-linear elliptic systems of partial differential equations. Part I. Analyticity in the interior (1958)
- Nguyen, Manh Tien, Weighted monotonicity theorems and applications to minimal surfaces of $\mathbb H^n$ and $S^n$ (2023)
- Nifa, Anass, Sharp {Schrödinger} inequalities for embedded hypersurfaces (2026)
- Obata, Morio, Certain conditions for a Riemannian manifold to be isometric with a sphere (1962)
- Perdomo, Oscar, On the average of the scalar curvature of minimal hypersurfaces of spheres with low stability index (2004)
- Perdomo, Oscar M., On the index of minimal hypersurfaces of spheres (2019)
- Pitts, Jon T., Existence and Regularity of Minimal Surfaces on Riemannian Manifolds (1981)
- Schoen, Richard, Simon, Leon, Regularity of stable minimal hypersurfaces (1981)
- Simon, Leon, Introduction to Geometric Measure Theory (2018)
- Simons, James, Minimal varieties in Riemannian manifolds (1968)
- Tang, Zizhou, Yan, Wenjiao, Isoparametric foliation and Yau conjecture on the first eigenvalue (2013)
- Taylor, Michael E., Pseudodifferential Operators
- Taylor, Michael E., Spectral Theory
- Viana, Celso, Isoperimetry and volume preserving stability in real projective spaces (2023)
- White, Brian, Currents and flat chains associated to varifolds, with an application to mean curvature flow (2009)
- White, Brian, Rectifiability of flat chains (1999)
- White, Brian, Topics in GMT (Math 258)
- Yau, Shing-Tung, Open problems in geometry (1994)
