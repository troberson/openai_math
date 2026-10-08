# Counterexample families outside T0, cross-checked against main_results

## Population

Rule: the ledger's `shapes` column contains `counterexample` **and** the tier is not `T0`. That is
**28** families — **18** at T3 and **10** at T2. The shape rule fires on **44** families overall, so
**16** carry the tag at T0; those are read in `notes/t0-triage.md`, which is why the bead's population
excludes them. Regenerate with `python3 notes/scripts/extract_counterexample_crosscheck.py` —
report-only, it writes nothing and runs nothing, and running it twice and diffing must give an
identical report.

Ledger sums over the 28: **27** `main_results` declarations, **51** comparator configs, **23**
formalized manuscripts out of **50**. Every one of the 28 has a scope note.

`lean/formalization.yaml` carries **185** `main_results` entries over **178** unique configs (one
block, `lean/formalization.yaml:917`). Of the 28 families, **18** have at least one entry and **10**
have none, and the no-entry tier counter reads `{'T2': 10}`: the absence is structural, not a reading
gap — T2 is the tier the release assigns to a family whose scope note links configs that no
`main_results` entry names.

All **27** declarations resolve to a statement line in the file the entry names. **11** of the 27 are
written `theorem main : <Carrier> :=`, so their content is opaque until the carrier is opened; all
**11** carriers resolve, through the declaration file's import closure rather than its directory tree.

Config accounting: the 28 scope notes link **51** distinct configs, **27** of them carry an entry and
**24** carry none. Inside T3 the gap is **11** configs in **7** families; inside T2 it is **13**
configs in all **10** families.

Source-level facts, stated at source level: `lean/formalization.yaml` records `scope: "Partial
progress."`, `automation: methods: [agent]`, `review: status: unchecked`. Nothing here says a
comparator was run, and nothing here says the library elaborates — `lake`, `lean`, and `comparator`
are never invoked in this repo.

## Summary table

Configs = distinct configs the family's scope note links. Entries = `main_results` entries naming one
of them. Gaps = configs with no entry.

| Fam | Tier | Configs | Entries | Gaps | Verdict |
|---|---|---|---|---|---|
| 047 | T3 | 1 | 1 | 0 | entry states the counterexample |
| 072 | T3 | 3 | 3 | 0 | entry states it; two companion entries |
| 095 | T3 | 1 | 1 | 0 | entry states the counterexample |
| 100 | T2 | 3 | 0 | 3 | structural absence |
| 118 | T3 | 1 | 1 | 0 | entry states the counterexample |
| 151 | T2 | 1 | 0 | 1 | structural absence |
| 155 | T3 | 1 | 1 | 0 | entry states the counterexample |
| 157 | T2 | 1 | 0 | 1 | structural absence |
| 161 | T2 | 1 | 0 | 1 | structural absence |
| 162 | T3 | 3 | 2 | 1 | entries state both claims; one gap |
| 172 | T3 | 7 | 2 | 5 | classification and spherical witness; five gaps |
| 185 | T3 | 2 | 1 | 1 | entry states claim 1; one gap |
| 190 | T3 | 1 | 1 | 0 | entry states the counterexample |
| 191 | T2 | 1 | 0 | 1 | structural absence |
| 192 | T2 | 1 | 0 | 1 | structural absence |
| 197 | T3 | 4 | 3 | 1 | three entries state the three claims; one gap |
| 198 | T3 | 2 | 2 | 0 | entry states claim 1; one companion |
| 199 | T3 | 2 | 2 | 0 | entries state claims 1 and 3 |
| 244 | T3 | 2 | 1 | 1 | entry states claim 1; one gap |
| 272 | T2 | 2 | 0 | 2 | structural absence |
| 289 | T2 | 1 | 0 | 1 | structural absence |
| 294 | T3 | 2 | 1 | 1 | entry states claim 1; one gap |
| 297 | T2 | 1 | 0 | 1 | structural absence |
| 323 | T2 | 1 | 0 | 1 | structural absence |
| 329 | T3 | 1 | 1 | 0 | entry states the counterexample |
| 347 | T3 | 1 | 1 | 0 | entry states a degenerate instance |
| 350 | T3 | 3 | 2 | 1 | entries state two forms; one gap |
| 361 | T3 | 1 | 1 | 0 | entry states the counterexample |

## The 18 T3 families

Each block quotes the abstract sentence that carries the counterexample language, the scope-note link
that names the config, the `main_results` entry, the Lean statement the entry's declaration opens
with, and — where the statement is carrier-typed — the carrier definition. Verdicts are readings of
those quotes, not claims that a proof was checked.

### 047 — Complex counterexamples to cancellation and affine fibrations

Claim 1 (`overview.tex:170`) — *"Constructs an integral complex affine fourfold $X\not\cong\mathbb A^4$ with
$X\times\mathbb A^1\cong\mathbb A^5$, disproving affine-space cancellation over $\mathbb C$ in
dimension four."*

Claim 2 (`overview.tex:170`) — *"It also disproves the Dolgachev--Weisfeiler affine-fibration conjecture: smooth surjections
$X\to\mathbb A^1$ and $\mathbb A^5\to\mathbb A^2$ have every residue-field fiber isomorphic to affine
three-space but are not Zariski-locally trivial."*

`ComplexCancellation` — `lean/docs/047.md:17`

`lean/formalization.yaml:1042`
```yaml
    - comparator_config: ComparatorChallenges/ComplexCancellation.json
      declaration: OAI.ComplexCancellation.main
      file: OAI/Algebra/AffineCancellation/Main.lean
```

`lean/OAI/Algebra/AffineCancellation/Main.lean:32`
```lean
theorem main : MainStatement :=
```

`lean/OAI/Algebra/AffineCancellation/Model.lean:20`
```lean
def MainStatement : Prop :=
  Algebra.FiniteType ℂ A ∧ IsDomain A ∧ ringKrullDim A = 4 ∧
  Nonempty (Polynomial A ≃ₐ[ℂ] MvPolynomial (Fin 5) ℂ) ∧
  ¬ Nonempty (A ≃ₐ[ℂ] MvPolynomial (Fin 4) ℂ)
```

Verdict: the carrier states claim 1 — dimension 4, cancellation after one factor, no cancellation
alone. Claim 2 has no linked config at all, so the affine-fibration half of the family has no
formalized counterpart.

### 072 — Brennan's conjecture and a counterexample to Kraetzer's prediction

Claim 1 (`overview.tex:218`) — *"A strict bound $B_b(-1)<1/4$ for bounded univalent functions disproves Kraetzer's
prediction at that parameter."*

`Brennan` — `lean/docs/072.md:22`

