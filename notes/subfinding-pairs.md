# Sub-finding pairs: the abstract clause and the display title that names it

Every family in the catalog lists its manuscripts as `\href` links inside its own `\resultentry`, so
`overview.tex` carries two descriptions of the same result: the family abstract, and one display title
per manuscript. This page reads, for the densest families, which abstract clause states a sub-finding
and which display title names it. Each pair is quoted with the line it was verified on, and clauses
that state a sub-finding no title names are recorded as unmatched rather than forced onto the nearest
title.

Population: **49 families over 203 manuscripts**. The rule is the bead's own two signals unioned with
its named targets — abstracts containing a multi-claim phrase **and** at least two manuscripts, plus
the ten densest families it names. The bead states 51 families for the intersection; that number does
not reproduce, and the gap is the first thing this page records.

## The population, and why it is not the bead's 51

The bead's probe vocabulary is `also prove` (25), `Independent` (35), `also establish` (5),
`not as a consequence` (1), and it warns that `corollary`, `we also prove`, `furthermore`, `we show`
are all zero. All four counts reproduce over the 372 shipped abstracts, with one spelling condition:
the second is the stem `independ`, not the word `independent` (34). The zero counts reproduce too.
So the vocabulary is right and the family count is not.

| rule | families |
|---|---|
| `also prove` | 25 |
| `independ` (stem) | 35 |
| `also establish` | 5 |
| `as a consequence` | 1 |
| union of the four, over all 372 | 62 |
| families with ≥2 manuscripts | 167 |
| **union of the four, over the 167** | **40** |

40, not 51. Nine of the bead's ten named densest targets (all but 034) sit **outside** its own
probe-and-multi set, so the 51 cannot be the intersection of the two signals it describes. Rules
tried and rejected: `also` (56), `both ` (48), `companion` (10), `together` (8), two or more
prove-verbs in the abstract (33), two or more sentences containing a prove-verb (32), three or more
sentences (73). None yields 51, and the same shape of gap — a quoted count with no reproducible rule —
is the counterexample 74 / 30 case recorded in `notes/counterexample-tag.md`.

**Decision, recorded 2026-10-07.** Population = (probe ∩ multi) ∪ the bead's ten named densest
families = **49 families, 203 manuscripts** (206 before the 2026-10-07 upstream merge; family 032 lost
three manuscripts to the withdrawal and stayed in the population). The union is chosen over the
intersection because the bead's named targets are the point of the task — 034 at n=14 down to 211 at
n=7 — and the probe is the point of its vocabulary warning. Revisit condition: if a later pass finds a
phrase rule that yields 51, re-measure the population before extending the page; the rework is a re-run
of `notes/scripts/extract_subfinding_pairs.py` plus blocks for the families the new rule adds, which is
cheap, so this bead keeps the task.

Probe-vocabulary false positives: 114, 122, 134, 157, 170, 235, 261, 262, 266, 267, 281, 325, 361. In
these the probe phrase modifies a noun (`independent` of a random choice, `independent` convergence,
`independent` in a theorem statement), not a second result. 13 of the 40 probe-hit families are in this
list, which is why the probe is a floor for the population and not a reading of it.

## Reading method

One line per pair. `main` pairs the clause that states the family's headline result; `clause` pairs a
clause that states an additional result. A clause is a sub-finding when it asserts a result the
headline does not already assert. The quoted clause and the quoted title are both taken verbatim from
the family's single `\resultentry` line, so one anchor proves both sides: the abstract and every
display title of a family sit on that line (verified for all 372 families). `[NNN:k]` is the k-th
manuscript of family NNN in `notes/subfindings.tsv`, whose `title` column is the same display text.
`claimed` and `unclaimed` partition the family's manuscripts, so every title is accounted for once.


## 009 · `overview.tex:94` · n=3 · T2

- main: "Reconstructs function fields of transcendence degree at least two over algebraically closed constants from $K^{\mathrm M}_1/\ell$, $K^{\mathrm M}_2/\ell$, and their product." (`overview.tex:94`) -> "Reconstruction of Function Fields from Mod-$\ell$ Milnor $K$-Theory" (`overview.tex:94`) [009:1]
- clause: "These data recover the perfect closure and constants when $\ell$ differs from the characteristic, and the original field and its named base in equal characteristic." (`overview.tex:94`) -> "Reconstruction from Milnor $K$-theory modulo the characteristic" (`overview.tex:94`) [009:2]
- clause: "Also proves Bogomolov--Pop reconstruction from abelian-by-central pro-$\ell$ Galois data away from the characteristic." (`overview.tex:94`) -> "The Bogomolov-Pop reconstruction theorem" (`overview.tex:94`) [009:3]
- claimed: 009:1 009:2 009:3
- unclaimed:
- note: The 009:2 pairing is the equal-characteristic half of the sentence; the abstract states both
  halves in one clause, so the clause covers 009:1 and 009:2 together and is assigned to the half the
  headline does not state.

## 010 · `overview.tex:96` · n=3 · T0

- main: "Every continuous odd absolutely irreducible two-dimensional $2$-adic representation of $G_{\mathbb Q}$ unramified outside finitely many primes occurs in a completed Hecke algebra at some odd tame level." (`overview.tex:96`) -> "Unrestricted pro-modularity" (`overview.tex:96`) [010:1]
- clause: "Also proves classical modularity up to Tate twist for irreducible odd representations with these finiteness conditions that are de Rham at $2$ with distinct Hodge--Tate weights, resolving the dyadic Fontaine--Mazur case without residual restrictions." (`overview.tex:96`) -> "Fontaine–Mazur modularity at the prime 2" (`overview.tex:96`) [010:3]
- claimed: 010:1 010:3
- unclaimed: 010:2
- note: "Two-adic Hecke dimension" names the dimension computation behind the headline; the abstract
  states no clause for it.

## 011 · `overview.tex:98` · n=3 · T0

- main: "Proves that the normalized ordered logarithms of the prime factors of $p-1$, counted with multiplicity, converge jointly to the Poisson--Dirichlet law $\mathrm{PD}(1)$ as $p$ ranges uniformly over primes up to $x$ and $x\to\infty$." (`overview.tex:98`) -> "The Poisson-Dirichlet law for prime predecessors" (`overview.tex:98`) [011:2]
- clause: "It also proves that infinitely many integers $n$ have more than $n^{1-\varepsilon}$ totient preimages, for every $\varepsilon>0$." (`overview.tex:98`) -> "Weighted dilation graphs, smooth shifted primes and totient fibers" (`overview.tex:98`) [011:1]
- claimed: 011:1 011:2
- unclaimed: 011:3
- note: "Prime Predecessors with an Even Number of Prime Factors" has no clause in the abstract.

## 014 · `overview.tex:104` · n=8 · T0

