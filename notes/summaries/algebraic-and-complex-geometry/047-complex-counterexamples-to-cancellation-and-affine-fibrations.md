Notes / Summaries / Algebraic and complex geometry / [Family 047](../../index/algebraic-and-complex-geometry/047-complex-counterexamples-to-cancellation-and-affine-fibrations.md)

# 047 — Complex counterexamples to cancellation and affine fibrations

## Original CONTENTS.md summary

[S1:170] carries the family entry:

> Constructs an integral complex affine fourfold $X\not\cong\mathbb A^4$ with $X\times\mathbb A^1\cong\mathbb A^5$, disproving affine-space cancellation over $\mathbb C$ in dimension four. It also disproves the Dolgachev--Weisfeiler affine-fibration conjecture: smooth surjections $X\to\mathbb A^1$ and $\mathbb A^5\to\mathbb A^2$ have every residue-field fiber isomorphic to affine three-space but are not Zariski-locally trivial.

The entry links the manuscript as "An explicit failure of complex affine-space cancellation" [S1:170].

The manuscript's title is `An Explicit Failure of Complex Affine-Space Cancellation` [S2:1].

The README dates it September 23, 2026 [S2:5].

## Undergraduate summary

The Zariski cancellation problem asks whether an affine variety is determined by its cylinder. Over the complex numbers, the algebraic form is: if adjoining one polynomial variable turns a finitely generated algebra $A$ into a polynomial ring, is $A$ itself a polynomial ring?

The manuscript's abstract states the answer. [S3:9–17] says: "We construct an explicit integral complex affine fourfold $X$ with $X\times\mathbb A^1\cong\mathbb A^5$ but $X\not\cong\mathbb A^4$. This gives a negative answer to Zariski's affine-space cancellation problem over $\mathbb C$ in dimension four. The same construction disproves the Stable Coordinate Conjecture in ambient dimension five and yields smooth $\mathbb A^3$-fibrations over $\mathbb A^1$ and $\mathbb A^2$ that are not Zariski-locally trivial. These fibrations disprove the Dolgachev--Weisfeiler affine-fibration conjecture over these bases."

The main theorem names the algebra. [S6:61–69] gives it: "The algebra $A$ in   is an integral complex algebra of dimension four. For an independent variable $w$, \[ A[w]\simeq\kk\poly5, \qquad A\not\simeq\kk\poly4. \] Consequently the Zariski cancellation problem over the complex numbers has a negative answer in dimension four."

The stabilizing variable is the one adjoined in the theorem. [S6:42–46] states its role: "over $\mathbb C$ for $n=4$. The defining polynomial also gives a negative answer to the Stable Coordinate Conjecture over $\kk$ in ambient dimension five, already after adjoining one variable."

The affine-fibration consequence is stated in the introduction. [S6:131–132] names the two counterexamples: "The residual-coordinate property of $H$ gives two counterexamples in relative dimension three:"

## Graduate summary

The introduction opens with the cancellation question. [S6:4–6] states it: "The Zariski cancellation problem asks whether an affine variety is determined by its cylinder when that cylinder is affine space. Over the complex numbers, its algebraic formulation is the implication"

The formulation is given. [S6:13–17] gives it: "where $A$ is a finitely generated commutative unital complex algebra, $w$ is an independent polynomial variable, and all isomorphisms fix the complex scalars. Here $C\poly r$ denotes a polynomial ring in $r$ variables over a ring $C$. The hypothesis says that adjoining one variable turns $A$ into a polynomial ring; the question is whether that variable can be cancelled."

An isomorphism of cylinders need not respect the projection. [S6:18–20] states it: "An isomorphism of cylinders need not respect the given projection to the affine line, so its existence alone does not identify polynomial coordinates on $A$."

Cancellation for the affine line is settled. [S6:22–23] records it: "Cancellation for the affine line follows from the work of Abhyankar, Heinzer, and Eakin"

The characteristic-zero problem in higher dimension is listed as open. [S6:37–38] records it: "The characteristic-zero problem in dimensions at least three is still listed as open in Gaifullin--Petrov's July 2026"

The stabilization belongs to the theory of residual and stable coordinates. [S6:73–79] states it: "The stabilization belongs to the theory of residual and stable coordinates. A polynomial in $\kk[p]\poly4$ is a _residual coordinate_ if its image is a polynomial coordinate over the residue field of every prime of $\kk[p]$; it is _one-stably a coordinate_ if it becomes a coordinate after adjoining one variable. Our $H$ is a residual coordinate: it is a coordinate after inverting $p$, while a linear change in $F,J$ makes its reduction at $p=0$ a coordinate."

The Stable Coordinate Conjecture is stated. [S6:84–86] states it: "The Stable Coordinate Conjecture asks whether a polynomial $f\in\kk\poly n$ that becomes a coordinate in $\kk\poly{n+1}$ after adjoining one variable must already be a coordinate in $\kk\poly n$"

The polynomial $H$ is the counterexample. [S6:92–95] states it: "The polynomial $H$ in   is not a coordinate of $P=\kk[p,s,u,F,J]$, but it is a coordinate of $P[w]$ for one independent variable $w$. Thus the Stable Coordinate Conjecture over $\kk$ fails in ambient dimension five after one stabilization."

