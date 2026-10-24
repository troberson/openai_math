[Notes](../../README.md) / [Summaries](../README.md) / [Algebra](../../index/disciplines/algebra.md) / [Family 198](../../index/algebra/198-a-counterexample-to-the-little-finitistic-dimension-conjecture.md)

# 198 — A counterexample to the little finitistic-dimension conjecture

[Index page](../../index/algebra/198-a-counterexample-to-the-little-finitistic-dimension-conjecture.md)

## Original CONTENTS.md summary

 carries the family entry:

> Constructs a finite-dimensional complex algebra whose finite-dimensional modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension conjecture. [S1:477]

The entry names the manuscript "An algebra of infinite little finitistic dimension [S1:477]" .

The README title is `An algebra of infinite little finitistic dimension` [S2:1].

The README dates it September 23, 2026 [S2:5].

## Undergraduate summary

The little finitistic dimension of an algebra is the supremum of the projective dimensions of its finitely generated modules that have finite projective dimension. The conjecture says that supremum is finite for every finite-dimensional algebra.

The manuscript's abstract states the result. states it: "We construct a finite-dimensional complex algebra whose finite-dimensional modules have unbounded finite projective dimensions. This disproves the little finitistic-dimension conjecture. [S3:9–11]"

The main theorem is the same claim, stated module by module. gives it: "There is a finite-dimensional unital complex algebra \(A\) such that, for every integer \(m\ge1\), there is a finite-dimensional left \(A\)-module \(N_m\) with \[ 2m-2\le\pd_A N_m<\infty. \] In particular, \(\findim A=\infty\). [S4:25–31]"

The algebra is fixed once, and the modules vary. makes that the point: "The algebra in   is fixed before \(m\) varies. Consequently its finitely generated modules admit terminating projective resolutions of unbounded lengths. This also makes its big finitistic dimension infinite and refutes the corresponding universal finiteness assertion for Artin algebras, since a finite-dimensional complex algebra is an Artin algebra. [S4:34–39]"

## Graduate summary

The conjecture is stated in the introduction, where the finitistic dimension is defined as a supremum over modules with finite projective dimension. states it: "The little finitistic-dimension conjecture asserts that this number is finite for every such algebra. Thus it asks for a bound on the lengths of the finite projective resolutions over each fixed algebra, while allowing other modules to have infinite projective dimension. [S4:12–15]"

The lineage is recorded. names Bass and the big variant: "The finitistic-dimension questions were publicized by Bass in 1960  . The _big_ finitistic dimension \(\Findim A\) is defined by allowing all left modules in the same supremum; the little dimension is at most the big one. [S4:16–19]"

The paper states its own verdict. says: "This paper gives a negative resolution of the little finitistic-dimension conjecture. [S4:21–22]"

The companion is distinguished. describes it: "Independently, the companion \cite[Corollary 1.3]OpenAITachikawa2026 obtains finite-dimensional opposite endomorphism algebras \(\Gamma_K\) of infinite little and big left finitistic dimensions for every field extension \(K/k\), where \(k=\mathbb F_2(q,H_1,H_2)\), using successive cokernels in a projective-injective resolution. This is a distinct characteristic-two example; the algebra in Theorem   remains the complex example constructed here. [S4:41–47]"

The equality question is separated from finiteness. records Huisgen-Zimmermann's counterexample to equality: "The equality of the little and big finitistic dimensions is a different question from their finiteness. Huisgen-Zimmermann disproved that equality: for every integer \(n\ge2\), she constructed a finite-dimensional monomial algebra with little finitistic dimension \(n\) and big finitistic dimension \(n+1\)  . Those examples have finite finitistic dimensions and vary with \(n\); they do not give unbounded finite projective dimensions over a single algebra. Her survey   describes the development of the two questions. [S4:51–58]"

