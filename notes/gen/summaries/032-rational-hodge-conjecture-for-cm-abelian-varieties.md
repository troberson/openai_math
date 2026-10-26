[Notes](../../README.md) / [Summaries](README.md) / [Algebraic and complex geometry](../index/disciplines/algebraic-and-complex-geometry.md) / [Family 032](../index/algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md)

# 032 — The rational Hodge conjecture for CM abelian varieties

[Index page](../index/algebraic-and-complex-geometry/032-rational-hodge-conjecture-for-cm-abelian-varieties.md)

## Original CONTENTS.md summary

 (family entry):

> **Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and codimension.** Through Milne's theorems, this also gives the Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every characteristic. [S1:755]

[S2:142] carries the same text as the release's family abstract, and the five manuscript entries under
the family block are [S1:762], [S1:771], [S1:780], [S1:789] and [S1:798], with the abstracts quoted
below.

[The rational Hodge conjecture for CM abelian varieties](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf)

 (its abstract):

> We prove the rational Hodge conjecture on every self-power of the Jacobian at each tensor Hodge-generic point of the full marked variation of a connected abelian cover of curves. This holds in every base genus and for every compatible branching pattern. For any CM abelian variety, the conclusion also holds for every self-power of its product with the Jacobian, on the same Hodge-generic locus. We also prove the conjecture on every self-power of a very general member of the full smooth labelled family of diagonal complete intersections cut out by at most two equations of a common degree, in every dimension and every degree at least two. [S1:791]

[Algebraic Kuga-Satake correspondences and Hodge conjectures on a K3 quadratic locus](../../../preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf)

 (its abstract):

> We prove the rational Hodge conjecture in every codimension on every self-power of a complex abelian sixfold with an imaginary-quadratic action and a compatible polarization whose rational homological Hermitian form is hyperbolic of signature $`(3,3)`$. We also prove it in every codimension on every self-power of a complex abelian variety of dimension at most five admitting an imaginary-quadratic action. Both results include nonsimple varieties and special periods with additional endomorphisms. The proof uses the companion theorem on the rational Hodge conjecture for CM abelian varieties. [S1:782]

[Weil classes and Hodge classes on abelian powers](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf)

 (its abstract):

> We prove the rational Hodge and generalized Hodge conjectures in every cohomological degree of every self-power of a projective complex K3 surface whose transcendental quadratic space, with its cup-product form, admits a rational isometric embedding in $`\mathbb U_{\mathbb Q}^{\oplus2}\perp\langle-1\rangle^4`$. This includes every ample *P*-polarized K3 surface, including all Picard jumps, for $`P=\mathbb U\oplus D_8(-1)\oplus D_4(-1)`$. On this locus we construct algebraic correspondences inducing every prescribed standard even-Clifford Kuga–Satake tensor. More generally, for any projective complex K3 surface, algebraicity of one exact standard even-Clifford Kuga–Satake tensor implies both conjectures for every self-power. [S1:773]

[Abelian covers, Gale correspondences, and the Hodge conjecture for powers](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf)

 (its abstract):

> We prove the rational Hodge conjecture for complex abelian varieties with complex multiplication: every rational Hodge class on such a variety is a rational linear combination of algebraic cycle classes. As consequences, we obtain the generalized Hodge conjecture for CM abelian varieties, the Tate conjecture for abelian varieties over finite fields, and the Hodge standard conjecture for abelian varieties in arbitrary characteristic. [S1:764]

[A Conditional Reduction for Algebraic Kuga-Satake Correspondences](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/paper.pdf)

 (its abstract):

> For a polarized K3 surface whose primitive cohomology has full orthogonal Hodge group, one algebraic correspondence inducing a nonzero map from that cohomology to the second cohomology of an abelian variety suffices to recover the prescribed full Kuga–Satake correspondence. We give an equivalent condition using holomorphic one-forms on a generically finite surface cover. If this input holds very generally in a polarized component, the prescribed correspondence is algebraic throughout that component, for every choice of standard data on the transcendental part. The existence of the initial correspondence remains a hypothesis. [S1:800]

## Undergraduate summary

The Hodge conjecture is a question about the cohomology of a smooth projective complex variety.
Cohomology splits into pieces indexed by pairs `(p,q)` of integers — the Hodge decomposition — and a
rational cohomology class living in the `(p,p)` piece is called a **Hodge class of codimension `p`**.
Algebraic subvarieties of codimension `p` produce such classes, so one always has a map from algebraic
cycle classes to Hodge classes. The conjecture asks whether that map is onto. The case `p = 1` is
classical and true (the Lefschetz (1,1) theorem: a `(1,1)` class is algebraic exactly when it is
integral); everything above codimension one is open in general, and abelian varieties — the projective
algebraic groups, of which elliptic curves are the dimension-one examples — are the standard testing
ground.

This family proves the conjecture for the abelian varieties with **complex multiplication** (CM):
those whose rational endomorphism algebra contains a commutative semisimple algebra of dimension
`2 dim A`, the largest such algebra an abelian variety can carry. MS1 states the result as a single
theorem: for a complex CM abelian variety, the cycle-class map from rational codimension-`p` cycle
classes to the `(p,p)` classes is surjective for every `p`, and therefore the rational Hodge
conjecture holds in every codimension on every finite product of CM abelian varieties and on every
power of such a product [S4:6–28]. CM varieties are the right place to start because their Hodge
groups are tori, so their cohomology splits into one-dimensional lines labelled by field embeddings,
and a tensor of those lines is a Hodge class exactly when it is *balanced* — every scalar conjugate
has equally many holomorphic and antiholomorphic factors [S4:83–90]. The whole difficulty is that
balance is a linear-algebra condition on periods, and algebraicity is a geometric condition on cycles.

The other four manuscripts widen the picture in two directions. MS3 proves the conjecture on powers
of abelian varieties with an **imaginary-quadratic action** — the sixfold case with a hyperbolic
polarization of signature `(3,3)`, and every dimension at most five [S13:79–100] — and MS4 proves it
for powers of Jacobians of abelian covers of curves, and for powers of very general diagonal complete
intersections [S14:104–146]. Both are strictly wider than CM, and both consume MS1: MS3 says so in
its own abstract, and MS4 quotes MS1's theorem inside a dedicated `companionresults` environment
[S14:371]. MS2 and MS5 are the K3 line: MS2 proves the Hodge and generalized Hodge conjectures for
every self-power of a K3 surface whose transcendental lattice embeds rationally and isometrically into
one fixed 8-dimensional quadratic form, by constructing the Kuga–Satake correspondence algebraically
on that locus [S12:179]; MS5 proves that MS2's hypothesis is *equivalent* to the existence of one
algebraic correspondence, and that if such a correspondence exists very generally in a polarized
component then it exists throughout it [S16:36–63]. MS5 proves no case of the conjecture: its own
abstract ends by saying the input is still a hypothesis [S15:31].