- main: "Proves the restricted geometric Langlands equivalence for connected reductive groups on smooth projective connected curves over $\overline{\mathbb F}_q$ under the four stated Lie-theoretic characteristic hypotheses." (`overview.tex:104`) -> "Restricted geometric Langlands" (`overview.tex:104`) [014:5]
- clause: "Over arbitrary algebraically closed fields of characteristic $p>0$, the same conclusion holds assuming additionally that $p$ is very good for the group and $p\nmid |W_G|$." (`overview.tex:104`) -> unmatched
- clause: "Over global function fields, proves Ramanujan at every place for globally generic cuspidal representations of split adjoint absolutely simple exceptional groups, without characteristic or ramification-depth restrictions" (`overview.tex:104`) -> "Temperedness at ramified places for globally generic exceptional groups" (`overview.tex:104`) [014:4]
- clause: "and at every unramified place for cuspidal representations of split adjoint absolutely simple groups with a generic unramified component." (`overview.tex:104`) -> "Unramified Arthur filtration" (`overview.tex:104`) [014:2]
- clause: "Assuming the finite-level Ramanujan--Arthur decomposition, constructs global Arthur enhancements of occurring cuspidal excursion parameters for split connected semisimple groups at full finite level, recovering the given parameters by diagonal specialization on the entire Weil group, including inertia." (`overview.tex:104`) -> "Global Arthur Enhancements of Cuspidal Excursion Parameters" (`overview.tex:104`) [014:1]
- claimed: 014:1 014:2 014:4 014:5
- unclaimed: 014:3 014:6 014:7 014:8
- note: The unmatched clause is the arbitrary-characteristic case of the headline; no display title
  names it separately. 014:3 is the assumption the last clause is made under
  ("Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level"), not a result the
  abstract claims. 014:6, 014:7 and 014:8 are tame-Hecke-eigensheaf manuscripts the abstract does not
  mention at all.

## 016 · `overview.tex:108` · n=4 · T0

- main: "Proves the abelian Zilber--Pink conjecture over $\overline{\mathbb Q}$: every irreducible subvariety has finitely many maximal atypical subvarieties relative to its smallest containing torsion coset." (`overview.tex:108`) -> "Abelian Zilber–Pink" (`overview.tex:108`) [016:1]
- clause: "It also proves the full curve case in the Siegel threefold $\mathcal A_2$ for Hodge-generic curves defined over $\overline{\mathbb Q}$, without boundary or reduction assumptions." (`overview.tex:108`) -> unmatched
- claimed: 016:1
- unclaimed: 016:2 016:3 016:4
- note: The clause is an umbrella: three titles each name one case of the $\mathcal A_2$ curve case
  ("$E\times\mathrm{CM}$ component", "Quaternionic division points", "Elliptic squares"), so pairing
  it with any one of them would be a forced pairing.

## 019 · `overview.tex:114` · n=2 · T0

- main: "Proves that rational points on every smooth proper geometrically connected curve of genus at least two over a finite extension of $\mathbb Q_p$ correspond bijectively to conjugacy classes of sections of its full arithmetic \'etale fundamental group." (`overview.tex:114`) -> "p-adic section conjecture" (`overview.tex:114`) [019:2]
- clause: "It also proves Grothendieck's section conjecture over $\mathbb Q$ for the modular curves $X_0(N)$ and $X_1(N)$ of genus at least two." (`overview.tex:114`) -> unmatched
- claimed: 019:2
- unclaimed: 019:1
- note: The $\mathbb Q$ case has no display title. "Prescribed exterior sheet" is an étale-cover
  construction the abstract does not state as a result.

## 032 · `overview.tex:142` · n=5 · T0

- main: "Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and codimension." (`overview.tex:142`) -> "The rational Hodge conjecture for CM abelian varieties" (`overview.tex:142`) [032:1]
- clause: "Through Milne's theorems, this also gives the Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every characteristic." (`overview.tex:142`) -> unmatched
- claimed: 032:1
- unclaimed: 032:2 032:3 032:4 032:5
- note: The unmatched clause states consequences through Milne's theorems, not a result the release
  ships a manuscript for. Four further manuscripts (K3 quadratic locus, Weil classes on abelian powers,
  Gale correspondences, a conditional reduction) carry no clause. This family is the withdrawal: the
  two clauses that paired here before the merge — the products-of-K3 theorem and the Kuga–Satake
  algebraicity result — were withdrawn on 2026-10-06 and their clauses are gone from the overview
  abstract, so the family lost two accepted pairs and three manuscripts. See
  `upstream_history/2026-10-07_3014888.md`.

## 034 · `overview.tex:146` · n=14 · T0

- main: "Using logarithmic Iitaka subadditivity, proves log abundance in every dimension for normal compact K\"ahler log canonical pairs with effective rational boundary: an analytically nef $\mathbb Q$-Cartier adjoint is semiample." (`overview.tex:146`) -> "Log abundance for compact Kähler spaces" (`overview.tex:146`) [034:1]
- clause: "It also proves projective log abundance over every algebraically closed field of characteristic zero" (`overview.tex:146`) -> "Log abundance in characteristic zero" (`overview.tex:146`) [034:4]
- clause: "and the effective Iitaka fibration conjecture for smooth projective varieties of nonnegative Kodaira dimension in that setting." (`overview.tex:146`) -> "Uniform pluricanonical Iitaka fibrations" (`overview.tex:146`) [034:10]
- clause: "A further result resolves the finite-rational-coefficient index conjecture for connected projective semi-log-canonical log Calabi--Yau pairs over such fields in each fixed dimension and for each fixed finite set of rational boundary coefficients, with a uniform index independent of the number of components." (`overview.tex:146`) -> "Uniform indices for semi-log-canonical log Calabi--Yau pairs" (`overview.tex:146`) [034:2]
- claimed: 034:1 034:2 034:4 034:10
- unclaimed: 034:3 034:5 034:6 034:7 034:8 034:9 034:11 034:12 034:13 034:14
- note: The densest family in the corpus states four results and ships fourteen manuscripts; the other
  ten are the machinery (conditional good minimal models, minimal metrics, fourfold nonvanishing,
  section lifting, Schnell fiber spaces, uniform log Iitaka fibrations, log Calabi–Yau fibrations,
  Stein-degree bounds, fourfold log Iitaka fibrations, abundance after nonvanishing).

## 039 · `overview.tex:156` · n=4 · T3

- main: "Proves Nagata's strict inequality $\sum_i m_i<d\sqrt r$ for every nonzero effective plane curve of degree $d$ through $r\ge10$ very general complex points, with arbitrary multiplicities $m_i$." (`overview.tex:156`) -> "Plane-curve Nagata conjecture" (`overview.tex:156`) [039:1]
- clause: "It also proves maximal multipoint Seshadri constants $(L^n/r)^{1/n}$ for every smooth polarized projective variety of dimension $n\ge2$ and all sufficiently large $r$: at very general points over $\mathbb C$" (`overview.tex:156`) -> "Maximal Multipoint Seshadri Constants in Higher Dimensions" (`overview.tex:156`) [039:3]
- clause: "and at the geometric generic tuple over any algebraically closed field of positive characteristic." (`overview.tex:156`) -> "Maximal multipoint Seshadri constants in positive characteristic" (`overview.tex:156`) [039:4]
- claimed: 039:1 039:3 039:4
- unclaimed: 039:2
- note: "Maximal Seshadri constants" (the surface case, `Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces`)
  is the $n=2$ instance of the clause paired to 039:3; the abstract states no separate surface clause.

## 041 · `overview.tex:160` · n=2 · T0

