# 032 — The rational Hodge conjecture for CM abelian varieties (Algebraic and complex geometry, 5 manuscripts, tier T0)

## Original CONTENTS.md summary

[S1:755] (family entry):

> **Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and
> codimension.** Through Milne's theorems, this also gives the Tate conjecture for all abelian
> varieties over finite fields and the Hodge standard conjecture for abelian varieties in every
> characteristic.

[S2:142] carries the same text as the release's family abstract, and the five manuscript entries under
the family block are [S1:762], [S1:771], [S1:780], [S1:789] and [S1:798], with the abstracts quoted
below.

[The rational Hodge conjecture for CM abelian varieties](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/paper.pdf)

[S1:764] (its abstract):

> We prove the rational Hodge conjecture for complex abelian varieties with complex multiplication:
> every rational Hodge class on such a variety is a rational linear combination of algebraic cycle
> classes. As consequences, we obtain the generalized Hodge conjecture for CM abelian varieties, the
> Tate conjecture for abelian varieties over finite fields, and the Hodge standard conjecture for
> abelian varieties in arbitrary characteristic.

[Algebraic Kuga-Satake correspondences and Hodge conjectures on a K3 quadratic locus](../../../preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf)

[S1:773] (its abstract):

> We prove the rational Hodge and generalized Hodge conjectures in every cohomological degree of
> every self-power of a projective complex K3 surface whose transcendental quadratic space, with its
> cup-product form, admits a rational isometric embedding in $`\mathbb U_{\mathbb Q}^{\oplus2}\perp\langle-1\rangle^4`$.
> This includes every ample *P*-polarized K3 surface, including all Picard jumps, for
> $`P=\mathbb U\oplus D_8(-1)\oplus D_4(-1)`$. On this locus we construct algebraic correspondences
> inducing every prescribed standard even-Clifford Kuga–Satake tensor. More generally, for any
> projective complex K3 surface, algebraicity of one exact standard even-Clifford Kuga–Satake tensor
> implies both conjectures for every self-power.

[Weil classes and Hodge classes on abelian powers](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf)

[S1:782] (its abstract):

> We prove the rational Hodge conjecture in every codimension on every self-power of a complex
> abelian sixfold with an imaginary-quadratic action and a compatible polarization whose rational
> homological Hermitian form is hyperbolic of signature $`(3,3)`$. We also prove it in every
> codimension on every self-power of a complex abelian variety of dimension at most five admitting an
> imaginary-quadratic action. Both results include nonsimple varieties and special periods with
> additional endomorphisms. The proof uses the companion theorem on the rational Hodge conjecture for
> CM abelian varieties.

[Abelian covers, Gale correspondences, and the Hodge conjecture for powers](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf)

[S1:791] (its abstract):

> We prove the rational Hodge conjecture on every self-power of the Jacobian at each tensor
> Hodge-generic point of the full marked variation of a connected abelian cover of curves. This holds
> in every base genus and for every compatible branching pattern. For any CM abelian variety, the
> conclusion also holds for every self-power of its product with the Jacobian, on the same
> Hodge-generic locus. We also prove the conjecture on every self-power of a very general member of
> the full smooth labelled family of diagonal complete intersections cut out by at most two equations
> of a common degree, in every dimension and every degree at least two.

[A Conditional Reduction for Algebraic Kuga-Satake Correspondences](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/paper.pdf)

[S1:800] (its abstract):

> For a polarized K3 surface whose primitive cohomology has full orthogonal Hodge group, one algebraic
> correspondence inducing a nonzero map from that cohomology to the second cohomology of an abelian
> variety suffices to recover the prescribed full Kuga–Satake correspondence. We give an equivalent
> condition using holomorphic one-forms on a generically finite surface cover. If this input holds
> very generally in a polarized component, the prescribed correspondence is algebraic throughout that
> component, for every choice of standard data on the transcendental part. The existence of the
> initial correspondence remains a hypothesis.

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
`A^m`. *Quadratic actions in dimension at most five* [S13:88]: `dim A ≤ 5` with an imaginary-quadratic
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
"The witness cycles, abelian varieties, or surface covers need not vary in a family" [S16:60]; a
corollary lifts this to every projective K3 surface provided the hypothesis holds in the required
component in every degree [S16:63]. The genericity hypothesis is not vacuous — it holds outside a
countable union of proper closed analytic subsets in every full polarized period chart [S16:55] — and
the paper states its own limit: "Constructing a very-general correspondence or surface cover with the
stated property remains the external existence problem. The hypotheses concern actual algebraic cycles;
absolute Hodge or motivated classes do not supply this input." [S16:71]. Its dependency table makes the
contract explicit: "No algebraicity theorem for the Kuga--Satake class is an input." [S17:4–5].

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
holomorphic and antiholomorphic factors, "Pohlmann's balance criterion" [S4:83–90], citing
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
formulation (0.1) [S9:226–227], "with the correction in" Milne's own online *Addenda to Lefschetz
motives and the Tate conjecture* [S9:227–228], which MS1 states concretely: the cofinal auxiliary
Galois CM fields are enlarged to contain a real subfield of degree greater than 2 that is inert at the
residue prime [S9:228–230]. The addenda entries are cited as author's corrections on Milne's site,
consulted September 30, 2026 [S10:434–448]; the Hodge standard part cites the parallel
*Addendum to Polarizations and Grothendieck's standard conjectures* [S10:442–448]. So the release's
Tate and Hodge-standard conclusions are not a self-contained derivation from the 1999 and 2002 papers
as published — they are derived from those papers as corrected by their author.

