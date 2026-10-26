[Notes](../README.md) / [Summaries](README.md) / [Operator algebras](../index/disciplines/operator-algebras.md) / [Family 300](../index/operator-algebras/300-popa-vaes-quadratic-strong-operator-paving-conjecture.md)

# 300 — The Popa–Vaes quadratic strong-operator paving conjecture

[Index page](../index/operator-algebras/300-popa-vaes-quadratic-strong-operator-paving-conjecture.md)

## Original CONTENTS.md summary

The release's blurb 

> Proves that every self-adjoint element of a complex von Neumann algebra admits strong-operator paving relative to any maximal abelian subalgebra with $`O(\varepsilon^{-2})`$ blocks. The norm bound holds after compression by a projection arbitrarily close to the identity in the strong topology, resolving the Popa–Vaes quadratic paving conjecture. [S1:7430]

The first manuscript's own blurb 

> We prove the approximation-paving conjecture of Popa and Vaes for every maximal abelian subalgebra of a complex von Neumann algebra. [S1:7439]

The second manuscript's blurb 

> We prove the quadratic strong-operator paving conjecture of Popa and Vaes. [S1:7448]

The catalog abstract [S2:692] says the same thing in one entry:
"Proves that every self-adjoint element of a complex von Neumann algebra admits strong-operator paving relative to any maximal abelian subalgebra with $O(\varepsilon^{-2})$ blocks. The norm bound holds after compression by a projection arbitrarily close to the identity in the strong topology, resolving the Popa–Vaes quadratic paving conjecture. [S2:692]" The manuscripts' own titles are
"Approximation Paving over Arbitrary Maximal Abelian Subalgebras [S3:1]" and
"Quadratic Strong-Operator Paving over Arbitrary Maximal Abelian Subalgebras [S4:1]" .

## Undergraduate summary

Paving asks how small the pinching of an operator can be made after subtracting a diagonal element . Norm paving requires the difference itself to be small in operator norm, and "Paving asks how small this operator can be made after subtracting a diagonal element of $A$. Requiring a small norm for $S_P(x)-a$ itself is norm paving, which fails for general masas \cite[Theorem 3.3]PV15. The following strong-operator formulation instead permits a compression whose complement is arbitrarily small in the strong operator topology. [S15:7]" The strong-operator formulation relaxes this: the pinching is small only after compression by a projection whose complement is arbitrarily small in the strong topology.

The definition fixes the number of projections before the test vectors and the neighborhood are chosen: "Let $x=x^*\in M$, $\varepsilon>0$, and $r\ge1$ be an integer. We say that $x$ is _$(\varepsilon,r)$ so-pavable over $A$_ if for every finite $F\subset H$ and every $\delta>0$ there are a partition $P=(p_1,\ldots,p_r)$ in $A$, an element $a=a^*\in A$ with $\|a\|\le\|x\|$, and a projection $q\in M$ such that [S15:10]" The projection $q$ compresses the pinching, and $\|q(S_P(x)-a)q\|\le\varepsilon\|x\|$ is the bound [S15:11–14]. "The integer $r$ is fixed before $F$ and $\delta$ are chosen. [S15:15]" 

The main theorem gives a quadratic bound: "For every masa $A\subseteq M\subseteq\mathcal B(H)$ and every $x=x^*\in M$, the element $x$ is $(\varepsilon,r_\varepsilon)$ so-pavable over $A$. In particular, the number of projections is fixed before the inclusion, operator, and strong neighborhood. No separability or conditional-expectation assumption is imposed on the inclusion. [S15:25]" The partition count $r_\varepsilon$ is at most $5\times10^8\varepsilon^{-2}$ [S15:19–24]. "Theorem   proves the quadratic so-paving conjecture of Popa and Vaes \cite[Conjecture 2.8(2)]PV15. Their definition of so-paving uses arbitrary strong neighborhoods of zero; Definition   gives the equivalent finite-vector formulation \cite[Definition 2.2]PV15. For self-adjoint $x$, allowing a general diagonal element in their definition gives the same condition, since taking its real part preserves the norm bound and the compression estimate. [S15:28]" 