`lean/formalization.yaml:986`
```yaml
    - comparator_config: ComparatorChallenges/Brennan.json
      declaration: OAI.Brennan.main_theorem
      file: OAI/Analysis/IntegralMeans/Main.lean
```

`lean/OAI/Analysis/IntegralMeans/Main.lean:10`
```lean
theorem main_theorem : MainStatement := by
```

`lean/OAI/Analysis/IntegralMeans/Model.lean:33`
```lean
def MainStatement : Prop :=
  (∀ ε : ℝ, 0 < ε → ∃ C : ℝ, ∀ f : ℂ → ℂ, Schlicht f →
  ∀ r : ℝ, 1 / 2 ≤ r → r < 1 →
  integralMean f (-2) r ≤ C * (1 - r) ^ (-1 - ε)) ∧
  spectrum (-2) = 1 ∧
  (∀ W : Set ℂ, IsOpen W → IsConnected W → SimplyConnectedSpace W →
  SphericalBoundaryNontrivial W → ∀ φ : ℂ → ℂ,
  DifferentiableOn ℂ φ W → Set.BijOn φ W disk →
  ∀ s : ℝ, 4 / 3 < s → s < 4 →
  IntegrableOn (fun z => ‖deriv φ z‖ ^ s) W volume) ∧
  (∀ f : ℂ → ℂ, UnivalentOn f disk → ∀ t : ℝ,
  -2 < t → t < 2 / 3 →
  IntegrableOn (fun z => ‖deriv f z‖ ^ t) disk volume)
```

`BrennanSharp` — `lean/docs/072.md:23`

`lean/formalization.yaml:990`
```yaml
    - comparator_config: ComparatorChallenges/BrennanSharp.json
      declaration: OAI.Brennan.Sharp.sharp_endpoints
      file: OAI/Analysis/IntegralMeans/SharpEndpoints.lean
```

`lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean:23`
```lean
theorem sharp_endpoints : SharpEndpointStatement := by
```

`lean/OAI/Analysis/IntegralMeans/SharpModel.lean:18`
```lean
def SharpEndpointStatement : Prop :=
  Schlicht koebeMap ∧
  areaMoment koebeMap disk (-2) = ⊤ ∧
  areaMoment koebeMap disk (2 / 3) = ⊤ ∧
  ¬ IntegrableOn (fun z => ‖deriv koebeInverse z‖ ^ (4 : ℝ)) koebeDomain volume ∧
  ¬ IntegrableOn (fun z => ‖deriv koebeInverse z‖ ^ (4 / 3 : ℝ)) koebeDomain volume
```

`StrictMeans` — `lean/docs/072.md:24`

`lean/formalization.yaml:1534`
```yaml
    - comparator_config: ComparatorChallenges/StrictMeans.json
      declaration: OAI.StrictInverseFirstPower.main
      file: OAI/Analysis/StrictMeans/Main.lean
```

`lean/OAI/Analysis/StrictMeans/Main.lean:7`
```lean
theorem main :
  (∃ ε C : ℝ, 0 < ε ∧ ε < 1 / 4 ∧
  ∀ (f : ℂ → ℂ), NormalizedUnivalent f →
  ∀ r : ℝ, 1 / 2 ≤ r → r < 1 →
  integralMean (-1) f r ≤ C * (1 - r) ^ (-(1 / 4 : ℝ) + ε)) ∧
  boundedSpectrum (-1) < (1 / 4 : EReal) ∧
  (¬ ∀ p : ℝ, boundedSpectrum p = kraetzerPrediction p) :=
```

Verdict: `StrictMeans` is the entry that carries the family's counterexample claim — the strict
bound at parameter −1 and the explicit negation of Kraetzer's predicted identity, written without a
carrier. `Brennan` states Brennan's conjecture at parameter −2 (a positive theorem) and
`BrennanSharp` states the sharp endpoints of the Koebe function; neither is the refutation the
abstract's counterexample sentence names.

### 095 — Hyperbolicity cones without semidefinite lifts

Claim 1 (`overview.tex:266`) — *"Disproves the Projected Lax conjecture: some hyperbolicity cones are not spectrahedral
shadows."*

Claim 2 (`overview.tex:266`) — *"This also disproves the generalized Lax conjecture that every hyperbolicity cone is
spectrahedral."*

`HyperbolicCones` — `lean/docs/095.md:15`

`lean/formalization.yaml:1226`
```yaml
    - comparator_config: ComparatorChallenges/HyperbolicCones.json
      declaration: OAI.Paper256.main_result
      file: OAI/Analysis/HyperbolicCones/Main.lean
```

`lean/OAI/Analysis/HyperbolicCones/Main.lean:25`
```lean
theorem main_result :
  Module.finrank ℝ Ambient = 23 ∧
  polynomial.IsHomogeneous 20 ∧
  polynomial.totalDegree = 20 ∧
  MvPolynomial.eval (coordinates basePoint) polynomial = 1 ∧
  (∀ (x : Ambient) (z : ℂ), (linePolynomial x).aeval z = 0 → z.im = 0) ∧
  ∀ (N : ℕ) (_hN : 0 < N) (L : Ambient →ₗ[ℝ] Sym N),
  cone ≠ {x | (L x : Mat N ℝ).PosSemidef} := by
```

Verdict: the final clause is the shadow form — no linear image of a positive-semidefinite slice
equals the cone — so the entry states claim 1. Claim 2's stronger form (not spectrahedral) is not
what the statement says; the statement's cone is a specific 23-dimensional, degree-20 example.

### 118 — Unbounded bin-packing gaps and the modified integer round-up conjecture

Claim 1 (`overview.tex:314`) — *"Disproves the modified integer round-up conjecture of Scheithauer and Terno: the integral
bin-packing optimum can exceed its configuration linear-programming value by an arbitrarily large
additive constant."*

`BinPackingGap` — `lean/docs/118.md:15`

`lean/formalization.yaml:954`
```yaml
    - comparator_config: ComparatorChallenges/BinPackingGap.json
      declaration: OAI.BinPackingGap.main_results
      file: OAI/Computability/BinPacking/Main.lean
```

`lean/OAI/Computability/BinPacking/Main.lean:7`
```lean
theorem main_results :
  (∀ c : ℕ, ∃ I : Instance, ∃ B : ℕ,
  I.n = 5 * B ∧
  (∀ i, (1 / 6 : ℚ) < I.size i ∧ I.size i < 1) ∧
  B + c < opt I ∧ individualLP I = (B : ℝ) ∧ typeLP I = (B : ℝ)) ∧
  (∀ c : Nat, PackingGapNPHard c) ∧
  ((∃ c : Nat, Nonempty (AbsoluteAdditiveAlgorithm c)) ↔ PEqualsNP) ∧
```