- main: "Proves the strong hyperk\"ahler SYZ conjecture: every holomorphic line bundle with nonzero nef isotropic first Chern class on a compact irreducible holomorphic symplectic K\"ahler manifold is semiample." (`overview.tex:160`) -> "Strong hyperkähler SYZ" (`overview.tex:160`) [041:2]
- clause: "It also proves that every projective Lagrangian fibration with normal projective base has projective space as its base, in every dimension and deformation type." (`overview.tex:160`) -> "Projective-space bases" (`overview.tex:160`) [041:1]
- claimed: 041:1 041:2
- unclaimed:

## 056 · `overview.tex:188` · n=5 · T0

- main: "Proves termination of every existing generalized log canonical flip sequence on globally Weil $\mathbb Q$-factorial compact K\"ahler fourfolds, with rational boundary, fixed rational analytically nef b-data, and projective small flip diagrams with the prescribed ample signs." (`overview.tex:188`) -> "Termination of generalized log canonical flips on compact Kähler fourfolds" (`overview.tex:188`) [056:1]
- clause: "Also proves termination of arbitrary permitted minimal model programs for projective log canonical fourfolds with rational boundary in characteristic zero." (`overview.tex:188`) -> "Log canonical fourfold termination" (`overview.tex:188`) [056:3]
- claimed: 056:1 056:3
- unclaimed: 056:2 056:4 056:5
- note: 056:2 is the generalized-**canonical** (terminal) flip case, which the abstract does not state
  as a separate clause; 056:4 and 056:5 are the two "finite ordinary minimal model programs" manuscripts,
  also unstated.

## 068 · `overview.tex:210` · n=7 · T0

- main: "If $X$ is a smooth connected complex projective variety and $-K_X$ admits a smooth Hermitian metric with nonnegative curvature, then $H^0(X,-mK_X)\ne0$ for some $m>0$." (`overview.tex:210`) -> "Smooth semipositivity" (`overview.tex:210`) [068:1]
- clause: "Thus smooth semipositivity forces a nonzero section of a positive tensor power of the anticanonical bundle in every dimension." (`overview.tex:210`) -> unmatched
- claimed: 068:1
- unclaimed: 068:2 068:3 068:4 068:5 068:6 068:7
- note: The second sentence restates the headline with the dimension uniformity made explicit, so it is
  recorded unmatched rather than paired to a companion. Six manuscripts (invariant indices, bounded
  metrics on klt pairs, cohomological transfer, metric descent, integrable metrics with controlled
  boundary, exact orders) ship with no clause at all — the most companion-heavy family in the population.

## 071 · `overview.tex:216` · n=2 · T2

- main: "Resolves the existence part of Koebe's circle-domain conjecture: every domain in the Riemann sphere is conformally equivalent to a domain whose complementary components are round disks or points." (`overview.tex:216`) -> "Koebe’s circle-domain conjecture" (`overview.tex:216`) [071:2]
- clause: "It also proves that circle domains with conformally removable boundary are rigid, meaning every conformal equivalence to another circle domain is M\"obius, establishing this direction of the He--Schramm conjecture." (`overview.tex:216`) -> "Removable boundaries and rigidity" (`overview.tex:216`) [071:1]
- claimed: 071:1 071:2
- unclaimed:

## 088 · `overview.tex:252` · n=2 · T3

- main: "Proves Petty's projection-volume conjecture in the remaining dimensions $n\ge4$: ellipsoids uniquely minimize projection-body volume at fixed body volume." (`overview.tex:252`) -> "Petty’s projection-volume conjecture" (`overview.tex:252`) [088:1]
- clause: "In contrast, products of simplices exceed Brannen's proposed simplex maximum for normalized projection-body volume by an exponential factor in every sufficiently large dimension." (`overview.tex:252`) -> "Product counterexample to simplex maximum" (`overview.tex:252`) [088:2]
- clause: "Also establishes the full Lutwak--Petty projection inequalities." (`overview.tex:252`) -> unmatched
- claimed: 088:1 088:2
- unclaimed:
- note: The Lutwak--Petty inequalities are stated as a result and named by no display title.

## 102 · `overview.tex:282` · n=5 · T3

- main: "Proves Khot's Unique Games Conjecture." (`overview.tex:282`) -> "Unique Games theorem" (`overview.tex:282`) [102:1]
- clause: "Independent direct reductions also establish NP-hardness, on unweighted graphs, of approximation beyond the Goemans--Williamson ratio for Max-Cut" (`overview.tex:282`) -> "Optimal Max-Cut hardness" (`overview.tex:282`) [102:2]
- clause: "below factor two for Vertex Cover" (`overview.tex:282`) -> "Factor-two Vertex Cover hardness" (`overview.tex:282`) [102:3]
- clause: "and within any fixed constant factor for Min-UnCut and directed feedback vertex set." (`overview.tex:282`) -> "Constant-factor Min-UnCut hardness" (`overview.tex:282`) [102:4]
- clause: "and within any fixed constant factor for Min-UnCut and directed feedback vertex set." (`overview.tex:282`) -> "Directed feedback vertex set hardness" (`overview.tex:282`) [102:5]
- claimed: 102:1 102:2 102:3 102:4 102:5
- unclaimed:
- note: One clause names two manuscripts, so it is quoted twice, once per title. This is the family the
  bead's own example names, and the pairing is exact: four of five titles name a clause.


## 113 · `overview.tex:304` · n=2 · T3

- main: "Gives a fully polynomial randomized approximation scheme for counting perfect matchings in arbitrary finite simple graphs, with exact detection of zero counts." (`overview.tex:304`) -> "Perfect-matching FPRAS" (`overview.tex:304`) [113:1]
- clause: "Also proves the perfect-matching entropy conjecture of Anari, Oveis Gharan, and Vinzant, bounding the maximum entropy of a matching law at every feasible edge-marginal vector in a loopless labelled multigraph, including boundary points." (`overview.tex:304`) -> "Entropy and face dimension" (`overview.tex:304`) [113:2]
- claimed: 113:1 113:2
- unclaimed:

## 114 · `overview.tex:306` · n=2 · T3

- main: "Gives a fully polynomial randomized approximation scheme for counting common integer bases of two integral polymatroids of equal total rank, supplied by exact rank-value oracles." (`overview.tex:306`) -> "An FPRAS for Common Integer Polymatroid Bases with Binary Capacities" (`overview.tex:306`) [114:1]
- clause: "For matroids presented by independence oracles, the results also cover common independent sets of prescribed, unrestricted, or maximum cardinality, even when the ranks differ." (`overview.tex:306`) -> "Approximate counting of common bases of two matroids" (`overview.tex:306`) [114:2]
- claimed: 114:1 114:2
- unclaimed:
- note: Probe hit only — the `independ` match is "independence oracles", a presentation of the input,
  not multi-claim language.

## 119 · `overview.tex:316` · n=2 · T3

