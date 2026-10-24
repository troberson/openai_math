[Notes](../../README.md) / [Summaries](../README.md) / [Algebraic and complex geometry](../../index/disciplines/algebraic-and-complex-geometry.md) / [Family 047](../../index/algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md)

# 047 — Complex counterexamples to cancellation and affine fibrations

[Index page](../../index/algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md)

## Original CONTENTS.md summary

 carries the family entry:

> Constructs an integral complex affine fourfold $X\not\cong\mathbb A^4$ with $X\times\mathbb A^1\cong\mathbb A^5$, disproving affine-space cancellation over $\mathbb C$ in dimension four. It also disproves the Dolgachev–Weisfeiler affine-fibration conjecture: smooth surjections $X\to\mathbb A^1$ and $\mathbb A^5\to\mathbb A^2$ have every residue-field fiber isomorphic to affine three-space but are not Zariski-locally trivial. [S1:170]

The entry links the manuscript as "An explicit failure of complex affine-space cancellation [S1:170]" .

The manuscript's title is `An Explicit Failure of Complex Affine-Space Cancellation` [S2:1].

The README dates it September 23, 2026 [S2:5].

## Undergraduate summary

The Zariski cancellation problem asks whether an affine variety is determined by its cylinder. Over the complex numbers, the algebraic form is: if adjoining one polynomial variable turns a finitely generated algebra $A$ into a polynomial ring, is $A$ itself a polynomial ring?

The manuscript's abstract states the answer. says: "We construct an explicit integral complex affine fourfold $X$ with $X\times\mathbb A^1\cong\mathbb A^5$ but $X\not\cong\mathbb A^4$. This gives a negative answer to Zariski's affine-space cancellation problem over $\mathbb C$ in dimension four. The same construction disproves the Stable Coordinate Conjecture in ambient dimension five and yields smooth $\mathbb A^3$-fibrations over $\mathbb A^1$ and $\mathbb A^2$ that are not Zariski-locally trivial. These fibrations disprove the Dolgachev–Weisfeiler affine-fibration conjecture over these bases. [S3:9–17]"

The main theorem names the algebra. gives it: "The algebra $A$ in   is an integral complex algebra of dimension four. For an independent variable $w$, \[ A[w]\simeq\kk\poly5, \qquad A\not\simeq\kk\poly4. \] Consequently the Zariski cancellation problem over the complex numbers has a negative answer in dimension four. [S6:61–69]"

The stabilizing variable is the one adjoined in the theorem. [S6:42–46] states its role: "over $\mathbb C$ for $n=4$. The defining polynomial also gives a negative answer to the Stable Coordinate Conjecture over $\kk$ in ambient dimension five, already after adjoining one variable. [S6:43–46]"

The affine-fibration consequence is stated in the introduction. names the two counterexamples: "The residual-coordinate property of $H$ gives two counterexamples in relative dimension three: [S6:131–132]"

## Graduate summary

The introduction opens with the cancellation question. states it: "The Zariski cancellation problem asks whether an affine variety is determined by its cylinder when that cylinder is affine space. Over the complex numbers, its algebraic formulation is the implication [S6:4–6]"

The formulation is given. gives it: "where $A$ is a finitely generated commutative unital complex algebra, $w$ is an independent polynomial variable, and all isomorphisms fix the complex scalars. Here $C\poly r$ denotes a polynomial ring in $r$ variables over a ring $C$. The hypothesis says that adjoining one variable turns $A$ into a polynomial ring; the question is whether that variable can be cancelled. [S6:13–17]"

An isomorphism of cylinders need not respect the projection. states it: "An isomorphism of cylinders need not respect the given projection to the affine line, so its existence alone does not identify polynomial coordinates on $A$. [S6:18–20]"

Cancellation for the affine line is settled. records it: "Cancellation for the affine line follows from the work of Abhyankar, Heinzer, and Eakin [S6:22–23]"

The characteristic-zero problem in higher dimension is listed as open. records it: "The characteristic-zero problem in dimensions at least three is still listed as open in Gaifullin–Petrov's July 2026 [S6:37–38]"

The stabilization belongs to the theory of residual and stable coordinates. states it: "The stabilization belongs to the theory of residual and stable coordinates. A polynomial in $\kk[p]\poly4$ is a _residual coordinate_ if its image is a polynomial coordinate over the residue field of every prime of $\kk[p]$; it is _one-stably a coordinate_ if it becomes a coordinate after adjoining one variable. Our $H$ is a residual coordinate: it is a coordinate after inverting $p$, while a linear change in $F,J$ makes its reduction at $p=0$ a coordinate. [S6:73–79]"

