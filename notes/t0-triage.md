# T0 triage: 137 families, 255 manuscripts, zero coverage signal

T0 is the tier with **no scope note, no comparator challenge, and no `main_results` entry** — 137
families holding 255 manuscripts. By construction every one of those manuscripts is unformalized
(the T3 set is exactly the families with at least one formalized manuscript), so T0 is where claim
shape has to carry the categorization on its own.

Regenerate the counts with `python3 notes/scripts/triage_t0.py`. Every number below is from that
run. Abstracts quoted from `overview.tex` are the release's own source-level text: "proves" in an
abstract is a claim, not a verified result.

## Buckets

First match wins, so buckets are a partition **for triage ordering only**; the `shapes` tags stay
multi-label. Ordered by how cheaply the claim can be checked, not by importance.

| Bucket | T0 families | Manuscripts | Meaning |
|---|---|---|---|
| C | 16 | 29 | counterexample — names an object that breaks a conjecture |
| R | 50 | 92 | resolution — resolves/proves/settles a named conjecture |
| B | 29 | 57 | bound — bound, sharpness, power-saving, improvement |
| K | 8 | 20 | classification — if and only if / classified / characterization |
| U | 12 | 17 | uniform — uniformity over every object in a class |
| O | 2 | 5 | density, partial, undecidability — tagged, no bucket above |
| N | 20 | 35 | no shape tag at all — title is the only signal |
| **Total** | **137** | **255** | reconciles with the T0 row count |

Bucket concentration by discipline (families with ≥2): C is Topology 5, A&CG 4, differential
geometry 3. R is A&CG 9, number theory 8, real/complex analysis 6, algebra 5, topology 5. B is
probability 5, A&CG 4, mathematical physics 4, TCS 3. N (untagged) is A&CG 5, differential geometry
4, number theory 2, probability 2, topology 2.

## The reading pass: 44 families first

Selection rule: the C bucket (16 families) ∪ the number-theory opening, family ids 001–031 (15) ∪
families with ≥3 manuscripts (22). Union: **44 families, 134 manuscripts**. The other 93 T0
families hold 121 manuscripts and were not read.

### C — counterexample (16 families, 29 manuscripts)

Each names a concrete object, which is the cheapest check in the whole tier: does the object exist
as described, and does it break the named conjecture?

- **046** (2p, A&CG) — a smooth projective complex fourfold with large π₁ whose universal cover has
  no positive-dimensional compact analytic subvariety and is neither Stein nor holomorphically
  convex; a separate surface counterexample settles dimension two.
- **053** (1p, A&CG) — a tautological relation that vanishes in rational Chow (hence cohomology)
  but lies outside Pixton's original span.
- **054** (1p, A&CG) — for every sufficiently large admissible Hassett discriminant *a*, a very
  general cubic fourfold is irrational despite an untwisted geometric K3 category and integral
  Hodge-theoretic K3 association. Qualifier in the abstract: "the discriminant threshold is
  ineffective".
- **059** (2p, diff geometry) — reduced holomorphic hypersurface germs, ambiently homeomorphic,
  with multiplicities 4 and 5 in C⁴.
- **109** (1p, TCS) — exact n-bit multiplication in deterministic worst case O(n(log n)^{1−κ}),
  κ = 2^{−182}, on one fixed finite-alphabet multitape TM; disproves Schönhage–Strassen optimality
  in the ordinary bit model.
- **209** (2p, algebra) — integral Gersten injectivity fails in degrees 3 and 5; two explicit
  2-dimensional ramified regular local rings of mixed characteristic (0,5).
- **278** (1p, math physics) — a three-electron Coulomb molecule with two equal positive-integer
  charge nuclei whose ground-state density has no noninteracting ensemble representation by one real
  spin-independent local potential in L^{3/2}+L^∞. Qualifier: "the required nuclear charge is
  specified nonnumerically".
- **285** (3p, operator algebras) — coefficient-free reduced Baum–Connes fails (rational-injectivity
  failure witnessed by a finitely generated torsion-free group, plus a separate surjectivity failure
  of assembly); a torsion-free group with nontrivial projection in the reduced C\*-algebra refutes
  Kadison–Kaplansky.
- **305** (3p, topology) — unrestricted 4-dimensional disk embedding fails; F₂ is not good
  (Freedman–Quinn); a finitely presented integral PD⁴ group with finite classifying space is not
  realizable, so Wall's manifold conjecture fails.