Verdict: the first conjunct is claim 1 verbatim in content — for every additive constant `c` an
instance whose integral optimum exceeds its configuration-LP value by more than `c`. The entry also
carries two complexity clauses (NP-hardness of the gap, and an equivalence with P = NP) that the
counterexample sentence does not name.

### 155 — A counterexample to periodic tiling in dimension three

Claim 1 (`overview.tex:391`) — *"Constructs a finite translational tile in $\mathbb Z^3$ that tiles space but admits no
fully periodic tiling, disproving the periodic tiling conjecture in the smallest possible lattice
dimension."*

Claim 2 (`overview.tex:391`) — *"Its unit-cube thickening gives the same counterexample in $\mathbb R^3$, even with
arbitrary real translation vectors."*

`PeriodicTilingThree` — `lean/docs/155.md:15`

`lean/formalization.yaml:1370`
```yaml
    - comparator_config: ComparatorChallenges/PeriodicTilingThree.json
      declaration: OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality
      file: OAI/Geometry/PeriodicTiling/Counterexample.lean
```

`lean/OAI/Geometry/PeriodicTiling/Counterexample.lean:23`
```lean
theorem periodic_tiling_counterexample_and_minimality :
  (∃ T : Finset (Lattice 3), T.Nonempty ∧
  (∃ A : Set (Lattice 3), Tiles T A) ∧
  (∀ A : Set (Lattice 3), Tiles T A → ¬ FullyPeriodic A) ∧
  (∃ A : Set (Space 3), AETiles (Thickening T) A) ∧
  (∀ A : Set (Space 3),
  AETiles (Thickening T) A → ¬ EuclideanFullyPeriodic A)) ∧
  IsLeast {d : ℕ | HasTileWithoutPeriodicComplement d} 3 :=
```

Verdict: one entry states both claims — the lattice conjuncts are claim 1, the `Thickening`/`Space 3`
conjuncts are claim 2, and `IsLeast … 3` is the minimality the blurb calls "the smallest possible
lattice dimension".

### 162 — Counterexamples to Ryser's covering and Gyárfás's tree-cover conjectures

Claim 1 (`overview.tex:405`) — *"Disproves Ryser's covering conjecture by constructing intersecting $(q+1)$-partite,
$(q+1)$-uniform hypergraphs with covering number $q+1$, rather than the predicted bound $q$, for
every sufficiently large prime $q$."*

Claim 2 (`overview.tex:405`) — *"A separate construction over extension fields also disproves Gy\'arf\'as's monochromatic
tree-cover conjecture."*

`BalancedRyser` — `lean/docs/162.md:18` — no `main_results` entry.

`RyserCovering` — `lean/docs/162.md:19`

`lean/formalization.yaml:1470`
```yaml
    - comparator_config: ComparatorChallenges/RyserCovering.json
      declaration: OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank
      file: OAI/Combinatorics/Ryser/Construction/Main.lean
```

`lean/OAI/Combinatorics/Ryser/Construction/Main.lean:14`
```lean
theorem exists_prime_eventually_counterexampleRank :
  ∃ p : ℕ, p.Prime ∧ 5 < p ∧ p % 3 = 2 ∧
  ∃ N : ℕ, ∀ n : ℕ, N ≤ n → n.Prime → 2 < n →
  CounterexampleRank (p ^ n + 1) := by
```

`RyserOddExtensions` — `lean/docs/162.md:20`

`lean/formalization.yaml:1474`
```yaml
    - comparator_config: ComparatorChallenges/RyserOddExtensions.json
      declaration: OAI.RyserOdd.eventualOddFailures_and_infinite
      file: OAI/Combinatorics/Ryser/OddExtensions.lean
```

`lean/OAI/Combinatorics/Ryser/OddExtensions.lean:132`
```lean
theorem eventualOddFailures_and_infinite :
  (∃ primeThreshold : ℕ, ∀ prime : ℕ, primeThreshold ≤ prime →
  prime.Prime → prime % 3 = 2 →
  ∃ degreeThreshold : ℕ, 3 ≤ degreeThreshold ∧
  ∀ degree : ℕ, degreeThreshold ≤ degree → Odd degree →
  Specification.ExplicitFailureAt (prime ^ degree + 1)) ∧
  Set.Infinite {rank : ℕ | Specification.ExplicitFailureAt rank} := by
```

Verdict: `RyserCovering` states claim 1 and `RyserOddExtensions` states claim 2, with one narrowing
each: both statements restrict the prime to residue class 2 modulo 3 (`p % 3 = 2`), while claim 1
says "every sufficiently large prime". `BalancedRyser` — the balanced case the scope note links —
carries no entry.

### 172 — Classification of finite Euclidean Ramsey configurations

Claim 1 (`overview.tex:423`) — *"It also disproves the Leader--Russell--Walters conjecture that every such configuration is
a subset of a finite transitive set."*

`EuclideanRamsey` — `lean/docs/172.md:17`

`lean/formalization.yaml:1150`
```yaml
    - comparator_config: ComparatorChallenges/EuclideanRamsey.json
      declaration: OAI.EuclideanRamsey.classification
      file: OAI/Combinatorics/EuclideanRamsey/Main.lean
```

`lean/OAI/Combinatorics/EuclideanRamsey/Main.lean:69`
```lean
theorem classification {s d : ℕ} (a : Fin s → Space d)
(hs : 2 ≤ s) (hd : 1 ≤ d) (ha : Function.Injective a)
(hspan : affineSpan ℝ (Set.range a) = ⊤) :
Ramsey a ↔ FieldCriterion a :=
```

`GrahamSpherical` — `lean/docs/172.md:18`

`lean/formalization.yaml:1198`
```yaml
    - comparator_config: ComparatorChallenges/GrahamSpherical.json
      declaration: OAI.GrahamSpherical.full_main
      file: OAI/Combinatorics/SphericalRamsey/Main.lean
```

`lean/OAI/Combinatorics/SphericalRamsey/Main.lean:23`
```lean
theorem full_main : Specification.FullAuthoredResult := by
```

`lean/OAI/Combinatorics/SphericalRamsey/Model.lean:58`
```lean
def FullAuthoredResult : Prop :=
  witness.ncard = 12 ∧
  witness ⊆ Metric.sphere (0 : Point 2) 1 ∧
  (∀ n : ℕ, 0 < n → ∃ color : Point n → Fin 50, AvoidsCopy witness color) ∧
  ¬ EuclideanRamsey witness
```

`EuclideanRamseyCircle` — `lean/docs/172.md:19` — no `main_results` entry.
`EuclideanRamseyNine` — `lean/docs/172.md:20` — no `main_results` entry.
`EuclideanRamseyQuadratic` — `lean/docs/172.md:21` — no `main_results` entry.
`EuclideanRamseySpherical` — `lean/docs/172.md:22` — no `main_results` entry.
`EuclideanRamseyTransitive` — `lean/docs/172.md:23` — no `main_results` entry.

