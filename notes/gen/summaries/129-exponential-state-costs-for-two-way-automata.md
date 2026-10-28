[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 129](../index/theoretical-computer-science/129-exponential-state-costs-for-two-way-automata.md)

# 129 — Exponential state costs for two-way automata

[Index page](../index/theoretical-computer-science/129-exponential-state-costs-for-two-way-automata.md)

## Original CONTENTS.md summary

[S1:3111] (family entry):

> **129. Exponential state costs for two-way automata.** Proves exponential lower bounds both for complementing two-way nondeterministic finite automata and for simulating one-way nondeterministic automata by two-way deterministic ones. The latter resolves the Sakoda–Sipser state-succinctness conjecture over growing finite alphabets; both results rule out polynomial state bounds independent of alphabet size. (Lean)

[S2:335] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

A **finite automaton** is a machine that reads an input string and decides
whether to accept it. A **one-way** automaton reads left to right; a
**two-way** automaton's head can move left, right, or stay in place. A
**nondeterministic** automaton (NFA) can branch at each step; a
**deterministic** automaton has exactly one move per state and symbol.

**Complementation** means: given an NFA that accepts language $L$, build
one that accepts everything $L$ does not. **Determinization** means: given
an NFA, build an equivalent deterministic one.

Both operations can blow up the number of states. This family proves that
the blow-up is **exponential** and that no polynomial bound is possible
when the alphabet grows with the input.

MS1 [S4:38–48] constructs, for every $n\ge4$, an $n$-state two-way NFA
whose complement requires at least
$\tfrac12\,2^{\lfloor(n-4)/127\rfloor}-1$ states. MS2 [S8:99–110] shows
that a one-way NFA with $h+3$ states (no left moves) has an equivalent
two-way DFA requiring $s\ge2^{\lfloor(h-2)/31\rfloor}/4-2$ states.
Both results rule out polynomial state bounds independent of alphabet size.

## Graduate summary

**MS1 main theorem** ([S4:38–48], `main:theorem`). "For every integer
$n\ge4$, set $H=\{1,\ldots,n-2\}$ and $\Sigma_n=\mathcal R_H$. There is
an $n$-state 2NFA $A_n$ recognizing $L_H$ such that every 2NFA recognizing
$\Sigma_n^*\setminus L(A_n)$ has at least
$\tfrac12\,2^{\lfloor(n-4)/127\rfloor}-1$ states. In particular, there is
no polynomial state bound for complementation that is independent of the
finite alphabet" [S4:38–48]. The alphabet $\Sigma_n$ consists of all
binary relations on a set of $n-2$ points, so $|\Sigma_n|=2^{(n-2)^2}$
[S4:50–51].

**MS2 main theorem** ([S8:99–110], `thm:main`). "For every integer
$h\ge2$, the language $\mathsf{OWL}_h$ is recognized by a nondeterministic
automaton with $h+3$ states using no left moves. Every equivalent
deterministic two-way automaton with $s$ states satisfies
$4(s+2)^2\ge 2^{\lfloor(h-2)/31\rfloor}$. If an initially accepting
configuration counts as acceptance, $s+2$ may be replaced by $s+1$"
[S8:99–110]. The language $\mathsf{OWL}_h$ is **one-way liveness**: a word of
binary relations on $h$ points is accepted when their ordered product is
nonempty [S7:9–10].

**Sakoda–Sipser context.** MS2's witness is Sakoda and Sipser's complete
family $B_h$, now called one-way liveness. Their Theorem 2.3 establishes
this family's completeness for one-to-two-way conversion
[S8:9–23]. The proof here gives the small nondeterministic side ($h+3$
states, no left moves) and the exponential lower bound against
unrestricted two-way deterministic targets [S8:27–36].

## History of the conjecture

**Sakoda and Sipser** posed the state cost of converting one-way and
two-way automata in 1978. Their Theorem 2.3 establishes the one-way
liveness family's completeness for the one-to-two-way conversion
[S8:9–23]. The question asked whether exponential state blow-up was
necessary for the conversion.

