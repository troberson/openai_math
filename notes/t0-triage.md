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

Buckets come from `shapes` alone. The ledger's `resolves_named` column (233 families repo-wide) is a
second T0 discriminator: it flags **88 of these 137**, including 12 of the 20 in N — 019, 031, 043,
051, 060, 164, 195, 258, 306, 316, 338, 341, all named-conjecture families — so N is no longer
title-only for half its families. Cross-tab and method: `notes/resolution-tag.md`.

`counterex_broad` (74 families repo-wide) is a third: it flags **22 of these 137**, of which 16 are
the C bucket and **6 are not** — 004 (R), 048 and 201 (K), 195 (N), 259 and 284 (B). First match
never shows them as counterexamples, which is why the signal is a column and not a widened tag.
Cross-tab and method: `notes/counterexample-tag.md`.

Bucket concentration by discipline (families with ≥2): C is Topology 5, A&CG 4, differential
geometry 3. R is A&CG 9, number theory 8, real/complex analysis 6, algebra 5, topology 5. B is
probability 5, A&CG 4, mathematical physics 4, TCS 3. N (untagged) is A&CG 5, differential geometry
4, number theory 2, probability 2, topology 2.

## The reading pass: 44 families first

Selection rule: the C bucket (16 families) ∪ the number-theory opening, family ids 001–031 (15) ∪
families with ≥3 manuscripts (22). Union: **44 families, 134 manuscripts**. The other 93 T0
families hold 121 manuscripts; they are read in the second pass below.

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

## Second pass: the remaining 93 families

All T0 families not in the first pass: **93 families, 121 manuscripts**, no family holding more than
2 manuscripts (65 hold one, 28 hold two). Buckets: R 40f/52p, B 23f/33p, U 10f/13p, K 5f/7p, N
15f/16p, C 0, O 0 — every counterexample-tagged T0 family was already in the first pass. Disciplines
(families): A&CG 19, topology 10, differential geometry 10, algebra 8, real/complex analysis 7, TCS
7, probability 6, mathematical physics 6, PDE 5, combinatorics 4, operator algebras 4, convex/metric
geometry 2, dynamical systems 2, group theory 2, functional analysis 1. 45 of the 93 titles name a
conjecture, problem, or question, so most of this pass states the claim it is checking.

### R — resolution (40 families, 52 manuscripts)

- **037** (2p, A&CG) — the ordinary-double-point volume-gap conjecture: every singular complex
  algebraic klt germ of dimension n≥2 with zero boundary has normalized volume ≤ 2(n−1)ⁿ, equality
  exactly for an analytic ordinary double point.
- **041** (2p, A&CG) — strong hyperkähler SYZ: every line bundle with nonzero nef isotropic first
  Chern class on a compact irreducible holomorphic symplectic Kähler manifold is semiample; every
  projective Lagrangian fibration with normal projective base has base Pⁿ, every dimension and
  deformation type.
- **062** (1p, A&CG) — LeBrun–Salamon: closed connected positive quaternionic-Kähler manifolds of
  real dimension ≥8 are homothetic to compact symmetric Wolf spaces; plus contact-Fano homogeneity
  and the classification of projective contact manifolds of dimension ≥3 (b₂=1 adjoint varieties,
  b₂≥2 the manifold P(T\*Z)).
- **063** (1p, A&CG) — generalized Mukai: ρ(ι−1) ≤ n for a Fano n-fold, equality exactly for
  (P^{ι−1})^ρ; ι is the least anticanonical degree of a rational curve.
- **064** (1p, A&CG) — the surface case of the μ-constant problem: constant Milnor number implies
  topological right-triviality for one-parameter families of isolated hypersurface singularities in
  C³. Qualifier: after shrinking the parameter disk and representatives.
- **065** (2p, A&CG) — full ordinary unreduced descendant Virasoro conjecture for smooth complete
  intersections, every genus, curve class, and insertion; constraints pass to projectivizations of
  bundles of rank ≥2.
- **067** (1p, A&CG) — Campana–Peternell in dimension six: Fano sixfold with nef tangent bundle is
  rational homogeneous.
- **074** (2p, analysis) — Kakeya maximal conjecture in three dimensions (radius-δ tube maximal
  L³(R³)→L³(S²) with norm O_ε(δ^{−ε})) and the Hausdorff-dimension conjecture in four.
- **075** (1p, analysis) — ordinary symmetric Fourier partial sums of every L log L(T) function
  converge almost everywhere along the full sequence.
- **077** (2p, analysis) — diagonal Fourier extension conjecture for compact smooth positively
  curved surfaces in R³, including surfaces with boundary: L^p→L^p bounded for every p>3.
- **078** (1p, analysis) — three-dimensional Bochner–Riesz in its strict range, δ >
  max{3|1/p−1/2|−1/2, 0}.
- **079** (1p, analysis) — Sogge's local smoothing conjecture for the Euclidean wave equation in
  three spatial dimensions, full strict range 2<p<∞, regularity above max{0, 1−3/p}.
- **086** (1p, analysis) — the principal-value trilinear Hilbert transform with shifts x−t, x−2t,
  x−3t is bounded L³(R)³ → L¹(R): the L³ exponent case for slopes 1, 2, 3.
- **101** (1p, convex/metric) — simplices uniquely maximize the isotropic constant in every dimension;
  plus the sharp entropy lower bound for log-concave densities, equality for affine images of
  products of one-sided exponentials.
- **103** (1p, TCS) — L = RL = BPL, via an effective compiler with explicit polynomial running-time
  bounds.
- **136** (1p, TCS) — quasilinear PCP for PPAD: an End-of-Line instance of length N reduces to
  circuit constraints of total length N(log N)^{O(1)}.
- **147** (2p, dyn systems) — near-boundary Birkhoff: a smooth strictly convex planar billiard of
  positive curvature is an ellipse when a full grazing annulus is foliated by invariant essential
  curves; a continuous collar of smooth closed convex caustics also suffices.
- **166** (1p, combinatorics) — higher-dimensional Erdős distinct distances: ≥ c_d n^{2/d} distinct
  distances for n points in R^d, d≥3, matching the integer-grid order.
- **171** (1p, combinatorics) — Burr–Erdős hypercube Ramsey: the two-color Ramsey number of the
  n-cube is Θ(2ⁿ).
- **193** (1p, algebra) — strict positivity of Serre's intersection multiplicity over any regular
  local ring, including ramified mixed characteristic.
- **200** (2p, algebra) — Eisenbud–Green–Harris and lex-plus-powers over every characteristic-zero
  field, for any homogeneous ideal containing a regular sequence.
- **202** (1p, algebra) — the numerical blockwise Alperin weight conjecture, every prime and finite
  group.
- **204** (1p, algebra) — tensor saturation factor one for Spin(2n), n≥2: the type-D part of the
  simply-laced saturation conjecture.
- **208** (1p, algebra) — the finite Benson–Etingof–Ostrik conjecture: every finite symmetric tensor
  category over algebraically closed k of characteristic p>0 has a faithful exact strong symmetric
  monoidal fiber functor to Ver_{p^n}; includes characteristic two, and the level may depend on the
  category.
- **226** (1p, probability) — half-plane Temperleyan double-dimer loops converge to nested CLE₄,
  matching every macroscopic loop as an unparametrized curve.