Verdict: this is the family where the entry present is not the one carrying the refutation. The
counterexample sentence names the Leader–Russell–Walters conjecture, whose config is
`EuclideanRamseyTransitive`, and that config has no entry. The two entries that do exist are the
positive classification (`Ramsey a ↔ FieldCriterion a`) and a spherical non-Ramsey witness of 12
points on the unit circle. Five of the family's seven linked configs are unformalized.

### 185 — Counterexamples to infinite matroid intersection and packing/covering

Claim 1 (`overview.tex:449`) — *"Disproves the unrestricted infinite matroid intersection and packing/covering conjectures
in ZFC, using two self-dual partitional matroids on a countably infinite ground set."*

Claim 2 (`overview.tex:449`) — *"The same examples answer Jo\'o’s partitional-matroid question negatively."*

`InfiniteMatroid` — `lean/docs/185.md:17`

`lean/formalization.yaml:1246`
```yaml
    - comparator_config: ComparatorChallenges/InfiniteMatroid.json
      declaration: OAI.InfiniteMatroidCounterexample.main
      file: OAI/Combinatorics/InfiniteMatroid/Main.lean
```

`lean/OAI/Combinatorics/InfiniteMatroid/Main.lean:12`
```lean
theorem main :
Countable E ∧ Infinite E ∧
∃ M₀ M₁ : Matroid E,
M₀.E = Set.univ ∧ M₁.E = Set.univ ∧
M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
(∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ Set.univ) ∧
¬ HasPackingCovering M₀ M₁ := by
```

`InfiniteMatroidCorollaries` — `lean/docs/185.md:18` — no `main_results` entry.

Verdict: the entry states claim 1 — countable infinite ground set, two self-dual matroids, no common
independent set covering the ground set, and no packing/covering. Claim 2, the Joó corollary, sits
under `InfiniteMatroidCorollaries`, which has no entry.

### 190 — Polynomial removal fails for ordered binary matrices

Claim 1 (`overview.tex:459`) — *"Disproves polynomial ordered binary matrix removal with one fixed $66\times66$ zero--one
pattern."*

`MatrixRemoval` — `lean/docs/190.md:15`

`lean/formalization.yaml:1326`
```yaml
    - comparator_config: ComparatorChallenges/MatrixRemoval.json
      declaration: OAI.Problem348.no_polynomial_removal_bound
      file: OAI/Combinatorics/MatrixRemoval/Main.lean
```

`lean/OAI/Combinatorics/MatrixRemoval/Main.lean:26`
```lean
theorem no_polynomial_removal_bound :
  ∀ c C : ℝ, 0 < c → 0 < C →
  ∃ n : ℕ, 1 ≤ n ∧
  ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
  ∃ A : BinaryMatrix n,
  fixedDistance A ≥ ε ∧
  (copyCount fixedH A : ℝ) <
  c * Real.rpow ε C * ((n : ℝ) ^ 132) := by
```

Verdict: the entry states claim 1 — for every exponent `C` a matrix at distance ≥ ε whose copy count
is below `c · ε^C · n^132`, so no polynomial removal bound holds for the fixed pattern `fixedH`.

### 197 — Nonsofic groups and group-ring counterexamples

Claim 1 (`overview.tex:475`) — *"Constructs a finitely presented torsion-free nonsofic group whose group algebra over
$\mathbb F_2$ is not directly finite, disproving Kaplansky's conjecture even without torsion."*

Claim 2 (`overview.tex:475`) — *"Companion examples give injective nonsurjective cellular automata on all configurations,
refuting Gottschalk's surjunctivity conjecture."*

Claim 3 (`overview.tex:475`) — *"Another counterexample is an integral group-ring matrix, invertible over the rational group
ring, with Fuglede--Kadison determinant strictly between zero and one, disproving the unrestricted
Determinant Conjecture."*

`GroupRingDeterminant` — `lean/docs/197.md:35`

`lean/formalization.yaml:1206`
```yaml
    - comparator_config: ComparatorChallenges/GroupRingDeterminant.json
      declaration: OAI.GroupRingDeterminant.main
      file: OAI/Analysis/GroupDeterminants/Main.lean
```

`lean/OAI/Analysis/GroupDeterminants/Main.lean:13`
```lean
theorem main : MainStatement := main_of_companion_input companion_input
```

`lean/OAI/Analysis/GroupDeterminants/Model.lean:45`
```lean
def MainStatement : Prop :=
  ∃ (G : Type) (_ : Group G) (_ : Group.FG G) (n : ℕ),
  1 ≤ n ∧ ∃ (A : Matrix (Fin n) (Fin n) (MonoidAlgebra ℤ G))
  (T : Hilbert G n →L[ℂ] Hilbert G n),
  IsUnit (rationalMatrix A) ∧ IsRegularOperator A T ∧ IsUnit T ∧
  0 < fkDet T ∧ fkDet T < 1
```

`KaplanskyDirectFiniteness` — `lean/docs/197.md:34` — no `main_results` entry.

`KaplanskyFinitelyPresented` — `lean/docs/197.md:33`

`lean/formalization.yaml:1266`
```yaml
    - comparator_config: ComparatorChallenges/KaplanskyFinitelyPresented.json
      declaration: OAI.KaplanskyCounterexample.finitelyPresented_counterexample
      file: OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean
```

`lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean:35`
```lean
theorem finitelyPresented_counterexample :
  ∃ (K : Type) (_ : Field K) (_ : Fintype K) (_ : CharP K 2),
  ∃ (G : Type) (_ : Group G) (_ : Group.IsFinitelyPresented G),
  (∃ (ℓ : ℕ) (_ : ℓ.Prime) (_ : Odd ℓ) (g : G), orderOf g = ℓ) ∧
  ∃ a_out b_out : MonoidAlgebra K G, a_out * b_out = 1 ∧ b_out * a_out ≠ 1 :=
```

`OddKaplansky` — `lean/docs/197.md:36`

`lean/formalization.yaml:1350`
```yaml
    - comparator_config: ComparatorChallenges/OddKaplansky.json
      declaration: OAI.OddKaplansky.main_theorem
      file: OAI/Algebra/OddKaplansky/Main.lean
```

`lean/OAI/Algebra/OddKaplansky/Main.lean:81`
```lean
theorem main_theorem : MainClaim := by
```