The Stable Coordinate Conjecture is stated. states it: "The Stable Coordinate Conjecture asks whether a polynomial $f\in\kk\poly n$ that becomes a coordinate in $\kk\poly{n+1}$ after adjoining one variable must already be a coordinate in $\kk\poly n$ [S6:84–86]"

The polynomial $H$ is the counterexample. states it: "The polynomial $H$ in   is not a coordinate of $P=\kk[p,s,u,F,J]$, but it is a coordinate of $P[w]$ for one independent variable $w$. Thus the Stable Coordinate Conjecture over $\kk$ fails in ambient dimension five after one stabilization. [S6:92–95]"

The stabilization method is exponential. describes it: "A derivation $D$ is _locally nilpotent_ if every element is killed by some iterate of $D$; over $\kk$, its exponential is an algebraic action of the additive group $\Ga$. We make the stabilization method explicit. A locally nilpotent derivation of $P$ sends $H$ to $p^3$. Exponentiating it converts $H$ into $H+p^3w$, and a coordinate calculation identifies the resulting quotient with a polynomial ring. This exponential-shift argument follows the method of [S6:112–118]"

The affine-fibration term is defined. defines it: "An $\Aff^3$-fibration is a morphism of complex affine varieties whose base change to every geometric point of the target is affine three-space. [S6:125–126]"

The Dolgachev–Weisfeiler assertion is stated. states it: "The affine-fibration assertion of Dolgachev and Weisfeiler predicts that an affine morphism to a normal locally noetherian integral base is Zariski-locally a product with affine $r$-space if every fiber is affine $r$-space over its residue field [S6:127–130]"

Both maps are smooth fibrations that are not locally trivial. [S6:138–141] states it: "Both maps are smooth $\Aff^3$-fibrations, but neither is a Zariski-locally trivial $\Aff^3$-bundle.   proves this consequence using the locally-polynomial-algebra theorem [S6:138–140]"

The main work is proving $A$ is not polynomial. states it: "The main work is to prove that $A$ itself is not polynomial. Additive actions have long served to distinguish affine varieties from affine space: Makar-Limanov used them to show that the Russell cubic is not affine three-space [S6:145–148]"

The valuation degree is defined. [S6:165–168] defines it: "The order $\ord_p$ along $p=0$ in $S$ applies to every nonzero element of $A$. Its negative defines the _valuation degree_ $\deg h=-\ord_p(h)$ and a filtration of $A$. We prove the exact [S6:165–167]"

The graded identification is an affine modification. states it: "Here $\tau$ is an indeterminate representing the initial form of $p$, and the right-hand side is generated by $R$, $\tau$, and all $i/\tau^2$ with $i\in I$. The coefficient inclusion is the one induced by $S\subset A$: the residue of $b\in S$ corresponds to its degree-zero class. This is an affine modification of $R[\tau]$ in the sense of Kaliman–Zaidenberg, and it is smooth. [S6:173–179]"

The polynomial assumption yields an action. yields it: "If $A$ were polynomial, some polynomial coordinate would have positive valuation degree: otherwise all of $A$ would have nonpositive degree, contrary to $\deg F=2$. Differentiation in a different coordinate fixes that positive-degree coordinate. The exact graded identification then induces a nonzero homogeneous locally nilpotent derivation of $G$ with a nonzero homogeneous invariant of positive degree. This is the action the remaining two stages exclude. [S6:181–187]"

The torus bundle principalizes $I$. states it: "The standard torus bundle from $\mathrm{SL}_2$ to the smooth affine quadric principalizes $I$ after adjoining the unchanged variable $u$. [S6:190–191]"

The weights are recorded. records them: "The valuation degree is zero on $\Rt$, with $\deg\tau=-1$ and $\deg V=2$. Separately, fiber scaling gives $a,d$ weight $1$, $b,c$ weight $-1$, and $u,\tau$ weight $0$; thus $v,V$ have fiber weight $2$. [S6:204–207]"

The lift is unique and homogeneous. states it: "The morphism $\Spec\Gt\to\Spec G$ is the complement of the zero section in a line bundle. Every additive action on the smooth affine base $\Spec G$ lifts uniquely to an action on this line bundle that is linear on fibers and normalized at the identity. For the homogeneous action just obtained, uniqueness makes the lift homogeneous with the same valuation degree shift, while fiber linearity preserves fiber weights. This applies even when the original action does not preserve the quadric algebra $R$. [S6:209–216]"

The lift constrains the derivation. states it: "Thus the lift converts the geometric action into a constrained derivation on the explicit determinant ring. [S6:225–226]"