- **268** (2p, math physics) — the spin-one Haldane gap for the pure antiferromagnetic Heisenberg
  chain on even periodic rings; companion gives a gap for odd open chains with endpoint field h=3/5
  and boundary-selected states of topological index −1.
- **270** (2p, math physics) — exactly one normalizable zero-energy state for the undeformed relative
  SU(N) BFSS model, every finite N≥2. Companion proves infinitely many normalizable positive-energy
  eigenstates for SU(2), **contradicting the original BFSS paper's exclusion of extra bound states at
  N=2** — a T0 result that disagrees with prior literature, with no coverage signal.
- **300** (2p, operator algebras) — Popa–Vaes quadratic paving: every self-adjoint element of a
  von Neumann algebra admits strong-operator paving relative to any MASA with O(ε^{−2}) blocks, the
  norm bound holding after compression by a projection arbitrarily close to the identity.
- **301** (1p, operator algebras) — classification of separable nuclear C\*-algebras after tensoring
  with the Razak–Jacelon algebra and the compacts, by cones of extended lower-semicontinuous tracial
  weights; answers Robert's trace-cone question.
- **304** (1p, topology) — Hilbert–Smith in every dimension: a locally compact second-countable
  Hausdorff group acting faithfully and jointly continuously on a connected finite-dimensional
  topological manifold is a Lie group.
- **309** (1p, topology) — the Kervaire invariant problem at p=3: classes 0, 2, 3 survive in stems
  10, 106, 322, each detection coset containing an element of exact additive order three.
- **310** (1p, topology) — Quillen's conjecture in rational homology, every finite group and prime.
- **311** (1p, topology) — Chai's invariant-ideal conjecture for Lubin–Tate deformation rings (every
  prime, positive height n), which through Barthel–Heard–Naumann proves Hovey–Strickland: dualizable
  K(n)-local spectra have exactly n+2 thick tensor ideals and a Balmer spectrum that is a chain of
  n+1 points. Cross-family chain, entirely inside T0.
- **313** (1p, topology) — every homotopy group of the K(n)-local sphere is a finitely generated
  Z_p-module; same after K(n)-localizing any finite p-local spectrum.
