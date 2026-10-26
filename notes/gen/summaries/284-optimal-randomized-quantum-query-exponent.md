[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 284](../index/mathematical-physics/284-optimal-randomized-quantum-query-exponent.md)

# 284 — The optimal randomized–quantum query exponent

[Index page](../index/mathematical-physics/284-optimal-randomized-quantum-query-exponent.md)

## Original CONTENTS.md summary

The release's blurb [S1:7084] and the catalog abstract [S2:658] state
the family's claim: the universal quartic bound relating bounded-error
randomized and quantum query complexity for total Boolean functions is
sharp in its exponent, and the bound is optimal — the conjectured cubic
relation is false. The manuscript's abstract "We construct total Boolean functions with a nearly quartic separation
between bounded-error randomized and quantum query complexity.
Writing these complexities as $\mathrm R(f)$ and $\mathrm Q(f)$, the examples rule
out every universal bound $\mathrm R(f)=O((1+\mathrm Q(f))^\alpha)$ with
$\alpha<4$. Thus the known quartic upper bound has the optimal
exponent, disproving the conjectured cubic bound. Both complexities
count worst-case bit queries with error at most $1/3$ on every input. [S3:9–17]"

## Undergraduate summary

Query complexity measures how many input bits an algorithm must read to
evaluate a function. A total Boolean function is defined on every input,
as opposed to a partial one that is only promised to be defined on a
subset. Bounded-error randomized query complexity $\mathrm R(f)$ counts the
worst-case number of bit queries of a classical algorithm that succeeds
with probability at least $2/3$; bounded-error quantum query complexity
$\mathrm Q(f)$ is the analogous count for a quantum algorithm, whose queries
are oracle calls that put the input bit into a quantum superposition.
For total functions the two measures are always polynomially related,
because totality rules out the exponential gaps that partial functions
admit. The question is the sharp power of that polynomial relation.
Define the optimal power $\alpha_{\mathrm{tot}}$ as the smallest
exponent for which a uniform constant makes $\mathrm R(f)\le
C(1+\mathrm Q(f))^\alpha$ hold for every total $f$ [S4:3–27]. The
manuscript proves it is exactly four:

> **theorem**
The optimal power is $\alpha_{\mathrm{tot}}=4$.
More precisely, $\mathrm R(f)=O((1+\mathrm Q(f))^4)$ for every total Boolean function.
For each fixed integer $k\ge2$, there are positive constants $c_k,C_k,b_k$
and total Boolean functions $F_{k,m}$, for all sufficiently large powers
of four $m$, such that
$$\label{eq:main-family}
 \mathrm Q(F_{k,m})\le C_k\sqrt m\,(\log m)^{b_k},
 \qquad
 \mathrm R(F_{k,m})\ge c_k\frac{m^{2-1/k}}{(\log m)^2}.$$ [S4:29–40]

The upper bound half — the universal quartic relation — was already
known; the new contribution is the family $F_{k,m}$, which rules out
every smaller power including the cubic relation that had been
conjectured.

## Graduate summary

**The construction and its two analyses.** The input is organized into
$m$ columns. Each column $i$ carries a string $X_i$ of $m$ bits and an
array of certificate cells; the address of the relevant cell is the
vector of answers to several disjoint instances of a partial function.
Those answers are cheap for a quantum algorithm on promised inputs but
hard for a classical algorithm to guess. A column wins when its own
string is all ones, its address is defined, and its certificate is
correct and points to a zero in every other column; the total function
asks whether a winner exists, and there can be at most one [S4:94–146].

The quantum analysis proves a tournament lemma: using the actual
probabilities of candidate comparisons as multiplicative weights, fresh
coherent workspaces and amplitude amplification sample those weights
exactly, so a short list containing the winner is produced in $\sqrt m$
times a polylogarithmic number of queries, after which quantum search
checks the certificates. The classical analysis starts with one hidden
zero in every column and blank certificate cells, erases the zero of a
uniformly random column, and fills its correctly addressed cell to
create a winner; a randomized algorithm distinguishes the two inputs
only by finding the erased zero or guessing a full hard address vector,
which an adaptive per-instance-capped direct-product argument lower
bounds. The only external lower-bound input is the Forrelation theorem
stated in the construction section [S4:94–146].

**Formalization status.** Nothing about this family is machine-checked.
There is no Lean library, no scope note, no comparator challenge, and
no reasoning trace; the LaTeX under `build/` is the only source.

## History of the conjecture

For total functions the basic quantum speedup is Grover's quadratic
factor, and the polynomial relation between deterministic and quantum
queries was shown by Beals, Buhrman, Cleve, Mosca, and de Wolf.
Pointer constructions introduced by Göös, Pitassi, and Watson and
developed by Ambainis, Balodis, Belovs, Lee, Santha, and Smotrovs gave
a nearly quartic deterministic–quantum separation. For bounded-error
randomized queries, Aaronson, Ben-David, and Kothari introduced the
cheat-sheet framework and obtained a power-$5/2$ separation up to
logarithms, later improved to power $3-o(1)$ by Bansal and Sinha and
independently by Sherstov, Storozhenko, and Wu [S4:48–90]. On the
upper-bound side, Aaronson, Ben-David, Kothari, Rao, and Tal, using
Huang's sensitivity theorem, proved the quartic relation and conjectured
the stronger cubic one; this manuscript's theorem disproves that
conjecture.

## Consequences

**The quartic exponent is optimal.** For every total Boolean function
$\mathrm R(f)=O((1+\mathrm Q(f))^4)$, and the family $F_{k,m}$ rules out every
smaller universal power, so $\alpha_{\mathrm{tot}}=4$
[S4:29–40].

