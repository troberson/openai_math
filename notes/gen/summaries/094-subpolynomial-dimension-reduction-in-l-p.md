[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 094](../index/convex-and-metric-geometry/094-subpolynomial-dimension-reduction-in-l-p.md)

# 094 — Subpolynomial dimension reduction in $L_p$

[Index page](../index/convex-and-metric-geometry/094-subpolynomial-dimension-reduction-in-l-p.md)

## Original CONTENTS.md summary

The release's blurb [S1:2320] and the catalog abstract [S2:264] state
the family's claim: for every fixed $`1<p<\infty`$ and distortion
$`D>1`$, every $`n`$-point subset of real $`L_p`$ embeds into
$`\ell_p^d`$ with distortion at most $`D`$ and subpolynomial dimension
$`d=n^{o(1)}`$. The manuscript's abstract 

> For every fixed $`1<p<\infty`$ and $`D>1`$, every $`n`$-point subset of a
real $`L_p`$ space embeds into $`\ell_p^d`$ with distortion at most $`D`$
and subpolynomial dimension $`d=n^{o(1)}`$. The target has the same
exponent $`p`$, and the embedding need not be linear. [S3:40–43]

## Undergraduate summary

Dimension reduction asks how many coordinates an $`n`$-point metric
space needs in order to preserve all pairwise distances up to a
fixed distortion. The Johnson–Lindenstrauss lemma answers this
for Hilbert space: $`O_D(\log n)`$ Euclidean dimensions suffice.
The open question, posed by Johnson and Lindenstrauss themselves, is
what the answer is in the other $`L_p`$ spaces.

This manuscript studies the coordinate-target version: the $`n`$ points
may be repositioned freely, but their images must land in
$`\ell_p^d`$ with the *same* exponent $`p`$ [S3:53–57]. The
quantity $`d_p(n,D)`$ is the least $`d`$ for which every $`n`$-point subset
of any real $`L_p`$ space admits such a $`D`$-distortion embedding
[S3:62–69]. The maps need not be linear. The result is that
for $`p\ne2`$ this dimension grows faster than any power of
$`\log n`$ but slower than any positive power of $`n`$
[S3:84–101].

## Graduate summary

**The main theorem** [S3:75–101, `thm:main`]. Fix
$`1<p<\infty`$, $`p\ne2`$, and put
$`\gamma(p)=2-p`$ for $`p<2`$ and $`1-2/p`$ for $`p>2`$. For every $`D>1`$
there is a constant $`C_{p,D}<\infty`$ such that, for every integer
$`n\ge2`$,

> **theorem**
Fix $`1<p<\infty`$, $`p\ne2`$, and put
$$\gamma(p)=
 \begin{cases}
  2-p,&1<p<2,\\
  1-2/p,&2<p<\infty.
 \end{cases}$$
For every $`D>1`$ there is a constant $`C_{p,D}<\infty`$ such that, for
every integer $`n\ge2`$,
$$\frac{\log n}{\log(1+2D)}
 \le d_p(n,D)
 \le \exp\!\bigl(C_{p,D}(\log n)^{\gamma(p)}\bigr).$$
For exact embeddings,
$$\left\lfloor\frac{n-1}{4}\right\rfloor^2
 \le d_p(n,1)\le\binom n2\qquad(n\ge9).$$
Consequently,
$$\lim_{n\to\infty}\frac{\log d_p(n,D)}{\log n}
 =\begin{cases}0,&D>1,\\2,&D=1.\end{cases}$$ [S3:75–101]

The constants depend on the fixed parameters $`p,D`$; no uniformity as
$`p`$ approaches an endpoint or $`D`$ approaches $`1`$ is asserted. The
theorem is existential and does not assert an efficient embedding
algorithm [S3:103–108].

**The exact-distortion contrast.** At distortion $`1`$ the
corresponding dimension is quadratically large in $`n`$
[S3:91–95], so the subpolynomial bound at $`D>1`$ is genuinely
new. Ball proved the exact-coordinate upper bound $`\binom n2`$ and
its quadratic-order sharpness for $`1\le p<2`$; the lower bound uses
an antipodal row-and-column configuration whose disjoint-support
test is the classical equality criterion for the
$`p`$-parallelogram defect, so the argument includes even integers
$`p>2`$ [S3:112–119].

## History of the conjecture

The Johnson–Lindenstrauss lemma gives the Hilbert-space
$`O_D(\log n)`$ bound and poses the other-$`L_p`$ question
[S3:48–52]. Approximate finite-set bounds and linear-subspace
discretization have different dimension parameters: Schechtman's
finite-set estimates below $`2`$ progress from $`O_D(n\log n)`$ to
$`O_{p,D}(n)`$ coordinates, while the Bourgain–Lindenstrauss
–Milman and Talagrand subspace results preserve a fixed
$`r`$-dimensional subspace by a linear map; neither gives the present
subpolynomial bound in cardinality [S3:121–130]. The absence of
a linearity requirement is essential to the coordinate version
[S3:135].

**Prior (my training data, not this repo).** I know the
Johnson–Lindenstrauss lemma, Ball's exact-coordinate
quadratic bound for $`L_p`$ with $`p<2`$, and the Schechtman /
Bourgain–Lindenstrauss–Milman dimension-reduction
landscape for $`L_p`$. A proof that every $`n`$-point subset of real
$`L_p`$ embeds into $`\ell_p^d`$ at a fixed distortion $`D>1`$ with
dimension $`n^{o(1)}`$ for every $`p\ne2`$, together with the matching
quadratic lower bound at distortion $`1`$, is, to my knowledge, not
established in the literature I was trained on. I cannot
independently verify this manuscript's argument.

## Consequences

**Subpolynomial dimension.** For $`p\ne2`$ and $`D>1`$,
$`d_p(n,D)\le\exp(C_{p,D}(\log n)^{\gamma(p)})`$ and
$`\log d_p(n,D)/\log n\to0`$ [S3:84–100].

**Quadratic cost at exact distortion.** At $`D=1`$ the dimension is
$`\Theta(n^2)`$: between $`\lfloor(n-1)/4\rfloor^2`$ and
$`\binom n2`$ for $`n\ge9`$ [S3:91–95, S3:96–100].

**The same exponent is preserved.** The target is
$`\ell_p^d`$, not a different $`\ell_q`$ [S3:42–43].

## Section skeleton

One manuscript [S3] (title [S3:33], date [S3:35]) — a single
1,468-line `paper.tex` under `build/` with seven sections
(introduction, the $`p<2`$ and $`p>2`$ upper bounds, the exact bound, the
lower bound, the logarithmic limit, and remarks); one figure
(`figures/truncation-ramp.tex`). No `.bib` file ships; the reference
list is a `thebibliography` block in the root. The manuscript ships
no `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S4:9]. The formalization bounds the least dimension
needed to embed every $`n`$-point subset of real $`L_p`$ with
distortion $`D`$: for each fixed $`D>1`$ the dimension lies between
$`\log n/\log(1+2D)`$ and
$`\exp(C(\log n)^{\gamma(p)})`$, at distortion $`1`$ between
$`\lfloor(n-1)/4\rfloor^2`$ and $`\binom n2`$, and its logarithm
divided by $`\log n`$ tends to $`0`$ for $`D>1`$ and to $`2`$ for $`D=1`$.
The scope note names one comparator [S4:13–15]. The release
records `scope: "Partial progress."` and `review: status: unchecked`;
zero `sorry` in the Lean source is not a comparator pass, and the
library has not been built here.

**The comparator stub** carries one `sorry`:

```lean
theorem source_main (p : ℝ) (hp : 1 < p) (hp2 : p ≠ 2) :
    (∀ D : ℝ, 1 < D → ∃ C : ℝ, ∀ n : ℕ, 2 ≤ n →
      GoodDimension.{u} p n D (dimension.{u} p n D) ∧
      Real.log (n : ℝ) / Real.log (1 + 2 * D) ≤ (dimension.{u} p n D : ℝ) ∧
      (dimension.{u} p n D : ℝ) ≤ Real.exp (C * Real.log (n : ℝ) ^ gamma p)) ∧
    (∀ n : ℕ, 9 ≤ n →
      GoodDimension.{u} p n 1 (dimension.{u} p n 1) ∧
      ((n - 1) / 4) ^ 2 ≤ dimension.{u} p n 1 ∧
      dimension.{u} p n 1 ≤ n.choose 2) ∧
    (∀ D : ℝ, 1 ≤ D →
      Tendsto (fun n : ℕ => Real.log (dimension.{u} p n D : ℝ) / Real.log (n : ℝ))
        atTop (𝓝 (if 1 < D then 0 else 2))) := by
  sorry