- main: "Proves the Courtade--Kumar conjecture: among Boolean functions of independent uniform bits, a single coordinate retains the most mutual information after independent bit-flip noise." (`overview.tex:316`) -> "Sharp binary-information contraction" (`overview.tex:316`) [119:1]
- clause: "The Hellinger conjecture is also proved for every Boolean output bias and noise correlation." (`overview.tex:316`) -> "Arbitrary-bias Hellinger contraction" (`overview.tex:316`) [119:2]
- clause: "A stronger theorem treats randomized binary summaries at fixed initial information." (`overview.tex:316`) -> unmatched
- claimed: 119:1 119:2
- unclaimed:
- note: The strengthening has no display title of its own; it is the theorem inside 119:1.

## 122 · `overview.tex:322` · n=3 · T2

- main: "At every fixed deletion probability in $(0,1)$, reconstructing an arbitrary length-$n$ binary string requires $n^{\Omega(\log\log n)}$ independent traces, ruling out polynomial-sample reconstruction." (`overview.tex:322`) -> "Quantitative lower bounds for trace reconstruction" (`overview.tex:322`) [122:3]
- clause: "A uniform decoder achieves quasipolynomial sample and running-time bounds for known fixed rational retention probabilities." (`overview.tex:322`) -> "Uniform quasipolynomial-time trace reconstruction" (`overview.tex:322`) [122:1]
- clause: "When the deletion probability is at most $n^{-\varepsilon}$ for fixed $\varepsilon>0$, both bounds become polynomial in the input and parameter encoding." (`overview.tex:322`) -> "A latest-anchor induction with spectrally compact masks for worst-case trace reconstruction" (`overview.tex:322`) [122:2]
- claimed: 122:1 122:2 122:3
- unclaimed:
- note: The 122:2 pairing is the weakest call on this page — the title names a technique
  (latest-anchor induction, spectrally compact masks) and the clause names a regime, so they match on
  subject, not on wording. Probe hit only: "independent traces" is the sample model.

## 129 · `overview.tex:335` · n=2 · T3

- main: "Proves exponential lower bounds both for complementing two-way nondeterministic finite automata" (`overview.tex:335`) -> "Nondeterministic complementation lower bound" (`overview.tex:335`) [129:1]
- clause: "and for simulating one-way nondeterministic automata by two-way deterministic ones." (`overview.tex:335`) -> "Two-way deterministic state lower bound" (`overview.tex:335`) [129:2]
- clause: "The latter resolves the Sakoda--Sipser state-succinctness conjecture over growing finite alphabets" (`overview.tex:335`) -> unmatched
- claimed: 129:1 129:2
- unclaimed:
- note: The headline is one "both … and …" sentence split across the two titles. The Sakoda--Sipser
  attribution is stated as a consequence and named by no title. Probe hit only: "independent of
  alphabet size".

## 134 · `overview.tex:345` · n=3 · T2

- main: "Every regular language over a finite alphabet has a generalized regular expression with at most three nested Kleene stars, allowing union, concatenation and complement over the same alphabet." (`overview.tex:345`) -> "Star height at most three" (`overview.tex:345`) [134:3]
- clause: "This establishes an absolute bound independent of automaton size, resolving the uniform-boundedness version of the generalized star-height problem." (`overview.tex:345`) -> unmatched
- claimed: 134:3
- unclaimed: 134:1 134:2
- note: The second sentence restates the headline as a uniformity statement, so it is unmatched.
  "Star height at most four" is the earlier, weaker rung and "Finite-monoid computations" the method;
  neither is stated. Probe hit only: "independent of automaton size".

## 157 · `overview.tex:395` · n=3 · T3

- main: "Disproves Hadwiger's conjecture even for fractional coloring: arbitrarily large finite simple graphs with independence number at most two satisfy $\chi_f(G)>h(G)$, where $h(G)$ is the largest clique-minor order." (`overview.tex:395`) -> "Hadwiger counterexample" (`overview.tex:395`) [157:1]
- clause: "Also disproves the fractional Colin de Verdi\`ere chromatic bound $\chi_f(G)\le\mu(G)+1$." (`overview.tex:395`) -> "Colin de Verdière counterexample" (`overview.tex:395`) [157:2]
- clause: "In the positive direction, every finite nonempty graph satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$ for a universal constant $C$." (`overview.tex:395`) -> "Linear list-coloring bound" (`overview.tex:395`) [157:3]
- claimed: 157:1 157:2 157:3
- unclaimed:
- note: Probe hit only: "independence number".

## 170 · `overview.tex:419` · n=2 · T2

- main: "For every fixed integer $s\ge5$, proves $r(s,t)=t^{s-1}/(\log t)^{s-2+o(1)}$ as $t\to\infty$, determining the logarithmic exponent and matching the classical upper bound at that scale." (`overview.tex:419`) -> "Fixed off-diagonal Ramsey numbers" (`overview.tex:419`) [170:2]
- claimed: 170:2
- unclaimed: 170:1
- note: "$r(5,t)$ logarithmic exponent" is the $s=5$ instance of the general clause; the abstract
  states no clause naming it. Probe hit only: "independent set".

## 184 · `overview.tex:447` · n=2 · T3

- main: "Proves the Alon--Krivelevich--Sudakov coloring conjecture in correspondence-coloring form: graphs avoiding any fixed subgraph $F$ need $O_F(\Delta/\log\Delta)$ colors when their maximum degree $\Delta$ is sufficiently large." (`overview.tex:447`) -> "Correspondence coloring graphs with a forbidden clique" (`overview.tex:447`) [184:1]
- clause: "Also proves the Ajtai--Erd\H{o}s--Koml\'os--Szemer\'edi independence conjecture: for fixed $r\ge4$, every $n$-vertex $K_r$-free graph of average degree $d\ge2$ has an independent set of size $\Omega_r(n\log d/d)$." (`overview.tex:447`) -> "A logarithmic independence bound for clique-free graphs" (`overview.tex:447`) [184:2]
- claimed: 184:1 184:2
- unclaimed:

## 203 · `overview.tex:487` · n=2 · T0

- main: "Proves Donovan's conjecture: over each fixed algebraically closed field of characteristic $p$, blocks of finite groups with bounded defect-group order have only finitely many Morita-equivalence classes, for every prime $p$." (`overview.tex:487`) -> "Donovan over algebraically closed fields" (`overview.tex:487`) [203:1]
- clause: "Also proves the integral form over each fixed complete mixed-characteristic discrete valuation ring with algebraically closed residue field." (`overview.tex:487`) -> "Integral Donovan over Witt vectors" (`overview.tex:487`) [203:2]
- claimed: 203:1 203:2
- unclaimed:

## 210 · `overview.tex:501` · n=2 · T3

- main: "Proves the sixth case of Foulkes’ conjecture: $\operatorname{Sym}^6(\operatorname{Sym}^bV)$ embeds equivariantly in $\operatorname{Sym}^b(\operatorname{Sym}^6V)$ for every $b\ge6$ and finite-dimensional complex $V$." (`overview.tex:501`) -> "Sixth symmetric power" (`overview.tex:501`) [210:1]
- clause: "More generally, the canonical multiplication map $\operatorname{Sym}^b(\operatorname{Sym}^aV)\to\operatorname{Sym}^a(\operatorname{Sym}^bV)$ is surjective for $a\ge2$ and $b\ge a(a-1)$, giving dimension-independent quadratic stabilization." (`overview.tex:501`) -> "Quadratic stabilization" (`overview.tex:501`) [210:2]
- claimed: 210:1 210:2
- unclaimed:
- note: Probe hit only: "dimension-independent".

