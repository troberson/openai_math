[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 348](../index/differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md)

# 348 — Nonnegatively curved Einstein four-manifolds and a topological gap

[Index page](../index/differential-geometry/348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md)

## Original CONTENTS.md summary

The release's blurb for family 348 

> 348. Nonnegative-curvature Einstein classification and an L2 topological gap. Classifies closed connected Einstein four-manifolds with positive Einstein constant and nonnegative sectional curvature: up to scaling, their universal Riemannian covers are the round S4, Fubini–Study $\mathbb{CP}^2$, or a product of equal round two-spheres. A closed simply connected nonnegatively curved four-manifold is diffeomorphic to one of these whenever the scale-invariant L2 norm of its trace-free Ricci curvature lies below a universal positive constant. [S1:8449]

The zero-plane manuscript's abstract 

> We prove that a closed Einstein four-manifold with positive Einstein constant, nonnegative sectional curvature, and a zero-curvature plane has universal Riemannian cover isometric to a product of two round two-spheres. Under the normalization $\mathop{\mathrm{Ric}}\nolimits =3g$, both spheres have radius $1/\sqrt3$. The proof extends coupled estimates for the two Weyl curvature blocks to the boundary of the sectional-curvature cone and determines their equality case. [S1:8458]

The L2 gap manuscript's abstract 

> We prove a universal, scale-invariant L2 gap for the trace-free Ricci tensor on simply connected closed four-manifolds with nonnegative sectional curvature. If the trace-free Ricci energy is sufficiently small, the manifold is diffeomorphic to S4, $\mathbb{CP}^2$, or $S^2\times S^2$. The proof uses the classification of positive-Einstein, nonnegatively curved four-manifolds supplied by the companion zero-plane rigidity theorem, stated explicitly as the classification premise of our result. No auxiliary curvature, volume, diameter, injectivity-radius, or Sobolev bound is required. The conclusion concerns the smooth manifold, not an isometry of the original metric. [S1:8467]

The positively-curved manuscript's abstract 

> We prove the classification conjecture for connected smooth closed Einstein four-manifolds with strictly positive sectional curvature. Up to positive scaling and isometry, every such manifold is the round four-sphere, the complex projective plane with its Fubini–Study metric, or real projective four-space with its round metric. No orientability assumption is needed. [S1:8476]

The three abstracts state three different results: a product-of-spheres rigidity under one zero-curvature plane, a diffeomorphism classification under a small L2 energy, and the classification conjecture under strict positivity. The catalog abstract in `overview.tex` is the blurb quoted above [S2:794]. The bibtex key the zero-plane manuscript ships [S3:10–13]:

> @misc{OAI:Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026,
>   author = {{OpenAI}},
>   title = {{Zero-Plane Rigidity for Einstein Four-Manifolds}},
>   howpublished = {OpenAI Math Release preprint

and the L2 gap manuscript's [S10:10–13]:

> @misc{OAI:An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026,
>   author = {{OpenAI}},
>   title = {{An $L^2$ Einstein Gap for Nonnegatively Curved Four-Manifolds}},
>   howpublished = {OpenAI Math Release preprint

and the positively-curved manuscript's [S14:8–11]:

> @misc{OAI:Positively-curved-Einstein-four-manifolds-September-23-2026,
>   author = {{OpenAI}},
>   title = {{Positively curved Einstein four-manifolds}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

The zero-plane manuscript's hypothesis is one plane, at one point. Its introduction states the result 

> factor have zero curvature. We prove that, for a closed Einstein four-manifold with positive Einstein constant, a single zero-curvature plane already forces this product geometry on the universal cover. [S6:10–12]

Its theorem is the rigidity [S6:14–26]:

> \begin{theorem}[Zero-plane rigidity]\label{thm:main}
> Let $(M^4,g)$ be a connected smooth closed Riemannian manifold satisfying
> \[
>  \operatorname{Ric}_g=3g,\qquad K_g(\sigma)\ge0
> \]
> for every tangent two-plane $\sigma$. If $K_g(\sigma_0)=0$ for at least
> one tangent two-plane, then the universal Riemannian cover is isometric to
> \[
>  S^2(1/\sqrt3)\times S^2(1/\sqrt3)
> \]
> with its product metric. In particular, the tangent bundle of the
> universal cover is the orthogonal sum of two parallel rank-two subbundles.
> \end{theorem}

The normalization fixes only the scale 

> Here $S^2(r)$ denotes the round sphere of radius $r$, and closed means compact without boundary. No orientation, symmetry, or topological condition is assumed on $M$. The Einstein normalization only fixes the scale: for $\mathrm{Ric}=\lambda g$ with $\lambda>0$, the two radii are $1/\sqrt\lambda$. [S6:28–32]

The same paper also gives the full classification under nonnegative sectional curvature, as a corollary 

> The argument also gives the full classification under nonnegative sectional curvature. [S6:76–77]

The corollary is the three-model statement [S6:79–85]:

> \begin{corollary}\label{cor:nonnegative-classification}
> Let $(M^4,g)$ be connected, smooth, and closed, with
> $\mathrm{Ric}=3g$ and nonnegative sectional curvature. Its universal
> Riemannian cover is one of the round $S^4$ of curvature $1$, the complex
> projective plane with its Fubini--Study metric normalized by
> $\mathrm{Ric}=3g$, or $S^2(1/\sqrt3)\times S^2(1/\sqrt3)$.
> \end{corollary}

The positively-curved manuscript states the classification conjecture for strict positivity, with no orientability assumption [S17:13–19]:

> \begin{theorem}\label{thm:classification}
> Let $(M,g)$ be a connected smooth closed Einstein four-manifold with
> strictly positive sectional curvature, without an orientability
> assumption. There is a constant $a>0$ such that $(M,ag)$ is isometric to
> the standard round $S^4$, to $\mathbb{CP}^2$ with its Fubini--Study
> metric, or to $\mathbb{RP}^4$ with its standard round metric.
> \end{theorem}

The L2 gap manuscript does not classify metrics; it classifies smooth manifolds under a small integral curvature error, and it takes the classification as a premise [S12:88–99]:

> \begin{theorem}\label{thm:gap}
> Assume Classification Assumption~\ref{ass:classification}. There is a
> universal constant $\varepsilon_0>0$ with the following property.
> If $(M,g)$ is a connected, simply connected, smooth closed Riemannian
> four-manifold with $\sec_g\ge0$ and
> \[
>  \int_M\left|\Ric_g-\frac{\Scal_g}{4}g\right|_g^2\,d\mu_g
>  <\varepsilon_0,
> \]
> then $M$ is diffeomorphic, without a prescribed orientation, to the
> standard smooth $S^4$, $\mathbb{CP}^2$, or $S^2\times S^2$.
> \end{theorem}

The premise it assumes is the zero-plane manuscript's corollary [S12:74–83]:

> \begin{assumption}\label{ass:classification}
> Every connected smooth closed Riemannian four-manifold $(N,h)$ satisfying
> \[
>  \Ric_h=3h,\qquad \sec_h\ge0
> \]
> has universal Riemannian cover isometric to one of the following:
> the round $S^4$ of sectional curvature $1$; Fubini--Study $\mathbb{CP}^2$ normalized
> by $\mathrm{Ric}=3g$; or
> $S^2(1/\sqrt3)\times S^2(1/\sqrt3)$ with its product metric.
> \end{assumption}

The L2 gap manuscript states the premise is used only for an exactly Einstein metric, and that no auxiliary bound is needed 

> There are no auxiliary bounds on curvature, volume, diameter, injectivity radius, Sobolev constants, or curvature derivatives. The conclusion is about the underlying smooth manifold, rather than the original metric. This distinction matters because small $L^2$ error does not itself give pointwise curvature control. [S12:101–105]

## Graduate summary

The zero-plane manuscript's reduction is to the two Weyl blocks. Its introduction sets up the variables 

> Choose an orientation and let $\Lambda^+$ and $\Lambda^-$ be the rank-three eigenspaces of the Hodge star on two-forms. The Einstein curvature operator has blocks $\mathrm{Id}+T$ and $\mathrm{Id}+U$, where $T,U$ are symmetric and trace-free. They are the self-dual and anti-self-dual Weyl blocks. Set \[ v=\frac|T|{\sqrt6},\qquad b=\frac|U|{\sqrt6},\qquad x=-\lambda_{\min}(T),\qquad y=-\lambda_{\min}(U). \] All matrix norms are Hilbert–Schmidt norms. As proved in Lemma  , the smallest sectional curvature is $1-(x+y)/2$, and \[ v\le x\le2v,\qquad b\le y\le2b,\qquad x+y\le2. \] [S6:95–109]

The zero-plane hypothesis is used only in the reduction, not in the estimates 

> If one Weyl block vanished identically, the metric would be half-conformally flat. The classical compact positive-scalar Einstein classification of Hitchin  , with conformal Einstein rigidity  , would identify our simply connected cover with the standard $S^4$ or $\mathbb{CP}^2$ up to scale; see also \cite[Remark 7]Derdzinski1983. Both have strictly positive sectional curvature. We may therefore assume throughout the remaining proof that neither block vanishes identically. The zero-plane hypothesis is used only in this reduction: the remaining estimates assume only nonnegative sectional curvature and that neither block vanishes identically. Individual blocks may still vanish at some points. [S6:113–123]

The proof has three stages 

> Write $\mathbf E f$ for the integral of $f$ divided by the volume of $M$. The proof now has three stages. First, the separate gaps $\mathbf E v^2,\mathbf E b^2\ge1$, a weighted variance inequality, and an upper volume deficit force \[ \mathbf E v^2=\mathbf E b^2. \] Second, a weighted Hessian identity and explicit polynomial inequalities couple the two blocks and force $dv=db=0$ almost everywhere. Third, the gaps and $v+b\le2$ give $v=b=1$. The weak norm equations then imply that both Weyl blocks are parallel, each with spectrum $(2,-1,-1)$. Their simple eigenlines produce the parallel tangent splitting. [S6:125–137]

The boundary case is the point. Three features let the estimates reach it 

> Three features allow these estimates to reach the boundary. The upper volume estimate integrates over the domain before the first conjugate point and needs no lower bound on the injectivity radius. The weighted Hessian identity needs a nonnegative quadratic form, so it remains valid when that form has a kernel. At a zero of one Weyl block, the pointwise algebraic estimates are obtained by introducing a small nonzero block and shrinking the opposite block while keeping its derivative data fixed. The decisive strictness then comes from the fact that the gradient of a Lipschitz function vanishes almost everywhere on a level set. This forces constant Weyl norms without requiring strict sectional positivity. [S6:139–148]

The organization names five sections and an appendix of exact polynomial certificates 

> Section   develops the curvature identities, including the weak norm equations at zeros. Sections   and   establish the scalar estimates and moment balance. Sections   and   give the Hessian and coupling inequalities. Section   resolves their equality case and proves Theorem  . Appendix   supplies the exact polynomial certificates, including all boundary faces. [S6:150–157]

The L2 gap manuscript's energy is the trace-free Ricci energy, scale-invariant in dimension four 

> For a Riemannian four-manifold $(M,g)$, let \[ E_g=\mathrmRic_g-\frac{\mathrmScal_g}4g, \qquad \mathcal D(g)=\int_M |E_g|_g^2\,d\mu_g. \] The tensor $E_g$ vanishes precisely when $g$ is Einstein, provided that $M$ is connected. The energy $\mathcal D$ is unchanged by constant rescaling in dimension four. It is therefore natural to ask whether a classification of Einstein metrics remains valid at the level of smooth manifolds when $\mathcal D$ is small. We address this question under nonnegative sectional curvature. [S12:59–69]

Its method is a smoothing argument that does not assume sectional curvature survives the flow 

> A second point concerns sectional curvature. Its nonnegativity is not assumed to persist under the flow. Instead, we bound the integral of its negative part by $Ct$. The limit is an exactly Einstein shrinking flow, and its explicit scaling converts this weak defect estimate into nonnegative sectional curvature of the fixed Einstein metric. This gives the classification-independent compactness statement of Proposition  ; classification then identifies the limiting manifold. [S12:164–171]

Its smoothing step isolates a globally small high part of the curvature 

> Smoothing from small critical curvature concentration was developed, in particular, by Chan, Chen, and Lee  . The formulation used here isolates a globally small _high part_ of the curvature. Consider a sequence $(M_j,g_j)$ satisfying the geometric hypotheses of Theorem   with $\mathcal D(g_j)\to0$. After normalization, nonnegative sectional curvature gives, for a fixed threshold $K_0$, \[ \left\lVert (|\mathrmRm_g_j|-K_0)_+\right\rVert_L^2(g_j)\longrightarrow0. \] A moving threshold propagates this estimate. It yields both a uniform Sobolev inequality and noncollapse along each existing flow; a curvature-concentration contradiction then establishes a common lifespan. The same tail bound controls the evolving Einstein error. Thus the high-part formulation supplies both the regularization and the defect estimate needed for the gap argument. [S12:148–162]

The L2 gap manuscript names the prior work it does not use, and names the companion as its premise 

> The exact Einstein problem has been studied under several additional hypotheses. Gursky and LeBrun obtained the Fubini–Study conclusion for nonnegative sectional curvature and a nonzero positive-definite intersection form  . Cao and Tran established sectional-pinching criteria  , and Liu classified the $T^2$-invariant case on closed simply connected four-manifolds  . Here the classification premise is supplied by _Zero-Plane Rigidity for Einstein Four-Manifolds_ \cite[Corollary 1.2]ZeroPlane. Our problem is instead to transfer that exact classification to metrics with small critical Ricci error. [S12:109–118]

The zero-plane manuscript's context paragraph names the antecedents it builds on 

> The classification of positively curved Einstein four-manifolds has a long history. Berger's rigidity under strict quarter pinching   was followed by quantitative curvature conditions of Yang, Costa, and Cao–Tran  . Gursky–LeBrun obtained the Fubini–Study conclusion under nonnegative sectional curvature and a nonzero positive-definite intersection form \cite[Theorem A]GurskyLeBrun1999. Their separate Weyl-norm gaps and analysis of the two Weyl blocks are important antecedents of the argument here. Scalar combinations of the two Weyl norms also appear in Yang's coupling argument \cite[Section 6]Yang2000 and in Cao–Tran \cite[Proposition 2.2]CaoTran2018. Under nonnegative isotropic curvature, which is a different curvature condition, the Einstein local-symmetry theorem in dimension four is due to Micallef–Wang \cite[Theorem 4.4]MicallefWang1993; Brendle established the analogous rigidity in higher dimensions \cite[Theorem 1]Brendle2010. [S6:36–51]

**Prior (my training data, not this repo).** As of my early-2025 cutoff, the classification of closed Einstein four-manifolds with positive sectional curvature is not a theorem I recall; the Hitchin-Thorpe inequality is classical, and the signs of the Euler characteristic and signature constrain Einstein four-manifolds. I recall LeBrun's 11/8 theorem for the Fubini-Study case under a positive intersection form, and the Micallef–Wang local-symmetry theorem under nonnegative isotropic curvature. I do not recall a rigidity theorem that uses a single zero-curvature plane at a single point to force a product-of-spheres universal cover, nor a scale-invariant L2 gap for the trace-free Ricci tensor that transfers a classification to the level of diffeomorphism type. The prior is a training-data recollection, self-rated, and the repo supplies only the manuscripts' citations.

## Consequences

The direct consequence is that one zero-curvature plane at one point, added to the Einstein condition and nonnegative sectional curvature, forces the universal cover to be a product of two equal round spheres [S6:14–26], and the same argument yields the full three-model classification under nonnegative curvature [S6:79–85]. The positively-curved manuscript's consequence is the classification conjecture under strict positivity, with no orientability assumption [S17:13–19]. The L2 gap manuscript's consequence is weaker and deliberately so: a small trace-free Ricci energy pins the diffeomorphism type, not the metric, and it reaches that by assuming the classification as a premise [S12:88–99] [S12:101–105].

Inside the release, the family is at tier T2 with no formalized manuscript. The scope note covers the positively-curved manuscript, names the comparator, and states the status [S21:9] [S21:11]. The comparator `EinsteinFour` carries three `sorry` occurrences, on the oriented classification, on `classificationOn`, and on the connected closed classification that includes the real projective quotient [S22:190–194] [S22:202–203] [S22:208–216]. The `main_results` table has no entry for `EinsteinFour`, so no declaration names this family [S23:344]. The two verification bundles check finite arithmetic and their `COVERAGE.md` says the scope is finite arithmetic, not the geometric reductions [S3:28–33] [S9] [S20].

What has not been checked: no Lean, lake, or comparator run was performed, and the comparator carries three `sorry`, so `lean/ComparatorChallenges/EinsteinFour.lean` was read as source text, not elaborated; the three manuscripts carry 863, 180 and 157 lines in their main text files, and I read only the introductions line by line, so every section-file claim is a section name the introduction names, not a statement read in the section file; the verification scripts were read as documents, not executed, so the identity and exact-value counts their READMEs state are their claim, not a run I observed; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 13 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb, three manuscript links, three manuscript abstracts |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family 348's `\resultentry`, at line 794 |
| S3 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/README.md`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/README.md) | 33 | Zero-plane README: date, bibtex key, verification command and record |
| S4 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf) | 16656 | Zero-plane manuscript PDF |
| S5 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/paper.tex`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/paper.tex) | 54 | Zero-plane preamble, theorem environments, abstract |
| S6 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/sections/01-introduction.tex`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/sections/01-introduction.tex) | 157 | Main theorem, the corollary, the Weyl-block reduction, the three stages, the boundary argument, the organization |
| S7 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/references.tex`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/references.tex) | 100 | Zero-plane bibliography |
| S8 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/README.md`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/README.md) | 24 | Verification entry point and the file list, including the optional scalar check |
| S9 | [`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/COVERAGE.md`](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/COVERAGE.md) | 8 | Scope of the finite arithmetic checks |
| S10 | [`preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/README.md`](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/README.md) | 18 | L2 gap README: date, bibtex key, no verification section |
| S11 | [`preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf`](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf) | 9643 | L2 gap manuscript PDF |
| S12 | [`preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/main.tex`](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/main.tex) | 863 | Abstract, classification assumption, gap theorem, the smoothing and defect arguments |
| S13 | [`preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/references.bib`](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/references.bib) | 191 | L2 gap bibliography |
| S14 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/README.md`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/README.md) | 27 | Positively-curved README: date, bibtex key, verification command and record |
| S15 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf) | 20242 | Positively-curved manuscript PDF |
| S16 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/paper.tex`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/paper.tex) | 56 | Positively-curved preamble, theorem environments, abstract |
| S17 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/sections/01-introduction.tex) | 180 | Classification theorem, the three models, the proof ingredients |
| S18 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/references.tex`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/references.tex) | 142 | Positively-curved bibliography |
| S19 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/README.md`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/README.md) | 23 | Verification entry point and the file list, without the optional scalar check |
| S20 | [`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/COVERAGE.md`](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/COVERAGE.md) | 8 | Scope of the finite arithmetic checks, byte-identical to S9 |
| S21 | [`lean/docs/348.md`](../../../lean/docs/348.md) | 15 | Scope note: what the formalization covers, the comparator, the status |
| S22 | [`lean/ComparatorChallenges/EinsteinFour.lean`](../../../lean/ComparatorChallenges/EinsteinFour.lean) | 222 | Comparator stub: the classification targets, with three `sorry` |
| S23 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Reading ledger row for family 348 |

## Bibliography

- W. Ambrose, _Parallel Translation of Riemannian Curvature_, Ann. of Math. (2) **64** (1956), no. 2, 337–363. doi:10.2307/1969978.
- M. Berger, _Sur quelques variétés d'Einstein compactes_, Ann. Mat. Pura Appl. **53** (1961), 89–95. doi:10.1007/BF02417787.
- M. Berger, _Sur quelques variétés d'Einstein compactes_, Ann. Mat. Pura Appl. **53** (1961), 89–95. doi:10.1007/BF02417787.
- F. Boudaoud, F. Caruso, and M.-F. Roy, _Certificates of Positivity in the Bernstein Basis_, Discrete Comput. Geom. **39** (2008), no. 4, 639–655. doi:10.1007/s00454-007-9042-x.
- F. Boudaoud, F. Caruso, and M.-F. Roy, _Certificates of Positivity in the Bernstein Basis_, Discrete Comput. Geom. **39** (2008), no. 4, 639–655. doi:10.1007/s00454-007-9042-x.
- S. Brendle, _Einstein manifolds with nonnegative isotropic curvature are locally symmetric_, Duke Math. J. **151** (2010), no. 1, 1–21. doi:10.1215/00127094-2009-061.
- S. Brendle, _Einstein manifolds with nonnegative isotropic curvature are locally symmetric_, Duke Math. J. **151** (2010), no. 1, 1–21. doi:10.1215/00127094-2009-061.
- D. M. J. Calderbank, P. Gauduchon, and M. Herzlich, _Refined Kato inequalities and conformal weights in Riemannian geometry_, J. Funct. Anal. **173** (2000), no. 1, 214–255. doi:10.1006/jfan.2000.3563.
- D. M. J. Calderbank, P. Gauduchon, and M. Herzlich, _Refined Kato inequalities and conformal weights in Riemannian geometry_, J. Funct. Anal. **173** (2000), no. 1, 214–255. doi:10.1006/jfan.2000.3563.
- Cao, Xiaodong, Tran, Hung, Einstein four-manifolds of pinched sectional curvature (2018)
- L. F. Di Cerbo, _A rigidity theorem for Einstein 4-manifolds with sectional curvature of a fixed sign, and its consequences_, Math. Ann. **396** (2026), article 11. doi:10.1007/s00208-026-03547-w. Author version: arXiv:2503.09570v3.
- L. F. Di Cerbo, _A rigidity theorem for Einstein 4-manifolds with sectional curvature of a fixed sign, and its consequences_, Math. Ann. **396** (2026), article 11. doi:10.1007/s00208-026-03547-w. Author version: arXiv:2503.09570v3.
- Chan, Pak-Yeung, Chen, Eric, Lee, Man-Chun, Small curvature concentration and Ricci flow smoothing (2022)
- Cheeger, Jeff, Colding, Tobias H., Lower bounds on Ricci curvature and the almost rigidity of warped products (1996)
- Cheeger, Jeff, Gromov, Mikhail, Taylor, Michael, Finite propagation speed, kernel estimates for functions of the Laplace operator, and the geometry of complete Riemannian manifolds (1982)
- L. Cheng, _On Positively Curved Einstein Four-Manifolds with Euler Characteristic at Most Three_, arXiv:2609.23337v1 [math.DG], September 20, 2026.
- L. Cheng, _On Positively Curved Einstein Four-Manifolds with Euler Characteristic at Most Three_, arXiv:2609.23337v1 [math.DG], September 20, 2026.
- E. Costa, _On Einstein four-manifolds_, J. Geom. Phys. **51** (2004), no. 2, 244–255. doi:10.1016/j.geomphys.2003.10.013.
- E. Costa, _On Einstein four-manifolds_, J. Geom. Phys. **51** (2004), no. 2, 244–255. doi:10.1016/j.geomphys.2003.10.013.
- G. Catino and D. Dameno, _Conformal Kähler rigidity of Einstein four-manifolds_, 2026, arXiv:2607.21538v1 [math.DG].
- D. Dameno, _A note on Einstein metrics and Riemannian twistor spaces_, Math. Z. **313** (2026), article 86. doi:10.1007/s00209-026-04100-w.
- A. Derdziński, _Self-dual Kähler manifolds and Einstein manifolds of dimension four_, Compositio Math. **49** (1983), no. 3, 405–433. Journal archive.
- A. Derdziński, _Self-dual Kähler manifolds and Einstein manifolds of dimension four_, Compositio Math. **49** (1983), no. 3, 405–433. Journal archive.
- P. B. Gilkey, _Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem_, Publish or Perish, 1984. Author-hosted electronic reprint, 1996.
- P. B. Gilkey, _Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem_, Publish or Perish, 1984. Author-hosted electronic reprint, 1996.
- Gursky, Matthew J., LeBrun, Claude, On Einstein manifolds of positive sectional curvature (1999)
- Hamilton, Richard S., Three-manifolds with positive Ricci curvature (1982)
- Hamilton, Richard S., A compactness property for solutions of the Ricci flow (1995)
- A. Hatcher, _Algebraic Topology_, Cambridge University Press, Cambridge, 2002. Author-hosted text.
- N. J. Hitchin, _Kählerian twistor spaces_, Proc. London Math. Soc. (3) **43** (1981), no. 1, 133–150. doi:10.1112/plms/s3-43.1.133.
- N. J. Hitchin, _Kählerian twistor spaces_, Proc. London Math. Soc. (3) **43** (1981), no. 1, 133–150. doi:10.1112/plms/s3-43.1.133.
- S. Ilias, _Constantes explicites pour les inégalités de Sobolev sur les variétés riemanniennes compactes_, Ann. Inst. Fourier (Grenoble) **33** (1983), no. 2, 151–165. doi:10.5802/aif.921.
- S. Ilias, _Constantes explicites pour les inégalités de Sobolev sur les variétés riemanniennes compactes_, Ann. Inst. Fourier (Grenoble) **33** (1983), no. 2, 151–165. doi:10.5802/aif.921.
- W. Klingenberg, _Contributions to Riemannian Geometry in the Large_, Ann. of Math. (2) **69** (1959), no. 3, 654–666. doi:10.2307/1970029.
- C. Koca, _Einstein Hermitian metrics of positive sectional curvature_, Proc. Amer. Math. Soc. **142** (2014), no. 6, 2119–2122. doi:10.1090/S0002-9939-2014-11929-0. Author version: arXiv:1112.4181v3.
- Th. Friedrich and H. Kurke, _Compact four-dimensional self-dual Einstein manifolds with positive scalar curvature_, Math. Nachr. **106** (1982), no. 1, 271–299. doi:10.1002/mana.19821060124.
- M. J. Gursky and C. LeBrun, _On Einstein manifolds of positive sectional curvature_, Ann. Global Anal. Geom. **17** (1999), no. 4, 315–328. doi:10.1023/A:1006597912184.
- M. J. Gursky and C. LeBrun, _On Einstein manifolds of positive sectional curvature_, Ann. Global Anal. Geom. **17** (1999), no. 4, 315–328. doi:10.1023/A:1006597912184.
- De Lellis, Camillo, Topping, Peter M., Almost-Schur lemma (2012)
- T. Liu, _Toric Einstein 4-manifolds with non-negative sectional curvature_, Ann. Global Anal. Geom. **67** (2025), article 14. doi:10.1007/s10455-025-09990-3.
- Liu, Tianyue, Toric Einstein 4-manifolds with non-negative sectional curvature (2025)
- M. J. Gursky and A. Malchiodi, _Einstein four-manifolds of positive sectional curvature and ADM mass_, arXiv:2609.30803v1 [math.DG], submitted September 25, 2026.
- M. J. Gursky and A. Malchiodi, _Einstein four-manifolds of positive sectional curvature and ADM mass_, arXiv:2609.30803v1 [math.DG], submitted September 25, 2026.
- H. P. McKean, Jr., and I. M. Singer, _Curvature and the eigenvalues of the Laplacian_, J. Differential Geom. **1** (1967), 43–69. doi:10.4310/jdg/1214427880.
- U. Abresch and W. T. Meyer, _Injectivity Radius Estimates and Sphere Theorems_, in _Comparison Geometry_, MSRI Publications **30**, Cambridge University Press, 1997, 1–47. Publisher-hosted text.
- Morgan, John, Tian, Gang, Ricci Flow and the Poincaré Conjecture (2007)
- S. B. Myers, _Riemannian manifolds with positive mean curvature_, Duke Math. J. **8** (1941), no. 2, 401–404. doi:10.1215/S0012-7094-41-00832-3.
- S. B. Myers, _Riemannian manifolds with positive mean curvature_, Duke Math. J. **8** (1941), no. 2, 401–404. doi:10.1215/S0012-7094-41-00832-3.
- B. O'Neill, _The fundamental equations of a submersion_, Michigan Math. J. **13** (1966), no. 4, 459–469. doi:10.1307/mmj/1028999604.
- M. Obata, _Certain conditions for a Riemannian manifold to be isometric with a sphere_, J. Math. Soc. Japan **14** (1962), no. 3, 333–340. doi:10.2969/jmsj/01430333.
- M. Obata, _Certain conditions for a Riemannian manifold to be isometric with a sphere_, J. Math. Soc. Japan **14** (1962), no. 3, 333–340. doi:10.2969/jmsj/01430333.
- OpenAI, _Positively curved Einstein four-manifolds_, OpenAI Math Release preprint OAI:Positively-curved-Einstein-four-manifolds-September-23-2026, 2026.
- OpenAI, Zero-Plane Rigidity for Einstein Four-Manifolds (2026)
- Perelman, Grisha, The entropy formula for the Ricci flow and its geometric applications (2002)
- Petersen, Peter, Sprouse, Chadwick, Integral curvature bounds, distance estimates and applications (1998)
- G. de Rham, _Sur la réductibilité d'un espace de Riemann_, Comment. Math. Helv. **26** (1952), 328–344. doi:10.1007/BF02564308.
- M.-F. Roy, _Certificates of Positivity in the Bernstein basis_, Oberwolfach Reports, report 14/2007, 800–804. Report on joint work with F. Boudaoud, F. Caruso, and R. Leroy. Report.
- M.-F. Roy, _Certificates of Positivity in the Bernstein basis_, Oberwolfach Reports, report 14/2007, 800–804. Report on joint work with F. Boudaoud, F. Caruso, and R. Leroy. Report.
- Shi, Wan-Xiong, Deforming the metric on complete Riemannian manifolds (1989)
- Sprouse, Chadwick, Integral curvature bounds and bounded diameter (2000)
- J. L. Synge, _On the Connectivity of Spaces of Positive Curvature_, Quart. J. Math. Oxford Ser. **7** (1936), 316–320. doi:10.1093/qmath/os-7.1.316.
- Topping, Peter M., Remarks on Hamilton's compactness theorem for Ricci flow (2014)
- X. Cao and H. Tran, _Einstein four-manifolds of pinched sectional curvature_, Adv. Math. **335** (2018), 322–342. doi:10.1016/j.aim.2018.07.003. Author version: arXiv:1612.06023v2.
- X. Cao and H. Tran, _Einstein four-manifolds of pinched sectional curvature_, Adv. Math. **335** (2018), 322–342. doi:10.1016/j.aim.2018.07.003. Author version: arXiv:1612.06023v2.
- D. Gilbarg and N. S. Trudinger, _Elliptic Partial Differential Equations of Second Order_, Classics in Mathematics, Springer, Berlin, 2001, reprint of the 1998 edition. doi:10.1007/978-3-642-61798-0.
- M.-F. Bidaut-Véron and L. Véron, _Nonlinear elliptic equations on compact Riemannian manifolds and asymptotics of Emden equations_, Invent. Math. **106** (1991), 489–539. doi:10.1007/BF01243922. Erratum, Invent. Math. **112** (1993), no. 2, 445. doi:10.1007/BF01232442.
- M. J. Micallef and M. Y. Wang, _Metrics with nonnegative isotropic curvature_, Duke Math. J. **72** (1993), no. 3, 649–672. doi:10.1215/S0012-7094-93-07224-9.
- M. J. Micallef and M. Y. Wang, _Metrics with nonnegative isotropic curvature_, Duke Math. J. **72** (1993), no. 3, 649–672. doi:10.1215/S0012-7094-93-07224-9.
- D. Yang, _Rigidity of Einstein 4-manifolds with positive curvature_, Invent. Math. **142** (2000), no. 2, 435–450. doi:10.1007/PL00005792.
- D. Yang, _Rigidity of Einstein 4-manifolds with positive curvature_, Invent. Math. **142** (2000), no. 2, 435–450. doi:10.1007/PL00005792.
- Ye, Rugang, The logarithmic Sobolev and Sobolev inequalities along the Ricci flow (2015)
- Zhang, Qi S., A uniform Sobolev inequality under Ricci flow (2007)
