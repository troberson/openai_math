[Notes](../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 133](../index/theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md)

# 133 — The complexity of Weisfeiler–Leman refinement

[Index page](../index/theoretical-computer-science/133-complexity-of-weisfeiler-leman-refinement.md)

## Original CONTENTS.md summary

[S1:3184] (family entry):

> **133. The computational complexity of Weisfeiler–Leman refinement.** Proves unconditional $`n^{\Omega(k)}`$ deterministic time lower bounds for joint and separate k-dimensional Weisfeiler–Leman equivalence, for sufficiently large fixed k in the specified sequential adjacency-matrix models. With dimension as input, joint equivalence is EXPTIME-complete even on subcubic graphs; deciding whether refinement identifies a graph is also EXPTIME-complete. ([Lean](lean/docs/133.md))

[S2:343] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

**Weisfeiler–Leman refinement** ($k$-WL) is a family of graph
algorithms. The $k=1$ version, **color refinement**, repeatedly
recolors each vertex by the multiset of its neighbors' colors until the
colors stop changing. Two graphs are *1-WL equivalent* if they end up
with the same color histogram. Higher dimensions ($k=2,3,\ldots$)
track ordered $k$-tuples of vertices instead of single vertices,
capturing increasingly fine structural information.

$k$-WL equivalence is a **necessary condition** for graph isomorphism:
isomorphic graphs are always $k$-WL equivalent, but the converse can
fail. The refinement is the workhorse of practical isomorphism
testing and of many graph-invariant computations.

This family asks: **how hard is it to decide $k$-WL equivalence?** Four
manuscripts answer different facets:

- **Parity lifts**: for fixed $k\ge4$, one can reduce the problem of
  finding a successful choice in a constraint system to checking
  $k$-WL equivalence of two constructed graphs [S4:76–96]. This gives
  the bounded-treewidth witness structure.
- **Identification**: deciding which dimension $k$ first identifies a
  graph among all its non-isomorphic mates is **EXPTIME-complete**
  [S6:36–44].
- **Unconditional lower bound**: deciding $k$-WL equivalence for fixed
  large $k$ requires **$n^{\Omega(k)}$** sequential time — no
  complexity assumption [S7:40–50].
- **Variable dimension**: when $k$ is part of the input, joint
  $k$-WL equivalence is **EXPTIME-complete**, even on subcubic
  graphs [S10:28–31].

## Graduate summary

**Parity reduction** ([S4:76–96], `thm:choice-reduction`). "Fix
$k\ge4$, either refinement convention, and the corresponding $t$ in
\eqref{eq:bag-parameter}. From every choice system on $t$ domains one
can explicitly construct two uncolored simple graphs $X_0,X_\star$ of
equal order such that $X_0\equiv_k X_\star \iff$ the choice system has
no successful choice" [S4:76–96]. The common order is at most
$A M_t$ where $M_t = t\,2^{t-2+3\binom{t-1}{2}} + 12\binom{t}{3}$.
When a successful choice exists, the histograms differ after at most
two joint rounds (or one separate round) [S4:87–95].

**Identification EXPTIME-completeness** ([S6:36–44], `thm:main`).
"The following problem is EXPTIME-complete under deterministic
polynomial-time many-one reductions: given a nonempty finite simple
undirected uncolored graph $G$ by its adjacency matrix and a positive
integer $k$ in binary, decide whether $\mathrm{WLdim}(G)\le k$" [S6:36–44].
The identification problem quantifies over every comparison graph
[S11:16].

**Unconditional time lower bound** ([S7:40–50], abstract). "For every
sufficiently large fixed $k$, deciding whether two $n$-vertex graphs
are $k$-Weisfeiler–Leman equivalent requires $n^{\Omega(k)}$
deterministic sequential time in the worst case" [S7:40–50]. The bound
holds at every sufficiently large graph order, even for simple
connected uncolored graphs of diameter at most two, without a
complexity assumption [S7:43–46]. The proof concludes with
$T_A(n)\ge n^{c_0 k}$ for every $n\ge M^{20}$ [S8:258–266].

**Variable-dimension EXPTIME-completeness** ([S10:28–31],
`thm:main`). "Both $\textnormal{\textsc{WL-Equiv}}$ and $\textnormal{\textsc{Subcubic-WL-Equiv}}$ are $\mathsf{EXPTIME}$-complete under
deterministic polynomial-time many-one reductions" [S10:28–31]. Here
$\textnormal{\textsc{WL-Equiv}}$ is joint-update $k$-WL equivalence with $k\ge2$ as input, and
$\textnormal{\textsc{Subcubic-WL-Equiv}}$ is the restriction to connected simple uncolored graphs of
equal positive order and maximum degree at most three
[S10:33–38].

## History of the conjecture

**Weisfeiler and Leman** (1968) introduced the $k$-dimensional
refinement as a generalization of the graph invariants used in
chemical graph theory. **Lovász** (1967) independently showed that the
1-dimensional version (color refinement / equitable partition) is
equivalent to the first Weisfeiler–Leman test, establishing the
connection to graph isomorphism.

**Cai, Fürer, and Immerman** (1992) proved the fundamental
correspondence: two graphs are $k$-WL equivalent if and only if they
satisfy the same sentences of $k$-dimensional first-order logic
($\mathrm{FO}^k$). This placed $k$-WL at the intersection of graph
theory and finite model theory, and showed that the refinement
captures exactly the expressive power of $\mathrm{FO}$ with $k$
variables.

The **bounded-treewidth** connection: $k$-WL equivalence on graphs of
treewidth $<k$ implies isomorphism, so the parity-lift construction
[S4:76–96] converts a constraint-satisfaction question into a WL
equivalence question on graphs with controlled structure.

The **complexity-theoretic** direction — determining the computational
cost of running $k$-WL — is the subject of this family. The
unconditional $n^{\Omega(k)}$ lower bound [S7:40–50] is notable
because it makes no assumption (no ETH, no randomized lower bound):
it is a deterministic, worst-case, sequential-time bound that holds
for any algorithm, not just the canonical refinement procedure
[S8:288–291].

**Prior (my training data, not this repo).** The Cai–Fürer–Immerman
correspondence and the Lovász equivalence are standard results in
finite model theory and graph theory. The EXPTIME-completeness of
variable-dimension WL equivalence follows the general pattern that
logistic-circuit problems parameterized by dimension become
EXPTIME-complete when the dimension is part of the input. The
unconditional lower bound technique (diagonalization + compression +
circuit simulation) is a standard complexity-theoretic toolkit. I
cannot confirm the specific prior results independently; the release
ships the manuscripts as proof.

## Consequences

- **$k$-WL equivalence is inherently exponential in $k$.** For fixed
  sufficiently large $k$, no algorithm decides $k$-WL equivalence in
  sub-$n^{\Omega(k)}$ sequential time [S7:40–50].
- **The lower bound is unconditional and model-robust.** It covers
  both joint and separate conventions, both multitape TM and
  sequential log-word RAM, and requires no complexity assumption
  [S7:43–46][S8:266].
- **Identification is EXPTIME-complete.** Deciding the WL dimension
  that identifies a graph is among the hardest problems in EXPTIME
  [S6:36–44].
- **Variable-dimension equivalence is EXPTIME-complete even on
  subcubic graphs.** The subcubic restriction $\textnormal{\textsc{Subcubic-WL-Equiv}}$ does not
  simplify the problem [S10:28–31][S10:33–38].
- **Parity lifts give bounded-treewidth witnesses.** For $k\ge4$,
  WL-equivalence witnesses can be read off graphs of controlled
  treewidth, connecting WL to the parameterized-complexity of
  constraint satisfaction [S4:76–96].

## Section skeleton

Four manuscripts, all shipping a compiled `paper.pdf`:

**MS1** [S3] — *Parity lifts and bounded-treewidth witnesses*. A
54-line root: preamble, title, abstract [S3:34–44], five sections
[S3:46–50]. Sections: `01-introduction` (255), `02-wl-tests` (199),
`03-parity-lifts` (174), `04-separator` (208), `05-complexity` (247) —
1,083 section lines. The proof develops the parity-lift construction,
verifies the WL-equivalence characterization, and extracts the
bounded-treewidth witness.