`lean/OAI/Algebra/OddKaplansky/Main.lean:71`
```lean
def MainClaim : Prop :=
  sourcePrime.Prime ∧ Odd sourcePrime ∧
  ∃ (K : Type) (_ : Field K) (_ : Fintype K) (_ : CharP K sourcePrime),
  Fintype.card K = sourcePrime^4 ∧
  ∃ (G : Type) (_ : Group G) (_ : Group.FG G),
  (∃ g : G, g ≠ 1 ∧ IsOfFinOrder g) ∧
  ∃ a b : MonoidAlgebra K G,
  a * b = 1 ∧ b * a ≠ 1 ∧
  Function.Injective (cellular b) ∧ ¬ Function.Surjective (cellular b)
```

Verdict: three entries for three claims. `GroupRingDeterminant` states claim 3 (integral group-ring
matrix, invertible over the rational group ring, Fuglede–Kadison determinant strictly between 0 and
1). `OddKaplansky` states claim 2 (injective, non-surjective cellular map) alongside a one-sided
inverse. `KaplanskyFinitelyPresented` states the direct-finiteness failure over a characteristic-2
field for a finitely presented group — and its group carries an element of odd prime order
(`orderOf g = ℓ`), so the blurb's "torsion-free" adjective is not in the statement.
`KaplanskyDirectFiniteness`, the general direct-finiteness config, has no entry.

### 198 — A counterexample to the little finitistic-dimension conjecture

Claim 1 (`overview.tex:477`) — *"This disproves the little finitistic-dimension conjecture."*

`LittleFinitistic` — `lean/docs/198.md:17`

`lean/formalization.yaml:1286`
```yaml
    - comparator_config: ComparatorChallenges/LittleFinitistic.json
      declaration: OAI.LittleFinitistic.Main.exists_counterexample
      file: OAI/Algebra/Finitistic/Main.lean
```

`lean/OAI/Algebra/Finitistic/Main.lean:44`
```lean
theorem exists_counterexample :
  ∃ (A : Type) (_ : Ring A) (_ : Algebra ℂ A),
  FiniteDimensional ℂ A ∧ littleFinitisticDimension A = ⊤ ∧
  ∀ m : ℕ, 0 < m → ∃ N : ModuleCat.{0} A, Module.Finite A N ∧
  ((2*m-2 : ℕ) : WithBot ℕ∞) ≤ projectiveDimension N ∧
  projectiveDimension N < ⊤ := by
```

`FinitisticAsymmetry` — `lean/docs/198.md:18`

`lean/formalization.yaml:1162`
```yaml
    - comparator_config: ComparatorChallenges/FinitisticAsymmetry.json
      declaration: OAI.LittleFinitistic.extreme_left_right_asymmetry
      file: OAI/Algebra/FinitisticAsymmetry/Main.lean
```

`lean/OAI/Algebra/FinitisticAsymmetry/Main.lean:48`
```lean
theorem extreme_left_right_asymmetry :
  ∃ (Λ : Type) (_ : Ring Λ) (_ : Algebra ℂ Λ),
  FiniteDimensional ℂ Λ ∧
  littleFinitisticDimension Λ = ⊤ ∧ bigFinitisticDimension Λ = ⊤ ∧
  littleFinitisticDimension Λᵐᵒᵖ = 0 ∧ bigFinitisticDimension Λᵐᵒᵖ = 0 ∧
  ¬ InjectivesGenerate Λ ∧ InjectivesGenerate Λᵐᵒᵖ := by
```

Verdict: `LittleFinitistic` states claim 1 (little finitistic dimension `⊤` over ℂ, with modules of
arbitrarily large finite projective dimension). `FinitisticAsymmetry` is a companion — the extreme
left/right asymmetry — and the family's single counterexample sentence does not name it.

### 199 — Counterexamples to conjectures of Auslander--Reiten, Tachikawa, and Nakayama

Claim 1 (`overview.tex:479`) — *"Constructs finite-dimensional algebras over a characteristic-two rational-function field
that disprove the Auslander--Reiten and Gorenstein-projective conjectures, and Tachikawa's second
conjecture."*

Claim 2 (`overview.tex:479`) — *"An associated endomorphism algebra also disproves the classical, generalized and strong
Nakayama conjectures, the Auslander--Gorenstein conjecture, and the Wakamatsu tilting conjecture."*

Claim 3 (`overview.tex:479`) — *"The counterexamples persist under every extension of the base field."*

`AuslanderReiten` — `lean/docs/199.md:22`

`lean/formalization.yaml:938`
```yaml
    - comparator_config: ComparatorChallenges/AuslanderReiten.json
      declaration: OAI.ArExplicit.Statement.main
      file: OAI/Algebra/AuslanderReiten/All.lean
```

`lean/OAI/Algebra/AuslanderReiten/All.lean:738`
```lean
theorem main : FullStatement.{v} :=
```

`lean/OAI/Algebra/AuslanderReiten/Statement.lean:52`
```lean
def FullStatement : Prop :=
  AlgebraicIndependent (ZMod 2) parameters ∧
  ∃ s : System,
  Conclusions K s.algebraCarrier s.moduleCarrier ∧
  ∀ (E : Type v) [Field E] [Algebra K E],
  ∃ action : Module (E ⊗[K] s.algebraCarrier) (E ⊗[K] s.moduleCarrier),
  letI := action
  ∃ tower : IsScalarTower E (E ⊗[K] s.algebraCarrier) (E ⊗[K] s.moduleCarrier),
  letI := tower
  (∀ (a b : E) (r : s.algebraCarrier) (z : s.moduleCarrier),
  (a ⊗ₜ[K] r) • (b ⊗ₜ[K] z) = (a*b) ⊗ₜ[K] (r • z)) ∧
  Conclusions E (E ⊗[K] s.algebraCarrier) (E ⊗[K] s.moduleCarrier)
```

`Tachikawa` — `lean/docs/199.md:23`

`lean/formalization.yaml:1570`
```yaml
    - comparator_config: ComparatorChallenges/Tachikawa.json
      declaration: OAI.Tachikawa.main_theorem
      file: OAI/RingTheory/Tachikawa/Counterexample.lean
```

`lean/OAI/RingTheory/Tachikawa/Counterexample.lean:293`
```lean
theorem main_theorem : Counterexample :=
```

`lean/OAI/RingTheory/Tachikawa/Symmetry.lean:17`
```lean
def Counterexample : Prop :=
  ∃ (A : Type) (rA : Ring A),
  letI := rA
  ∃ (aA : Algebra k A),
  letI := aA
  Module.Finite k A ∧ SymmetricOver k A ∧
  ∃ (M : Type) (gM : AddCommGroup M),
  letI := gM
  ∃ (mA : Module A M) (mk : Module k M),
  letI := mA
  letI := mk
  IsScalarTower k A M ∧ Module.Finite k M ∧
  ¬ Module.Projective A M ∧
  ∀ n : ℕ, 0 < n →
  Subsingleton (CategoryTheory.Abelian.Ext (ModuleCat.of A M) (ModuleCat.of A M) n)
```