**The conjectured cubic bound is false.** The randomized complexity of
the family satisfies
$\mathrm R(F_{k,m})\ge c_k m^{2-1/k}/(\log m)^2$ while the quantum complexity
satisfies $\mathrm Q(F_{k,m})\le C_k\sqrt m\,(\log m)^{b_k}$, which for any
$k\ge2$ grows faster than $(1+\mathrm Q(F_{k,m}))^3$ up to logarithmic
factors, contradicting the cubic relation
[S4:29–40].

## Section skeleton

**Manuscript** [S3:9–17], 6 sections under `build/sections/`:
01-introduction [S4:29–40], 02-construction, 03-quantum, 04-classical,
05-exponent, 06-upper-bound. Plus one figure under `build/figures/`.
Its root is `build/main.tex`, with a `references.bib` bibliography [S5].

The manuscript ships no `verification/` bundle.

## Coverage

T0: no Lean, no scope note, no comparator challenge, no reasoning
trace. Nothing about this family's theorems is machine-checked. The
ledger reads `paps_form 0`, `mainres 0`, `scope_note 0`, `chal 0`,
`verification 0`, `trace` empty. The family ships one LaTeX manuscript —
8 `.tex` files plus a preamble under `build/` — and no non-LaTeX
evidence.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9142 | The release's blurb for family 284 at line 7084. |
| S2 | [`overview.tex`](../../../overview.tex) | 859 | The catalog abstract at line 658. |
| S3 | [`preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/main.tex`](../../../preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/main.tex) | 27 | Manuscript main file: title and abstract. |
| S4 | [`preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/sections/01-introduction.tex) | 157 | Introduction: the setup, the main theorem, the historical context, the construction, and the conventions. |
| S5 | [`preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/references.bib`](../../../preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026/build/references.bib) | 329 | Manuscript bibliography. |

## Bibliography

- Scott Aaronson, Shalev Ben-David, Robin Kothari, Separations in Query Complexity Using Cheat Sheets (2016)
- Scott Aaronson, Andris Ambainis, Forrelation: A Problem That Optimally Separates Quantum from Classical Computing (2018)
- Scott Aaronson, Shalev Ben-David, Robin Kothari, Shravas Rao, Avishay Tal, Degree vs. Approximate Degree and Quantum Implications of Huang's Sensitivity Theorem (2021)
- Andris Ambainis, Kaspars Balodis, Aleksandrs Belovs, Troy Lee, Miklos Santha, Juris Smotrovs, Separations in Query Complexity Based on Pointer Functions (2017)
- Andris Ambainis, Quantum Lower Bounds by Quantum Arguments (2002)
- Andris Ambainis, J{\=a}nis Iraids, Martins Kokainis, Near-Optimal Separations of Certificate Complexity from Randomized and Quantum Query Complexity (2026)
- Nikhil Bansal, Makrand Sinha, {$k$-Forrelation} Optimally Separates Quantum and Classical Query Complexity (2021)
- Howard Barnum, Michael E. Saks, Mario Szegedy, Quantum Query Complexity and Semi-Definite Programming (2003)
- Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca, Ronald de Wolf, Quantum Lower Bounds by Polynomials (2001)
- Shalev Ben-David, Robin Kothari, Randomized Query Complexity Can Beat Certificate Complexity (2026)
- Charles H. Bennett, Ethan Bernstein, Gilles Brassard, Umesh Vazirani, Strengths and Weaknesses of Quantum Computing (1997)
- Michel Boyer, Gilles Brassard, Peter Høyer, Alain Tapp, Tight Bounds on Quantum Searching (1998)
- Gilles Brassard, Peter Høyer, Michele Mosca, Alain Tapp, Quantum Amplitude Amplification and Estimation (2002)
- Andrew Drucker, Improved Direct Product Theorems for Randomized Query Complexity (2012)
- Lov K. Grover, A Fast Quantum Mechanical Algorithm for Database Search (1996)
- Hao Huang, Induced Subgraphs of Hypercubes and a Proof of the Sensitivity Conjecture (2019)
- Nikhil S. Mande, Manaswi Paraashar, Nitin Saurabh, Randomized and Quantum Query Complexities of Finding a King in a Tournament (2023)
- Gatis Midrijanis, Exact Quantum Query Complexity for Total Boolean Functions (2004)
- Noam Nisan, CREW PRAMs and Decision Trees (1991)
- Noam Nisan, Mario Szegedy, On the Degree of Boolean Functions as Real Polynomials (1994)
- Christoph Dürr, Peter Høyer, A Quantum Algorithm for Finding the Minimum (1996)
- Mika Göös, Toniann Pitassi, Thomas Watson, Deterministic Communication vs. Partition Number (2015)
- Ronen Shaltiel, Towards Proving Strong Direct Product Theorems (2003)
- Alexander A. Sherstov, Andrey A. Storozhenko, Pei Wu, An Optimal Separation of Randomized and Quantum Query Complexity (2023)
- Xiaoming Sun, Andrew C. Yao, Shengyu Zhang, Graph Properties and Circular Functions: How Low Can Quantum Query Complexity Go? (2004)
- Avishay Tal, Towards Optimal Separations between Quantum and Randomized Query Complexities (2020)
- Andrew Chi-Chih Yao, Probabilistic Computations: Toward a Unified Measure of Complexity (1977)
- Robert Špalek, Mario Szegedy, All Quantum Adversary Methods Are Equivalent (2006)
