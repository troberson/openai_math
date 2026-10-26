[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 124](../index/theoretical-computer-science/124-polynomial-time-scheduling-on-three-identical-machines.md)

# 124 — Polynomial-time scheduling on three identical machines

[Index page](../index/theoretical-computer-science/124-polynomial-time-scheduling-on-three-identical-machines.md)

## Original CONTENTS.md summary

[S1:3013] (family entry):

> **124. Polynomial-time scheduling on three identical machines.** Resolves the three-processor unit-job scheduling problem of Garey and Johnson: a deterministic polynomial-time algorithm minimizes makespan for nonpreemptive unit-length jobs with arbitrary precedence constraints on three identical parallel machines. For an explicitly given precedence graph, it decides deadline feasibility exactly and constructs a feasible schedule. ([Lean](lean/docs/124.md))

[S2:325] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Scheduling** is the art of assigning work to machines. You have a set of
jobs, each taking one unit of time, and three identical machines. Some jobs
must finish before others can start — a **precedence constraint**. The
question is: can you finish everything by a deadline, and if so, what is the
shortest possible makespan (the time the last job finishes)?

With two machines the problem is easy — solved in the 1960s. With a
variable number of machines it is NP-complete. The **three-machine** case
sat open as problem OPEN8 in the classic Garey–Johnson book for over four
decades.

This family resolves it: a deterministic polynomial-time algorithm finds
the optimal schedule [S3:120–130]. The catch is the exponent —
$O((L+2)^{150020})$ — polynomial in principle, useless in practice.
The proof works by showing that every feasible schedule can be broken
into intervals whose job sets are describable by short Boolean formulas
[S3:456–460], and then doing a dynamic program over those descriptions.

## Graduate summary

**Main theorem** ([S3:120–130], `thm:main`). "Let an explicitly listed
finite directed acyclic graph specify the precedence constraints on
$n\ge1$ nonpreemptive unit-length jobs on three identical machines. There
is a uniform deterministic algorithm that constructs a feasible schedule of
minimum makespan. Given also an integer deadline $1\le T\le n$, it decides
feasibility exactly and returns a schedule whenever the answer is
affirmative. Both tasks can be performed in $O((L+2)^{150020})$ steps on a
deterministic multitape Turing machine, where $L$ is the total binary input
length" [S3:120–130]. The model is the explicit one: the graph is listed
vertex by vertex and edge by edge, and the deadline is an integer in
$[1,n]$.

**Algorithm** ([S3:374–379], `prop:algorithm`). "This is a uniform
deterministic polynomial-time algorithm. Every set it accepts has a full
schedule, which the algorithm can explicitly return. With $K=10000$, its
deadline decision and schedule construction take
$O((L+2)^{150020})$ deterministic multitape steps" [S3:374–379]. The
algorithm enumerates a fixed family of Boolean formulas with at most
$K=10000$ leaves over atomic tests (rank thresholds, membership in job
triples and their precedence cones), evaluates each to a subset of the job
set, and runs a dynamic program over the resulting states
[S3:341–372].

**Structural theorem** ([S3:456–460], `thm:structure`). "Every feasible
full three-machine schedule has a bounded-description hierarchy. In fact,
the global node predicates and relative split predicates needed in the
hierarchy have fewer than $500$ leaves" [S3:456–460]. This is the key
completeness step: it shows the finite search covers every feasible
instance. The proof spans five sections — separators [S4], construction
[S5], lists [S6], boundary [S7], and descriptions [S8] — totaling 1,144
lines of structural lemmas.

## History of the conjecture

The two-processor case was solved by **Fujii, Kasami, and Ninomiya** and
**Coffman and Graham** in the 1960s–70s; allowing the number of machines
to be part of the input yields an NP-complete problem
(**Ullman**) [S3:82–93]. The fixed-three decision problem appears as
**OPEN8** in Appendix A13 of **Garey and Johnson** and has remained a
central complexity question in scheduling [S3:82–93].

Structural restrictions on precedence yielded intermediate results.
**Garey, Johnson, Tarjan, and Yannakakis** gave a linear-time algorithm on
three processors for opposing forests [S3:138–153]. **Dolev and Warmuth**
obtained $O(n^{h(m-1)+1})$ when the precedence graph has height $h$ and at
most $m$ processors are available per slot — polynomial when both are
fixed [S3:138–153].

**Nederlof, Swennenhuis, and Węgrzycki** developed the structural approach
into an exact algorithm with running time
$(1+n/m)^{O(\sqrt{nm})}$, hence $2^{O(\sqrt n\log n)}$ for three machines —
subexponential but not polynomial [S3:155–169]. Their decomposition at
selected slots and memoization of subproblems described by source and sink
sets already control the number of subproblems. This family builds on that
decomposition viewpoint but proves the separator statements and
global-description bounds directly, without specializing their
subexponential bound [S3:155–169].

Approximation algorithms also revealed recursive structure: **Levey and
Rothvoß**, **Garg**, **Li**, and **Das and Wiese** gave
$(1+\varepsilon)$-approximations with quasipolynomial running time
[S3:171–183].

**Prior (my training data, not this repo).** The three-machine unit-job
scheduling problem (GJ OPEN8) was a long-standing open problem in
algorithmic scheduling. A polynomial-time resolution is a significant
positive result at the frontier of the problem, though the exponent
150020 makes the algorithm purely existential. I cannot confirm the
specific prior results independently; the release ships the manuscript as
proof.

## Consequences