Verdict: `AuslanderReiten` states claim 1's Auslander–Reiten part and claim 3 — the carrier's last
conjunct quantifies over every field extension `E / K` and requires `Conclusions E …` there.
`Tachikawa` states the Tachikawa part of claim 1 (self-injective algebra, non-projective module,
vanishing higher Ext). Claim 2's Nakayama/Auslander–Gorenstein/Wakamatsu list has no linked config,
so it has no formalized counterpart.

### 244 — The partition principle does not imply choice

Claim 1 (`overview.tex:573`) — *"Assuming ZF is consistent, constructs a model in which every surjective image of a set
injects into that set, yet the axiom of choice fails."*

`PartitionPrinciple` — `lean/docs/244.md:17`

`lean/formalization.yaml:1362`
```yaml
    - comparator_config: ComparatorChallenges/PartitionPrinciple.json
      declaration: OAI.PartitionPilot.Forcing.TransitiveGround.exists_model_partitionPrinciple_without_choice
      file: OAI/SetTheory/PartitionPrinciple/Models/Separation.lean
```

`lean/OAI/SetTheory/PartitionPrinciple/Models/Separation.lean:34`
```lean
theorem exists_model_partitionPrinciple_without_choice
(pairing : Realize M.sets SetFormula.pairing Fin.elim0)
(unions : Realize M.sets SetFormula.union Fin.elim0)
(powers : Realize M.sets powerSet Fin.elim0) (separation : SeparationSchema M.sets)
(collection : CollectionSchema M.sets) (infinite : Realize M.sets infinity Fin.elim0)
(choice : Realize M.sets SetFormula.choice Fin.elim0)
(small : M.sets.Countable)
{K : ZFSet.{u}} (hK : K ∈ M.sets) (standard : GroundStandardInaccessible M K) :
∃ N : TransitiveGround.{u}, M.sets ⊆ N.sets ∧ ZFRealization N.sets ∧
Realize N.sets partitionPrinciple Fin.elim0 ∧
¬ Realize N.sets SetFormula.choice Fin.elim0 := by
```

`PartitionConsistency` — `lean/docs/244.md:18` — no `main_results` entry.

Verdict: the entry states claim 1's conclusion — a transitive ground model realizing the partition
principle and refuting choice — under hypotheses the blurb compresses: the theorem takes the ZF
axiom schemata as explicit arguments plus a countability and an inaccessible-ground hypothesis, so
"assuming ZF is consistent" is not the statement's hypothesis form. `PartitionConsistency` has no
entry.

### 294 — A counterexample to Kaplansky's quasitrace conjecture

Claim 1 (`overview.tex:680`) — *"Disproves Kaplansky's quasitrace conjecture by constructing a separable unital complex
$C^*$-algebra admitting normalized $2$-quasitraces, all of which are nonadditive."*

`KaplanskyQuasitrace` — `lean/docs/294.md:17`

`lean/formalization.yaml:1270`
```yaml
    - comparator_config: ComparatorChallenges/KaplanskyQuasitrace.json
      declaration: OAI.Kaplansky.kaplansky_quasitrace_counterexample
      file: OAI/Analysis/Kaplansky/Main.lean
```

`lean/OAI/Analysis/Kaplansky/Main.lean:17`
```lean
theorem kaplansky_quasitrace_counterexample : MainTarget :=
```

`lean/OAI/Analysis/Quasitrace/Matrix.lean:27`
```lean
def MainTarget : Prop :=
  ∃ (A : Type) (inst : CStarAlgebra A),
  letI := inst
  TopologicalSpace.SeparableSpace A ∧
  (∃ τ : OneQuasitrace A, τ.Normalized ∧ τ.IsTwo) ∧
  ∃ a b : A, PositiveContraction a ∧ PositiveContraction b ∧
  ∀ τ : OneQuasitrace A, τ.Normalized → τ.IsTwo →
  (1 : ℝ) / 144 ≤ (τ (a+b) - τ a - τ b).re
```

`KaplanskyStableFiniteness` — `lean/docs/294.md:18` — no `main_results` entry.

Verdict: the carrier states claim 1 — separable C\*-algebra, a normalized 2-quasitrace exists, and
every normalized 2-quasitrace has an additive defect at least 1/144 on a fixed pair of positive
contractions. The carrier is not in the declaration's own tree: `Main.lean` imports
`OAI.Analysis.Cuntz.Quasitrace`, and the definition sits under `OAI/Analysis/Quasitrace/`.
`KaplanskyStableFiniteness` has no entry.

### 329 — A counterexample to Pietsch's metric-entropy duality conjecture

Claim 1 (`overview.tex:754`) — *"Disproves Pietsch's dimension-free duality conjecture for metric entropy."*

Claim 2 (`overview.tex:754`) — *"Origin-symmetric convex bodies violate every proposed choice of universal constants in the
conjectured comparison between covering numbers and those of the polar bodies, even when the covering
body is a cube."*

`MetricEntropyDuality` — `lean/docs/329.md:15`

`lean/formalization.yaml:1338`
```yaml
    - comparator_config: ComparatorChallenges/MetricEntropyDuality.json
      declaration: OAI.MetricEntropyDuality.exists_entropy_duality_counterexample_with_covers
      file: OAI/Analysis/MetricEntropy/Main.lean
```

`lean/OAI/Analysis/MetricEntropy/Main.lean:48`
```lean
theorem exists_entropy_duality_counterexample_with_covers
(a b : ℝ) (ha : 1 ≤ a) (hb : 1 ≤ b) :
∃ n : ℕ, 0 < n ∧ ∃ K : Set (RealSpace (Fin n)),
IsSymmetricConvexBody K ∧
Coverable K (cube (Fin n)) ∧
Coverable (polar (cube (Fin n))) (a⁻¹ • polar K) ∧
b * Real.log (coveringNumber (polar (cube (Fin n))) (a⁻¹ • polar K) : ℝ) <
Real.log (coveringNumber K (cube (Fin n)) : ℝ) := by
```

Verdict: the entry states both claims — the body is symmetric, the covering body is the cube, and
the polar-side covering number beats the original by any prescribed factor `b`, which is the
"every proposed choice of universal constants" form.

### 347 — Counterexamples to strong forms of Arnold's fixed-point conjecture

Claim 1 — *"Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply
connected closed K\"ahler manifolds of real dimension $22$, the deficit below the stable Morse number
is unbounded."* (`overview.tex:792`)

`ArnoldCounterexample` — `lean/docs/347.md:15`