The positive cases are listed. lists two: "Important positive cases for little finitistic finiteness include finite-dimensional monomial algebras, by Green, Kirkman, and Kuzmanovich  , and Artin algebras with radical cube zero, by Green and Huisgen-Zimmermann  . [S4:60–64]"

The syzygy invariants are named. names them: "Igusa and Todorov introduced numerical invariants of syzygies that give another proof of the radical-cube-zero case and establish little finiteness for Artin algebras of representation dimension at most three \cite[Corollaries 7 and 9]IgusaTodorov2005. [S4:65–68]"

Cummings' reduction is stated. states it: "More recently, Cummings proved that universal little finitistic finiteness is equivalent to the assertion that, for every finite-dimensional algebra, finiteness holds on the left if and only if it holds on the right \cite[Theorem A]Cummings2024. [S4:69–72]"

The derived-category consequence is drawn through Rickard. sets it up: "There is also a derived-category consequence. Say that injective left modules _generate_ if the smallest triangulated subcategory of the unbounded derived category of all left modules that contains them and is closed under arbitrary coproducts is the whole category. Rickard proved that injective generation implies finite big finitistic dimension \cite[Theorem 4.3]Rickard2019. [S4:77–82]" draws the conclusion: "Thus injective left \(A\)-modules do not generate for the algebra of  : its big left finitistic dimension is infinite. This applies Rickard's theorem to \(A^{\mathrmop}\), matching his right-module convention. [S4:82–85]"

The asymmetry is announced. announces it: "Combining this example with Cummings' auxiliary triangular algebra gives an extreme left–right asymmetry for both dimensions and for injective generation. [S4:87–89]"

The corollary is stated. states it: "There is a finite-dimensional unital complex algebra \(\Lambda\) such that \[ \findim \Lambda=\Findim \Lambda=\infty, \qquad \findim(\Lambda^{\mathrmop})=\Findim(\Lambda^{\mathrmop})=0. \] All four dimensions here use left modules. Thus the little and big finitistic dimensions of \(\Lambda\) are infinite on the left and zero on the right. Injective left \(\Lambda\)-modules do not generate the unbounded derived category of all left \(\Lambda\)-modules, whereas injective right \(\Lambda\)-modules generate the unbounded derived category of all right \(\Lambda\)-modules. [S4:93–104]"

The auxiliary algebra is bounded. bounds it: "The algebra \(\Lambda\) is auxiliary: the corollary makes no assertion about the right finitistic dimensions or right injective generation of the original algebra \(A\). Passing from \(\Lambda\) to \(\Lambda^{\mathrmop}\) reverses the two sides of the corollary. We give the proof in  , after constructing \(A\). [S4:107–112]"

The proof is announced as three stages. announces them: "The proof connects a finite presentation with a derived tensor process and then with ordinary projective resolutions. We describe the three stages, including the points at which compatibility of the constructions is needed. [S4:116–119]"

The first stage is a group algebra. describes it: "First,   constructs one finitely presented complex algebra \(R\), a central idempotent \(e\), and an automorphism \(\alpha\). The functor \[ H(Y)={}_{\alpha}(eY) \] selects the direct summand \(eY\) and restricts its action along \(\alpha\). It admits finite-dimensional modules \(Y_m\) that survive exactly \(m-1\) iterations and vanish on the \(m\)th. The algebra \(R\) is a group algebra. In the underlying group, an automorphism shifts an indexed family of central involutions; finite matrix quotients detect arbitrarily long independent segments of that family. Prescribing their characters gives the modules \(Y_m\). The group is motivated by matrix groups of Abels type  ; its finite presentation, centrality relations, quotients, and representations are established here. [S4:121–136]"

The selection proposition is the fixed data. states it: "There exist a finitely presented unital complex algebra $R$, a central idempotent $e\in R$, and an automorphism $\alpha$ of $R$ such that, for every integer $m\geq 1$, a finite-dimensional left $R$-module $Y_m$ satisfies $$H^{\circ j}(Y_m)\neq 0\quad(0\leq j<m), \qquad H^{\circ m}(Y_m)=0. \label{eq:extinction}$$ The algebra, idempotent, and automorphism are independent of $m$. [S5:21–30]"