## 211 · `overview.tex:505` · n=7 · T2

- main: "Critical Fortuin--Kasteleyn planar maps converge to Liouville quantum gravity spheres for $0<q\le4$" (`overview.tex:505`) -> "Critical sphere at $q=4$" (`overview.tex:505`) [211:5]
- clause: "and to the Brownian continuum random tree for $q>4$, establishing the surface-to-tree geometric transition." (`overview.tex:505`) -> "Brownian CRT limits for $q>4$" (`overview.tex:505`) [211:7]
- clause: "For FK--Ising and spanning-tree-weighted maps, stationary random walks converge to Liouville Brownian motion on the limiting sphere." (`overview.tex:505`) -> "Random Walks on Critical FK--Ising Maps and Liouville Brownian Motion" (`overview.tex:505`) [211:1]
- clause: "The FK--Ising spectral result also gives convergence of eigenvalues and heat traces, using the stated Brownian/LQG inputs." (`overview.tex:505`) -> "Spectral convergence for critical FK--Ising planar maps" (`overview.tex:505`) [211:2]
- claimed: 211:1 211:2 211:5 211:7
- unclaimed: 211:3 211:4 211:6
- note: The headline is a two-case sentence; each half is paired with the title naming that case. The
  linear-clock manuscript, the subcritical conformal limits, and the metric-measure limits ship with no
  clause. This family is one of the bead's densest targets and has **no probe hit** — its multi-claim
  language is "also gives", which the bead's vocabulary does not list.


## 213 · `overview.tex:509` · n=2 · T3

- main: "Resolves the Benjamini--Schramm criticality conjecture for bond percolation on every infinite connected locally finite quasi-transitive graph with $p_c<1$: at the critical probability, there is almost surely no infinite cluster." (`overview.tex:509`) -> "Quasi-transitive graphs at criticality" (`overview.tex:509`) [213:2]
- clause: "The family also establishes this conclusion for both nearest-neighbor bond and site percolation on $\mathbb Z^3$." (`overview.tex:509`) -> "Cubic-lattice bond and site percolation" (`overview.tex:509`) [213:1]
- claimed: 213:1 213:2
- unclaimed:

## 215 · `overview.tex:513` · n=5 · T3

- main: "Constructs the canonical continuum limit of the two-dimensional nearest-neighbor $O(3)$ model: a non-Gaussian local relativistic theory with a unique vacuum and a positive mass gap." (`overview.tex:513`) -> "O(3) massive continuum limit" (`overview.tex:513`) [215:1]
- clause: "For the square-lattice $O(4)$ model, determines the exact leading asymptotic of the full transfer gap, $m_{\mathrm{lat}}(\beta)\sim32e^{\pi/4-1/2}\sqrt\beta\,e^{-\pi\beta}$." (`overview.tex:513`) -> "Exact mass asymptotics for the two-dimensional $O(4)$ lattice model" (`overview.tex:513`) [215:3]
- clause: "The family also proves exponential spin-correlation decay for two-dimensional nearest-neighbor $O(n)$ models with $n\ge3$ at every positive temperature." (`overview.tex:513`) -> "O(n) exponential decay" (`overview.tex:513`) [215:5]
- claimed: 215:1 215:3 215:5
- unclaimed: 215:2 215:4
- note: "O(3) isolated particle pole" and "O(4) mass bounds" ship with no clause; the mass-gap phrase in
  the headline is the closest the abstract comes to either.

## 227 · `overview.tex:537` · n=8 · T3

- main: "For zero-field Gaussian SK heat-bath dynamics with rate-one updates per spin, proves worst-start cutoff on the $\log n$ scale for fixed $0\le\beta<1$" (`overview.tex:537`) -> "High-temperature cutoff" (`overview.tex:537`) [227:4]
- clause: "mixing time $n^{2/3+o(1)}$ at $\beta=1$" (`overview.tex:537`) -> "Critical mixing" (`overview.tex:537`) [227:8]
- clause: "and stretched-exponential mixing from a Gibbs-sampled fixed starting configuration for $\beta>1$, in probability over disorder." (`overview.tex:537`) -> "Typical-start stretched-exponential barriers" (`overview.tex:537`) [227:6]
- clause: "At criticality, rescaled stationary and quench autocorrelation processes have universal random limits for Gaussian and Rademacher disorder; the quench limit relaxes to the stationary limit." (`overview.tex:537`) -> "Universality of critical quench autocorrelations in the Sherrington--Kirkpatrick model" (`overview.tex:537`) [227:1]
- claimed: 227:1 227:4 227:6 227:8
- unclaimed: 227:2 227:3 227:5 227:7
- note: The headline is a three-regime sentence ($\beta<1$, $\beta=1$, $\beta>1$) and each regime has a
  title, so the pairing is unusually clean for a family with no probe hit. The autocorrelation clause is
  an umbrella over 227:1 and 227:2 ("Functional universality"), so it is paired to the quench title and
  227:2 is left unclaimed. The spectral-gap, critical-slowing-down, and low-temperature-upper-bound
  manuscripts carry no clause.

## 235 · `overview.tex:553` · n=4 · T2

- main: "For random $k$-SAT with independent uniformly signed proper clauses sampled with replacement, proves finite positive limiting thresholds" (`overview.tex:553`) -> "Fixed-clause-size limiting threshold" (`overview.tex:553`) [235:1]
- clause: "and hitting-time variance $\Theta_k(n)$ for every fixed $k\ge3$" (`overview.tex:553`) -> "Random k-SAT hitting-time variance" (`overview.tex:553`) [235:3]
- clause: "and computability of the 3-SAT threshold." (`overview.tex:553`) -> "Computing the random 3-SAT threshold" (`overview.tex:553`) [235:4]
- claimed: 235:1 235:3 235:4
- unclaimed: 235:2
- note: "Linear Variance of the Random 3-SAT Hitting Time" is the $k=3$ instance of the variance clause.
  The abstract also carries a priority credit — "We credit Gaia Carenini with priority for resolving the
  threshold-existence conjecture in her concurrent … ECCC TR26-229" — pointing at an **external** report,
  not a manuscript in this family; it is the only abstract in the population that cites outside the
  release. Probe hit only: "independent uniformly signed".

## 237 · `overview.tex:557` · n=13 · T3

- main: "Proves the diameter form of Nienhuis's predicted three-quarter exponent: a uniformly chosen $n$-step self-avoiding walk on the honeycomb lattice has diameter $n^{3/4+o(1)}$." (`overview.tex:557`) -> unmatched
- clause: "Its local mass and covering numbers have exponent $4/3$." (`overview.tex:557`) -> "Mass and covering exponents for fixed-length walks" (`overview.tex:557`) [237:4]
- clause: "These estimates hold at every sufficiently large fixed length, simultaneously across scales, with arbitrarily high polynomial probability." (`overview.tex:557`) -> unmatched
- claimed: 237:4
- unclaimed: 237:1 237:2 237:3 237:5 237:6 237:7 237:8 237:9 237:10 237:11 237:12 237:13
- note: The worst pairing in the population. The third-densest family (13 manuscripts) states a headline
  that **no** display title names — none of the thirteen mentions diameter or the three-quarter exponent —
  and twelve of its titles are machinery (radial transfer, chords, cylinder loops, signed propagation,
  bridge windows, vacuum representations, renewal, strip crossings, bridge moments, cap amplitudes).

