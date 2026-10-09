# The topic vocabulary

Built 2026-10-07. The vocabulary is **92 curated terms** in [`notes/topics.tsv`](topics.tsv) —
**9 columns** (`term`, `pattern`, `fams`, `title`, `abstract`, `scope`, `path`, `status`, `note`) —
and the pattern column is the source of truth: `notes/scripts/measure_topics.py` loads it, matches
it, and records the counts the row carries as evidence. `python3 notes/scripts/measure_topics.py`
prints the report every number below comes from and writes nothing;
`python3 notes/scripts/measure_topics.py --check` re-measures all 92 rows and exits non-zero on
drift. Pages are rendered by `python3 notes/scripts/build_index.py` into `notes/index/topics/`. No
`lake`, `lean`, `lake exe cache get`, or comparator run.

Headline, with the rule that yields it: **92 patterns matched case-insensitively against the title,
abstract, scope-note text, and derived Lean file paths of the 372 catalogued families → 978
family-topic assignments over 372 families, 0 families uncovered, 4 terms with no hit.**

## What a topic is, and what it is not

A family has four searchable texts, and a term hits a family when its pattern matches any of them:

| Layer | Text | Families with the text |
|---|---|---|
| title | the 2nd argument of the family's `\resultentry` in `overview.tex` | 372 |
| abstract | the 3rd argument of the same entry | 372 |
| scope | the text of `lean/docs/<NNN>.md` | 242 |
| path | Lean file paths reached from the family's comparator configs through `formalization.yaml` `main_results`, plus the Lean module dir names | 136 |

- **A term's yield is the number of families with at least one hit**, counted once per family
  however many layers hit. Per-layer counts are reported separately because they are not the same
  kind of evidence: the abstract layer is the release's own prose, the path layer is the release's
  own filing choice, and the path layer is **derived, not shipped** — the release ships no
  manuscript→Lean edge, so the chain is family→config→file.
- **Topics are multi-label.** A family carries zero or more topics; the 17 catalog disciplines stay
  the partition. A topic is a label added on top of the ledger's claim-shape columns, never a
  replacement for them.
- **A yield is a keyword floor, not a census.** A listing means the pattern hit one of four texts,
  not that anyone judged the family to be about the term. The incidental matches are quoted below.
- **A term with no hit is kept, not deleted.** Four such terms are recorded as measured statements
  about the corpus.

## Why the vocabulary is curated, not derived

The release ships no topic vocabulary to derive from and nothing to validate a derived term
against: **0 MSC codes over 8,206 files, 0 `keywords` fields over 12,876 bibliography entries,
`\keywords` defined in 12 of 719 manuscript directories** (all three measured by
`python3 notes/scripts/extract_links.py`). Word-frequency probing is useless here for a second
reason: the corpus names results by conjecture and by model, not by generic subject words. Its PDE
families are "Boltzmann nonuniqueness", "the hot spots conjecture", "De Giorgi's conjecture in
dimension eight"; its probability families are "planar first-passage percolation", "the
Benjamini–Schramm nonuniqueness conjecture", "the Mézard–Parisi formula for diluted spin glasses".
A pattern therefore carries the named models the corpus actually uses — Vlasov–Maxwell, Mumford–Shah,
Lane–Emden, De Giorgi; planar maps, Benjamini–Schramm, six-vertex, dimer, XY, random-cluster, SK,
Ising, GOE, factor of IID, perceptron and jamming; Shub, billiards, Bernoulli convolutions, Hilbert's
sixteenth — and a bare subject stem contributes little on its own.

## Yield, by term

`fams` is the yield; `T/A/S/P` are the per-layer family counts. Rule: the 92 curated patterns over
the 372 families, as printed by `python3 notes/scripts/measure_topics.py`.

