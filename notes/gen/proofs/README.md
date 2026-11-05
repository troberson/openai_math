# Proof-level faithfulness audits

103 per-family audits comparing a preprint's proof with its Lean formalization. The
statement-level comparison is family-specific; the proof-level comparison follows the
shared protocol in the data file [`README.md`](../../data/proofs/README.md) — the
"lost in translation" failure modes, the seven extraction targets, the reparameterization
test, and the sign audit.

Each page is rendered by `build_proofs.py` from a hand-edited data file
(`notes/data/proofs/<NNN>.md`) and the page skeleton; the checker
(`verify_proofs.py`) measures the rendered bytes and writes nothing.

## The pages

- [072](./072.md) — Brennan's conjecture and a counterexample to Kraetzer's prediction
- [073](./073.md) — The Falconer distance conjecture
- [075](./075.md) — The $L\log L$ Fourier-convergence conjecture
- [076](./076.md) — Ultraflat real Littlewood polynomials
- [079](./079.md) — Local smoothing for the Euclidean wave equation
- [081](./081.md) — The David–Semmes Riesz-transform problem in higher codimension
- [082](./082.md) — Maximal and variational bounds for the triangular Hilbert transform
- [085](./085.md) — Endpoint regularity of the planar centered maximal function
- [087](./087.md) — The Mahler conjectures and symplectic width
- [091](./091.md) — The logarithmic Brunn–Minkowski conjecture
- [094](./094.md) — Subpolynomial dimension reduction in $L_p$
- [102](./102.md) — The Unique Games Conjecture and optimal approximation thresholds
- [103](./103.md) — Derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$
- [104](./104.md) — Quasipolynomial algorithms for mean-payoff, stochastic and parity games
- [105](./105.md) — The 2-to-1 Games Conjecture with perfect completeness
- [106](./106.md) — Hardness of coloring three-colorable graphs
- [107](./107.md) — Matrix multiplication with exponent at most $9/4$
- [112](./112.md) — Beyond the square-root exponent for depth-three circuits
- [113](./113.md) — Approximate counting and the perfect-matching entropy conjecture
- [114](./114.md) — Approximate counting of common integer polymatroid bases
- [116](./116.md) — Uniform identity testing for noncommutative formulas
- [117](./117.md) — Uniform sparsest cut: hardness and semidefinite gaps
- [118](./118.md) — Unbounded bin-packing gaps and the modified integer round-up conjecture
- [119](./119.md) — The Courtade–Kumar and Hellinger conjectures
- [125](./125.md) — The approximation threshold for metric $k$-median
- [127](./127.md) — The asymptotic Gotsman–Linial conjecture
- [128](./128.md) — A factor-two approximation for shortest common superstring
- [129](./129.md) — Exponential state costs for two-way automata
- [130](./130.md) — Fourier transforms below $n\log n$
- [132](./132.md) — A counterexample to the quadratic sensitivity conjecture
- [137](./137.md) — One-tape time simulation in two-fifths-power space
- [139](./139.md) — Subpolynomial queries for log-concave sampling
- [140](./140.md) — Memory–sample lower bounds for noiseless Gaussian regression
- [155](./155.md) — A counterexample to periodic tiling in dimension three
- [156](./156.md) — Borsuk's conjecture fails in dimension nine
- [157](./157.md) — Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures
- [158](./158.md) — The Euclidean plane cannot be colored with five colors
- [159](./159.md) — Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds
- [160](./160.md) — Superexponential van der Waerden numbers
- [162](./162.md) — Counterexamples to Ryser's covering and Gyárfás's tree-cover conjectures
- [165](./165.md) — Exact crossing numbers of complete and complete bipartite graphs
- [167](./167.md) — Pinned distances and a power saving for planar unit distances
- [172](./172.md) — Classification of finite Euclidean Ramsey configurations
- [173](./173.md) — Seymour's second-neighborhood conjecture
- [174](./174.md) — Deterministic construction of strong thin spanning trees
- [175](./175.md) — Talagrand's conjectures and graph decompositions at expectation thresholds
- [176](./176.md) — The second Kahn–Kalai conjecture
- [179](./179.md) — The circulant Hadamard conjecture
- [181](./181.md) — The Erdős–Gallai cycle-decomposition conjecture
- [184](./184.md) — Coloring and independence in graphs with forbidden subgraphs
- [185](./185.md) — Counterexamples to infinite matroid intersection and packing/covering
- [190](./190.md) — Polynomial removal fails for ordered binary matrices
- [195](./195.md) — A counterexample to the small Cohen–Macaulay module conjecture
- [196](./196.md) — A counterexample to Kaplansky's zero-divisor conjecture
- [197](./197.md) — Nonsofic groups and group-ring counterexamples
- [198](./198.md) — A counterexample to the little finitistic-dimension conjecture
- [199](./199.md) — Counterexamples to conjectures of Auslander–Reiten, Tachikawa, and Nakayama
- [205](./205.md) — Saxl's conjecture and universal tensor squares
- [207](./207.md) — The $\ell^1$-Bass and complex Bass trace conjectures
- [210](./210.md) — Foulkes’ conjecture for sixth powers and quadratic stabilization
- [212](./212.md) — No bigeodesics and smooth limit shapes in planar first-passage percolation
- [213](./213.md) — No infinite critical clusters on quasi-transitive graphs
- [215](./215.md) — Massive continuum limits and exact mass asymptotics for planar $O(n)$ models
- [220](./220.md) — Directional zero–one laws and ballisticity in random environments
- [227](./227.md) — The dynamical phase transition in the Sherrington–Kirkpatrick model
- [228](./228.md) — Continuum phase transitions for radial pair potentials
- [230](./230.md) — Exact Hausdorff measure for SLE
- [234](./234.md) — All-temperature pressure for orthogonally invariant Ising spin glasses
- [235](./235.md) — Random-SAT thresholds, sharp variance and computability
- [236](./236.md) — The factor-of-IID threshold for free Ising states on trees
- [237](./237.md) — The three-quarter diameter exponent for honeycomb walks
- [238](./238.md) — Optimal logarithmic mixing of the Thorp shuffle
- [240](./240.md) — Shelah's eventual categoricity conjecture
- [241](./241.md) — Rigidity of the Turing degrees
- [242](./242.md) — Single-fold Diophantine representations
- [243](./243.md) — Choiceless counting does not capture polynomial time
- [244](./244.md) — The partition principle does not imply choice
- [288](./288.md) — Kadison's similarity conjecture
- [290](./290.md) — Connes' bicentralizer conjecture and relative bicentralizers
- [291](./291.md) — Toms–Winter and equivariant Jiang–Su stability
- [293](./293.md) — A counterexample to the hyperinvariant-subspace problem
- [294](./294.md) — A counterexample to Kaplansky's quasitrace conjecture
- [296](./296.md) — The generator problem for finite factors
- [299](./299.md) — The Kirchberg–Rø rdam character criterion
- [301](./301.md) — Classification by trace cones after Razak–Jacelon stabilization
- [322](./322.md) — Tingley's sphere-isometry problem
- [324](./324.md) — Lipschitz equivalence without linear isomorphism
- [325](./325.md) — The complete Crouzeix conjecture
- [326](./326.md) — The cotype–cotype conjecture under the approximation property
- [327](./327.md) — Markov type characterizes superreflexivity
- [328](./328.md) — Fixed points of nonexpansive maps in reflexive Banach spaces
- [329](./329.md) — A counterexample to Pietsch's metric-entropy duality conjecture
- [331](./331.md) — Asymptotic midpoint uniform convexity without asymptotically uniformly convex renorming
- [334](./334.md) — A smooth surface metric with no local immersion in $\mathbb R^3$
- [342](./342.md) — Donaldson's tamed-to-compatible conjecture
- [347](./347.md) — Counterexamples to strong forms of Arnold's fixed-point conjecture
- [350](./350.md) — Yau's nodal conjecture: surfaces and counterexamples
- [356](./356.md) — Gigli's characterization of Alexandrov curvature
- [358](./358.md) — A three-manifold with no conjugate points and no nonpositively curved metric
- [359](./359.md) — Negative Kähler curvature without bounded holomorphic coordinates
- [360](./360.md) — Villani’s convexity conjecture and regular optimal transport
- [361](./361.md) — Counterexamples to Yau's harmonic dimension bound
- [378](./378.md) — Disproof of the Exponential Time Hypothesis

## Not checked

- A green page proves the citation surface, not the mathematics: it names the lines each
  quote sits on, and those lines are what they say. It does not re-derive the proof.
- Nothing in this repo builds, and no Lean run was made here; a Lean statement is evidence
  the claim was stated and proved by the agent, not independently verified.
