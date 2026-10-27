[Notes](../../README.md) / [Summaries](README.md) / [Theoretical computer science](../index/disciplines/theoretical-computer-science.md) / [Family 132](../index/theoretical-computer-science/132-a-counterexample-to-the-quadratic-sensitivity-conjecture.md)

# 132 — A counterexample to the quadratic sensitivity conjecture

[Index page](../index/theoretical-computer-science/132-a-counterexample-to-the-quadratic-sensitivity-conjecture.md)

## Original CONTENTS.md summary

[S1:3168] (family entry):

> **132. A superquadratic separation of sensitivity and block sensitivity.** Constructs total Boolean functions with block sensitivity $`\mathop{\mathrm{bs}}\nolimits (f)\ge s(f)^\alpha`$ for a fixed α > 2, disproving the quadratic strengthening of the Sensitivity Conjecture. Here $`s(f)`` counts influential individual-bit flips, while block sensitivity allows disjoint groups of bits to change together. ([Lean](../../../lean/docs/132.md))

[S2:341] carries the `\resultentry`, so the release blurb and the overview
agree on the statement.

## Undergraduate summary

For a Boolean function (an input of $n$ bits producing one bit of
output), **sensitivity** $s(f)$ counts the most number of *single bits*
that can be flipped to change the output. **Block sensitivity**
$\mathrm{bs}(f)$ counts the most number of *disjoint groups of bits* that can
each be flipped to change the output.

It was conjectured that block sensitivity is at most a constant power of
sensitivity. The **quadratic strengthening** was the specific guess
$\mathrm{bs}(f)\le s(f)^2$.

This family constructs functions where block sensitivity grows **faster
than $s(f)^2$** [S4:53–64] — in fact faster than $s(f)^\alpha$ for some
$\alpha>2$ — so the quadratic bound is **false**. It is a genuine
**counterexample** to that strengthening.

## Graduate summary

**Main theorem** ([S4:53–64], `thm:main`). "For every real $C>0$, there
are a positive integer $n$ and a nonconstant total Boolean function $f$
such that $\mathrm{bs}(f)>C\,s(f)^2$. More precisely, for every integer $d\ge1$
the construction below gives a nonconstant total Boolean function $f$
with $\mathrm{bs}(f)/s(f)^2\ge 2^d/[4(d+2)^2]$" [S4:53–64]. The ratio
$\mathrm{bs}(f)/s(f)^2$ is unbounded as $d\to\infty$.

**The construction.** The separation is built recursively: a seed
function with block sensitivity exceeding sensitivity squared is
amplified through recurrences that track how $s$ and $\mathrm{bs}$ scale under a
tensor-like product [S4:135]. The recurrences yield the explicit
$2^d/[4(d+2)^2]$ lower bound and, along a subsequence, a fixed exponent
$\alpha>2$ with $\mathrm{bs}(f)\ge s(f)^\alpha$.

**Relationship to the resolved conjecture.** The full *polynomial*
Sensitivity Conjecture ($\mathrm{bs}$ polynomial in $s$) was resolved by **Huang**
in 2019, giving $\mathrm{bs}(f)\le s(f)^4$ via the degree bound and Tal's
refinement, later sharpened by **Wellens** to
$\mathrm{bs}(f)\le\sqrt{2/3}\,s(f)^4+1$ [S4:43–49]. The theorem here does not
contradict that polynomial bound; it only rules out the *quadratic*
strengthening [S4:50–51].

## History of the conjecture

The question goes back to **Nisan's** work on parallel computation, which
introduced block sensitivity and already recorded **Rubinstein's**
quadratic separation [S4:25–27]. **Nisan and Szegedy** studied the problem
through the degree of the unique multilinear real polynomial representing
a Boolean function and explicitly suggested the quadratic inequality
$\mathrm{bs}(f)\le s(f)^2$ [S4:28–30].

**Huang** resolved the polynomial conjecture in 2019. His degree bound,
together with **Tal's** refinement of the degree–block-sensitivity
comparison, gives $\mathrm{bs}(f)\le s(f)^4$ for every total Boolean function.
**Wellens** later improved its leading constant, proving
$\mathrm{bs}(f)\le\sqrt{2/3}\,s(f)^4+1$ [S4:43–49]. These results settle the
polynomial question but leave the quadratic strengthening open — the
theorem below rules it out.

**Prior (my training data, not this repo).** Huang's resolution of the
Sensitivity Conjecture in 2019 was a landmark result. The quadratic
strengthening $\mathrm{bs}(f)\le s(f)^2$ was the natural guess, and the known
upper bound $s(f)^4$ left open how tight the true exponent was. A
superquadratic separation is a clean negative result pinning down that
the square is not the right scale. I cannot confirm the specific prior
results independently; the release ships the manuscript as proof.

## Consequences

- **The quadratic sensitivity bound is false.** There are total Boolean
  functions with $\mathrm{bs}(f)>C\,s(f)^2$ for every constant $C$
  [S4:53–64].
- **The separation is unbounded and explicit.** For every $d\ge1$, the
  constructed function satisfies
  $\mathrm{bs}(f)/s(f)^2\ge 2^d/[4(d+2)^2]$ [S4:53–64].
- **A fixed exponent above 2 is achieved.** Along a subsequence,
  $\mathrm{bs}(f)\ge s(f)^\alpha$ for some $\alpha>2$, with $\mathrm{bs}(f)\to\infty$
  [S6:9].
- **The polynomial bound stands.** This does not contradict Huang's
  $\mathrm{bs}(f)\le s(f)^4$; it only rules out the quadratic strengthening
  [S4:50–51].
- **The question is settled at the quadratic level.** The true exponent
  separating $\mathrm{bs}$ from $s$ lies strictly between 2 and 4 in this sense
  [S4:43–51].

## Section skeleton

The manuscript [S3] is a 39-line root: a 24-line preamble with package
declarations and theorem styles, title block, abstract [S3:26–32], four
section files [S3:33–36], and an `alpha` bibliography [S3:37–38]. The
sections, in order and line count: `00-introduction` (139),
`01-construction` (193), `02-recurrences` (149), `03-separation` (275) —
756 section lines. The proof develops the seed and the recursive
amplification, analyzes the scaling recurrences for $s$ and $\mathrm{bs}$, and
extracts the separation bound. The shipped PDF [S5] is the manuscript in
the form the release distributes.

## Comparison with the formalized statement

The release formalizes this family at tier T3 with one scope note [S6:9],
one comparator stub [S7:30–35], and **one** `main_results` declaration — the
formalization is **complete at the declaration level**.

The scope note [S6:9] states precisely what is formalized: "The formalized
result disproves a universal quadratic bound of block sensitivity by
sensitivity for total Boolean functions. For every integer $d\ge1$, it
constructs a nonconstant function with
$\mathrm{bs}(f)/s(f)^2\ge2^d/(4(d+2)^2)$, making the ratio unbounded.
The formalization also gives a fixed exponent $\alpha>2$ and a sequence
with $s(f)^\alpha\le\mathrm{bs}(f,0)$ while the latter tends to infinity;
here $\mathrm{bs}(f,0)$ is block sensitivity at the all-zero input"
[S6:9].

The scope note links a single comparator config
[`SensitivitySeparation.lean`] [S6:15]. That config carries a
`main_results` entry: declaration
`OAI.Paper320.quantitative_separation` in
`OAI/Combinatorics/Sensitivity/Separation.lean`.

The `SensitivitySeparation.lean` comparator stub [S7:30–35] (42 lines) defines
the sensitivity and block-sensitivity machinery and one statement

- `quantitative_separation` [S7:30–35] — for every $d\ge1$, there is a
  positive $n$ and a nonconstant function $f$ (with
  $f(0^n)=0$) such that
  $2^d/[4(d+2)^2]\le \mathrm{bs}(f)/s(f)^2$; `sorry` at [S7:36].

The comparator still carries a `sorry`, but the declaration
`OAI.Paper320.quantitative_separation` exists in the library's
`main_results` list, so the challenge is registered as a target the
release set itself with a named entry point. The reading is of source
text only — no `lake` or `lean` run elaborates the library, so the claim
here is that the statement and its `sorry` exist in the source, not that
the declaration is proved.

## Coverage

The ledger row `fam=132` [S8] records: `tier=T3`, `paps=1`,
`paps_form=1`, `chal=1`, `mainres=1`, `scope_note=1`, `verification=0`,
`trace=`. The formalization chain is **complete at the declaration level**:
the `SensitivitySeparation.lean` comparator config carries a
`main_results` entry with declaration
`OAI.Paper320.quantitative_separation`. The manuscript is formalized
(`paps_form=1`). The shape flags are empty (no `shapes` tag);
`resolves_named=1` — the result resolves (negatively) the quadratic
strengthening of the Sensitivity Conjecture; `counterex_broad=1` — the
result is a counterexample construction to the quadratic bound.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:3168], manuscript link [S1:3168] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 132 at [S2:341] |
| S3 | [`preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/paper.tex`](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/paper.tex) | 39 | document root; abstract [S3:26–32]; four section `\input` directives [S3:33–36]; 39 lines |
| S4 | [`preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/sections/00-introduction.tex`](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/build/sections/00-introduction.tex) | 139 | `thm:main` [S4:53–64]; 139 lines |
| S5 | [`preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf`](../../../preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026/paper.pdf) | 10331 | the manuscript as shipped |
| S6 | [`lean/docs/132.md`](../../../lean/docs/132.md) | 15 | scope note — Scope at [S6:9], comparator link at [S6:15] |
| S7 | [`lean/ComparatorChallenges/SensitivitySeparation.lean`](../../../lean/ComparatorChallenges/SensitivitySeparation.lean) | 42 | comparator — `quantitative_separation` [S7:30–35], `sorry` at [S7:36]; 42 lines |
| S8 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=132`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |
