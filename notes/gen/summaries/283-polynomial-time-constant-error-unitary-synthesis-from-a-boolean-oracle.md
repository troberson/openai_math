[Notes](../../README.md) / [Summaries](README.md) / [Mathematical physics](../index/disciplines/mathematical-physics.md) / [Family 283](../index/mathematical-physics/283-polynomial-time-constant-error-unitary-synthesis-from-a-boolean-oracle.md)

# 283 — Polynomial-time, constant-error unitary synthesis from a Boolean oracle

[Index page](../index/mathematical-physics/283-polynomial-time-constant-error-unitary-synthesis-from-a-boolean-oracle.md)

## Original CONTENTS.md summary

[S1:7077] (family entry):

> **283. Polynomial-time unitary synthesis from a Boolean oracle.** Solves the constant-error Aaronson–Kuperberg unitary synthesis problem: a uniform polynomial-size quantum oracle circuit approximates every *n*-qubit unitary channel within diamond-norm error 1/2, after a suitable Boolean oracle is chosen. Gates, qubits, oracle calls and query length are polynomially bounded. The target-dependent oracle may have an unrestricted truth table; its efficient classical construction is not asserted.

[S2:658] carries the `\resultentry`, so the release blurb and the overview agree.
The single manuscript [S3:34, S3:36]:

> We give a positive answer to the constant-error formulation of the
Aaronson–Kuperberg unitary synthesis problem. For every $`n`$, a quantum oracle
circuit generated in polynomial time from $`n`$ alone can approximate the channel
of every $`n`$-qubit unitary to full diamond-norm error at most $`1/2`$, after a
suitable Boolean oracle is chosen. Using the fixed gates
$`H,T,T^\dagger,\mathrm{CNOT}`$, the circuit has polynomially many qubits,
elementary gates, and oracle calls, and its oracle queries have polynomial
length. The oracle may depend on the target unitary; the theorem does not give
an efficient classical procedure for constructing it. [S3:39–49]

## Undergraduate summary

A **unitary** is a quantum operation that preserves the total probability of
a system — rotate the state vector, never stretch or shrink it. The
**unitary synthesis problem** asks: can a single quantum circuit, built once
for a given size $`n`$, emulate *any* $`n`$-qubit unitary operation, as long as it
has access to a classical lookup table (a **Boolean oracle**) that encodes the
target operation? Aaronson and Kuperberg posed this in 2007.

This paper answers the **constant-error** version: the circuit gets the
target unitary *approximately* right, with full diamond-norm error at most
$`1/2`$. One circuit, determined by $`n`$ alone, works for every $`n`$-qubit
unitary after the right oracle is chosen. The circuit uses polynomially many
gates, qubits, and oracle calls, and each query has polynomial length [S3:39–49,
S2:658]. The oracle may depend on the target unitary; the theorem does not
give an efficient way to build it from a description of the unitary.

## Graduate summary

**Main theorem** (Theorem 1) [S4:46–58, S2:658].
There exist a polynomial $`p`$ and a deterministic classical algorithm which,
on input $`1^n`$, outputs in time at most $`p(n)`$ a quantum oracle circuit $`A_n`$
using the gates $`H, T, T^\dagger, \mathrm{CNOT}`$ and a single Boolean oracle
of input length $`m(n) \le p(n)`$. The circuit's total qubits, elementary gates,
and oracle calls are each at most $`p(n)`$. For every unitary
$`U \in U(2^n)`$ there is a function
$`f: \{0,1\}^{m(n)} \to \{0,1\}`$ for which the output channel
$`\Phi_{n,f}`$ of $`A_n^{O_f}`$ satisfies
$`\|\Phi_{n,f} - \mathcal{U}\|_\diamond \le 1/2`$.

**The reduction.** The central construction replaces synthesis of a
$`d`$-dimensional unitary by synthesis of a smaller, coherently controlled
unitary. Each reduction removes a fraction at least $`1/\mathrm{poly}(n)`$
of the dimension, so only polynomially many reductions are needed even when
$`d = 2^n`$. The smaller synthesis circuit is used exactly once at each step,
preventing the recursion from producing an exponentially large circuit
[S4:60–168].

**The mechanism.** After changes of basis (permutations, diagonal signs,
Walsh transforms), the current unitary is written as a block matrix
$`V = \begin{pmatrix}A & B \\ C & D\end{pmatrix}`$ with $`\|D\| \le 3/4`$.
Random diagonal signs and Walsh transforms supply this contracting block.
Closing the lower output back through a diagonal unitary $`Z`$ on the removed
coordinates gives a smaller unitary
$`F = A + BZ(I - DZ)^{-1}C`$ by the transfer-function construction. Two
nearly isometric maps $`\mathcal{E}`$ and $`\mathcal{R}`$ (encoders) satisfy an
approximate intertwining relation $`\widetilde{F}\,\mathcal{E} \approx
\mathcal{R}\,V`$, coming from truncating the forward and backward geometric
series associated with $`(I-DZ)^{-1}`$. The errors decay exponentially with
the truncation length [S4:60–168].