The second stage encodes the presentation. describes the encoding: "We first encode the presentation of $R$ in a finite-dimensional directed algebra. This is a three-vertex version of the homogenized quiver construction in \cite[Section 1, Theorem 1.1 and Proposition 1.2]NRS2004. We then work directly with a Verdier quotient and its evaluation functors. [S6:15–19]" gives the quadratic form: "Choose a presentation \[ R=k\langle x_1,\ldots,x_d\rangle/(p_1,\ldots,p_t) \] in which each $p_j$ has degree at most two, allowing constant and linear terms. Such a presentation exists: in any finite presentation, introduce finitely many auxiliary generators for the successive partial products in its finitely many monomials, together with their binary-product definitions. The resulting relations have degree at most two, and eliminating the auxiliary generators recovers the original presentation. [S6:23–32]"

The realization is stated. states it: "The second stage realizes this selection process over a finite-dimensional algebra. A quadratic presentation of \(R\) gives a directed algebra \(B\) with three vertices and \(\gldim B\le2\), together with modules \(M(Y)\). The module \(M(Y)\) places the vector space \(Y\) at each vertex and records the generator actions along the arrows. The encoding follows the homogenization principle used in universal localization  . The principal realization statement,  , constructs a fixed bounded \(B\)-bimodule complex \(P\), projective term by term on the right, for which \[ P\otL_B M(Y)\simeq M(H(Y))\oplus M(H(Y))[3] \] for every finite-dimensional \(R\)-module \(Y\). [S4:138–152]"

The realization theorem is the formal statement. states it: "Let \(k\) be a field, let \(R\) be a finitely presented \(k\)-algebra, let \(e\in R\) be a central idempotent, and let \(\alpha:R\to R\) be a unital endomorphism. Use the finite-dimensional algebra \(B\) and the modules \(M(Y)\) constructed in the preceding section, and put \(H(Y)={}_{\alpha}(eY)\). There is a single bounded complex \(P\) of finite-dimensional \(B\)-bimodules, termwise projective on the right, such that for every finite-dimensional left \(R\)-module \(Y\) one has \beginequation  P\otL_B M(Y) \simeq M(H(Y))\oplus M(H(Y))[3] \qquadin \D^b(B-\modu). [S7:9–21]"

The obstacle is uniformity. names it: "The principal obstacle is to make this realization uniform in \(Y\). Inverting the two distinguished arrows of \(B\) makes the presentation of \(R\) act on a localized category of complexes. The summand selected by \(e\) need not lift by itself; two mapping cones represent its direct sum with a copy shifted by three inside that localized category ( ). We then clear denominators for one finite diagram, before choosing any test module ( ). Its relations initially hold only up to chain homotopy. A three-column differential incorporates those homotopies into an actual bimodule complex ( ). There are no paths of length three, so no further relation overlaps require higher compatibility data. Finally, the gap between the two surviving cohomological degrees exceeds the global-dimension bound on \(B\), so the complex splits as displayed. These steps realize selection by a single tensor functor over \(B\). [S4:154–168]"

The third stage replaces the complex by a bimodule. describes it: "The third stage turns this bounded complex into an ordinary bimodule. A directed radical-square-zero chain records the terms and differential of \(P\). With a suitable product algebra \(D\) of finite global dimension and an ordinary \(D\)-bimodule \(X\), the second iterate of \(F=X\otL_D-\) is isomorphic, on the \(B\)-factor of \(D\), to \(P\otL_B-\) up to a fixed shift ( ). We then take \[ A=D\ltimes X. \] [S4:170–179]"

