[Notes](../../README.md) / [Summaries](README.md) / [Combinatorics](../index/disciplines/combinatorics.md) / [Family 157](../index/combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md)

# 157 — Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures

[Index page](../index/combinatorics/157-counterexamples-to-the-hadwiger-and-colin-de-verdi-ere-conjectures.md)

## Original CONTENTS.md summary

The release's blurb [S1:3743] and the catalog abstract [S2:397] state
the family's combined claim. It **disproves Hadwiger's conjecture even
for fractional coloring**: arbitrarily large finite simple graphs with
independence number at most two satisfy
$`\chi_f(G)>h(G)`$, where $`h(G)`$ is the largest clique-minor order. It
**also disproves the fractional Colin de Verdière chromatic
bound** $`\chi_f(G)\le\mu(G)+1`$. And in the positive direction it
proves that every finite nonempty graph satisfies
$`\chi_{\mathrm{list}}(G)\le C h(G)`$ for a universal constant
$`C`$. Three manuscripts carry the family. The first, *A counterexample
to Hadwiger's conjecture* [S3:3, S3:5], abstract 

> We disprove Hadwiger's conjecture by constructing arbitrarily large
graphs whose chromatic number exceeds their Hadwiger number. The examples
have independence number at most two, and even their ordinary fractional
chromatic number exceeds their Hadwiger number. Thus they also disprove
the fractional-coloring weakening discussed by Reed and Seymour. [S3:9–13]

The second, *A counterexample to the Colin de Verdière
chromatic conjecture* [S4:3, S4:5], abstract [S4:9–13]:

We disprove the Colin de Verdière chromatic conjecture by
constructing graphs whose chromatic number exceeds their Colin de
Verdière invariant by more than one. The examples have
independence number at most two. In fact, their ordinary fractional
chromatic number also exceeds their Colin de Verdière invariant
by more than one [S4:9–13].

The third, *A linear list-coloring bound in terms of the Hadwiger
number* [S5:27, S5:29], abstract [S5:33–36]:

We prove that every finite nonempty graph $`G`$ satisfies
$`\chi_{\mathrm{list}}(G)\le C h(G)`$ for an absolute integer $`C`$,
where $`h(G)`$ is the largest order of a clique minor. This resolves the
Linear List Hadwiger conjecture affirmatively [S5:33–36].

## Undergraduate summary

Graph coloring asks for the fewest colors so that no two adjacent
vertices share a color; the minimum is the *chromatic number*
$`\chi(G)`$. Hadwiger's conjecture links this to a structural
obstruction: a graph's *Hadwiger number* $`h(G)`$ is the size of the
largest complete-graph minor it contains (a minor you get by deleting
edges/vertices and shrinking edges), and the conjecture says
$`\chi(G)\le h(G)`$ — a graph can never need more colors than the
size of its largest complete minor. A *minor* is a graph obtained by
deleting things and fusing edges, so it is a coarser shadow of the
original. The Colin de Verdière invariant $`\mu(G)`$ is another
graph invariant (defined via the nullity of matrices associated to
$`G`$) that is also expected to bound chromatic number. The *fractional
chromatic number* $`\chi_f(G)`$ is a relaxed version of $`\chi(G)`$ that
allows fractional color assignments; it is always at least as large a
lower bound as the naive one. This family shows **both** conjectures
fail: it builds graphs where the chromatic (and fractional
chromatic) number exceeds $`h(G)`$, and where it exceeds
$`\mu(G)+1`$ — all from graphs whose independence number is at
most two (so the graphs are dense, no large set of mutually
non-adjacent vertices) [S3:9–13, S4:9–13, S5:33–36].

## Graduate summary

**The Hadwiger counterexample** [S3:9–13]. There are arbitrarily
large finite simple graphs $`G`$ with independence number $`\alpha(G)
\le2`$ such that the *ordinary fractional* chromatic number
$`\chi_f(G)`$ exceeds the Hadwiger number $`h(G)`$; in particular the
ordinary chromatic number
$`\chi(G)\ge\chi_f(G)>h(G)`$. This disproves Hadwiger's conjecture in
its strongest (fractional) form, and hence in the ordinary one, and
also rules out the fractional-coloring weakening discussed by Reed and
Seymour [S3:9–13, S6:10–12].

**The Colin de Verdière counterexample** [S4:9–13]. There
are finite simple graphs with independence number at most two whose
chromatic number exceeds the Colin de Verdière invariant
$`\mu(G)`$ **by more than one**; in fact their ordinary fractional
chromatic number also exceeds $`\mu(G)+1`$. This is a strict disproof
of the fractional bound $`\chi_f(G)\le\mu(G)+1`$
[S4:9–13, S2:397].

