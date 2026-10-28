[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 097](../index/convex-and-metric-geometry/097-euclidean-steinitz-bergstrom-conjecture.md)

# 097 — The Euclidean Steinitz–Bergström conjecture

[Index page](../index/convex-and-metric-geometry/097-euclidean-steinitz-bergstrom-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:2386] and the catalog abstract [S2:270] state
the family's claim: any finite sequence in the Euclidean unit ball of
$\mathbb R^d$ admits signs keeping every partial sum within
$C\sqrt d$, independently of length, and every zero-sum family can be
reordered with the same bound on unsigned partial sums. The
manuscript's abstract 

> Every prescribed-order finite sequence of vectors in the Euclidean unit
ball of $\mathbb R^d$ has one signing for which every signed prefix has norm at
most $C\sqrt d$, with $C$ absolute and independent of the sequence length.
Consequently, every indexed zero-sum family of unit-ball vectors admits an
ordering with the same bound for its unsigned partial sums. This determines
the Euclidean Steinitz constant up to absolute factors,
$S_2(d)=\Theta(\sqrt d)$, and resolves the Euclidean
Steinitz–Bergström conjecture. [S3:40–47]

## Undergraduate summary

Take a finite list of vectors, each of length at most 1. Can you put a
$+$ or $-$ in front of each so that the running total never wanders
far from the origin? The Steinitz–Bergstr\H{o}m question asks
for a universal bound on how far the partial sums can drift, in terms
of the dimension $d$ alone [S4:10–20]. The answer here is
$C\sqrt d$ for some absolute constant $C$ [S4:15–16]. A second,
companion form: if the vectors sum to zero, some ordering keeps every
unsigned partial sum within the same bound [S4:35–45]. A
matching lower bound shows $\sqrt d$ is the right order
[S2:270].

## Graduate summary

**The prescribed-order signed-prefix bound** [S4:10–20,
`thm:signing`]. There is an absolute constant $C$ such that, for all
$d,N\ge1$ and every sequence $v_1,\ldots,v_N$ of unit-ball vectors
in $\mathbb R^d$, there are signs
$\varepsilon_i\in\{-1,1\}$ with

> **Theorem 1.2**
There is an absolute constant $C$ such that, for all integers $d,N\ge1$ and
every indexed family $v_1,\ldots,v_N\in\mathbb R^d$ satisfying
$\lVert v_i\rVert_2\le1$ and $\sum_{i=1}^N v_i=0$, some permutation
$\pi\in\mathfrak S_N$ satisfies
$$\max_{0\le k\le N}\left\lVert\sum_{i=1}^k v_{\pi(i)}\right\rVert_2
 \le C\sqrt d.$$
The constant in Theorem also suffices here. [S4:35–45]

The same signs control all prefixes, and $C$ is independent of $d$,
$N$ and the sequence [S4:18–19].

**The zero-sum reordering** [S4:35–45, `thm:steinitz`]. Under
the added condition $\sum_i v_i=0$, some permutation
$\pi$ satisfies
$\max_k\lVert\sum_{i\le k}v_{\pi(i)}\rVert_2\le C\sqrt d$, with
the constant from the signed bound also sufficing
[S4:44–45].

## History of the conjecture

Steinitz's classical sign-assignment result and its higher-dimensional
extensions give a long-standing question about the optimal
dimension-dependent constant for unit-ball vectors; Bergstr\H{o}m's
formulation isolates the zero-sum reordering case
[S2:270]. The manuscript resolves both the signed-prescribed-order and
the reordering forms with a single constant and proves the
$\Theta(\sqrt d)$ order sharp.

**Prior (my training data, not this repo).** I know Steinitz's
polygon (sign-assignment) lemma in the plane and the classical
higher-dimensional sign-assignment problem, and that the optimal
constant's dependence on dimension was a question of interest. A proof
that the Euclidean Steinitz constant is $\Theta(\sqrt d)$
simultaneously for the prescribed-order signed form and the zero-sum
reordering form, with a matching lower bound, is, to my knowledge,
not established in the literature I was trained on. I cannot
independently verify this manuscript's argument.

## Consequences

**Optimal Steinitz constant.** The Euclidean Steinitz constant
$S_2(d)$ is $\Theta(\sqrt d)$: upper-bounded by $C\sqrt d$
(both signed and reordered forms) and matched from below by
$\sqrt d$ [S3:44–47, S2:270].

**Signed and reordered agree.** The same absolute constant bounds the
prescribed-order signed prefixes and the zero-sum reordered unsigned
prefixes [S4:44–45].

## Section skeleton

One manuscript [S3:40–47] (title [S3:34], date [S3:36]) — a 60-line
`main.tex` under `build/` plus seven section files (introduction,
signing, survival, brownian, matrix, assembly, consequences); a
21-entry `references.bib` [S8]. Total 2,102 lines. No manuscript ships
a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S5:9]. The formalized result gives the Euclidean
Steinitz–Bergstr\H{o}m bound with one absolute constant $C$:
for every finite family of unit-ball vectors, signs make every
prescribed-order prefix have norm at most $C\sqrt d$, and when the sum
is zero a permutation makes every unsigned prefix satisfy the same
bound. Repeated and zero vectors are included; the result is
existential and does not supply an online algorithm [S5:9]. The scope
note names one comparator [S5:13–15]. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library
has not been built here.

**The comparator stub** [S6:24–25] states both forms together,
with one `sorry`:

```lean
theorem main : ∃ C : ℝ, SignedPrefixBound C ∧ OrderingPrefixBound C := by
  sorry
```
[S6:24–25]

