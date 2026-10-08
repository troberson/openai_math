# T0 cross-family chains and the 28 two-manuscript second-pass families

## Population

Rule, all three conditions: the ledger's `tier` is `T0`, the ledger's `paps` is exactly **2**, and the
family id appears in the second-pass reading sections of `notes/t0-triage.md` (the `## Second pass:
the remaining 93 families` heading through the line before `## What the triage shows`). That is
**28** families carrying **56** manuscripts.

Repo-wide there are **96** families with exactly 2 manuscripts, split `T0:36`, `T2:20`, `T3:40`. Of the
**36** at T0, **8** were read in the first pass (004, 006, 018, 019, 029, 046, 059, 209), so **28**
remain. The bead's "no coverage signal" framing holds for **27** of the 28 and fails for **1**: 268
carries `verification = 2`, a certificate bundle under each of its two manuscripts.

Regenerate with `python3 notes/scripts/extract_t0_chains.py` — report-only, it writes nothing and runs
nothing; `lake`, `lean`, `lake exe cache get`, and `comparator` are never invoked here, so nothing on
this page means "a proof was checked". Run it twice and diff: the report must be identical. Check this
page with `python3 notes/scripts/verify_t0_chains.py --mutant` before quoting any of its counts — it
re-derives every number from the ledger, `overview.tex`, `notes/subfindings.tsv` and the `.bib` files
on disk, resolves every `file:line` anchor, matches every fenced block and quotation, and flags twelve
injected mutations. It writes nothing.

## The chains the release records

The release records a cross-family link in exactly one form: a `result (NNN)` clause inside the
`overview.tex` abstract, which is what the ledger's `companions` column parses. Over **372** families
that yields **2** edges — 001 → 032 and 002 → 006 — and both point between T0 families.

**001 + 032.** The chain sentence sits in 001's abstract, not in 032's:

Claim (`overview.tex:78`) — *"Together with result 032, every specialized Hodge class is represented by
a single rational algebraic cycle simultaneously in all prime-to-$p$ and crystalline realizations, for
every residue characteristic $p$."*

The link is one-directional in the record: 032's abstract names no result, and its contribution is
stated as a consequence of a named theorem rather than of a numbered family:

Claim (`overview.tex:142`) — *"Through Milne's theorems, this also gives the Tate conjecture for all
abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every
characteristic."*

**002 + 006.** Same shape — the sentence sits in 002's abstract:

Claim (`overview.tex:80`) — *"With result 006, this gives full BSD for a density-one set of quadratic
twists of every elliptic curve over $\mathbb Q$."*

006's abstract is self-contained and names no result (`overview.tex:88`); the edge lives only in 002.

**Coverage of the chain families.** Every link in both chains is unformalized, so "a chain is only as
strong as its weakest unformalized link" reads here as *every* link:

| Fam | Tier | Manuscripts | Formalized | Challenges | `main_results` | Scope note | Verification | Trace | Shapes |
|---|---|---|---|---|---|---|---|---|---|
| 001 | T0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | classification, uniform |
| 032 | T0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | resolution, classification, uniform |
| 002 | T0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | density, uniform |
| 006 | T0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | density |
| 311 | T0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | resolution |

The triage record states the same finding, and its consequence sentence is the reason this page
exists (`notes/t0-triage.md:501`) — *"Cross-family chains sit entirely inside T0."* — and
(`notes/t0-triage.md:504`) — *"Both chains are unformalized"* — with the follow-up phrased at
(`notes/t0-triage.md:854`) — *"Cross-family chains inside T0: 001↔032, 002↔006, and
311⇒Hovey–Strickland. A chain is only as"* and (`notes/t0-triage.md:855`) — *"strong as its weakest,
unformalized link."*

## 311 ⇒ Hovey–Strickland is a literature chain, not a release edge

311 carries no `companions` value: the release records no family it depends on. Its overview abstract
names the dependency as a published implication, not as a corpus result
(`overview.tex:716`) — *"Through the implication of Barthel--Heard--Naumann, this proves the
Hovey--Strickland conjecture: dualizable $K(n)$-local spectra have exactly $n+2$ thick tensor ideals,
and their Balmer spectrum is a chain of $n+1$ points."*

The manuscript says the same thing at manuscript level, and it is the only family on this page where
that reading was done. Its own main theorem is the conjecture, stated in the introduction
(`preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/build/sections/01-introduction.tex:74`):