Earlier exponential lower bounds restricted the motion of the
deterministic target. **Sipser** proved an exponential separation for
sweeping automata, whose head changes direction only at an endmarker
[S8:28–29]. Quadratic lower bounds against unrestricted two-way
deterministic targets were known, but the exponential case over growing
alphabets was open [S8:36].

MS1's proof builds on a nesting and amplification construction over the
relational alphabet $\mathcal R_H$: the $n$-state automaton $A_n$
recognizes a language $L_H$ whose complement forces exponential state
growth through a 127-state amplification layer
[S4:38–48].

**Prior (my training data, not this repo).** The state complexity of
converting between automaton types is a classical question in automata
theory. Sakoda and Sipser's 1978 paper established the one-way liveness
family and proved its completeness for the one-to-two-way conversion.
Exponential lower bounds for complementation of two-way NFAs over growing
alphabets are significant results in automata theory. I cannot confirm
the specific prior results independently; the release ships the two
manuscripts as proofs.

## Consequences

- **Two-way NFA complementation has no polynomial state bound.** For
  every $n\ge4$, there is an $n$-state 2NFA whose complement requires
  at least $\tfrac12\,2^{\lfloor(n-4)/127\rfloor}-1$ states
  [S4:38–48].
- **One-way liveness simulation has no polynomial state bound.** Every
  equivalent two-way DFA for $\mathsf{OWL}_h$ requires $s$ states satisfying
  $4(s+2)^2\ge 2^{\lfloor(h-2)/31\rfloor}$ [S8:99–110].
- **The Sakoda–Sipser conjecture is resolved over growing alphabets.**
  MS2 provides the exponential lower bound that the conjecture
  predicted; the alphabet grows with $h$, so the bound is
  alphabet-dependent [S8:99–110].
- **Both results are over the full two-way model.** The model has two
  endmarkers, left, right, and stay moves, and acceptance by a finite
  run [S6:12].
- **The formalization covers all three lower bounds.** The scope note
  formalizes the complementation bound, the determinization bound, and
  the liveness bound [S6:10–14].

## Section skeleton

MS1 [S3] is a 46-line root: a 28-line preamble with package declarations,
title block, abstract [S3:30–36], five section files [S3:37–41], and a
`plain` bibliography [S3:42–45]. The sections, in order and line count:
`introduction` (151), `diagrams` (415), `nesting` (211),
`amplification` (369), `automata` (224) — 1,370 section lines. The
shipped PDF [S5] is the manuscript in the form the release distributes.

MS2 [S7] is a 29-line root: `\input{preamble}` (a 36-line preamble
file), title block, abstract [S7:8–18], five section files [S7:19–23],
and a `plainurl` bibliography [S7:24–28]. The sections, in order and
line count: `introduction` (193), `machines` (335), `matching` (331),
`rank` (353), `separation` (103) — 1,315 section lines. The shipped
PDF [S9] is the manuscript in the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S6:10–14],
**three** comparator stubs, and **three** `main_results` declarations —
the formalization is **complete at the declaration level** for all three
results.

The scope note [S6:10–14] describes two layers of formalized content:
[S6:10] the complementation lower bound for every $n\ge4$ and the
determinization lower bound for every $n\ge131$; [S6:12] the model
(two endmarkers, left/right/stay moves, finite-run acceptance) and the
explicit exclusion of the one-way liveness results from the first scope;
and [S6:14] the liveness family with its exponential lower bound
$2^{\lfloor(h-2)/31\rfloor}\le4(s+2)^2$.

The scope note links **three** comparator configs [S6:20–22]:

- `TwoWayComplementation.lean` [S10:36–40] (45 lines) —
  `complementation_lower_bound_finite` [S10:36–40]: for every $n\ge4$,
  there exists an $n$-state 2NFA whose complement requires at least
  $\tfrac12\,2^{\lfloor(n-4)/127\rfloor}-1$ states; `sorry` at [S10:41].
  Declaration `OAI.TwoWayComplementation.complementation_lower_bound_finite`.