The stabilization method is exponential. [S6:112–118] describes it: "A derivation $D$ is _locally nilpotent_ if every element is killed by some iterate of $D$; over $\kk$, its exponential is an algebraic action of the additive group $\Ga$. We make the stabilization method explicit. A locally nilpotent derivation of $P$ sends $H$ to $p^3$. Exponentiating it converts $H$ into $H+p^3w$, and a coordinate calculation identifies the resulting quotient with a polynomial ring. This exponential-shift argument follows the method of"

The affine-fibration term is defined. [S6:125–126] defines it: "An $\Aff^3$-fibration is a morphism of complex affine varieties whose base change to every geometric point of the target is affine three-space."

The Dolgachev–Weisfeiler assertion is stated. [S6:127–130] states it: "The affine-fibration assertion of Dolgachev and Weisfeiler predicts that an affine morphism to a normal locally noetherian integral base is Zariski-locally a product with affine $r$-space if every fiber is affine $r$-space over its residue field"

Both maps are smooth fibrations that are not locally trivial. [S6:138–141] states it: "Both maps are smooth $\Aff^3$-fibrations, but neither is a Zariski-locally trivial $\Aff^3$-bundle.   proves this consequence using the locally-polynomial-algebra theorem"

The main work is proving $A$ is not polynomial. [S6:145–148] states it: "The main work is to prove that $A$ itself is not polynomial. Additive actions have long served to distinguish affine varieties from affine space: Makar-Limanov used them to show that the Russell cubic is not affine three-space"

The valuation degree is defined. [S6:165–168] defines it: "The order $\ord_p$ along $p=0$ in $S$ applies to every nonzero element of $A$. Its negative defines the _valuation degree_ $\deg h=-\ord_p(h)$ and a filtration of $A$. We prove the exact"

The graded identification is an affine modification. [S6:173–179] states it: "Here $\tau$ is an indeterminate representing the initial form of $p$, and the right-hand side is generated by $R$, $\tau$, and all $i/\tau^2$ with $i\in I$. The coefficient inclusion is the one induced by $S\subset A$: the residue of $b\in S$ corresponds to its degree-zero class. This is an affine modification of $R[\tau]$ in the sense of Kaliman--Zaidenberg, and it is smooth."

The polynomial assumption yields an action. [S6:181–187] yields it: "If $A$ were polynomial, some polynomial coordinate would have positive valuation degree: otherwise all of $A$ would have nonpositive degree, contrary to $\deg F=2$. Differentiation in a different coordinate fixes that positive-degree coordinate. The exact graded identification then induces a nonzero homogeneous locally nilpotent derivation of $G$ with a nonzero homogeneous invariant of positive degree. This is the action the remaining two stages exclude."

The torus bundle principalizes $I$. [S6:190–191] states it: "The standard torus bundle from $\mathrm{SL}_2$ to the smooth affine quadric principalizes $I$ after adjoining the unchanged variable $u$."

The weights are recorded. [S6:204–207] records them: "The valuation degree is zero on $\Rt$, with $\deg\tau=-1$ and $\deg V=2$. Separately, fiber scaling gives $a,d$ weight $1$, $b,c$ weight $-1$, and $u,\tau$ weight $0$; thus $v,V$ have fiber weight $2$."

The lift is unique and homogeneous. [S6:209–216] states it: "The morphism $\Spec\Gt\to\Spec G$ is the complement of the zero section in a line bundle. Every additive action on the smooth affine base $\Spec G$ lifts uniquely to an action on this line bundle that is linear on fibers and normalized at the identity. For the homogeneous action just obtained, uniqueness makes the lift homogeneous with the same valuation degree shift, while fiber linearity preserves fiber weights. This applies even when the original action does not preserve the quadric algebra $R$."

The lift constrains the derivation. [S6:225–226] states it: "Thus the lift converts the geometric action into a constrained derivation on the explicit determinant ring."

The highest component is constrained. [S6:229–232] states it: "A highest component $E'$ for an auxiliary grading remains a nonzero locally nilpotent derivation with the same fiber weight. The grading separates the two parts of $v$ so that $(E')^2(d^2+a^2u^3)=0$. The polynomial orbit of $d^2+a^2u^3$ therefore has degree at most one."

The inequality forces a contradiction. [S6:233–236] forces it: "The Mason--Stothers polynomial $abc$ inequality and the nonsquareness of $-u^3$ in $\Frac\Rt$ force $E'$ to fix $a,d,u$. The determinant relation then forces positive fiber weight, contradicting the sign obtained in the preceding stage."

## History of the conjecture

The characteristic-zero problem in higher dimension is listed as open. [S6:37–38] records it: "The characteristic-zero problem in dimensions at least three is still listed as open in Gaifullin--Petrov's July 2026"

Additive actions have long served to distinguish affine varieties from affine space. [S6:145–148] records it: "The main work is to prove that $A$ itself is not polynomial. Additive actions have long served to distinguish affine varieties from affine space: Makar-Limanov used them to show that the Russell cubic is not affine three-space"

