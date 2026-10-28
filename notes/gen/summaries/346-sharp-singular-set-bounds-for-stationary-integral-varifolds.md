[Notes](../../README.md) / [Summaries](README.md) / [Differential geometry](../index/disciplines/differential-geometry.md) / [Family 346](../index/differential-geometry/346-sharp-singular-set-bounds-for-stationary-integral-varifolds.md)

# 346 — Sharp singular-set bounds for stationary integral varifolds

[Index page](../index/differential-geometry/346-sharp-singular-set-bounds-for-stationary-integral-varifolds.md)

## Original CONTENTS.md summary

The release's blurb for family 346 

> **346. Sharp singular-set bounds for stationary integral varifolds.** Proves that every stationary integral m-varifold in a Euclidean open set has singular set of Hausdorff dimension at most $m-1$, a sharp bound in every positive dimension and codimension. On round spheres, the family also proves almost-everywhere regularity: the singular set has zero m-dimensional Hausdorff measure. [S1:8372]

The first manuscript's abstract 

> Brena, Decio, and De Lellis \cite[Conjectures 1.1 and 1.2]BDD2025 separate the dimension bound from the weaker assertion $\mathcal H^m(\mathrm{Sing} V)=0$. The latter Euclidean assertion is proved in _Almost-everywhere regularity of stationary integral varifolds_ , which we henceforth call AE. Our proof uses AE's signed-excess theorem and local estimates from its fitting and frequency arguments. [S6:104–109]

The second manuscript's abstract 

> We resolve the almost-everywhere regularity conjecture of Brena, Decio, and De Lellis for stationary integral varifolds of arbitrary positive dimension and codimension in Euclidean open sets. The singular set has zero measure in the dimension of the varifold: near almost every support point, the varifold is a constant positive integer multiple of a smooth embedded minimal submanifold. The corresponding statement also holds on round spheres. [S1:8390]

The catalog abstract in `overview.tex` [S2:790] is the blurb. The bibtex keys the release ships [S3:10–13]:

> @misc{OAI:A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026,
>   author = {{OpenAI}},
>   title = {{A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold}},
>   howpublished = {OpenAI Math Release preprint

and [S8:10–13]:

> @misc{OAI:Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026,
>   author = {{OpenAI}},
>   title = {{Almost-everywhere regularity of stationary integral varifolds}},
>   howpublished = {OpenAI Math Release preprint

## Undergraduate summary

A stationary integral varifold is a measure-theoretic minimal surface with integer multiplicity: a countably $m$-rectifiable set carrying a positive integer weight whose first variation of area vanishes under every compactly supported ambient deformation. Its tangent plane exists almost everywhere, but a tangent plane alone need not describe an entire neighborhood 

> A stationary integral varifold is a measure-theoretic minimal surface with integer multiplicity. Its tangent plane exists almost everywhere, but a tangent plane alone need not describe an entire neighborhood. The basic regularity question is whether the points without a smooth minimal neighborhood can carry positive measure. We prove that they have zero $m$-dimensional measure. [S11:3–7]

A point is regular when a neighborhood of it contains a smooth embedded minimal submanifold whose support equals the varifold's support there and whose weight is a constant integer multiple; the remaining support points are the singular set 

> A point $p\in\mathrm{spt}\mu\cap U$ is _regular_ if some neighborhood $W$ of $p$ contains a smooth embedded minimal $m$-submanifold $\Sigma$, without boundary in $W$, such that $\mathrm{spt}\mu\cap W=\Sigma$ and $V\llcorner W=q|\Sigma|$ for a positive integer $q$. We denote the remaining support points by $\mathrm{Sing} V$. Thus regularity includes equality of the local support with one embedded submanifold, not merely a smooth parametrization on a set of full measure. [S6:21–28]

The second manuscript proves the measure-zero statement [S11:26–33]:

> \begin{theorem}\label{thm:main}
> Every stationary integral $m$-varifold in an open subset of $\mathbb R^{m+n}$ satisfies
> $$>  \mathcal H^m(\mathrm{Sing}V)=0.
>$$
> Here $m,n\geq1$ are arbitrary. No stability, minimizing, orientability,
> density upper bound, or codimension-one hypothesis is required.
> \end{theorem}

The first manuscript proves the sharp dimension bound, and its regularity definition is stronger: regularity requires equality of the local support with one embedded submanifold, not merely a smooth parametrization on a set of full measure 

> A point $p\in\mathrm{spt}\mu\cap U$ is _regular_ if there are a neighborhood $W$ of $p$, a smooth embedded minimal $m$-submanifold $\Sigma\subset W$, and an integer $q\geq1$ such that the restriction of the varifold to $W$ is $q|\Sigma|$. The remaining support points form $\mathrm{Sing}V$. [S11:21–24]

The main theorem is the dimension bound [S6:32–38]:

> \begin{theorem}\label{thm:main}
> For every stationary integral $m$-varifold $V$ in an open set
> $U\subset\mathbb R^{m+n}$, where $m,n\ge1$,
> $$>  \dim_{\mathcal H}\mathrm{Sing} V\le m-1.
>$$
> \end{theorem}

The bound is sharp, and the manuscript names the example that attains it 

> Theorem proves the Euclidean conjecture recorded as Conjecture 1.1 by Brena, Decio, and De Lellis . There is no stability, minimizing, orientability, density-upper-bound, or codimension hypothesis. The estimate is sharp: the sum of the varifolds of two distinct $m$-planes meeting along an $(m-1)$-plane is stationary, and its singular set is exactly that intersection. [S6:40–45]

The second manuscript also settles the spherical case, where the classical theory needs a mass bound [S11:35–47]:

> \begin{corollary}[Round spheres]\label{cor:round-spheres}
> Let $m,n\geq1$ and let $V$ be an integral $m$-varifold on the full unit round
> sphere $S^{m+n}$, stationary for variations tangent to the sphere. A support
> point is regular if on a spherical neighborhood $V=q|\Sigma|$ for an integer
> $q\geq1$ and a smooth embedded minimal $m$-submanifold $\Sigma$ of the sphere.
> If $\mathrm{Sing}_S V$ denotes the remaining support points, then
> $$>  \mathcal H^m_{g_{\mathrm{round}}}(\mathrm{Sing}_S V)=0.
>$$
> No fixed upper bound on mass, density, or multiplicity is required, nor are
> stability, orientability, or mod-two cyclicity. The same conclusion holds on
> every round sphere of positive radius.
> \end{corollary}

## Graduate summary

The two manuscripts name the same conjecture. Brena, Decio, and De Lellis separate the dimension bound from the weaker assertion that the singular set has zero $m$-dimensional measure; the first manuscript proves the dimension bound and cites the second for the measure-zero statement, and the second manuscript proves the measure-zero statement as Conjecture 1.2 

> Simon's 2018 notes already record the question whether the singular set must be $\mathcal H^m$-null even when the generalized mean curvature is zero \cite[Chapter 5, Remark 6.4]Simon2018. The measure-zero singular-set assertion is Conjecture 1.2 of Brena, Decio, and De Lellis . proves this conjecture in its full Euclidean scope. They isolate a local criterion in Conjecture 1.3: [S11:65–70]

The first manuscript separates the two assertions and cites the second manuscript for the measure-zero one [S6:104–109]:

> Brena, Decio, and De Lellis \cite[Conjectures~1.1 and~1.2]{BDD2025}
> separate the dimension bound from the weaker assertion
> $\mathcal H^m(\mathrm{Sing} V)=0$. The latter Euclidean assertion is proved in
> \emph{Almost-everywhere regularity of stationary integral varifolds}
> \cite{AE}, which we henceforth call AE. Our proof uses AE's signed-excess
> theorem and local estimates from its fitting and frequency arguments.

The first manuscript states that the almost-everywhere conclusion is not an input to its proof 

> The elliptic correction of the averaged graph in \cite[Sections 6.3–6.4]BDLF2025 is an antecedent of this fitting construction. The almost-everywhere regularity conclusion itself is not an input: a set can have zero $\mathcal H^m$ measure and still have Hausdorff dimension greater than $m-1$. [S6:110–114]

The prior literature is the Allard–Federer–Simon tradition. Allard's compactness and regularity theory gives a relatively open dense regular set; the dimension-reduction method leads to the classical stratification by translation symmetries of tangent cones, and for stationary integral varifolds the set of points admitting no planar tangent has dimension at most $m-1$. Naber and Valtorta proved rectifiability of these strata for integral varifolds with bounded mean curvature, so the remaining difficulty is the singular set at higher-multiplicity planar tangents, where Allard's multiplicity-one theorem does not apply [S6:47–58]. For area-minimizing integral currents, Almgren gives the $m-2$ bound in arbitrary codimension, and De Lellis–Spadaro's multiple-valued, center-manifold, frequency analysis explains subtracting a well-chosen smooth center before normalizing the height — but their theorems do not apply to arbitrary stationary integral varifolds, and the crossing example prevents the same bound in this setting [S6:59–68]. The manuscript names Hirsch–Spolaor's $m-1$ bound for two-valued stationary Lipschitz graphs and their almost-everywhere regularity for stationary codimension-one integral currents with density at most two, Krummel–Minter–Wickramasekera's bounds at controlled densities under an explicit epsilon-regularity assumption, Brakke's $C^{1,\alpha}$ rectifiability, Menne's second-order rectifiability, Brena–De Lellis–Franceschini's smooth rectifiability and Kolasiński's independent proof, and De Lellis–Hirsch–Lihn–Spolaor's stationary varifolds with planar tangents and infinite local topology in non-Euclidean metrics [S6:72–102].

The first manuscript's proof runs by contradiction on the dimension bound [S6:120–135]:

> Suppose that $\dim_{\mathcal H}\mathrm{Sing} V>m-1$ and choose an exponent $s$ strictly between these two numbers. A first dimension-reduction argument produces a singular point, placed at the origin, an integer $Q$, and radii $L_i\downarrow0$ for which the rescaled varifolds converge to the multiplicity-$Q$ plane. At these same scales there are nonzero measures $\sigma_i$ carried by density-$Q$ points in a fixed compact ball, with mass bounded above and away from zero and the estimate $$\sigma_i(\mathbf B_r(x))\le Cr^s.$$ Here $\mathbf B_r(x)$ is an ambient Euclidean ball. The limiting measure of centers cannot be carried by an $(m-1)$-plane. This first reduction, proved in Section , is the familiar geometric starting point of dimension reduction; the challenge is to retain these centers in a further, height-normalized limit. [S6:121–135]

The four further stages are the new parts 

> The proof has four further stages. First, we construct smooth reference graphs at the prescribed scales $L_i$. AE's minimal fitting gives intervals of radii on which a centered height admits frequency control. Section proves that these intervals cover every sufficiently small prescribed flat scale, including their transition regions. Section then normalizes the height by numbers $a_i\downarrow0$. The normalized second moment is nonzero, the first moment tends to zero, and the reference graphs' mean curvature and its first derivative are $o(a_i)$. Both moment conclusions are needed: subtracting a reference graph must neither remove the entire limit nor leave an arbitrary translation in it. [S6:137–148]

Second, the linearized-measures section passes the first variations and signed excess to measures on the limiting plane 

> Second, Section passes the first variations and signed excess to measures on the limiting plane. The resulting data consist of a nonnegative height measure, a positive-semidefinite tilt measure, a mixed height–tilt measure, and a signed mass measure. They satisfy linear first-variation identities, a positive-semidefinite block inequality, and a one-sided comparison of mass and tilt. This formulation avoids assuming that the limiting sheets can be globally labeled or represented by a single-valued function. [S6:150–157]

Third, the density-centers section supplies the curvature-corrected comparison 

> Third, the density of the points carrying $\sigma_i$ must still be visible after division by $a_i^2$. Ordinary uncorrected radial comparison does not provide that precision on curved reference graphs. Section uses geodesic radial fields weighted by the inverse reference-volume density. The resulting curvature error can be averaged against $\sigma_i$ at every radius down to zero. For a fixed $l>0$, its decisive integral is $$\int_0^l t^{s-m}\,\mathrm d t<\infty,$$ which holds exactly when $s>m-1$. The centered first-moment estimate then removes the translation terms and yields a density comparison at every limiting center. [S6:159–171]

Finally, the dimension-reduction section closes the contradiction 

> Finally, Section isolates an abstract dimension-reduction statement for these measures. Its frequency is monotone at the retained centers. A second blow-up makes that frequency constant at enough independent centers. Equality in the positive-semidefinite inequality then forces the height measure to vanish, contrary to its normalization. This is the contradiction that proves Theorem . [S6:173–179]

The manuscript names which parts are new 

> The prescribed-scale construction, the averaged curved radial comparison, and the final measure-valued reduction are the parts needed to strengthen AE's almost-everywhere conclusion to a dimension bound. [S6:181–183]

The second manuscript's engine is a signed-excess estimate. With $\pi$ projection onto the first factor, $Q$ a positive integer, and $P_{vv}$ the vertical block of the tangent projection, it defines the signed mass measure $M$ and the tilt measure $D$ and keeps the sign in the comparison 

> Here $|M|$ denotes the total variation of the signed measure $M$, and $\tau=|M|+D$ is the positive excess measure in this flat setting. When $\tau$ has mass at most $d$ on a fixed enlarged ball, we prove an interior bound of the form $$\label{eq:intro-signed} \int w(2M-D) \leq d\exp\!\left[-F_Q\!\left(\log\frac1d\right)\right]$$ for nonnegative Lipschitz weights with fixed bounds. The explicit function $F_Q$ grows faster than every fixed power of $\log T$ as $T\to\infty$. gives the precise statement, including the curvature error for a reference surface of sufficiently high finite regularity. Retaining the sign permits a substantially smaller error than an absolute-value estimate. [S11:124–136]

The manuscript's own organization paragraph names the section files and what each proves [S11:213–224]:

> \paragraph{Organization.}
> \Cref{sec:local} establishes the first-variation, integer-count, and height
> estimates. \Cref{sec:signed-statement} states the signed-excess theorem and
> fixes its parameter hierarchy. \Cref{sec:contact} constructs the heat
> contacts and reduces separated configurations to lower multiplicities;
> \Cref{sec:excess} develops the outward comparison and controls mergers;
> \Cref{sec:packing} closes the integer induction by packing witness scales.
> \Cref{sec:centering} constructs the center from minimal fits and
> multiplicity defects. \Cref{sec:inward} derives inward doubling,
> forces the height to vanish, and proves the Hausdorff-measure conclusion
> on the entire support. \Cref{sec:spheres} proves the round-sphere
> consequence by the separate cone argument.

The section files on disk are `introduction.tex`, `local.tex`, `signed-statement.tex`, `contact.tex`, `excess.tex`, `packing.tex`, `centering.tex`, `inward.tex`, and `spheres.tex`. The spherical corollary is derived from the theorem by that cone argument, which adapts the hypersurface first-variation calculation in a cited lemma and rederives it in the present dimensions [S11:49–52]. The first manuscript's section files carry its four stages: `02-flat-scales.tex` the first reduction, `03-normal-inputs.tex` the imported measure estimates, `04-fitting-frequency.tex` the minimal fitting and frequency control, `05-centered-blowup.tex` the height-normalized blowup, `06-linearized-measures.tex` the linearized first variations and signed excess, `06b-density-centers.tex` the curvature-corrected geodesic radial comparison, and `07-dimension-reduction.tex` the measure-valued reduction.

**Prior (my training data, not this repo).** The almost-everywhere regularity conjecture for stationary integral varifolds — that the singular set has zero $m$-dimensional Hausdorff measure — was, as of my cutoff, open in general codimension. Allard's theory gives regularity at density-one points, and the codimension-one dimension bound was known for stable varifolds (Schoen–Simon) and under density bounds. The unconditional measure-zero statement for arbitrary dimension and codimension is what I recall as open. The prior is a training-data recollection at an early-2025 cutoff, self-rated, and the repo supplies only the manuscripts' citations.

## Consequences

The direct consequence is the conjecture's resolution in its full Euclidean scope: the singular set of a stationary integral varifold has zero $m$-dimensional measure, with no stability, minimizing, orientability, density-bound, or codimension-one hypothesis [S11:26–33] [S1:8390]. The dimension bound is sharp, and the manuscript names the two-plane crossing that attains it [S6:40–45].

The spherical corollary removes the mass, density, and multiplicity bounds the classical theory requires [S11:35–47]. The consequence for the field is that the regular set is measure-theoretically full, so the remaining questions are about the structure of a set of measure zero, not about its size.

Inside the release, this family is at tier T0 with no formalization. The ledger records `paps_form` 0, `chal` 0, `mainres` 0, `scope_note` 0, `verification` 0, `inputs` 0, `covmd` 0, no trace, and no companion edge [S13:342]. The claim-shape column is `bound|partial` and the conditional, resolves-named, and broad counterexample flags are 0. Nothing in `lean/` states either theorem, so no Lean or comparator run can confirm any part of them.

What has not been checked: no Lean, lake, or comparator run was performed, and for this family there is nothing in the release to run; the two manuscripts carry 2,244 and 6,244 lines in their section files, and I read only the two introductions line by line, so every section-file claim in the machinery paragraph is a section heading I read from the introductions, not a statement I read in the section file; the prior paragraph is a training-data recollection, not a literature check; the page covers one family, and 14 differential-geometry families in bead `math-ckd.4`'s group have no page.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb, manuscript links, both manuscript abstracts |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | Family 346's `\resultentry`, at line 790 |
| S3 | [`preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/README.md`](../../../preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/README.md) | 18 | First manuscript README, date, bibtex key |
| S4 | [`preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf`](../../../preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf) | 15834 | First manuscript PDF |
| S5 | [`preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/build/main.tex`](../../../preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/build/main.tex) | 28 | Preamble, theorem environments, section include list |
| S6 | [`preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/build/sections/01-introduction.tex) | 200 | Main theorem, regularity definition, sharpness, antecedents, proof stages |
| S7 | [`preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/build/references.bib`](../../../preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/build/references.bib) | 251 | First manuscript bibliography |
| S8 | [`preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/README.md`](../../../preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/README.md) | 18 | Second manuscript README, date, bibtex key |
| S9 | [`preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf`](../../../preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf) | 22614 | Second manuscript PDF |
| S10 | [`preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/paper.tex`](../../../preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/paper.tex) | 71 | Preamble, theorem environments, section include list |
| S11 | [`preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/sections/introduction.tex`](../../../preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/sections/introduction.tex) | 237 | Main theorem, regularity definition, spherical corollary, the named conjecture |
| S12 | [`preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/references.bib`](../../../preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/build/references.bib) | 222 | Second manuscript bibliography |
| S13 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | Reading ledger row for family 346 |

## Bibliography

- Allard, William K., On the first variation of a varifold (1972)
- Allard, William K., Notes on the theory of varifolds (1987)
- Allard, William K., On the first variation of a varifold (1972)
- Allard, William K., Notes on the theory of varifolds (1987)
- Almgren, Jr., Frederick J., Almgren's Big Regularity Paper: $Q$-Valued Functions Minimizing Dirichlet's Integral and the Regularity of Area-Minimizing Rectifiable Currents up to Codimension $2$ (2000)
- Almgren, Jr., Frederick J., Almgren's Big Regularity Paper (2000)
- Brakke, Kenneth A., The Motion of a Surface by Its Mean Curvature (1978)
- Brena, Camillo, Decio, Stefano, De Lellis, Camillo, Remarks and conjectures on stationary varifolds dedicated to Enrico Bombieri (2025)
- Brena, Camillo, De Lellis, Camillo, Franceschini, Federico, $C^\infty$ rectifiability of stationary varifolds (2025)
- Brena, Camillo, De Lellis, Camillo, Franceschini, Federico, $C^\infty$ rectifiability of stationary varifolds (2025)
- Brena, Camillo, Decio, Stefano, De Lellis, Camillo, Remarks and conjectures on stationary varifolds dedicated to Enrico Bombieri (2025)
- Caffarelli, Luis, Silvestre, Luis, An extension problem related to the fractional Laplacian (2007)
- Federer, Herbert, Geometric Measure Theory (1969)
- Federer, Herbert, The singular sets of area minimizing rectifiable currents with codimension one and of area minimizing flat chains modulo two with arbitrary codimension (1970)
- Hirsch, Jonas, Spolaor, Luca, Dimension of the singular set for $2$-valued stationary Lipschitz graphs (2023)
- Hirsch, Jonas, Spolaor, Luca, Measure $0$ of the singular set for $2$-valued stationary hypercurrents (2025)
- Hirsch, Jonas, Spolaor, Luca, Measure $0$ of the singular set for $2$-valued stationary hypercurrents (2025)
- Krummel, Brian, Minter, Paul, Wickramasekera, Neshan, A Branch Set Stratification for Stationary Varifolds with Epsilon-Regularity (2026)
- De Lellis, Camillo, Spadaro, Emanuele Nunzio, $Q$-valued functions revisited (2011)
- De Lellis, Camillo, Spadaro, Emanuele, Regularity of area minimizing currents II: center manifold (2016)
- De Lellis, Camillo, Spadaro, Emanuele, Regularity of area minimizing currents III: blow-up (2016)
- De Lellis, Camillo, Hirsch, Jonas, Lihn, Zachary, Spolaor, Luca, Stationary varifolds with singularities II (2026)
- De Lellis, Camillo, Hirsch, Jonas, Spolaor, Luca, Stationary and stable varifolds with singularities (2026)
- De Lellis, Camillo, Spadaro, Emanuele Nunzio, $Q$-valued functions revisited (2011)
- De Lellis, Camillo, Spadaro, Emanuele, Regularity of area minimizing currents II: center manifold (2016)
- De Lellis, Camillo, Spadaro, Emanuele, Regularity of area minimizing currents III: blow-up (2016)
- De Lellis, Camillo, Hirsch, Jonas, Lihn, Zachary, Spolaor, Luca, Stationary varifolds with singularities II (2026)
- Mattila, Pertti, Geometry of Sets and Measures in Euclidean Spaces: Fractals and Rectifiability (1995)
- Menne, Ulrich, Second order rectifiability of integral varifolds of locally bounded first variation (2013)
- Menne, Ulrich, Second order rectifiability of integral varifolds of locally bounded first variation (2013)
- Milnor, John, Analytic Proofs of the ``Hairy Ball Theorem'' and the Brouwer Fixed Point Theorem (1978)
- Calderón, A. P., Zygmund, A., On the existence of certain singular integrals (1952)
- Naber, Aaron, Valtorta, Daniele, The singular structure and regularity of stationary varifolds (2020)
- Hytönen, Tuomas, Kairema, Anna, Systems of dyadic cubes in a doubling metric space (2012)
- OpenAI, Almost-everywhere regularity of stationary integral varifolds (2026)
- OpenAI, The Solomon–Yau least-volume theorem (2026)
- Simon, Leon, Introduction to Geometric Measure Theory (2018)
- Simon, Leon, Lectures on Geometric Measure Theory (1983)
- Simon, Leon, Lectures on Geometric Measure Theory (1983)
- Simon, Leon, Introduction to Geometric Measure Theory (2018)
- Kolasiński, Sławomir, Rectifiability of every finite order for stationary integral varifolds (2026)
- Kolasiński, Sławomir, Rectifiability of every finite order for stationary integral varifolds (2026)
- Whitney, Hassler, Analytic extensions of differentiable functions defined in closed sets (1934)