The companion manuscript proves a different paving property for the same class of masas. It norm-paves a nearby bounded operator $y$ with $\|y\|\le3\|x\|$, with error relative to $\|y\|$'s norm [S6:38–57]. "There is a universal constant \(C_{\mathrmap}>0\) such that for every [S6:39]" The partition count is $C\varepsilon^{-6}$, a universal sixth power. "Thus the norm-control constant is universal, and the number of
projections is independent of the algebra, its representation, the [S6:60–61]" "The relative error in the theorem is measured against the actual [S6:64]" the approximant's norm; a clipping argument ensures the normalization [S6:62–66]. The two results are independent, and the companion claims no quadratic rate: "The separate companion \cite[Theorem 1.1]OAQuadratic26 proves a direct [S6:88]" quadratic strong-operator paving bound for the original operator. Theorem   instead norm-paves a nearby bounded operator,
with error relative to that approximant's norm. The two main proofs are
independent; the conversion in Corollary   retains its normal-expectation
hypothesis. We claim no quadratic bound for \(R(\varepsilon)\). [S6:90–93] [S6:88–93]

## Graduate summary

**Manuscript B (quadratic strong-operator paving).** The proof reduces to a faithful central state and decomposes the operator into a Cartan term (normalizer algebra) and a kernel term (atomless kernels) [S16] [S17]. The Cartan term is treated on a relative Bernoulli extension of the measured equivalence relation: each relation class receives independent site labels, and a measurable coloring has uniform conditional color marginals [S18] [S19] [S20]. The finite-dimensional input is the mixed determinantal bound of Ravichandran–Srivastava [S15:79]. The kernel term is handled by a free-product matrix dilation: uniform conditional color marginals give a free compression bound on $\ker E_N$ [S21]. The completion section clips to bounded approximants and transfers a sufficiently high fixed moment to produce the projection $q$ [S22].

**Manuscript A (approximation paving).** The measured argument develops one-sided matrix paving for nonsingular equivalence relations, using the finite paving-polynomial framework of Ravichandran–Luo and Ravichandran–Srivastava [S8] [S9]. A buffered pinning lemma selects a color while controlling positive-root mass [S8:492–530]. Nonsingularity is handled by passing to the Maharam extension and weighting by the height variable [S9:63–165]. The operator-algebra argument paves the normalizer algebra using the Feldman–Moore representation, adapts the free-product matrix dilation of Popa–Vaes with random diagonal phases, and removes the normal-expectation hypothesis through a three-corner construction [S11] [S12].

**The two manuscripts are companions.** Each cites the other as a separate companion. Manuscript B's introduction names the approximation theorem: "Theorem   controls a compression of the pinching of the original $x$. A separate expectation-free approximation-paving theorem instead supplies self-adjoint approximants $y$ near $x$ strongly, with $\|y\|\leq3\|x\|$, and norm-paves them with error measured against $\|y\|$ \cite[Theorem 1.1]ApproxCompanion26. Its arbitrary-masa conclusion has a finite $\varepsilon$-dependent count but states no quadratic rate. The two proofs are independent. [S15:65]" Manuscript A's introduction names the quadratic theorem: "The separate companion \cite[Theorem 1.1]OAQuadratic26 proves a direct [S6:88]" The dependency is symmetric at the statement level: each proves the other's conjecture's companion assertion, and the two proofs are independent .

## History of the conjecture

The classical context is Kadison–Singer and its diagonal paving counterpart, resolved by Marcus–Spielman–Srivastava . "The classical Kadison–Singer paving problem concerns the diagonal masa in $\mathcal B(\ell^2\mathbb N)$. Marcus, Spielman, and Srivastava resolved it by their mixed-characteristic-polynomial method  . For general masas, norm paving is much more restrictive: when $M$ has separable predual, it holds exactly when $M$ is type I and $A$ is the range of a normal conditional expectation \cite[Theorem 3.3]PV15. Strong-operator paving retains a uniform partition count while allowing a compression that approaches the identity strongly. [S15:48]" The restriction to general masas is sharp: norm paving characterizes type I algebras with a normal expectation.