The simulation proposition is the formal statement. states it: "The algebra \(D\) has finite global dimension on both sides. Let \(F=X\otL_D-\). For every complex \(Z\) of left \(B\)-modules, regarded as a complex on the first factor of \(D\), there is an isomorphism \beginequation   F^2(Z)\simeq P[b_*]\otL_B Z, \qquad [S8:79–86]"

The bar splitting is the transfer. states it: "For a \(D\)-module \(N\) inflated to \(A\), the absolute bar construction decomposes by the number of occurrences of \(X\): \[ D\otL_A N\simeq\bigoplus_{r\ge0}(F^rN)[r]. \] [S4:180–184]" records its provenance: "proves this decomposition with derived tensor powers, including the nonflat case. This splitting is also a consequence of Minamoto and Yamaura's graded-component decomposition for trivial extensions \cite[Lemma 4.13(4) and the proof of Theorem 4.17]MinamotoYamaura. Their projective-dimension formula gives a stronger form of the final transfer. We prove the required splitting directly by the bar construction and give the minimal-resolution argument used here. [S4:185–192]"

The bar splitting proposition is stated over the square-zero algebra. states it: "Let \(D\) be a finite-dimensional \(k\)-algebra, let \(X\) be a finite-dimensional \(D\)-bimodule, and let \(A=D\ltimes X\) be the algebra with multiplication \[ (d,x)(d',x')=(dd',dx'+xd'). \] Let \(N\) be a left \(D\)-module, inflated to \(A\) through the projection \(A\to D\), and put \(F=X\otL_D-\). In the derived category of left \(D\)-modules there is an [S9:21–29]"

The transfer gives the bounds. gives them: "Eventual vanishing of \(F^rN\) yields finite projective dimension, while a nonzero \(r\)th iterate forces projective dimension at least \(r\). For \(N_m=M(Y_m)\), the two-step simulation of selection gives \(F^2mN_m\simeq0\) and \(F^{2m-2}N_m\not\simeq0\). These yield the finiteness and lower bound in  , respectively. [S4:193–197]"

The fixed data are assembled once. assembles them: "Work over \(k=\C\). Fix the algebra \(R\), its central idempotent \(e\), the automorphism \(\alpha\), and the selection functor \(H\) supplied by  . Apply   to these fixed data, obtaining \(B\) and \(P\) satisfying  . Choose the support interval \([a_*,b_*]\) once, and construct \(C,W,O,D,X\) as in  . [S9:254–263]"

The asymmetry is transported by Morita equivalence. transports it: "Let \(A\) be the algebra of  , and choose a basic finite-dimensional complex algebra \(C\) Morita equivalent to \(A^{\mathrmop}\). The right-module little and big finitistic dimensions of \(C\) are infinite, and its injective right modules do not generate: these are the conclusions for left \(A\)-modules in  , transported through Morita equivalence. Indeed, this equivalence preserves projective dimensions and finite generation, and the induced equivalence of unbounded derived categories preserves injectives and coproducts. [S9:347–355]"

## Section skeleton

- `build/sections/01-introduction.tex` [S4]
  - Introduction (line 1)
  - The main result (line 11)
  - Background and consequences (line 49)
  - The left-right asymmetry corollary (line 78)
  - The construction and its principal mechanisms (line 114)
  - Conventions (line 212)
- `build/sections/02-selection-process.tex` [S5:21–30]
  - The selection process (line 1)
  - The group and its finite presentation (line 11)
  - Finite quotients and characters (line 101)
  - The selection functor (line 211)
  - The extinction property (line 309)
- `build/sections/03-localization-and-lifting.tex` [S6]
  - Localization and a fixed lifted diagram (line 1)
  - A quadratic presentation and its directed encoding (line 21)
  - The Verdier quotient and evaluation functors (line 101)
  - A lifted diagram (line 211)
  - Rectification (line 341)