**The registered entry point.** The `main_results` entry names
`OAI.EuclideanSteinitzBergstrom.main` in
`OAI/Analysis/Steinitz/Main.lean`, proved at line 111


```lean
theorem main : ∃ C : ℝ, SignedPrefixBound C ∧ OrderingPrefixBound C :=
  ⟨universalConstant,signed_prefix_bound,signing_implies_ordering universalConstant signed_prefix_bound⟩
```
[S7:111–112]

The proof is a direct term: `universalConstant` discharges the signed
bound via `signed_prefix_bound`, and the reordering form follows by
`signing_implies_ordering`. The `main_results` entry links the config
`ComparatorChallenges/SteinitzBergstrom.json` to the declaration, so
this is the family's headline bound, registered and proven. The OAI
`Steinitz` tree is 29 files over 15,082 lines with zero `sorry`.

## Coverage

T3: the family is formalized. The ledger row `fam=097` records
`paps 1`, `paps_form 1`, `tier T3`, `chal 1`, `mainres 1`,
`scope_note 1`, `verification 0`, `trace` empty,
`shapes bound|partial`, `resolves_named 1`, `summary 1`. The family
ships one 2,102-line LaTeX manuscript, a scope note, one comparator
challenge carrying one `sorry` theorem, and the registered
`main_results` declaration `OAI.EuclideanSteinitzBergstrom.main`,
the signed+reordered prefix bound, proven in the 29-file `Steinitz` OAI
tree. The matching $\sqrt d$ lower bound giving the sharp order is a
manuscript claim alongside the bound. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 097 at [S1:2386] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{097} at [S2:270] |
| S3 | [`preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/main.tex`](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/main.tex) | 60 | the single manuscript root; title [S3:34], date [S3:36], abstract [S3:40–47] |
| S4 | [`preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/introduction.tex`](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/introduction.tex) | 206 | introduction; the prescribed-order signed-prefix theorem [S4:10–20] and the Steinitz–Bergstr\H{o}m bound [S4:35–45] |
| S5 | [`lean/docs/097.md`](../../../lean/docs/097.md) | 15 | the formalization scope note: the scope paragraph [S5:9] and the comparator table [S5:13–15] |
| S6 | [`lean/ComparatorChallenges/SteinitzBergstrom.lean`](../../../lean/ComparatorChallenges/SteinitzBergstrom.lean) | 29 | comparator stub: the `SignedPrefixBound` def [S6:9–15], the `OrderingPrefixBound` def [S6:17–22], the `main` theorem [S6:24], and the `sorry` [S6:25] |
| S7 | [`lean/OAI/Analysis/Steinitz/Main.lean`](../../../lean/OAI/Analysis/Steinitz/Main.lean) | 118 | the OAI proven `main` theorem [S7:111–112] |
| S8 | [`preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/references.bib`](../../../preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/build/references.bib) | 200 | 21-entry BibTeX bibliography |

## Bibliography

- Akbas, Emrullah, Sra, Suvrit, Tighter bounds on Komlós discrepancy: existence and algorithmic results (2026)
- Ambrus, Gergely, Heck, Rainie, A note on the Steinitz Lemma (2026)
- Banaszczyk, Wojciech, Balancing vectors and Gaussian measures of $n$-dimensional convex bodies (1998)
- Banaszczyk, Wojciech, On series of signed vectors and their rearrangements (2012)
- Bandeira, Afonso S., A simplification of the solution to the Komlós Conjecture (2026)
- Bansal, Nikhil, Jiang, Haotian, Meka, Raghu, Singla, Sahil, Sinha, Makrand, Prefix Discrepancy, Smoothed Analysis, and Combinatorial Vector Balancing (2021)
- Behrend, F. A., The Steinitz–Gross theorem on sums of vectors (1954)
- Borell, Christer, The Brunn–Minkowski inequality in Gauss space (1975)
- Brascamp, Herm Jan, Lieb, Elliott H., On extensions of the Brunn–Minkowski and Prékopa–Leindler theorems, including inequalities for log concave functions, and with an application to the diffusion equation (1976)
- Bryan, Paul, Clutterbuck, Julie, Rankin, Cale, Convexity inequalities for eigenvalues and log-concavity of eigenfunctions (2026)
- Chobanyan, Sergei, Chobanyan, Levon, Gorgadze, Zaza, Ghlonti, Giorgi, An Algorithm for Finding a Near-Optimal Rearrangement in the Steinitz Functional (2023)
- Chobanyan, Sergej, Convergence A.S. of Rearranged Random Series in Banach Space and Associated Inequalities (1994)
- Davies, E. B., Simon, Barry, Ultracontractivity and the heat kernel for Schrödinger operators and Dirichlet Laplacians (1984)
- Dutta, Kunal, Jha, Agastya Vibhuti, Jiang, Haotian, Near-Optimal Constructive Bounds for $\ell_2$ Prefix Discrepancy and Steinitz Problems via Affine Spectral Independence (2026)
- Grinberg, V. S., Sevast'yanov, S. V., Value of the Steinitz constant (1980)
- Guo, Shengtao, Fang, Ethan X., Lu, Junwei, Vector Balancing via Directional Total Variation (2026)
- Prékopa, András, On logarithmic concave measures and functions (1973)
- Li, Xiaoyu, Fast Spectral Signing for Vector Balancing (2026)
- Bergström, Viktor, Zwei Sätze über ebene Vektorpolygone (1931)
- Bárány, Imre, A matrix version of the Steinitz lemma (2024)
- Royen, Thomas, A simple proof of the Gaussian correlation conjecture extended to some multivariate gamma distributions (2014)