- **318** (5p, algebraic topology) — strong chromatic splitting fails at height 3 for p≥5; weak
  splitting fails at heights p (p≥5) and p+1 (p≥7); the overlap L_{n−1}L_{K(n)}S_p^∧ admits a
  2ⁿ-stage filtration for p>n+1. Scope clause: at height 3 and prime 3, even finite assembly fails
  in E(2)-local modules.
- **319** (1p, algebraic topology) — Hahn–Wilson refuted at height 2: for every sufficiently large
  p, a connective p-complete spectrum of exact fp-type 2 not buildable from completed BP⟨2⟩ by
  finitely many sums, shifts, cones, and retracts, while satisfying finite and telescopic
  localization comparisons.
- **320** (1p, topology) — closed aspherical topological 4-manifolds, homotopy equivalent and not
  homeomorphic, with common word-hyperbolic π₁: Borel rigidity fails in dimension 4.
- **321** (1p, topology) — a finite 3-dimensional CW complex whose universal cover has no integral
  homology above degree 2 and H³ = 0 for every local coefficient module, with no finite
  2-dimensional model: Wall's finite D(2) fails; π₁ is infinite.
- **340** (1p, A&CG) — the nearby Lagrangian conjecture fails: for some sufficiently large even N, a
  closed exact Lagrangian in T\*(S⁹×S^{N−1}) diffeomorphic to the base, not Hamiltonian isotopic to
  the zero section. Qualifier: existence, not a construction of a specific N.
- **351** (3p, diff geometry) — Ricci flow on a closed 4-manifold extends past any time with bounded
  scalar curvature; the higher-dimensional counterexample has bounded scalar curvature and unbounded
  full curvature at its finite maximal time.
- **352** (1p, diff geometry) — Chen's long-time Calabi-flow existence fails: a smooth
  U(10)-invariant Kähler metric on CP¹⁰ in the Fubini–Study class develops a finite-time singularity.

### Number-theory opening (15 of the first 31 families are T0)

The most scrutinized results in the release have the least shipped evidence.

- **001** (1p, K) — Milne rationality for abelian varieties over Q̄ with good reduction. Companion to
  032: "with 032, every specialized Hodge class is represented by one rational cycle in all
  prime-to-p and crystalline realizations".
- **002** (3p, U) — the BSD leading term for every elliptic curve over Q whose full q-power Selmer
  group has corank 0 or 1 for some q, including finiteness of Sha. With 006 it yields full BSD on a
  density-one set of quadratic twists.
- **004** (2p, R) — no algorithm for rational zeros: Hilbert's tenth over Q has a negative answer.
  The only T0 family tagged `undecidability`.
- **006** (2p, O) — Goldfeld's conjecture for quadratic twists of every elliptic curve over Q (ranks
  0 and 1 each of density 1/2, mean rank → 1/2), twists ordered by absolute value.
- **010** (3p, R) — every continuous odd absolutely irreducible 2-dimensional 2-adic G_Q
  representation unramified outside finitely many primes occurs in a completed Hecke algebra at odd
  tame level; classical modularity up to Tate twist for de Rham representations at 2 with distinct
  Hodge–Tate weights; the dyadic Fontaine–Mazur conjecture "without residual restrictions".
- **011** (3p, R) — prime-factor logarithmic laws of p−1 converge to Poisson–Dirichlet PD(1); also
  infinitely many n with more than n^{1−ε} totient preimages.
- **014** (8p, K) — restricted geometric Langlands "under the four stated Lie-theoretic
  characteristic hypotheses"; over an arbitrary algebraically closed field of characteristic p>0
  "assuming additionally that p is very good for the group and p∤|W_G|". Ramanujan is unconditional
  for split adjoint absolutely simple exceptional groups, unramified-only for split adjoint groups
  with a generic unramified component. Arthur enhancements are constructed "assuming the finite-level
  Ramanujan–Arthur decomposition". The `conditional` tag is genuine here.
- **016** (4p, R) — abelian Zilber–Pink over Q̄, plus the full curve case in the Siegel threefold A₂
  for Hodge-generic curves "without boundary or reduction assumptions".
