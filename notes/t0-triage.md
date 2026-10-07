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
   Repo-wide, 74 of 372 families use counterexample language in title or abstract
   ("counterexample", "disprov", "answers … negatively"); 44 carry the tag, 31 do not. Reading those
   31, 30 are genuine — the only false positive is 348, matched through "nonnegatively". In T0 the
   untagged ones are 048, 195, 201, 259, 284 (004 is a negative *resolution*, not an object). So the
   object-level check set in T0 is **21 families, not 16**, and the ledger's C bucket is a floor, not
   a census. `conditional` mislabels (9 tagged, 5 genuine); `counterexample` omits.
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

## Reading priority for the next passes

The first two passes cover all 137 T0 families at abstract level, so priority is now about what to
check, not what to read.

1. The 21 counterexample-shaped T0 families: the 16 tagged in the C bucket plus 048, 195, 201, 259,
   284. One object each; record the object and the conjecture it breaks.
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

- No manuscript PDF was read. Every claim above is quoted from the release's own abstracts in
  `overview.tex`, which are source-level assertions.
- No Lean, `lake`, or comparator run. Zero `sorry` in a source tree is not a comparator pass, and T0
  families have no comparator challenge to begin with.
- Bucket assignment is keyword-driven off the `shapes` column. A reading pass can move a family, as
  the `conditional` audit did (9 tagged, 5 genuine), and finding 9 shows it should.
- Whether a counterexample family's object is constructed explicitly or only proved to exist is not
  recorded in the ledger; 340 and 054 are existence claims, and the rest were not checked for that
  distinction.
- The second pass read abstracts, not proofs. "Proves the X conjecture" was not checked against the
  conjecture as stated in the literature, so the 45 named-conjecture families are recorded as claims.
- The 30 untagged counterexample-shaped families outside T0 were classified from abstract snippets,
  not full abstracts.
- No T0 family has been checked against `lean/docs/` for a scope note that the ledger says is absent;
  the tier assignment is taken from the generator's report.