**The positive list-coloring bound** [S5:33–36]. There is an
absolute integer $`C\ge1`$ — independent of the graph — such
that every finite nonempty simple graph $`G`$ satisfies
$`\chi_{\mathrm{list}}(G)\le C h(G)`$, where
$`\chi_{\mathrm{list}}`$ is the list chromatic number (choosability):
the worst case over all assignments of a list of colors to each
vertex. This resolves the Linear List Hadwiger conjecture
affirmatively [S5:33–36, S6:14].

**The scope of the formalization.** The registered statement is the
**ordinary chromatic** Hadwiger counterexample, not the fractional
one: the scope note is explicit that the paper's fractional-chromatic
strengthening and the Colin de Verdière consequence lie
**outside** the selected statement
[S6:10–12, S6:14, S6:20–21].

## History of the conjecture

Hadwiger's conjecture (1943) is one of the central open problems in
graph theory, a chromatic analogue of the graph-minor structure
program; it was proved for small Hadwiger numbers and for special
graph classes. The Colin de Verdière invariant (mid-1980s) was
proposed as another chromatic upper bound and has been verified for
planar and other graph families. The Linear List Hadwiger question
asks whether list chromatic number is linearly bounded by the
Hadwiger number — a positive answer has long been expected, and
the negative counterexample line (disproving the chromatic and
Colin de Verdière bounds in the fractional form simultaneously)
is the family's counterexample content, while the universal linear
list bound is its positive content
[S3:9–13, S4:9–13, S5:33–36].

**Prior (my training data, not this repo).** I know Hadwiger's
conjecture, the Colin de Verdière invariant, and that both are
expected chromatic upper bounds proven only in special cases. Concrete
counterexamples to **both** — in the fractional form, on graphs
of independence number at most two — together with an
affirmative universal **linear** list-coloring bound
$`\chi_{\mathrm{list}}(G)\le C h(G)`$, go beyond the specific
constructions I recall; I cannot independently verify the graph
families or the constant $`C`$ from training alone.

## Consequences

**Hadwiger's conjecture is false, fractionally.** Arbitrarily large
finite simple graphs with independence number at most two have
$`\chi_f(G)>h(G)`$, and hence $`\chi(G)>h(G)`$
[S3:9–13, S6:10–12].

**The Colin de Verdière bound is false, fractionally.** Graphs
with independence number at most two have
$`\chi_f(G)>\mu(G)+1`$ [S4:9–13, S2:397].

**A universal linear list-coloring bound.** Every finite nonempty
graph satisfies $`\chi_{\mathrm{list}}(G)\le C h(G)`$ for an
absolute $`C`$, resolving the Linear List Hadwiger conjecture
[S5:33–36, S6:14].

**The failures are on dense, low-independence graphs.** Both
counterexamples are built on graphs with independence number at most
two [S3:9–13, S4:9–13].

## Section skeleton

Three manuscripts. Manuscript 1 [S3:9–13] (title [S3:3], date [S3:5])
— `main.tex` (41 lines) under `build/`. Manuscript 2 [S4] (title
[S4:3], date [S4:5]) — `main.tex` (38 lines) under `build/`.
Manuscript 3 [S5] (title [S5:27], date [S5:29]) — `main.tex`
(48 lines) under `build/`. The family ships no `verification/`
bundle.

## Comparison with the formalized statement

**Scope note** [S6:10–12, S6:14]. The formalization
constructs arbitrarily large finite simple counterexamples to
Hadwiger's conjecture with independence number at most two: for a
graph on $`m`$ vertices it proves
$`h(G)<26m/75+2/3<m/2\le\chi(G)`$, which disproves the **ordinary
chromatic** form. The scope note is explicit that the paper's
fractional-chromatic strengthening and the Colin de Verdière
consequence are **outside** this selected statement
[S6:10–12]. Separately, it proves the positive Linear List
Hadwiger bound: a single integer $`C\ge1`$ with
$`\chi_{\mathrm{list}}(G)\le C h(G)`$ for every finite nonempty
simple graph, the constant independent of the graph [S6:14]. The
scope note names two comparators [S6:20–21]:
`ListHadwiger.lean` and `HadwigerCounterexample.lean`.