## 238 · `overview.tex:559` · n=12 · T3

- main: "Proves that the Thorp shuffle randomizes $N=2^d$ labeled cards in $\Theta(\log N)$ physical shuffles, settling its optimal mixing order for power-of-two deck sizes." (`overview.tex:559`) -> "Optimal-order mixing of the Thorp shuffle" (`overview.tex:559`) [238:1]
- clause: "Convergence is in total variation from the worst initial ordering and concerns the entire permutation, not just individual card positions." (`overview.tex:559`) -> unmatched
- claimed: 238:1
- unclaimed: 238:2 238:3 238:4 238:5 238:6 238:7 238:8 238:9 238:10 238:11 238:12
- note: The second sentence strengthens the headline (worst-case start, whole permutation) rather than
  adding a result, so it is unmatched. Eleven companion manuscripts — coordinate frames, Fourier bounds,
  deterministic sweeps, revealed switching, routing, row–column symmetry, subspace tests, compatibility
  entropy, tensor densities, conditional sweeps, a permanent inequality — have no clause.

## 239 · `overview.tex:561` · n=2 · T0

- main: "Determines the sharp exponential singularity rate of symmetric random sign matrices with independent entries on and above the diagonal." (`overview.tex:561`) -> "The sharp exponential rate of singularity for symmetric Bernoulli matrices" (`overview.tex:561`) [239:1]
- clause: "for fixed bias $p\in(0,1)\setminus\{1/2\}$, the rate is $(p^2+(1-p)^2+o(1))^n$." (`overview.tex:561`) -> "The sharp singularity rate for biased symmetric sign matrices" (`overview.tex:561`) [239:2]
- clause: "In the biased case, agreeing rows attain this rate." (`overview.tex:561`) -> unmatched
- claimed: 239:1 239:2
- unclaimed:
- note: The headline sentence covers the uniform case, which the next sentence states numerically. Probe
  hit only: "independent entries".

## 258 · `overview.tex:603` · n=2 · T0

- main: "Proves Gersten's conjecture: every finitely generated one-relator group containing no Baumslag--Solitar subgroup $\mathrm{BS}(m,n)$, with $m,n\ne0$, is word-hyperbolic." (`overview.tex:603`) -> "Baumslag–Solitar-free one-relator groups" (`overview.tex:603`) [258:1]
- clause: "It also proves that every word-hyperbolic one-relator group is virtually compact special." (`overview.tex:603`) -> "Virtual compact specialness" (`overview.tex:603`) [258:2]
- claimed: 258:1 258:2
- unclaimed:

## 260 · `overview.tex:609` · n=13 · T2

- main: "Proves the sharp enclosing-area spacetime Penrose inequality for smooth one-ended asymptotically flat initial data in every spatial dimension $n\ge3$, under dominant energy, weak future trapping, positive enclosing area, and the stated decay assumptions." (`overview.tex:609`) -> "Numerical spacetime" (`overview.tex:609`) [260:9]
- clause: "It bounds invariant ADM mass below using minimum enclosing area, with equality rigidity under additional horizon hypotheses." (`overview.tex:609`) -> "Equality and rigidity" (`overview.tex:609`) [260:11]
- clause: "Charged upper-area bounds treat dyonic three-dimensional data;" (`overview.tex:609`) -> "Three-dimensional charged inequality" (`overview.tex:609`) [260:1]
- clause: "the higher-dimensional purely electric extension uses the matched neutral theorem." (`overview.tex:609`) -> "Higher-dimensional charged reduction" (`overview.tex:609`) [260:2]
- claimed: 260:1 260:2 260:9 260:11
- unclaimed: 260:3 260:4 260:5 260:6 260:7 260:8 260:10 260:12 260:13
- note: The densest family in the population after 034. Nine unclaimed titles name settings the abstract
  does not mention at all — Kerr–Newman, electromagnetic tails, nonmaximal anti-de Sitter, asymptotically
  hyperbolic, local Schwarzschild–anti-de Sitter, the Riemannian endpoint, boundary graphs, and the
  Bondi/CKS class — so this family's abstract under-describes its own shelf.

## 261 · `overview.tex:611` · n=2 · T2

- main: "In dimension two, every positive disorder strength gives almost surely pure-point spectrum." (`overview.tex:611`) -> "Pure-point spectrum" (`overview.tex:611`) [261:2]
- clause: "In every fixed dimension $d\ge3$, sufficiently weak positive disorder gives purely absolutely continuous spectrum on a fixed open interval with nonzero spectral weight." (`overview.tex:611`) -> "Absolutely continuous spectrum" (`overview.tex:611`) [261:1]
- clause: "Resolves the predicted spectral contrast for the lattice Anderson model with independent uniform site potentials." (`overview.tex:611`) -> unmatched
- claimed: 261:1 261:2
- unclaimed:
- note: The first sentence is the umbrella over both titles, so it is recorded unmatched and the two
  case sentences carry the pairing. Probe hit only: "independent uniform site potentials".

## 262 · `overview.tex:613` · n=3 · T3

- main: "Proves the sharp one-dimensional Lieb--Thirring inequality for $1/2<\gamma<3/2$ and arbitrary finite-matrix potentials $W\ge0$ with $\int\operatorname{tr}(W^{\gamma+1/2})<\infty$" (`overview.tex:613`) -> "Sharp one-dimensional Lieb--Thirring inequalities for matrix potentials" (`overview.tex:613`) [262:2]
- clause: "the optimal constant is the scalar one-bound-state value, independent of matrix size." (`overview.tex:613`) -> "Sharp one-dimensional Lieb–Thirring constants" (`overview.tex:613`) [262:3]
- clause: "All equality cases are direct sums, in one constant unitary basis, of scalar $\operatorname{sech}^2$ solitons with independent scales and centers, and zero channels." (`overview.tex:613`) -> "Equality cases in the sharp one-dimensional matrix Lieb--Thirring inequality" (`overview.tex:613`) [262:1]
- claimed: 262:1 262:2 262:3
- unclaimed:
- note: Probe hit only ("independent of matrix size", "independent scales"). The three display titles are
  not encoded consistently: 262:1 and 262:2 carry `Lieb--Thirring` (source dashes) while 262:3 carries
  `Lieb–Thirring` (en dash), so a normalized title string is not verbatim on the line.


## 266 · `overview.tex:621` · n=2 · T2

- main: "Proves $N(6)=3$, resolving Zauner\textquotesingle s dimension-six mutually unbiased bases conjecture: three such bases exist in $\mathbb C^6$, but four cannot." (`overview.tex:621`) -> "Maximum number of bases" (`overview.tex:621`) [266:1]
- clause: "An independent companion proves the Matolcsi--Ruzsa--Weiner Fourier-vanishing conjecture for order-six complex Hadamard matrices outside Tao\textquotesingle s cubic equivalence class." (`overview.tex:621`) -> "Exact Fourier certificates" (`overview.tex:621`) [266:2]
- claimed: 266:1 266:2
- unclaimed:
- note: The one probe hit in the population that **is** multi-claim language: "An independent companion
  proves" announces a second result, which is exactly what the probe was meant to find.

