[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 112](../index/theoretical-computer-science/112-beyond-the-square-root-exponent-for-depth-three-circuits.md)

# 112 — Beyond the square-root exponent for depth-three circuits

[Index page](../index/theoretical-computer-science/112-beyond-the-square-root-exponent-for-depth-three-circuits.md)

## Original CONTENTS.md summary

[S1:2752] (family entry):

> **112. Beyond the square-root exponent for depth-three circuits.** Constructs a single language in deterministic polynomial time whose n-bit membership function requires $`2^{\omega(\sqrt n)}`$ total gates in unbounded-fan-in OR–AND–OR circuits, at every sufficiently large input length. This crosses the square-root-exponent threshold for explicit depth-three Boolean circuit lower bounds. ([Lean](../../../lean/docs/112.md))

[S1:2759] (the manuscript entry, with its abstract at [S1:2761]):

> We construct a language in deterministic polynomial time whose n-bit membership function requires $`2^{\omega(\sqrt n)}`$ gates in an unbounded-fan-in OR–AND–OR circuit. The bound holds at every sufficiently large input length and counts all gates, including the bottom layer.

[S2:302] carries the `\resultentry`, so the release blurb and the overview
agree. The family title names the crossing ("Beyond the square-root
exponent"); the manuscript title names the same threshold, and the abstract
adds the gate-counting convention — all gates, including the bottom layer
[S1:2761].

## Undergraduate summary

A **depth-three OR–AND–OR circuit** is a disjunction of CNFs: "such a
circuit is a disjunction of CNFs: conjunctions of clauses, each a
disjunction of literals" [S4:4–5], with arbitrary fan-in and fan-out. The
cost measure $S_3(f)$ is the **total** gate count: "throughout the paper,
$S_3(f)$ denotes the minimum *total* number of AND and OR gates in an
OR–AND–OR circuit computing $f$ exactly" [S4:13–15] — every bottom gate and
the output gate are counted, and input negations are free [S4:15–16].

The classical explicit lower bounds for this model sit at the
square-root-exponent scale: parity needs $2^{\Omega(\sqrt n)}$ gates
[S4:38–40], and the sharp parity bound is $\Omega(n^{1/4}2^{\sqrt n})$
[S4:43–46]. The question the family answers: can **one** fixed
polynomial-time language require more than $2^{A\sqrt n}$ gates for
*every* constant $A>0$? The word "one" is the constraint: "the language
and its membership algorithm must be fixed before $A$ is chosen"
[S4:10–11] — a family of languages, one per $A$, would be a weaker claim.

The answer is yes: "there is a language $L\subseteq\{0,1\}^*$, a
deterministic Turing machine deciding $L$, and fixed positive integers
$C,a$ such that the machine runs in time at most $C(n+1)^a$ on every input
of length $n$", and the ratio $\log_2 S_3(f_n)/\sqrt n$ tends to infinity
[S4:22–28]. Equivalently, for every $A>0$ there is $N_A$ with
$S_3(f_n)>2^{A\sqrt n}$ for every $n\ge N_A$ [S4:29–33].

## Graduate summary

**Main theorem** ([S4:21–35], `thm:main`). Statement as quoted in the
undergraduate section; the theorem also notes "no uniformity or bottom
fan-in restriction is imposed on the circuits" [S4:34]. The model allows
sharing, unrestricted finite fan-in, free negations, and constants
[S10:9].

**The language** ([S7:15–46], `def:language`). For input length $n$, put
$d=\left\lfloorn/5\right\rfloor$; set $r=\left\lceild^{2/3}\right\rceil$ and the largest even $t$ with
$j^6\le d$ [S7:16–20]. The input parses into consecutive blocks: $d$ data
bits, $d+r-1$ hash bits, $r$ polynomial coefficients, and $t$ blocks of
$r$ bits encoding elements $\beta_0,\ldots,\beta_{t-1}$ of the quotient
ring $R_P=\mathbb F_2[Z]/(P)$ [S7:24–33]. The hash is the linear Toeplitz map
$h(x)=\sum_i h_i(x)Z^{i-1}$ built from the hash bits [S7:36–39], and $L$
accepts exactly when $\lambda(\sum_{j=0}^{t-1}\beta_jh(x)^j)=0$, where
$\lambda$ reads the degree-zero coefficient of the representative of
degree less than $r$ [S7:41–45]. The construction is an evaluator whose
*non-data* bits (the hash, the polynomial, the $\beta$ blocks) act as the
hard restriction settings [S7:4–9].

**Polynomial time** ([S7:72–76], `prop:polytime`): "the language $L$ is
decided on every input of length $n$ by one deterministic Turing machine
in time $C(n+1)^a$, for some fixed positive integers $C,a$" [S7:73–75] —
the Horner-loop arithmetic on the tape runs in fixed polynomial time.

**The two structural lemmas.** The restriction lemma ([S5:14–21],
`lem:restriction`): for a CNF $H$ of width at most $k$, retaining each
coordinate with probability $p$ and fixing a uniform assignment outside
$T$, the theta sum
$\theta=\sum_{\ell=b+1}^{k}\binom{k}{\ell}(2p/(1-p))^{\ell}<1$ controls
the restricted function's complexity in a bound independent of the clause
count [S5:14–21]. The sparse-partition lemma ([S6:14–21],
`lem:sparse-partition`): every width-$b$ CNF on $m$ variables is a pointwise
sum of at most $2^{\eta m}$ sub-CNFs [S6:15–21], proved through the
Erdős–Rado sunflower bound $s!(r-1)^s$ [S6:33–36].

**Good slices** ([S7:118–127], `prop:good-slices`): for each fixed width
$b$ and constant $B$, all sufficiently large $n$ admit fixed settings of
the non-data bits such that, at restriction probability
$p=B/\sqrt d$, the language's sign $g$ has small correlation with every
bounded-width CNF on most random restrictions [S7:118–127].

**The lower bound** ([S8:1–16]). The proof of `thm:main` fixes $A$ first,
then chooses $B=64(3A+1)$ and the width, and only then lets $n$ grow,
with $p=B/\sqrt d$, $m_0=B\sqrt d$; the parameter bits stay restrictions
of the language already defined [S8:3–16]. The sparse partition applied
under the restriction bound turns small correlation into the gate-count
inequality $S_3(f_n)>2^{A\sqrt n}$.

## History of the conjecture

The manuscript positions the result on the classical square-root line.
**Håstad**'s random-restriction and switching method gives the
$2^{\Omega(\sqrt n)}$ depth-three lower bound for parity [S4:38–40];
**Håstad, Jukna and Pudlák** improved the constants for parity and
majority by a top-down approach [S4:40–42]; **Paturi, Pudlák and Zane**
obtained the sharp parity bound $\Omega(n^{1/4}2^{\sqrt n})$ through the
satisfiability coding lemma, so parity itself cannot witness the
improvement [S4:43–47]; **Paturi, Pudlák, Saks and Zane**'s
code-membership bound has leading exponent $(\pi/\sqrt6)\sqrt n$ under
stated code-parameter conditions [S4:47–52] — all at the
constant-times-square-root scale.

`thm:main` makes the exponent-to-$\sqrt n$ ratio unbounded; the
introduction names this as the depth-three lower-bound problem discussed
by **Gurumukhani, Paturi, Pudlák, Saks and Talebanfard** and "still
identified as open" in a later survey [S4:54–58]. The result is weaker
than a fixed $2^{n^{1/2+\varepsilon}}$ bound, the question raised by
Håstad–Jukna–Pudlák, and the depth stays three throughout [S4:58–61].
The evaluator-and-hard-subfunction method has an earlier instance in the
input-index construction of **Pudlák, Saks and Zane**, in a model with
bottom fan-in two [S7:10–13].

**Prior (my training data, not this repo).** The switching-lemma route to
depth-three lower bounds is classical (Håstad 1989, AIMJ), the
square-root exponent was the accepted ceiling for *explicit* functions in
this model, and crossing it with one polynomial-time language is the kind
of step the satisfiability-coding-line papers gestured at; the
Erdős–Rado sunflower lemma is the standard sparse-family tool. I cannot
confirm these positions independently; the release ships the manuscript as
a proof, and the Lean layer formalizes the single language statement
(see the comparison below).

## Consequences

- **The threshold crossing.** One fixed polynomial-time language $L$ with
  $\lim_{n\to\infty}\log_2 S_3(f_n)/\sqrt n=\infty$: the exponent-to-$\sqrt n$
  ratio is unbounded [S4:22–28].
- **Per-constant form.** For every $A>0$, $S_3(f_n)>2^{A\sqrt n}$ at every
  length $n\ge N_A$, counting all gates [S4:29–33, S10:9].
- **No extra restrictions.** No uniformity and no bottom fan-in bound are
  imposed on the circuits [S4:34].
- **A method, not a function.** The language is an evaluator (polynomial
  at a linear-hash-selected point), so the hard slices are restriction
  settings of one machine [S7:4–9, S8:5–6].
- **Not the fixed-exponent question.** The result deliberately stops short
  of $2^{n^{1/2+\varepsilon}}$ for fixed $\varepsilon>0$ [S10:9, S4:58–60].

## Section skeleton

The root [S3] includes six sections in the order [S3:23–28]:
`00_introduction`, `01_preliminaries` (Clauses, correlation, and
restrictions), `02_restriction` (A restriction bound independent of clause
count), `03_sparse_partition` (A disjoint sparse partition of bounded-width
CNFs), `04_construction` (One explicit language and its hard slices),
`05_lower_bound` (The depth-three circuit lower bound), then the appendix
`appendices/finite_fields` (Irreducible polynomials over $\mathbb F_2$) and
`references` [S3:29–31]. The LaTeX sits under `build/latex/`, and the
shipped PDF [S9] is `main.pdf` at the manuscript's top level.

## Comparison with the formalized statement

The release formalises this family at tier T3 with one scope note [S10], one
comparator stub [S11:133–140], and one `main_results` entry [S13]. The Scope
paragraph: "the formalized result gives one polynomial-time Boolean
language whose exact depth-three OR–AND–OR circuit size eventually exceeds
$2^{A\sqrt n}$ for every fixed $A>0$" [S10:9], with the language and its
algorithm fixed before $A$ is chosen, unrestricted finite fan-in and
sharing, free input negations and constants, and the caveat "the result
does not assert a fixed exponent $n^{1/2+\varepsilon}$ or a lower bound for
unrestricted depth" [S10:9].

The `main_results` entry [S13:1165–1167] names
`OAI.DepthThreeLowerBound.exists_polynomial_time_language_depth_three_lower_bound`
in `lean/OAI/Computability/DepthThree/Main.lean`. In the source the theorem
is stated and closed: "theorem exists_polynomial_time_language_depth_three_lower_bound : ∃ (L : List Bool → Bool) (M : FiniteMultiTapeMachine) (C a : ℕ), 0 < C ∧ 0 < a ∧ (∀ w : List Bool, MultiTapeHaltsIn M w (L w) (C * (w.length + 1) ^ a)) ∧ ∀ A : ℝ, 0 < A → ∃ N : ℕ, ∀ n : ℕ, N ≤ n → ∀ D : Circuit3 (Fin n), D.Computes (fun x => L (List.ofFn x)) → (2 : ℝ) ^ (A * Real.sqrt (n : ℝ)) < (D.gateCount : ℝ) := by [S12:8–14]" , proved by pairing
`language_polynomial_time` with `language_depth_three_gate_lower_bound`
[S12:15–16]. `grep` finds **zero** `sorry` in the whole
`lean/OAI/Computability/DepthThree/` tree (179 files).

The comparator stub [S11:133–140] carries the same target statement "theorem exists_polynomial_time_language_depth_three_lower_bound : ∃ (L : List Bool → Bool) (M : FiniteMultiTapeMachine) (C a : ℕ), 0 < C ∧ 0 < a ∧ (∀ w : List Bool, MultiTapeHaltsIn M w (L w) (C * (w.length + 1) ^ a)) ∧ ∀ A : ℝ, 0 < A → ∃ N : ℕ, ∀ n : ℕ, N ≤ n → ∀ D : Circuit3 (Fin n), D.Computes (fun x => L (List.ofFn x)) → (2 : ℝ) ^ (A * Real.sqrt (n : ℝ)) < (D.gateCount : ℝ) := by sorry [S11:133–140]"
[S11:133–140] over the config `ComparatorChallenges/DepthThree.json`; the
stub ends in `sorry` at [S11:140], and the proved copy is the one the
`main_results` entry names [S12:8–16]. The scope note's comparator link
[S10:15] names the stub file. A comparator stub is a target the release
set itself. The reading is of source text only — no `lake` or `lean` run
elaborates the proof, so the claim here is that the proof body exists in
the source, not that the file compiles.

## Coverage

The ledger row `fam=112` [S14] records the tier and the counts: `tier=T3`,
`paps=1`, `paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`,
`verification=0`, `trace=`. This is the strong single-manuscript coverage
shape, as families 105 and 106: the manuscript is a formalization source
and the one `main_results` entry names the statement the manuscript's
`thm:main` makes [S4:21–35]. The shape flag is `bound`, and
`resolves_named=0` — the family title names a threshold, not a named
conjecture, so the ledger verb rule has nothing to fire on. There is no
verification bundle and no reasoning trace; the shipped PDF [S9] and the
Lean layer [S10] [S11:133–140] [S12:8–14] [S13] are the two evidence surfaces.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:2752], the manuscript link [S1:2759], and the manuscript abstract [S1:2761]. The release's inline code spans stay as backticked markdown, and the release's italic markup is folded to the plain word |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 112 at [S2:302] |
| S3 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/main.tex`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/main.tex) | 32 | root (`\documentclass`); abstract [S3:15–21]; the include order [S3:23–31] |
| S4 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/00_introduction.tex`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/00_introduction.tex) | 144 | the gate-count definition [S4:13–19]; the main theorem [S4:21–35]; the square-root-exponent paragraph [S4:37–52]; the open-problem positioning [S4:54–61] |
| S5 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/02_restriction.tex`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/02_restriction.tex) | 342 | the restriction lemma [S5:14–21] |
| S6 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/03_sparse_partition.tex`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/03_sparse_partition.tex) | 264 | the sparse-partition lemma [S6:14–21]; the sunflower bound [S6:33–36] |
| S7 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/04_construction.tex`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/04_construction.tex) | 305 | the language definition [S7:15–30]; the polynomial-time proposition [S7:72–76]; the good-slices proposition [S7:118–127] |
| S8 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/05_lower_bound.tex`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/build/latex/sections/05_lower_bound.tex) | 141 | the lower-bound section opening and parameter order [S8:1–16] |
| S9 | [`preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/main.pdf`](../../../preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/main.pdf) | 7076 | the manuscript as shipped |
| S10 | [`lean/docs/112.md`](../../../lean/docs/112.md) | 15 | scope note — the Scope paragraph at [S10:9] and the comparator link at [S10:15] |
| S11 | [`lean/ComparatorChallenges/DepthThree.lean`](../../../lean/ComparatorChallenges/DepthThree.lean) | 144 | the comparator stub — the target theorem at [S11:133–140] with its `sorry` |
| S12 | [`lean/OAI/Computability/DepthThree/Main.lean`](../../../lean/OAI/Computability/DepthThree/Main.lean) | 20 | the formalized file — the proved theorem at [S12:8–16] |
| S13 | [`lean/formalization.yaml`](../../../lean/formalization.yaml) | 1833 | the `main_results` entry naming the declaration, at [S13:1165–1167] |
| S14 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=112`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
