[Notes](../../README.md) / [Summaries](README.md) / [Number theory](../index/disciplines/number-theory.md) / [Family 028](../index/number-theory/028-gaussian-moat-conjecture.md)

# 028 — The Gaussian moat conjecture

[Index page](../index/number-theory/028-gaussian-moat-conjecture.md)

## Original CONTENTS.md summary

The release blurb 

> **028. Uniformly bounded components of Gaussian-prime graphs.** Proves the Gaussian moat conjecture: no infinite walk through distinct Gaussian primes can have uniformly bounded steps. More strongly, for every distance bound *D*, the graph joining Gaussian primes at distance at most *D* has uniformly bounded finite component sizes, depending only on *D*, including primes on the coordinate axes. [S1:682]

The manuscript abstract 

> We prove the Gaussian moat conjecture: no infinite walk through distinct
Gaussian primes can have bounded steps. More strongly, for each fixed finite
step bound, the connected components of the Gaussian-prime graph have
uniformly bounded size. This bound applies to every starting prime, including
primes on the coordinate axes, and is nonexplicit. The proof constructs a
finite periodic sieve obstruction using geometric sampling and
information-theoretic estimates. [S2:43–51]

## Undergraduate summary

A "Gaussian prime" is a prime in the grid of complex numbers
$`a + bi`$ — a point on the integer lattice that cannot be factored into
two closer lattice points. The "Gaussian moat" question asks whether you
can walk from Gaussian prime to Gaussian prime (always to a *new* prime,
never repeating) while keeping every step short — say, never longer than
some fixed distance $`D`$.

The paper says no. For any fixed step size $`D`$, the graph that joins two
Gaussian primes when they are at most $`D`$ apart has only *finite*
connected components, and the size of a component is bounded by a number
$`B_D`$ that depends only on $`D`$ and not on where you start. So any walk
with steps of length at most $`D`$ can take at most $`B_D`$ steps before it
runs out of distinct primes to land on. There is always a "moat" — a gap
bigger than $`D`$ — eventually, no matter which prime you start from,
including primes sitting on the coordinate axes.

The main statement 

> **theorem**
For every finite real $`D`$ there is a finite $`B_D`$ such that every
connected component of $`G_D`$ has at most $`B_D`$ vertices.
The bound is independent of the starting prime and includes primes on
the coordinate axes. Consequently every sequence of distinct Gaussian
primes whose successive distances are at most $`D`$ has at most $`B_D`$ terms. [S2:63–69]

## Graduate summary

The theorem is a uniform component-size bound on the bounded-step
Gaussian-prime graph, whose consequence is the moat result.

**Main theorem.** 

> **theorem**
For every finite real $`D`$ there is a finite $`B_D`$ such that every
connected component of $`G_D`$ has at most $`B_D`$ vertices.
The bound is independent of the starting prime and includes primes on
the coordinate axes. Consequently every sequence of distinct Gaussian
primes whose successive distances are at most $`D`$ has at most $`B_D`$ terms. [S2:63–69]

For every finite real $`D`$ there is a finite $`B_D`$ such that every
connected component of $`G_D`$ (the graph joining Gaussian primes within
distance $`D`$) has at most $`B_D`$ vertices. The bound is independent of the
starting prime and includes axis primes. The moat statement follows
immediately: an injective bounded-step walk is a path in $`G_D`$, so it has
at most $`B_D`$ terms and is therefore finite.

**The nonexplicit bound.** The bound $`B_D`$ exists but is *not* given as
an explicit function of $`D`$ [S4:9] — the proof is a compactness/finite
obstruction argument, so it produces the constant only by existence. The
scope note is explicit here: "No explicit function of $`D`$ is supplied."

**The machine.** The proof builds a finite periodic sieve obstruction —
a geometric-sampling argument (the one-step coverage transfer in
[S3:102–129]) combined with information-theoretic estimates — to show no
infinite injective bounded-step walk can exist.

## history of the conjecture

Prior (my training data, not this repo): the "moat" language comes from
the prime moat heuristics (Cramér's random model and the Bateman–Horn
conjecture), which predict that arbitrarily large gaps occur in the
primes. The Gaussian-prime version asks the same question in
$`\mathbb Z[i]`$: do bounded-step walks through distinct Gaussian primes go on
forever? The answer here is negative, and uniformly — the component-size
bound that implies the moat is the stronger content. The axis primes
(those on the real or imaginary axis) are the delicate case for the
geometric sampling, which is why the theorem calls them out explicitly.
The bound is nonexplicit, in the compactness style of the prime
divergence arguments.

## Consequences

**The Gaussian moat conjecture is proved.** No infinite walk through
distinct Gaussian primes has uniformly bounded steps [S2:63–69].

**A uniform component-size bound depending only on $`D`$.** Every
connected component of the bounded-step graph has at most $`B_D`$ vertices,
independent of the starting prime and including axis primes [S2:63–69].

**No explicit function of $`D`$.** The bound is an existence result; no
closed form for $`B_D`$ is supplied [S4:9].

## section skeleton

Single main file [S2] with seven flat section inputs [S2:180–186]
(periodicity, preliminaries, geometry, coverage-transfer, schedule,
information, references), the bibliography being an inline
`thebibliography` in references.tex [S7] (14 items, no `.bib` file).

**Sections** [S2:180–186]: The main theorem is in main.tex itself (line
63), with the finite sieve obstruction theorem (line 120); periodicity
(periodicity.tex); preliminaries (preliminaries.tex); geometry
(geometry.tex); coverage-transfer (coverage-transfer.tex) with the
one-step coverage transfer theorem (line 102); schedule (schedule.tex);
information (information.tex); references (references.tex).

