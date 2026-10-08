# The named-result inventory in the manuscript sources, checked against `resolves_named`

## Population

The ledger's `resolves_named` column is a title-and-abstract heuristic: `notes/scripts/build_catalog.py:215`
returns 1 when a family's **overview abstract** matches both `TARGET_NOUN`
(`conjectur|\bquestion|\bproblem`) and `RESOLVE_VERB`
(`\bprov(?:e|es|ed|ing)\b|\bdisprov|\brefut|\bresolv|\banswer|\bsettl|\bestablis|\bconfirm|\bfail|\bviolat|\bcounterexample`).
It reads **233** of **372** families. This page measures the manuscript side of the same claim and
compares the two.

Regenerate with `python3 notes/scripts/extract_named_results.py` — report-only, it writes nothing and
runs nothing; `lake`, `lean`, `lake exe cache get`, and `comparator` are never invoked here, so nothing
on this page means "a proof was checked". Run it twice and diff: the report must be identical. Check
this page with `python3 notes/scripts/verify_named_results.py --mutant` before quoting any of its
counts — it imports the extractor's own `population()`, re-derives every count from the ledger and the
7,401 `.tex` files on disk, resolves every `file:line` anchor, matches every quotation against the
anchored file, and flags twelve injected mutations. It writes nothing.

Population, from the report's POPULATION section: **372** ledger rows, **372** families in
`overview.tex`, **722** manuscript directories, **7,401** `.tex` files at glob depths 1–4 under
`preprints/`, and `resolves_named = 1` on **233** families.

Manuscript ownership is the path component after `preprints`, never `parts[-2]` — every resolved main
file sits under a `build/` directory, so a `parts[-2]` read files manuscripts under `build/` and
`sections/` and matches no family.

## The headline inventory

Rule: `\begin{X}` at any position in a manuscript `.tex` file, for X in `theorem`, `maintheorem`,
`thm`. That is the **headline** set — the statement environments whose names the release's own
numbering uses. It is deliberately narrow: `conjecture`, `thmstar`, `theoremA`, `theoremB`, `mainthm`
and `theoremstar` all read **0** begins, so no headline statement is being counted under a
conjecture environment.

| Measure | Count | Rule |
|---|---|---|
| headline begins | 2,270 | `\begin{theorem}` 2,265, `\begin{maintheorem}` 4, `\begin{thm}` 1 |
| titled headline begins | 1,498 | `\begin{X}[title]`, scanned **per line** |
| titled headline begins, whole-text scan | 1,508 | same pattern over the whole file |
| of those, titles whose match spans a newline | 10 | the 1,498 / 1,508 gap |
| families with ≥1 headline begin | 372 | every family |
| families with ≥1 titled headline | 271 | |
| families with no titled headline | 101 | |
| titles matching `Main…` (content-free) | 0 | no generic headline titles exist |

Quote the titled count with the per-line rule: **1,498** is the per-line scan, **1,508** is the
whole-text scan, and the 10-title gap is titles written across a line break. A page that quotes 1,508
with the per-line rule is quoting the wrong number.

## Target-named headline statements: 17 over 17 families

Rule: a titled headline statement whose **title** matches the target noun, case-insensitively. The
case-insensitivity is stated because it changes the count: the ledger rule sees lowercase abstracts,
while titles, directory names, and prose capitalize the same words, so a case-sensitive match on them
undercounts.

Over **1,498** titled headline statements, **17** titles name a conjecture, question, or problem, in
**17** families:

| Fam | Tier | `rn` | Statement | Title |
|---|---|---|---|---|
| 006 | T0 | 1 | `preprints/Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-September-23-2026/build/sections/00-introduction.tex:35` | *"Goldfeld's analytic density conjecture"* |
| 013 | T2 | 1 | `preprints/the-additive-indecomposability-of-the-primes-September-24-2026/build/sections/01-introduction.tex:15` | *"Ostmann's conjecture"* |
| 060 | T0 | 1 | `preprints/Global-Spherical-Shells-on-Minimal-Surfaces-of-Class-VII-September-24-2026/build/paper.tex:102` | *"Global Spherical Shell conjecture"* |
| 072 | T3 | 1 | `preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/00-introduction.tex:52` | *"Brennan's conjecture and inverse-square means"* |
| 074 | T0 | 1 | `preprints/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/build/sections/02-framework.tex:1160` | *"Reduction to a bad weighted problem"* |
| 087 | T3 | 1 | `preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/build/sections/00-introduction.tex:26` | *"General Mahler conjecture"* |
| 119 | T3 | 1 | `preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/build/main.tex:54` | *"Hellinger conjecture"* |
| 186 | T2 | 1 | `preprints/A-Sharp-Threshold-Bound-for-Monotone-Graph-Properties-September-25-2026/build/sections/introduction.tex:12` | *"Friedgut--Kalai sharp-threshold conjecture"* |
| 194 | T2 | 1 | `preprints/Lechs-multiplicity-conjecture-September-23-2026/build/main.tex:80` | *"Lech's conjecture"* |
| 203 | T0 | 1 | `preprints/Donovans-Conjecture-over-Algebraic-Closures-of-Prime-Fields-September-24-2026/build/sections/00_introduction.tex:27` | *"Donovan's conjecture"* |
| 205 | T3 | 1 | `preprints/A-Cyclic-Polytabloid-Proof-of-Saxls-Conjecture-September-24-2026/build/sections/introduction.tex:18` | *"Saxl's conjecture"* |
| 245 | T2 | 1 | `preprints/Weak-and-strong-normalization-in-pure-type-systems-September-25-2026/build/sections/introduction.tex:116` | *"The $\beta$-Barendregt--Geuvers--Klop conjecture"* |
| 246 | T2 | 1 | `preprints/A-Modulus-Proof-of-Cannons-Conjecture-September-23-2026/build/main.tex:94` | *"Cannon's conjecture"* |
| 263 | T3 | 0 | `preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/build/sections/01-introduction.tex:38` | *"Generalized ionization conjecture: radii"* |
| 275 | T2 | 0 | `preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/build/sections/01-finite-models.tex:19` | *"Source problem"* |
| 304 | T0 | 1 | `preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026/build/sections/01-introduction.tex:9` | *"The Hilbert--Smith conjecture"* |
| 311 | T0 | 1 | `preprints/Stabilizer-Orbits-and-Thick-Tensor-Ideals-of-Dualizable-Kn-Local-Spectra-September-24-2026/build/sections/01-introduction.tex:74` | *"Hovey--Strickland conjecture"* |

**The load-bearing negative: 0 of these 17 titles pairs a target noun with a resolve verb.** A
theorem title names *content* — "General Mahler conjecture", "Source problem" — never the act of
resolving it. So the statement layer cannot, by itself, back a column whose rule is
target-noun **and** resolve-verb. Two of the 17 (263, 275) sit in families the column reads 0; the
other 15 sit in families it reads 1.

## Subject-named headline statements: 208 over 112 families

Rule: a titled headline statement whose title contains a **name-layer subject** — one of the 552
subject names measured by `notes/scripts/measure_names.py` (subjects, not citations; the rule and the
subject/citation split are in `notes/names.md`).

**208** statements over **112** families. **68** of those families are `rn = 1`; **44** are not:
002 009 010 014 015 022 023 036 069 096 097 099 114 115 116 125 140 211 212 216 218 222 223 224 227
231 232 238 239 260 261 271 275 282 286 289 297 318 331 337 347 353 376 377.

This is the layer that shows the column is not a *name* detector: 44 families name a person, theorem,
or object in a headline theorem title while the column reads 0, and it names them in the theorem's own
name, not as a resolved conjecture.

## Cross-tabs against `resolves_named`

| Comparison | Count |
|---|---|
| headline-target ∩ `rn` | 15 |
| headline-target, `rn = 0` | 2 → 263 275 |
| `rn = 1`, no target-named headline statement | 218 |
| `rn = 1` with **no titled headline theorem at all** | 71 (T3 35, T2 23, T1 0, T0 13) |
| `rn = 0` with titled headline theorems | 109 |

The 71 is the number that decides the bead's framing: **71 of the 233 flagged families ship no titled
headline theorem**, so for those families there is no statement-level text in which a named-result
claim could be recorded at all. The column's evidence is not statement-level anywhere near them.

## Layer 1 — the manuscript's own name names a target

Rule: the directory name after `preprints` matches the target noun, case-insensitively.

**76** families over **89** directories. **67** are `rn = 1`. **9** are not: 022 039 044 151 209 297
354 365 372. **166** `rn = 1` families have no directory name naming a target.

## Layer 2 — the manuscript's own abstract names a target with a resolve verb

Rule: inside the manuscript's own `\begin{abstract}`…`\end{abstract}` (bibliography and `\cite` braces
stripped), one sentence matching the target noun **and** the column's resolve verb.

**275** families over **398** sentences. **212** are `rn = 1`. **63** are not, and **21** `rn = 1`
families have no such sentence: 020 027 085 094 124 126 129 134 144 155 158 160 187 191 277 280 299
309 322 323 342.