```
\begin{theorem}[Hovey--Strickland conjecture]\label{thm:main}
```

The implication it uses is cited to the published paper, which already proved the conjecture at height
two, so 311's contribution is the general height rather than the conjecture as such
(`preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/build/sections/01-introduction.tex:116`):

```
Barthel, Heard, and Naumann proved the Hovey--Strickland conjecture at
height two for every prime and established the general implication from
Chai's invariant-ideal assertion to the spectral classification
```

The dependency's bibliography entry is external literature — it is not a corpus manuscript, so no
intra-corpus edge can exist for it
(`preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/build/references.bib:1`):

```
@article{BHN22,
  author = {Barthel, Tobias and Heard, Drew and Naumann, Niko},
  title = {On conjectures of {Hovey--Strickland} and {Chai}},
  journal = {Selecta Mathematica. New Series},
  volume = {28},
  number = {3},
  year = {2022},
  pages = {Paper No. 56, 31},
```

The entry runs from line 1 through line 8 of that file. So the third chain in the triage's list is a
chain to the literature, and unlike the other two it has no unformalized corpus link to be the weak
one — its weak link is outside the release.

## The cross-reference layer is two edges wide

The word "companion" is how the release gestures at a second manuscript, and it is not a link. The
ledger's `companion_word` column (`\bcompanion` in the same overview abstract) fires on **10**
families — 003, 032, 197, 207, 256, 266, 268, 270, 307, 364 — and **0** of them carry a `companions`
edge. Of the 28 families here, **3** use the word (268, 270, 364).

So the release's own machine-readable cross-reference layer is 2 edges over 372 families, while the
companion relation it describes in prose is at least 10 families wide, and the manuscript-level
citation layer below measures 16 of 28. The `companions` column is not a census of how these results
relate; it is a record of how many abstracts spell a dependency as `result (NNN)`.

## Summary table

Shapes = the ledger's claim-shape tags, `-` for none. `.bib` = LaTeX bibliography files shipped under
the family's two manuscript directories. Edges = intra-family citation edges (see the last section);
Mutual = how many of them form a pair citing in both directions. Anchor = the family's `\resultentry`
line in `overview.tex`.

| Fam | Discipline | Shapes | `.bib` | Edges | Mutual | Anchor |
|---|---|---|---|---|---|---|
| 035 | A&CG | bound, classification | 1 | 0 | 0 | `overview.tex:148` |
| 037 | A&CG | resolution, bound, partial | 1 | 1 | 0 | `overview.tex:152` |
| 041 | A&CG | resolution | 2 | 2 | 1 | `overview.tex:160` |
| 055 | A&CG | uniform | 2 | 0 | 0 | `overview.tex:186` |
| 065 | A&CG | resolution, uniform | 1 | 0 | 0 | `overview.tex:204` |
| 066 | A&CG | bound, classification | 2 | 2 | 1 | `overview.tex:206` |
| 074 | real&complex | resolution, uniform | 2 | 1 | 0 | `overview.tex:222` |
| 077 | real&complex | resolution, bound, uniform | 2 | 2 | 1 | `overview.tex:228` |
| 080 | real&complex | bound, uniform | 1 | 1 | 0 | `overview.tex:234` |
| 138 | TCS | bound, uniform | 1 | 0 | 0 | `overview.tex:353` |
| 147 | dyn sys | resolution, bound | 2 | 1 | 0 | `overview.tex:373` |
| 200 | algebra | resolution, classification, uniform | 0 | 0 | 0 | `overview.tex:481` |
| 203 | algebra | bound, classification, uniform | 1 | 1 | 0 | `overview.tex:487` |
| 217 | prob | classification, uniform | 2 | 2 | 1 | `overview.tex:517` |
| 219 | prob | uniform | 1 | 0 | 0 | `overview.tex:521` |
| 239 | prob | bound, partial, uniform | 0 | 0 | 0 | `overview.tex:561` |
| 258 | group theory | - | 1 | 1 | 0 | `overview.tex:603` |
| 265 | mathphys | bound, partial, uniform | 2 | 2 | 1 | `overview.tex:619` |
| 268 | mathphys | resolution, bound, uniform | 2 | 2 | 1 | `overview.tex:625` |
| 270 | mathphys | resolution, bound, uniform | 1 | 0 | 0 | `overview.tex:629` |
| 286 | opalg | classification, uniform | 2 | 2 | 1 | `overview.tex:664` |
| 300 | opalg | resolution, bound | 0 | 0 | 0 | `overview.tex:692` |
| 302 | opalg | bound, partial, uniform | 2 | 2 | 1 | `overview.tex:696` |
| 308 | topology | uniform | 2 | 0 | 0 | `overview.tex:710` |
| 335 | diffgeom | resolution, uniform | 1 | 0 | 0 | `overview.tex:768` |
| 346 | diffgeom | bound, partial | 2 | 1 | 0 | `overview.tex:790` |
| 364 | PDE | bound, density, uniform | 2 | 0 | 0 | `overview.tex:828` |
| 368 | PDE | resolution, bound, uniform | 2 | 2 | 1 | `overview.tex:837` |

