[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 128](../index/theoretical-computer-science/128-a-factor-two-approximation-for-shortest-common-superstring.md)

# 128 — A factor-two approximation for shortest common superstring

[Index page](../index/theoretical-computer-science/128-a-factor-two-approximation-for-shortest-common-superstring.md)

## Original CONTENTS.md summary

[S1:3086] (family entry):

> **128. A factor-two approximation for shortest common superstring.** Gives a deterministic polynomial-time algorithm constructing a common superstring of length at most twice the optimum for every finite family of explicitly represented strings. The running time is polynomial in the full encoded input length, including symbol labels. ([Lean](lean/docs/128.md))

[S2:333] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

A **common superstring** of a set of strings is a longer string that
contains every member as a contiguous substring. The **shortest common
superstring** problem asks for the shortest such string. For example, given
"abc", "bca", and "cab", the shortest common superstring is "abcab"
(length 5), containing all three.

The approximation ratio measures how much longer the algorithm's output is
compared to the optimal (shortest) superstring. A **factor-2
approximation** means the algorithm's output is at most twice as long as
the optimum.

This family gives a **deterministic polynomial-time factor-2
approximation** [S4:5–10]. The algorithm applies to every finite family of
explicitly represented strings, with running time polynomial in the full
encoded input length (including symbol labels). This is the first
polynomial-time factor-2 approximation for the problem — prior best results
had a larger ratio [S4:13].

## Graduate summary

**Main theorem** ([S4:5–10], `thm:main`). "There is a deterministic
algorithm, polynomial in the total encoded input size, that on every finite
collection $\mathcal S$ of explicitly represented ordinary strings outputs
a common superstring $T$ satisfying $|T|\le 2\mathrm{OPT}(\mathcal S)$"
[S4:5–10]. The ratio is measured in symbols; the running time is
measured in bits of the explicitly encoded input, so the two measures are
deliberately distinguished [S4:3].

**Proof method.** The proof constructs integer counts on all substrings of
the inputs. The one-letter sum of these counts is a lower bound $W$ on the
optimum. The counts determine a balanced multigraph of cost $W$. Decomposing
the graph into closed walks and assigning a layer budget of $p$ to each
layer of period $p$ (total budget $W$), the connection procedure joins all
layers at additional cost at most $W$, giving the factor-2 bound [S4:13].

**Not the Greedy procedure.** The guarantee applies to the algorithm
constructed in the paper, not to the classical maximum-overlap Greedy
procedure [S3:45–46]. A September 2026 preprint of Shibata reports a
counterexample to the Greedy conjecture with worst-case ratio at least
$9/4$ [S4:13].

## History of the conjecture

**Tarhio and Ukkonen** proposed the factor-2 conjecture for the
maximum-overlap Greedy procedure in 1988. **Blum, Jiang, Li, Tromp, and
Yannakakis** established a polynomial-time $3$-approximation; **Sweedyk**
later obtained a $5/2$ guarantee. **Mucha** obtained $2+11/23$, and
**Englert, Matsakis, and Veselý** obtained
$(14+\sqrt{67})/9 < 2.466$. An August 2026 preprint of **Chukhin,
Kulikov, Mihajlin, and Smal** reports a $7/3$-approximation
[S4:13]. The theorem here answers affirmatively the question of whether
a polynomial-time factor-2 approximation exists.

The proof builds on the hierarchical graph formulation of **Golovnev,
Kulikov, and Mihajlin** and the Collapsing framework, where a superstring
is a closed walk on the all-substrings graph [S4:13].

**Prior (my training data, not this repo).** The shortest common
superstring problem is a classical NP-hard problem in string algorithms.
The factor-2 barrier had resisted all polynomial-time approaches for
decades; the best known approximation before this work was in the
$2.466$ range. A deterministic factor-2 approximation is a major
breakthrough. I cannot confirm the specific prior results independently;
the release ships the manuscript as proof.

## Consequences

- **A factor-2 approximation exists in polynomial time.** For every
  finite family of explicitly represented strings, a deterministic
  algorithm outputs a common superstring of length at most twice the
  optimum [S4:5–10].
- **The running time is in the full encoded input.** The polynomial
  bound is in the total bit length of the explicitly encoded input,
  including symbol labels [S4:3].