The 63 is the widest candidate set on the page and it is **unadjudicated**: it includes families whose
manuscript abstract uses "problem" for its own technical sub-problem. Taken raw it would read 233 + 63
= **296**; the page does not endorse that number.

## Layer 3 — manuscript prose

Rule: prose text with bibliography and `\cite`/`\xref` braces stripped, two scopes.

| Scope | Hits | Families | ∩`rn` | prose-not-`rn` | `rn`-not-prose |
|---|---|---|---|---|---|
| window ±80 characters | 1,674 | 337 | 225 | 112 | 8 → 085 094 126 144 187 299 323 333 |
| one sentence | 1,291 | 332 | 223 | 109 | 10 → 020 085 094 144 158 187 280 299 322 323 |

**6** families are `rn = 1` and name no target anywhere in their manuscript prose under **both** rules:
085 094 144 187 299 323.

## The verb-vocabulary gap

Rule: a prose sentence with a target noun and one of the verbs the column's `RESOLVE_VERB` does not
carry — `solve/solves/solved`, `resolution`, `answer/answers`, `settled`, `settling`, `negatively`,
`positively`, `refutation`, `counterexample(s)` — and none of the column's verbs.

**5** families: 085 138 144 234 358, of which **2** are `rn = 1`. Read, the five split:

- 085 — *"This gives a positive resolution of the planar centered-disk case of the endpoint question
  of Haj{\l}asz and Onninen."* (`preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/build/main.tex:51`)
  — a real named pairing the column's verb list misses.
- 144 — *"We solve the probability-preserving form of Banach's simple Lebesgue-spectrum problem in
  smooth dynamics."* (`preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/main.tex:45`)
  — a real named pairing; "solve" is not in `RESOLVE_VERB`.
- 138 — *"We study the memory needed to solve this problem while retaining running time polynomial
  times $2^{n/2}$."* (`preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/introduction.tex:9`)
  — "this problem" is the manuscript's own memory/space sub-problem. **Not** a named-result pairing.
- 234 — *"We solve this problem for every fixed temperature when the limiting spectral law is
  compactly supported and there are no asymptotic outliers."*
  (`preprints/All-temperature-pressure-for-orthogonally-invariant-Ising-spin-glasses-September-25-2026/build/invariant-sk.tex:81`)
  — "this problem" is its pressure formula. **Not** a named-result pairing.
- 358 — *"Uniformization then supplies a flat or negatively curved metric, so the existence problem
  begins in dimension three."*
  (`preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/build/sections/introduction.tex:19`)
  — background prose. **Not** a named-result pairing.

So the verb gap is real for 2 families and is a self-framed sub-problem for 3. Widening
`RESOLVE_VERB` on the strength of this list would add 3 false flags for 2 true ones.

## The title-scope candidate: 233 → 247

Rule: target noun in the family's **overview title**, resolve verb in its overview abstract. The
column reads the abstract only; this is the same generator's precedent — `counterex_broad` is
documented at `notes/scripts/build_catalog.py:238` as
*"Input scope is title + abstract, stated because it changes the count"*.

**14** additions: 022 039 044 096 097 151 156 192 209 263 289 297 347 367. **Removals 0** — a union
keeps every current flag, so the union column reads **247**. A strict title+abstract *replacement*
would read 149 (98 removals), which is why the candidate is a union and not a scope swap.

All **14** are corroborated by a manuscript-abstract naming sentence (layer 2, count ≥ 1). **8** of the
14 are not directory-named: 096 097 156 192 263 289 347 367. Their manuscript abstracts:

- 096 — *"We prove the Gaussian propeller conjecture:"*
  (`preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/main.tex:36`)
- 097 — *"This determines the Euclidean Steinitz constant up to absolute factors, $S_2(d)=\Theta(\sqrt d)$, and resolves the Euclidean Steinitz--Bergstr\"om conjecture."*
  (`preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/main.tex:44`)
- 156 — *"It therefore gives a counterexample to Borsuk's conjecture in dimension nine."*
  (`preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/build/main.tex:14`)
- 192 — *"We disprove the Gopalan--Servedio square-root conjecture, even up to an arbitrary constant factor."*
  (`preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/build/main.tex:27`)
- 289 — *"This resolves the strong Kadison--Kastler conjecture."*
  (`preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/build/main.tex:13`),
  *"We disprove the separable $C^*$-algebraic spatial form of the Kadison--Kastler conjecture."*
  (`preprints/Close-Separable-Cstar-Algebras-Without-Spatial-Conjugacy-October-5-2026/build/main.tex:41`),
  *"We give a negative answer to the unrestricted small-spatial-embedding problem for one-sided near
  inclusions of von Neumann algebras."*
  (`preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026/build/main.tex:39`)