## 267 · `overview.tex:623` · n=5 · T2

- main: "Proves Bose--Einstein condensation for the exact canonical Gibbs state of the three-dimensional hard-sphere gas: each fixed exclusion distance and sufficiently small fixed density admit a strictly positive temperature, independent of volume, with positive condensate fraction in the thermodynamic limit." (`overview.tex:623`) -> "Bose--Einstein condensation at positive temperature in the dilute hard-sphere gas" (`overview.tex:623`) [267:1]
- clause: "At zero temperature, proves the Bogoliubov leading quantum-depletion law for hard spheres and fixed bounded nonnegative radial finite-range potentials of positive scattering length, taking the thermodynamic limit before the dilute limit." (`overview.tex:623`) -> "Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas" (`overview.tex:623`) [267:2]
- clause: "At zero temperature, proves the Bogoliubov leading quantum-depletion law for hard spheres and fixed bounded nonnegative radial finite-range potentials of positive scattering length, taking the thermodynamic limit before the dilute limit." (`overview.tex:623`) -> "Quantum Depletion for Fixed Bounded Repulsive Potentials" (`overview.tex:623`) [267:3]
- claimed: 267:1 267:2 267:3
- unclaimed: 267:4 267:5
- note: One clause names two manuscripts (hard spheres, then general repulsive potentials), so it is
  quoted twice. "A density-uniform condensate bound for dilute Bose gases" and "Ground-state condensation
  in the dilute hard-sphere gas" carry no clause. Probe hit only: "independent of volume".

## 271 · `overview.tex:631` · n=4 · T2

- main: "Proves Bloch's $T^{3/2}$ law with its exact coefficient for three-dimensional quantum Heisenberg ferromagnets at every positive quantum spin, allowing nonnegative symmetric finite-range couplings whose support generates $\mathbb Z^3$." (`overview.tex:631`) -> "Bloch's Law for Finite-Range Heisenberg Ferromagnets in Three Dimensions" (`overview.tex:631`) [271:1]
- clause: "The family also proves spontaneous magnetization for nearest-neighbor models in every dimension $d\ge3$" (`overview.tex:631`) -> "Spontaneous magnetization in the quantum Heisenberg ferromagnet" (`overview.tex:631`) [271:4]
- clause: "and determines the first lattice correction for three-dimensional nearest-neighbor couplings." (`overview.tex:631`) -> "The first lattice correction to Bloch's law" (`overview.tex:631`) [271:2]
- claimed: 271:1 271:2 271:4
- unclaimed: 271:3
- note: The "also proves … and determines …" sentence splits cleanly into two results. "The spherical
  magnetization law for the three-dimensional quantum Heisenberg ferromagnet" carries no clause.

## 281 · `overview.tex:651` · n=2 · T2

- main: "Proves that QAOA approaches the ground-state energy of the Gaussian zero-field Sherrington--Kirkpatrick model when system size tends to infinity before circuit depth." (`overview.tex:651`) -> "QAOA attains the SK ground-state energy in the thermodynamic-first limit" (`overview.tex:651`) [281:1]
- clause: "This also yields leading-order optimal expected MaxCut values on large-degree random regular graphs, with size tending to infinity before degree." (`overview.tex:651`) -> unmatched
- claimed: 281:1
- unclaimed: 281:2
- note: The MaxCut consequence is stated as a result and named by no display title.
  "Full support of the zero-temperature Sherrington-Kirkpatrick order parameter" carries no clause.
  Probe hit only: "independent of size and disorder".

## 291 · `overview.tex:674` · n=4 · T3

- main: "Proves equivariant Jiang--Su stability for every countable discrete amenable group action on a simple separable unital infinite-dimensional nuclear stably finite Jiang--Su-stable $C^*$-algebra, resolving this case of Szab\'o's conjecture without restrictions on trace dynamics." (`overview.tex:674`) -> "Equivariant Jiang--Su Stability for Amenable Actions in the Unital Stably Finite Case" (`overview.tex:674`) [291:1]
- clause: "The family also proves the unital Toms--Winter conjecture, equating strict comparison, finite nuclear dimension and Jiang--Su stability in the simple separable unital infinite-dimensional nuclear setting." (`overview.tex:674`) -> "Nuclear dimension and Jiang–Su stability" (`overview.tex:674`) [291:3]
- claimed: 291:1 291:3
- unclaimed: 291:2 291:4
- note: "Cuntz comparison and absorption" and "Uniform property $\Gamma$" carry no clause. The two
  Jiang--Su titles are encoded differently: 291:1 uses source dashes and capitalises "Stability", 291:3
  uses an en dash and lowercase "stability".

## 325 · `overview.tex:746` · n=2 · T3

- main: "Resolves the complete Crouzeix conjecture: for every bounded operator $A$ on a complex Hilbert space and every finite matrix-valued polynomial $P$, one has $\lVert P[A]\rVert\le2\sup_{z\in W(A)}\lVert P(z)\rVert$, where $W(A)$ is the numerical range." (`overview.tex:746`) -> "Structural proof" (`overview.tex:746`) [325:2]
- clause: "The constant $2$ is sharp, independent of the matrix size, and valid in infinite dimensions." (`overview.tex:746`) -> unmatched
- claimed: 325:2
- unclaimed: 325:1
- note: The family ships **two proofs of one theorem**, so its display titles name a method
  ("Direct proof", "Structural proof") rather than a sub-finding; the pairing is degenerate by
  construction. Probe hit only: "independent of the matrix size".

## 335 · `overview.tex:768` · n=2 · T0

- main: "Proves $\int_M(\mathrm{Scal}_g^-)^{n/2}\,dV_g\ge a_n\lVert M\rVert$ for every closed connected oriented smooth $n$-manifold, $n\ge3$, and every smooth metric, with $a_n>0$ depending only on dimension." (`overview.tex:768`) -> "An integral scalar curvature bound for real simplicial volume" (`overview.tex:768`) [335:1]
- clause: "Also proves rational inessentiality under positive scalar curvature, resolving the Gromov--Lawson conjecture; every nonnegative-scalar-curvature metric on a closed aspherical manifold is flat." (`overview.tex:768`) -> "Positive scalar curvature forces rational inessentiality" (`overview.tex:768`) [335:2]
- claimed: 335:1 335:2
- unclaimed:

## 337 · `overview.tex:772` · n=2 · T2

- main: "Proves generalized Cartan--Hadamard isoperimetry in every dimension: in a complete simply connected manifold with sectional curvature at most $\kappa\le0$, every finite-volume finite-perimeter set satisfies the sharp comparison with the equal-volume model ball." (`overview.tex:772`) -> "Cartan–Hadamard isoperimetry and rigidity" (`overview.tex:772`) [337:1]
- clause: "Bounded positive-volume equality regions for $\kappa=0$ are Euclidean balls." (`overview.tex:772`) -> unmatched
- clause: "Also proves sharp Euclidean filling bounds for compactly supported integral $n$-cycles, $n\ge2$, in arbitrary proper CAT$(0)$ spaces." (`overview.tex:772`) -> "Sharp integral fillings in CAT(0) spaces" (`overview.tex:772`) [337:2]
- claimed: 337:1 337:2
- unclaimed:
- note: The rigidity clause is unmatched because 337:1's single title names both halves of the headline
  ("isoperimetry **and rigidity**"), so pairing the equality case to it would duplicate a claimed title.