`lean/formalization.yaml:926`
```yaml
    - comparator_config: ComparatorChallenges/ArnoldCounterexample.json
      declaration: OAI.ArnoldCounterexample.main
      file: OAI/Geometry/Arnold/Main.lean
```

`lean/OAI/Geometry/Arnold/Main.lean:14`
```lean
theorem main :
  ∃ φ : Q3 ≃ Q3, IsHamiltonian φ ∧ (fixedSet φ).encard = 3 ∧
  (3 : ℕ∞) < 4 ∧ 4 ≤ criticalNumber ∧ HasDegenerateFixedPoint φ := by
```

Verdict: the entry is a counterexample to a fixed-point lower bound — a Hamiltonian self-equivalence
of `Q3` with 3 fixed points while `criticalNumber` is at least 4 — and it is explicitly the
degenerate case (`HasDegenerateFixedPoint φ`). The abstract's claim is about nondegenerate fixed
points and an unbounded deficit on 22-dimensional Kähler manifolds; the statement names one
manifold, one fixed-point count, and a degenerate fixed point.

### 350 — Yau's nodal conjecture: surfaces and counterexamples

Claim 1 (`overview.tex:798`) — *"The upper bound fails for fixed smooth metrics in dimensions three and four, including
metrics on $S^3$ arbitrarily close to round."*

`NodalLength` — `lean/docs/350.md:21` — no `main_results` entry.

`SmoothYau` — `lean/docs/350.md:22`

`lean/formalization.yaml:1526`
```yaml
    - comparator_config: ComparatorChallenges/SmoothYau.json
      declaration: OAI.YauCounterexamples.sphere_two_torus_two
      file: OAI/Geometry/SmoothYau/ProductMetric/SphereProduct.lean
```

`lean/OAI/Geometry/SmoothYau/ProductMetric/SphereProduct.lean:75`
```lean
theorem sphere_two_torus_two :
  ∃ g : SmoothMetric FourModel FourManifold,
  HasUnboundedNodalRatio g 4 := by
```

`YauCounterexample` — `lean/docs/350.md:23`

`lean/formalization.yaml:1654`
```yaml
    - comparator_config: ComparatorChallenges/YauCounterexample.json
      declaration: OAI.Yau.Target.yau_nodal_set_upper_bound_counterexample
      file: OAI/Geometry/NodalSets/Main.lean
```

`lean/OAI/Geometry/NodalSets/Main.lean:8`
```lean
theorem yau_nodal_set_upper_bound_counterexample : MainTarget := by
```

`lean/OAI/Geometry/NodalSets/Model.lean:54`
```lean
def MainTarget : Prop :=
  ∃ (g : SmoothMetric) (lam : ℕ → ℝ) (u : ℕ → Manifold5 → ℝ),
  (∀ k, 0 < lam k) ∧
  (∀ k, u k ≠ 0) ∧
  (∀ k, ContMDiff modelWithCorners 𝓘(ℝ, ℝ) ∞ (u k)) ∧
  (∀ k x, -chartLaplacian g (extChartAt modelWithCorners x) (u k) ((extChartAt modelWithCorners x) x) =
  lam k * u k x) ∧
  Tendsto lam atTop atTop ∧
  Tendsto (fun k ↦ nodalMeasure g (u k) / ENNReal.ofReal (Real.sqrt (lam k)))
  atTop (𝓝 ⊤)
```

Verdict: two entries, in two settings. `SmoothYau` states the fixed-metric failure in dimension 4
(`HasUnboundedNodalRatio g 4` on `FourManifold`). `YauCounterexample` states the eigenvalue-sequence
form — Laplace eigenfunctions `u k` with `lam k → ∞` whose nodal measure over `√lam k` tends to `⊤`
— on the model `Manifold5 := Base × Circle` with chart model `𝓡 4 × 𝓡 1`, i.e. the 5-dimensional
model, not the 3- and 4-dimensional metrics claim 1 names. `NodalLength` has no entry.

### 361 — Counterexamples to Yau's harmonic dimension bound

Claim 1 (`overview.tex:820`) — *"Disproves Yau's proposed Euclidean dimension bound for harmonic functions of integer
growth on manifolds with nonnegative Ricci curvature."*

`HarmonicGrowth` — `lean/docs/361.md:15`

`lean/formalization.yaml:1214`
```yaml
    - comparator_config: ComparatorChallenges/HarmonicGrowth.json
      declaration: OAI.HarmonicCounterexample.main
      file: OAI/Geometry/HarmonicGrowth/Main.lean
```

`lean/OAI/Geometry/HarmonicGrowth/Main.lean:475`
```lean
theorem main : MainClaim := by
```

`lean/OAI/Geometry/HarmonicGrowth/Basic.lean:92`
```lean
def MainClaim : Prop :=
  ∃ (n k : ℕ) (g : SmoothMetric n), Even n ∧ 8 ≤ n ∧ 2 ≤ k ∧
  Complete g ∧ RicciNonnegative g ∧ EuclideanNearOrigin g ∧ PositiveSubunitAVR g ∧
  ∃ u : Fin (euclideanDimension n k + 1) → (Space n → ℝ),
  LinearIndependent ℝ u ∧ ∀ i, HarmonicGrowth g k (u i)
```

Verdict: the carrier states claim 1 — a complete manifold with nonnegative Ricci curvature, Euclidean
near the origin, carrying `euclideanDimension n k + 1` linearly independent harmonic functions of
integer growth `k`, one more than the proposed bound.

## Claim-level gaps inside T3

The 11 configs a T3 scope note links that carry no `main_results` entry, in 7 families:

| Config | Family | Scope-note anchor | What the family's claim needs from it |
|---|---|---|---|
| `BalancedRyser` | 162 | `lean/docs/162.md:18` | the balanced case of the Ryser covering claim |
| `EuclideanRamseyCircle` | 172 | `lean/docs/172.md:19` | no claim sentence names it |
| `EuclideanRamseyNine` | 172 | `lean/docs/172.md:20` | no claim sentence names it |
| `EuclideanRamseyQuadratic` | 172 | `lean/docs/172.md:21` | no claim sentence names it |
| `EuclideanRamseySpherical` | 172 | `lean/docs/172.md:22` | no claim sentence names it |
| `EuclideanRamseyTransitive` | 172 | `lean/docs/172.md:23` | the Leader–Russell–Walters refutation (claim 1) |
| `InfiniteMatroidCorollaries` | 185 | `lean/docs/185.md:18` | the Joó partitional-matroid corollary (claim 2) |
| `KaplanskyDirectFiniteness` | 197 | `lean/docs/197.md:34` | the general direct-finiteness counterexample |
| `PartitionConsistency` | 244 | `lean/docs/244.md:18` | no claim sentence names it |
| `KaplanskyStableFiniteness` | 294 | `lean/docs/294.md:18` | no claim sentence names it |
| `NodalLength` | 350 | `lean/docs/350.md:21` | the nodal-length bound |