| Term | fams | T | A | S | P |
|---|---|---|---|---|---|
| graph-theory | 43 | 14 | 37 | 34 | 3 |
| algebraic-topology | 42 | 10 | 29 | 21 | 0 |
| algebraic-geometry | 35 | 30 | 34 | 7 | 1 |
| manifolds | 31 | 4 | 31 | 8 | 1 |
| riemannian-geometry | 29 | 10 | 26 | 17 | 0 |
| complexity-theory | 28 | 17 | 21 | 20 | 3 |
| group-theory | 27 | 15 | 26 | 16 | 1 |
| metric-geometry | 25 | 10 | 19 | 21 | 3 |
| algorithms | 24 | 2 | 10 | 16 | 0 |
| operator-algebras | 24 | 20 | 21 | 19 | 1 |
| computability | 23 | 3 | 13 | 11 | 12 |
| complex-geometry | 21 | 7 | 19 | 5 | 3 |
| mathematical-physics | 21 | 16 | 19 | 8 | 2 |
| statistical-mechanics | 21 | 15 | 19 | 9 | 2 |
| convex-geometry | 20 | 12 | 12 | 16 | 3 |
| curves | 17 | 2 | 17 | 3 | 1 |
| harmonic-analysis | 17 | 13 | 13 | 11 | 1 |
| measure-theory | 17 | 2 | 10 | 10 | 0 |
| partial-differential-equations | 17 | 14 | 12 | 8 | 0 |
| disordered-systems | 16 | 10 | 11 | 12 | 1 |
| functional-analysis | 16 | 5 | 11 | 13 | 1 |
| surfaces | 16 | 8 | 13 | 7 | 1 |
| spectral-theory | 15 | 2 | 9 | 9 | 0 |
| banach-spaces | 13 | 10 | 13 | 11 | 2 |
| discrete-geometry | 13 | 11 | 10 | 11 | 2 |
| logic | 13 | 7 | 13 | 10 | 2 |
| planar-maps-and-lattice-models | 13 | 9 | 13 | 4 | 1 |
| quantum-theory | 13 | 6 | 12 | 8 | 1 |
| symplectic-geometry | 12 | 8 | 10 | 6 | 1 |
| condensed-matter | 11 | 9 | 10 | 6 | 1 |
| conformal-universality | 11 | 11 | 9 | 3 | 0 |
| dynamical-systems | 11 | 8 | 6 | 7 | 0 |
| primes | 11 | 6 | 10 | 6 | 1 |
| probability | 11 | 6 | 8 | 7 | 1 |
| quantum-information | 11 | 6 | 7 | 9 | 0 |
| diophantine-equations | 10 | 5 | 10 | 6 | 0 |
| graph-coloring | 10 | 3 | 9 | 7 | 2 |
| arithmetic-geometry | 9 | 5 | 8 | 3 | 0 |
| commutative-algebra | 9 | 6 | 6 | 6 | 1 |
| expanders-and-spectral-graphs | 9 | 5 | 5 | 5 | 0 |
| fractal-geometry | 9 | 2 | 6 | 6 | 0 |
| number-fields | 9 | 1 | 8 | 3 | 0 |
| representation-theory | 9 | 4 | 6 | 5 | 2 |
| abelian-varieties | 8 | 3 | 7 | 1 | 0 |
| analytic-number-theory | 8 | 4 | 8 | 4 | 0 |
| ergodic-theory | 8 | 2 | 6 | 5 | 0 |
| information-theory | 8 | 6 | 4 | 8 | 0 |
| noncommutative-algebra | 8 | 7 | 7 | 5 | 0 |
| stable-homotopy | 8 | 8 | 7 | 2 | 0 |
| category-theory | 7 | 2 | 6 | 3 | 1 |
| combinatorial-optimization | 7 | 4 | 2 | 7 | 0 |
| differential-geometry | 7 | 6 | 7 | 4 | 0 |
| enumerative-combinatorics | 7 | 5 | 6 | 5 | 1 |
| geometric-topology | 7 | 7 | 5 | 1 | 0 |
| lie-theory | 7 | 1 | 6 | 2 | 0 |
| potential-theory | 7 | 2 | 4 | 6 | 0 |
| probabilistic-combinatorics | 7 | 5 | 6 | 7 | 0 |
| additive-combinatorics | 6 | 4 | 5 | 4 | 0 |
| geometric-measure-theory | 6 | 2 | 5 | 3 | 0 |
| quantum-computing | 6 | 6 | 5 | 4 | 0 |
| random-graphs | 6 | 2 | 3 | 3 | 0 |
| sampling-and-counting | 6 | 4 | 3 | 6 | 0 |
| extremal-combinatorics | 5 | 4 | 3 | 4 | 1 |
| general-relativity | 5 | 3 | 4 | 2 | 0 |
| modularity | 5 | 5 | 5 | 0 | 0 |
| spin-glasses | 5 | 5 | 4 | 3 | 0 |
| calculus-of-variations | 4 | 2 | 3 | 3 | 0 |
| convex-optimization | 4 | 3 | 4 | 3 | 0 |
| elliptic-curves | 4 | 1 | 4 | 0 | 0 |
| galois-theory | 4 | 1 | 3 | 2 | 0 |
| kinetic-theory | 4 | 4 | 3 | 3 | 1 |
| modular-representation | 4 | 3 | 3 | 1 | 0 |
| optimal-transport | 4 | 3 | 3 | 4 | 0 |
| percolation | 4 | 3 | 3 | 2 | 0 |
| ramsey-theory | 4 | 4 | 1 | 3 | 1 |
| coding-theory | 3 | 2 | 1 | 3 | 1 |
| complex-analysis | 3 | 3 | 3 | 3 | 0 |
| game-theory | 3 | 2 | 2 | 2 | 0 |
| matroids | 3 | 3 | 3 | 3 | 2 |
| minimal-surfaces | 3 | 3 | 3 | 0 | 0 |
| formal-languages | 2 | 1 | 2 | 1 | 0 |
| hilbert-problems | 2 | 2 | 2 | 1 | 0 |
| hypergraphs | 2 | 1 | 2 | 2 | 0 |
| combinatorial-games | 1 | 1 | 1 | 1 | 0 |
| fluid-dynamics | 1 | 1 | 0 | 1 | 0 |
| knot-theory | 1 | 1 | 1 | 0 | 0 |
| random-matrices | 1 | 1 | 0 | 0 | 0 |
| ricci-flow | 1 | 0 | 1 | 0 | 0 |
| automorphic-forms | 0 | 0 | 0 | 0 | 0 |
| cluster-algebras | 0 | 0 | 0 | 0 | 0 |
| machine-learning | 0 | 0 | 0 | 0 | 0 |
| tropical-geometry | 0 | 0 | 0 | 0 | 0 |

