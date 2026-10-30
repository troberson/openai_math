# Family summary pages

310 extended summaries, one per family, each built from the manuscript's own LaTeX and
verified by script. The pages are rendered by `build_summaries.py` from a hand-edited data
file and the page skeleton; the checker measures the rendered bytes and writes nothing.

## Coverage, as four layers

The release's own formalization surface is four separate counts, and one percentage over them says
nothing. The numbers are the ledger's, quoted with the rule that yields each:

| Layer | Count | What the count is |
| --- | --- | --- |
| Formalized manuscripts | **175** of **721** listed manuscript directories | The per-manuscript formalized flag, counting only listed manuscripts. |
| Scope notes | **245** of **373** families | `lean/docs/NNN.md`, each with a `## Scope` section. |
| Comparator challenges | **418** distinct configs | `lean/ComparatorChallenges/*.lean` files, each a challenge **stub** with a `sorry` body. |
| `main_results` entries | **191** entries over reaching **138** of 373 families | `lean/formalization.yaml`'s `main_results:` list. |

The summaries are a fifth layer: **310** of **373** families have a page.

## The pages

- [001](001-milnes-rationality-conjecture.md) — Milne's rationality conjecture
- [002](002-full-birch-swinnerton-dyer-formula-in-selmer-coranks-zero-and-one.md) — The full Birch–Swinnerton-Dyer formula in Selmer coranks zero and one
- [003](003-quasi-riemann-hypothesis.md) — The quasi-Riemann hypothesis
- [004](004-hilberts-tenth-problem-over-q.md) — Hilbert's tenth problem over $`\mathbb Q`$
- [005](005-irrationality-of-catalans-constant.md) — Irrationality of Catalan's constant
- [006](006-goldfelds-conjecture.md) — Goldfeld's conjecture
- [007](007-two-point-chowla-and-the-corrected-binary-elliott-conjecture.md) — Two-point Chowla and the corrected binary Elliott conjecture
- [008](008-deligne-drinfeld-conjecture.md) — The Deligne–Drinfeld conjecture
- [009](009-bogomolov-pop-and-milnor-k-theoretic-reconstruction.md) — Bogomolov–Pop and Milnor $`K`$-theoretic reconstruction
- [010](010-fontaine-mazur-modularity-at-the-prime-2-and-2-adic-pro-modularity.md) — Fontaine–Mazur modularity at the prime $`2`$ and $`2`$-adic pro-modularity
- [011](011-ford-konyagin-luca-conjecture-on-prime-predecessors.md) — The Ford–Konyagin–Luca conjecture on prime predecessors
- [012](012-independent-largest-prime-factors-of-consecutive-integers.md) — Independent largest prime factors of consecutive integers
- [013](013-ostmanns-inverse-goldbach-conjecture.md) — Ostmann's inverse Goldbach conjecture
- [014](014-restricted-geometric-langlands-generic-ramanujan-and-arthur-parameters.md) — Restricted geometric Langlands, generic Ramanujan and Arthur parameters
- [015](015-torus-packet-equidistribution-in-prime-quartic-and-sextic-degrees.md) — Torus-packet equidistribution in prime, quartic, and sextic degrees
- [016](016-zilber-pink-in-abelian-varieties-and-the-siegel-threefold.md) — Zilber–Pink in abelian varieties and the Siegel threefold
- [017](017-irrationality-exponent-of-is-2.md) — The irrationality exponent of $`\pi`$ is $`2`$
- [018](018-margulis-platonov-conjecture-over-global-fields.md) — The Margulis–Platonov conjecture over global fields
- [019](019-p-adic-section-conjecture.md) — The $`p`$-adic section conjecture
- [020](020-squarefree-quartics-and-power-free-polynomial-values.md) — Squarefree quartics and power-free polynomial values
- [021](021-a-quadratic-bound-for-jacobsthals-function.md) — A quadratic bound for Jacobsthal's function
- [022](022-weak-inhomogeneous-duffin-schaeffer-conjecture.md) — The weak inhomogeneous Duffin–Schaeffer conjecture
- [023](023-pattersons-first-moment-for-cubic-gauss-sums.md) — Patterson’s first moment for cubic Gauss sums
- [024](024-an-asymptotic-formula-for-the-number-of-totients.md) — An asymptotic formula for the number of totients
- [025](025-erdoss-short-egyptian-fraction-conjecture.md) — Erdős’s short Egyptian-fraction conjecture
- [026](026-positive-lower-density-of-large-prime-gaps.md) — Positive lower density of large prime gaps
- [027](027-integral-density-on-curve-character-varieties.md) — Integral density on curve character varieties
- [028](028-gaussian-moat-conjecture.md) — The Gaussian moat conjecture
- [029](029-artins-primitive-root-conjecture-infinitude-for-every-base.md) — Artin's primitive root conjecture: infinitude for every base
- [030](030-modularity-over-imaginary-quadratic-fields.md) — Modularity over imaginary quadratic fields
- [031](031-uchidas-conjecture-for-open-galois-homomorphisms.md) — Uchida's conjecture for open Galois homomorphisms
- [032](032-rational-hodge-conjecture-for-cm-abelian-varieties.md) — The rational Hodge conjecture for CM abelian varieties
- [033](033-campanas-orbifold-iitaka-conjecture-and-logarithmic-subadditivity.md) — Campana's orbifold Iitaka conjecture and logarithmic subadditivity
- [034](034-log-abundance-and-effective-iitaka-fibrations.md) — Log abundance and effective Iitaka fibrations
- [035](035-threefold-log-abundance-in-numerical-dimension-one-in-characteristic-p-3.md) — Threefold log abundance in numerical dimension one in characteristic $`p>3`$
- [036](036-numerical-semiampleness-and-generalized-minimal-models.md) — Numerical semiampleness and generalized minimal models
- [037](037-sharp-ordinary-double-point-volume-gap.md) — The sharp ordinary-double-point volume gap
- [038](038-fujitas-freeness-conjecture.md) — Fujita's freeness conjecture
- [039](039-nagatas-conjecture-and-maximal-seshadri-constants.md) — Nagata's conjecture and maximal Seshadri constants
- [040](040-blochs-conjecture-for-complex-surfaces.md) — Bloch's conjecture for complex surfaces
- [041](041-hyperkahler-syz-and-projective-space-bases.md) — Hyperkähler SYZ and projective-space bases
- [042](042-oka-classification-for-k3-surfaces-and-other-compact-complex-surfaces.md) — Oka classification for K3 surfaces and other compact complex surfaces
- [043](043-p-w-for-fixed-determinant-moduli-spaces.md) — $`P=W`$ for fixed-determinant moduli spaces
- [044](044-equivariant-cohomological-hikita-conjecture-for-quivers.md) — The equivariant cohomological Hikita conjecture for quivers
- [046](046-counterexamples-to-shafarevich-holomorphic-convexity.md) — Counterexamples to Shafarevich holomorphic convexity
- [047](047-complex-counterexamples-to-cancellation-and-affine-fibrations.md) — Complex counterexamples to cancellation and affine fibrations
- [048](048-a-characteristic-zero-counterexample-to-lipman-zariski.md) — A characteristic-zero counterexample to Lipman–Zariski
- [049](049-a-stable-coordinate-counterexample-in-four-variables.md) — A stable-coordinate counterexample in four variables
- [050](050-a-counterexample-to-griffiths-positivity-conjecture.md) — A counterexample to Griffiths' positivity conjecture
- [051](051-kobayashis-canonical-ampleness-conjecture.md) — Kobayashi's canonical-ampleness conjecture
- [052](052-tangent-bundle-splittings-and-universal-covers.md) — Tangent-bundle splittings and universal covers
- [053](053-a-counterexample-to-pixtons-original-completeness-conjecture.md) — A counterexample to Pixton's original completeness conjecture
- [054](054-counterexamples-to-kuznetsovs-rationality-conjecture.md) — Counterexamples to Kuznetsov's rationality conjecture
- [055](055-todas-gepner-conjecture-and-large-volume-stability.md) — Toda's Gepner conjecture and large-volume stability
- [056](056-termination-of-fourfold-minimal-model-programs.md) — Termination of fourfold minimal model programs
- [057](057-campanas-abelianity-conjecture-and-special-varieties.md) — Campana's abelianity conjecture and special varieties
- [058](058-kollar-pardon-universal-cover-conjecture.md) — The Kollár–Pardon universal-cover conjecture
- [059](059-counterexamples-to-zariskis-multiplicity-conjecture.md) — Counterexamples to Zariski's multiplicity conjecture
- [060](060-global-spherical-shell-conjecture.md) — The Global Spherical Shell conjecture
- [062](062-lebrun-salamon-conjecture-and-projective-contact-classification.md) — The LeBrun–Salamon conjecture and projective contact classification
- [063](063-generalized-mukai-conjecture.md) — The generalized Mukai conjecture
- [064](064-constant-problem-for-surface-singularities.md) — The $`\mu`$-constant problem for surface singularities
- [065](065-virasoro-constraints-for-complete-intersections-and-projective-bundles.md) — Virasoro constraints for complete intersections and projective bundles
- [066](066-bounded-klt-complements-for-fano-contractions.md) — Bounded klt complements for Fano contractions
- [067](067-campana-peternell-conjecture-in-dimension-six.md) — The Campana–Peternell conjecture in dimension six
- [068](068-anticanonical-nonvanishing-under-smooth-semipositivity.md) — Anticanonical nonvanishing under smooth semipositivity
- [069](069-quantum-geometric-langlands-at-irrational-level.md) — Quantum geometric Langlands at irrational level
- [071](071-koebes-circle-domain-conjecture-and-circle-domain-rigidity.md) — Koebe's circle-domain conjecture and circle-domain rigidity
- [072](072-brennans-conjecture-and-a-counterexample-to-kraetzers-prediction.md) — Brennan's conjecture and a counterexample to Kraetzer's prediction
- [073](073-falconer-distance-conjecture.md) — The Falconer distance conjecture
- [074](074-kakeya-in-three-and-four-dimensions.md) — Kakeya in three and four dimensions
- [075](075-l-l-fourier-convergence-conjecture.md) — The $`L\log L`$ Fourier-convergence conjecture
- [076](076-ultraflat-real-littlewood-polynomials.md) — Ultraflat real Littlewood polynomials
- [077](077-fourier-restriction-for-positively-curved-surfaces.md) — Fourier restriction for positively curved surfaces
- [078](078-three-dimensional-bochner-riesz-conjecture.md) — The three-dimensional Bochner–Riesz conjecture
- [079](079-local-smoothing-for-the-euclidean-wave-equation.md) — Local smoothing for the Euclidean wave equation
- [080](080-sobolev-endpoint-in-carlesons-schrodinger-convergence-problem.md) — The Sobolev endpoint in Carleson's Schrödinger convergence problem
- [081](081-david-semmes-riesz-transform-problem-in-higher-codimension.md) — The David–Semmes Riesz-transform problem in higher codimension
- [082](082-maximal-and-variational-bounds-for-the-triangular-hilbert-transform.md) — Maximal and variational bounds for the triangular Hilbert transform
- [083](083-steins-conjecture-for-hilbert-transforms-along-lipschitz-directions.md) — Stein's conjecture for Hilbert transforms along Lipschitz directions
- [084](084-geometric-case-of-the-erdos-similarity-conjecture.md) — The geometric case of the Erdős similarity conjecture
- [085](085-endpoint-regularity-of-the-planar-centered-maximal-function.md) — Endpoint regularity of the planar centered maximal function
- [086](086-an-l-3-bound-for-the-trilinear-hilbert-transform.md) — An $`L^3`$ bound for the trilinear Hilbert transform
- [087](087-mahler-conjectures-and-symplectic-width.md) — The Mahler conjectures and symplectic width
- [088](088-pettys-projection-volume-conjecture-and-simplex-counterexamples.md) — Petty's projection-volume conjecture and simplex counterexamples
- [089](089-bounded-distortion-l-1-embeddings-of-planar-and-bounded-treewidth-graphs.md) — Bounded-distortion $`L_1`$ embeddings of planar and bounded-treewidth graphs
- [090](090-universal-optimality-of-the-triangular-lattice.md) — Universal optimality of the triangular lattice
- [091](091-logarithmic-brunn-minkowski-conjecture.md) — The logarithmic Brunn–Minkowski conjecture
- [092](092-optimal-order-of-convex-body-covering-density.md) — The optimal order of convex-body covering density
- [093](093-dimension-free-logarithmic-sobolev-inequality-for-subgaussian-log-concave-measures.md) — Dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures
- [094](094-subpolynomial-dimension-reduction-in-l-p.md) — Subpolynomial dimension reduction in $`L_p`$
- [095](095-hyperbolicity-cones-without-semidefinite-lifts.md) — Hyperbolicity cones without semidefinite lifts
- [096](096-gaussian-propeller-conjecture.md) — The Gaussian propeller conjecture
- [097](097-euclidean-steinitz-bergstrom-conjecture.md) — The Euclidean Steinitz–Bergström conjecture
- [098](098-a-negative-answer-to-the-lang-plaut-problem.md) — A negative answer to the Lang–Plaut problem
- [099](099-sharp-distortion-of-edit-distance-into-1.md) — The sharp distortion of edit distance into $`\ell_1`$
- [100](100-a-counterexample-to-bangs-cylinder-covering-bound.md) — A counterexample to Bang's cylinder-covering bound
- [101](101-sharp-simplex-conjecture-for-isotropic-constants.md) — The sharp simplex conjecture for isotropic constants
- [102](102-unique-games-conjecture-and-optimal-approximation-thresholds.md) — The Unique Games Conjecture and optimal approximation thresholds
- [103](103-derandomization-of-logarithmic-space-l-rl-bpl.md) — Derandomization of logarithmic space: $`\mathsf L=\mathsf{RL}=\mathsf{BPL}`$
- [104](104-quasipolynomial-algorithms-for-mean-payoff-stochastic-and-parity-games.md) — Quasipolynomial algorithms for mean-payoff, stochastic and parity games
- [105](105-2-to-1-games-conjecture-with-perfect-completeness.md) — The 2-to-1 Games Conjecture with perfect completeness
- [106](106-hardness-of-coloring-three-colorable-graphs.md) — Hardness of coloring three-colorable graphs
- [107](107-matrix-multiplication-with-exponent-at-most-9-4.md) — Matrix multiplication with exponent at most $`9/4`$
- [108](108-a-cubic-permanent-determinant-lower-bound.md) — A cubic permanent–determinant lower bound
- [109](109-integer-multiplication-below-n-n.md) — Integer multiplication below $`n\log n`$
- [110](110-optimal-order-randomized-k-server-on-arbitrary-metrics.md) — Optimal-order randomized $`k`$-server on arbitrary metrics
- [111](111-one-sample-matroid-prophet-inequalities-against-an-almighty-adversary.md) — One-sample matroid prophet inequalities against an almighty adversary
- [112](112-beyond-the-square-root-exponent-for-depth-three-circuits.md) — Beyond the square-root exponent for depth-three circuits
- [113](113-approximate-counting-and-the-perfect-matching-entropy-conjecture.md) — Approximate counting and the perfect-matching entropy conjecture
- [114](114-approximate-counting-of-common-integer-polymatroid-bases.md) — Approximate counting of common integer polymatroid bases
- [115](115-sampling-and-counting-contingency-tables-with-arbitrary-margins.md) — Sampling and counting contingency tables with arbitrary margins
- [116](116-uniform-identity-testing-for-noncommutative-formulas.md) — Uniform identity testing for noncommutative formulas
- [117](117-uniform-sparsest-cut-hardness-and-semidefinite-gaps.md) — Uniform sparsest cut: hardness and semidefinite gaps
- [118](118-unbounded-bin-packing-gaps-and-the-modified-integer-round-up-conjecture.md) — Unbounded bin-packing gaps and the modified integer round-up conjecture
- [119](119-courtade-kumar-and-hellinger-conjectures.md) — The Courtade–Kumar and Hellinger conjectures
- [120](120-almost-linear-time-exact-matching-in-general-graphs.md) — Almost-linear-time exact matching in general graphs
- [121](121-almost-linear-expected-time-approximation-of-edit-distance.md) — Almost-linear expected-time approximation of edit distance
- [122](122-superpolynomial-lower-bounds-and-quasipolynomial-reconstruction-from-deletion-traces.md) — Superpolynomial lower bounds and quasipolynomial reconstruction from deletion traces
- [124](124-polynomial-time-scheduling-on-three-identical-machines.md) — Polynomial-time scheduling on three identical machines
- [125](125-approximation-threshold-for-metric-k-median.md) — The approximation threshold for metric $`k`$-median
- [126](126-exponential-semidefinite-complexity-of-perfect-matching.md) — Exponential semidefinite complexity of perfect matching
- [127](127-asymptotic-gotsman-linial-conjecture.md) — The asymptotic Gotsman–Linial conjecture
- [128](128-a-factor-two-approximation-for-shortest-common-superstring.md) — A factor-two approximation for shortest common superstring
- [129](129-exponential-state-costs-for-two-way-automata.md) — Exponential state costs for two-way automata
- [130](130-fourier-transforms-below-n-n.md) — Fourier transforms below $`n\log n`$
- [131](131-polynomial-mixing-of-graph-switches-with-prescribed-degrees.md) — Polynomial mixing of graph switches with prescribed degrees
- [132](132-a-counterexample-to-the-quadratic-sensitivity-conjecture.md) — A counterexample to the quadratic sensitivity conjecture
- [133](133-complexity-of-weisfeiler-leman-refinement.md) — The complexity of Weisfeiler–Leman refinement
- [134](134-generalized-star-height-at-most-three.md) — Generalized star height at most three
- [135](135-sharp-homogeneous-depth-five-complexity-of-matrix-products.md) — Sharp homogeneous depth-five complexity of matrix products
- [136](136-quasilinear-pcp-for-ppad-conjecture.md) — The quasilinear PCP-for-PPAD conjecture
- [137](137-one-tape-time-simulation-in-two-fifths-power-space.md) — One-tape time simulation in two-fifths-power space
- [138](138-subset-sum-in-o-2-0-49n-time.md) — Subset Sum in $`O(2^{0.49n})`$ time
- [139](139-subpolynomial-queries-for-log-concave-sampling.md) — Subpolynomial queries for log-concave sampling
- [140](140-memory-sample-lower-bounds-for-noiseless-gaussian-regression.md) — Memory–sample lower bounds for noiseless Gaussian regression
- [141](141-existential-theory-of-the-reals-and-existential-universal-sentences-in-the-counting-hierarchy.md) — The existential theory of the reals and existential–universal sentences in the counting hierarchy
- [142](142-deterministic-polynomial-factorization-over-prime-fields.md) — Deterministic polynomial factorization over prime fields
- [143](143-uniform-limit-cycle-bounds-in-hilberts-sixteenth-problem.md) — Uniform limit-cycle bounds in Hilbert's sixteenth problem
- [144](144-banachs-simple-lebesgue-spectrum-problem.md) — Banach's simple Lebesgue-spectrum problem
- [145](145-rokhlins-multiple-mixing-problem.md) — Rokhlin's multiple-mixing problem
- [146](146-sinais-positive-entropy-conjecture-for-the-standard-map.md) — Sinai's positive-entropy conjecture for the standard map
- [147](147-near-boundary-birkhoff-conjecture.md) — The near-boundary Birkhoff conjecture
- [148](148-dimension-formula-for-self-similar-measures-on-the-line.md) — The dimension formula for self-similar measures on the line
- [149](149-permanence-for-weakly-reversible-reaction-networks.md) — Permanence for weakly reversible reaction networks
- [150](150-weak-mixing-of-irrational-triangular-billiards.md) — Weak mixing of irrational triangular billiards
- [151](151-a-c-1-counterexample-to-shubs-entropy-conjecture.md) — A $`C^1`$ counterexample to Shub’s entropy conjecture
- [152](152-zero-entropy-does-not-guarantee-a-smooth-positive-volume-model.md) — Zero entropy does not guarantee a smooth positive-volume model
- [153](153-arithmetic-classification-of-bernoulli-convolutions.md) — Arithmetic classification of Bernoulli convolutions
- [154](154-pointwise-multiple-ergodic-averages-for-mixing-transformations.md) — Pointwise multiple ergodic averages for mixing transformations
- [155](155-a-counterexample-to-periodic-tiling-in-dimension-three.md) — A counterexample to periodic tiling in dimension three
- [156](156-borsuks-conjecture-fails-in-dimension-nine.md) — Borsuk's conjecture fails in dimension nine
- [157](157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md) — Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures
- [158](158-euclidean-plane-cannot-be-colored-with-five-colors.md) — The Euclidean plane cannot be colored with five colors
- [159](159-erdoss-reciprocal-sum-conjecture-and-quasipolynomial-szemeredi-bounds.md) — Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds
- [160](160-superexponential-van-der-waerden-numbers.md) — Superexponential van der Waerden numbers
- [161](161-counterexamples-to-sidorenkos-conjecture-and-the-forcing-conjecture.md) — Counterexamples to Sidorenko's conjecture and the forcing conjecture
- [162](162-counterexamples-to-rysers-covering-and-gyarfass-tree-cover-conjectures.md) — Counterexamples to Ryser's covering and Gyárfás's tree-cover conjectures
- [164](164-hindmans-finite-sums-and-products-conjecture.md) — Hindman's finite sums and products conjecture
- [165](165-exact-crossing-numbers-of-complete-and-complete-bipartite-graphs.md) — Exact crossing numbers of complete and complete bipartite graphs
- [166](166-higher-dimensional-erdos-distinct-distances-conjecture.md) — The higher-dimensional Erdős distinct-distances conjecture
- [167](167-pinned-distances-and-a-power-saving-for-planar-unit-distances.md) — Pinned distances and a power saving for planar unit distances
- [168](168-combinatorial-invariance-of-kazhdan-lusztig-polynomials.md) — Combinatorial invariance of Kazhdan–Lusztig polynomials
- [169](169-shareshian-wachs-e-positivity-conjecture.md) — The Shareshian–Wachs $`e`$-positivity conjecture
- [170](170-sharp-logarithmic-exponents-for-off-diagonal-ramsey-numbers.md) — Sharp logarithmic exponents for off-diagonal Ramsey numbers
- [171](171-hypercube-ramsey-conjecture.md) — The hypercube Ramsey conjecture
- [172](172-classification-of-finite-euclidean-ramsey-configurations.md) — Classification of finite Euclidean Ramsey configurations
- [173](173-seymours-second-neighborhood-conjecture.md) — Seymour's second-neighborhood conjecture
- [174](174-deterministic-construction-of-strong-thin-spanning-trees.md) — Deterministic construction of strong thin spanning trees
- [175](175-talagrands-conjectures-and-graph-decompositions-at-expectation-thresholds.md) — Talagrand's conjectures and graph decompositions at expectation thresholds
- [176](176-second-kahn-kalai-conjecture.md) — The second Kahn–Kalai conjecture
- [177](177-bounded-degree-coboundary-expanders-in-every-dimension.md) — Bounded-degree coboundary expanders in every dimension
- [178](178-deterministic-nonbipartite-ramanujan-graphs-in-every-fixed-degree.md) — Deterministic nonbipartite Ramanujan graphs in every fixed degree
- [179](179-circulant-hadamard-conjecture.md) — The circulant Hadamard conjecture
- [180](180-barnettes-hamiltonian-cycle-conjecture.md) — Barnette's Hamiltonian-cycle conjecture
- [181](181-erdos-gallai-cycle-decomposition-conjecture.md) — The Erdős–Gallai cycle-decomposition conjecture
- [182](182-power-savings-for-polynomial-difference-free-sets.md) — Power savings for polynomial-difference-free sets
- [183](183-power-savings-for-planar-halving-lines-and-k-sets.md) — Power savings for planar halving lines and $`k`$-sets
- [184](184-coloring-and-independence-in-graphs-with-forbidden-subgraphs.md) — Coloring and independence in graphs with forbidden subgraphs
- [185](185-counterexamples-to-infinite-matroid-intersection-and-packing-covering.md) — Counterexamples to infinite matroid intersection and packing/covering
- [186](186-friedgut-kalai-graph-and-hypergraph-threshold-conjectures.md) — The Friedgut–Kalai graph and hypergraph threshold conjectures
- [187](187-snaky-in-21-maker-moves.md) — Snaky in 21 Maker moves
- [188](188-sharp-constant-in-random-triangle-removal.md) — The sharp constant in random triangle removal
- [189](189-exact-cycle-clique-ramsey-numbers.md) — Exact cycle–clique Ramsey numbers
- [190](190-polynomial-removal-fails-for-ordered-binary-matrices.md) — Polynomial removal fails for ordered binary matrices
- [191](191-a-power-improvement-in-the-heilbronn-triangle-problem.md) — A power improvement in the Heilbronn triangle problem
- [192](192-a-counterexample-to-the-gopalan-servedio-conjecture.md) — A counterexample to the Gopalan–Servedio conjecture
- [193](193-serres-intersection-multiplicity-conjecture.md) — Serre's intersection-multiplicity conjecture
- [194](194-lechs-multiplicity-conjecture.md) — Lech's multiplicity conjecture
- [195](195-a-counterexample-to-the-small-cohen-macaulay-module-conjecture.md) — A counterexample to the small Cohen–Macaulay module conjecture
- [196](196-a-counterexample-to-kaplanskys-zero-divisor-conjecture.md) — A counterexample to Kaplansky's zero-divisor conjecture
- [197](197-nonsofic-groups-and-group-ring-counterexamples.md) — Nonsofic groups and group-ring counterexamples
- [198](198-a-counterexample-to-the-little-finitistic-dimension-conjecture.md) — A counterexample to the little finitistic-dimension conjecture
- [199](199-counterexamples-to-conjectures-of-auslander-reiten-tachikawa-and-nakayama.md) — Counterexamples to conjectures of Auslander–Reiten, Tachikawa, and Nakayama
- [200](200-eisenbud-green-harris-and-lex-plus-powers-in-characteristic-zero.md) — Eisenbud–Green–Harris and lex-plus-powers in characteristic zero
- [201](201-a-counterexample-to-kuroshs-division-ring-problem.md) — A counterexample to Kurosh's division-ring problem
- [202](202-blockwise-alperin-weight-conjecture.md) — The blockwise Alperin weight conjecture
- [203](203-donovans-conjecture-over-fields-and-discrete-valuation-rings.md) — Donovan's conjecture over fields and discrete valuation rings
- [204](204-tensor-saturation-for-even-spin-groups.md) — Tensor saturation for even spin groups
- [205](205-saxls-conjecture-and-universal-tensor-squares.md) — Saxl's conjecture and universal tensor squares
- [206](206-finite-lattice-representation-counterexamples-and-undecidability.md) — Finite lattice representation: counterexamples and undecidability
- [207](207-1-bass-and-complex-bass-trace-conjectures.md) — The $`\ell^1`$-Bass and complex Bass trace conjectures
- [208](208-finite-benson-etingof-ostrik-conjecture.md) — The finite Benson–Etingof–Ostrik conjecture
- [209](209-integral-counterexamples-to-gerstens-conjecture.md) — Integral counterexamples to Gersten’s conjecture
- [210](210-foulkes-conjecture-for-sixth-powers-and-quadratic-stabilization.md) — Foulkes’ conjecture for sixth powers and quadratic stabilization
- [211](211-geometry-diffusion-and-spectra-of-random-planar-maps.md) — Geometry, diffusion, and spectra of random planar maps
- [212](212-no-bigeodesics-and-smooth-limit-shapes-in-planar-first-passage-percolation.md) — No bigeodesics and smooth limit shapes in planar first-passage percolation
- [213](213-no-infinite-critical-clusters-on-quasi-transitive-graphs.md) — No infinite critical clusters on quasi-transitive graphs
- [214](214-benjamini-schramm-nonuniqueness-conjecture.md) — The Benjamini–Schramm nonuniqueness conjecture
- [215](215-massive-continuum-limits-and-exact-mass-asymptotics-for-planar-o-n-models.md) — Massive continuum limits and exact mass asymptotics for planar $`O(n)`$ models
- [216](216-critical-logarithmic-corrections-and-bkt-scaling-for-the-planar-xy-model.md) — Critical logarithmic corrections and BKT scaling for the planar XY model
- [217](217-low-temperature-sherrington-kirkpatrick-fluctuation-law.md) — The low-temperature Sherrington–Kirkpatrick fluctuation law
- [218](218-conformal-universality-for-weakly-interacting-and-disordered-ising-models.md) — Conformal universality for weakly interacting and disordered Ising models
- [219](219-goe-universality-for-random-regular-graphs-with-weak-disorder.md) — GOE universality for random regular graphs with weak disorder
- [220](220-directional-zero-one-laws-and-ballisticity-in-random-environments.md) — Directional zero–one laws and ballisticity in random environments
- [221](221-mezard-parisi-formula-for-diluted-spin-glasses.md) — The Mézard–Parisi formula for diluted spin glasses
- [222](222-perceptron-free-energies-and-microscopic-jamming.md) — Perceptron free energies and microscopic jamming
- [223](223-conformal-limits-of-square-lattice-random-cluster-interfaces.md) — Conformal limits of square-lattice random-cluster interfaces
- [224](224-critical-and-near-critical-universality-for-voronoi-percolation.md) — Critical and near-critical universality for Voronoi percolation
- [225](225-gaussian-free-field-limits-for-the-balanced-six-vertex-model.md) — Gaussian free field limits for the balanced six-vertex model
- [226](226-double-dimer-cle-4-conjecture-in-the-half-plane.md) — The double-dimer $`\mathrm{CLE}_4`$ conjecture in the half-plane
- [227](227-dynamical-phase-transition-in-the-sherrington-kirkpatrick-model.md) — The dynamical phase transition in the Sherrington–Kirkpatrick model
- [228](228-continuum-phase-transitions-for-radial-pair-potentials.md) — Continuum phase transitions for radial pair potentials
- [229](229-sharp-three-and-four-state-reconstruction-thresholds.md) — Sharp three- and four-state reconstruction thresholds
- [230](230-exact-hausdorff-measure-for-sle.md) — Exact Hausdorff measure for SLE
- [231](231-free-uniform-spanning-forest-is-a-factor-of-iid.md) — The free uniform spanning forest is a factor of IID
- [232](232-gaussian-fields-and-sle-interfaces-for-lipschitz-heights.md) — Gaussian fields and SLE interfaces for Lipschitz heights
- [233](233-joint-critical-ashkin-teller-scaling-limit.md) — The joint critical Ashkin–Teller scaling limit
- [234](234-all-temperature-pressure-for-orthogonally-invariant-ising-spin-glasses.md) — All-temperature pressure for orthogonally invariant Ising spin glasses
- [235](235-random-sat-thresholds-sharp-variance-and-computability.md) — Random-SAT thresholds, sharp variance and computability
- [236](236-factor-of-iid-threshold-for-free-ising-states-on-trees.md) — The factor-of-IID threshold for free Ising states on trees
- [237](237-three-quarter-diameter-exponent-for-honeycomb-walks.md) — The three-quarter diameter exponent for honeycomb walks
- [238](238-optimal-logarithmic-mixing-of-the-thorp-shuffle.md) — Optimal logarithmic mixing of the Thorp shuffle
- [239](239-sharp-singularity-rates-for-symmetric-sign-matrices.md) — Sharp singularity rates for symmetric sign matrices
- [240](240-shelahs-eventual-categoricity-conjecture.md) — Shelah's eventual categoricity conjecture
- [241](241-rigidity-of-the-turing-degrees.md) — Rigidity of the Turing degrees
- [242](242-single-fold-diophantine-representations.md) — Single-fold Diophantine representations
- [243](243-choiceless-counting-does-not-capture-polynomial-time.md) — Choiceless counting does not capture polynomial time
- [244](244-partition-principle-does-not-imply-choice.md) — The partition principle does not imply choice
- [245](245-barendregt-geuvers-klop-conjecture.md) — The $`\beta`$-Barendregt–Geuvers–Klop conjecture
- [246](246-cannons-conjecture.md) — Cannon's conjecture
- [247](247-an-infinite-finitely-presented-residually-finite-2-group.md) — An infinite finitely presented residually finite $`2`$-group
- [248](248-thompsons-group-f-is-nonamenable.md) — Thompson's group $`F`$ is nonamenable
- [249](249-a-finitely-generated-counterexample-to-eilenberg-ganea.md) — A finitely generated counterexample to Eilenberg–Ganea
- [250](250-boone-higman-conjecture-and-higher-finiteness.md) — The Boone–Higman conjecture and higher finiteness
- [251](251-amenability-unitarizability-and-ulam-stability.md) — Amenability, unitarizability, and Ulam stability
- [252](252-a-non-residually-finite-torsion-free-hyperbolic-group.md) — A non-residually-finite torsion-free hyperbolic group
- [253](253-an-infinite-finitely-presented-simple-amenable-group.md) — An infinite finitely presented simple amenable group
- [254](254-classifying-spaces-and-geometric-obstructions-for-artin-groups.md) — Classifying spaces and geometric obstructions for Artin groups
- [255](255-quasi-isometric-rigidity-of-virtually-polycyclic-groups.md) — Quasi-isometric rigidity of virtually polycyclic groups
- [256](256-howies-conjecture-on-equations-over-groups.md) — Howie's conjecture on equations over groups
- [257](257-a-hyperbolic-group-with-no-geometric-cat-0-action.md) — A hyperbolic group with no geometric CAT(0) action
- [258](258-gerstens-conjecture-for-one-relator-groups.md) — Gersten's conjecture for one-relator groups
- [259](259-a-group-without-fixed-price.md) — A group without fixed price
- [260](260-spacetime-penrose-inequalities-and-rigidity.md) — Spacetime Penrose inequalities and rigidity
- [261](261-localization-and-delocalization-in-the-anderson-model.md) — Localization and delocalization in the Anderson model
- [262](262-sharp-one-dimensional-lieb-thirring-inequalities.md) — Sharp one-dimensional Lieb–Thirring inequalities
- [263](263-ionization-and-generalized-ionization-conjectures.md) — The ionization and generalized ionization conjectures
- [264](264-strong-cosmic-censorship-near-two-ended-kerr-data.md) — Strong cosmic censorship near two-ended Kerr data
- [265](265-two-dimensional-gapped-area-law.md) — The two-dimensional gapped area law
- [266](266-exactly-three-mutually-unbiased-bases-in-dimension-six.md) — Exactly three mutually unbiased bases in dimension six
- [267](267-positive-temperature-bose-einstein-condensation-and-quantum-depletion.md) — Positive-temperature Bose–Einstein condensation and quantum depletion
- [268](268-spin-one-haldane-gap.md) — The spin-one Haldane gap
- [269](269-laughlin-gap-and-stability-under-scalar-disorder.md) — The Laughlin gap and stability under scalar disorder
- [270](270-threshold-and-positive-energy-bound-states-of-the-bfss-model.md) — Threshold and positive-energy bound states of the BFSS model
- [271](271-blochs-law-and-spontaneous-ferromagnetic-order.md) — Bloch's law and spontaneous ferromagnetic order
- [272](272-entanglement-without-secret-key-and-the-ppt-square-conjecture.md) — Entanglement without secret key and the PPT-square conjecture
- [273](273-entropy-photon-number-inequality.md) — The entropy photon-number inequality
- [274](274-moores-parity-conjecture-for-qac-0.md) — Moore's parity conjecture for $`\mathrm{QAC}^0`$
- [275](275-qma-hardness-of-continuum-coulomb-energy.md) — QMA-hardness of continuum Coulomb energy
- [284](284-optimal-randomized-quantum-query-exponent.md) — The optimal randomized–quantum query exponent
- [285](285-counterexamples-to-baum-connes-and-kadison-kaplansky.md) — Counterexamples to Baum–Connes and Kadison–Kaplansky
- [287](287-all-nonabelian-free-group-factors-are-isomorphic.md) — All nonabelian free group factors are isomorphic
- [300](300-popa-vaes-quadratic-strong-operator-paving-conjecture.md) — The Popa–Vaes quadratic strong-operator paving conjecture
- [304](304-hilbert-smith-conjecture-in-every-dimension.md) — The Hilbert–Smith conjecture in every dimension
- [305](305-counterexamples-to-disk-embedding-and-walls-manifold-conjecture.md) — Counterexamples to disk embedding and Wall's manifold conjecture
- [306](306-purely-cosmetic-surgery-conjecture-for-knots-in-s-3.md) — The purely cosmetic surgery conjecture for knots in $`S^3`$
- [309](309-kervaire-invariant-problem-at-the-prime-three.md) — The Kervaire invariant problem at the prime three
- [310](310-quillens-conjecture-in-rational-homology.md) — Quillen's conjecture in rational homology
- [311](311-chais-invariant-ideal-conjecture.md) — Chai's invariant-ideal conjecture
- [313](313-finite-generation-for-the-k-n-local-sphere.md) — Finite generation for the $`K(n)`$-local sphere
- [315](315-four-dimensional-singer-conjecture.md) — The four-dimensional Singer conjecture
- [316](316-curtiss-conjecture.md) — Curtis’s conjecture
- [319](319-counterexamples-to-the-hahn-wilson-conjecture-at-height-two.md) — Counterexamples to the Hahn–Wilson conjecture at height two
- [320](320-a-four-dimensional-counterexample-to-borel-rigidity.md) — A four-dimensional counterexample to Borel rigidity
- [321](321-a-counterexample-to-walls-finite-d-2-conjecture.md) — A counterexample to Wall's finite D(2) conjecture
- [324](324-lipschitz-equivalence-without-linear-isomorphism.md) — Lipschitz equivalence without linear isomorphism
- [325](325-complete-crouzeix-conjecture.md) — The complete Crouzeix conjecture
- [331](331-asymptotic-midpoint-uniform-convexity-without-asymptotically-uniformly-convex-renorming.md) — Asymptotic midpoint uniform convexity without asymptotically uniformly convex renorming
- [332](332-metric-markov-cotype-two-for-1.md) — Metric Markov cotype two for $`\ell_1`$
- [334](334-a-smooth-surface-metric-with-no-local-immersion-in-r-3.md) — A smooth surface metric with no local immersion in $`\mathbb R^3`$
- [335](335-gromovs-integral-scalar-curvature-inequality.md) — Gromov's integral scalar-curvature inequality
- [338](338-yaus-uniformization-conjecture.md) — Yau's uniformization conjecture
- [339](339-katoks-entropy-rigidity-conjecture.md) — Katok's entropy rigidity conjecture
- [340](340-a-counterexample-to-the-nearby-lagrangian-conjecture.md) — A counterexample to the nearby Lagrangian conjecture
- [341](341-donaldsons-hypersymplectic-deformation-conjecture.md) — Donaldson's hypersymplectic deformation conjecture
- [342](342-donaldsons-tamed-to-compatible-conjecture.md) — Donaldson's tamed-to-compatible conjecture
- [344](344-metric-blaschke-conjecture.md) — The metric Blaschke conjecture
- [345](345-infinitely-many-closed-geodesics-on-spheres-and-three-manifolds.md) — Infinitely many closed geodesics on spheres and three-manifolds
- [346](346-sharp-singular-set-bounds-for-stationary-integral-varifolds.md) — Sharp singular-set bounds for stationary integral varifolds
- [347](347-counterexamples-to-strong-forms-of-arnolds-fixed-point-conjecture.md) — Counterexamples to strong forms of Arnold's fixed-point conjecture
- [348](348-nonnegatively-curved-einstein-four-manifolds-and-a-topological-gap.md) — Nonnegatively curved Einstein four-manifolds and a topological gap
- [349](349-solomon-yau-least-volume-conjecture.md) — The Solomon–Yau least-volume conjecture
- [351](351-scalar-curvature-detects-four-dimensional-ricci-flow-singularities.md) — Scalar curvature detects four-dimensional Ricci-flow singularities
- [352](352-finite-time-singularity-of-calabi-flow.md) — Finite-time singularity of Calabi flow
- [362](362-global-smoothness-for-relativistic-vlasov-maxwell.md) — Global smoothness for relativistic Vlasov–Maxwell
- [366](366-planar-mumford-shah-regularity-conjecture.md) — The planar Mumford–Shah regularity conjecture
- [368](368-three-dimensional-ball-evans-approximation-problem.md) — The three-dimensional Ball–Evans approximation problem
- [375](375-de-giorgis-conjecture-in-dimension-eight.md) — De Giorgi's conjecture in dimension eight
- [378](378-disproof-of-the-exponential-time-hypothesis.md) — Disproof of the Exponential Time Hypothesis

