[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 134](../index/theoretical-computer-science/134-generalized-star-height-at-most-three.md)

# 134 — Generalized star height at most three

[Index page](../index/theoretical-computer-science/134-generalized-star-height-at-most-three.md)

## Original CONTENTS.md summary

 (family entry):

> **134. Generalized star height at most three.** Every regular language over a finite alphabet has a generalized regular expression with at most three nested Kleene stars, allowing union, concatenation and complement over the same alphabet. This establishes an absolute bound independent of automaton size, resolving the uniform-boundedness version of the generalized star-height problem. (Lean) [S1:3236]

[S2:345] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

A **regular expression** builds a set of strings from letters. The
ordinary operations are **union** (or), **concatenation** (followed by),
and the **Kleene star** (replicate any number of times). The **star
height** of a language is the deepest nesting of stars in an expression
that recognizes it.

A **generalized** regular expression adds one more operation:
**complement** (the strings *not* in the set). The **generalized star
height** $`h_\Sigma(L)`$ of a language $`L`$ over alphabet $`\Sigma`$ is the
smallest star nesting of a *generalized* expression recognizing $`L`$.

Adding complement makes a big difference. Ordinary star height is
**unbounded** — over just two letters there are languages of arbitrarily
high star height. But with complement, the question becomes: is there a
**uniform bound** that works for *every* regular language?

This family answers **yes**: every regular language has generalized
star height **at most three**
[S10:29–35]. The bound is absolute — it does not depend on the
alphabet, the language, or the size of a recognizing automaton.

## Graduate summary

**The bound of thirteen** ([S4:33–39], `thm:main`). "For every finite
alphabet $`\Sigma`$ and every regular language $`L\subseteq\Sigma^*`$,
$`h_\Sigma(L)\le 13`$" [S4:33–39]. This is the first uniform bound,
obtained by a prediction-trial / full-decision-history construction
[S4:44–51]. Its numerical value records the depth of that method.

**The bound of four** ([S7:24–27], `thm:main`). "For every finite
alphabet $`\Sigma`$ and every regular language $`L\subseteq\Sigma^*`$, one
has $`h_\Sigma(L)\le4`$" [S7:24–27]. Proved by a complete construction
over the given alphabet using multiscale periodic transport; the bound
is independent of $`\Sigma`$, $`L`$, and the number of states in a
recognizing automaton [S7:29–34].

**The bound of three** ([S10:29–35], `thm:main`). "For every finite
alphabet $`\Sigma`$ and every regular language $`L\subseteq\Sigma^*`$,
$`h_\Sigma(L)\le3`$" [S10:29–35]. Proved by arbitrary-function shift
tables with a whole-stencil decoder. The expressions use the letters of
$`\Sigma`$ itself; their finite parameters and lengths may depend on the
language, but the *nesting* is bounded [S10:37–40].

**The hierarchy is nested.** Each stronger bound subsumes the weaker
one: three implies four implies thirteen. The scope note makes the
selection explicit — "This is stronger than the bound of thirteen in
the accompanying finite-monoid paper" [S12:11], and "The bound of three
implies the accompanying paper's bound of four" [S12:13].

## History of the conjecture

**Ordinary star height** (without complement) was studied by **Eggan**
(1963), who related it to the cycle structure of transition graphs, and
by **Dejean and Schützenberger** (1966), who showed it is **unbounded**
over a two-letter alphabet [S7:36–39][S10:44–50]. Those lower bounds
do not carry over once complement is added [S4:39–47].

**Generalized star height** was introduced with the same algebraic
characterization as its ordinary counterpart: **Schützenberger** (1965)
showed the height-zero (star-free) languages are exactly those
recognized by *aperiodic* finite monoids [S7:41–43]. Height one then
extends beyond aperiodic: **Henneman** proved every language
recognized by a finite commutative group has height at most one, and
**Pin, Straubing, and Thérien** extended this to finite nilpotent
groups of class two [S7:46–52]. These algebraic results do *not*
supply a uniform bound for arbitrary finite monoids.