- **018** (2p, R) — Margulis–Platonov over every global field, including characteristic 2.
- **019** (2p, N) — the p-adic section conjecture for smooth proper geometrically connected curves of
  genus ≥2 over finite extensions of Q_p; plus the Grothendieck section conjecture over Q for X₀(N)
  and X₁(N) of genus ≥2. No shape tag at all.
- **022** (1p, U) — weak inhomogeneous Duffin–Schaeffer: numerators unrestricted, no monotonicity or
  Diophantine condition on γ.
- **027** (1p, R) — resolves the determinant-one curve case of Litt's integral-density question:
  integral points Zariski dense in every SL_r character-variety component over the full ring of
  integers of one number field, quasi-unipotent representations including nonsemisimple boundary
  classes.
- **029** (2p, R) — Artin infinitude for every a≠−1 that is not a square, with ≥ c_a x/(log x)²
  primes in every large interval (x,2x).
- **030** (1p, R) — modularity for every elliptic curve over every imaginary quadratic field.
- **031** (1p, N) — Uchida's conjecture for open Galois homomorphisms, "no restriction on the kernel
  or separate cyclotomic-compatibility assumption". No shape tag.
- **032** (8p, R) — rational Hodge for every complex CM abelian variety in every dimension and
  codimension; via Milne also Tate for all abelian varieties over finite fields, plus the Hodge
  standard conjecture for abelian varieties in every characteristic. Companions: rational Hodge for
  arbitrary products of projective K3, Kuga–Satake algebraicity.

### Multi-manuscript T0 (≥3 manuscripts, 22 families)

Most exposed and least checked. 034 alone holds 14 manuscripts.

- **034** (14p, R) — log abundance in every dimension for normal compact Kähler lc pairs with
  effective rational boundary, via log Iitaka subadditivity; projective log abundance in
  characteristic 0; effective Iitaka fibration for nonnegative Kodaira dimension; resolves the
  finite-rational-coefficient index conjecture for semi-lc log Calabi–Yau pairs per fixed dimension
  and fixed finite coefficient set.
- **056** (5p, B) — termination of every existing generalized lc flip sequence on globally Weil
  Q-factorial compact Kähler fourfolds; termination of arbitrary permitted MMPs for projective lc
  fourfolds with rational boundary in characteristic 0.
- **057** (3p, O) — Campana abelianity: special compact Kähler ⇒ virtually abelian π₁; same for
  order-two root orbifolds of fourfolds along one smooth divisor "when special in the stated
  differential-line sense"; the quasi-projective case gives a virtually nilpotent image of class ≤2.
- **068** (7p, N) — smooth semipositive −K_X ⇒ H⁰(X,−mK_X) ≠ 0 for some m>0, in every dimension. No
  shape tag.
- **154** (4p, B) — almost-everywhere convergence of consecutive multiple ergodic averages of every
  finite length for invertible mixing transformations; the limit is the product of the integrals. "No
  mixing rate or standardness assumption".
- **216** (6p, N) — XY model: C_{βc}(r) ~ A r^{−1/4}(log r)^{1/8}, and the BKT law
  √(βc−β)·log ξ(β) → B; heights converge to Gaussian fields through the rough phase. Qualifier:
  "critical center-magnetization and spin-field conclusions retain their stated height,
  renormalization, and field-input assumptions". No shape tag.
- **223** (6p, B) — chordal SLE_κ limits for critical square-lattice random-cluster interfaces 0<q≤4
  with κ = 4π/arccos(−√q/2), on bounded Jordan domains for q≥1 and smooth domains for q<1, "under
  the stated marked-boundary approximations"; CLE_κ for 1≤q≤4.
- **224** (3p, B) — Cardy's formula for annealed critical Poisson–Voronoi crossings in every bounded
  Jordan quadrilateral; quenched near-critical universality.
- **232** (3p, B) — GFF limits for triangular-lattice height models (odd heights 0,±2 with two-arc
  ±1 boundary; integer Lipschitz heights weighted by a fixed x∈[1/√2,1]); the tuned interface
  converges to chordal SLE₄, matching Schramm's predictions.
- **264** (3p, N) — local strong cosmic censorship near each fixed rotating subextremal Kerr bridge:
  a dense G_δ of two-ended asymptotically flat vacuum data. "No symmetry is imposed; extensions need
  not satisfy the vacuum equations". No shape tag.
- **036** (4p, K) — numerical semiampleness for nef adjoints K_X+B+M (projective klt rational pairs
  in characteristic 0; smooth compact Kähler rational klt SNC pairs via Bott–Chern cohomology);
  separately, minimal models and Mori fiber spaces with nef b-data fixed.