```
[S5:32–44]

**The registered entry point.** The `main_results` entry names
`OAI.SubpolynomialLp.source_main` in
`OAI/Analysis/LpDimension/Main.lean`, proved at line 13


```lean
theorem source_main (p : ℝ) (hp : 1 < p) (hp2 : p ≠ 2) :
    (∀ D : ℝ, 1 < D → ∃ C : ℝ, ∀ n : ℕ, 2 ≤ n →
      GoodDimension.{u} p n D (dimension.{u} p n D) ∧
      Real.log (n : ℝ) / Real.log (1 + 2 * D) ≤ (dimension.{u} p n D : ℝ) ∧
      (dimension.{u} p n D : ℝ) ≤ Real.exp (C * Real.log (n : ℝ) ^ gamma p)) ∧
    (∀ n : ℕ, 9 ≤ n →
      GoodDimension.{u} p n 1 (dimension.{u} p n 1) ∧
      ((n - 1) / 4) ^ 2 ≤ dimension.{u} p n 1 ∧
      dimension.{u} p n 1 ≤ n.choose 2) ∧
    (∀ D : ℝ, 1 ≤ D →
      Tendsto (fun n : ℕ => Real.log (dimension.{u} p n D : ℝ) / Real.log (n : ℝ))
        atTop (𝓝 (if 1 < D then 0 else 2))) := by
  have hupper : ∀ D : ℝ, 1 < D → ∃ C : ℝ, ∀ n : ℕ, 2 ≤ n →
      (dimension.{u} p n D : ℝ) ≤ Real.exp (C * Real.log (n : ℝ) ^ gamma p) := by