- **GJ OPEN8 is resolved.** The three-processor unit-job scheduling
  problem with arbitrary precedence constraints is in P: a deterministic
  polynomial-time algorithm minimizes makespan and decides deadline
  feasibility exactly [S3:120–130].
- **The algorithm is explicit and constructive.** It returns a feasible
  schedule whenever one exists, not just a certificate of existence
  [S3:374–379].
- **The running time is polynomial but impractical.** The exponent 150020
  is a fixed constant independent of the input, so the algorithm is
  polynomial in the formal sense, but no practical running-time claim is
  made [S3:120–130].
- **The proof technique is a bounded-description dynamic program.** The
  key structural insight is that every feasible schedule decomposes into
  intervals whose job sets are describable by Boolean formulas with fewer
  than 500 leaves, independent of decomposition depth [S3:456–460].
- **The subexponential-to-polynomial gap is closed.** The prior best
  exact algorithm was $2^{O(\sqrt n\log n)}$ [S3:155–169]; this result
  brings the running time to polynomial at the cost of a large exponent.

## Section skeleton

The manuscript [S3] is a 541-line root: a preamble, title block, abstract
[S3:69–77], introduction [S3:80–235], preliminaries [S3:237–339], the
algorithm and structural certificate [S3:341–479], running-time
accounting [S3:480–535], and a `bibliographystyle`/`bibliography` pair
[S3:539–540]. Five section files are imported at [S3:475–479] and the
conclusion at [S3:537]:

- `separators` [S4] (162 lines) — shared-cutoff separators, 5 environments
- `construction` [S5] (239 lines) — child-interval construction, 1
  environment
- `lists` [S6] (372 lines) — inherited predicate lists, 8 environments
- `boundary` [S7] (168 lines) — global boundary invariants, 3 environments
- `descriptions` [S8] (203 lines) — bounded-description hierarchy, 3
  environments

Total: 1,144 section lines plus 13-line conclusion [S9]. The shipped PDF
[S10] is the manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note [S11:9]
and one comparator stub [S12:95–96], but **no** `main_results` declaration.
This is a structural absence: the scope note links a comparator config,
and that config has no proved declaration in `lean/OAI/`.

The scope note [S11:9] describes the formalized content: "The formalization
gives a deterministic polynomial-time algorithm for scheduling nonempty
collections of unit-length jobs with arbitrary acyclic precedence
constraints on three identical parallel machines. It constructs a schedule
of minimum makespan and decides exactly whether a valid specified deadline
can be met. The algorithm is one fixed finite machine, and its running
time is bounded by a polynomial in the binary input length" [S11:9].

The scope note links a single comparator config
[`ThreeMachine.lean`] [S11:15].

The `ThreeMachine.lean` comparator stub [S12:95–96] (100 lines) defines the full
scheduling apparatus: `Instance` (a DAG over `Fin n`), `Feasible`
(a slot assignment respecting precedence and the machine count),
`CorrectOutput` (the machine's output encodes a correct schedule or
rejection), `Machine` / `Configuration` (a multitape Turing machine), and
`ReleaseTheorem` — an existential statement that there exists a machine
and a polynomial time bound such that the machine produces a correct
output for every acyclic input. It declares one theorem, closing with
`sorry`:

- `main_theorem` [S12:95–96] — the `ReleaseTheorem` existence claim;
  `sorry` at [S12:96].

There is no `OAI/**` declaration that proves the theorem, so the
formalization stops at the challenge stub.

The reading is of source text only — no `lake` or `lean` run elaborates
the library, so the claim here is that the stub's statement and its
`sorry` exist in the source, not that anything is proved.

## Coverage

The ledger row `fam=124` [S13] records: `tier=T2`, `paps=1`,
`paps_form=0`, `chal=1`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **incomplete**: the scope note links
the `ThreeMachine.lean` comparator config, but that config has no
`main_results` entry and no proved declaration — a T2 structural
absence. The manuscript is unformalized (`paps_form=0`). The shape flags
are `resolution|uniform`; `resolves_named=1` — the result resolves the
named Garey–Johnson problem OPEN8; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3013], manuscript link [S1:3013] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 124 at [S2:325] |
| S3 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/paper.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/paper.tex) | 541 | document root; abstract [S3:69–77]; `thm:main` [S3:120–130]; `prop:algorithm` [S3:374–379]; `thm:structure` [S3:456–460]; six `\input` directives [S3:475–479, 537]; 541 lines |
| S4 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/separators.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/separators.tex) | 162 | shared-cutoff separators; 5 environments; 162 lines |
| S5 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/construction.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/construction.tex) | 239 | child-interval construction; 1 environment; 239 lines |
| S6 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/lists.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/lists.tex) | 372 | inherited predicate lists; 8 environments; 372 lines |
| S7 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/boundary.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/boundary.tex) | 168 | global boundary invariants; 3 environments; 168 lines |
| S8 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/descriptions.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/descriptions.tex) | 203 | bounded-description hierarchy; 3 environments; 203 lines |
| S9 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/conclusion.tex`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/conclusion.tex) | 13 | conclusion; 13 lines |
| S10 | [`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf`](../../preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) | 6939 | the manuscript as shipped |
| S11 | [`lean/docs/124.md`](../../lean/docs/124.md) | 15 | scope note — Scope at [S11:9], comparator link at [S11:15] |
| S12 | [`lean/ComparatorChallenges/ThreeMachine.lean`](../../lean/ComparatorChallenges/ThreeMachine.lean) | 100 | the comparator — `main_theorem` [S12:95–96]; 100 lines |
| S13 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=124`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