The highest component is constrained. states it: "A highest component $E'$ for an auxiliary grading remains a nonzero locally nilpotent derivation with the same fiber weight. The grading separates the two parts of $v$ so that $(E')^2(d^2+a^2u^3)=0$. The polynomial orbit of $d^2+a^2u^3$ therefore has degree at most one. [S6:229–232]"

The inequality forces a contradiction. forces it: "The Mason–Stothers polynomial $abc$ inequality and the nonsquareness of $-u^3$ in $\Frac\Rt$ force $E'$ to fix $a,d,u$. The determinant relation then forces positive fiber weight, contradicting the sign obtained in the preceding stage. [S6:233–236]"

## History of the conjecture

The characteristic-zero problem in higher dimension is listed as open. records it: "The characteristic-zero problem in dimensions at least three is still listed as open in Gaifullin–Petrov's July 2026 [S6:37–38]"

Additive actions have long served to distinguish affine varieties from affine space. records it: "The main work is to prove that $A$ itself is not polynomial. Additive actions have long served to distinguish affine varieties from affine space: Makar-Limanov used them to show that the Russell cubic is not affine three-space [S6:145–148]"

The organization of the proof is recorded. records it: "records the rings used in the argument.   proves the stabilization.   constructs the filtration and identifies $G$.   describes the torus bundle and proves the lifting statement.   extracts the constrained derivation on $\Rt$, and   excludes it and completes the proof of  .   derives the two nontrivial affine-space fibrations. All locally nilpotent derivations and algebraic group actions in the proof are defined over $\kk$. [S6:263–271]"

## Section skeleton

- `build/main.tex` [S3:9–17]
- `build/preamble.tex` [S4]
- `build/sections/01-introduction.tex` [S6]
- `build/sections/02-construction.tex` [S7]
- `build/sections/03-degeneration.tex` [S8]
- `build/sections/04-bundle.tex` [S9]
- `build/sections/05-reduction.tex` [S10]
- `build/sections/06-rigidity.tex` [S11]
- `build/sections/07-affine-fibrations.tex` [S12]
- `build/references.tex` [S5]

## Comparison with the formalized statement

The scope note states the formalized claim. says: "Affine-space cancellation asks whether $X\times\mathbb A^1\cong\mathbb A^{n+1}$ forces $X\cong\mathbb A^n$. The formalized result gives an explicit finite-type complex domain $A$ of Krull dimension four with $A[w]\cong\mathbb C[x_1,\ldots,x_5]$ but $A\not\cong\mathbb C[x_1,\ldots,x_4]$. Thus adjoining one variable erases a genuine algebraic distinction. [S13:9]"

The scope note states what is not included. says: "The separate stable-coordinate and general line-bundle lifting consequences are not included. [S13:11]"