**Antecedents of the K3 and cover lines.** MS4's "Earlier work" section [S14:162–229] names the
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

## Consequences now that the proof has been found

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
prime [S9:228–230], and then: "The theorem's hypothesis is supplied by Theorem~\ref{thm:cm}."
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
standard conclusion is stated "in arbitrary characteristic" [S9:288]. The blurb's phrasing is
therefore a faithful summary of the corollaries, and the load-bearing dependency is the one MS1
states in its own consequences section — Milne's two theorems, as corrected by their author, with
`thm:cm` supplying the hypothesis.

## Sources

Body markers name a source and, where given, the lines it cites: `[S9:226–231]` is lines 226–231
of S9, `[S9]` is the file itself. Line numbers are 1-based, as in the shipped files. File names and
links appear once, here.

Manuscript root — `preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/`
(MS1, the family's root: 12 `.tex` files under `build/`, its README naming a previous version of the
same manuscript [S11:21]). The release keeps that previous directory on disk and stops naming it in
`overview.tex`; the supersession record is [S19]. Every File cell below is the
repository-relative path, in backticks — that is the text the checker resolves — and the hrefs stay
relative to this page. S4–S11 sit under the MS1 root, S12–S14 under the other manuscript roots, S1–S2
at the repository root, S15–S17 under MS5's root, S18–S19 under `notes/`.

| # | File | Lines | Role |
|---|---|---|---|
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9,142 | the release's catalog — family entry [S1:755]; the five manuscript entries [S1:762], [S1:771], [S1:780], [S1:789], [S1:798] and their abstracts [S1:764], [S1:773], [S1:782], [S1:791], [S1:800]. Quoted word-for-word; the release's inline HTML is rendered as markdown, so its italic P tags became *P* and its PDF links were rewritten to resolve from this page |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | the release's `\resultentry` list — 032 at [S2:142] |
| S4 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/01-introduction.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/01-introduction.tex) | 227 | MS1 introduction — CM convention [S4:10–14]; `thm:cm` [S4:17–29]; consequences paragraph [S4:31–44]; Hodge's problem [S4:49–55]; Weil classes [S4:67–75]; the reductions [S4:80–112] |
| S5 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/02-tensors.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/02-tensors.tex) | 521 | MS1 tensor algebra — the balanced-tensor lemmas at [S5:34], [S5:71], [S5:268], [S5:486]; the four-factor switch [S5:303] |
| S6 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/03-surface.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/03-surface.tex) | 156 | MS1 surface criterion [S6:10] and its corollary [S6:130] |
| S7 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05a-moduli.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05a-moduli.tex) | 534 | MS1 degree-one CM extraction [S7:29] |
| S8 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05c-cm-types.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/05c-cm-types.tex) | 430 | MS1 finite-family CM extraction [S8:395] |
| S9 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/07-consequences.tex`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/sections/07-consequences.tex) | 335 | MS1 consequences — section intro [S9:4–16]; `cc:ghc` [S9:154]; `cc:tate` [S9:213] and its proof [S9:226–233]; `cc:standard` [S9:274] and its proof [S9:292–300]; the specialization remark [S9:311–335] |
| S10 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/references.bib`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/build/references.bib) | 448 | MS1 bibliography — Deligne [S10:117], André [S10:15], Abdulali [S10:1], Hazama [S10:191], Pohlmann [S10:370], Moonen–Zarhin [S10:344], Markman [S10:251], Hodge [S10:214], Milne 2022 [S10:306], the companion rationality manuscript [S10:407–413], the two Milne addenda [S10:434–448] |
| S11 | [`preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/README.md`](../../../preprints/The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026/README.md) | 21 | MS1 README — the version note [S11:21] |
| S12 | [`preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/build/paper.tex`](../../../preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/build/paper.tex) | 5,391 | MS2 — the extended criterion [S12:151–158] and its independence note [S12:160–161]; the quadratic locus [S12:163–175]; `main:theorem` [S12:179] |
| S13 | [`preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/build/paper.tex`](../../../preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/build/paper.tex) | 8,285 | MS3 — split Weil sixfolds [S13:79]; quadratic actions in dimension at most five [S13:88]; scope and polarization [S13:96–100]; the dependency on MS1 at [S13:8212] |
| S14 | [`preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/build/paper.tex`](../../../preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/build/paper.tex) | 3,779 | MS4 — powers of abelian-cover Jacobians [S14:104]; powers of diagonal complete intersections [S14:146]; earlier work [S14:162–229]; the determinant corollary [S14:1110]; `thm:gale` [S14:2817]; its MS1 and MS3 citations at [S14:3736] and [S14:3743] |
| S15 | [`preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/paper.tex`](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/paper.tex) | 46 | MS5 root — abstract [S15:31]; section includes |
| S16 | [`preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/sections/introduction.tex`](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/sections/introduction.tex) | 75 | MS5 — `main:generic` [S16:36]; `main:specialization` [S16:57]; the equivalence [S16:63]; the external existence problem [S16:71] |
| S17 | [`preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/references/dependency-table.tex`](../../../preprints/A-Conditional-Reduction-for-Algebraic-Kuga-Satake-Correspondences-September-10-2026/build/references/dependency-table.tex) | 163 | MS5 dependency contract [S17:4–5] |
| S18 | [`notes/catalog.tsv`](../../catalog.tsv) | 373 | the reading ledger — family 032 at [S18:33] (tier, manuscript count, coverage columns) |
| S19 | [`notes/sources.md`](../../sources.md) | 144 | the source-surface note — the supersession measurement [S19] |