- **332** (1p, functional analysis) — real ℓ₁ has metric Markov cotype two (Mendel–Naor), so every
  Lipschitz map from a subset of a Hilbert space into ℓ₁ extends with universal multiplicative loss
  (Ball's extension problem for this target).
- **335** (2p, diff geometry) — Gromov's integral scalar-curvature inequality
  ∫(Scal⁻)^{n/2}dV ≥ a_n‖M‖ for closed connected oriented smooth n-manifolds, n≥3, every metric;
  plus rational inessentiality under positive scalar curvature (Gromov–Lawson) and flatness of every
  nonnegative-scalar-curvature metric on a closed aspherical manifold.
- **344** (1p, diff geometry) — metric Blaschke: injectivity radius equal to diameter implies the
  manifold is, up to scaling, a standard compact rank-one symmetric space.
- **349** (1p, diff geometry) — Solomon–Yau least volume for minimal hypersurfaces of round spheres,
  m≥2, counting covering multiplicity.
- **366** (1p, PDE) — planar Mumford–Shah interior regularity for reduced absolute minimizers with
  bounded fidelity data: the discontinuity set is locally a C^{1,α} arc, a regular crack tip, or
  three arcs meeting at 120°.
- **368** (2p, PDE) — the three-dimensional Ball–Evans approximation problem: every W^{1,p}
  homeomorphism between bounded domains in R³, 1≤p<∞, is a strong W^{1,p} limit of smooth
  diffeomorphisms onto the same target.

### B — bound (23 families, 33 manuscripts)

- **035** (2p, A&CG) — threefold log abundance in characteristic p>3: projective log canonical
  threefold pairs over algebraically closed fields, effective rational boundary, Q-Cartier adjoint
  nef of numerical dimension one, adjoint semiample. Qualifier: "without requiring the original
  variety to be terminal or Q-factorial".
- **038** (1p, A&CG) — Fujita's freeness conjecture at its sharp bound in every dimension: K_X+mL
  globally generated for every m ≥ n+1 with L ample.
- **066** (2p, A&CG) — the finite-rational-coefficient form of Shokurov's bounded-klt-complement
  conjecture for ε-lc complex Fano-type pairs with nef anti-log-canonical divisor; index bounded only
  by dimension and ε.
- **080** (2p, analysis) — Carleson's Schrödinger convergence at the sharp Sobolev endpoint:
  a.e. convergence for every f in H^{n/(2(n+1))}(Rⁿ), n≥2, including the planar H^{1/3}.
- **093** (1p, convex/metric) — dimension-free logarithmic Sobolev for centered log-concave densities
  with uniformly subgaussian linear marginals.
- **120** (1p, TCS) — randomized exact maximum matching in (n+m)^{1+o(1)} word time, success ≥ 2/3,
  bound holding on every computation path.
- **137** (1p, TCS) — one-tape simulation in O(T^{2/5} log^C(T+2)) space, improving the square-root
  exponent. Qualifiers: heads move at most one cell per step; initial contents independent of T;
  polylogarithmic-space access to contents and input symbols; simulation time unrestricted.
- **138** (2p, TCS) — uniform randomized worst-case Subset Sum in O(2^{0.49n}) word-RAM time, bound
  on every execution, success ≥ 2/3 on every input, words of O(n+b) bits.
- **203** (2p, algebra) — Donovan's conjecture: blocks with bounded defect-group order have finitely
  many Morita classes over each fixed algebraically closed field of characteristic p, plus the
  integral form over each fixed complete mixed-characteristic DVR with algebraically closed residue
  field.
- **233** (1p, probability) — joint critical Ashkin–Teller scaling limit (heights to the GFF, both
  current-cluster collections to recursive sets) throughout the critical line including the
  four-state Potts endpoint, in bounded Jordan domains with admissible lattice approximations and
  wired primal/free dual boundaries.
- **239** (2p, probability) — sharp singularity rate for symmetric random sign matrices:
  (1/2+o(1))ⁿ for uniform signs, (p²+(1−p)²+o(1))ⁿ for fixed bias p.
- **259** (1p, group theory) — a finitely generated group with two essentially free
  probability-measure-preserving actions of different costs, answering the fixed-price problem
  negatively. Tagged `bound`, and it is a counterexample in kind.
- **265** (2p, math physics) — entropy area law for unique ground states of finite-range Hamiltonians
  on arbitrary finite induced square-lattice domains, using only a uniform full-system spectral gap
  and local interaction bounds; PEPS approximations on L×L squares with polynomial bond dimension and
  error ≤ L^{−1}.
- **282** (1p, math physics) — scale symmetry implies local conformal symmetry in four-dimensional
  QFT. The `conditional` tag is genuine: "under the stated bounded-local-net and field-reconstruction
  hypotheses", plus a discrete bounded-below scaling spectrum of finite multiplicity, finite scaling
  support, and a physical local scale current. The conclusion is local Ward identities, "not a global
  conformal action on the whole net".
- **283** (1p, math physics) — constant-error Aaronson–Kuperberg unitary synthesis: a uniform
  polynomial-size quantum oracle circuit approximates every n-qubit channel to diamond-norm error
  1/2. Qualifier: the target-dependent oracle "may have an unrestricted truth table; its efficient
  classical construction is not asserted".
- **284** (1p, math physics) — R(f) = O((1+Q(f))⁴) is exponent-sharp, "disproving the conjectured
  cubic relation". Tagged `bound|partial`, and it is a counterexample in kind.
- **302** (2p, operator algebras) — Phillips–Toms: rc(C(X)⋊_h Z) = ½ mdim(X,h) for every minimal
  homeomorphism, including infinite values; zero mean dimension is equivalent to the small boundary
  property, Jiang–Su stability, and finite nuclear dimension.
- **314** (1p, topology) — the optimal chromatic Smith loss from H-fixed to G-fixed points equals the
  shortest subnormal-chain length with cyclic quotients, at every height, with finite spectra
  witnessing sharpness.
- **346** (2p, diff geometry) — the singular set of a stationary integral m-varifold has Hausdorff
  dimension ≤ m−1, sharp in every dimension and codimension; on round spheres it has zero
  m-dimensional Hausdorff measure.
- **355** (1p, diff geometry) — tangent-flow uniqueness at the first singular time for smooth compact
  embedded surfaces in R³, "without mean-convexity or a prescribed tangent model".
- **364** (2p, PDE) — derivation of the nonlinear Boltzmann equation from three-dimensional
  grand-canonical Newtonian gases throughout every regular kinetic interval with uniform Gaussian
  decay; stable finite-range radial potentials may have attractive wells and a singular repulsive
  core. Companion gives hard-sphere Gaussian fluctuations.
- **375** (1p, PDE) — De Giorgi's conjecture at its sharp dimension-eight endpoint; a stronger
  theorem classifies stable entire solutions R⁷→[−1,1] as constant wells or planar transitions
  "without an energy-growth assumption".
- **377** (1p, PDE) — uniform interior C^{1,α_d} regularity for bounded infinity-harmonic functions
  in every dimension d≥3; the exponent is not explicit.

### K — classification (5 families, 7 manuscripts)

- **048** (1p, A&CG) — a singular normal affine complex surface with free rank-two tangent sheaf,
  disproving the characteristic-zero Lipman–Zariski conjecture. Tagged only `classification`; it is a
  counterexample in kind.
- **201** (1p, algebra) — a countable characteristic-zero division ring algebraic over its center,
  generated by two elements over it, of infinite dimension over it: Kurosh's local-finiteness problem
  answered negatively. Tagged only `classification`; a counterexample in kind.
- **217** (2p, probability) — the low-temperature Sherrington–Kirkpatrick fluctuation law: for every
  β>1 the log partition function has variance asymptotic to c_β n^{1/3}, confirming the predicted
  n^{1/6} scale, with full-sequence convergence to a uniquely characterized nondegenerate law under
  exact centering and standardization.
- **286** (2p, operator algebras) — classification of finite-index bimodules between scalar-twisted
  group factors of ICC groups commensurable with property-(T) lattices over characteristic-zero local
  fields and arbitrary ICC group factors; recovers the group, scalar cocycle, and amplification scale
  up to stable equivalence.
- **339** (1p, diff geometry) — Katok's entropy rigidity: on a closed connected Riemannian manifold
  of dimension ≥3 with strictly negative sectional curvature, normalized Liouville measure maximizes
  geodesic-flow entropy if and only if the metric is locally symmetric.

### U — uniform (10 families, 13 manuscripts)

- **040** (1p, A&CG) — Bloch's conjecture for complex surfaces: p_g(S)=0 makes the Albanese map on
  integral degree-zero zero-cycles an isomorphism, combining the new p_g=q=0 theorem with
  Bloch–Kas–Lieberman.
- **044** (1p, A&CG) — the equivariant cohomological Hikita correspondence for every finite quiver,
  including loops and multiple arrows, with arbitrary dimension and framing vectors and a commuting
  flavor torus; the identification requires every semistable point to be stable and the gauge action
  to be free.
- **055** (2p, A&CG) — Toda's Gepner conjecture for every smooth quintic threefold (phase shift 2/5),
  plus numerical Bridgeland stability at every sufficiently large volume on all smooth projective
  threefolds with trivial canonical bundle.
- **069** (1p, A&CG) — unramified de Rham quantum geometric Langlands for every connected simple
  complex algebraic group on every smooth projective complex curve, at every shifted level
  c ∈ C \ Q.
- **142** (1p, TCS) — uniform deterministic factorization of degree-n polynomials over F_p in time
  polynomial in (n+1) log p, "no randomness, integer-factorization or primitive-root oracle, or GRH
  assumption".
- **153** (1p, dyn systems) — arithmetic classification of unbiased Bernoulli convolutions for every
  λ ∈ (0,1), plus singularity at reciprocals of every quartic Salem number in (1,2).
- **178** (1p, combinatorics) — deterministic construction of simple d-regular nonbipartite Ramanujan
  graphs on every sufficiently large even number of vertices, d≥3 fixed, in polynomial bit time with
  exponent depending on d.
- **219** (2p, probability) — GOE bulk universality for uniform simple random d-regular graphs, every
  fixed d≥3 including cubic, persisting under weak fixed iid diagonal disorder inside the clean
  spectral edges.
- **308** (2p, topology) — Smith–Toda complexes at every height when the prime may vary, with an
  explicit V(4) at p=1009.
- **315** (1p, topology) — the four-dimensional Singer conjecture: L²-Betti numbers of the universal
  cover of a closed connected aspherical topological four-manifold vanish outside degree two, and the
  same for finite connected aspherical integral Poincaré complexes of formal dimension four.

### N — no shape tag (15 families, 16 manuscripts)

Reading the titles settles most of them, which is what reading-priority item 4 asked for.

- **042** (1p, A&CG) — every complex K3 surface is Oka, including nonprojective ones; minimal compact
  complex surfaces of Kodaira dimension zero are Oka; class VII surfaces are Oka exactly when Hopf or
  Enoki. Shape: classification.
- **043** (1p, A&CG) — P_k = W_{2k} = W_{2k+1} on the rational cohomology of smooth coprime
  fixed-determinant trace-free Higgs moduli spaces and character varieties, composite ranks, genus
  ≥2; with the prime-rank theorems this gives fixed-determinant P=W in every coprime rank. Shape:
  resolution of a named conjecture.
- **051** (1p, A&CG) — Kobayashi's canonical-ampleness conjecture: a compact connected Kähler
  manifold with no nonconstant entire curve has ample canonical bundle and is projective. Shape:
  resolution, uniform.
- **060** (1p, A&CG) — the positive-b₂ Global Spherical Shell conjecture: every connected minimal
  compact complex surface of class VII with b₂>0 contains a global spherical shell. Shape:
  resolution, uniform.
- **141** (1p, TCS) — the existential theory of the reals lies in the counting hierarchy; ∃∀ real
  sentences are decidable at one fixed level even for polynomials given by arithmetic circuits.
  Shape: complexity containment — no bucket fits.
- **164** (1p, combinatorics) — Hindman's finite sums and products conjecture. Shape: resolution.
- **195** (1p, algebra) — a three-dimensional complete Noetherian normal local domain over C with no
  nonzero finitely generated maximal Cohen–Macaulay module, disproving the domain form of the small
  Cohen–Macaulay module conjecture. Shape: counterexample — the tag is missing.
- **225** (1p, probability) — the balanced square-lattice six-vertex height field (a=b=1, 0<c≤2)
  converges to a Gaussian free field including at c=2, variance multiplier 1/arcsin(c/2). Shape:
  scaling-limit identification — no bucket fits.
- **258** (2p, group theory) — Gersten's conjecture: a finitely generated one-relator group with no
  BS(m,n) subgroup is word-hyperbolic; every word-hyperbolic one-relator group is virtually compact
  special. Shape: resolution, uniform.
- **306** (1p, topology) — the purely cosmetic surgery conjecture for knots in S³, including the
  meridional slope. Shape: resolution, uniform.
- **316** (1p, topology) — Curtis's conjecture: the positive-degree mod-two stable Hurewicz image of
  the sphere is spanned by the Hopf-invariant-one classes η, ν, σ and the Kervaire-invariant-one
  classes that exist. Shape: resolution.
- **338** (1p, diff geometry) — Yau's uniformization conjecture: complete connected noncompact Kähler
  with strictly positive holomorphic bisectional curvature is biholomorphic to Cⁿ. Shape: resolution.
- **341** (1p, diff geometry) — Donaldson's hypersymplectic deformation conjecture in a
  cohomology-preserving form: a normalized positive triple of closed two-forms on a closed oriented
  four-manifold deforms through positive closed triples to a hyperkähler triple, preserving all three
  cohomology classes. Shape: resolution.
- **345** (1p, diff geometry) — infinitely many prime closed geodesics with distinct images for every
  smooth metric on Sⁿ (n≥2), on closed manifolds with a finite smooth spherical cover, and on every
  closed three-manifold, "without orientability or nondegeneracy restrictions". Shape: infinitude —
  no bucket fits.
- **357** (1p, diff geometry) — every regular point of a noncollapsed RCD(K,n) space, n≥2, has a
  neighborhood bi-Lipschitz to an open subset of Rⁿ, with a point-dependent finite constant. Shape:
  uniform.

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
8. **The second pass is resolution-heavy and counterexample-free:** R 40 families / 52 manuscripts,
   B 23/33, U 10/13, K 5/7, N 15/16, C 0, O 0. All 16 counterexample-tagged T0 families fell in the
   first pass, so the first pass took the whole cheap-check set the ledger can see. 45 of the 93
   titles name a conjecture, problem, or question, which pins the claim even where no evidence ships.
9. **The `counterexample` tag under-covers, and the gap is bigger than the `conditional` gap.**
   Repo-wide, **74 of 372** families use counterexample language in title or abstract and **44** carry
   the tag, so **30** are flagged without being tagged; all 30 are counterexamples in kind. The rule
   that reproduces those counts is now written down — `COUNTEREX_PHRASE` in
   `notes/scripts/build_catalog.py`, a phrase rule rather than a stem rule — and the per-family reading
   is in **`notes/counterexample-tag.md`**. It excludes three false positives found by reading the
   matched sentence: 348 ("answers … nonnegatively"), 339 ("strictly negative sectional curvature"),
   355 ("at every negative time"). In T0 the flag-only families are **004, 048, 195, 201, 259, 284**;
   004 is a negative *resolution* of Hilbert's tenth problem over **Q**, not an exhibited object. So
   the object-level check set in T0 is **21 families, not 16**, and the ledger's C bucket is a floor,
   not a census. `conditional` mislabels (9 tagged, 5 genuine); `counterexample` omits. The signal now
   ships as the `counterex_broad` column, so the C bucket keeps the reading order readers expect.
10. **Reading the untagged families mostly resolves them.** Of the 15 untagged in the second pass, 9
    resolve a conjecture named in the title (043, 051, 060, 164, 258, 306, 316, 338, 341), 1 is a
    counterexample (195), 2 are shaped but untagged (357 uniform, 042 classification), and only 3
    resist the vocabulary: 141 (complexity containment), 225 (scaling-limit identification), 345
    (infinitude of geodesics). A `resolution` tag would discriminate for 9 of them and
    `counterexample` for 195. No tag was added to the ledger — that is a change to the tagging rules
    in `notes/scripts/build_catalog.py`, and it needs the same yield check the `conditional` audit
    used.
11. **One T0 result contradicts the literature it reports on.** 270's companion proves infinitely
    many normalizable positive-energy eigenstates for the SU(2) BFSS model, which the abstract states
    contradicts the original BFSS paper's exclusion of additional bound states at N=2. Nothing in the
    release corroborates either side: no scope note, no challenge, no formalized manuscript.
12. **The `conditional` tag is clean in the second pass.** 282 is the only T0 family in it carrying
    the tag, and its hypotheses are stated in the abstract ("under the stated bounded-local-net and
    field-reconstruction hypotheses"), with the conclusion explicitly limited to local Ward
    identities. Across T0 the tag is genuine on 014 and 282.

## The counterexample check: 21 families, 34 manuscripts

Priority item 1, done at abstract level. The set is the 16 tagged C-bucket families plus the 5 that
break a named conjecture and carry no `counterexample` tag: **048, 195, 201, 259, 284**. All 21 have
**no scope note, no comparator challenge, no `main_results` entry, and no reasoning trace** — the
abstract in `overview.tex` is the whole body of evidence the release ships for them.

The `counterex_broad` column flags **6** T0 families that the tag misses: the five above plus **004**,
which is a negative *resolution* (Hilbert's tenth over **Q**) with no counterexample object exhibited,
so it stays out of this object-level set. See `notes/counterexample-tag.md`.

Mode: **E** = the abstract names a constructed object; **X** = the object is indexed by a parameter
the abstract leaves unspecified ("sufficiently large", "higher-dimensional", "nonnumerically").

| Fam | Object | Conjecture it breaks | Mode |
|---|---|---|---|
| 046 | Smooth projective complex fourfold with large π₁ whose universal cover has no positive-dimensional compact analytic subvariety and is neither Stein nor holomorphically convex; a second manuscript settles the surface case | Shafarevich holomorphic convexity, unrestricted | E |
| 048 | Singular normal affine complex surface with free rank-2 tangent sheaf | Lipman–Zariski conjecture in characteristic zero | E |
| 053 | Tautological relation on the moduli of stable pointed curves that vanishes in rational Chow, hence in cohomology, yet lies outside Pixton's span | Pixton's original completeness conjecture (Chow and rational-cohomological forms) | E |
| 054 | Very general smooth cubic fourfold that is irrational while carrying both an untwisted geometric K3 category and an integral Hodge-theoretic K3 association, for every sufficiently large admissible Hassett discriminant | Kuznetsov's rationality conjecture; sufficiency of the associated-K3 criterion | X — "the discriminant threshold is ineffective" |
| 059 | Reduced holomorphic hypersurface germs in C⁴ with isolated critical points, ambiently homeomorphic, of multiplicities 4 and 5 | Zariski's multiplicity conjecture | E |
| 109 | One fixed finite-alphabet TM with finitely many 1-D tapes multiplying n-bit integers exactly at every length in O(n(log n)^{1−κ}), κ = 2^{−182} | Schönhage–Strassen n log n optimality in the ordinary multitape bit model | E — κ is astronomically small |
| 195 | 3-dimensional complete Noetherian normal local domain over ℂ with no nonzero finitely generated maximal Cohen–Macaulay module, plus an example essentially of finite type over ℂ | Small Cohen–Macaulay module conjecture, domain form | E |
| 201 | Countable characteristic-zero division ring, algebraic over its center, 2-generated over the center, infinite-dimensional over it | Kurosh's division-ring problem (local finiteness) | E |
| 209 | Two explicit 2-dimensional ramified regular local rings of mixed characteristic (0,5) with nonzero integral K-theory classes vanishing over the fraction fields | Integral Gersten injectivity, unrestricted, in degrees 3 and 5 | E |
| 259 | Finitely generated group (rank-100 amalgam) with two essentially free pmp actions of different costs: Bernoulli action cost bounded away from 1, finite-height extensions with costs tending to 1 | Gaboriau's general fixed-price problem | E — answered negatively |
| 278 | Three-electron Coulomb molecule with two equal positive-integer-charge nuclei whose absolute ground-state density has no noninteracting ensemble representation by one real spin-independent local potential in L^{3/2}+L^∞ | Kohn–Sham ensemble representability for that potential class | X — "the required nuclear charge is specified nonnumerically" |
| 284 | Family of total Boolean functions showing R(f) = O((1+Q(f))^4) is sharp in its exponent, ruling out every smaller power | Conjectured cubic randomized–quantum query separation | X — an asymptotic family, not one function |
| 285 | Finitely generated torsion-free group witnessing failure of rational injectivity for coefficient-free reduced Baum–Connes; a separate failure of surjectivity of assembly; a torsion-free group with a nontrivial projection in its reduced group C\*-algebra | Coefficient-free reduced Baum–Connes; Kadison–Kaplansky | Mixed — E for the two named witnesses, the surjectivity witness is not named |
| 305 | Framed algebraic dual spheres that do not yield disjoint locally flat spanning disks (F₂ is not good, Freedman–Quinn); finitely presented integral PD⁴ group with finite classifying space and no closed aspherical topological 4-manifold realizing it | 4-dimensional disk-embedding conjecture, unrestricted; Wall's manifold conjecture | E |
| 318 | Strong chromatic splitting fails at height 3 for p≥5; weak splitting fails at heights p (p≥5) and p+1 (p≥7); positively, for n≥1 and p>n+1 the overlap L_{n−1}L_{K(n)}S_p^∧ admits a 2ⁿ-stage filtration | Strong and weak chromatic splitting | X — prime-indexed; at height 3 and prime 3 even finite assembly fails in E(2)-local modules |
| 319 | For every sufficiently large prime p, a connective p-complete spectrum of exact fp-type 2 not buildable from completed BP⟨2⟩ by finitely many sums, shifts, cones, and retracts, while satisfying the finite and telescopic localization comparisons | Hahn–Wilson conjecture at height 2 | E per prime, threshold unspecified |
| 320 | Closed connected aspherical topological 4-manifolds, homotopy equivalent and not homeomorphic, with common word-hyperbolic π₁ | Borel conjecture, homeomorphism-existence form, in dimension 4 | E |
| 321 | Finite connected 3-dimensional CW complex whose universal cover has no integral homology above degree 2 and whose H³ vanishes for every local coefficient module, with no finite 2-dimensional homotopy model; π₁ infinite | Wall's finite D(2) conjecture | E |
| 340 | Closed exact embedded Lagrangian in T\*(S⁹×S^{N−1}) diffeomorphic to the base, not Hamiltonian isotopic to the zero section, for some sufficiently large even N | Nearby Lagrangian conjecture, unrestricted | X — N unspecified |
| 351 | Positively, a smooth Ricci flow on a closed 4-manifold extends past any finite time with uniformly bounded scalar curvature; a higher-dimensional flow has bounded scalar curvature and unbounded full curvature at its finite maximal time | Scalar-curvature extension conjecture, unrestricted | X — counterexample dimension unspecified |
| 352 | Smooth U(10)-invariant Kähler metric on ℂP¹⁰ in the Fubini–Study class whose Calabi flow develops a finite-time singularity | Chen's smooth long-time existence conjecture for Calabi flow | E |

**Mode split: 14 E, 6 X, 1 mixed.** The X families are the ones whose abstract does not name an
object at all — 054, 319, 340 quantify over "sufficiently large", 351 leaves the dimension open, 278
leaves the nuclear charge nonnumeric, 284 is a family of functions. For those six, the abstract
records a *shape* of counterexample and the reading pass has to find the parameter.

**Only 2 of the 21 ship executable support, and both state their own limit.** 059 and 352 carry
`verification/` scripts; I ran them from temp copies, stdlib only, assertions enabled. 059:
`support/supplied_finite_rank.py` exits silently 0 and `validation/explicit_relation.py` reports
`"verification_passed": true`. 352: `certificate.py` exits 0, `arithmetic_allowances.py` prints
`"all_exact_rational_checks_pass": true`, and `tail-check.py` prints "All root, projection,
convolution, coefficient, derivative, residual, and contraction checks passed exactly." Neither
certifies its theorem — 059's report scope line: "it does not certify the topological or
lattice-theoretic parts of the proof"; 352's README: "Successful execution means the programs'
assertions hold; it does not independently verify their analytic interpretation or the full
theorem."

**059's "explicit" counterexample is explicit in form only.** Its certificate reports the
construction's ambient dimension as `4*s0+16`, where
`s0 = 4*sum_abs_e + 2*sum_e + common_tail_variable_count_per_side + 2`; the reported s0 is
1.1439…×10¹⁴³, so the ambient dimension is 4.5758…×10¹⁴³ variables. Nothing about the object is
checkable by inspection; the shipped check is the finite integer relation behind it.

**318 ships a coverage statement for support that is not in the repo.** Its
`SUPPORT-COVERAGE.md` names `support/r-ce/ce_certificate.py`, the matching `.json` and `.txt`
transcripts, `BUILDING.md`, `SUPPORT-COVERAGE.json`, and a `support/historical/r-ce/` archive. None
of those paths exist on disk or in `git ls-files`; the manuscript directory holds only `README.md`,
`SUPPORT-COVERAGE.md`, `build/`, and `paper.pdf`. The same file states "No Lean source or Lean
verification is supplied for this article." So 318 has a *documented* support bundle with zero
shipped artifacts — the only family in this set where the release's own coverage text overstates
what is present.

**259's INPUTS.md is a provenance caveat, not an input list**: "The manuscript was developed from an
intermediate source argument. The available source record does not establish that it was the final
revision of that argument."

**Depth is available offline.** All 34 manuscripts ship full LaTeX source (`build/`, 2–17 `.tex`
files each), so checking any of these objects against its proof needs no `lake`, `lean`, or
comparator run.

## The open parameters: 7 families read in manuscript source

Done 2026-10-06. This closes reading-priority item 1. **Fifteen manuscripts across seven families**
were read in their shipped LaTeX (`build/`), which every one of them ships — 15 of the 34 manuscripts
in the 21-family counterexample check. All seven are counterexample-tagged: 318 alone, 278 with
`density`, 054 and 319 with `uniform`, 351 with `bound` and `uniform`, and 285 and 340 with
`resolution`. No `lake`, `lean`, or comparator run; no PDF read; no proof checked.

Every `file:line` citation below was resolved against the shipped file by script after writing, and
four citations that did not land on the quoted text were corrected.

**Answer in one line each:** five of the seven parameters are *ineffective by design* and the source
says so; one (278) is not a threshold at all but a specific integer defined by a formula the source
calls nonnumerical; and 318's ranges are per-manuscript hypotheses, not one range.

| Fam | Parameter the abstract leaves open | What the source states | Effective? |
|---|---|---|---|
| 054 | Hassett threshold | "There is an integer \(d_0\) such that, for every admissible \(d>d_0\)…" (`introduction.tex:77`) | **No** — "The threshold \(d_0\) is ineffective" (`introduction.tex:87`) |
| 278 | nuclear charge | \(Z=2+\lceil\sup_{0<t\le1} t^{-1}\mathbf 1_{\mathcal B}(t)\rceil\) (`06-parameters.tex:268`) | **Defined, not evaluated** — "no evaluated decimal value or effective numerical upper bound for this integer is asserted" (`06-parameters.tex:7`) |
| 285 | surjectivity witness | \(G_{\mathrm{sur}}=V\rtimes\Gamma\), \(V=\F_p^{(\Gamma)}/W_0\), projection \(b_0\) with \(\tau(b_0)=\sum_{i\ge1}p^{-k_i}\notin\Q\) | **Named** — and not asserted torsion-free |
| 318 | prime range | Five manuscripts, five ranges: \(p\ge5\); \(p\ge5\) / \(p\ge7\); \(p>n+1\); \(p\ge5\); \(p=n=3\) | **Stated per claim**, sharpness declined |
| 319 | Hahn–Wilson threshold | \(M\ge81,\ p>16M^2,\ 2\lfloor M/8\rfloor>p^{1/3}\) (`operator.tex:262`) | **No** — "No particular numerical lower bound for \(p\) will be needed" |
| 340 | even \(N\) | "For some sufficiently large even integer \(N\)" (`introduction.tex:25`), \(N=2m\), \(m\ge20\) | **No** — bound on \(m\), never on \(N\) |
| 351 | flow dimension | \(q\ge10\) on \(\Sp^2\times\Sp^{q+1}\) (`01-introduction.tex:69`); source states the dimension only as \(q+3\ge4\) (`06-barriers.tex:279`) | **No** — threshold is an inequality, no minimal \(n\) |

### 054 — irrational cubic fourfolds with geometric K3 categories

The theorem is generic existence with an ineffective threshold. `cub:criterion` (`cubics.tex:12`)
proves irrationality from lattice data (\(\operatorname{rank}T_X=21\), \(d=|\det T_X|>d_0\),
\(\operatorname{End}_{\mathrm{Hdg}}(T_X\otimes\Q)=\Q\)); `cub:generic` (`cubics.tex:95`) shows that
data holds at a very general point of each \(\mathcal C_d\), outside a countable union of proper
closed algebraic subsets. Admissible discriminants are arithmetic
(`introduction.tex:50`: \(d>6\), \(d\equiv0,2\pmod6\), \(4\nmid d\), \(9\nmid d\), and
\(p\nmid d\) for every odd prime \(p\equiv2\pmod3\)), not a list.

\(d_0\) is chosen "at least as large as the uniform bound in Theorem sf:vanishing"
(`cubics.tex:29`), that bound is existential (`subfields.tex:514`), and it bottoms out at
"There is an integer \(b\), depending only on these families and on \(N\)" (`bounds.tex:166`). The
only numeric constraints in the source are \(d_0>2\) and admissibility \(d>6\). Since Russo–Staglianò
proved rationality throughout \(\mathcal C_{26}\), \(\mathcal C_{38}\) and \(\mathcal C_{42}\)
(`introduction.tex:87`), any valid \(d_0\) exceeds 42 — the source does not draw that conclusion.
Named positive subfamilies: \(d=2\cdot7^j\) and the Hilbert-square family \(d=2n^2+2n+2>d_0\).

Load-bearing caveat, verbatim (`introduction.tex:93`): "Here ``very general'' means outside a
countable union of proper closed algebraic subsets separately in each divisor \(\mathcal C_d\). This
qualification matters: Yang and Yu construct rational subloci of codimension two in the full moduli
space inside every Hassett divisor." Also: no stable-rationality assertion
(`introduction.tex:288`); the categorical, Hodge-associated, and Hilbert-square K3 surfaces "need not
be identified" (`introduction.tex:252`); Fay's quaternion obstruction vanishes throughout the range
(`introduction.tex:331`).

### 278 — a Coulomb ground state without Kohn–Sham ensemble representation

The abstract's "nuclear charge" is not a threshold. The main theorem fixes \(D=10^{200}\) and asserts
one integer \(Z\) "specified by eq:explicit-charge" (`main.tex:134`), defined at
`06-parameters.tex:268` as \(Z=2+\lceil\sup_{0<t\le1} t^{-1}\mathbf 1_{\mathcal B}(t)\rceil\) over a
set \(\mathcal B\) of bad couplings; finiteness is `lem:explicit-charge-finite` and the only derived
bound is \(Z>C_{\mathcal B}\). The source states the gap itself, twice: "The definition is
nonnumerical: no evaluated decimal value or effective numerical upper bound for this integer is
asserted" (`06-parameters.tex:7`) and "It is a nonnumerical specification, and no effective numerical
bound for the charge is asserted" (`main.tex:156`).

Mode is a **single fixed finite system**, not a family: two nuclei of charge \(Z\) at
\((0,0,\pm D/Z)\), three electrons, \(Z\) selected by the scaling \(\lambda=1/Z\)
(`01-coulomb-setup.tex:52`). The threshold form the abstract suggests exists only in a separate,
weaker theorem — "For every sufficiently large fixed \(D\), there is an integer \(Z_0(D)\) such
that, for every integer \(Z\ge Z_0(D)\)…" (`05-plane-obstruction.tex:457`), scoped to "a single real,
spin-independent noninteracting potential in \(L^{3/2}+L^\infty\)". Caveats: no restriction on
degeneracy of a putative representing ground space; "no assertion about larger classes of
distributional potentials, spin-dependent potentials, or nonlocal one-particle operators"
(`main.tex:163`). No mention of finite temperature anywhere in the source.

### 285 — the surjectivity witness is named, and it is not torsion-free

Three manuscripts, three separate counterexamples; the family abstract's "torsion-free" qualifier
attaches to two of them, not to the surjectivity result.

| Manuscript | Object | Broken claim |
|---|---|---|
| `A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity` | \(G_{\mathrm{inj}}\): f.g. torsion-free, extracted by a finite-witness argument from a Heisenberg-voltage graphical small-cancellation group, containing \(\Z^2\) | **injectivity** only: \(h=(Bi)_*[D_{T^2}]\) has infinite order in \(K_0(BG_{\mathrm{inj}})\) while its reduced analytic assembly image is zero |
| `A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture` | \(G_{\mathrm{proj}}=G_{\mathrm{base}}*\F_N\), projection \(e\) with \(0<\tau(e)<\tfrac12\) | Kadison–Kaplansky: a projection other than 0 and 1 in a reduced group C\*-algebra |
| `An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes` | **\(G_{\mathrm{sur}}=V\rtimes\Gamma\)**, \(V=\F_p^{(\Gamma)}/W_0\), \(\Gamma\) from Osajda-labelled expanders coned off; \(b_0=\mathbf 1_{\{0\}}(T)\), the spectral projection at zero of the enabled-graph operator | **surjectivity**: \([b_0]\notin\mu_0^{G_{\mathrm{sur}}}(K_0^{G_{\mathrm{sur}}}(\underline E\,G_{\mathrm{sur}}))\) |

The mechanism is a trace obstruction. Lück's theorem gives
\(\tau_G(\mu_0^G(K_0^G(\underline EG)))\subseteq\Q\) for every countable discrete group
(`introduction.tex:71`), and \(\tau_{G_{\mathrm{sur}}}(b_0)=\sum_{i\ge1}p^{-k_i}\notin\Q\)
(`trace.tex:9`); the class survives rationalization (`trace.tex:61`), so this is a surjectivity
failure, not a torsion artifact.

**The qualifier to carry:** M3's theorem says "a finitely generated discrete group", not
torsion-free; the string "torsion" does not occur anywhere in its sources, and its own definition of
\(V\) as an \(\F_p\)-vector space yields elements of order \(p\). No manuscript in the family states a
surjectivity failure for a torsion-free group as a theorem. M1's surjectivity content is hypothetical
only — "a nontrivial projection in the scalar algebra \(C_r^*(G_{\mathrm{inj}})\) would obstruct
surjectivity … Such a projection alone does not identify an assembly kernel class"
(`00_introduction.tex:129`) — and M2's is a corollary cited to BGW2016 Prop. 10.3, not derived
in-file, for \(\Gamma_{\mathrm{proj}}\) and a matrix class \([p_0]\), not for \(G_{\mathrm{proj}}\).
M1 also states it disproves the reduced formulation only ("maximal assembly detects the same class
\(h\)"), and asserts finite generation, not finite presentation or exactness.

### 318 — five manuscripts, five prime ranges, and a support bundle that is not there

| Manuscript | Range | Height |
|---|---|---|
| `A-rational-obstruction-to-strong-chromatic-splitting-at-height-three` | \(p\ge5\) | 3 |
| `Counterexamples-to-weak-chromatic-splitting…` | \(p\ge5\) (height \(p\)); \(p\ge7\) (height \(p+1\)); \(p\ge5\) for the descent-exponent theorem | \(p\), \(p+1\), \(p\) |
| `Filtered-chromatic-splitting-at-generic-primes` | \(n\ge1\), \(p>n+1\) | \(n\) |
| `The-height-three-chromatic-overlap…` | \(p\ge5\) — "the height-three case of … whose range \(p>n+1\) becomes \(p\ge5\) here" | 3 |
| `Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three` | \(p=n=3\), "Its scope is the specified prime and height" | 3 |

The bounds are hypotheses consumed in-proof, not afterthoughts: no \(p\)-torsion gives the
cohomological bound at `07-detection.tex:84` ("Since \(p-1>n\) for \(n=2,3\) and \(p\ge5\), this is
impossible"), and the weak-splitting ranges come from displayed numerical margins
\(p^2-4p+1>0\) for \(p\ge5\) and \(p(p-6)>0\) for \(p\ge7\) (`08-upper-kernels.tex:188`). Sharpness is
explicitly declined: "We make no sharpness claim for the prime bound"
(`Filtered-chromatic-splitting/01-introduction.tex:83`). No manuscript claims the height-\(p+1\) case
at \(p=5\); the source simply omits it. The general question — \(L_{n-1}L_{K(n)}S\in
\Thick\{L_0S,L_1S,L_2S\}\) for every prime and \(n\ge1\) — is posed and left open at
`Failure-of-finite-assembly/01-introduction.tex:31`.

**Support bundle: confirmed absent.** `SUPPORT-COVERAGE.md` is tracked; the artifacts it names
(`SUPPORT-COVERAGE.json`, `BUILDING.md`, `support/`, `support/r-ce/`,
`support/r-ce/ce_certificate.py|.json|.txt`, `support/historical/r-ce`) are missing on disk **and**
in `git ls-files` (18 files in that directory, the only match for `support|BUILDING|COVERAGE` being
the `.md`), with `git status --porcelain` clean — so nothing is deleted-pending or untracked. The
bundle was never in this release.

### 319 — Hahn–Wilson at height two, at primes the source refuses to bound

"For every sufficiently large prime \(p\), there is a connective \(p\)-complete spectrum \(X\) of
exact fp-type two such that … \(X\notin\Thick(\BP\langle2\rangle_p^\wedge)\). The same spectrum
satisfies \(L_2^fX\simeq L_2X\), \(L_{T(2)}X\simeq L_{K(2)}X\)" (`main.tex:114`). No prime is
exhibited anywhere in the manuscript. The operative quantitative condition is
`op:parameters` (`operator.tex:262`): \(M\ge81\), \(p>16M^2\), \(2\lfloor M/8\rfloor>p^{1/3}\),
satisfiable by taking \(M\sim p^{2/5}\), followed by "They are compatible with every earlier
large-prime hypothesis. **No particular numerical lower bound for \(p\) will be needed.**" Component
sections carry their own thresholds (\(p>5\), \(p>8\), \(p>n^2+n+2\), \(D=2(p-1)>12\)); \(M\ge81\) is
an auxiliary odd integer, not a prime.

Mode is by properties, built in the algebraic category and transferred: a cone
\(m=\cofib(a:\widehat T'\to\widehat T')\), \(Y=\bigoplus_{r=0}^{D-1}m[r]\), a homotopy pullback
\(U=Y\times_{LY}V\) in \(\mathbf D(\mathcal N)\) with \(U\notin\Thick_{\mathbf D(\mathcal N)}(T')\),
then `transfer:criterion` giving \(X_{\mathrm{sp}}=\tau_{\ge0}Z_{\mathrm{sp}}\). No attaching map, no
named finite complex. Exact fp-type two is **proved**, not assumed (`consequences.tex:31`).

Caveats that bound the claim: "This gives the asserted failure at sufficiently large primes,
**without a claim at the remaining primes**" (`consequences.tex:187`); height one is not refuted —
the height-one theorem of Lee–Pstrągowski would put \(X_{\mathrm{sp}}\) in
\(\Thick(\BP\langle1\rangle_p^\wedge)\) (`consequences.tex:37`); the Burklund–Hahn–Levy–Schlank
counterexamples "disproved the unrestricted telescope conjecture at every prime and every height at
least two … Thus those counterexamples do not supply the fp counterexample studied here"
(`main.tex:152`); and the telescope comparisons "are properties of this example; they neither assume
nor settle the general restricted telescope conjecture for fp-spectra" (`consequences.tex:188`). The
local Hovey–Strickland classification is untouched — it is "established unconditionally for every
prime and every height \(n\ge1\)" (`consequences.tex:409`).

### 340 — the nearby Lagrangian counterexample, and the \(N\) nobody fixes

"For some sufficiently large even integer \(N\), the manifold \(Q=S^9\times S^{N-1}\) admits a closed
exact smoothly embedded Lagrangian \(L\subset T^*Q\) such that \(L\) is diffeomorphic to \(Q\) and no
compactly supported Hamiltonian isotopy carries the zero section to \(L\)" (`introduction.tex:25`).
\(N=2m\) (`embedding.tex:30`); the only numeric bound in the source is on \(m\) — "for arbitrarily
large \(m\ge20\)" (`tubes.tex:203`) — so \(N\ge40\) is derivable and never stated.

Mode is an explicit **Morse family**, not a 1-form graph and not a named Weinstein model:
\(F(b,v,w)=G_b(w)-R(b)\beta(\lVert w\rVert/T)\langle v,w\rangle\) with \(R(b)=\Lambda e^{K\theta(b)}\)
(`embedding.tex:51`), whose critical locus is diffeomorphic to \(Q\) and whose Euler identity supplies
the global primitive \(F|_{\Crit(F)}=-g_b(w)\). The ambient is exactly \(T^*(S^9\times S^{N-1})\); the
exponent 9 never varies, and it is tied to the kernel class \(0\ne a\in\pi_9\T\) with \(\gamma_*a=0\)
(`tubes.tex:156`).

The obstruction is **not** Floer cohomology, a spectral invariant, or \(\pi_1\): it is the stable
smooth tube class in Waldhausen's tube fibration, contradicted by the one-critical-point proposition
(`morse.tex:5`, closed at `transport.tex:537`). Scope, verbatim (`introduction.tex:32`): "The theorem
resolves the unrestricted nearby Lagrangian conjecture negatively. Both the base and the Lagrangian in
this example are connected and simply connected." The source never defines "unrestricted" and never
lists which restricted forms it leaves untouched; predecessors it cites carry extra hypotheses
(base topology, Maslov class, spin structures) or live in \(J^1Q\).

### 351 — the dimension is an inequality, and the family is a pair of results

Manuscript A: "There are an integer \(q\ge10\), a time \(T>0\), and a smooth Ricci flow \(g(t)\) … on
the closed connected manifold \(M=\Sp^2\times\Sp^{q+1}\), with smooth initial metric, such that
\(\sup_{M\times[0,T)}|R_{g(t)}|<\infty\), \(\lim_{t\uparrow T}\max_M|\Rm_{g(t)}|=\infty\)"
(`01-introduction.tex:68`). Dimension is derived, not named: \(m=p+q\) with \(p=2\), "The dimension of
the manifold is \(m+1\)" (`02-construction.tex:21`), and the proof closes by noting the product "is
closed, connected, and has dimension \(q+3\ge4\), as required" (`06-barriers.tex:279`) — the source
writes the lower bound as 4 there, so \(\dim M\ge13\) is a consequence of the theorem's \(q\ge10\),
not a stated dimension. The operative threshold is an inequality — "choose \(q\) large enough that
\(2<d<a\), all universal thresholds above hold, and \(\mathfrak m:=(a-2)(q-1)-C\sqrt q-2a^2-1>0\)"
with \(a=5/2\) (`06-barriers.tex:23`) — and no minimal \(n\) is stated. Prose says "sufficiently high
dimension"; the caveat is explicit: "The example is in sufficiently high dimension; no dimension-four
conclusion is asserted" (`01-introduction.tex:83`).

Mode is an explicit doubly warped ansatz \(g=ds^2+\phi(s,t)^2g_{\Sp^2}+r(s,t)^2g_{\Sp^q}\) whose
existence is imported: "Stolarski's construction supplies a smooth Ricci flow up to a finite time
\(T\)…" (`02-construction.tex:26`, citing Lemma 3.12 and the proof of Theorem 1.1 of Stolarski 2019),
with the paper's own contribution being the scalar bound and the cap estimate — "We do not import a
scalar-curvature upper bound, a full-curvature bound at the cap scale, or convergence to a particular
complete cap metric" (`02-construction.tex:150`). Bounded: scalar curvature. Unbounded: the full
curvature tensor, with two-sided rate \(c(T-t)^{-2k/d_q}\le\max_M|\Rm|\le C(T-t)^{-2k/d_q}\).

The family's other two manuscripts are the positive half: B proves scalar-curvature extension on
closed **four**-manifolds ("If \(\sup_{M\times[0,T)}|R(g(t))|<\infty\), then there are
\(\varepsilon>0\) and a smooth Ricci flow \(\widetilde g(t)\) … on \(M\), \(0\le t<T+\varepsilon\)"),
with the corollary that a finite-time singularity on a closed smooth four-manifold forces
\(\limsup R=+\infty\); C is B's static input ("Path selection …" is cited in B as
`StaticTrees`, Theorem 2.2) and is **not** cited by A. So 351 is a dimension-split pair: positive in
dimension four, negative at \(q+3\ge13\), with the gap between 4 and 13 unaddressed by the family.

## Reading priority for the next passes


The first two passes cover all 137 T0 families at abstract level, so priority is now about what to
check, not what to read.

1. ~~Find the parameter the abstracts leave open in 054, 278, 318, 319, 340, 351; name the witness of
   the Baum–Connes surjectivity failure in 285; ask 318 where its `support/r-ce/` bundle went.~~
   **Done 2026-10-06** — recorded in "The open parameters: 7 families read in manuscript source"
   above. Follow-ups that the answers opened: 054's threshold must exceed 42 and the source does not
   say so; 319 makes no claim at small primes and 318 declines sharpness, so neither has a checked
   boundary; 351 leaves dimensions 5–12 open; 285's surjectivity witness is not asserted torsion-free,
   so the family abstract's qualifier does not cover it.
2. The 45 second-pass families whose titles name a conjecture — check the named conjecture against
   the stated statement, starting with the sharp-bound claims (038, 078, 079, 101, 202, 344, 346,
   375) where an off-by-one in the exponent is the whole result.
3. Cross-family chains inside T0: 001↔032, 002↔006, and 311⇒Hovey–Strickland. A chain is only as
   strong as its weakest, unformalized link.
4. The tag-yield question from finding 9: measure what a `resolution` tag would add repo-wide before
   touching `build_catalog.py`, and record the yield the way `notes/conditional.md` records it.
5. The 28 two-manuscript families of the second pass (035, 037, 041, 055, 065, 066, 074, 077, 080,
   138, 147, 200, 203, 217, 219, 239, 258, 265, 268, 270, 286, 300, 302, 308, 335, 346, 364, 368) —
   the companion manuscript is where scope limits hide.

## Not checked

- No manuscript PDF was read. The abstract-level passes quote the release's own abstracts in
  `overview.tex`, which are source-level assertions. Fifteen manuscripts across seven families (054,
  278, 285, 318, 319, 340, 351) were additionally read in the LaTeX source shipped in their
  directories, and those entries quote theorem statements and body text with file:line, every citation
  resolved against the file by script. **No proof in those fifteen was checked** — the reads establish
  what each statement says, not that its proof is correct.
- No Lean, `lake`, or comparator run. Zero `sorry` in a source tree is not a comparator pass, and T0
  families have no comparator challenge to begin with.
- Bucket assignment is keyword-driven off the `shapes` column. A reading pass can move a family, as
  the `conditional` audit did (9 tagged, 5 genuine), and finding 9 shows it should.
- Whether a counterexample family's object is constructed explicitly or only proved to exist is now
  recorded for the 21 checked families (mode column above), from abstract wording only, and confirmed
  in shipped source for 054, 278, 285, 319, 340, 351. It is still unrecorded for the
  counterexample-shaped families outside T0.
- The counterexample table records the release's own naming of each broken conjecture. None of the 21
  objects was checked against the conjecture as stated in the literature, so "breaks X" is the
  release's claim. For the seven source-read families the stated claim, its quantifier range, and its
  caveats are recorded from the manuscript body; the proofs behind them were not checked.
- The 059 and 352 scripts were run here and their assertions hold on this machine. That is a replay
  of shipped arithmetic, not a review: both files say so in their own scope lines.
- 318's `SUPPORT-COVERAGE.md` was read and the bundle it names was searched for on disk and in git.
  No other manuscript in the release ships a `SUPPORT-COVERAGE.md`, so that finding is about one
  manuscript, not a pattern.
- The second pass read abstracts, not proofs. "Proves the X conjecture" was not checked against the
  conjecture as stated in the literature, so the 45 named-conjecture families are recorded as claims.
- The 30 untagged counterexample-shaped families outside T0 were classified from abstract snippets,
  not full abstracts.
- No T0 family has been checked against `lean/docs/` for a scope note that the ledger says is absent;
  the tier assignment is taken from the generator's report.