Popa and Vaes introduced the strong-operator and approximation versions and conjectured both for every masa . "Popa's $\mathrm{II}_1$-factor approach established paving for singular-masa ultraproducts  . Popa and Vaes then obtained so-paving bounds of order $\varepsilon^{-4}$ for arbitrary masas in type I algebras with separable predual, for Cartan masas in amenable algebras, and for the Cartan inclusions associated with essentially free ergodic probability-measure-preserving profinite actions of countable groups \cite[Proposition 3.2 and Theorem 4.1]PV15. In contrast, their theorem for tracial ultraproducts of singular masas in finite algebras gives a common norm-paving partition of order $\varepsilon^{-2}$ for each finite family of centered self-adjoint contractions \cite[Theorem 5.1]PV15. Their later work gives the optimal uniform error for singular-masa ultraproducts \cite[Theorem 4.1]PV16. They explicitly identified the need to unite the Cartan and singular arguments \cite[Remark 2.9(ii)]PV15. On the finite-dimensional side, Ravichandran and Srivastava obtained asymptotically optimal multipaving bounds from mixed determinantal polynomials  ; these supply the finite input used here. [S15:50]" Their prior bounds were quartic ($\varepsilon^{-4}$) for arbitrary masas in type I algebras and for Cartan inclusions in amenable algebras, and quadratic only for tracial ultraproducts of singular masas. They "explicitly identified the need to unite the Cartan and singular arguments" . The finite-dimensional input is the multipaving bound of Ravichandran–Srivastava .

The exponent two is necessary: "The exponent two is forced already by the $L^2$ obstruction in a $\mathrm{II}_1$ factor from \cite[Proposition 5.4]PV15. Fix an integer $1\leq n<\varepsilon^{-2}$, choose $\varepsilon<\eta<n^{-1/2}$, and use the centered self-adjoint unitary $x$ from that proposition at threshold $\eta$. Write $\tau$ for the normalized trace and $\|b\|_2=\tau(b^*b)^{1/2}$. For every partition $P$ with $n$ pieces and every $a\in A$, trace orthogonality gives [S15:54]" The argument uses a centered self-adjoint unitary from Popa–Vaes's $L^2$ obstruction proposition and shows that the obstruction persists with the varying diagonals and compressions allowed by strong-operator paving. "The exponent in Theorem   is optimal, although its numerical constant is not optimized. [S15:63]" 

Manuscript A's positioning is the same conjecture from the approximation side: "Kadison and Singer posed the pure-state extension problem for the atomic [S6:15]" diagonal masa of $\mathcal B(\ell^2)$ [S6:15–16]. Anderson formulated its diagonal paving counterpart, and Marcus–Spielman–Srivastava resolved it [S6:17–19]. For general masas, norm paving is too restrictive and characterizes type I algebras [S6:20–21]. Popa and Vaes "introduced strong-operator and approximation versions of paving and conjectured that every MASA has both properties" [S6:22–24]. "approximation versions of paving and conjectured that every MASA has both properties \cite[Definitions 2.2–2.3 and Conjecture 2.8(1)]PV15.
We resolve the approximation-paving assertion of that conjecture positively. [S6:23–25]" The restricted cases (type I, Cartan in amenable algebras, singular ultraproducts) do not provide the expectation-free theorem [S6:27–35].

## Consequences

**Quadratic norm paving in ultrapowers.** The strong-operator result implies norm paving in the Ocneanu ultrapower for countably decomposable expected masas: "**corollary**
Let $A\subseteq M$ be a masa. Suppose that $A$ is countably decomposable and is the range of a normal conditional expectation from $M$. Let $\omega$ be a free ultrafilter on $\mathbb N$, and let $A^\omega\subseteq M^\omega$ be the associated inclusion in the Ocneanu von Neumann ultrapower. For every $0<\varepsilon<1$ and every $x=x^*\in M^\omega$, there are a partition $p_1,\ldots,p_{r_\varepsilon}\in A^\omega$ and an element $a=a^*\in A^\omega$ such that
\[
 \|a\|\le\|x\|,
 \qquad
 \left\|\sum_i=1^{r_\varepsilon}p_i x p_i-a\right\|\le\varepsilon\|x\|.
\]
Here $r_\varepsilon$ is the same integer as in Theorem  . [S15:32–39]" The forward transfer of Popa–Vaes converts the so-paving to norm paving in the ultrapower with the same error and partition count [S15:40–43].

**Quadratic approximation paving for expected MASAs.** When the masa is the range of a normal conditional expectation, the approximation-paving partition count improves from $\varepsilon^{-6}$ to $\varepsilon^{-2}$: "**corollary**
There is a universal constant \(C>0\) such that for every
\(0<\varepsilon<1\) one can choose an integer
\(N(\varepsilon)\leq C\varepsilon^-2\) with the following property.
If the MASA \(A\subseteq M\) is the range of a normal conditional expectation,
then the conclusion of Theorem   holds with [S6:95–101]" in place of $R(\varepsilon)$ [S6:102].