The **uniform-boundedness** question — whether some absolute
$`h_\Sigma(L)\le h`$ works for every regular $`L`$ — is the one this family
settles. **Straubing** (2002) distinguished the absolute-boundedness
question from the height-one question [S4:39–42]: a language needing
height greater than one would rule out the bound one, but not a larger
absolute bound. The construction here gives the absolute bound; it does
not determine the *minimum* height of any particular language
[S4:43–45].

**Prior (my training data, not this repo).** The Eggen/Dejean–
Schützenberger unboundedness of ordinary star height and
Schützenberger's aperiodic-monoid characterization of the star-free
languages are standard results in the syntactic-monoid theory of formal
languages. The uniform boundedness of *generalized* star height was a
genuine open question — the release's proof that height three
suffices for all regular languages is the load-bearing claim, and I
cannot independently confirm the specific intermediate bounds (four,
thirteen) as prior results; the release ships the three manuscripts as
proof.

## Consequences

- **A uniform generalized star-height bound exists.** Every regular
  language over a finite alphabet has $`h_\Sigma(L)\le3`$
  [S10:29–35].
- **The bound is absolute.** It is independent of the alphabet, the
  language, and the size of a recognizing automaton [S7:29–32].
- **The bound of three is the sharpest of the three.** Three implies
  four implies thirteen; the selected formalized statement is the
  bound of three [S12:11–13].
- **The minimum height is not determined.** The construction gives an
  upper bound on nesting, not the least nesting for a given language;
  computing that minimum is a separate question [S4:43–45][S10:37–40].
- **The uniform-boundedness problem is resolved.** The family answers
  the absolute-boundedness version of the generalized star-height
  problem affirmatively [S1:3236].

## Section skeleton

Three manuscripts, each shipping a compiled PDF (top-level, with
non-standard names: the two older bound papers ship a PDF named after
the directory; the bound-of-three paper ships `article.pdf`):

**MS1** [S3] — *Finite monoid computations and a uniform
generalized star-height bound*. A 49-line root: preamble, title,
abstract [S3:33–39], eight section files [S3:40–47], a
`references/bibliography` import [S3:48]. Sections, in order and line
count: `introduction` (183), `algebra` (215), `clock` (443),
`geometry` (462), `outer` (375), `aligned` (471), `parameters` (668),
`compilation` (292) — 3,109 section lines. The proof develops the
prediction-trial / decision-history machinery and compiles it into a
height-13 expression; the shipped PDF [S5] is in release form.

**MS2** [S6] — *Generalized star height at most four*. A 70-line root:
preamble, `macros` import [S6:48], abstract [S6:55–60], seven section
files [S6:61–67]. Sections: `01-introduction` (159), `02-algebra`
(277), `03-clock` (246), `04-scales` (618), `05-episodes` (314),
`06-splits` (566), `07-compilation` (269) — 2,449 section lines. The
proof runs a multiscale periodic transport, then splits and compiles
into a height-4 expression; the shipped PDF [S8] is in release form.

**MS3** [S9] — *Generalized star height at most three*. A 29-line root:
`preamble` import [S9:2], title, abstract [S9:8–12], ten section files
[S9:14–23]. Sections: `introduction` (223), `algebra` (332), `clock`
(316), `markers` (130), `schedule` (325), `episodes` (286),
`outer-split` (283), `decoder` (335), `inner-split` (215),
`compilation` (270) — 2,715 section lines. The proof builds
arbitrary-function shift tables and a whole-stencil decoder, compiling
into a height-3 expression; the shipped PDF [S11] is in release form.

## Comparison with the formalized statement

The release formalizes this family at tier T2 with one scope note
[S12:11] and **one** comparator stub, but **no** `main_results`
declaration. This is a structural absence: the scope note links a
comparator config, and that config has no proved declaration in
`lean/OAI/`.

The scope note [S12:11] carries three scope paragraphs, all selecting the
same statement — the uniform bound of three:

- [S12:11]: "The formalization proves that every regular language over
  a finite alphabet has a generalized expression over the same
  alphabet of star height at most three. This is stronger than the
  bound of thirteen in the accompanying finite-monoid paper. The
  selected statement asserts the uniform expression bound, without
  separately encoding every construction step of that paper."
- [S12:13]: "The formalization proves that every regular language over
  a finite alphabet has a generalized regular expression over that
  same alphabet with star height at most three. Generalized
  expressions allow Boolean operations as well as concatenation and
  Kleene star. The bound of three implies the accompanying paper's
  bound of four; the selected statement concerns the expression bound
  itself."