**Compilation.** The circuit is first built with programmable gates whose
entries may be arbitrary functions of control bits. A compilation step
replaces every such gate by a polynomial-length word over the fixed gate set,
read from one Boolean oracle. This compilation preserves relative phases
between different control values [S4:60–168].

## History of the conjecture

Aaronson and Kuperberg posed the unitary synthesis problem in 2007 [S4:1–10].
Aaronson later highlighted it among open problems in quantum query
complexity. The problem sits between state synthesis (prepare one specified
state) and full circuit synthesis (build a circuit for a named unitary):
unitary synthesis must act coherently on *every* input, not just prepare a
chosen column.

**Earlier work.** In state synthesis, Irani, Natarajan, Nirkhe, Rao, and Yuen
obtained one- and two-query results with polynomial space; Rosenthal gave
uniform polynomial-size circuits using one or four Boolean queries. For
unitary synthesis, Rosenthal gave a running-time upper bound of order
$`2^{n/2}`$ (exponential); Lombardi, Ma, and Wright proved a general one-query
lower bound; Dong, Lombardi, and Ma obtained explicit one-query separations
for structured families. Nehoran and Yuen showed every $`N`$-dimensional unitary
admits a constant-query implementation using diagonal-phase queries, but the
query width is exponential in $`n`$ for $`N = 2^n`$ [S4:69–168]. The result here
concerns polynomial *total* resources including query width, which is the
distinction from the constant-query results.

**Prior (my training data, not this repo).** The Aaronson–Kuperberg problem
(2007) is a well-known open problem in quantum complexity. The
transfer-function construction for unitary block matrices (Forgács, Klčar,
Kocsis, 2009) is a standard linear-algebraic tool. The constant-error
formulation with a target-dependent oracle of unrestricted truth-table size
is the novel contribution; I cannot confirm the polynomial resource bounds
independently from training alone.

## Consequences

- **The constant-error Aaronson–Kuperberg problem is resolved**
  [S3:39–49, S4:46–58]: a uniform polynomial-size quantum oracle circuit
  approximates every $`n`$-qubit unitary to diamond-norm error $`\le 1/2`$,
  with polynomially bounded gates, qubits, oracle calls, and query length.
- **The oracle is an existence witness, not a constructible object**
  [S4:60–68]: the theorem is an existence statement about an encoding of
  the target unitary. It does not give an efficient classical procedure for
  constructing the oracle from a description of $`U`$, and imposes no
  restriction on the truth-table size or classical circuit complexity of
  the oracle function.
- **Polynomial total resources, including query width** [S4:60–168]:
  the result concerns the total width of the oracle interface, distinguishing
  it from constant-query results whose query width is exponential in $`n`$.

## Section skeleton

One manuscript [S3:39–49], 7 sections under `build/sections/`:
introduction [S4:46–58], slots, contraction, fields, encoders, recursion,
compilation. A `references.tex` bibliography and a figure
(`figures/recursion.tex`) complete the tree. No verification bundle.

## Comparison with the formalized statement

The release does **not** formalize this family. There is no scope note under
`lean/docs/`, no comparator challenge stub under `lean/ComparatorChallenges/`,
and no `main_results` entry in `lean/formalization.yaml` naming it. The
ledger records `scope_note=0`, `chal=0`, and `mainres=0` [S5]. The
formalization gap is total: the synthesis theorem exists only as the
manuscript's LaTeX.

## Coverage

The ledger row `fam=283` [S5] records the tier and the counts:
`tier=T0`, `paps=1`, `paps_form=0`, `chal=0`, `mainres=0`,
`scope_note=0`, `verification=0`, `trace=`. The whole row is the coverage
signature: no scope note, no comparator, no `main_results` entry, and no
verification bundle, so the family sits entirely outside the release's
checking workflow. The shape flags are `bound|uniform`, `resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:7077] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 283 at [S2:658] |
| S3 | [`preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/build/main.tex`](../../../preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/build/main.tex) | 61 | the manuscript; title [S3:34], date [S3:36], abstract [S3:39–49] |
| S4 | [`preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026/build/sections/01-introduction.tex) | 168 | the introduction; main theorem [S4:46–58] |
| S5 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=283`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