## Section skeleton

**Manuscript A** (main file [S5], 7 sections under `build/source/sections/`):

1. Introduction [S6]
2. State topology and bounded sequence quotients [S7]
3. Finite mixed polynomials and buffered pinning [S8]
4. Measured matrices and coherent choices on Maharam slabs [S9]
5. Sparse pinning and descent [S10]
6. Expected maximal abelian subalgebras [S11]
7. Passage to arbitrary von Neumann algebras [S12]

**Manuscript B** (main file [S14], 8 sections under `build/source/sections/`):

1. Introduction [S15]
2. Reduction to a faithful central state [S16]
3. The normalizing algebra and atomless kernels [S17]
4. Finite polynomials and the cost of assigning a color [S18]
5. Rooted costs on invariant measured graphs [S19]
6. Coloring a nonsingular measured graph [S20]
7. A Bernoulli model and transfer of state moments [S21]
8. Completion of the paving argument [S22]

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning trace. Nothing about this family is machine-checked. The ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`, `trace` empty. The two manuscripts ship 11 `.tex` files each under `build/source/`, with the bibliography as a `\bibitem` list in `references.tex` [S13] [S23].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | The release's blurb for family 300 at line 7430, the two manuscript links at 7437 and 7446, and the two manuscript blurbs at 7439 and 7448. |
| S2 | [`overview.tex`](../../overview.tex) | 859 | The catalog abstract at line 692. |
| S3 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/README.md`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S4 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/README.md`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/README.md) | 18 | Citation-only manuscript readme: title, author, date, BibTeX block. |
| S5 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/main.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/main.tex) | 66 | The main file: the abstract and the section order. |
| S6 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/introduction.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/introduction.tex) | 158 | The conjecture, the main theorem, the strong-operator corollary, the companion paragraph, the expected-MASA corollary, and the proof outline. |
| S7 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/preliminaries.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/preliminaries.tex) | 151 | State topology and bounded sequence quotients. |
| S8 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/polynomials.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/polynomials.tex) | 690 | Finite mixed polynomials, stable polynomials, local spectral data, the initial largest-root bound, residue tails, and the buffered choice. |
| S9 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/slabs.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/slabs.tex) | 700 | Measured matrices, coherent choices on Maharam slabs, invariant measure, locality, far-deletion comparison, and the color choice. |
| S10 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/pinning.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/pinning.tex) | 405 | Sparse pinning, removal of unassigned vertices, and descent from a slab to the base relation. |
| S11 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/expected.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/expected.tex) | 594 | Expected MASAs, the normalizer algebra, random diagonal unitaries, a free-product matrix dilation, and the state-preserving paving argument. |
| S12 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/general.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/general.tex) | 444 | Passage to arbitrary von Neumann algebras: separable reduction, the corner without centralizing normal functionals, assembly of the three corners, and consequences for related formulations. |
| S13 | [`preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sources/references.tex`](../../preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sources/references.tex) | 144 | The bibliography as a `\bibitem` list. |
| S14 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/main.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/main.tex) | 51 | The main file: the abstract and the section order. |
| S15 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/introduction.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/introduction.tex) | 89 | The definition of so-paving, the main theorem, the ultrapower corollary, the history and significance, the optimality argument, the companion paragraph, and the proof outline. |
| S16 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/reductions.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/reductions.tex) | 360 | Reduction to a faithful central state. |
| S17 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/kernels.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/kernels.tex) | 350 | The normalizing algebra and atomless kernels. |
| S18 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/polynomials.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/polynomials.tex) | 681 | Finite polynomials and the cost of assigning a color. |
| S19 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/invariant.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/invariant.tex) | 493 | Rooted costs on invariant measured graphs. |
| S20 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/coloring.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/coloring.tex) | 850 | Coloring a nonsingular measured graph: the probability extension, the coloring theorem, homogeneous costs, and the assignment. |
| S21 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/transfer.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/transfer.tex) | 769 | A Bernoulli model and transfer of state moments. |
| S22 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/completion.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/sections/completion.tex) | 193 | Completion of the paving argument. |
| S23 | [`preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/references.tex`](../../preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/build/source/references.tex) | 122 | The bibliography as a `\bibitem` list. |

## Bibliography

- J. Anderson, _Extensions, restrictions, and representations of states on $C^*$-algebras_, Trans. Amer. Math. Soc. **249** (1979), no. 2, 303–329. doi:10.2307/1998793.
- H. Araki, _Some properties of modular conjugation operator of von Neumann algebras and a non-commutative Radon–Nikodym theorem with a chain rule_, Pacific J. Math. **50** (1974), no. 2, 309–354. Journal PDF.
- Huzihiro Araki, _Some properties of modular conjugation operator of von Neumann algebras and a non-commutative Radon–Nikodym theorem with a chain rule_, Pacific Journal of Mathematics **50** (1974), no. 2, 309–354. Published article.
- G. Boole, _On the comparison of transcendents, with certain applications to the theory of definite integrals_, Philosophical Transactions of the Royal Society of London **147** (1857), 745–803. doi:10.1098/rstl.1857.0037.
- Uffe Haagerup, _The standard form of von Neumann algebras_, Mathematica Scandinavica **37** (1975), 271–283. doi:10.7146/math.scand.a-11606.
- Uffe Haagerup, _$L^p$-spaces associated with an arbitrary von Neumann algebra_, in _Alg\`ebres d'opérateurs et leurs applications en physique mathématique_ (Marseille, 1977), Colloques Internationaux du C.N.R.S. **274**, C.N.R.S., Paris, 1979, pp. 175–184. Original paper.
- F. Hiai, _Concise lectures on selected topics of von Neumann algebras_, 2020, arXiv:2004.02383v1.
- A. S. Kechris, S. Solecki and S. Todorcevic, _Borel chromatic numbers_, Adv. Math. **141** (1999), no. 1, 1–44. doi:10.1006/aima.1998.1771.
- Alexander S. Kechris, _Classical Descriptive Set Theory_, Graduate Texts in Mathematics **156**, Springer-Verlag, New York, 1995. doi:10.1007/978-1-4612-4190-4.
- M. Ravichandran and J. Leake, _Mixed determinants and the Kadison–Singer problem_, Math. Ann. **377** (2020), 511–541. doi:10.1007/s00208-020-01986-7; arXiv:1609.04195v2 (cited theorem numbering).
- D. Maharam, _Incompressible transformations_, Fund. Math. **56** (1964), no. 1, 35–50. doi:10.4064/fm-56-1-35-50.
- Dorothy Maharam, _Incompressible transformations_, Fundamenta Mathematicae **56** (1964), no. 1, 35–50. doi:10.4064/fm-56-1-35-50.
- A. W. Marcus, D. A. Spielman and N. Srivastava, _Interlacing families II: Mixed characteristic polynomials and the Kadison–Singer problem_, Ann. of Math. (2) **182** (2015), no. 1, 327–350. doi:10.4007/annals.2015.182.1.8; arXiv:1306.3969v4.
- Adam W. Marcus, Daniel A. Spielman, and Nikhil Srivastava, _Interlacing families II: Mixed characteristic polynomials and the Kadison–Singer problem_, Annals of Mathematics (2) **182** (2015), no. 1, 327–350. doi:10.4007/annals.2015.182.1.8.
- J. Feldman and C. C. Moore, _Ergodic equivalence relations, cohomology, and von Neumann algebras. II_, Trans. Amer. Math. Soc. **234** (1977), no. 2, 325–359. doi:10.1090/S0002-9947-1977-0578730-2.
- Jacob Feldman and Calvin C. Moore, _Ergodic equivalence relations, cohomology, and von Neumann algebras. II_, Transactions of the American Mathematical Society **234** (1977), 325–359. doi:10.1090/S0002-9947-1977-0578730-2.
- OpenAI, _Quadratic Strong-Operator Paving over Arbitrary Maximal Abelian Subalgebras_, OpenAI Math Release preprint OAI:Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026, 2026.
- OpenAI, _Approximation Paving over Arbitrary Maximal Abelian Subalgebras_, OpenAI Math Release preprint OAI:Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026, 2026, Theorem 1.1.
- A. Poltoratski, B. Simon and M. Zinchenko, _The Hilbert transform of a measure_, 2009, arXiv:0811.0791v2.
- S. Popa, _A $\mathrm{II}_1$ factor approach to the Kadison–Singer problem_, Comm. Math. Phys. **332** (2014), 379–414. doi:10.1007/s00220-014-2055-4; arXiv:1303.1424v3.
- Sorin Popa, _A $\mathrm{II}_1$ factor approach to the Kadison–Singer problem_, Communications in Mathematical Physics **332** (2014), 379–414. doi:10.1007/s00220-014-2055-4.
- Richard V. Kadison and John R. Ringrose, _Fundamentals of the Theory of Operator Algebras_, Vol. II: _Advanced Theory_, Pure and Applied Mathematics **100**, Academic Press, Orlando, FL, 1986. Publisher information.
- P. Roy and G. Samorodnitsky, _Maharam extension for nonsingular group actions_, 2006, arXiv:math/0611891v1.
- Parthanil Roy and Gennady Samorodnitsky, _Maharam extension for nonsingular group actions_, 2006, arXiv:math/0611891v1.
- C. A. Akemann and D. Sherman, _Conditional expectations onto maximal abelian $*$-subalgebras_, J. Operator Theory **68** (2012), no. 2, 597–607. Journal PDF.
- Charles A. Akemann and David Sherman, _Conditional expectations onto maximal abelian star-subalgebras_, Journal of Operator Theory **68** (2012), no. 2, 597–607. Published article.
- R. V. Kadison and I. M. Singer, _Extensions of pure states_, Amer. J. Math. **81** (1959), no. 2, 383–400. doi:10.2307/2372748.
- M. Ravichandran and N. Srivastava, _Asymptotically optimal multi-paving_, Int. Math. Res. Not. IMRN **2021**, no. 14, 10908–10940. doi:10.1093/imrn/rnz111; arXiv:1706.03737v2 (cited theorem numbering).
- Mohan Ravichandran and Nikhil Srivastava, _Asymptotically optimal multi-paving_, International Mathematics Research Notices **2021** (2021), no. 14, 10908–10940. doi:10.1093/imrn/rnz111; numbered theorem locators refer to arXiv:1706.03737v2.
- Robert T. Powers and Erling Størmer, _Free states of the canonical anticommutation relations_, Communications in Mathematical Physics **16** (1970), 1–33. doi:10.1007/BF01645492.
- M. Takesaki, _Conditional expectations in von Neumann algebras_, J. Funct. Anal. **9** (1972), no. 3, 306–321. doi:10.1016/0022-1236(72)90004-3.
- Masamichi Takesaki, _Conditional expectations in von Neumann algebras_, Journal of Functional Analysis **9** (1972), no. 3, 306–321. doi:10.1016/0022-1236(72)90004-3.
- C. Houdayer and Y. Ueda, _Asymptotic structure of free product von Neumann algebras_, Math. Proc. Cambridge Philos. Soc. **161** (2016), no. 3, 489–516. doi:10.1017/S0305004116000396; arXiv:1503.02460v3.
- Yoshimichi Ueda, _Amalgamated free product over Cartan subalgebra_, Pacific Journal of Mathematics **191** (1999), no. 2, 359–392. doi:10.2140/pjm.1999.191.359.
- Yoshimichi Ueda, _Some analysis of amalgamated free products of von Neumann algebras in the non-tracial setting_, Journal of the London Mathematical Society (2) **88** (2013), no. 1, 25–48. doi:10.1112/jlms/jds081.
- S. Popa and S. Vaes, _Paving over arbitrary MASAs in von Neumann algebras_, Anal. PDE **8** (2015), no. 4, 1001–1023. doi:10.2140/apde.2015.8.1001; arXiv:1412.0631v3.
- S. Popa and S. Vaes, _On the optimal paving over MASAs in von Neumann algebras_, Contemp. Math. **671** (2016), 199–208. doi:10.1090/conm/671/13511; arXiv:1507.01072v1.
- Sorin Popa and Stefaan Vaes, _Paving over arbitrary MASAs in von Neumann algebras_, Analysis & PDE **8** (2015), no. 4, 1001–1023. doi:10.2140/apde.2015.8.1001.
- Sorin Popa and Stefaan Vaes, _On the optimal paving over MASAs in von Neumann algebras_, Contemporary Mathematics **671** (2016), 199–208. doi:10.1090/conm/671/13511.
- M. Aizenman and S. Warzel, _On the ubiquity of the Cauchy distribution in spectral problems_, Probab. Theory Related Fields **163** (2015), 61–87. doi:10.1007/s00440-014-0587-3; arXiv:1312.7769v2 (cited proposition numbering).