- [S12:15]: "The formalization proves that every regular language over
  a finite alphabet has a generalized regular expression over that
  same alphabet of star height at most three. Complements are taken in
  the same free monoid. This is the paper's uniform bound."

The scope note lists two comparator rows [S12:21–22], but **both** link
the same config [`GeneralizedStarHeight.lean`], so the ledger's
`chal=1` is the deduped distinct-config count. That config has **no**
`main_results` entry, so the formalization stops at the challenge
stub.

The `GeneralizedStarHeight.lean` comparator stub [S13:42–44] (48 lines)
defines the generalized-expression language: an inductive `Expression`
([S13:9–16]) with constructors `zero`, `one`, `letter`, `union`,
`concat`, `compl`, `star`, a `language` interpretation
([S13:22–29]), a `height` function ([S13:31–35]) — `compl` preserves
height and `star` adds one — and the predicate
`HasHeightAtMost L n := ∃ P, P.language = L ∧ P.height ≤ n`
[S13:39–40]. Its single statement is

- `main` [S13:42–43] — for every finite alphabet and every regular
  $`L`$, `HasHeightAtMost L 3`; `sorry` at [S13:44].

There is no `OAI/**` declaration that proves this statement, so the
formalization stops at the challenge stub. The reading is of source
text only — no `lake` or `lean` run elaborates the library, so the
claim here is that the statement and its `sorry` exist in the source,
not that the bound is proved.

## Coverage

The ledger row `fam=134` [S14] records: `tier=T2`, `paps=3`,
`paps_form=0`, `chal=1`, `mainres=0`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **incomplete**: the single scope
note links one comparator config (named twice, deduped to one), but
that config has no `main_results` entry and no proved declaration under
`lean/OAI/` — a T2 structural absence. All three manuscripts are
unformalized (`paps_form=0`). The shape flags are
`resolution|bound|partial|uniform`; `resolves_named=1` — the result
resolves (affirmatively) the uniform-boundedness version of the
generalized star-height problem; `counterex_broad=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3236], manuscript links [S1:3236] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 134 at [S2:345] |
| S3 | [`preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/paper.tex`](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/paper.tex) | 49 | document root; abstract [S3:33–39]; eight section `\input` directives [S3:40–47], bibliography [S3:48]; 49 lines |
| S4 | [`preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/sections/introduction.tex`](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/sections/introduction.tex) | 183 | `thm:main` [S4:33–39] ($h_\Sigma(L)\le13$); 183 lines |
| S5 | [`preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf`](../../../preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf) | 15009 | the manuscript as shipped |
| S6 | [`preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/main.tex`](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/main.tex) | 70 | document root; abstract [S6:55–60]; `macros` import [S6:48], seven section `\input` directives [S6:61–67]; 70 lines |
| S7 | [`preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/sections/01-introduction.tex`](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/sections/01-introduction.tex) | 159 | `thm:main` [S7:24–27] ($h_\Sigma(L)\le4$); 159 lines |
| S8 | [`preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf`](../../../preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf) | 15758 | the manuscript as shipped |
| S9 | [`preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/paper.tex`](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/paper.tex) | 29 | document root; `preamble` import [S9:2], abstract [S9:8–12]; ten section `\input` directives [S9:14–23]; 29 lines |
| S10 | [`preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/sections/introduction.tex`](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/sections/introduction.tex) | 223 | `thm:main` [S10:29–35] ($h_\Sigma(L)\le3$); 223 lines |
| S11 | [`preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf`](../../../preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf) | 16976 | the manuscript as shipped |
| S12 | [`lean/docs/134.md`](../../../lean/docs/134.md) | 22 | scope note — Scope at [S12:9], three scope paragraphs [S12:11,13,15], two comparator links [S12:21–22] |
| S13 | [`lean/ComparatorChallenges/GeneralizedStarHeight.lean`](../../../lean/ComparatorChallenges/GeneralizedStarHeight.lean) | 48 | comparator — `HasHeightAtMost` [S13:39–40], `main` [S13:42–43], `sorry` at [S13:44]; 48 lines |
| S14 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=134`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