**MS2** [S5] — *The complexity of identifying a graph by WL
refinement*. A 55-line root: preamble, title, abstract [S5:34–40],
seven sections [S5:44–50], bibliography [S5:53]. Sections:
`01-introduction` (160), `02-wl` (219), `03-encoding` (327),
`04-offsets` (266), `05-projection` (441), `06-computation` (84),
`07-identification` (322) — 1,819 section lines. The proof encodes
the identification problem, projects through the offset machinery, and
reduces from a canonical EXPTIME problem.

**MS3** [S7:40–50] — *Unconditional time lower bounds for WL
equivalence*. A 267-line root: a long preamble (package declarations,
definitions), title, abstract [S7:40–50], five sections [S7:260–264],
references [S7:265]. Sections: `01-game` (192), `02-compression`
(591), `03-circuits` (398), `04-diagonal` (220), `05-transfer` (292) —
1,693 section lines. The proof establishes the WL/bijective-game
correspondence, compresses the computation, simulates it in circuits,
diagonalizes against all polynomial-time machines, and transfers the
diagonal lower bound to explicit graph inputs.

**MS4** [S9] — *Variable-dimension WL equivalence on general and
subcubic graphs*. A 67-line root: preamble, title, abstract [S9:49–55],
eight sections [S9:57–64] in the order 01,02,03,04,05,07,06,08.
Sections: `01-introduction` (229), `02-refinement-game` (228),
`03-computation-images` (429), `04-blocks-projection` (592),
`05-general-realization` (115), `06-subcubic-realization` (548),
`07-game-reduction` (311), `08-uniformity` (320) — 2,772 section
lines. The proof builds the computation-image encoding, realizes it in
general and subcubic graphs, and reduces from a canonical EXPTIME
problem through the game interface.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note
[S11:12] and **four** comparator stubs, but **no** `main_results`
declarations. This is a structural absence: all four scope-note links
point to comparator configs, and none of those configs carries a
`main_results` entry in `lean/formalization.yaml`.

The scope note [S11:12] states precisely what is formalized. The four
scope paragraphs:

- **Parity-lift construction** [S11:12]: "The formalization gives the
  paper's parity-lift graph construction for every Weisfeiler–Leman
  dimension $k\ge4$, under both joint and separate conventions. From a
  finite choice system it constructs two equal-size uncolored graphs
  that are Weisfeiler–Leman equivalent exactly when the system has no
  successful compatible choice. The same equivalence holds for the
  pure variant" [S11:12].
- **Identification** [S11:16]: "The formalization proves that deciding
  whether Weisfeiler–Leman refinement of a supplied dimension
  identifies a graph is EXPTIME-complete under polynomial-time
  many-one reductions" [S11:16].
- **Unconditional lower bound** [S11:18–20]: "The formalization proves
  an unconditional deterministic time lower bound for deciding
  $k$-dimensional Weisfeiler–Leman equivalence. For every sufficiently
  large fixed $k$, every deciding algorithm in the stated multitape
  Turing-machine or sequential logarithmic-word RAM model requires at
  least $n^{ck}$ worst-case time" [S11:18], covering "both joint and
  separate replacement conventions and remains valid for explicit
  adjacency-matrix inputs restricted to simple connected uncolored
  graphs of diameter at most two" [S11:20].
- **Variable dimension** [S11:22]: "The formalization proves
  EXPTIME-completeness of deciding joint-update $k$-dimensional
  Weisfeiler–Leman equivalence when $k\ge2$ is part of the input in
  binary" [S11:22].

The scope note links four comparator configs [S11:28–31]. **None**
carries a `main_results` entry, so the formalization stops at the
challenge-stub level for all four results.

The four comparator stubs:

- `ParityLifts.lean` [S12:204–205] (209 lines) — defines the choice-system
  and WL-equivalence machinery and one statement:
  `parity_reduction` [S12:204], `sorry` at [S12:205].
- `WLIdentification.lean` [S13:140–142] (146 lines) — defines
  `EXPTIMEComplete` and `dimensionLanguage` and one statement:
  `main` [S13:140], `sorry` at [S13:142].
- `WeisfeilerLeman.lean` [S14:259] (270 lines) — defines the
  `Convention`, `InputClass`, `Model`, `worstTime` apparatus and the
  `MainClaim` [S14:259] ($\exists c>0, k_0, \forall k\ge k_0, \forall$
  convention, input class, model: deciding time $\ge n^{ck}$), and one
  statement: `unconditional_time_lower_bound` [S14:267], `sorry` at
  [S14:268].