Two of these are the load-bearing gaps: family 172's disproven conjecture is exactly the
`EuclideanRamseyTransitive` config, and the entry that family does have is a positive classification;
family 185's second claim is exactly `InfiniteMatroidCorollaries`. The rest are companion configs the
release set that its own abstract sentence does not name.

Two claims have no linked config at all, so no config-level gap records them: family 047's
Dolgachev–Weisfeiler affine-fibration claim and family 199's Nakayama/Auslander–Gorenstein/Wakamatsu
claim.

## The 10 T2 families: structural absence

Every T2 family in this population has `mainres` 0 and `paps_form` 0: the release links comparator
configs for them and names no `main_results` declaration for any of them. The lack of a formalized
counterpart is a property of the release's own coverage record, not of what was read here.

| Fam | Configs with no entry | Anchor |
|---|---|---|
| 100 | `CylinderCovering`, `RuledCovering`, `TriangularCovering` | `lean/docs/100.md:32` |
| 151 | `C1EntropyCounterexample` | `lean/docs/151.md:15` |
| 157 | `ListHadwiger` | `lean/docs/157.md:15` |
| 161 | `SidorenkoCounterexample` | `lean/docs/161.md:15` |
| 191 | `HeilbronnTriangle` | `lean/docs/191.md:15` |
| 192 | `SquareRootDegree` | `lean/docs/192.md:17` |
| 272 | `DimensionTenChannel`, `DimensionTenPair` | `lean/docs/272.md:17` |
| 289 | `StrongKadisonKastler` | `lean/docs/289.md:15` |
| 297 | `Naimark` | `lean/docs/297.md:15` |
| 323 | `SeparableQuotientNegative` | `lean/docs/323.md:17` |

The counterexample sentence each family ships:

Claim 100-1 (`overview.tex:276`) — *"This disproves Bang's half-area cylinder-covering bound and the stronger directionwise
normalized conjecture in dimension three."*

Claim 151-1 (`overview.tex:381`) — *"This disproves the homological entropy lower bound for general $C^1$ self-maps:
homological growth need not force positive orbit complexity."*

Claim 157-1 (`overview.tex:395`) — *"Disproves Hadwiger's conjecture even for fractional coloring: arbitrarily large finite
simple graphs with independence number at most two satisfy $\chi_f(G)>h(G)$, where $h(G)$ is the
largest clique-minor order."*

Claim 161-1 (`overview.tex:403`) — *"Disproves Sidorenko's conjecture with a connected bipartite pattern on $35$ vertices
and $66$ edges that occurs less frequently than in a random graph of the same edge density."*

Claim 191-1 (`overview.tex:461`) — *"This disproves the conjectured almost-$n^{-2}$ upper bound in Heilbronn's triangle
problem, which asks how large the smallest determined triangle can be."*

Claim 192-1 (`overview.tex:463`) — *"Disproves the proposed square-root bound relating a Boolean function's linear Fourier
coefficients to its polynomial degree."*

Claim 272-1 (`overview.tex:633`) — *"A trace-preserving PPT channel on $M_{21}(\mathbb C)$ whose square is not entanglement
breaking disproves Christandl\textquotesingle s PPT-square conjecture."*

Claim 289-1 (`overview.tex:670`) — *"Counterexamples show that near-identity conjugacy fails for one-sided near inclusions,
and that arbitrarily close norm-separable $C^*$-algebras need not be ambiently unitarily
conjugate."*

Claim 297-1 (`overview.tex:686`) — *"Thus the unrestricted compact-operator characterization fails without additional
set-theoretic assumptions; the counterexample is nonseparable."*

Claim 323-1 (`overview.tex:742`) — *"The assertion that every infinite-dimensional Banach space has a separable
infinite-dimensional quotient can hold for all real and complex Banach spaces, whereas the continuum
hypothesis yields counterexamples over both fields."*

Family 100 is the only one whose scope note repeats a config: 6 link occurrences, 3 distinct configs
(`CylinderCovering` appears at `lean/docs/100.md:32`, `lean/docs/100.md:34`, `lean/docs/100.md:36`,
`lean/docs/100.md:37`).

## Challenge stubs behind the population

The 28 scope notes link **51** distinct configs, and each has a stub file under
`lean/ComparatorChallenges/` carrying **53** `sorry` occurrences. Counted per scope-note link
occurrence instead of per distinct config the same files carry 56, the 3-gap being family 100's four
links to `CylinderCovering`. A stub is the target the release
set itself, not a proof: it states the claim the release asked a comparator to close. The proved
version, where one exists, is the `main_results` declaration read above — which is why 27 entries
over 51 configs is the coverage answer, and the `sorry` count is not a failure of the manuscripts.

## The bead's "21" and the shape rule's "16"

The bead says "The 21 T0 counterexample-shaped families are already recorded in
`notes/t0-triage.md`". The ledger's `counterexample` shape tag fires on **16** T0 families. The
**21** is the count of counterexample families in the t0-triage reading record, which uses the broader
phrase rule (the same rule behind the ledger's `counterex_broad` column, 74 families corpus-wide: 22
T0, 33 T3, 19 T2). Both numbers are recorded here with the rule behind each; they are not resolved
against each other, because they count different things — a keyword tag versus a read verdict.

## What has not been checked

- No Lean was elaborated, no comparator was run, and no proof was checked. Every verdict is a reading
  of a statement line against an abstract sentence.
- The 27 declarations were resolved to the statement line the entry's `file:` names. Where a
  declaration is proved from lemmas (11 of them are), the proof body was not followed, so this record
  says what the formalized statement *says*, not that it proves the manuscript's theorem.
- Carrier resolution is bounded: the import walk is capped at 400 files and takes the nearest
  definition whose last dotted component matches the carrier name. A carrier defined under a
  different name, or behind a type synonym, would be reported as a statement whose content is opaque.
- Claim-to-config pairings are readings of the abstract sentence against the config name and the
  statement text. The release records no claim-to-config relation, so a pairing is an inference, not
  a recorded edge.
- The 16 T0 families with the shape tag were not cross-checked here; the T0 reading record is
  `notes/t0-triage.md`.
- Configs linked by scope notes outside this population, and the 178 − 51 = 127 configs named by
  `main_results` that no population scope note links, were not examined.
- Whether a `main_results` declaration's statement is the manuscript's own theorem, a specialization,
  or a companion result is judged from the statement text only; the manuscripts' theorem environments
  were not paired against these declarations.
