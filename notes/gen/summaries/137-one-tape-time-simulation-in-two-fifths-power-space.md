[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 137](../index/theoretical-computer-science/137-one-tape-time-simulation-in-two-fifths-power-space.md)

# 137 — One-tape time simulation in two-fifths-power space

[Index page](../index/theoretical-computer-science/137-one-tape-time-simulation-in-two-fifths-power-space.md)

## Original CONTENTS.md summary

[S1:3302] (family entry):

> **137. One-tape time simulation in two-fifths-power space.** Determines the halting and finite-control outcome of a fixed deterministic one-writable-tape machine up to time *T* using $`O(T^{2/5}\log^C(T+2))`$ space, improving the square-root exponent. Heads move at most one cell per step; finitely many read-only input heads are allowed. Initial contents are independent of $`T`$, and contents and input symbols have polylogarithmic-space access. Simulation time is unrestricted. (Lean)

[S2:351] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

A **Turing machine** writes on a tape as it computes. To **simulate**
one machine on a general-purpose computer, you must keep track of what's
on the tape. The naive approach copies the whole tape into memory, which
costs as much space as the tape has used — about $`O(T)`$ for a
computation of $`T`$ steps.

This family asks how little *space* a simulator can get by with. The
key observation: in $`T`$ steps, a one-tape head has only visited about
$`T`$ cells, and those cells are *roughly evenly spaced* from the origin.
By storing a compressed summary (a "block" partition) rather than the
raw tape, the simulator needs only

$$O\bigl(T^{2/5}\,\mathrm{polylog}\,T\bigr)$$

space [S4:64–79] — a genuine improvement over the $`O(T^{1/2})`$
"square-root" bound that was the long-standing best answer for this
model.

The result answers a specific open question about one-tape machines
[S3:41–42].

## Graduate summary

**Main theorem** ([S4:64–79], `thm:main`). "Fix a deterministic
machine with one writable tape and head, a fixed number of read-only
input heads, unit movement and fixed origins for all heads,
cap-independent symbol functions, and a fixed accessor as above. For
every public input $`x`$ and supplied binary cap $`T\ge2`$ for which the
access condition holds, its finite-control and halting outcome by time
$`T`$ can be computed deterministically in $`\widetilde O(T^{2/5})`$ work-space
bits, excluding storage for the read-only input. Simulation time is
unrestricted, and the final writable tape need not be materialized.
If the access condition holds for $`(x,T)`$ at every $`T\ge2`$, and the
machine halts on $`x`$ after $`t`$ steps without a supplied running time,
its outcome can be computed in $`\widetilde O((t+2)^{2/5})`$ work-space bits"
[S4:64–79].

**The two forms.** The theorem has a **capped** version (a binary
time cap $`T\ge2`$ is supplied) and an **unknown-time** version (no
cap; the bound is in the actual halting time $`t`$) [S6:9][S6:11]. The
capped simulator returns the finite-control outcome *and* the halting
flag by time $`T`$; the unknown-time simulator returns the halted
outcome on an input that halts.

**Improving the square-root exponent.** For any fixed
$`0<\delta<1/10`$, the bound is $`O(T^{1/2-\delta})`$, as requested by
**Williams's** one-tape simulation question [S4:85–87]. No log-free
endpoint at exponent $`2/5`$ is asserted.

**The scope is deliberately one-tape.** The result applies to one
writable head, even when additional read-only input heads are present;
it is *not* a two-fifths bound for arbitrary multitape machines
[S4:88–90]. A separate $`\widetilde O(\sqrt T)`$ simulation covers every fixed
number of writable tapes [S4:91–92].

## History of the conjecture

The question is a **space-bounded simulation** problem: how much
workspace is enough to run a given machine? For a one-writable-tape
deterministic machine, the classical target is to beat the
straightforward tape-copying $`O(T)`$ space.

**Williams** posed the one-tape simulation question — asking whether
the square-root workspace exponent is the right scale for this model
[S4:86–87]. The $`O(\sqrt T)`$ ("square-root") bound was the long-standing
best general answer, coming from storing the visited portion of the
tape with a coarse granularity.

The improvement here is to a **two-fifths** exponent,
$`T^{2/5}`$, by a more refined block-partition / compressed-window
argument: the simulator partitions the writable tape into blocks of a
chosen width and stores, per block, only the entries within the range
the head can reach at the relevant time [S4:94–95]. Because the head
moves at most one cell per step, the number of "active" blocks near the
origin is small, and the two-fifths power balances the block width
against the number of blocks that must be kept.

The **access condition** is the price: contents and input symbols must
be *accessible in polylogarithmic space* (a fixed accessor supplies
every symbol within distance $`T`$ of a head origin in polylog space)
[S3:39–41][S6:9]. This is a natural and standard hypothesis for
one-tape simulations — the symbols are simple, not arbitrary.

The mechanism is a shifted partition of the writable tape into blocks
[S4:94–95]; the proof then tracks which blocks are live at each time
and bounds the total workspace. General multitape simulation,
hierarchy consequences, and bounded-space-halting results are left to
other sections and are outside the selected statements [S6:11].

**Prior (my training data, not this repo).** One-tape simulation and
the relationship between time and workspace are classical
descriptive/complexity topics; the $`O(\sqrt T)`$ square-root workspace
bound for one-tape machines is a known general result. The exact
two-fifths exponent and its sharp dependence on the access condition
are the load-bearing claims of the release, and I cannot independently
confirm the precise exponent as a prior result; the release ships the
manuscript as proof.

## Consequences

- **A two-fifths workspace bound.** A fixed one-writable-tape
  deterministic machine is simulated in
  $`O(T^{2/5}\,\mathrm{polylog}\,T)`$ work-space bits up to a binary
  time cap $`T`$ [S4:64–79][S6:9].
