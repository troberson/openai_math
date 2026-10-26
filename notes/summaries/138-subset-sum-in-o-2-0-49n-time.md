[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 138](../index/theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md)

# 138 — Subset Sum in $O(2^{0.49n})$ time

[Index page](../index/theoretical-computer-science/138-subset-sum-in-o-2-0-49n-time.md)

## Original CONTENTS.md summary

[S1:3309] (family entry):

> **138. Subset Sum in $`O(2^{0.49n})`$ time.** Gives a uniform randomized classical algorithm for worst-case Subset Sum in ordinary $`O(2^{0.49n})`$ word-RAM time on polynomial-bit inputs, where n counts the integers. The time bound holds on every execution and success probability is at least 2/3 on every input. Inputs may repeat positive integers; words have $`O(n+b)`$ bits for maximum input bit length b.

[S2:353] carries the `\resultentry`, so the release blurb and the overview
agree on the statement. The `\resultentry` lists two manuscripts:
"Subset Sum in Time $O(2^{0.49n})$" [S2:353] and "A Low-Space Algorithm
for Worst-Case Subset Sum" [S2:353].

## Undergraduate summary

**Subset Sum**: given $n$ positive integers $a_1,\ldots,a_n$ and a
target $t$, is there a subset whose entries sum to $t$? It is one of
the foundational NP-complete problems (it appears as Knapsack in
Karp's list) and a test case for exact exponential-time algorithms
[S4:11–13].

The standard **meet-in-the-middle** algorithm of **Horowitz and
Sahni** (1974) splits the input in half, lists both halves' subset
sums, and searches for complementary sums. That gives the familiar
**$2^{n/2}$** time scale [S4:14–17]. Since then, improvements have
mostly shaved off *polynomial* factors or traded time for space
(**Schroeppel and Shamir** cut the space exponent to $1/4$)
[S4:17–19].

This family achieves something different: it pushes the *exponential
rate* below $1/2$, to **$2^{0.49n}$**, with a uniform randomized
algorithm whose bound holds on *every* execution [S4:58–72]. The
companion paper [S6:70–84] shows the same regime can be reached with
very low space.

## Graduate summary

**Main theorem, time** ([S4:58–72], `thm:main`). "There is a uniform
randomized classical algorithm $\mathcal A$ for Subset Sum with the
following properties in the word-RAM model. For every input with
$n\ge2$, the algorithm halts on every execution and outputs the
correct answer with probability at least $2/3$. For every fixed
positive integer $c$, there are constants $C_c>0$ and $N_c\ge2$ such
that every input with $n\ge N_c$ and $b\le n^c$ is processed, on every
outcome of the random choices, in at most $C_c\,2^{0.49n}$ word
operations. The program is not given $c$ and does not depend on
$c$" [S4:58–72].

**The bound is worst-case, not average-case.** The probability is over
the algorithm's internal random words for each fixed input; no
distributional assumption is made on the input integers. The
running-time bound applies even to executions on which the answer is
incorrect [S4:74–77]. The intermediate bound has the form
$2^{0.489995n}\mathrm{poly}(n+b+2)$; the strict exponent slack
absorbs the polynomial factor separately for every fixed $c$
[S4:78–80].

**Companion theorem, space** ([S6:70–84], `thm:main`). The second
manuscript gives a single uniform classical randomized algorithm that
"never answers YES incorrectly and answers each YES instance correctly
with probability at least $2/3$" [S6:72–74]. For every fixed $c$,
whenever $n\ge N_c$ and $b\le n^c$, every outcome of the randomness
uses at most $A_c n^{k_c}2^{n/2}$ operations and
$A_c(n+b+2)^{15}2^{0.199n}$ writable words [S6:76–82].

**The space corollary.** `cor:target` [S6:86–93] sharpens the space:
for every fixed $\rho>0.199$, the same algorithm has ordinary
$O_{c,\rho}(2^{\rho n})$ word space under each fixed polynomial-bit
convention, and in particular $O_c(2^{n/5})$ word space
[S6:88–92]. The factor $(n+b+2)^{15}$ is absorbed into the $2^{\rho n}$
for any $\rho>0.199$ [S6:95–96].

**The two papers are complementary.** The time paper [S4:58–72] fixes the
space budget (poly words) and minimizes time; the space paper [S6:70–84]
keeps the $2^{n/2}$ time scale and minimizes space to the
$2^{0.199n}$ regime. Together they pin the tradeoff frontier for
worst-case Subset Sum in the word-RAM model.

**Formalization status.** None. No `lean/OAI/` file, no
`lean/docs/138.md`, no comparator challenge, no `main_results` entry —
the ledger row `fam=138` records tier T0 with zero challenges, zero
main results, zero formalized manuscripts, and no reasoning trace
[S9]. Both manuscripts ship their LaTeX under `build/` and a
typeset PDF at their roots [S7][S8]; the release ships nothing for
this family beyond those files. Nothing about this family is
machine-checked: "proves" in the abstract is the release's claim, and
everything above is read from that LaTeX.

## History of the conjecture

**Subset Sum** is one of the foundational NP-complete problems,
appearing as Knapsack in **Karp's** 1972 list [S4:11–13]. Its simple
formulation has made it a basic problem in exact exponential-time
algorithms and cryptanalysis.

The **meet-in-the-middle** algorithm of **Horowitz and Sahni** (1974)
divides the input into two parts, lists their subset sums, and
searches for complementary sums, giving the familiar $2^{n/2}$ time
scale [S4:14–16]. **Schroeppel and Shamir** (1981) preserved that time
scale while reducing the space exponent to $1/4$ [S4:17–18].

More recent work has improved the *polynomial* factor:
**Chen, Jin, Randolph, and Servedio** (2023) obtained a randomized
worst-case running time $O(2^{n/2}n^{-\gamma})$ for a constant
$\gamma>0.5023$ in word-RAM and circuit-RAM models with polynomial
word length [S4:19–22]. A fixed reduction of the *exponential rate*
below $1/2$ is a different objective from such polynomial-factor
savings [S4:23–24].

The theorem here establishes that improvement, with ordinary
$O(2^{0.49n})$ running time, in the precise word-RAM model
[S4:25–26][S4:58–72]. The companion paper [S6:70–84] achieves the matching
space result, $O(2^{n/5})$ writable words, with the same
$2^{n/2}$-time scale [S6:86–93].

**Prior (my training data, not this repo).** Subset Sum's hardness,
the Horowitz–Sahni $2^{n/2}$ meet-in-the-middle bound, and the
Schroeppel–Shamir space reduction are standard results in
exponential-time algorithms. The $O(2^{n/2}n^{-\gamma})$ polynomial
improvements of recent years are also established. The exponent
$0.49$ — a fixed reduction of the exponential rate below $1/2$ — is
the load-bearing claim of the release and is a genuine advance over
the prior state; I cannot confirm the specific exponent as a prior
result, and the release ships the two manuscripts as proof.

## Consequences

- **The exponential rate is below $1/2$.** A uniform randomized
  algorithm decides worst-case Subset Sum in ordinary
  $O(2^{0.49n})$ word-RAM time on polynomial-bit inputs, with the
  bound holding on every execution [S4:58–72][S1:3309].
- **The bound is uniformly valid.** The algorithm does not depend on
  the polynomial-bit parameter $c$; the same program works for every
  fixed $c$ [S4:70–71].
- **The error is one-sided in the space variant.** The companion
  algorithm never answers YES incorrectly and accepts each solvable
  instance with probability at least $2/3$ [S6:72–74][S5:45–47].
- **Very low space is compatible with the $2^{n/2}$ time scale.** The
  same model admits $O_c(2^{n/5})$ writable words
  [S6:86–93][S5:43–44].
- **Both papers are worst-case.** The bounds hold for every input; no
  distributional assumption is made on the integers
  [S4:74–77][S5:42–44].
- **The two results pin the tradeoff frontier.** Time-minimization at
  fixed space [S4:58–72] and space-minimization at fixed time [S6:70–84]
  together characterize the Pareto frontier of worst-case Subset Sum
  in the word-RAM model.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3309], manuscript links [S1:3309] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 138 at [S2:353] |
| S3 | [`preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/main.tex`](../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/main.tex) | 67 | document root; abstract [S3:45–50]; eight section `\input` directives [S3:52–59]; 67 lines |
| S4 | [`preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/introduction.tex`](../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/build/sections/introduction.tex) | 234 | `thm:main` [S4:58–72], word-RAM model [S4:38]; 234 lines |
| S5 | [`preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/main.tex`](../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/main.tex) | 60 | document root; abstract [S5:40–48]; ten section `\input` directives [S5:50–59]; 60 lines |
| S6 | [`preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/introduction.tex`](../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/build/introduction.tex) | 227 | `thm:main` [S6:70–84], `cor:target` [S6:86–93]; 227 lines |
| S7 | [`preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf`](../../preprints/Subset-Sum-in-Time-2-power-0-49n-October-4-2026/subset-sum.pdf) | 14853 | the first manuscript as shipped |
| S8 | [`preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf`](../../preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026/paper.pdf) | 14371 | the second manuscript as shipped |
| S9 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=138`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