- `VariableWL.lean` [S15:125–126] (130 lines) — defines `WL` and `SubWL`
  languages and one statement:
  `main : EXPTIMEComplete WL ∧ EXPTIMEComplete SubWL` [S15:125],
  `sorry` at [S15:126].

There is no `OAI/**` declaration that proves any of the four
statements, so the formalization stops at the challenge stubs. The
reading is of source text only — no `lake` or `lean` run elaborates
the library, so the claim here is that the statements and their
`sorry` exist in the source, not that anything is proved.

## Coverage

The ledger row `fam=133` [S16] records: `tier=T2`, `paps=4`,
`paps_form=0`, `chal=4`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **incomplete**: the single scope
note links four comparator configs, but none of them carries a
`main_results` entry and no proved declaration exists under
`lean/OAI/` — a T2 structural absence across all four results.
All four manuscripts are unformalized (`paps_form=0`). The shape flag
is `bound`; `resolves_named=0`; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../CONTENTS.md) | 9142 | the release's catalog — family entry [S1:3184], manuscript links [S1:3184] |
| S2 | [`overview.tex`](../../overview.tex) | 859 | the release's `\resultentry` list — 133 at [S2:343] |
| S3 | [`preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/build/main.tex`](../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/build/main.tex) | 54 | document root; abstract [S3:34–44]; five section `\input` directives [S3:46–50]; 54 lines |
| S4 | [`preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/build/sections/01-introduction.tex`](../../preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/build/sections/01-introduction.tex) | 255 | `thm:choice-reduction` [S4:76–96]; 255 lines |
| S5 | [`preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/build/paper.tex`](../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/build/paper.tex) | 55 | document root; abstract [S5:34–40]; seven section `\input` directives [S5:44–50], bibliography [S5:53]; 55 lines |
| S6 | [`preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/build/sections/01-introduction.tex`](../../preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/build/sections/01-introduction.tex) | 160 | `thm:main` [S6:36–44]; 160 lines |
| S7 | [`preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/build/main.tex`](../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/build/main.tex) | 267 | document root; abstract [S7:40–50]; five section `\input` directives [S7:260–264], references [S7:265]; 267 lines |
| S8 | [`preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/build/sections/05-transfer.tex`](../../preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/build/sections/05-transfer.tex) | 292 | lower-bound proof concludes [S8:258–266]; 292 lines |
| S9 | [`preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/build/main.tex`](../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/build/main.tex) | 67 | document root; abstract [S9:49–55]; eight section `\input` directives [S9:57–64]; 67 lines |
| S10 | [`preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/build/sections/01-introduction.tex`](../../preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/build/sections/01-introduction.tex) | 229 | `thm:main` [S10:28–31]; 229 lines |
| S11 | [`lean/docs/133.md`](../../lean/docs/133.md) | 31 | scope note — Scope at [S11:10], four comparator links [S11:28–31] |
| S12 | [`lean/ComparatorChallenges/ParityLifts.lean`](../../lean/ComparatorChallenges/ParityLifts.lean) | 209 | comparator — `parity_reduction` [S12:204], `sorry` at [S12:205]; 209 lines |
| S13 | [`lean/ComparatorChallenges/WLIdentification.lean`](../../lean/ComparatorChallenges/WLIdentification.lean) | 146 | comparator — `main` [S13:140], `sorry` at [S13:142]; 146 lines |
| S14 | [`lean/ComparatorChallenges/WeisfeilerLeman.lean`](../../lean/ComparatorChallenges/WeisfeilerLeman.lean) | 270 | comparator — `MainClaim` [S14:259], `unconditional_time_lower_bound` [S14:267], `sorry` at [S14:268]; 270 lines |
| S15 | [`lean/ComparatorChallenges/VariableWL.lean`](../../lean/ComparatorChallenges/VariableWL.lean) | 130 | comparator — `main` [S15:125], `sorry` at [S15:126]; 130 lines |
| S16 | [`notes/tables/catalog.tsv`](../../notes/tables/catalog.tsv) | 373 | the ledger row `fam=133`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