The organization of the proof is recorded. [S6:263–271] records it: "records the rings used in the argument.   proves the stabilization.   constructs the filtration and identifies $G$.   describes the torus bundle and proves the lifting statement.   extracts the constrained derivation on $\Rt$, and   excludes it and completes the proof of  .   derives the two nontrivial affine-space fibrations. All locally nilpotent derivations and algebraic group actions in the proof are defined over $\kk$."

## Section skeleton

- `build/main.tex` [S3]
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

The scope note states the formalized claim. [S13:9] says: "Affine-space cancellation asks whether $X\times\mathbb A^1\cong\mathbb A^{n+1}$ forces $X\cong\mathbb A^n$. The formalized result gives an explicit finite-type complex domain $A$ of Krull dimension four with $A[w]\cong\mathbb C[x_1,\ldots,x_5]$ but $A\not\cong\mathbb C[x_1,\ldots,x_4]$. Thus adjoining one variable erases a genuine algebraic distinction."

The scope note states what is not included. [S13:11] says: "The separate stable-coordinate and general line-bundle lifting consequences are not included."

The declaration is `OAI.ComplexCancellation.main` [S14:32]. The comparator stub carries `sorry` at `ComplexCancellation.lean:26` [S15:26].

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `overview.tex` | 859 | Family entry, line 170 |
| S2 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/README.md` | 18 | Manuscript title, date |
| S3 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/main.tex` | 27 | Abstract, lines 9–17 |
| S4 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/preamble.tex` | 43 | Macro definitions |
| S5 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/references.tex` | 172 | Bibliography entries |
| S6 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/01-introduction.tex` | 271 | Introduction: theorem, history, proof stages |
| S7 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/02-construction.tex` | 256 | Construction |
| S8 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/03-degeneration.tex` | 369 | Degeneration |
| S9 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/04-bundle.tex` | 412 | Bundle |
| S10 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/05-reduction.tex` | 239 | Reduction |
| S11 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/06-rigidity.tex` | 338 | Rigidity |
| S12 | `preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/07-affine-fibrations.tex` | 154 | Affine fibrations |
| S13 | `lean/docs/047.md` | 17 | Scope |
| S14 | `lean/OAI/Algebra/AffineCancellation/Main.lean` | 38 | Declaration |
| S15 | `lean/ComparatorChallenges/ComplexCancellation.lean` | 32 | Comparator stub |

## Links

- [S1](../../../overview.tex)
- [S2](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/README.md)
- [S3](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/main.tex)
- [S4](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/preamble.tex)
- [S5](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/references.tex)
- [S6](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/01-introduction.tex)
- [S7](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/02-construction.tex)
- [S8](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/03-degeneration.tex)
- [S9](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/04-bundle.tex)
- [S10](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/05-reduction.tex)
- [S11](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/06-rigidity.tex)
- [S12](../../../preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/07-affine-fibrations.tex)
- [S13](../../../lean/docs/047.md)
- [S14](../../../lean/OAI/Algebra/AffineCancellation/Main.lean)
- [S15](../../../lean/ComparatorChallenges/ComplexCancellation.lean)

## Bibliography

**26 entries** from `references.tex`:
- [AEH] S.~S. Abhyankar, W. Heinzer, and P. Eakin, \emph{On the uniqueness of the coefficient ring in a polynomial ring}, J. Alg…
- [Asanuma] T. Asanuma, \emph{Polynomial fibre rings of algebras over Noetherian rings}, Invent. Math. \textbf{87} (1987), 101--127.…
- [BassConnellWright] H. Bass, E.~H. Connell, and D.~L. Wright, \emph{Locally polynomial algebras are symmetric}, Bull. Amer. Math. Soc. \text…
- [BlancVanSanten] J. Blanc and I. van Santen, \emph{Embeddings of affine spaces into quadrics}, Trans. Amer. Math. Soc. \textbf{371} (2019…
- [Brion] M. Brion, \emph{On linearization of line bundles}, J. Math. Sci. Univ. Tokyo \textbf{22} (2015), no.~1, 113--147. \url{h…
- [DuttaLahiri] A.~K. Dutta and A. Lahiri, \emph{On residual and stable coordinates}, J. Pure Appl. Algebra \textbf{225} (2021), no.~10,…
- [EdoVenereau] E. Edo and S. V\'en\'ereau, \emph{Length $2$ variables of $A[x,y]$ and transfer}, Ann. Polon. Math. \textbf{76} (2001), …
- [ElKahouiOuali] M. El Kahoui and M. Ouali, \emph{A note on residual coordinates of polynomial rings}, J. Commut. Algebra \textbf{10} (20…
- [FinstonMaubach] D. Finston and S. Maubach, \emph{Constructing (almost) rigid rings and a UFD having infinitely generated Derksen and Mak…
- [Fujita] T. Fujita, \emph{On Zariski problem}, Proc. Japan Acad. Ser. A Math. Sci. \textbf{55} (1979), no.~3, 106--110. \url{http…
- … and 16 more