The declaration is `OAI.ComplexCancellation.main` [S14:32]. The comparator stub carries `sorry` at `ComplexCancellation.lean:26` [S15:26].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 859 | Family entry, line 170 |
| S2 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/README.md`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/README.md) | 18 | Manuscript title, date |
| S3 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/main.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/main.tex) | 27 | Abstract, lines 9–17 |
| S4 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/preamble.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/preamble.tex) | 43 | Macro definitions |
| S5 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/references.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/references.tex) | 172 | Bibliography entries |
| S6 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/01-introduction.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/01-introduction.tex) | 271 | Introduction: theorem, history, proof stages |
| S7 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/02-construction.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/02-construction.tex) | 256 | Construction |
| S8 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/03-degeneration.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/03-degeneration.tex) | 369 | Degeneration |
| S9 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/04-bundle.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/04-bundle.tex) | 412 | Bundle |
| S10 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/05-reduction.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/05-reduction.tex) | 239 | Reduction |
| S11 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/06-rigidity.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/06-rigidity.tex) | 338 | Rigidity |
| S12 | [`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/07-affine-fibrations.tex`](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/07-affine-fibrations.tex) | 154 | Affine fibrations |
| S13 | [`lean/docs/047.md`](../../../lean/docs/047.md) | 17 | Scope |
| S14 | [`lean/OAI/Algebra/AffineCancellation/Main.lean`](../../../lean/OAI/Algebra/AffineCancellation/Main.lean) | 38 | Declaration |
| S15 | [`lean/ComparatorChallenges/ComplexCancellation.lean`](../../../lean/ComparatorChallenges/ComplexCancellation.lean) | 32 | Comparator stub |

## Bibliography

- S. S. Abhyankar, W. Heinzer, and P. Eakin, _On the uniqueness of the coefficient ring in a polynomial ring_, J. Algebra **23** (1972), no. 2, 310–342.  .
- T. Asanuma, _Polynomial fibre rings of algebras over Noetherian rings_, Invent. Math. **87** (1987), 101–127.  .
- The Stacks Project Authors, _The Stacks Project_, accessed September 23, 2026.  .
- H. Bass, E. H. Connell, and D. L. Wright, _Locally polynomial algebras are symmetric_, Bull. Amer. Math. Soc. **82** (1976), no. 5, 719–720.  .
- M. Brion, _On linearization of line bundles_, J. Math. Sci. Univ. Tokyo **22** (2015), no. 1, 113–147.  .
- B. Yu. Weisfeiler and I. V. Dolgachev, _Unipotent group schemes over integral rings_, Math. USSR-Izv. **8** (1974), no. 4, 761–800.  .
- T. Fujita, _On Zariski problem_, Proc. Japan Acad. Ser. A Math. Sci. **55** (1979), no. 3, 106–110.  .
- N. Gupta, _On the cancellation problem for the affine space $\mathbb A^3$ in characteristic $p$_, Invent. Math. **195** (2014), no. 1, 279–288.  .
- N. Gupta, _On Zariski's cancellation problem in positive characteristic_, Adv. Math. **264** (2014), 296–307.  . Preprint: arXiv:1309.1368v1.
- N. Gupta, _The Zariski cancellation problem and related problems in affine algebraic geometry_, in _Proceedings of the International Congress of Mathematicians 2022_, vol. 3, EMS Press, Berlin, 2023, 1578–1598.  .
- A. K. Dutta and A. Lahiri, _On residual and stable coordinates_, J. Pure Appl. Algebra **225** (2021), no. 10, article 106707.  . Preprint: arXiv:1908.03549v1.
- Sh. Kaliman and L. Makar-Limanov, _AK-invariant of affine domains_, in _Affine Algebraic Geometry_, Osaka University Press, Osaka, 2007, 231–255.  .
- L. Makar-Limanov, _On the hypersurface $x+x^2y+z^2+t^3=0$ in $\mathbb C^4$ or a $\mathbb C^3$-like threefold which is not $\mathbb C^3$_, Israel J. Math. **96** (1996), 419–429.  .
- L. Makar-Limanov, P. van Rossum, V. Shpilrain, and J.-T. Yu, _The stable equivalence and cancellation problems_, Comment. Math. Helv. **79** (2004), no. 2, 341–349.  .
- R. C. Mason, _Diophantine Equations over Function Fields_, London Mathematical Society Lecture Note Series **96**, Cambridge University Press, Cambridge, 1984.  .
- D. Finston and S. Maubach, _Constructing (almost) rigid rings and a UFD having infinitely generated Derksen and Makar-Limanov invariants_, Canad. Math. Bull. **53** (2010), no. 1, 77–86.  .
- S. Maubach, _The commuting derivation conjecture_, J. Pure Appl. Algebra **179** (2003), nos. 1–2, 159–168.  .
- M. El Kahoui and M. Ouali, _A note on residual coordinates of polynomial rings_, J. Commut. Algebra **10** (2018), no. 3, 317–326.  .
- S. Gaifullin and M. Petrov, _Non-cancellative varieties, maximal tori, and the Makar-Limanov invariant_, preprint, 15 July 2026. arXiv:2607.13593v1.
- J. Blanc and I. van Santen, _Embeddings of affine spaces into quadrics_, Trans. Amer. Math. Soc. **371** (2019), no. 12, 8429–8465.  .
- W. W. Stothers, _Polynomial identities and Hauptmoduln_, Quart. J. Math. Oxford Ser. (2) **32** (1981), no. 3, 349–370.  .
- M. Miyanishi and T. Sugie, _Affine surfaces containing cylinderlike open sets_, J. Math. Kyoto Univ. **20** (1980), no. 1, 11–42.  .
- A. A. Suslin, _Projective modules over a polynomial ring are free_, Dokl. Akad. Nauk SSSR **229** (1976), no. 5, 1063–1066.  .
- C. Traverso, _Seminormality and Picard group_, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (3) **24** (1970), no. 4, 585–595.  .
- E. Edo and S. Vénéreau, _Length $2$ variables of $A[x,y]$ and transfer_, Ann. Polon. Math. **76** (2001), nos. 1–2, 67–76.  .
- Sh. Kaliman and M. Zaidenberg, _Affine modifications and affine hypersurfaces with a very transitive automorphism group_, Transform. Groups **4** (1999), no. 1, 53–95.  .