- **336** (3p, B) — complete n-manifolds (n≥3) with −4Δ+Scal ≥ 1 map to a complex of dimension ≤ n−2
  with fiber diameters bounded only by n, so universal covers of closed positive-scalar-curvature
  manifolds have macroscopic dimension ≤ n−2.

The remaining multi-manuscript families in the subset — 010, 011, 014, 016, 019, 029, 032, 034, 053,
054, 059, 109, 154, 209, 278, 285, 305, 318, 319, 320, 321, 340, 351, 352 — are entered above under
their bucket.

## What the triage shows

1. **T0 is not a weakness signal.** 137 families, 255 manuscripts, zero formalized — that is the
   absence of a coverage mechanism, not evidence of a defect. 560 of 722 manuscripts are
   unformalized overall.
2. **The most scrutinized results are the least covered.** 15 of the first 31 family ids are T0,
   including Hilbert's tenth over Q (004), BSD (002), the p-adic section conjecture (019), geometric
   Langlands (014), and modularity over imaginary quadratic fields (030).
3. **The counterexample bucket is the cheapest place to start.** 16 families, 29 manuscripts,
   concentrated in topology (5), A&CG (4), and differential geometry (3). Each names an object — a
   fourfold, a spectrum, a Lagrangian, a Kähler metric, a CW complex, a local ring — so the check is
   object-level, not proof-level.
4. **The resolution bucket is the largest claim-to-evidence gap:** 50 families, 92 manuscripts, all
   asserting that a named conjecture is settled, none with a scope note, challenge, or formalized
   manuscript.
5. **Cross-family chains sit entirely inside T0.** 001 + 032: Milne rationality plus rational Hodge
   for CM abelian varieties is claimed to give the Tate conjecture for all abelian varieties over
   finite fields and the Hodge standard conjecture for abelian varieties. 002 + 006: BSD plus
   Goldfeld yields full BSD on a density-one set of quadratic twists. Both chains are unformalized
   end to end, and the README lists the Hodge-conjecture-for-CM-abelian-varieties work as an
   exception to the standard production procedure.
6. **Scope qualifiers live in abstracts, not titles.** 054's threshold is ineffective; 216's
   magnetization conclusions "retain their stated height, renormalization, and field-input
   assumptions"; 223 is "under the stated marked-boundary approximations"; 278's nuclear charge is
   "specified nonnumerically"; 340 asserts existence for "some sufficiently large even N"; 014 lists
   four Lie-theoretic hypotheses plus two extra characteristic conditions; 318's scope clause (height
   3, prime 3) is a separate sentence from its headline claims. A title-level taxonomy cannot see any
   of this.
7. **The taxonomy is silent on 20 T0 families** that carry no shape tag at all, including 019, 031,
   068, 216, 264 — marquee-grade results where the title is the only signal. 21 T0 families match
   three or more shapes (004, 014, 027, 032, 034, 037, 056, 077, 078, 166, 200, 203, 239, 265, 268,
   270, 302, 336, 351, 364, 368), which is the multi-label reality the buckets deliberately collapse.

## Reading priority for the next passes

1. The C bucket (16 families, 29 manuscripts): one object per family; record the object and the
   conjecture it breaks.
2. The number-theory opening (15 families, 36 manuscripts), starting with the chains 001↔032 and
   002↔006.
3. The multi-manuscript families (22 families, 104 manuscripts), largest first: 034, 014, 032, 068,
   216, 223.
4. The 20 untagged families — decide by reading titles, then add a tag only if it discriminates.

## Not checked

- No manuscript PDF was read. Every claim above is quoted from the release's own abstracts in
  `overview.tex`, which are source-level assertions.
- No Lean, `lake`, or comparator run. Zero `sorry` in a source tree is not a comparator pass, and T0
  families have no comparator challenge to begin with.
- Bucket assignment is keyword-driven off the `shapes` column. A reading pass can move a family, as
  the `conditional` audit did (9 tagged, 5 genuine).
- The abstracts of the other 93 T0 families (121 manuscripts) were not read.
- Whether a counterexample family's object is constructed explicitly or only proved to exist is not
  recorded in the ledger; 340 and 054 are existence claims, and the rest were not checked for that
  distinction.
