Notes / Summaries / Differential geometry / [Family 348](../../index/differential-geometry/348-einstein-four-manifold-classification-and-l2-gap.md)

# 348 — Nonnegatively curved Einstein four-manifolds and a topological gap

## Original CONTENTS.md summary

The release's blurb for family 348 [S1:8449]:

> 348. Nonnegative-curvature Einstein classification and an L2 topological gap. Classifies closed connected Einstein four-manifolds with positive Einstein constant and nonnegative sectional curvature: up to scaling, their universal Riemannian covers are the round S4, Fubini–Study $\mathbb{CP}^2$, or a product of equal round two-spheres. A closed simply connected nonnegatively curved four-manifold is diffeomorphic to one of these whenever the scale-invariant L2 norm of its trace-free Ricci curvature lies below a universal positive constant.

The zero-plane manuscript's abstract [S1:8458]:

> We prove that a closed Einstein four-manifold with positive Einstein constant, nonnegative sectional curvature, and a zero-curvature plane has universal Riemannian cover isometric to a product of two round two-spheres. Under the normalization $\mathop{\mathrm{Ric}}\nolimits =3g$, both spheres have radius $1/\sqrt3$. The proof extends coupled estimates for the two Weyl curvature blocks to the boundary of the sectional-curvature cone and determines their equality case.

The L2 gap manuscript's abstract [S1:8467]:

> We prove a universal, scale-invariant L2 gap for the trace-free Ricci tensor on simply connected closed four-manifolds with nonnegative sectional curvature. If the trace-free Ricci energy is sufficiently small, the manifold is diffeomorphic to S4, $\mathbb{CP}^2$, or $S^2\times S^2$. The proof uses the classification of positive-Einstein, nonnegatively curved four-manifolds supplied by the companion zero-plane rigidity theorem, stated explicitly as the classification premise of our result. No auxiliary curvature, volume, diameter, injectivity-radius, or Sobolev bound is required. The conclusion concerns the smooth manifold, not an isometry of the original metric.

The positively-curved manuscript's abstract [S1:8476]:

> We prove the classification conjecture for connected smooth closed Einstein four-manifolds with strictly positive sectional curvature. Up to positive scaling and isometry, every such manifold is the round four-sphere, the complex projective plane with its Fubini–Study metric, or real projective four-space with its round metric. No orientability assumption is needed.

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

The zero-plane manuscript's hypothesis is one plane, at one point. Its introduction states the result [S6:10–12]:

> factor have zero curvature. We prove that, for a closed Einstein four-manifold with positive Einstein constant, a single zero-curvature plane already forces this product geometry on the universal cover.

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

The normalization fixes only the scale [S6:28–32]:

> Here $S^2(r)$ denotes the round sphere of radius $r$, and closed means compact without boundary. No orientation, symmetry, or topological condition is assumed on $M$. The Einstein normalization only fixes the scale: for $\mathrm{Ric}=\lambda g$ with $\lambda>0$, the two radii are $1/\sqrt\lambda$.

The same paper also gives the full classification under nonnegative sectional curvature, as a corollary [S6:76–77]:

> The argument also gives the full classification under nonnegative sectional curvature.

The corollary is the three-model statement [S6:79–85]:

> \begin{corollary}\label{cor:nonnegative-classification}
> Let $(M^4,g)$ be connected, smooth, and closed, with
> $\operatorname{Ric}=3g$ and nonnegative sectional curvature. Its universal
> Riemannian cover is one of the round $S^4$ of curvature $1$, the complex
> projective plane with its Fubini--Study metric normalized by
> $\operatorname{Ric}=3g$, or $S^2(1/\sqrt3)\times S^2(1/\sqrt3)$.
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
> standard smooth $S^4$, $\CP^2$, or $S^2\times S^2$.
> \end{theorem}

The premise it assumes is the zero-plane manuscript's corollary [S12:74–83]:

> \begin{assumption}\label{ass:classification}
> Every connected smooth closed Riemannian four-manifold $(N,h)$ satisfying
> \[
>  \Ric_h=3h,\qquad \sec_h\ge0
> \]
> has universal Riemannian cover isometric to one of the following:
> the round $S^4$ of sectional curvature $1$; Fubini--Study $\CP^2$ normalized
> by $\Ric=3g$; or
> $S^2(1/\sqrt3)\times S^2(1/\sqrt3)$ with its product metric.
> \end{assumption}

The L2 gap manuscript states the premise is used only for an exactly Einstein metric, and that no auxiliary bound is needed [S12:101–105]:

> There are no auxiliary bounds on curvature, volume, diameter, injectivity radius, Sobolev constants, or curvature derivatives. The conclusion is about the underlying smooth manifold, rather than the original metric. This distinction matters because small $L^2$ error does not itself give pointwise curvature control.

## Graduate summary

The zero-plane manuscript's reduction is to the two Weyl blocks. Its introduction sets up the variables [S6:95–109]:

> Choose an orientation and let $\Lambda^+$ and $\Lambda^-$ be the rank-three eigenspaces of the Hodge star on two-forms. The Einstein curvature operator has blocks $\mathrm{Id}+T$ and $\mathrm{Id}+U$, where $T,U$ are symmetric and trace-free. They are the self-dual and anti-self-dual Weyl blocks. Set \[ v=\frac{|T|}{\sqrt6},\qquad b=\frac{|U|}{\sqrt6},\qquad x=-\lambda_{\min}(T),\qquad y=-\lambda_{\min}(U). \] All matrix norms are Hilbert--Schmidt norms. As proved in Lemma~ , the smallest sectional curvature is $1-(x+y)/2$, and \[ v\le x\le2v,\qquad b\le y\le2b,\qquad x+y\le2. \]

The zero-plane hypothesis is used only in the reduction, not in the estimates [S6:113–123]:

> If one Weyl block vanished identically, the metric would be half-conformally flat. The classical compact positive-scalar Einstein classification of Hitchin~ , with conformal Einstein rigidity~ , would identify our simply connected cover with the standard $S^4$ or $\mathbb{CP}^2$ up to scale; see also \cite[Remark~7]{Derdzinski1983}. Both have strictly positive sectional curvature. We may therefore assume throughout the remaining proof that neither block vanishes identically. The zero-plane hypothesis is used only in this reduction: the remaining estimates assume only nonnegative sectional curvature and that neither block vanishes identically. Individual blocks may still vanish at some points.

The proof has three stages [S6:125–137]:

> Write $\mathbf E f$ for the integral of $f$ divided by the volume of $M$. The proof now has three stages. First, the separate gaps $\mathbf E v^2,\mathbf E b^2\ge1$, a weighted variance inequality, and an upper volume deficit force \[ \mathbf E v^2=\mathbf E b^2. \] Second, a weighted Hessian identity and explicit polynomial inequalities couple the two blocks and force $dv=db=0$ almost everywhere. Third, the gaps and $v+b\le2$ give $v=b=1$. The weak norm equations then imply that both Weyl blocks are parallel, each with spectrum $(2,-1,-1)$. Their simple eigenlines produce the parallel tangent splitting.

The boundary case is the point. Three features let the estimates reach it [S6:139–148]:

> Three features allow these estimates to reach the boundary. The upper volume estimate integrates over the domain before the first conjugate point and needs no lower bound on the injectivity radius. The weighted Hessian identity needs a nonnegative quadratic form, so it remains valid when that form has a kernel. At a zero of one Weyl block, the pointwise algebraic estimates are obtained by introducing a small nonzero block and shrinking the opposite block while keeping its derivative data fixed. The decisive strictness then comes from the fact that the gradient of a Lipschitz function vanishes almost everywhere on a level set. This forces constant Weyl norms without requiring strict sectional positivity.

The organization names five sections and an appendix of exact polynomial certificates [S6:150–157]:

> Section~  develops the curvature identities, including the weak norm equations at zeros. Sections~  and~  establish the scalar estimates and moment balance. Sections~  and~  give the Hessian and coupling inequalities. Section~  resolves their equality case and proves Theorem~ . Appendix~  supplies the exact polynomial certificates, including all boundary faces.

The L2 gap manuscript's energy is the trace-free Ricci energy, scale-invariant in dimension four [S12:59–69]:

> For a Riemannian four-manifold $(M,g)$, let \[ E_g=\Ric_g-\frac{\Scal_g}{4}g, \qquad \mathcal D(g)=\int_M |E_g|_g^2\,d\mu_g. \] The tensor $E_g$ vanishes precisely when $g$ is Einstein, provided that $M$ is connected. The energy $\mathcal D$ is unchanged by constant rescaling in dimension four. It is therefore natural to ask whether a classification of Einstein metrics remains valid at the level of smooth manifolds when $\mathcal D$ is small. We address this question under nonnegative sectional curvature.

Its method is a smoothing argument that does not assume sectional curvature survives the flow [S12:164–171]:

> A second point concerns sectional curvature. Its nonnegativity is not assumed to persist under the flow. Instead, we bound the integral of its negative part by $Ct$. The limit is an exactly Einstein shrinking flow, and its explicit scaling converts this weak defect estimate into nonnegative sectional curvature of the fixed Einstein metric. This gives the classification-independent compactness statement of Proposition~ ; classification then identifies the limiting manifold.

Its smoothing step isolates a globally small high part of the curvature [S12:148–162]:

> Smoothing from small critical curvature concentration was developed, in particular, by Chan, Chen, and Lee  . The formulation used here isolates a globally small _high part_ of the curvature. Consider a sequence $(M_j,g_j)$ satisfying the geometric hypotheses of Theorem~  with $\mathcal D(g_j)\to0$. After normalization, nonnegative sectional curvature gives, for a fixed threshold $K_0$, \[ \left\lVert (|\Rm_{g_j}|-K_0)_+\right\rVert_{L^2(g_j)}\longrightarrow0. \] A moving threshold propagates this estimate. It yields both a uniform Sobolev inequality and noncollapse along each existing flow; a curvature-concentration contradiction then establishes a common lifespan. The same tail bound controls the evolving Einstein error. Thus the high-part formulation supplies both the regularization and the defect estimate needed for the gap argument.

The L2 gap manuscript names the prior work it does not use, and names the companion as its premise [S12:109–118]:

> The exact Einstein problem has been studied under several additional hypotheses. Gursky and LeBrun obtained the Fubini--Study conclusion for nonnegative sectional curvature and a nonzero positive-definite intersection form  . Cao and Tran established sectional-pinching criteria  , and Liu classified the $T^2$-invariant case on closed simply connected four-manifolds  . Here the classification premise is supplied by _Zero-Plane Rigidity for Einstein Four-Manifolds_ \cite[Corollary~1.2]{ZeroPlane}. Our problem is instead to transfer that exact classification to metrics with small critical Ricci error.

The zero-plane manuscript's context paragraph names the antecedents it builds on [S6:36–51]:

> The classification of positively curved Einstein four-manifolds has a long history. Berger's rigidity under strict quarter pinching   was followed by quantitative curvature conditions of Yang, Costa, and Cao--Tran  . Gursky--LeBrun obtained the Fubini--Study conclusion under nonnegative sectional curvature and a nonzero positive-definite intersection form \cite[Theorem~A]{GurskyLeBrun1999}. Their separate Weyl-norm gaps and analysis of the two Weyl blocks are important antecedents of the argument here. Scalar combinations of the two Weyl norms also appear in Yang's coupling argument~\cite[Section~6]{Yang2000} and in Cao--Tran~\cite[Proposition~2.2]{CaoTran2018}. Under nonnegative isotropic curvature, which is a different curvature condition, the Einstein local-symmetry theorem in dimension four is due to Micallef--Wang \cite[Theorem~4.4]{MicallefWang1993}; Brendle established the analogous rigidity in higher dimensions~\cite[Theorem~1]{Brendle2010}.

**Prior (my training data, not this repo).** As of my early-2025 cutoff, the classification of closed Einstein four-manifolds with positive sectional curvature is not a theorem I recall; the Hitchin-Thorpe inequality is classical, and the signs of the Euler characteristic and signature constrain Einstein four-manifolds. I recall LeBrun's 11/8 theorem for the Fubini-Study case under a positive intersection form, and the Micallef–Wang local-symmetry theorem under nonnegative isotropic curvature. I do not recall a rigidity theorem that uses a single zero-curvature plane at a single point to force a product-of-spheres universal cover, nor a scale-invariant L2 gap for the trace-free Ricci tensor that transfers a classification to the level of diffeomorphism type. The prior is a training-data recollection, self-rated, and the repo supplies only the manuscripts' citations.

## Consequences

The direct consequence is that one zero-curvature plane at one point, added to the Einstein condition and nonnegative sectional curvature, forces the universal cover to be a product of two equal round spheres [S6:14–26], and the same argument yields the full three-model classification under nonnegative curvature [S6:79–85]. The positively-curved manuscript's consequence is the classification conjecture under strict positivity, with no orientability assumption [S17:13–19]. The L2 gap manuscript's consequence is weaker and deliberately so: a small trace-free Ricci energy pins the diffeomorphism type, not the metric, and it reaches that by assuming the classification as a premise [S12:88–99] [S12:101–105].