## The checker

```
python3 notes/scripts/verify_summaries.py
```

It resolves every `[Sn:line]` marker against the shipped file, checks every quotation against the
lines it cites, counts a Sources-table `File` cell that resolves under both roots as a problem, and
writes nothing. Its self-tests are in `notes/scripts/tests/test_summaries.py`, run by
`python3 notes/scripts/run_tests.py notes/scripts/tests/test_summaries.py -q`.

Three more tools read the pages: `check_summary_manuscripts.py` reports which manuscripts each page
reads and whether the release still names them, `locate_summary_quotes.py` (takes a page path)
reports where a quotation's text actually sits when the checker flags a miss, and
`read_manuscript.py` takes a `preprints/` directory name and prints the abstract, the section
skeleton and the titled statement environments with anchors. All three write nothing.

This page is link-only: it names no manuscript directory and cites no family-keyed file, so the
checker's manuscript-directory pass and its family-citation pass skip it. Its links are checked.

## Not checked

- **63 families have no summary page.** The 310 pages cover 310 of 373 families; the rest are recorded
  in the ledger and the index, not summarized.
- **The coverage counts are the release's own.** The yaml's `scope`, `automation` and `review` fields
  state partial progress, the agent method, and an unchecked review — those are the release's claims, not
  verified results. Zero `sorry` in a formalized file is not a comparator pass, and it does not mean the
  library elaborates.
- **No page was checked by running Lean.** Nothing in this repo builds, and a Lean run would prove the
  formalized statement, not the manuscript's theorem.