- **The result is for the algorithm constructed here.** The guarantee
  does not transfer to the Greedy procedure or any other prescribed
  algorithm [S3:45–46].
- **The proof is via the hierarchical graph.** The lower bound is the
  one-letter count sum $W$; the upper bound is $2W$ through the
  layer-budget connection procedure [S4:13].

## Section skeleton

The manuscript [S3] is a 56-line root: a 30-line preamble with package
declarations, title block, abstract [S3:41–47], seven section files
[S3:48–54], and a `references` import [S3:55]. The sections, in order and
line count: `01-introduction` (31), `02-counts` (107), `03-layers` (117),
`04-connections` (131), `05-processing` (147), `06-cycles` (68),
`07-algorithm` (26) — 627 section lines. The proof proceeds by constructing
substring counts and their balanced graph, developing the layer
representation, connecting layers within budget, processing equal primitive
texts, resolving remaining cycles, and finally proving polynomial time and
extracting the output string. The shipped PDF [S5] is the manuscript in
the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S6:9],
one comparator stub [S7:36–38], and **one** `main_results` declaration — the
formalization is **complete at the declaration level**.

The scope note [S6:9] states precisely what is formalized: "The shortest
common superstring problem asks for the shortest string containing each
input string as a contiguous substring. The formalized result gives one
deterministic polynomial-time algorithm whose output is a common superstring
of length at most twice the unrestricted optimum. It applies to every
finite list of explicitly encoded strings, with running time measured in
input bits and the approximation ratio measured in symbol length" [S6:9].

The scope note links a single comparator config [`Superstring.lean`]
[S6:15]. That config carries a `main_results` entry: declaration
`OAI.Superstring.main` in `OAI/Computability/Superstring/Main.lean`.

The `Superstring.lean` comparator stub [S7:36–38] (43 lines) defines the full
apparatus: `Symbol`, `Word`, `Instance` abbreviations, `encodeList` /
`encodeSymbol` / `encodeWord` / `encodeInstance`, `IsCommonSuperstring`,
`opt`, `HasPolynomialImplementation`, and the statement

- `main` [S7:36–38] — there exists a function $f$ from instances to words
  such that: (i) $f$ has a polynomial-time finite-stack-machine
  implementation in the encoded input, and (ii) for every instance $S$,
  $f(S)$ is a common superstring of $S$ with
  `length ≤ 2 * opt S`; `sorry` at [S7:39].

The comparator still carries a `sorry`, but the declaration
`OAI.Superstring.main` exists in the library's `main_results` list, so
the challenge is registered as a target the release set itself with a
named entry point. The reading is of source text only — no `lake` or
`lean` run elaborates the library, so the claim here is that the statement
and its `sorry` exist in the source, not that the declaration is proved.

## Coverage

The ledger row `fam=128` [S8] records: `tier=T3`, `paps=1`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration level**:
the `Superstring.lean` comparator config carries a `main_results` entry
with declaration `OAI.Superstring.main`. The manuscript is formalized
(`paps_form=1`). The shape flags are `partial|uniform`;
`resolves_named=0` — the result is a factor-2 approximation, not a
resolution of a named conjecture; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3086], manuscript link [S1:3086] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 128 at [S2:333] |
| S3 | [`preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/paper.tex`](../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/paper.tex) | 56 | document root; abstract [S3:41–47]; seven section `\input` directives [S3:48–54]; 56 lines |
| S4 | [`preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/sections/01-introduction.tex`](../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/build/sections/01-introduction.tex) | 31 | `thm:main` [S4:5–10]; 31 lines |
| S5 | [`preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf`](../../preprints/A-Polynomial-Time-2-Approximation-for-Shortest-Common-Superstring-September-24-2026/paper.pdf) | 10588 | the manuscript as shipped |
| S6 | [`lean/docs/128.md`](../../lean/docs/128.md) | 15 | scope note — Scope at [S6:9], comparator link at [S6:15] |
| S7 | [`lean/ComparatorChallenges/Superstring.lean`](../../lean/ComparatorChallenges/Superstring.lean) | 43 | comparator — `main` [S7:36–38], `sorry` at [S7:39]; 43 lines |
| S8 | [`notes/gen/tables/catalog.tsv`](../../notes/gen/tables/catalog.tsv) | 373 | the ledger row `fam=128`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