```
[S6:13–26]

The proof discharges the upper bound by cases on $`p<2`$ / $`p>2`$
(`below_main_upper` / `above_main_upper`), the exact bound by
`exact_dimension_bounds`, and the logarithmic limits by
`subpower_log_limit`. The `main_results` entry links the config
`ComparatorChallenges/SubpolynomialLp.json` to the declaration, so
this is the family's headline theorem, registered and proven. The
OAI `LpDimension` tree is 45 files over 7,918 lines with zero
`sorry`.

## Coverage

T3: the family is formalized. The ledger row `fam=094` records
`paps 1`, `paps_form 1`, `tier T3`, `chal 1`, `mainres 1`,
`scope_note 1`, `verification 0`, `trace` empty,
`shapes partial|uniform`, `resolves_named 1`, `summary 1`. The family
ships one 1,468-line LaTeX manuscript, a scope note, one comparator
challenge carrying one `sorry` theorem, and the registered
`main_results` declaration
`OAI.SubpolynomialLp.source_main`, which is the family's headline
theorem and is proven in the 45-file `LpDimension` OAI tree. The
family ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 094 at [S1:2320] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{094} at [S2:264] |
| S3 | [`preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/build/paper.tex`](../../../preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/build/paper.tex) | 1467 | the single manuscript; title [S3:33], date [S3:35], abstract [S3:40–43], the $d_p(n,D)$ definition [S3:62–69], the main theorem [S3:75–101], the constants remark [S3:103–108], and the exact-distortion contrast [S3:112–119] |
| S4 | [`lean/docs/094.md`](../../../lean/docs/094.md) | 15 | the formalization scope note: the scope paragraph [S4:9] and the comparator table [S4:13–15] |
| S5 | [`lean/ComparatorChallenges/SubpolynomialLp.lean`](../../../lean/ComparatorChallenges/SubpolynomialLp.lean) | 50 | comparator stub: the `source_main` theorem [S5:32–43] and the `sorry` [S5:44] |
| S6 | [`lean/OAI/Analysis/LpDimension/Main.lean`](../../../lean/OAI/Analysis/LpDimension/Main.lean) | 63 | the OAI proven `source_main` theorem [S6:13–26] |

## Bibliography

- Gideon Schechtman. _Dimension reduction in $`L_p`$, $`0<p<2`$_. arXiv:1110.2148v1, 2011. arxiv.org/abs/1110.2148v1.
- Assaf Naor. Metric dimension reduction: a snapshot of the Ribe program. In _Proceedings of the International Congress of Mathematicians—Rio de Janeiro 2018_, volume I, pages 759–837. World Scientific, 2018. arXiv:1809.02376v1.
- Bo Brinkman and Moses Charikar. On the impossibility of dimension reduction in $`\ell_1`$. _Journal of the ACM_, 52(5):766–788, 2005. doi:10.1145/1089023.1089026.
- James R. Lee and Assaf Naor. Embedding the diamond graph in $`L_p`$ and dimension reduction in $`L_1`$. _Geometric and Functional Analysis_, 14(4):745–747, 2004. doi:10.1007/s00039-004-0473-8.
- Michel Talagrand. Embedding subspaces of $`L_p`$ in $`\ell_p^N`$. In _Geometric Aspects of Functional Analysis_, Operator Theory: Advances and Applications, volume 77, pages 311–326. Birkhäuser, Basel, 1995. doi:10.1007/978-3-0348-9090-8\_26.
- Assaf Naor and Kevin Ren. _A threshold phenomenon for embeddings of Euclidean snowflakes and impossibility of dimension reduction_. arXiv:2609.01079v1, 2026. arxiv.org/abs/2609.01079v1.
- Wassily Hoeffding. Probability inequalities for sums of bounded random variables. _Journal of the American Statistical Association_, 58(301):13–30, 1963. doi:10.1080/01621459.1963.10500830.
- Jean Bourgain, Joram Lindenstrauss, and Vitali Milman. Approximation of zonoids by zonotopes. _Acta Mathematica_, 162:73–141, 1989. doi:10.1007/BF02392835.
- Keith Ball. Isometric embedding in $`l_p`$-spaces. _European Journal of Combinatorics_, 11(4):305–311, 1990. doi:10.1016/S0195-6698(13)80131-X.
- Piotr Indyk. Stable distributions, pseudorandom generators, embeddings, and data stream computation. _Journal of the ACM_, 53(3):307–323, 2006.
- Gilles Pisier. Remarques sur un résultat non publié de B. Maurey. _Séminaire d'analyse fonctionnelle_, 1980–1981, Exposé no. 5, pages 1–12. École Polytechnique, Palaiseau, 1981. .
- Alexandros Eskenazis. $`\varepsilon`$-isometric dimension reduction for incompressible subsets of $`\ell_p`$. _Discrete & Computational Geometry_, 71:160–176, 2024. doi:10.1007/s00454-023-00587-w.
- Ori Gurel-Gurevich, Asaf Nachmias, and Sushant Sachdeva. _A Tight Bound on Localization of Electrical Flows_. arXiv:2605.24130v1, 2026. arxiv.org/abs/2605.24130v1.
- James R. Lee, Manor Mendel, and Assaf Naor. Metric structures in $`L_1`$: dimension, snowflakes, and average distortion. _European Journal of Combinatorics_, 26(8):1180–1190, 2005. doi:10.1016/j.ejc.2004.07.002.
- Rick Durrett. _Probability: Theory and Examples_. Author-posted manuscript, Version 5, January 11, 2019. .
- Gideon Schechtman. More on embedding subspaces of $`L_p`$ in $`l_r^n`$. _Compositio Mathematica_, 61(2):159–169, 1987. .
- Jean Bourgain. On Lipschitz embedding of finite metric spaces in Hilbert space. _Israel Journal of Mathematics_, 52(1–2):46–52, 1985. doi:10.1007/BF02776078.
- John Lamperti. On the isometries of certain function-spaces. _Pacific Journal of Mathematics_, 8(3):459–466, 1958. doi:10.2140/pjm.1958.8.459.
- Haskell P. Rosenthal. On the subspaces of $`L^p`$ $`(p>2)`$ spanned by sequences of independent random variables. _Israel Journal of Mathematics_, 8:273–303, 1970. doi:10.1007/BF02771562.
- OpenAI. _A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding_. OpenAI Math Release preprint OAI:A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026, 2026.
- Allen Hatcher. _Algebraic Topology_. Cambridge University Press, Cambridge, 2002. .
- William B. Johnson and Joram Lindenstrauss. Extensions of Lipschitz mappings into a Hilbert space. In _Conference in Modern Analysis and Probability_, Contemporary Mathematics, volume 26, pages 189–206. American Mathematical Society, Providence, RI, 1984. doi:10.1090/conm/026/737400.
- Iosif Pinelis. Exact Rosenthal-type bounds. _The Annals of Probability_, 43(5):2511–2544, 2015. doi:10.1214/14-AOP942.
- Aaron Schild, Satish Rao, and Nikhil Srivastava. Localization of electrical flows. In _Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms_, pages 1577–1584, 2018. doi:10.1137/1.9781611975031.103. Preprint version: arXiv:1708.01632v1.
- R. Tyrrell Rockafellar. _Convex Analysis_. Princeton Mathematical Series, volume 28. Princeton University Press, Princeton, NJ, 1970; second printing, 1972.