All 28 are T0, all 56 manuscripts carry `formalized = 0`, and 27 of 28 carry no coverage signal at all.

## The 28 families

Each block names both manuscripts by the display title the release gives them (verbatim, from the
family's `\resultentry` line) and the PDF path. The pairing line is a **reading judgement** made from
the two titles and the abstract clauses — it is not a release record, and no manuscript proof was read
to make it. The scope-limit clause is quoted from the overview abstract, which is the release's
rewritten paraphrase of the manuscript abstract, not the manuscript abstract.

### 035 — Threefold log abundance in numerical dimension one in characteristic $p>3$

- **1** (`overview.tex:148`) — *"Log abundance in numerical dimension one for threefolds in positive characteristic"*
  → `preprints/Log-abundance-in-numerical-dimension-one-for-threefolds-in-positive-characteristic-October-5-2026/paper.pdf`
- **2** (`overview.tex:148`) — *"Abundance in numerical dimension one for terminal threefolds in positive characteristic"*
  → `preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/paper.pdf`

Pairing: the headline drops the terminal and $\mathbb Q$-factorial hypotheses; manuscript 2 keeps
them. Scope limit (`overview.tex:148`) — *"when the effective boundary is rational and the $\mathbb
Q$-Cartier adjoint is nef of numerical dimension one"*. Citation layer: 1 `.bib` file, 0 intra-family
edges, 0 mutual pair.

### 037 — The sharp ordinary-double-point volume gap

- **1** (`overview.tex:152`) — *"Gap in every dimension"*
  → `preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/paper.pdf`
- **2** (`overview.tex:152`) — *"Dimension-four normalized-volume gap"*
  → `preprints/The-normalized-volume-gap-in-dimension-four-September-24-2026/paper.pdf`

Pairing: all-dimension theorem plus the dimension-four case. Scope limit (`overview.tex:152`) — *"with
zero boundary, has normalized volume at most $2(n-1)^n$"*. Citation layer: 1 `.bib` file, 1
intra-family edges, 0 mutual pair.

### 041 — Hyperk\"ahler SYZ and projective-space bases

- **1** (`overview.tex:160`) — *"Projective-space bases"*
  → `preprints/Projective-Space-Bases-of-Lagrangian-Fibrations-September-23-2026/main.pdf`
- **2** (`overview.tex:160`) — *"Strong hyperkähler SYZ"*
  → `preprints/The-Strong-Hyperkahler-SYZ-Conjecture-September-23-2026/main.pdf`

Pairing: one manuscript per named claim. Scope limit (`overview.tex:160`) — *"every holomorphic line
bundle with nonzero nef isotropic first Chern class on a compact irreducible holomorphic symplectic
K\"ahler manifold is semiample"*. Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.

### 055 — Toda's Gepner conjecture and large-volume stability

- **1** (`overview.tex:186`) — *"Gepner stability on quintic threefolds"*
  → `preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/paper.pdf`
- **2** (`overview.tex:186`) — *"Prescribed large-volume charges"*
  → `preprints/Prescribed-large-volume-charges-on-threefolds-with-trivial-canonical-bundle-September-24-2026/paper.pdf`

Pairing: the named conjecture, then the general large-volume family it sits inside. Scope limit
(`overview.tex:186`) — *"constructing a numerical Bridgeland stability condition with the prescribed
phase shift $2/5$"*. Citation layer: 2 `.bib` files, 0 intra-family edges, 0 mutual pair.

### 065 — Virasoro constraints for complete intersections and projective bundles

- **1** (`overview.tex:204`) — *"Virasoro Constraints under Projectivization"*
  → `preprints/Virasoro-Constraints-under-Projectivization-October-5-2026/virasoro-constraints-under-projectivization.pdf`
- **2** (`overview.tex:204`) — *"Virasoro Constraints for Projective Complete Intersections"*
  → `preprints/Virasoro-Constraints-for-Projective-Complete-Intersections-September-24-2026/article.pdf`

Pairing: the base case, then the transfer under projectivization. Scope limit (`overview.tex:204`) —
*"to the projectivization of every algebraic vector bundle of rank at least two"*. Citation layer: 1
`.bib` files, 0 intra-family edges, 0 mutual pair.

### 066 — Bounded klt complements for Fano contractions

- **1** (`overview.tex:206`) — *"Bounded klt complements"*
  → `preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf`
- **2** (`overview.tex:206`) — *"Uniform Cartier sections"*
  → `preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf`

Pairing: the complement theorem and the uniform-sections machinery. Scope limit (`overview.tex:206`) —
*"with index bounded only by dimension and positive rational $\epsilon$"*. Citation layer: 2 `.bib`
files, 2 intra-family edges, 1 mutual pair.

### 074 — Kakeya in three and four dimensions

- **1** (`overview.tex:222`) — *"3D Kakeya maximal conjecture"*
  → `preprints/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/paper.pdf`
- **2** (`overview.tex:222`) — *"4D Kakeya Hausdorff dimension"*
  → `preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/paper.pdf`

Pairing: two different conjectures at two different dimensions — not one conjecture in two dimensions.
Scope limit (`overview.tex:222`) — *"Resolves the Kakeya maximal conjecture in three dimensions and the
Hausdorff-dimension conjecture in four."* Citation layer: 2 `.bib` files, 1 intra-family edges, 0
mutual pair.

### 077 — Fourier restriction for positively curved surfaces

- **1** (`overview.tex:228`) — *"Sphere restriction"*
  → `preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf`
- **2** (`overview.tex:228`) — *"Diagonal Fourier extension"*
  → `preprints/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026/Diagonal-Fourier-extension-for-positively-curved-surfaces-in-three-dimensions-September-24-2026.pdf`

Pairing: the sphere case, then the general positively curved surface. Scope limit (`overview.tex:228`)
— *"the extension operator is bounded from $L^p(\Sigma)$ to $L^p(\mathbb R^3)$ for every $p>3$"*.
Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.

### 080 — The Sobolev endpoint in Carleson's Schr\"odinger convergence problem

- **1** (`overview.tex:234`) — *"Planar endpoint convergence"*
  → `preprints/Endpoint-convergence-for-the-planar-Schrodinger-equation-September-24-2026/paper.pdf`
- **2** (`overview.tex:234`) — *"Higher-dimensional endpoint convergence"*
  → `preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/paper.pdf`

Pairing: the planar endpoint, then every dimension. Scope limit (`overview.tex:234`) — *"for every $f
\in H^{n/(2(n+1))}(\mathbb R^n)$ and every dimension $n\ge2$"*. Citation layer: 1 `.bib` file, 1
intra-family edges, 0 mutual pair.

### 138 — Subset Sum in $O(2^{0.49n})$ time

- **1** (`overview.tex:353`) — *"Subset Sum in Time $O(2^{0.49n})$"*
  → `preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf`
- **2** (`overview.tex:353`) — *"A Low-Space Algorithm for Worst-Case Subset Sum"*
  → `preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf`

Pairing: the time bound and the space bound — two resources, not two theorems. Scope limit
(`overview.tex:353`) — *"The time bound holds on every execution and success probability is at least
$2/3$ on every input."* Citation layer: 1 `.bib` file, 0 intra-family edges, 0 mutual pair.

### 147 — The near-boundary Birkhoff conjecture

- **1** (`overview.tex:373`) — *"Analytic caustic collars"*
  → `preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf`
- **2** (`overview.tex:373`) — *"Billiard rigidity"*
  → `preprints/Rigidity-of-Smooth-Billiards-with-a-Continuous-Caustic-Collar-September-24-2026/paper.pdf`

Pairing: the mechanism that produces a collar, then the rigidity conclusion it feeds. Scope limit
(`overview.tex:373`) — *"Such a billiard is an ellipse whenever a full grazing annulus is continuously
foliated by individually invariant essential curves."* Citation layer: 2 `.bib` files, 1 intra-family
edges, 0 mutual pair.

### 200 — Eisenbud--Green--Harris and lex-plus-powers in characteristic zero

- **1** (`overview.tex:481`) — *"Artinian lex-plus-powers Betti theorem"*
  → `preprints/The-Artinian-Lex-Plus-Powers-Betti-Theorem-September-23-2026/paper.pdf`
- **2** (`overview.tex:481`) — *"Commuting division-coefficient forms"*
  → `preprints/Commuting-Division-Coefficient-Forms-and-the-Artinian-Eisenbud-Green-Harris-Conjecture-September-23-2026/paper.pdf`

Pairing: the two named conjectures, one per manuscript. Scope limit (`overview.tex:481`) — *"of
arbitrary length and degrees at least two, admits a lex-plus-powers ideal with the same Hilbert
function and no smaller graded Betti numbers"*. Citation layer: 0 `.bib` files, 0 intra-family edges,
0 mutual pair.

### 203 — Donovan's conjecture over fields and discrete valuation rings

- **1** (`overview.tex:487`) — *"Donovan over algebraically closed fields"*
  → `preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/main.pdf`
- **2** (`overview.tex:487`) — *"Integral Donovan over Witt vectors"*
  → `preprints/Integral-Donovan-Finiteness-over-Witt-Vectors-September-25-2026/main.pdf`

Pairing: the field form, then the integral form. Scope limit (`overview.tex:487`) — *"over each fixed
algebraically closed field of characteristic $p$, blocks of finite groups with bounded defect-group
order have only finitely many Morita-equivalence classes, for every prime $p$"*. Citation layer: 1
`.bib` files, 1 intra-family edges, 0 mutual pair.

### 217 — The low-temperature Sherrington--Kirkpatrick fluctuation law

- **1** (`overview.tex:517`) — *"Free-energy limiting law"*
  → `preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf`
- **2** (`overview.tex:517`) — *"Fluctuation scale"*
  → `preprints/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-fluctuation-scale-September-24-2026.pdf`

Pairing: the limiting law and the scale it fluctuates at. Scope limit (`overview.tex:517`) — *"For
every fixed inverse temperature $\beta>1$"*. Citation layer: 2 `.bib` files, 2 intra-family edges, 1
mutual pair.

### 219 — GOE universality for random regular graphs with weak disorder

- **1** (`overview.tex:521`) — *"Fixed-energy universality for weak Anderson disorder on random regular graphs"*
  → `preprints/Fixed-energy-universality-for-weak-Anderson-disorder-on-random-regular-graphs-October-5-2026/fixed-energy-universality-weak-anderson-disorder-random-regular-graphs.pdf`
- **2** (`overview.tex:521`) — *"GOE bulk universality for fixed-degree random regular graphs"*
  → `preprints/GOE-bulk-universality-for-fixed-degree-random-regular-graphs-September-23-2026/paper.pdf`

Pairing: the clean graph, then the disordered graph. Scope limit (`overview.tex:521`) — *"throughout
compact bands strictly inside the clean spectral edges"*. Citation layer: 1 `.bib` file, 0
intra-family edges, 0 mutual pair.

### 239 — Sharp singularity rates for symmetric sign matrices

- **1** (`overview.tex:561`) — *"The sharp exponential rate of singularity for symmetric Bernoulli matrices"*
  → `preprints/The-sharp-exponential-rate-of-singularity-for-symmetric-Bernoulli-matrices-October-3-2026/symmetric-bernoulli-singularity.pdf`
- **2** (`overview.tex:561`) — *"The sharp singularity rate for biased symmetric sign matrices"*
  → `preprints/The-sharp-singularity-rate-for-biased-symmetric-sign-matrices-October-4-2026/biased-symmetric-sign-singularity.pdf`

Pairing: uniform signs, then biased signs. Scope limit (`overview.tex:561`) — *"symmetric random sign
matrices with independent entries on and above the diagonal"*. Citation layer: 0 `.bib` files, 0
intra-family edges, 0 mutual pair.

### 258 — Gersten's conjecture for one-relator groups

- **1** (`overview.tex:603`) — *"Baumslag–Solitar-free one-relator groups"*
  → `preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/paper.pdf`
- **2** (`overview.tex:603`) — *"Virtual compact specialness"*
  → `preprints/Virtual-compact-specialness-of-hyperbolic-one-relator-groups-September-25-2026/paper.pdf`

Pairing: the two claims of the family; 258 is the only population family with no claim-shape tag at
all. Scope limit (`overview.tex:603`) — *"containing no Baumslag--Solitar subgroup $\mathrm{BS}(m,n)$,
with $m,n\ne0$, is word-hyperbolic"*. Citation layer: 1 `.bib` file, 1 intra-family edges, 0 mutual
pair.

### 265 — The two-dimensional gapped area law

- **1** (`overview.tex:619`) — *"Two-dimensional area law"*
  → `preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf`
- **2** (`overview.tex:619`) — *"Polynomial PEPS approximation"*
  → `preprints/Polynomial-PEPS-approximation-of-gapped-square-grid-ground-states-September-24-2026/paper.pdf`

Pairing: the entropy law, then the tensor-network approximation. Scope limit (`overview.tex:619`) —
*"using only a uniform full-system spectral gap and bounds on the local interactions"*. Citation layer:
2 `.bib` files, 2 intra-family edges, 1 mutual pair.

### 268 — The spin-one Haldane gap

- **1** (`overview.tex:625`) — *"Periodic Haldane gap"*
  → `preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf`
- **2** (`overview.tex:625`) — *"Boundary-field gap"*
  → `preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/paper.pdf`

Pairing: the release calls 2 explicitly a companion (`overview.tex:625`) — *"A companion establishes
a gap for odd open chains with endpoint field $h=3/5$ and gives boundary-selected infinite-volume
states with topological index $-1$."* The headline's scope limit is the geometry it covers — *"for the
pure antiferromagnetic Heisenberg chain on even periodic rings"*.
Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.

### 270 — Threshold and positive-energy bound states of the BFSS model

- **1** (`overview.tex:629`) — *"The unique threshold bound state of the SU(N) BFSS model"*
  → `preprints/The-unique-threshold-bound-state-of-the-SU-N-BFSS-model-September-24-2026/paper.pdf`
- **2** (`overview.tex:629`) — *"Positive eigenvalues of the relative SU(2) BFSS Hamiltonian"*
  → `preprints/Positive-eigenvalues-of-the-relative-SU-2-BFSS-Hamiltonian-October-5-2026/positive-eigenvalues-relative-su2-bfss.pdf`

Pairing: the headline at every $N$, then the companion at $N=2$, which the release records as
contradicting an external paper (`overview.tex:629`) — *"For $\mathrm{SU}(2)$, a companion proves
infinitely many normalizable positive-energy eigenstates with unbounded energies"*. Scope limit of the
headline — *"has exactly one normalizable zero-energy state for every finite $N\ge2$"*.
Citation layer: 1 `.bib` file, 0 intra-family edges, 0 mutual pair.

### 286 — Arithmetic rigidity of lattice von Neumann algebras

- **1** (`overview.tex:664`) — *"Twisted finite correspondences"*
  → `preprints/Arithmeticity-of-twisted-finite-correspondences-for-lattices-over-local-fields-September-23-2026/paper.pdf`
- **2** (`overview.tex:664`) — *"Arithmetic category and stable recovery"*
  → `preprints/The-arithmetic-category-and-stable-recovery-of-lattice-factors-September-23-2026/paper.pdf`

Pairing: the bimodule classification, then the recovery of the group data from it. Scope limit
(`overview.tex:664`) — *"between scalar-twisted group factors of ICC groups commensurable with
property-$(T)$ lattices over characteristic-zero local fields and arbitrary ICC group factors"*.
Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.

### 300 — The Popa--Vaes quadratic strong-operator paving conjecture

- **1** (`overview.tex:692`) — *"Approximation paving"*
  → `preprints/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Approximation-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf`
- **2** (`overview.tex:692`) — *"Quadratic strong-operator paving"*
  → `preprints/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026/Quadratic-Strong-Operator-Paving-over-Arbitrary-Maximal-Abelian-Subalgebras-September-25-2026.pdf`

Pairing: the approximation form, then the quadratic form the family is named for. Scope limit
(`overview.tex:692`) — *"admits strong-operator paving relative to any maximal abelian subalgebra with
$O(\varepsilon^{-2})$ blocks"*. Citation layer: 0 `.bib` files, 0 intra-family edges, 0 mutual pair.

### 302 — The Phillips--Toms formula for minimal integer actions

- **1** (`overview.tex:696`) — *"Boundary-preserving cobordism compression"*
  → `preprints/Filtered-products-and-boundary-preserving-compression-in-complex-cobordism-September-25-2026/paper.pdf`
- **2** (`overview.tex:696`) — *"Radius $=\frac12$ mean dimension"*
  → `preprints/Radius-of-comparison-equals-half-the-mean-dimension-September-25-2026/paper.pdf`

Pairing: the compression tool, then the radius-of-comparison formula. Scope limit (`overview.tex:696`)
— *"the radius of comparison of $C(X)\rtimes_h\mathbb Z$ equals $\tfrac12\mathrm{mdim}(X,h)$,
including infinite values"*. Citation layer: 2 `.bib` files, 2 intra-family edges, 1 mutual pair.

### 308 — Smith--Toda complexes at every height with varying primes

- **1** (`overview.tex:710`) — *"Varying primes"*
  → `preprints/Finite-Smith-Toda-Complexes-at-Varying-Primes-September-23-2026/paper.pdf`
- **2** (`overview.tex:710`) — *"V(4) at prime 1009"*
  → `preprints/A-finite-Smith-Toda-complex-V4-at-the-prime-1009-September-23-2026/paper.pdf`

Pairing: the general construction, then the single explicit instance. Scope limit (`overview.tex:710`)
— *"constructs a finite Smith--Toda spectrum at a prime $p$ depending on $n$"*. Citation layer: 2
`.bib` files, 0 intra-family edges, 0 mutual pair.

### 335 — Gromov's integral scalar-curvature inequality

- **1** (`overview.tex:768`) — *"An integral scalar curvature bound for real simplicial volume"*
  → `preprints/An-integral-scalar-curvature-bound-for-real-simplicial-volume-October-5-2026/v126-proof.pdf`
- **2** (`overview.tex:768`) — *"Positive scalar curvature forces rational inessentiality"*
  → `preprints/Positive-scalar-curvature-forces-rational-inessentiality-September-23-2026/paper.pdf`

Pairing: the integral inequality, then the Gromov--Lawson resolution. Scope limit (`overview.tex:768`)
— *"for every closed connected oriented smooth $n$-manifold, $n\ge3$, and every smooth metric, with
$a_n>0$ depending only on dimension"*. Citation layer: 1 `.bib` file, 0 intra-family edges, 0 mutual
pair.

### 346 — Sharp singular-set bounds for stationary integral varifolds

- **1** (`overview.tex:790`) — *"A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold"*
  → `preprints/A-Codimension-One-Bound-for-the-Singular-Set-of-a-Stationary-Integral-Varifold-October-5-2026/varifold-singular-dimension.pdf`
- **2** (`overview.tex:790`) — *"Almost-everywhere regularity of stationary integral varifolds"*
  → `preprints/Almost-everywhere-regularity-of-stationary-integral-varifolds-September-23-2026/paper.pdf`

Pairing: the dimension bound, then measure-zero regularity on spheres. Scope limit
(`overview.tex:790`) — *"has singular set of Hausdorff dimension at most $m-1$, a sharp bound in every
positive dimension and codimension"*. Citation layer: 2 `.bib` files, 1 intra-family edges, 0 mutual
pair.

### 364 — Kinetic limits and fluctuations over the Boltzmann lifespan

- **1** (`overview.tex:828`) — *"Boltzmann–Grad limit for stable radial potentials"*
  → `preprints/The-Boltzmann-Grad-limit-for-stable-radial-potentials-on-regular-kinetic-intervals-September-23-2026/paper.pdf`
- **2** (`overview.tex:828`) — *"Hard-sphere fluctuations"*
  → `preprints/Hard-sphere-fluctuations-on-the-regular-Boltzmann-lifespan-September-23-2026/paper.pdf`

Pairing: the derivation, then the companion's fluctuation theorem. Scope limit (`overview.tex:828`) —
*"Stable finite-range radial potentials may have attractive wells and a singular repulsive core;
initial pair exclusion and spatially summable Gaussian density and gradient bounds are assumed."*
Citation layer: 2 `.bib` files, 0 intra-family edges, 0 mutual pair.

### 368 — The three-dimensional Ball--Evans approximation problem

- **1** (`overview.tex:837`) — *"Diffeomorphic approximation, $1\le p\le2$"*
  → `preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf`
- **2** (`overview.tex:837`) — *"Diffeomorphic approximation, $p>2$"*
  → `preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf`

Pairing: the family's resolution is split at $p=2$ across the two manuscripts, and the overview
abstract states only the merged conclusion (`overview.tex:837`) — *"every $W^{1,p}$ homeomorphism
between arbitrary bounded domains in $\mathbb R^3$, for $1\le p<\infty$, is a strong $W^{1,p}$ limit of
smooth diffeomorphisms onto the same target."* Citation layer: 2 `.bib` files, 2 intra-family edges, 1
mutual pair.

## The intra-family citation layer

Rule: a manuscript-to-manuscript edge inside one family, where the citing file is a `.bib` entry
carrying the release's own `OpenAI Math Release` note, its `href` target is a
`preprints/<dir>/<file>.pdf` that exists on disk, and the citing and cited directories belong to the
same family. Manuscript ownership is the path component after `preprints`, never the second-to-last
component — keying by `parts[-2]` files these manuscripts under `build/` and makes every edge
disappear.

**16** of the 28 cite their sibling: **9** mutual pairs and **7** one-directional. **12** cite no
sibling, and **3** of those (200, 239, 300) ship no `.bib` file at all, so their absence is
unmeasurable rather than a negative.

The mutual pairs are 041, 066, 077, 217, 265, 268, 286, 302, 368. The one-directional edges are 037,
074, 080, 147, 203, 258, 346. Direction is informative in the one-directional cases: 074's
four-dimensional manuscript cites its three-dimensional sibling, 080's higher-dimensional manuscript
cites the planar one, 203's integral form cites the field form, 147's caustic-collar mechanism cites
the rigidity conclusion, 258's hyperbolicity paper cites the specialness paper, 346's codimension-one
bound cites the regularity paper, and 037's every-dimension gap cites the dimension-four gap.

The 12 with no intra-family edge are 035, 055, 065, 138, 200, 219, 239, 270, 300, 308, 335, 364. Three
of them (200, 239, 300) ship no `.bib` file; the other nine ship at least one and cite only external
literature. 270 is the notable case: its companion is announced in prose in the overview abstract and
the two manuscripts share no bibliography edge.

## The 268 exception to "no coverage signal"

The bead describes the 28 as "the group with two manuscripts and no coverage signal". That is true of
**27**; 268 carries `verification = 2`. Both of its manuscripts ship a `verification/` directory:
`preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/verification/` and
`preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/verification/`.
The second carries a README, two Python checkers, and four JSON result files.

Source-level, stated at source level: those are finite-arithmetic certificate scripts and their
recorded outputs. Nothing here says a certificate was run, and nothing here says a theorem was checked
— this page runs nothing. 268 is T0 because it has no scope note, no comparator challenge, and no
`main_results` entry; a verification bundle is not coverage in the tier rule.

## What has not been checked

- No Lean, lake, or comparator run. The `formalized = 0` flags are the ledger's read of
  `lean/formalization.yaml`, not evidence about any manuscript.
- Every abstract quoted here is the release's rewritten paraphrase in `overview.tex`, not the
  manuscript abstract — 0 of 722 manuscript comparisons read identical or abridged
  (`notes/abstracts.md`), so a scope-limit clause quoted from the overview is a claim about the
  summary.
- Pairing labels are reading judgements from titles and overview clauses. No manuscript proof,
  theorem environment, or hypothesis list was read for any of the 28; 311 is the only family on this
  page read at manuscript level, and only its introduction and bibliography entry were read.
- No literature check. The Barthel--Heard--Naumann implication is quoted from 311's own prose; the
  published paper was not read, and its `Theorems~4.9 and~4.15` numbering is unverified.
- The intra-family edge rule sees `.bib` hrefs only. A manuscript that cites its sibling in prose, in
  a footnote, or in a bibliography block that is not a `.bib` file is not counted, and 3 families ship
  no `.bib` at all.
- No authorship check: whether the two manuscripts of a family share authors is not measured.
- The chain families' abstracts were quoted, not verified against their manuscripts; the claim that
  032's theorems give the Tate and Hodge standard conjectures is the release's claim, unverified.
- The 8 first-pass T0 two-manuscript families (004, 006, 018, 019, 029, 046, 059, 209) are outside
  this page by construction; 006 is itself a chain family and is read in `notes/t0-triage.md`.