- **An unknown-time variant.** On an input halting at time $`t`$, the
  outcome is computed in $`O((t+2)^{2/5}\,\mathrm{polylog}(t+2))`$
  space [S6:11].
- **The square-root exponent is improved.** For every fixed
  $`0<\delta<1/10`$ the bound is $`O(T^{1/2-\delta})`$, answering
  Williams's question for this model [S4:85–87][S3:41–42].
- **The bound is one-tape specific.** It is not a two-fifths bound for
  arbitrary multitape machines; a separate $`\widetilde O(\sqrt T)`$ result
  covers fixed numbers of writable tapes [S4:88–92].
- **Simulation time is unrestricted.** The result is a space bound
  only; the simulator's running time is not bounded [S4:73][S3:38].

## Section skeleton

The manuscript [S3] is a 51-line root: preamble, title, abstract
[S3:34–43], and five section files [S3:44–48] (under `build/source/`,
not `build/`). The sections, in order and line count: `introduction`
(136), `evaluation` (406), `simulation` (411), `multitape` (105),
`hierarchy` (156) — 1,214 section lines. The proof fixes the
accessor-based model, establishes the two-fifths bound through the
block-partition / window evaluation, and then treats the multitape
variant and the hierarchy consequences in the final two sections. The
shipped PDF [S5] is the manuscript in the form the release
distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note
[S6:9], one comparator stub [S7], and **two** `main_results`
declarations — the formalization is **complete at the declaration
level**.

The scope note [S6:9] states precisely what is formalized, in two
paragraphs:

- **The capped simulator** [S6:9]: "Given a binary time cap $`T\ge2`$,
  the simulator returns the source's finite-control outcome and
  halting flag using $`O(T^{2/5}(\log(T+2))^C)`$ space."
- **The unknown-time simulator** [S6:11]: "A second simulator needs no
  time cap: on an input that halts at time $`t`$, it returns the halted
  outcome using $`O((t+2)^{2/5}(\log(t+2))^C)`$ space. Simulation time
  is unrestricted." It excludes general multitape simulation,
  hierarchy consequences, and bounded-space-halting results.

The scope note links a single comparator config
[`OneTapeSpace.lean`] [S6:16]. That config carries **two**
`main_results` entries, one per simulator:

- `OAI.Fifths.Single.capped` in
  `OAI/Computability/SpaceSimulation/Main.lean`; and
- `OAI.Fifths.Single.unknown` in
  `OAI/Computability/SpaceSimulation/Main.lean`.

The `OneTapeSpace.lean` comparator stub [S7] (275 lines) defines the
machine and simulator machinery — the `Dir` / `Mark` / `Readers` /
`Tape` / `TM` / `Window` apparatus, the `Single` tape-simulation model,
and the `Access` predicate — and carries two statements, one per
simulator, each with a `sorry`:

- `capped` [S7:258–263] — there is a simulator $`N`$ and exponent $`e`$
  with a constant $`c`$ such that, for every input $`x`$ and cap
  $`T\ge2`$ satisfying the access condition, the outcome is computed
  within $`c\,T^{\mathrm{exponent}}(\log T)^e`$ space; `sorry` at
  [S7:263].
- `unknown` [S7:265–271] — the same for an input that halts at time
  $`t`$, within $`c\,(t+2)^{\mathrm{exponent}}(\log t)^e`$ space;
  `sorry` at [S7:271].

The comparator still carries its `sorry`s, but both declarations
`OAI.Fifths.Single.capped` and `OAI.Fifths.Single.unknown` exist in
the library's `main_results` list, so the challenge is registered as a
target the release set itself with named entry points. The reading is
of source text only — no `lake` or `lean` run elaborates the library,
so the claim here is that the statements and their `sorry` exist in
the source, not that the declarations are proved.

**Tree measurement (source-level).**

The `main_results` entry OAI.Fifths.Single.unknown resolves to `OAI/Computability/SpaceSimulation/Main.lean` (91 lines); the top-level theorem is `theorem accessed (A`.

No carrier `def … : Prop` is present; the theorem states its claim directly.

The surrounding directory carries 49 files with 497 theorems and 293 defs.

The preprint states 12 theorem environments; the tree carries 41× as many (source-level count, not a proof-quality ratio).

## Coverage

The ledger row `fam=137` [S8] records: `tier=T3`, `paps=1`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration
level**: the single `OneTapeSpace.lean` comparator config (counted once
in the ledger's `mainres` column, the distinct-config count) carries
two `main_results` declarations, `OAI.Fifths.Single.capped` and
`OAI.Fifths.Single.unknown`. The manuscript is formalized
(`paps_form=1`). The shape flags are `bound|partial`;
`resolves_named=0`; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3302], manuscript link [S1:3302] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 137 at [S2:351] |
| S3 | [`preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/source/main.tex`](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/source/main.tex) | 51 | document root; abstract [S3:34–43]; five section `\input` directives [S3:44–48]; 51 lines |
| S4 | [`preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/source/sections/introduction.tex`](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/build/source/sections/introduction.tex) | 136 | `thm:main` [S4:64–79]; 136 lines |
| S5 | [`preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf`](../../../preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf) | 11933 | the manuscript as shipped |
| S6 | [`lean/docs/137.md`](../../../lean/docs/137.md) | 17 | scope note — Scope at [S6:7], capped simulator [S6:9], unknown-time simulator [S6:11], comparator link at [S6:16] |
| S7 | [`lean/ComparatorChallenges/OneTapeSpace.lean`](../../../lean/ComparatorChallenges/OneTapeSpace.lean) | 275 | comparator — `capped` [S7:258–263] `sorry` [S7:263], `unknown` [S7:265–271] `sorry` [S7:271]; 275 lines |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=137`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