## Comparison with the formalized statement

The scope note states the formalization's reach: "The Gaussian moat problem asks whether an infinite walk through distinct Gaussian primes can have bounded step lengths. The formalized result gives a negative answer for every real step bound $`D`$. More strongly, one finite bound depending only on $`D`$ limits the size of every connected component of the bounded-step graph and the length of every injective bounded-step walk. Axis primes and all associates are included. No explicit function of $`D`$ is supplied. [S4:9]" — the
negative answer for every real step bound $`D`$, with the uniform
component-size bound, axis primes and all associates included.

The comparator stub [S5:36–37] states the combined moat-plus-uniform
target and ends in `sorry`:

```lean
theorem fullMain : MainEndpoint ∧ UniformEndpoint := by
  sorry
```
[S5:36–37]

The proof lands in `OAI/NumberTheory/GaussianMoat/Main.lean` [S6], which
carries **zero** `sorry` occurrences; the `main_results` entry
`OAI.GaussianMoat.fullMain` is in that file at line 102 (ledger
`paps_form 1`, `mainres 1`, `chal 1`), and it discharges both the
moat endpoint and the uniform endpoint, so the formalization is landed,
in contrast to a stub-only family.

**Tree measurement (source-level).**

The `main_results` entry OAI.GaussianMoat.fullMain resolves to `OAI/NumberTheory/GaussianMoat/Main.lean` (107 lines); the top-level theorem is `theorem exists_sieveCertificate (D`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 41 files with 339 theorems and 157 defs.

The preprint states 15 theorem environments; the tree carries 23× as many (source-level count, not a proof-quality ratio).

## Coverage

T3: one manuscript, one comparator challenge, one `main_results` entry,
one scope note. The ledger reads `paps 1`, `paps_form 1`, `mainres 1`,
`chal 1`, `scope_note 1`, `verification 0`, `trace` empty,
`shapes resolution|bound|partial|uniform`, `resolves_named 1`. The
family ships a nine-file LaTeX manuscript (main file plus seven flat
sections including the inline-bibliography references.tex [S7]) and a
compiled `paper.pdf` [S8]. The catalog entry [S9:132] names the single
PDF. No `.bib` file, no `verification/` bundle, no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | Release blurb (family 028 at line 682) |
| S2 | [`preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex`](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex) | 187 | Main file: abstract, main theorem, section inputs |
| S3 | [`preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex) | 273 | One-step coverage transfer theorem |
| S4 | [`lean/docs/028.md`](../../../lean/docs/028.md) | 15 | Scope note |
| S5 | [`lean/ComparatorChallenges/GaussianMoat.lean`](../../../lean/ComparatorChallenges/GaussianMoat.lean) | 41 | Challenge stub (fullMain = moat + uniform bound, sorry) |
| S6 | [`lean/OAI/NumberTheory/GaussianMoat/Main.lean`](../../../lean/OAI/NumberTheory/GaussianMoat/Main.lean) | 107 | Proved version in the Lean tree (fullMain, 0 sorry) |
| S7 | [`preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/references.tex`](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/references.tex) | 89 | Bibliography (inline thebibliography, no .bib) |
| S8 | [`preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf`](../../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf) | 14061 | Compiled manuscript |
| S9 | [`overview.tex`](../../../overview.tex) | 861 | Catalog entry (family 028 at line 132) |

## Bibliography

- S. Boucheron, G. Lugosi, and P. Massart, _Concentration Inequalities: A Nonasymptotic Theory of Independence_, Oxford University Press, Oxford, 2013. .
- K. Conrad, _The Gaussian Integers_, expository notes. (accessed 27 September 2026).
- P. Erdős, Problems and results on combinatorial number theory III, in _Number Theory Day_ (Rockefeller University, New York, 1976), Lecture Notes in Mathematics, vol. 626, Springer, Berlin, 1977, pp. 43–72. .
- E. Gethner, S. Wagon, and B. Wick, A stroll through the Gaussian primes, _American Mathematical Monthly_ **105** (1998), no. 4, 327–337. .
- L. H. Harper, Optimal assignments of numbers to vertices, _Journal of the Society for Industrial and Applied Mathematics_ **12** (1964), no. 1, 131–135. .
- A. Hatcher, _Algebraic Topology_, Cambridge University Press, Cambridge, 2002. .
- W. Hoeffding, Probability inequalities for sums of bounded random variables, _Journal of the American Statistical Association_ **58** (1963), no. 301, 13–30. .
- G. Lugosi, _Concentration-of-measure inequalities_, lecture notes, June 25, 2009. Author-hosted lecture notes.
- A. Selberg, An elementary proof of the prime-number theorem for arithmetic progressions, _Canadian Journal of Mathematics_ **2** (1950), 66–78. .
- E. Gethner and H. M. Stark, Periodic Gaussian moats, _Experimental Mathematics_ **6** (1997), no. 4, 289–292. .
- T. Tao, The logarithmically averaged Chowla and Elliott conjectures for two-point correlations, _Forum of Mathematics, Pi_ **4** (2016), e8, 36 pp. .
- T. M. Cover and J. A. Thomas, _Elements of Information Theory_, second edition, Wiley-Interscience, Hoboken, NJ, 2006. .
- N. Tsuchimura, Computational results for Gaussian moat problem, _IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences_ **E88-A** (2005), no. 5, 1267–1273. .
- I. Vardi, Prime percolation, _Experimental Mathematics_ **7** (1998), no. 3, 275–289. .