## Coverage

- **families covered 372 of 372, uncovered 0.** Coverage grew by adding pattern *alternatives* to
  existing terms, never by adding terms. Three alternatives are load-bearing for coverage, measured
  by ablating each one from its pattern and re-measuring: `irrationalit` in `diophantine-equations`
  is the only reason **017** ("The irrationality exponent of $\pi$ is $2$") has a topic; `sensitivit`
  in `complexity-theory` is the only reason **132** ("A counterexample to the quadratic sensitivity
  conjecture") has one; `anticanonical` in `algebraic-geometry` is the only reason **068**
  ("Anticanonical nonvanishing under smooth semipositivity") has one. Ablating any one of the three
  drops coverage to 371.
- **Two alternatives added for coverage reach nothing unique.** `gotsman--linial` reaches only
  **127** ("The asymptotic Gotsman--Linial conjecture"), which `complexity-theory` already reaches,
  so ablating it leaves coverage at 372; `newton polytope` reaches **0** families in any layer — a
  dead alternative kept in the pattern. The earlier draft of this page credited those two with
  covering 113 and 115; that is false. 113 ("Approximate counting and the perfect-matching entropy
  conjecture") carries 7 topics and 115 ("Sampling and counting contingency tables with arbitrary
  margins") carries 2, none of them `algebraic-geometry`.
- **topics per family 1:93 2:103 3:87 4:51 5:21 6:13 7:2 8:1 9:1** — median **2**, mean 2.63, so a
  family typically sits on the boundary of two of these terms. 93 families carry exactly one topic.
  The 9-topic family is **211** ("Geometry, diffusion, and spectra of random planar maps":
  graph-theory, metric-geometry, statistical-mechanics, spectral-theory, surfaces,
  planar-maps-and-lattice-models, quantum-theory, probability, fractal-geometry) and the 8-topic
  family is **281** ("QAOA optimality for the SK model").
- **yield histogram 0:4 1:5 2:3 3:5 4:9 5:4 6:5 7:8 8:6 9:6 10:2 11:6 12:1 13:5 15:1 16:3 17:4
  20:1 21:3 23:1 24:2 25:1 27:1 28:1 29:1 31:1 35:1 42:1 43:1.** **17** terms have a yield of 3 or less
  and 9 have a yield of 1 or less; those are thin topics, kept and labelled as thin, not merged
  away.

## Four measured negatives

These terms were proposed, matched over all four layers, and returned nothing. They are recorded,
not deleted:

| Term | What was tried | Result |
|---|---|---|
| automorphic-forms | `automorphic`, `modular form` | 0 families. The language survives only inside the `modularity` pattern. |
| cluster-algebras | `cluster algebra`, `cluster variety`, exchange relations | 0 hits over title, abstract, scope note, and Lean path. |
| machine-learning | `machine learning`, `neural network`, `deep learning`, `gradient descent` | 0 hits. The perceptron and jamming results sit under disordered-systems and condensed-matter. |
| tropical-geometry | `tropical`, `nonarchimedean polytope`, `tropicalization` | 0 hits. |

A negative is a statement about this corpus, not about mathematics: the release catalogued 372
families and none of them is a tropical-geometry family.

## The reading pass: what each narrowing was forced by

A term is quotable only after its flagged families have been read (`--families` prints them, marked
T/A/S/P). Every narrowing below was forced by a quoted family that the bare stem reached and that
is not about the term. Full per-term verdicts live in the `note` column of `notes/topics.tsv` —
**57 of 92 rows carry one**.

The **reach** column is the bare stem measured over all four layers, and **excluded** is the set it
reaches that the narrowed term does not — the false positives the narrowing removed. Both columns
are regenerated by script, not written from memory (see finding 4 below).

| Term | Bare stem | Reach (measured) | Yield now | Excluded | Why |
|---|---|---|---|---|---|
| stable-homotopy | `chromatic` | 10: 157 158 160 162 169 171 172 314 318 319 | 8 | 157 158 160 162 169 171 172 319 | chromatic homotopy is stable homotopy; graph colouring and Euclidean Ramsey are not. 314 318 stay via `chromatic smith` / `chromatic splitting`; 319 no longer hits |
| stable-homotopy | `kervaire` | 3: 256 309 316 | 8 | 256 | 256 is "Howie's conjecture on equations over groups"; it matched through its companion paper "The Kervaire theorem for groups" → `kervaire invariant` |
| algebraic-geometry | `moduli` | 5: 003 043 053 331 372 | 35 | 003 331 372 | 372 is elasticity — "moduli of elasticity" → `moduli space`, `moduli of` |
| graph-coloring | `chromatic` | 10: 157 158 160 162 169 171 172 314 318 319 | 10 | 162 314 318 319 | chromatic homotopy, not colouring; 157 158 160 169 171 172 stay via `coloring` / `chromatic number` / `chromatic polynomial` |
| analytic-number-theory | `dirichlet`, `chowla`, `m[oö]bius` | 6: 003 007 011 071 227 365 | 8 | 071 227 365 | Dirichlet forms, Chowla-type sums outside the conjecture, Möbius inversion → `dirichlet character/series/l-function/probability`, `chowla conjecture`, `elliott conjecture`, `m[oö]bius function` |
| commutative-algebra | `gersten's` | 2: 209 258 | 9 | 209 258 | Gersten's conjecture is group cohomology; 209 258 live in noncommutative-algebra |
| operator-algebras | `kaplansky` | 5: 196 197 207 285 294 | 24 | 196 207 | Kaplansky's zero-divisor conjecture is noncommutative algebra → `kaplansky's quasitrace` |
| mathematical-physics | `einstein` | 2: 267 348 | 21 | 348 | 348 is "Nonnegatively curved Einstein four-manifolds" (differential geometry) → `bose--einstein`, which keeps 267 |
| statistical-mechanics | `bloch's` | 2: 040 271 | 21 | 040 | 040 is "Bloch's conjecture for complex surfaces" → `bloch's law`, which keeps 271 (ferromagnetic order) |
| complex-geometry | `holomorphic` | 11: 041 046 050 052 058 059 060 064 325 338 359 | 21 | 050 058 059 064 325 | stem dropped; 041 046 359 stay through `hler`, `syz`, `uniformization` |
| convex-geometry | `divisor`, `cancellation` | 11: 001 007 020 021 023 047 057 066 196 197 266 | 20 | all 11 | divisor theory and cancellation laws are not convex geometry; both stems dropped |
| harmonic-analysis | `hilbert` | 18: 004 082 083 086 098 143 194 200 238 251 288 289 293 296 297 304 325 332 | 17 | 14 of 18 | Hilbert *space* is not harmonic analysis → `hilbert transform` |
| harmonic-analysis | `fourier` | 9: 023 075 077 090 130 192 238 266 371 | 17 | 023 266 371 | bare `fourier` dropped; `fourier transform` and friends kept, so 090 ("Universal optimality of the triangular lattice") stays through its scope note |
| functional-analysis | `hilbert space` | 9: 098 251 288 289 293 296 297 325 332 | 16 | none | kept deliberately: Hilbert-space geometry *is* functional analysis, so these land here and not in harmonic-analysis |
| discrete-geometry | `packing`, `covering` | 15: 009 014 090 092 100 118 156 162 185 226 228 237 329 343 349 | 13 | 10 (009 014 162 185 226 228 237 329 343 349) | Langlands covering groups (162), symplectic ball-packing (343) → `packing density`, `covering density`, `covering bound`, `covering of`, `hadwiger's covering`. 009 and 014 enter the reach only because the bare stem is a substring of "re**covering**". `bin-packing` was **kept**, so 118 ("Unbounded bin-packing gaps") stays. The other 8 of the 13 come from named alternatives, not from the stems: 028 (Gaussian moat), 155 (periodic tiling), 165 (crossing numbers), 166 167 (distinct / pinned distances), 183 (halving lines and $k$-sets), 191 (Heilbronn), 224 (Voronoi percolation) |
| conformal-universality | `conformal` | 6: 071 072 218 223 280 282 | 11 | 071 072 280 282 | conformal field theory → `conformal universality`, `conformal limit`, which keep 218 223 |
| ergodic-theory | `lebesgue` | 3: 073 091 144 | 8 | 073 091 | Lebesgue measure, not the Lebesgue-spectrum property → `lebesgue spectrum` |
| noncommutative-algebra | `noncommutative` | 1: 116 | 8 | 116 | a bare adjective → dropped as a stem |
| category-theory | `adjoint`, `spectral sequence` | 11: 014 034 035 036 038 062 261 296 298 300 309 | 7 | all 11 | algebraic-geometry abstracts and scope notes; both stems dropped |
| random-graphs | `erd` (LaTeX stem) | 14: 012 024 025 026 084 157 159 160 166 167 171 181 184 189 | 6 | all 14 | attribution is not a topic → Erdős–Rényi spellings only |
| random-matrices | `spectrum`, `spectra of` | 12: 072 144 211 234 238 261 282 308 311 313 319 361 | 1 | all 12 | every physics spectrum result → dropped |
| modular-representation | `modular` | 6: 010 019 030 255 256 290 | 4 | all 6 | modular forms (modularity) and physics usage → `modular representation`. 255 256 entered the reach with the scope notes the merge added, and they match only as a substring of "uni**modular**" |
| kinetic-theory | `fluid` | 1: 376 | 4 | none | measured: the bare stem reaches exactly one family ("Universal computation in forced Navier–Stokes flows") → kept as a bare stem |
| spectral-theory | `spectral gap` | 5: 131 227 265 268 269 | 15 | none | kept: a gap statement is a spectral statement |
| algorithms | `algorithm` | 24 by prefix probe `\balgorithm`; 23 by the shipped `algorithm\b` | 24 | 139 | kept broad. 076 097 372 match only in scope-note exclusion prose ("The result is existential and does not supply an online algorithm"); 004 206 match "no algorithm decides". 139 is reached only by the loose prefix — its scope note says "Algorithms may be measurable, randomized, and adaptive", a sentence about the model, not a result about algorithms. 109 enters through a named alternative, not the stem |

Terms whose yield is 1 are thin by measurement, not by neglect: combinatorial-games is 187 (Snaky),
fluid-dynamics, knot-theory, ricci-flow, random-matrices each reach one family.

## Four findings from auditing my own notes

The reading pass produced claims; the claims were then checked against the live patterns, and four
of them were wrong. All four are recorded in the `note` column so a future reader does not repeat
them.

1. **A missing `|` silently deleted a pattern alternative.** `partial-differential-equations`
   carried `…|defocusing"` followed by `"schr[oö]dinger|…"`, which concatenates to the alternation
   `defocusingschr[oö]dinger` — a string that never matches. `schrödinger` was therefore absent from
   the PDE term while the note claimed it was present. The compile check passes: it is a perfectly
   legal regex. Fixed to `|one-phase bernoulli|defocusing|schr[oö]dinger`. **A compile check proves
   a pattern is legal, not that it says what you meant.**
2. **Five notes asserted narrowings that had never been applied** — kinetic-theory,
   analytic-number-theory, graph-coloring, commutative-algebra, extremal-combinatorics. The narrowings
   have now been applied for real, and the notes rewritten to match the code.
3. **`overview.tex` apostrophes are inconsistent, and ASCII-apostrophe patterns miss titles
   silently.** Over the 372 titles, **76 use ASCII `'` and 8 use U+2019** — 023 Patterson’s, 025
   `Erd\H{o}s’s`, 151 Shub’s, 209 Gersten’s, 210 Foulkes’, 298 Voiculescu’s, 316 Curtis’s, 360
   Villani’s. **16 patterns contain an ASCII apostrophe**, so 209 "Integral counterexamples to
   Gersten’s conjecture" was uncovered while `gersten's conjecture` sat in the pattern. Fixed by
   folding U+2019 → ASCII in the text layer (`norm()`), applied to all four layers.
4. **The "bare stem reached" column was written from memory and did not reproduce.** Of the 21 rows
   that named families, **3 reproduced exactly** (commutative-algebra `gersten's` → 209 258,
   noncommutative-algebra `noncommutative` → 116, kinetic-theory `fluid` → 376), **8 were subsets**
   (the stem reaches more than recorded — `kaplansky` reaches 5, not 1; `holomorphic` reaches 11,
   not 8), and **9 named at least one family the stem does not reach at all**: graph-coloring's 162,
   mathematical-physics's 281, convex-geometry's 324, functional-analysis's 326 328,
   discrete-geometry's 014, spectral-theory's 211 219 234, harmonic-analysis's 089 090 094 and 010
   014 020 031, and stable-homotopy's 160 162 171 172 256. The table above is now generated by
   measuring each stem over all four layers, so the reach and excluded columns are reproducible.
   **A narrowing you remember is not a narrowing you measured.**

Accented names are matched on the letters after the accent escape: `hler` reaches both `K\"ahler`
and `Kähler`, and `erd` reaches every spelling of Erdős. That is a property of LaTeX source, and it
is why the patterns carry stems rather than whole words.

## Axes considered and rejected

- **Discipline-mirror terms** (a term per catalog discipline): redundant with the 17 disciplines,
  which are already a partition carried in `families.tsv`. A mirror term adds a second name for the
  same grouping and no new information. The 17 catalog disciplines and the 23 Lean discipline
  directories (`lean/OAI/*/`: Algebra, AlgebraicGeometry, AlgebraicTopology, Analysis,
  CategoryTheory, Combinatorics, Computability, Dynamics, GameTheory, Geometry, GroupTheory,
  InformationTheory, LinearAlgebra, MathematicalPhysics, MeasureTheory, ModelTheory, NumberTheory,
  Optimization, Probability, RepresentationTheory, RingTheory, SetTheory, Topology) are two
  unaligned groupings, so a mirror term would have had to pick one.
- **Attribution axes** (`erdos-problems`, `shub-problems`): attribution already lives in
  `notes/conjecture-standing.tsv` and in the `resolves_named` ledger column. As a topic it is a
  property of catalog prose, not of the mathematics — which is exactly why bare `erdos` had to be
  dropped from random-graphs.
- **Claim-shape axes** (`counterexample`, `resolution`, `algorithms`, `conditional`): these are
  ledger columns (`counterex_broad`, `resolves_named`, `conditional`, `shapes`), and a topic is a
  subject label, not a claim shape. `algorithms` is kept as a topic because it names a subject area,
  and it is deliberately broad — the incidental matches are quoted above.
- **A graph database** for the index: rejected on size grounds in `math-u41` planning; TSV plus
  markdown is what ships.

## How to reproduce

```
python3 notes/scripts/measure_topics.py            # the report every count above comes from
python3 notes/scripts/measure_topics.py --check    # re-measure all 92 rows, exit 1 on drift
python3 notes/scripts/measure_topics.py --families # the reading pass: families per term, by layer
python3 notes/scripts/build_index.py               # renders notes/index/topics/<term>.md
```

`--check` was mutant-tested: perturbing two recorded `title` counts to +3 makes it print
`graph-theory.title: recorded 17, measured 14` and `algebraic-topology.title: recorded 13, measured
10` and exit 1.

## Not checked

- **No family was read to decide its topics.** Assignment is a pattern match over four texts. The
  reading pass read the *flagged families of the terms being narrowed*, not all 978 pairs, so a
  listing is a keyword floor.
- **The path layer is derived.** It exists for 136 families, through scope-note config links into
  `formalization.yaml` `main_results`. For the other 236 families the path layer is empty, so a
  family can only be reached through prose.
- **Topic coverage is not topic quality.** 372 of 372 families carry a topic because three pattern
  alternatives (`irrationalit`, `sensitivit`, `anticanonical`) each close coverage for exactly one
  family; ablate any one and coverage is 371. That closes coverage, it does not mean the vocabulary
  is complete. **17** terms have a yield of 3 or less.
- **Nothing here says a proof is correct.** The scope-note layer is release prose under
  `review: status: unchecked` with `automation: methods: [agent]`.
- **Not verified:** that each family's topic set is *right* — only that each pattern hit the text it
  hit; that the 4 negatives are exhaustive for the terms proposed (no systematic search over the
  corpus's vocabulary was run); that the incidental lists in the `note` column are exhaustive — they
  are the matches read during the narrowing pass, not a census of every incidental match.