**The registration.** The family is at tier T3: the ledger row
records `mainres 1` and `paps_form 1`. `formalization.yaml` registers
one `main_results` entry — the
`OAI.HadwigerCounterexample.not_hadwiger_conjecture` declaration at
`OAI/Combinatorics/HadwigerCounterexample/Main.lean` — and the
manuscript is in its `sources:` listing. The registered declaration is
the **ordinary chromatic** counterexample; the `ListHadwiger.lean`
comparator (the positive list-coloring bound) is a scope-note link
but carries no `main_results` entry of its own.

**What the proof does.** The registered `not_hadwiger_conjecture`
states
$`\neg\bigl(\forall m\,(\forall G\colon\mathrm{SimpleGraph\
(Fin\ m)},\ \chi(G)\le h(G))\bigr)`$, i.e. no universal
chromatic-above-Hadwiger bound exists. The OAI tree proves it with a
genuine Lean proof: it invokes the explicit
`exists_counterexamples` construction to exhibit a concrete
counterexample graph and discharges the universal statement by
contradiction 

```lean
theorem not_hadwiger_conjecture : ¬ (∀ (m:ℕ)(G:SimpleGraph (Fin m)), G.chromaticNumber ≤ ↑(hadwigerNumber G)) := by
  intro h; obtain ⟨m,hM,G,h1,h2,h3,h4,h5,h6,he,hC⟩:=exists_counterexamples 0
  have ht:=h m G; rw [hC] at ht
  exact h6.not_ge (by exact_mod_cast ht)
```
[S9:120–123]

The proof is not a `sorry`: `exact h6.not_ge (by exact_mod_cast
ht)` closes the goal from the lower-bound conjunct `h6` of the
constructed example [S9:123].

**What the OAI tree does carry.** The
`OAI/Combinatorics/HadwigerCounterexample` package (276 files over
38,704 lines, zero `sorry`) carries the supporting definitions
(`hadwigerNumber`, `HasCliqueMinor`, the `AnalyticParameters`
construction, `exists_graphs`, `exists_counterexamples`, the
`eventual_conflict_lower_bound`) that `not_hadwiger_conjecture`
assembles [S9:120–123].

**The comparator stubs.** The registered
`HadwigerCounterexample.lean` comparator restates
`not_hadwiger_conjecture` with a bare `sorry` body


```lean
theorem not_hadwiger_conjecture :
    ¬ (∀ (m : ℕ) (G : SimpleGraph (Fin m)),
      G.chromaticNumber ≤ ↑(hadwigerNumber G)) := by
  sorry
```
[S7:49–52]

The `ListHadwiger.lean` comparator (the positive bound) restates
`MainStatement` —
$`\exists C\ge1\ \forall G\,
\chi_{\mathrm{list}}(G)\le C h(G)`$ — with a bare `sorry`
body [S8:26–28, S8:30–31]. The release records
`scope: "Partial progress."` and `review: status: unchecked`; the
comparators' `sorry` bodies are the targets the release set itself,
and the proved `not_hadwiger_conjecture` in the OAI tree is the
registered result.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 157 at [S1:3743] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{157} at [S2:397] |
| S3 | [`preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/main.tex`](../../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/main.tex) | 41 | manuscript 1 (Hadwiger counterexample): title [S3:3], date [S3:5], abstract [S3:9–13] |
| S4 | [`preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/build/main.tex`](../../../preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/build/main.tex) | 38 | manuscript 2 (Colin de Verdière counterexample): title [S4:3], date [S4:5], abstract [S4:9–13] |
| S5 | [`preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/build/main.tex`](../../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/build/main.tex) | 48 | manuscript 3 (linear list-coloring bound): title [S5:27], date [S5:29], abstract [S5:33–36] |
| S6 | [`lean/docs/157.md`](../../../lean/docs/157.md) | 21 | the formalization scope note: the Hadwiger scope paragraph [S6:10–12], the list-coloring paragraph [S6:14], and the comparator table [S6:20–21] |
| S7 | [`lean/ComparatorChallenges/HadwigerCounterexample.lean`](../../../lean/ComparatorChallenges/HadwigerCounterexample.lean) | 56 | the registered comparator stub: the `not_hadwiger_conjecture` theorem [S7:49–51] and the `sorry` [S7:52] |
| S8 | [`lean/ComparatorChallenges/ListHadwiger.lean`](../../../lean/ComparatorChallenges/ListHadwiger.lean) | 35 | the unregistered comparator stub: `MainStatement` [S8:26–28], the `main_theorem` [S8:30], and the `sorry` [S8:31] |
| S9 | [`lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean`](../../../lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean) | 128 | the registered declaration in the OAI tree: the real proof of `not_hadwiger_conjecture` [S9:120–123] |