- `TwoWayDeterminization.lean` [S11:58–68] (73 lines) —
  `explicit_family_main` [S11:58–68]: for every $n\ge4$, there exists
  an $n$-state 2NFA such that (i) its complement requires
  $\tfrac12\,2^{\lfloor(n-4)/127\rfloor}-1$ states, and (ii) for
  $n\ge131$, every equivalent deterministic 2NFA requires
  $\tfrac12\,2^{\lfloor(n-4)/127\rfloor}$ states; `sorry` at [S11:69].
  Declaration `OAI.TwoWayComplementation.explicit_family_main`.
- `OneWayLiveness.lean` [S12:95–100] (105 lines) —
  `main_theorem` [S12:95–100]: for every $h\ge2$, there exists an
  $h+3$-state one-way NFA (no left moves) recognizing $\mathsf{OWL}_h$, and
  every equivalent two-way DFA with $s$ states satisfies
  $2^{\lfloor(h-2)/31\rfloor}\le4(s+2)^2$ (or $4(s+1)^2$ under the
  initially-accepting convention); `sorry` at [S12:101].
  Declaration `OAI.OneWayLiveness.main_theorem`.

All three comparators carry `sorry`, but all three have `main_results`
entries, so the challenges are registered as targets the release set
itself with named entry points. The reading is of source text only — no
`lake` or `lean` run elaborates the library, so the claim here is that
the statements and their `sorry` exist in the source, not that the
declarations are proved.

## Coverage

The ledger row `fam=129` [S13] records: `tier=T3`, `paps=2`,
`paps_form=2`, `chal=3`, `mainres=3`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration level**
for all three comparator configs. Both manuscripts are formalized
(`paps_form=2`). The shape flags are `resolution|bound`;
`resolves_named=1` — MS2 resolves the Sakoda–Sipser state-succinctness
conjecture over growing finite alphabets; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3111], manuscript link [S1:3111] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 129 at [S2:335] |
| S3 | [`preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/paper.tex`](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/paper.tex) | 46 | MS1 document root; abstract [S3:30–36]; five section `\input` directives [S3:37–41]; 46 lines |
| S4 | [`preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/sections/introduction.tex`](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/build/sections/introduction.tex) | 151 | MS1 `main:theorem` [S4:38–48]; 151 lines |
| S5 | [`preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf`](../../../preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf) | 11050 | MS1 as shipped |
| S6 | [`lean/docs/129.md`](../../../lean/docs/129.md) | 22 | scope note — Scope at [S6:10–14], comparator links at [S6:20–22] |
| S7 | [`preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/main.tex`](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/main.tex) | 29 | MS2 document root; abstract [S7:8–18]; five section `\input` directives [S7:19–23]; 29 lines |
| S8 | [`preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/sections/introduction.tex`](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/build/sections/introduction.tex) | 193 | MS2 `thm:main` [S8:99–110]; 193 lines |
| S9 | [`preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf`](../../../preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf) | 11621 | MS2 as shipped |
| S10 | [`lean/ComparatorChallenges/TwoWayComplementation.lean`](../../../lean/ComparatorChallenges/TwoWayComplementation.lean) | 45 | comparator — `complementation_lower_bound_finite` [S10:36–40], `sorry` at [S10:41]; 45 lines |
| S11 | [`lean/ComparatorChallenges/TwoWayDeterminization.lean`](../../../lean/ComparatorChallenges/TwoWayDeterminization.lean) | 73 | comparator — `explicit_family_main` [S11:58–68], `sorry` at [S11:69]; 73 lines |
| S12 | [`lean/ComparatorChallenges/OneWayLiveness.lean`](../../../lean/ComparatorChallenges/OneWayLiveness.lean) | 105 | comparator — `main_theorem` [S12:95–100], `sorry` at [S12:101]; 105 lines |
| S13 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=129`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