**Proof sketch (MS1, the family's root).** The theorem is reduced to tensors of embedding lines, and
the reduction is a chain of three proved steps. (1) *Four-factor switch* [S5:303]: every balanced
tensor is generated by relations involving only four labels, so it suffices to algebraize four-factor
tensors. (2) *Degree-one CM extraction* [S7:29]: a CM type can be extracted from a degree-one
construction over moduli, which supplies the auxiliary CM factors the reduction needs [S8:395]. (3)
*Surface criterion* [S6:10–130]: a nonzero mixed period is produced from theta differentials on a
surface, and the surface criterion turns such a period into an algebraic correspondence. Composing
those correspondences algebraizes the balanced tensors, which is the theorem. The consequences are
then derived, not assumed: the generalized Hodge conjecture for CM abelian varieties follows by
applying the theorem to correspondences from auxiliary CM varieties [S9:4–14, 154], and Milne's
Hodge-to-Tate and polarization theorems convert it into the Tate conjecture for all abelian varieties
over finite fields [S9:213] and the Hodge standard conjecture for abelian varieties [S9:274].

## Graduate summary

**MS1 — the CM theorem.** `thm:cm` [S4:17–29] states surjectivity of the Betti cycle-class map
`cl_B: CH^p(A)_Q → H^{2p}(A,Q) ∩ H^{p,p}(A)` for every `p ≥ 0`, for `A` a complex CM abelian variety,
and asserts the conjecture on every finite product and every power. The CM condition is
`End(A) ⊗_Z Q` containing a commutative semisimple `Q`-algebra of dimension `2 dim A`, and the paper
states explicitly that the point is included by convention [S4:10–14]. The engine is three named
results: the *Four-factor switch* [S5:303] (with support lemmas *Scalar descent* [S5:34], *Realization
in degree one* [S5:71], *Transfer of an embedding line* [S5:268], *Choice of the distinguished
embedding* [S5:486]); *Degree-one CM extraction* [S7:29] with its *Finite-family CM extraction*
corollary [S8:395]; and the *Surface criterion* [S6:10] with the *Surface criterion for complex spans*
corollary [S6:130]. The consequences section is self-contained: *Effective realization of a simple CM
Hodge structure* [S9:55] feeds the *Generalized Hodge conjecture for CM abelian varieties* [S9:154],
following Abdulali's effective-realization argument and Hazama's codimension-two reduction
[S9:7–12], and the two Milne theorems give *Tate conjecture for abelian varieties over finite fields*
[S9:213] and *Hodge standard conjecture for abelian varieties* [S9:274].

**MS3 — imaginary-quadratic actions.** Two headline theorems. *Split Weil sixfolds* [S13:79]: an
imaginary quadratic field acting on a complex abelian **sixfold** with a compatible polarization whose
rational Hermitian form is hyperbolic of signature `(3,3)` ⇒ rational HC in every codimension on every
`A^m`. *Quadratic actions in dimension at most five [S13:88]* `dim A ≤ 5` with an imaginary-quadratic
action ⇒ the same conclusion, and the paper notes that this second theorem
"requires no separately chosen compatible polarization: one is obtained by averaging any rational
Riemann form" [S13:99–100]. Both statements include nonsimple varieties and periods with additional
endomorphisms [S13:96–97], so neither is a simple-variety theorem. The engine theorems are *A
determinant criterion for all powers* [S13:558] and *Algebraicity of the hyperbolic Weil plane*
[S13:900], the latter built on a geometric seed constructed by a compact-type degeneration and a
relative Fourier–Mukai kernel [S13:2043, 2584], with a Hochschild–Atiyah trace identity [S13:3221]
closing the invariant obstruction space.

**MS4 — abelian covers and diagonal complete intersections.** *Powers of abelian-cover Jacobians*
[S14:104]: fix a connected topological abelian cover; then for every Hodge-generic parameter in the
full marked variation, every complex CM abelian variety `M`, and every `N ≥ 1`, rational HC holds in
every codimension on `(Jac(C_s) × M)^N` and on `C_s^a × M^b` for all `a, b ≥ 0`. The parameter is
chosen before the CM companion, so one Hodge-generic locus serves every `M`. *Powers of diagonal
complete intersections* [S14:146]: for `n ≥ 2`, `d ≥ 0`, `c ∈ {0,1,2}`, `m = d+c+1`, outside a
countable union of proper closed algebraic subsets of the Grassmannian locus `D_{c,m}` (proved to be
exactly the smooth locus at [S14:141]), rational HC holds in every codimension on every power of the
intersection; for `c ≤ 1`, or `d = 0`, no exceptional subset is needed. The Gale machinery is a
separate block — *Perfect Gale tensor* [S14:2817], *Gale cohomology supply* [S14:2964], *Sources in
codimension at most two* [S14:3024], *The branch map* [S14:3088].

**MS2 — the K3 quadratic locus.** One headline theorem, and it is **untitled** [S12:179]
(`label main:theorem`): if the transcendental quadratic space `(T_S, q)` of a projective complex K3
surface admits a rational isometric embedding into the fixed 8-dimensional form
`V_P = U_Q^{⊕2} ⊥ ⟨−1⟩^4` (signature `(2,6)` [S12:172]), then for any full even-Clifford realization
`H^1(A,Q) = C^+(T_S, q)`, any rational nonisotropic `w ∈ T_S` and any rational polarization `E`, there
is a cycle `Γ_S ∈ CH^2(S×A×A)_Q` acting on `T_S` exactly as the prescribed Kuga–Satake map `ι_{w,E}` —
and moreover rational HC and rational GHC hold in every degree of every self-power `S^m`. The covered
locus includes every ample `P`-polarized K3 with `P = U ⊕ D_8(−1) ⊕ D_4(−1)`, Picard jumps included
[S12:163–175]. The paper separates the conditional part from the construction: the criterion
`ext:criterion` [S12:151–158] — one cycle in `CH^2(S×A^2)_Q` inducing `j_w(v)(a) = vaw` gives both
conjectures on every self-power — is proved "independently of the concrete K3 family constructed
later" [S12:160–161].

**MS5 — the conditional reduction, and its boundary.** *Recovery at a point with full Hodge group*
[S16:36]: when `Hg(V) = SO(V,q)`, the three conditions (a nonzero cycle-induced map
`α_*: V → H^2(B,Q)`; a generically finite surface cover `f: Y → S` with nonzero pushforward of
`im[∧²H⁰(Y,Ω¹) → H⁰(Y,Ω²)]`; the prescribed full Kuga–Satake map realized) are **equivalent** — this
is a reduction, not a case of the conjecture. *Specialization in a polarized component* [S16:57]: if
condition (i) or (ii) holds very generally in a component of primitively amply polarized K3 surfaces of
degree `2d`, then every `(S,h)` in that component satisfies the cycle target, and
"The witness cycles, abelian varieties, or surface covers need not vary in a family [S16:60]" ; a
corollary lifts this to every projective K3 surface provided the hypothesis holds in the required
component in every degree [S16:63]. The genericity hypothesis is not vacuous — it holds outside a
countable union of proper closed analytic subsets in every full polarized period chart [S16:55] — and
the paper states its own limit: "Constructing a very-general correspondence or surface cover with the
stated property remains the external existence problem. The hypotheses concern actual algebraic cycles;
absolute Hodge or motivated classes do not supply this input." [S16:71]. Its dependency table makes the
contract explicit: "No algebraicity theorem for the Kuga–Satake class is an input. [S17:4–5]" .

**The family's dependency graph (measured from `bibitem` and `\cite` in the main files).** MS1 is the
root: MS3 cites it as `OpenAICM2026` (bibitem [S13:8212], used at [S13:195] — "This is the precise CM
input used in this paper." — and as `Theorem~1.1` at [S13:286]); MS4 cites it as `OpenAICM` (bibitem
[S14:3736], used at [S14:234], [S14:345], [S14:3582]) and cites MS3 as `OpenAIAbelianPowers` (bibitem
[S14:3743], used at [S14:317], [S14:380], [S14:391], [S14:396], [S14:403], [S14:442], [S14:466]). MS4
also declares a `companionresults` environment used three times [S14:371, 407, 449] to restate sibling
results inline. MS1, MS2 and MS5 cite no sibling: MS5's whole `build/` tree contains no `OpenAI*`
bibkey. So the abelian line is MS1 → {MS3, MS4} and the K3 line MS2, MS5 is parallel to it, MS5 being
the conditional companion of MS2's criterion.

**Cross-family edge.** MS1's bibliography carries one intra-release entry: `OpenAIMilneRationality2026`
= family 001's manuscript [S10:407–413], cited twice in the consequences section [S9:316, 329]. The
application is the *Specialization of Hodge classes* remark [S9:311–335]: combined with the CM
transport of that paper's Corollary 3.4, every rational Hodge class on an abelian variety over
`Qbar` with good reduction at a `p`-adic place specializes to a single rational algebraic cycle on the
special fiber, simultaneously in all prime-to-`p` realizations and in crystalline cohomology. MS1
bounds the use precisely: "It asserts algebraicity on the special fiber, not the Hodge conjecture for
arbitrary complex abelian varieties." [S9:334–335], and says the CM transport — not family 001's
independent rationality proof — is what is used, and that it is not an input to `thm:cm`.

**Formalization status.** Nothing about this family is machine-checked. The ledger row records tier T0
with 5 manuscripts, 0 formalized, 0 comparator challenges, 0 `main_results` declarations, no scope
note, no verification bundle and no reasoning trace [S18:33]. There is no Lean file, no challenge stub
and no coverage document for any of the five manuscripts, so every claim on this page is read from the
manuscript text and nothing here has been checked by a machine against a formalization.

**What the family does not prove.** MS1 proves CM only: the abelian varieties its theorem covers are
exactly those with a CM algebra of dimension `2 dim A`, and MS3/MS4 widen to imaginary-quadratic
actions and to Jacobians of abelian covers, not to arbitrary abelian varieties. MS5 proves no case of
the Hodge conjecture at all — it is an equivalence plus a specialization principle whose hypothesis is
open [S16:71]. MS2's theorem is a locus theorem: it needs a rational isometric embedding of
`(T_S, q)` into one fixed quadratic form [S12:179], and its own abstract states the general implication
separately from the locus [S1:773].

## History of the conjecture

MS1 states the shape of the problem in its introduction. The codimension-one case is the Lefschetz
`(1,1)` theorem, and "Hodge formulated the broader problem by asking for an extension of this
algebraicity criterion to higher-dimensional cycles" [S4:49–51], citing Hodge's own text at
`Hodge1952` [S10:214]. For an abelian variety the cohomology is the exterior algebra on `H^1`, and
"this description of its cohomology does not make every Hodge class a linear combination of divisor
products" [S4:53–55] — the gap the paper has to fill.

**Weil classes are the standing obstruction.** An imaginary quadratic action on a `2n`-dimensional
abelian variety, with the two embeddings occurring equally in `H^{1,0}`, produces a two-dimensional
rational space of `(n,n)` classes from `Λ_K^{2n} H^1(A,Q)` [S4:58–64]; the general CM-field version is
`Deligne1982`, Proposition 4.4 [S10:117]. Their Hodge type is formal; their algebraicity is the
question, and "Weil classes need not lie in the algebra generated by divisor classes; this occurs
already on abelian fourfolds" [S4:67–68], citing `MoonenZarhin1999`, Theorem 0.1 [S10:344]. The recent
antecedent MS1 names is Markman's secant work: algebraicity of the Weil classes on polarized abelian
sixfolds of Weil type for an imaginary quadratic field with polarization discriminant `-1`, from which
the Hodge conjecture for all abelian fourfolds follows [S4:69–73], citing `Markman2025Secant`,
Theorem 1.5.1 and Corollary 1.6.1 [S10:251]. MS1 locates its own theorem against that result: the
sixfold theorem needs an imaginary quadratic action, not the full CM condition [S4:74–75] — which is
exactly the direction MS3 later takes, proving the sixfold case from an imaginary-quadratic action with
a hyperbolic `(3,3)` polarization [S13:79] rather than from CM.

**Absolute Hodge classes and the balance criterion.** Deligne proved every Hodge class on an abelian
variety is absolute Hodge (`Deligne1982`, Main Theorem 2.11 [S10:117]), and MS1 is explicit about what
that buys: "This establishes an arithmetic compatibility shared by algebraic cycle classes, but does not
by itself produce algebraic cycles." [S4:80–82]. The CM case is where the criterion becomes
computable — Hodge groups are tori, `H^1` splits into embedding lines after extending coefficients, and
a line tensor is a rational Hodge class exactly when every scalar conjugate has equally many
holomorphic and antiholomorphic factors, "Pohlmann's balance criterion [S4:88]" [S4:83–90], citing
`Pohlmann1968` [S10:370], `Milne2022` §1.2(c) [S10:306] and `GaoUllmo2026`, Theorem 3.1 [S10:151].

**Two reductions the literature had already supplied, and what they leave open.** The Deligne–André
route reduces CM Hodge classes to Weil-type classes on auxiliary CM varieties; in the formulation at
`Milne2022`, Theorem 1, attributed there to André, a CM Hodge class is a sum of pullbacks of *split*
Weil classes [S4:92–98] — split meaning the Hermitian polarization form has a totally isotropic
subspace of half its dimension. MS1's reading of that reduction: "This reduction identifies classes
whose algebraicity would suffice; it does not supply their algebraic representatives in all
dimensions." [S4:98–100]. The four-label route is Hazama's arrangement method, whose rational balance
kernel is spanned by antipodal pairs and four-label square relations (`Hazama2003CM`, Theorem 7.13,
with the codimension-two algebraicity reduction at Corollary 7.14.1 [S4:102–106], [S10:191]), and Gao–
Ullmo's equivalent quadratic indicator relations [S4:106–109]. The distinction MS1 draws is the whole
difference between this family and the prior literature: "Their conclusion concerns relations among
periods. Our task is to construct algebraic representatives for the corresponding four-factor tensors
and to compose those representatives as correspondences." [S4:110–112].

**The arithmetic consequences have a documented dependency, including a correction.** MS1's Tate
corollary is derived from Milne's `Milne1999Tate` (Compositio Math. 117 (1999) 45–76) Theorem 7.1 and
formulation (0.1) [S9:226–227], "with the correction in [S9:227]" Milne's own online *Addenda to Lefschetz
motives and the Tate conjecture* [S9:227–228], which MS1 states concretely: the cofinal auxiliary
Galois CM fields are enlarged to contain a real subfield of degree greater than 2 that is inert at the
residue prime [S9:228–230]. The addenda entries are cited as author's corrections on Milne's site,
consulted September 30, 2026 [S10:434–448]; the Hodge standard part cites the parallel
*Addendum to Polarizations and Grothendieck's standard conjectures* [S10:442–448]. So the release's
Tate and Hodge-standard conclusions are not a self-contained derivation from the 1999 and 2002 papers
as published — they are derived from those papers as corrected by their author.

**Antecedents of the K3 and cover lines.** MS4's "Earlier work [S14:162]" section [S14:162–229] names the
literature its theorem sits in: Schoen's phase-kernel/permutation-quotient correspondence
(`Theorem~2.0`), Shioda–Katsura's Fermat domination, Deligne–Mostow (1986) on monodromy of
hypergeometric families, Rohde (2009, `Theorem~5.1.1`) on cyclic covers with full special-unitary
monodromy, Moonen (2010, `Proposition~4.7`), Griffiths (1968, `Theorem~1.27`) on the Kodaira–Spencer
period differential, Landesman–Litt–Sawin (2025, `Theorem~1.3`) identifying connected monodromy as the
derived group of the symplectic centralizer, and André (1992, `Section~4, Lemma~4`). MS2's introduction
names the constructions it improves on: Van Geemen's Proposition 6.3 for the full even-Clifford
Kuga–Satake realization, Paranjape's curve-product and Prym construction for six-line double planes,
Bolognesi–Laterveer (Theorem 4.4 and §6) for order-three non-symplectic automorphisms, and
Floccari–Fu on the gap between an algebraic embedding and the prescribed Kuga–Satake map.

**Prior (my training data, not this repo).** Before this release, the rational Hodge conjecture for CM
abelian varieties in codimension greater than one was, to my knowledge, open in general; the known
cases were codimension one (Lefschetz), the Weil-type sixfold/fourfold line (including Markman's
2025 announcement), and products of low-dimensional cases. Milne's 1999 paper reduced the Tate
conjecture for abelian varieties over finite fields to the Hodge conjecture for CM abelian varieties,
and his 2002 paper reduced the Hodge standard conjecture for abelian varieties to polarizations of CM
Hodge classes, so the release's "this also gives the Tate conjecture" framing is a *known reduction*
whose hypothesis is what MS1 supplies — the arithmetic conclusions are conditional on the CM theorem by
construction, not a second independent proof. The K3 Kuga–Satake program (the algebraicity of the
Kuga–Satake correspondence implying the Hodge conjecture for the surface) is long-standing, with the
special-hyperkähler cases known; MS2's locus theorem and MS5's equivalence sit inside that program.
This paragraph is my training-data prior, not a fact supplied by this repository.

## Consequences

MS1 has a consequences section, and it is a **consumer** of the CM theorem rather than a second
proof. Its opening sentence states the mechanism: "Theorem~\ref{thm:cm} applies to products of CM
abelian varieties and therefore algebraizes rational Hodge correspondences between them." [S9:4–5]
Everything after that line is a corollary of a theorem someone else proved, with MS1 supplying the
hypothesis.

**Generalized Hodge conjecture for CM abelian varieties** [S9:154]: for a complex CM abelian
variety `A`, a rational Hodge substructure `W ⊂ H^k(A, ℚ)` whose twist `W(r)` is effective is
killed by the restriction `H^k(A, ℚ) → H^k(A \ Z, ℚ)` for some closed algebraic `Z` of codimension
at least `r`; the corollary explicitly includes "every finite product of CM abelian varieties and
every power of such a product" [S9:164–165]. MS1 follows Abdulali's effective-realization argument
(citing its Lemma 1 and Theorems 3–4) and notes that "Hazama had earlier reduced this implication
to codimension-two Hodge classes on a special family of CM abelian varieties" [S9:9–11].

**Tate conjecture for abelian varieties over finite fields** [S9:213]: for every abelian variety over
a finite field, every `r ≥ 0` and every `ℓ` away from the characteristic, the cycle-class map into the
`G_q`-invariant `ℓ`-adic classes is surjective, and numerical and `ℓ`-adic homological equivalence
coincide on rational cycles [S9:221–222]. The proof is a sentence of dependency — "Apply Milne's
Theorem~7.1 and his formulation (0.1)" [S9:226] — citing `Milne1999Tate` [S10:263] "with the
correction in" the addenda entry [S9:227], whose content is that the cofinal auxiliary Galois CM
fields are enlarged to contain a real subfield of degree greater than 2 that is inert at the residue
prime [S9:228–230], and then: "The theorem's hypothesis is supplied by Theorem  . [S9:230–231]"
[S9:230–231]

**Hodge standard conjecture for abelian varieties** [S9:274]: for an abelian variety `A/K` of
dimension `g`, numerical and `ℓ`-adic homological equivalence coincide, and for every rational ample
divisor class `h` and every `0 ≤ r ≤ g/2` the form `(x, y) ↦ (-1)^r deg(xy h^{g-2r})` on `P_h^r(A)` is
positive definite over `ℝ`; MS1's own closing clause is "for abelian varieties in arbitrary
characteristic" [S9:288]. Its proof applies Milne's Theorem 3.3 from the 2002 polarizations paper
[S10:290], read "with the author's addendum \cite{cc:Milne2002Addendum} and the corrected
auxiliary-field choice from \cite{cc:Milne1999Addenda}" [S9:295–297].

**Specialized Hodge classes in good reduction**, and the family's one cross-family edge. The last
item is a remark [S9:311–335] that cites two corollaries of the companion Milne rationality
manuscript — `[Corollary~3.4]` at [S9:316] and `[Corollary~6.4]` at [S9:329], the entry being
`OpenAIMilneRationality2026` in MS1's bibliography [S10:407–413] — and transports a Hodge class on
a good-reduction abelian variety to a CM special fiber where `thm:cm` applies. MS1 bounds the
result itself: "It asserts algebraicity on the special fiber, not the Hodge conjecture for
arbitrary complex abelian varieties." [S9:334–335] That is the whole of family 032's dependence on
family 001, and it runs one way: MS1 uses that manuscript's corollaries, and nothing in `thm:cm`
depends on them.

**Consequences inside the family.** MS3's two theorems are consequences for powers of varieties
with an imaginary-quadratic action: the split sixfold case [S13:79] and "Quadratic actions in
dimension at most five" [S13:88], the second of which "requires no separately chosen compatible
polarization: one is obtained by averaging any rational Riemann form" [S13:99–100]. MS4's are its
two headline theorems — powers of abelian-cover Jacobians at Hodge-generic points [S14:104] and
powers of diagonal complete intersections [S14:146] — plus the determinant corollary at
[S14:1110]. MS2's consequence is the implication form of its criterion: algebraicity of one exact
standard even-Clifford Kuga–Satake tensor implies both conjectures for every self-power of the
surface [S12:179]. MS5's is the conditional chain — its generic theorem [S16:36] feeding its
specialization corollary [S16:57] — with the existence problem left open on its own statement
[S16:71].

**What the release claims, and what MS1 claims.** The blurb says the CM theorem "also gives the
Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for
abelian varieties in every characteristic" [S1:755]. MS1's statements match that scope: its Tate
corollary is quantified over every abelian variety over a finite field [S9:215], and its Hodge
standard conclusion is stated "in arbitrary characteristic [S9:288]" . The blurb's phrasing is
therefore a faithful summary of the corollaries, and the load-bearing dependency is the one MS1
states in its own consequences section — Milne's two theorems, as corrected by their author, with
`thm:cm` supplying the hypothesis.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:755]; the five manuscript entries [S1:762], [S1:771], [S1:780], [S1:789], [S1:798] and their abstracts [S1:764], [S1:773], [S1:782], [S1:791], [S1:800]. Quoted word-for-word; the release's inline HTML is rendered as markdown, so its italic P tags became *P* and its PDF links were rewritten to resolve from this page |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | the release's `\resultentry` list — 032 at [S2:142] |
| S4 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/01-introduction.tex) | 227 | MS1 introduction — CM convention [S4:10–14]; `thm:cm` [S4:17–29]; consequences paragraph [S4:31–44]; Hodge's problem [S4:49–55]; Weil classes [S4:67–75]; the reductions [S4:80–112] |
| S5 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/02-tensors.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/02-tensors.tex) | 521 | MS1 tensor algebra — the balanced-tensor lemmas at [S5:34], [S5:71], [S5:268], [S5:486]; the four-factor switch [S5:303] |
| S6 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/03-surface.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/03-surface.tex) | 156 | MS1 surface criterion [S6:10] and its corollary [S6:130] |
| S7 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05a-moduli.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05a-moduli.tex) | 534 | MS1 degree-one CM extraction [S7:29] |
| S8 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05c-cm-types.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05c-cm-types.tex) | 430 | MS1 finite-family CM extraction [S8:395] |
| S9 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/07-consequences.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/07-consequences.tex) | 335 | MS1 consequences — section intro [S9:4–16]; `cc:ghc` [S9:154]; `cc:tate` [S9:213] and its proof [S9:226–233]; `cc:standard` [S9:274] and its proof [S9:292–300]; the specialization remark [S9:311–335] |
| S10 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/references.bib`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/references.bib) | 448 | MS1 bibliography — Deligne [S10:117], André [S10:15], Abdulali [S10:1], Hazama [S10:191], Pohlmann [S10:370], Moonen–Zarhin [S10:344], Markman [S10:251], Hodge [S10:214], Milne 2022 [S10:306], the companion rationality manuscript [S10:407–413], the two Milne addenda [S10:434–448] |
| S11 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/README.md`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/README.md) | 21 | MS1 README — the version note [S11:21] |
| S12 | [`preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/build/paper.tex`](../../../preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/build/paper.tex) | 5391 | MS2 — the extended criterion [S12:151–158] and its independence note [S12:160–161]; the quadratic locus [S12:163–175]; `main:theorem` [S12:179] |
| S13 | [`preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/build/paper.tex`](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/build/paper.tex) | 8285 | MS3 — split Weil sixfolds [S13:79]; quadratic actions in dimension at most five [S13:88]; scope and polarization [S13:96–100]; the dependency on MS1 at [S13:8212] |
| S14 | [`preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/build/paper.tex`](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/build/paper.tex) | 3779 | MS4 — powers of abelian-cover Jacobians [S14:104]; powers of diagonal complete intersections [S14:146]; earlier work [S14:162–229]; the determinant corollary [S14:1110]; `thm:gale` [S14:2817]; its MS1 and MS3 citations at [S14:3736] and [S14:3743] |
| S15 | [`preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/paper.tex`](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/paper.tex) | 46 | MS5 root — abstract [S15:31]; section includes |
| S16 | [`preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/sections/introduction.tex`](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/sections/introduction.tex) | 75 | MS5 — `main:generic` [S16:36]; `main:specialization` [S16:57]; the equivalence [S16:63]; the external existence problem [S16:71] |
| S17 | [`preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/references/dependency-table.tex`](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/references/dependency-table.tex) | 163 | MS5 dependency contract [S17:4–5] |
| S18 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 373 | the reading ledger — family 032 at [S18:33] (tier, manuscript count, coverage columns) |
| S19 | [`notes/gen/reports/sources.md`](../../../notes/gen/reports/sources.md) | 144 | the source-surface note — the supersession measurement [S19] |