- `build/sections/04-tensor-realization.tex` [S7:9–21]
  - Tensor realization of the selection process (line 1)
  - The realization theorem (line 7)
  - The localized module category (line 41)
  - The lifted tensor diagram (line 121)
  - The natural isomorphism (line 211)
  - The splitting (line 261)
- `build/sections/05-ordinary-simulation.tex` [S8:79–86]
  - Ordinary simulation of the tensor process (line 1)
  - The product algebra and bimodule (line 11)
  - The compression (line 77)
  - The simulation statement (line 111)
- `build/sections/06-square-zero-and-conclusion.tex` [S9]
  - The square-zero algebra and the conclusion (line 1)
  - The bar construction (line 19)
  - The finitistic dimension transfer (line 121)
  - The fixed algebra and its modules (line 251)
  - The auxiliary left-right asymmetry (line 343)

## Comparison with the formalized statement

The scope note states what the formalized theorem says. says: "The little finitistic-dimension conjecture predicts that finitely generated modules of finite projective dimension over a fixed finite-dimensional algebra have bounded projective dimensions. The formalized counterexample is a finite-dimensional complex algebra with a finitely generated module of projective dimension at least $2m-2$ and still finite for every $m\ge1$. [S10:9]"

The scope note states the second formalized fact. says: "A separate formalized result gives a finite-dimensional complex algebra whose little and big finitistic dimensions are infinite on the left and zero on the right. Injectives fail to generate its unbounded derived category on the left and generate it on the right. [S10:11]"

The manuscript names the algebra and the modules; the formalized statement is an existence claim. The declaration is `OAI.LittleFinitistic.Main.exists_counterexample` at `lean/OAI/Algebra/Finitistic/Main.lean:44` [S11:44]. The asymmetry declaration is `OAI.LittleFinitistic.extreme_left_right_asymmetry` at `lean/OAI/Algebra/FinitisticAsymmetry/Main.lean:48` [S12:48].

The comparator stubs carry `sorry` at `lean/ComparatorChallenges/LittleFinitistic.lean:29` [S13:29] and `lean/ComparatorChallenges/FinitisticAsymmetry.lean:35` [S14:35].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 477 |
| S2 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/README.md`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/README.md) | 18 | Title, date |
| S3 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/paper.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/paper.tex) | 21 | Abstract, section inputs |
| S4 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/01-introduction.tex) | 230 | Conjecture, theorem, corollaries, three stages |
| S5 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/02-selection-process.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/02-selection-process.tex) | 377 | Selection proposition |
| S6 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/03-localization-and-lifting.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/03-localization-and-lifting.tex) | 452 | Quadratic presentation, Verdier quotient, lifting, rectification |
| S7 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/04-tensor-realization.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/04-tensor-realization.tex) | 304 | Realization theorem |
| S8 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/05-ordinary-simulation.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/05-ordinary-simulation.tex) | 149 | Simulation proposition |
| S9 | [`preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/06-square-zero-and-conclusion.tex`](../../../preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026/build/sections/06-square-zero-and-conclusion.tex) | 389 | Bar splitting, fixed algebra, asymmetry |
| S10 | [`lean/docs/198.md`](../../../lean/docs/198.md) | 18 | Scope |
| S11 | [`lean/OAI/Algebra/Finitistic/Main.lean`](../../../lean/OAI/Algebra/Finitistic/Main.lean) | 56 | Declaration |
| S12 | [`lean/OAI/Algebra/FinitisticAsymmetry/Main.lean`](../../../lean/OAI/Algebra/FinitisticAsymmetry/Main.lean) | 65 | Declaration |
| S13 | [`lean/ComparatorChallenges/LittleFinitistic.lean`](../../../lean/ComparatorChallenges/LittleFinitistic.lean) | 37 | Comparator stub |
| S14 | [`lean/ComparatorChallenges/FinitisticAsymmetry.lean`](../../../lean/ComparatorChallenges/FinitisticAsymmetry.lean) | 41 | Comparator stub |