- 347 — *"Thus the example disproves the unrestricted critical-number and rational cup-length forms of the Arnold conjecture."*
  (`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/main.tex:36`),
  *"This disproves the Morse-number form of the Arnold conjecture."*
  (`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/main.tex:44`)
- 367 — *"We prove that seven is the critical dimension for the one-phase Bernoulli problem:"*
  (`preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/build/paper.tex:44`)

**The union does not cover everything the source names.** 354, 365 and 372 are directory-named and
manuscript-abstract-named but **not** title-named, so they sit outside the 14. The manuscript-abstract
layer alone (63 families) would cover them and reach 296, and that layer is unadjudicated.

## Direction A — the source names a target, the column reads 0

**11** families. Ten are real; one is the rule's false positive.

Seven are named in the **overview title** while the overview abstract carries only a prove-verb, so the
abstract-only rule cannot see them: 022 (`overview.tex:120`), 039 (`:156`), 044 (`:166`), 151
(`:381`), 209 (`:499`), 297 (`:686`), 263 (`:615`). Three are named by **manuscript name plus
manuscript abstract only**: 354 (`overview.tex:806`), 365 (`:830`), 372 (`:846`).

- 022 — *"We prove the weak inhomogeneous Duffin--Schaeffer conjecture."*
  (`preprints/The-weak-inhomogeneous-Duffin-Schaeffer-conjecture-September-25-2026/build/main.tex:37`)
- 039 — *"This resolves positively the qualitative Nagata--Biran conjecture for surfaces."*
  (`preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/build/main.tex:11`)
- 044 — *"We prove the equivariant cohomological Hikita conjecture for arbitrary finite quivers, including loops and multiple arrows."*
  (`preprints/The-equivariant-cohomological-Hikita-conjecture-for-arbitrary-quivers-September-24-2026/build/main.tex:48`)
- 151 — *"We disprove the general \(C^1\) self-map formulation of Shub's entropy conjecture."*
  (`preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/build/source/main.tex:39`)
- 209 — *"This gives a negative answer to the unrestricted integral Gersten conjecture."*
  (`preprints/An-Integral-Degree-Three-Gersten-Counterexample-September-26-2026/build/main.tex:33`)
- 297 — *"This gives a negative answer to Naimark's problem without additional set-theoretic assumptions."*
  (`preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/build/main.tex:34`)
- 354 — *"We prove the isoperimetric conjecture for the cubic flat three-torus and classify all minimizers, including the equality cases at the transition volumes $4\pi/81$ and $1/\pi$."*
  (`preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/build/paper.tex:36`)
- 365 — *"We resolve the smooth anisotropic Calder\'on uniqueness problem with arbitrary same-patch measurements."*
  (`preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/build/paper.tex:8`)
- 372 — *"This resolves the smooth three-dimensional isotropic elastic Calder\'on uniqueness problem under these positivity assumptions."*
  (`preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/build/main.tex:46`)
- 263 — headline statement *"Generalized ionization conjecture: radii"*
  (`preprints/Generalized-outer-electron-radii-of-neutral-Coulomb-atoms-September-24-2026/build/sections/01-introduction.tex:38`)
  and manuscript abstract *"We prove the energy part of the generalized ionization conjecture for full
  nonrelativistic Coulomb atoms with two electron spin states."*
  (`preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/build/paper.tex:51`)

**275 is the false positive.** Its only target-named headline statement is
*"Source problem"* (`preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/build/sections/01-finite-models.tex:19`)
— the name of a technical sub-problem inside a reduction, with no manuscript-abstract sentence naming a
target with a resolve verb. Its prose hit is a citation of prior QMA-completeness work. So Direction A
reads **10 real misses and 1 false positive**.

## Direction B — the column reads 1, the manuscript naming is thin

**8** families, all `rn = 1`, that name no target in manuscript prose under either prose rule: 085
(`overview.tex:244`), 094 (`:264`), 126 (`:329`), 144 (`:367`), 187 (`:453`), 299 (`:690`), 323
(`:742`), 333 (`:764`). In every one of the 8 the naming is supplied by the release's overview
abstract:

- 085 (`overview.tex:244`) — *"Resolves the planar centered-disk case of the Haj{\l}asz--Onninen maximal-function regularity problem."*
- 094 (`overview.tex:264`) — *"answering Naor's sublinear-dimension question for $p\ne2$"*
- 126 (`overview.tex:329`) — *"answering Rothvoss's polynomial-size lift question negatively"*
- 144 (`overview.tex:367`) — *"Resolves the probability-preserving form of Banach's simple Lebesgue-spectrum problem"*
- 187 (`overview.tex:453`) — *"Settles the Snaky achievement problem"*
- 299 (`overview.tex:690`) — *"This answers the Kirchberg--R\o rdam character question."*
- 323 (`overview.tex:742`) — *"the separable quotient problem is independent of ZFC"*
- 333 (`overview.tex:764`) — *"resolving the closed-surface form of the four-dimensional isometric-immersion problem"*

Read against the manuscripts, the 8 split **3 corroborated / 5 resting on the overview paraphrase
alone**:

- **Corroborated (3).** 085 — *"This gives a positive resolution of the planar centered-disk case of
  the endpoint question of Haj{\l}asz and Onninen."*
  (`preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/build/main.tex:51`);
  144 — *"We solve the probability-preserving form of Banach's simple Lebesgue-spectrum problem in
  smooth dynamics."*
  (`preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/main.tex:45`);
  333 — *"This resolves the closed-surface form of the classical four-dimensional isometric-immersion problem."*
  (`preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/build/main.tex:38`).
- **Overview-only (5).** 094, 126, 187, 299, 323. Their manuscripts name the target only in background
  prose with no resolve verb: 094 — *"Johnson and Lindenstrauss also asked what analogues of their
  lemma hold in other Banach spaces"*
  (`preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026/build/paper.tex:50`); 187 —
  *"described the ordinary planar problem as undecided at the time"*
  (`preprints/Snaky-in-21-Maker-moves-September-25-2026/build/introduction.tex:75`); 299 — *"Kirchberg
  and R\o rdam asked whether the absence of characters on $F_\omega(A)$ characterizes Jiang--Su
  absorption"* (`preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/build/sections/introduction.tex:26`);
  323 — *"The corresponding assertion for quotients is the \emph{separable quotient problem},
  traditionally attributed to Banach and Mazur."*
  (`preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/build/sections/introduction.tex:5`).
- **126's prose hit is a false pairing.** *"We prove an exponential lower bound for perfect matching by
  studying an exact factorization problem that also allows a fixed positive shift of every odd-cut
  slack."* (`preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/build/source/sections/introduction.tex:7`)
  — "exact factorization problem" is the manuscript's own sub-problem, paired with "prove". Its
  overview flag rests on "answering Rothvoss's … question negatively", which the manuscript does not
  say.

7 of the 8 also sit in the layer-2 `rn-not-abstract` list; 333 does not.

## What the check shows

**The manuscript statement layer is not where the release names conjectures.** Over 1,498 titled
headline statements, 17 titles name a target and **0** of them pair a target noun with a resolve verb.
The naming sits in the manuscript's **name, abstract, and prose**, and in the overview **title** —
which the column does not read.

So `resolves_named` becomes evidence-backed by the record, not by theorem titles:

- **10 real misses** (Direction A) and **14 title-scope additions**, overlapping in 022 039 044 151 209
  263 297; the union of the two is the documented candidate at **247**, removals 0.
- **5 of the 8 Direction-B families** rest on the overview paraphrase alone, which is what the column
  is: a reading of the release's summary, not of the manuscript.
- The column stays a **column**, not a shape: it is a flag on the ledger, and the claim-shape tags are
  keyed to the same overview paraphrase (`notes/abstracts.md`), so a flag is a claim about the summary.

## What has not been checked

- The 63-family layer-2 set is **unadjudicated**. It is the widest candidate (296) and includes
  manuscripts using "problem" for their own sub-problems; no family in it has been read.
- The 112-family `prose-not-rn` set (window scope) has not been read, so the 112 are counts, not
  verdicts.
- The 44 subject-named-not-`rn` families were not read; the name layer is a measured layer, and a
  subject in a theorem title is not a resolved conjecture.
- Headline statements were read as **titles only**. The body of a theorem statement — where a paper
  says "we prove Conjecture X" inside the statement — was not parsed.
- The 101 families with no titled headline theorem have no title-level statement text; nothing here
  says what their `.tex` files state in prose.
- Nothing here is a proof check. `lake`, `lean`, `lake exe cache get`, and `comparator` were never
  invoked, and zero of the 121,734 files under `lean/OAI/**/*.lean` contain `sorry` while the 405
  comparator files carry 509 `sorry` occurrences — a comparator file states a target, it does not
  prove it.
- The 14 title-scope additions have not been applied to the ledger. Changing the column means
  re-measuring every page that quotes 233, including the `resolves_named` AUC row in
  `notes/proof-density.md`; that sweep is tracked as a bd issue, not done here.