## Bibliography

- Abdulali, Salman, Hodge structures of CM-type (2005)
- Y. André, _Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part_, Compositio Mathematica **82** (1992), no. 1, 1–24.
- N. Aoki, _A note on complete intersections of Fermat type_, Commentarii Mathematici Universitatis Sancti Pauli **35** (1986), 231–245. Institutional record.
- N. Aoki, _Some new algebraic cycles on Fermat varieties_, Journal of the Mathematical Society of Japan **39** (1987), 385–396. doi:10.2969/jmsj/03930385.
- Arapura, Donu, _Motivation for Hodge cycles_, Advances in Mathematics **207** (2006), no. 2, 762–781. Cited locators follow arXiv:math/0501348v3 (16 December 2005). doi:10.1016/j.aim.2006.01.005;  .
- Artin, Michael, _Algebraic construction of Brieskorn's resolutions_, Journal of Algebra **29** (1974), no. 2, 330–348. doi:10.1016/0021-8693(74)90102-1.
- M. Artin, On the solutions of analytic equations, _Inventiones Mathematicae_ **5** (1968), 277–291.
- The Stacks Project Authors, The Stacks Project (2026)
- The Stacks Project Authors, _The Stacks project_, https://stacks.math.columbia.edu. The cited tag and theorem locators were consulted on 30 September 2026.
- P. Baum, W. Fulton, and R. MacPherson, Riemann–Roch for singular varieties, _Publications Mathématiques de l'IHÉS_ **45** (1975), 101–145.
- Bergeron, Nicolas, Millson, John, Mœglin, Colette, The Hodge conjecture and arithmetic quotients of complex balls (2016)
- Bhatt, Bhargav, Morrow, Matthew, Scholze, Peter, Integral $p$-adic Hodge theory (2018)
- Birkenhake, Christina; Lange, Herbert, _Complex Abelian Varieties_, second edition, Grundlehren der mathematischen Wissenschaften **302**, Springer-Verlag, 2004. doi:10.1007/978-3-662-06307-1.
- Bolognesi, Michele; Laterveer, Robert, _A 9-dimensional family of K3 surfaces with finite-dimensional motive_, Rendiconti del Circolo Matematico di Palermo, Series 2 **73** (2024), 2313–2331. Cited locators follow arXiv:2310.11981v2 (16 April 2024). doi:10.1007/s12215-024-01036-0;  .
- Borade, Neelima, Franzel, Jonas, Girsch, Johannes and Yao, Wei, Yu, Qiyao, Zelingher, Elad, On tori periods of Weil representations of unitary groups (2025)
- Borel, Armand, Harish-Chandra, Arithmetic subgroups of algebraic groups (1962)
- Bosch, Siegfried, Lectures on Formal and Rigid Geometry (2014)
- Bosch, Siegfried, Lütkebohmert, Werner, Raynaud, Michel, Néron Models (1990)
- Boucksom, Sébastien; Demailly, Jean-Pierre; Păun, Mihai; Peternell, Thomas, _The pseudo-effective cone of a compact {Kähler} manifold and varieties of negative Kodaira dimension_, Journal of Algebraic Geometry **22** (2013), no. 2, 201–248. Cited locators follow arXiv:math/0405285v1. doi:10.1090/S1056-3911-2012-00574-8;  .
- Brieskorn, Egbert, _Die Auflösung der rationalen Singularitäten holomorpher Abbildungen_, Mathematische Annalen **178** (1968), 255–270. doi:10.1007/BF01352140.
- Brinon, Olivier, Conrad, Brian, CMI Summer School Notes on $p$-adic Hodge Theory (2009)
- Buskin, Nikolay, _Every rational Hodge isometry between two K3 surfaces is algebraic_, Journal für die reine und angewandte Mathematik **755** (2019), 127–150. Cited locators follow arXiv:1510.02852v3. doi:10.1515/crelle-2017-0027;  .
- D. Calaque, C. A. Rossi, and M. Van den Bergh, C\ualdăraru's conjecture and Tsygan's formality, _Annals of Mathematics_ (2) **176** (2012), no. 2, 865–923.
- de Cataldo, Mark Andrea A.; Migliorini, Luca, _The Chow groups and the motive of the Hilbert scheme of points on a surface_, Journal of Algebra **251** (2002), no. 2, 824–848. doi:10.1006/jabr.2001.9105.
- E. Cattani, P. Deligne, and A. Kaplan, _On the locus of Hodge classes_, preprint arXiv:alg-geom/9402009v1, 10 February 1994, preprint PDF. Published in Journal of the American Mathematical Society **8** (1995), 483–506. doi:10.1090/S0894-0347-1995-1273413-2.
- C.-L. Chai, _Compactification of Siegel Moduli Schemes_, London Mathematical Society Lecture Note Series, vol. 107, Cambridge University Press, Cambridge, 1985.
- A. Căldăraru, The Mukai pairing—II: the Hochschild–Kostant–Rosenberg isomorphism, _Advances in Mathematics_ **194** (2005), 34–66.
- Deligne, Pierre, Hodge cycles on abelian varieties (1982)
- Deligne, Pierre, _Théorie de Hodge, II_, Publications Mathématiques de l'IHÉS **40** (1971), 5–57. doi:10.1007/BF02684692.
- Deligne, Pierre, _La conjecture de Weil pour les surfaces K3_, Inventiones Mathematicae **15** (1972), 206–226. doi:10.1007/BF01404126.
- Deligne, Pierre, _Théorie de Hodge, III_, Publications Mathématiques de l'IHÉS **44** (1974), 5–77. doi:10.1007/BF02685881.
- Deligne, Pierre; Milne, James S., _Tannakian Categories_, in _Hodge Cycles, Motives, and Shimura Varieties_, Lecture Notes in Mathematics **900**, Springer, 1982, 101–228. Cited locators follow the corrected author version of 15 August 2012, which retains the original numbering. doi:10.1007/978-3-540-38955-2\_4;  .
- P. Deligne, Théor\`eme de Lefschetz et crit\`eres de dégénérescence de suites spectrales, _Publications Mathématiques de l'IHÉS_ **35** (1968), 107–126.
- P. Deligne, Le lemme de Gabber, _Astérisque_ **127** (1985), 131–150.
- P. Deligne, _Théorie de Hodge, III_, Publications Mathématiques de l'IHÉS **44** (1974), 5–77.
- Demailly, Jean-Pierre, _Complex Analytic and Differential Geometry_, 2012 version. Chapter II, Section 8.2, Theorem 8.8.  .
- Donagi, Ron, _The fibers of the Prym map_, arXiv:alg-geom/9206008v2, 23 June 1992.  .
- Edixhoven, Bas, van der Geer, Gerard, Moonen, Ben, Abelian Varieties: Chapter XI, Polarizations and Weil pairings (2011)
- P. Etingof, _Lie groups and Lie algebras_, arXiv:2201.09397v4 (2024). Section locators refer to this version.
- P. Etingof, _Lie groups and Lie algebras_, arXiv:2201.09397v4 (2024). Section locators refer to this version.
- R.-O. Buchweitz and H. Flenner, A semiregularity map for modules and applications to deformations, _Compositio Mathematica_ **137** (2003), no. 2, 135–210.
- R.-O. Buchweitz and H. Flenner, The global decomposition theorem for Hochschild (co-)homology of singular spaces via the Atiyah–Chern character, _Advances in Mathematics_ **217** (2008), 243–281. Numbered locators refer to arXiv:math/0606730v1.
- Floccari, Salvatore; Fu, Lie, _The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties_, Journal de Mathématiques Pures et Appliquées **210** (2026), Article 103876. Cited locators follow the author-hosted version. doi:10.1016/j.matpur.2026.103876;  .
- S. Floccari, K3 surfaces associated with varieties of generalized Kummer type, _Geometry & Topology_ **30** (2026), no. 3, 1129–1154. Theorem locators refer to arXiv:2501.02315v2.
- Folland, Gerald B., A Course in Abstract Harmonic Analysis (2015)
- S. Floccari and L. Fu, The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties, _Journal de Mathématiques Pures et Appliquées_ **210** (2026), article 103876. Theorem locators refer to arXiv:2504.13607v2.
- Fulton, William, _Intersection Theory_, second edition, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3. Folge **2**, Springer-Verlag, 1998. doi:10.1007/978-1-4612-1700-8.
- Gao, Ziyang, Ullmo, Emmanuel, Hodge cycles and quadratic relations between holomorphic periods on CM abelian varieties (2026)
- van Geemen, Bert, _Kuga–Satake varieties and the Hodge conjecture_, in _The Arithmetic and Geometry of Algebraic Cycles_, B. B. Gordon et al. (eds.), Kluwer Academic Publishers, 2000, 51–82. Cited locators follow arXiv:math/9903146v1 (24 March 1999).  .
- van Geemen, Bert, _Real multiplication on K3 surfaces and Kuga–Satake varieties_, Michigan Mathematical Journal **56** (2008), no. 2, 375–399. Cited locators follow arXiv:math/0609839v1. doi:10.1307/mmj/1224783519;  .
- van Geemen, Bert; Verra, Alessandro, _Quaternionic Pryms and Hodge classes_, Topology **42** (2003), no. 1, 35–53. Cited locators follow the author-hosted arXiv:math/0103111v1 (17 March 2001). doi:10.1016/S0040-9383(02)00004-6;  .
- B. van Geemen, An introduction to the Hodge conjecture for abelian varieties, in _Algebraic Cycles and Hodge Theory_ (Torino, 1993), Lecture Notes in Mathematics 1594, Springer, 1994, 233–252. Lemma and section locators refer to the author version.
- V. Golyshev, V. Lunts, and D. Orlov, Mirror symmetry for abelian varieties, _Journal of Algebraic Geometry_ **10** (2001), no. 3, 433–496; version used: arXiv:math/9812003v2.
- G. González-Diez, R. A. Hidalgo, and M. Leyton, _Generalized Fermat curves_, Journal of Algebra **321** (2009), 1643–1660. doi:10.1016/j.jalgebra.2009.01.002; author proof.
- Grauert, Hans, _Ein Theorem der analytischen Garbentheorie und die {Modulräume} komplexer Strukturen_, Publications Mathématiques de l'IHÉS **5** (1960), 5–64. doi:10.1007/BF02684746.
- H. Grauert, Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen, _Publications Mathématiques de l'IHÉS_ **5** (1960), 5–64.
- P. A. Griffiths, _Periods of integrals on algebraic manifolds, II: Local study of the period mapping_, American Journal of Mathematics **90** (1968), no. 3, 805–865.
- Gross, Benedict H., On the Satake isomorphism (1998)
- Grothendieck, Alexander, Hodge's general conjecture is false for trivial reasons (1969)
- Grothendieck, Alexander, _Techniques de construction et théor{\`e}mes d'existence en géométrie algébrique IV: les schémas de Hilbert_, Séminaire Bourbaki, 1960/61, Exposé 221, 249–276.  . See also the 1962 erratum, which does not change the statement of Theorem 3.2:  .
- A. Grothendieck, Techniques de construction et théor\`emes d'existence en géométrie algébrique IV: les schémas de Hilbert, _Séminaire Bourbaki_, 1960/61, exposé 221, vol. 6 (1961), 249–276.
- Hazama, Fumio, On the General Hodge Conjecture for Abelian Varieties of CM-type (2003)
- Hellmann, Eugen, On families of weakly admissible filtered $\varphi$-modules and the adjoint quotient of $\mathrm{GL}_d$ (2011)
- R. A. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez, and P. Paramantzoglou, _Automorphisms of generalized Fermat curves_, Journal of Pure and Applied Algebra **221** (2017), 2312–2337. doi:10.1016/j.jpaa.2016.12.011; preprint arXiv:1409.3063.
- F. Hirzebruch, Arithmetic genera and the theorem of Riemann–Roch for algebraic varieties, _Proc. Natl. Acad. Sci. USA_ **40** (1954), 110–114. doi:10.1073/pnas.40.2.110.
- Hodge, W. V. D., The topological invariants of algebraic varieties (1952)
- S. Huang, A note on a question of Markman, _Journal of Pure and Applied Algebra_ **225** (2021), no. 9, article 106673. arXiv:2011.10207v3.
- Huybrechts, Daniel, _Lectures on K3 Surfaces_, Cambridge Studies in Advanced Mathematics **158**, Cambridge University Press, 2016. Cited locators follow the 2015 prepublication copy; the published book incorporates further corrections. doi:10.1017/CBO9781316594193;  .
- T. Shioda and T. Katsura, _On Fermat varieties_, Tohoku Mathematical Journal, Second Series **31** (1979), 97–115. doi:10.2748/tmj/1178229881.
- K. Kodaira, On a differential-geometric method in the theory of analytic stacks, _Proc. Natl. Acad. Sci. USA_ **39** (1953), 1268–1273. doi:10.1073/pnas.39.12.1268.
- Kraft, Hanspeter; Procesi, Claudio, _Classical Invariant Theory: A Primer_, preliminary version, July 1996.  .
- Kudla, Stephen S., Splitting metaplectic covers of dual reductive pairs (1994)
- Kudla, Stephen S., Millson, John J., Intersection numbers of cycles on locally symmetric spaces and Fourier coefficients of holomorphic modular forms in several complex variables (1990)
- Kuga, Michio; Satake, Ichiro, _Abelian varieties attached to polarized K3-surfaces_, Mathematische Annalen **169** (1967), 239–242. doi:10.1007/BF01399540.
- A. Landesman, D. Litt, and W. Sawin, _Big monodromy for higher Prym representations_, Geometry & Topology **29** (2025), no. 5, 2733–2782. Theorem locators refer to arXiv:2401.13906v2.
- Lehrer, Gustav I.; Zhang, Ruibin, _Invariants of the special orthogonal group and an enhanced Brauer category_, L'Enseignement Mathématique **63** (2017), no. 1–2, 181–200. Cited locators follow arXiv:1612.03998v1 (13 December 2016). doi:10.4171/LEM/63-1/2-6;  .
- Li, Li, _Chow motive of Fulton–MacPherson configuration spaces and wonderful compactifications_, Michigan Mathematical Journal **58** (2009), no. 2, 565–598. Cited locators follow arXiv:math/0611459v2 (1 January 2009).  .
- Möller, Martin, Zagier, Don, Modular embeddings of {Teichmüller} curves (2016)
- Bülles, Tim-Henrik, _Motives of moduli spaces on K3 surfaces and of special cubic fourfolds_, Manuscripta Mathematica **161** (2020), no. 1–2, 109–124. Cited locators follow arXiv:1806.08284v1 (21 June 2018). doi:10.1007/s00229-018-1086-0;  .
- Di Lorenzo, Andrea; Fringuelli, Roberto; Vistoli, Angelo, _Integral Picard group of moduli of polarized K3 surfaces_, Bulletin of the London Mathematical Society **56** (2024), no. 2, 833–846. Cited locators follow arXiv:2305.07574v2 (3 November 2023). doi:10.1112/blms.12968;  .
- B. Farb and D. Margalit, _A Primer on Mapping Class Groups_, Princeton Mathematical Series 49, Princeton University Press, 2012.
- Markman, Eyal, Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds (2025)
- E. Markman, _Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds_, arXiv:2502.03415v2 (2025). Theorem locators refer to this version.
- E. Markman, Secant sheaves and Weil classes on abelian varieties, in _Proceedings of the International Congress of Mathematicians 2026_, vol. 3, S. Friedlander and Y. Tschinkel (eds.), SIAM, 2026, 586–602.
- Milne, J. S., Lefschetz Motives and the Tate Conjecture (1999)
- Milne, J. S., Abelian Varieties (1986)
- Milne, J. S., Polarizations and Grothendieck's standard conjectures (2002)
- Milne, J. S., Hodge classes on abelian varieties (2022)
- Milne, J. S., Introduction to Shimura varieties (2005)
- Milne, J. S., Addenda to Lefschetz motives and the Tate conjecture
- Milne, J. S., Addendum to Polarizations and Grothendieck's standard conjectures
- J. S. Milne, _Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field_, Cambridge Studies in Advanced Mathematics 170, Cambridge University Press, 2017. Theorem locators refer to the corrected online version (2022).
- Milnor, John W.; Stasheff, James D., _Characteristic Classes_, Annals of Mathematics Studies **76**, Princeton University Press, 1974.
- J. Milnor, _Morse Theory_, Annals of Mathematics Studies 51, Princeton University Press, 1963. Public scan.
- Moonen, Ben, Zarhin, Yuri G., Hodge classes on abelian varieties of low dimension (1999)
- B. Moonen, _Special subvarieties arising from families of cyclic covers of the projective line_, Documenta Mathematica **15** (2010), 793–819. doi:10.4171/DM/314. Locators refer to arXiv:1006.3400v2 (2010).
- P. Deligne and G. D. Mostow, _Monodromy of hypergeometric functions and non-lattice integral monodromy_, Publications Mathématiques de l'IHÉS **63** (1986), 5–89.
- S. Mukai, Duality between $D(X)$ and $D(\widehat X)$ with its application to Picard sheaves, _Nagoya Math. J._ **81** (1981), 153–175. doi:10.1017/S002776300001922X.
- Mumford, David, Fogarty, John, Geometric Invariant Theory (1982)
- Mumford, David, _Tata Lectures on Theta I_, Progress in Mathematics **28**, Birkhäuser Boston, 1983. doi:10.1007/978-1-4899-2843-6.
- C.-L. Chai and F. Oort, Moduli of abelian varieties and $p$-divisible groups, in _Arithmetic Geometry_, H. Darmon, D. A. Ellwood, B. Hassett, and Y. Tschinkel (eds.), Clay Mathematics Proceedings 8, American Mathematical Society, 2009, 441–536.
- OpenAI, Milne's rationality conjecture for abelian varieties (2026)
- OpenAI, _The rational Hodge conjecture for CM abelian varieties_, OpenAI Math Release preprint OAI:The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026, 2026.
- OpenAI, _The rational Hodge conjecture for CM abelian varieties_, OpenAI Math Release preprint OAI:The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026, 2026.
- OpenAI, _Weil classes and Hodge classes on abelian powers_, OpenAI Math Release preprint OAI:Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026, 2026.
- I. Dolgachev and D. Ortland, _Point sets in projective spaces and theta functions_, Astérisque **165**, Société mathématique de France, 1988. Numdam record.
- J. Coelho and M. Pacini, _Abel maps for curves of compact type_, arXiv:0904.0039v1 (2009).
- Paranjape, Kapil, _Abelian varieties associated to certain K3 surfaces_, Compositio Mathematica **68** (1988), no. 1, 11–22.  .
- Peters, Chris; Sterk, Hans, _Symmetric and Quadratic Forms, with Applications to Coding Theory, Algebraic Geometry and Topology_, author-hosted draft, version label ``JUNE 2024,'' dated 16 September 2024.  .
- Pohlmann, Henry, Algebraic cycles on abelian varieties of complex multiplication type (1968)
- Poon, Flora, _Kuga–Satake construction on families of K3 surfaces of Picard rank 14_, Mathematische Nachrichten **299** (2026), no. 8, 1894–1916. doi:10.1002/mana.70173.
- D. Eisenbud and S. Popescu, _The projective geometry of the Gale transform_, Journal of Algebra **230** (2000), 127–173. doi:10.1006/jabr.1999.7940; preprint arXiv:math/9807127.
- G. Pourcin, Théor\`eme de Douady au-dessus de $S$, _Annali della Scuola Normale Superiore di Pisa, Scienze Fisiche e Matematiche_, Serie 3, **23** (1969), no. 3, 451–459.
- Schnürer, Olaf M.; Soergel, Wolfgang, _Proper base change for separated locally proper maps_, Rendiconti del Seminario Matematico della Universit{\`a} di Padova **135** (2016), 223–250. Cited locators follow arXiv:1404.7630v2 (5 November 2014). doi:10.4171/RSMUP/135-13;  .
- Rieß, Ulrike, _On the Chow ring of birational irreducible symplectic varieties_, Manuscripta Mathematica **145** (2014), no. 3–4, 473–501. Cited locators follow arXiv:1304.4404v2 (11 September 2014). doi:10.1007/s00229-014-0698-2;  .
- J. C. Rohde, _Cyclic coverings, Calabi–Yau manifolds and complex multiplication_, Lecture Notes in Mathematics **1975**, Springer, Berlin, 2009. The preprint locator refers to arXiv:0711.2195v4 (2008).
- Saito, Morihiko, _Introduction to mixed Hodge modules_, Astérisque **179–180** (1989), 145–162.  .
- Saito, Morihiko, _Mixed Hodge complexes on algebraic varieties_, Mathematische Annalen **316** (2000), no. 2, 283–331. Cited locators follow arXiv:math/9906088v1 (13 June 1999). doi:10.1007/s002080050014;  .
- C. Schoen, Hodge classes on self-products of a variety with an automorphism, _Compositio Mathematica_ **65** (1988), no. 1, 3–32.
- C. Schoen, Addendum to: Hodge classes on self-products of a variety with an automorphism, _Compositio Mathematica_ **114** (1998), no. 3, 329–336.
- C. Schoen, _Hodge classes on self-products of a variety with an automorphism_, Compositio Mathematica **65** (1988), 3–32. Original article.
- Scholze, Peter, $p$-adic Hodge theory for rigid-analytic varieties (2013)
- Scholze, Peter, $p$-adic Hodge theory for rigid-analytic varieties—corrigendum (2016)
- A. Schrijver, Tensor subalgebras and first fundamental theorems in invariant theory, _Journal of Algebra_ **319** (2008), no. 3, 1305–1319. The section locator refers to the author version.
- Serre, Jean-Pierre, _Géométrie algébrique et géométrie analytique_, Annales de l'Institut Fourier **6** (1956), 1–42. doi:10.5802/aif.59.
- A. Borel and J.-P. Serre, Le théor\`eme de Riemann–Roch, _Bulletin de la Société Mathématique de France_ **86** (1958), 97–136.
- J.-P. Serre, Un théor\`eme de dualité, _Commentarii Mathematici Helvetici_ **29** (1955), 9–26.
- J.-P. Serre, Géométrie algébrique et géométrie analytique, _Annales de l'Institut Fourier_ **6** (1956), 1–42.
- J.-P. Serre, Groupes algébriques associés aux modules de Hodge–Tate, _Astérisque_ **65** (1979), 155–188.
- C. Peters and H. Sterk, _Symmetric and Quadratic Forms, with Applications to Coding Theory, Algebraic Geometry and Topology_, author monograph draft, version June 2024, dated 16 September 2024. The corollary locator refers to this version.
- T. Terasoma, _Complete intersections of hypersurfaces—the Fermat case and the quadric case_, Japanese Journal of Mathematics, New Series **14** (1988), 309–384. doi:10.4099/math1924.14.309.
- Varesco, Mauro, _Hodge similarities, algebraic classes, and Kuga–Satake varieties_, Mathematische Zeitschrift **305** (2023), Article 69. Cited locators follow arXiv:2304.02519v3 (2 November 2023). doi:10.1007/s00209-023-03390-8;  .
- Varesco, Mauro, _The Hodge conjecture for powers of K3 surfaces of Picard number 16_, Michigan Mathematical Journal **75** (2025), no. 5, 1085–1116. Cited locators follow arXiv:2203.09778v3 (13 May 2024). doi:10.1307/mmj/20236349;  .
- Weil, André, Sur certains groupes d'opérateurs unitaires (1964)
- A. Weil, Abelian varieties and the Hodge ring, in _Collected Papers_, vol. III, Springer-Verlag, New York, 1979, 421–429 (essay 1977c).
- A. Căldăraru and S. Willerton, The Mukai pairing, I: a categorical approach, _New York Journal of Mathematics_ **16** (2010), 61–98. arXiv:0707.2052.
- Włodarczyk, Jarosław, _Simple Hironaka resolution in characteristic zero_, Journal of the American Mathematical Society **18** (2005), no. 4, 779–822. doi:10.1090/S0894-0347-05-00493-5.
- Zarhin, Yuri G., _Hodge groups of K3 surfaces_, Journal für die reine und angewandte Mathematik **341** (1983), 193–220. doi:10.1515/crll.1983.341.193.
- B. J. J. Moonen and Yu. G. Zarhin, Hodge classes on abelian varieties of low dimension, _Mathematische Annalen_ **315** (1999), no. 4, 711–733. Theorem locators refer to arXiv:math/9901113v2.
- G. I. Lehrer and R. B. Zhang, The Brauer category and invariant theory, _Journal of the European Mathematical Society_ **17** (2015), no. 9, 2311–2351.
- G. I. Lehrer and R. B. Zhang, Invariants of the special orthogonal group and an enhanced Brauer category, _L'Enseignement Mathématique_ **63** (2017), nos. 1–2, 181–200.
- André, Yves, Une remarque {\`a} propos des cycles de Hodge de type CM (1992)
- André, Yves, _Pour une théorie inconditionnelle des motifs_, Publications Mathématiques de l'IHÉS **83** (1996), 5–49. doi:10.1007/BF02698643.