Inside the release, the family is at tier T2 with no formalized manuscript. The scope note covers the positively-curved manuscript, names the comparator, and states the status [S21:9] [S21:11]. The comparator `EinsteinFour` carries three `sorry` occurrences, on the oriented classification, on `classificationOn`, and on the connected closed classification that includes the real projective quotient [S22:190–194] [S22:202–203] [S22:208–216]. The `main_results` table has no entry for `EinsteinFour`, so no declaration names this family [S23:344]. The two verification bundles check finite arithmetic and their `COVERAGE.md` says the scope is finite arithmetic, not the geometric reductions [S3:28–33] [S9] [S20].

What has not been checked: no Lean, lake, or comparator run was performed, and the comparator carries three `sorry`, so `lean/ComparatorChallenges/EinsteinFour.lean` was read as source text, not elaborated; the three manuscripts carry 863, 180 and 157 lines in their main text files, and I read only the introductions line by line, so every section-file claim is a section name the introduction names, not a statement read in the section file; the verification scripts were read as documents, not executed, so the identity and exact-value counts their READMEs state are their claim, not a run I observed; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 13 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `CONTENTS.md` | 9142 | Release blurb, three manuscript links, three manuscript abstracts |
| S2 | `overview.tex` | 859 | Family 348's `\resultentry`, at line 794 |
| S3 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/README.md` | 33 | Zero-plane README: date, bibtex key, verification command and record |
| S4 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf` | 16656 | Zero-plane manuscript PDF |
| S5 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/paper.tex` | 54 | Zero-plane preamble, theorem environments, abstract |
| S6 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/sections/01-introduction.tex` | 157 | Main theorem, the corollary, the Weyl-block reduction, the three stages, the boundary argument, the organization |
| S7 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/references.tex` | 100 | Zero-plane bibliography |
| S8 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/README.md` | 24 | Verification entry point and the file list, including the optional scalar check |
| S9 | `preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/COVERAGE.md` | 8 | Scope of the finite arithmetic checks |
| S10 | `preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/README.md` | 18 | L2 gap README: date, bibtex key, no verification section |
| S11 | `preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf` | 9643 | L2 gap manuscript PDF |
| S12 | `preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/main.tex` | 863 | Abstract, classification assumption, gap theorem, the smoothing and defect arguments |
| S13 | `preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/references.bib` | 191 | L2 gap bibliography |
| S14 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/README.md` | 27 | Positively-curved README: date, bibtex key, verification command and record |
| S15 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf` | 20242 | Positively-curved manuscript PDF |
| S16 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/paper.tex` | 56 | Positively-curved preamble, theorem environments, abstract |
| S17 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/sections/01-introduction.tex` | 180 | Classification theorem, the three models, the proof ingredients |
| S18 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/references.tex` | 142 | Positively-curved bibliography |
| S19 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/README.md` | 23 | Verification entry point and the file list, without the optional scalar check |
| S20 | `preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/COVERAGE.md` | 8 | Scope of the finite arithmetic checks, byte-identical to S9 |
| S21 | `lean/docs/348.md` | 15 | Scope note: what the formalization covers, the comparator, the status |
| S22 | `lean/ComparatorChallenges/EinsteinFour.lean` | 222 | Comparator stub: the classification targets, with three `sorry` |
| S23 | `notes/tables/catalog.tsv` | 373 | Reading ledger row for family 348 |

## Links

- [S1](../../../CONTENTS.md)
- [S2](../../../overview.tex)
- [S3](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/README.md)
- [S4](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/einstein-boundary.pdf)
- [S5](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/paper.tex)
- [S6](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/sections/01-introduction.tex)
- [S7](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/build/references.tex)
- [S8](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/README.md)
- [S9](../../../preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/COVERAGE.md)
- [S10](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/README.md)
- [S11](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/einstein-gap.pdf)
- [S12](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/main.tex)
- [S13](../../../preprints/An-L2-Einstein-Gap-for-Nonnegatively-Curved-Four-Manifolds-October-5-2026/build/source/references.bib)
- [S14](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/README.md)
- [S15](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/paper.pdf)
- [S16](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/paper.tex)
- [S17](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/sections/01-introduction.tex)
- [S18](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/references.tex)
- [S19](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/README.md)
- [S20](../../../preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/COVERAGE.md)
- [S21](../../../lean/docs/348.md)
- [S22](../../../lean/ComparatorChallenges/EinsteinFour.lean)
- [S23](../../../notes/tables/catalog.tsv)