## 346 · `overview.tex:790` · n=2 · T0

- main: "Proves that every stationary integral $m$-varifold in a Euclidean open set has singular set of Hausdorff dimension at most $m-1$, a sharp bound in every positive dimension and codimension." (`overview.tex:790`) -> "A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold" (`overview.tex:790`) [346:1]
- clause: "On round spheres, the family also proves almost-everywhere regularity: the singular set has zero $m$-dimensional Hausdorff measure." (`overview.tex:790`) -> "Almost-everywhere regularity of stationary integral varifolds" (`overview.tex:790`) [346:2]
- claimed: 346:1 346:2
- unclaimed:

## 361 · `overview.tex:820` · n=2 · T3

- main: "Disproves Yau's proposed Euclidean dimension bound for harmonic functions of integer growth on manifolds with nonnegative Ricci curvature." (`overview.tex:820`) -> unmatched
- clause: "For every sufficiently large integer $k$, a complete smooth metric on $\mathbb R^3$ has at least $(k+2)^2$ independent harmonic functions of growth at most $k$, exceeding the Euclidean count $(k+1)^2$." (`overview.tex:820`) -> "Three-dimensional counterexample" (`overview.tex:820`) [361:2]
- claimed: 361:2
- unclaimed: 361:1
- note: The headline is the disproof, which both manuscripts instantiate; the abstract states only the
  three-dimensional case, so "Even-dimensional counterexample" is claimed by no clause. Probe hit only:
  "independent harmonic functions".

## 376 · `overview.tex:855` · n=9 · T2

- main: "Constructs viscous incompressible flows starting from rest on a fixed flat three-dimensional domain that perform universal computation under smooth external forcing." (`overview.tex:855`) -> "Finite instructions and shear flows" (`overview.tex:855`) [376:1]
- clause: "A terminating compiler turns a Turing machine and input into a finite program for the force, so a designated particle reaches a fixed region exactly when the machine halts." (`overview.tex:855`) -> "Fixed particle test" (`overview.tex:855`) [376:2]
- claimed: 376:1 376:2
- unclaimed: 376:3 376:4 376:5 376:6 376:7 376:8 376:9
- note: One of the bead's densest targets, with **no probe hit**. Seven companions — eventually
  stationary forcing, geometric programs for solenoidal forcing, prefix instructions for incompressible
  flows, rapidly vanishing forcing, velocity-field detection, scalar potentials and slow clocks,
  incompressible box transport — carry no clause.


## Summary

| measure | value |
|---|---|
| families read | 49 |
| manuscripts in the population | 203 |
| sub-finding clause pairs accepted | 62 |
| headline clause pairs accepted | 47 |
| clauses recorded unmatched | 18 |
| titles claimed by a clause | 109 |
| titles claimed by no clause | 94 |
| families with >=1 accepted sub-finding pair | 40 |
| families with >=1 clause recorded unmatched | 17 |
| families with an accepted sub-finding pair and no probe hit | 6 |

## What the pairing shows

- **Most families pair cleanly.** 40 of 49 families have at least one accepted sub-finding pair, and
  109 of the 203 titles are claimed by a clause. The catalog's own link text is a usable index of what
  each family proves, for the families where the abstract was written as a list.
- **The densest families are the worst paired.** 034 states 4 results over 14 manuscripts; 238 states 1
  over 12; 237 states 2 over 13 and its headline is named by no title; 260 states 4 over 13 and nine of
  its titles name settings the abstract never mentions; 376 states 2 over 9. Density and description do
  not track each other — a family ships manuscripts for the proof's machinery, and the abstract states
  only the theorems.
- **Unmatched clauses are a real category, not a failure.** 18 clauses in 17 families state a result no
  display title names: the arbitrary-characteristic case of 014's headline; the umbrella clauses in 016
  (three titles for one $\mathcal A_2$ case), 068, 237, 261, 361; the Milne-mediated consequences in
  032; the $\mathbb Q$ case in 019; the Lutwak--Petty inequalities in 088; the strengthening clauses in
  119, 238, 239; the Sakoda--Sipser attribution in 129; the star-height uniformity in 134; the MaxCut
  consequence in 281; the Crouzeix sharpness in 325; and the CAT$(0)$ rigidity in 337. Recording them is
  the point of the "do not force a pairing" instruction.
- **The probe vocabulary is a floor, not a reading.** 6 families pair sub-findings with no probe hit at
  all (014, 211, 227, 237, 260, 376) — six of the bead's ten named densest targets — because their
  multi-claim language is a second bare declarative sentence with no connective at all: "Over global
  function fields, proves Ramanujan at every place …", "Its local mass and covering numbers have
  exponent $4/3$.", "Charged upper-area bounds treat dyonic three-dimensional data;", "mixing time
  $n^{2/3+o(1)}$ at $\beta=1$", "A terminating compiler turns a Turing machine and input into a finite
  program for the force", and 211's "this also gives", which is the only "also gives" in the set —
  none of it is a phrase the bead's four probes list. 13 of the 40 probe hits are
  technical uses of the same words. A pass that probes only the bead's second list finds nothing, which
  is how the bead's own first probe of this question produced a false negative.
- **A display title is not the manuscript's title.** The `preprints/` directory name carries the full
  manuscript title; the `\href` display text in `overview.tex` is a short label the release chose. They
  agree for some families and not for others ("Maximum number of bases" vs
  `The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026`). Pairing must use
  the display text, and the display text is not consistently encoded: en dash vs `--`, capitalised vs
  lowercase, accent normalised vs raw (`Correspondence coloring graphs …` drops the word
  "clique-free" that the directory name carries).

## Not checked

- No Lean build. `lake`, `lean`, `lake exe cache get`, and the comparator are never run here, so nothing
  on this page says a family's formalization proves the clause it is paired to; `tier` is the ledger's
  formalization tier, read from `notes/catalog.tsv`.
- The pairing is a reading call on the abstract and the link text only. Manuscripts were not opened to
  confirm that a claimed title's paper contains the clause it is paired to, and an unclaimed title's
  paper may well prove a result the abstract omits — 260 and 238 are the cases that make that likely.
- The population rule is provisional. The bead's 51 does not reproduce; the recorded rule yields 49
  families over 203 manuscripts, and the revisit condition is in the population section.
- 118 families with two or more manuscripts are not read. The page covers 49 of the 167.
- The 426 comparator-link rows in `notes/subfindings.tsv` are not paired; only the 719 manuscript rows
  are eligible, and only 203 of those are in this population.
- Clause boundaries were chosen by reading, not by a parser: a clause is a sentence, or a sentence
  fragment when one sentence states two results (039, 227, 271). Two clauses are quoted twice because
  each names two manuscripts (102, 267).


