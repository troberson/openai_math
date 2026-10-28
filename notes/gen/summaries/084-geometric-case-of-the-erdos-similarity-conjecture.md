[Notes](../../README.md) / [Summaries](README.md) / [Real and complex analysis](../index/disciplines/real-and-complex-analysis.md) / [Family 084](../index/real-and-complex-analysis/084-geometric-case-of-the-erdos-similarity-conjecture.md)

# 084 — The geometric case of the Erdős similarity conjecture

[Index page](../index/real-and-complex-analysis/084-geometric-case-of-the-erdos-similarity-conjecture.md)

## Original CONTENTS.md summary

The release's blurb [S1:2079] and the catalog abstract [S2:242] state
the family's claim: for every fixed $q\in(0,1)$, a compact subset of
$[0,1]$ of arbitrarily close to full measure that contains no translated,
nontrivially dilated copy of $\{q^n:n\ge1\}$, with dilations of either
sign — the geometric-progression case of the Erd\H{o}s similarity
conjecture. The family ships two manuscripts: the general-ratio (geometric)
statement [S5:34–42] and the dyadic subcase it subsumes
. The geometric manuscript's abstract 

> We prove the geometric-progression case of the Erdős similarity
conjecture. For every fixed $q\in(0,1)$ and every $\eta\in(0,1)$, we
construct a compact set $E_{q,\eta}\subseteq[0,1]$ of measure greater
than $1-\eta$ containing no nontrivial affine copy of
$\{q^n:n\ge1\}$, for any translation and either sign of nonzero dilation.
The set may depend on $q$; the result makes no simultaneous assertion
for different ratios. [S5:34–42]

## Undergraduate summary

Erd\H{o}s's similarity conjecture asks whether any infinite set
$A\subseteq\mathbb R$ is *measure universal* — that is, whether every
set of positive Lebesgue measure contains a translated, dilated copy
$x+sA$ of $A$. The conjecture says no infinite set is. Finite patterns
always are universal, by a simple $L^1$ continuity argument [S4:13–17],
so the question is genuinely about infinite sets.

The dyadic sequence $D=\{2^{-n}:n\ge1\}$ [S4:19–22] and its
one-parameter generalization, the geometric progression
$G_q=\{q^n:n\ge1\}$ [S6:11–15], are the natural infinite
candidates. The two manuscripts prove two nested statements: the dyadic
case [S4:24–33] — no positive-measure set contains a signed
affine copy of $D$ — and the full geometric case [S6:17–24]
— the same, for every ratio $q\in(0,1)$. The dyadic case is exactly
the $q=1/2$ instance of the geometric one [S6:26–30].

The construction is probabilistic at its core: it builds an open set of
arbitrarily small density that meets every scaled copy of the target
sequence, then takes the complement. The complement is the avoiding set
— large in measure, yet containing no copy of the sequence.

## Graduate summary

**The two statements.** The geometric-case manuscript proves


> **Theorem 1.1**
For every $q\in(0,1)$ and $\eta\in(0,1)$, there is a compact set
$E_{q,\eta}\subseteq[0,1]$ with $m(E_{q,\eta})>1-\eta$ such that
$$\text{for every }x\in\mathbb R\text{ and }s\in\mathbb R\setminus\{0\},
 \quad x+sq^n\notin E_{q,\eta}\text{ for some integer }n\ge1.$$ [S6:17–24]

The set $E_{q,\eta}$ may depend on $q$; the statement makes no
simultaneous assertion over different ratios [S5:40–41]. The
dyadic-case manuscript proves the $q=1/2$ instance 

> **theorem**
For every $\eta\in(0,1)$, there is a compact set $E_\eta\subseteq[0,1]$
with $m(E_\eta)>1-\eta$ such that
$$\text{for every }x\in\mathbb R\text{ and every }s\in\mathbb R\setminus\{0\},
 \quad x+sD\nsubseteq E_\eta.$$
Equivalently, for every such $x,s$ there is an integer $n\ge1$ with
$x+s2^{-n}\notin E_\eta$. [S4:24–33]

**The proof mechanism** [S6:34–50]. Both papers construct the open
complement of the avoiding set. The intermediate goal is an open,
$1$-periodic set of arbitrarily small density meeting $x+tG_q$ for every
$x\in\mathbb R$ and every $t\in[1,2]$; a summable union of its dilations
and reflections then covers every nonzero scale. The difficulty is
controlling all scales at once: the random cell tests are arranged on a
finite ordered tree so that each group of tests uses only the grids on one
edge and its child subtree, keeping the per-group scale count bounded, while
other parts of the tree may use finer grids for free. Each point is routed to
a leaf by independent binary tables.

**The relationship between the two.** The geometric case subsumes the dyadic
case (take $q=1/2$) [S6:26–30]. The dyadic paper was written first
(September 25) and the geometric paper (October 5) extends it to arbitrary
ratios. The formalization, however, covers only the dyadic case — see
the formalized section.

## History of the conjecture

Erd\H{o}s posed the similarity conjecture as Problem 4.33.7$^\ast$ in his
1974 problem collection [S4:9–12]. The pre-existing results concern
slowly decreasing sequences: Falconer and Eigen proved nonuniversality for
positive sequences $a_n\downarrow0$ with $a_{n+1}/a_n\to1$, and Humke
and Laczkovich gave a finite hitting-set characterization with further
relative-gap criteria [S4:43–49]. Kolountzakis's finite-gap criterion
and Chleb\'ik's translation-invariant formulation cover sequences with
appropriate gap structure [S4:50–55]. The dyadic sequence satisfies
neither the slow-decreasing nor the finite-gap condition: for $n\ge2$
dyadic points the normalized minimum gap is at most
$2^{-(n-3)}$ [S4:56–59].

Additive-structure results give a separate line. Bourgain proved a sum of
three infinite sets is nonuniversal, and Kolountzakis treated sums of two
copies of certain sequences, including $D+D$ [S4:61–64]. The single
dyadic sequence is distinct from these sumset results — avoiding a
larger pattern does not imply avoiding a subset of it
[S4:71–72].

**Prior (my training data, not this repo).** The Erd\H{o}s similarity
conjecture and the nonuniversality of specific infinite sets are
well-studied in harmonic analysis and additive combinatorics. I know the
Falconer, Eigen, Humke–Laczkovich, Kolountzakis, and Chleb\'ik
results for slowly decreasing sequences. A compact near-full-measure set
avoiding every signed affine copy of the dyadic sequence — or of a
general geometric progression — is, to my knowledge, not established
in the literature I was trained on. I cannot independently verify these
2026 manuscripts' arguments.

## Consequences

**Geometric-progression case resolved.** For every fixed $q\in(0,1)$ and
$\eta\in(0,1)$, a compact set of measure $>1-\eta$ avoids every
translated, nontrivially dilated copy of $\{q^n:n\ge1\}$, for both
dilation signs [S6:17–24].

**Dyadic case resolved.** The $q=1/2$ instance: a compact
near-full-measure set avoids every signed affine copy of
$\{2^{-n}:n\ge1\}$ [S4:24–33].

**Scope of the conjecture.** These are specific infinite patterns; the
conjecture for arbitrary infinite sets is not addressed by either
manuscript [S4:35–39].

## Section skeleton

Two manuscripts, a dyadic $\to$ geometric extension:

- **dyadic** `The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026`
  — root `build/paper.tex` [S3:36–42] (title [S3:31], date [S3:33]), eight
  sections under `build/sections/` (introduction [S4:24–33], periodic, windows,
  routing, tests, scales, repair, global), two figures (`figures/routing.tex`,
  `figures/windows.tex`), and a 14-entry `references.bib` [S10].
- **geometric** `The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026`
  — root `build/main.tex` [S5:34–42] (title [S5:29], date [S5:31]), six
  files under `build/sections/` (01-introduction [S6:17–24], 01-history,
  02-periodic, 03-windows, 04-routing, 05-scales), one figure
  (`figures/window-block.tex`), and a `references.bib`.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S7]. The formalization proves the **dyadic** case of the
Erd\H{o}s similarity conjecture: for every $0<\eta<1$, a compact set
$E\subset[0,1]$ of measure greater than $1-\eta$ containing no affine
copy of $\{2^{-n}:n\ge1\}$, both dilation signs. The scope note links
only the dyadic manuscript. It records `scope: "Partial progress."` and
`review: status: unchecked`; zero `sorry` in the Lean source is not a
comparator pass, and the library has not been built here.

**Two structural gaps.** First, the formalization proves the dyadic
subcase, not the family's headline geometric-progression claim: the family
is named for the general-ratio statement [S5:34–42], but the Lean
work covers only $q=1/2$. Second, the work is unregistered:
`formalization.yaml` carries **no `main_results` entry** for this family,
and the ledger records `paps_form 0` and `mainres 0`. This is a T2
structural absence.

**The comparator stub** [S8:12–18] carries the target with a `sorry`


```lean
theorem dyadic_affine_avoidance :
    ∀ η : ℝ, 0 < η → η < 1 → ∃ E : Set ℝ,
      E ⊆ Set.Icc (0 : ℝ) 1 ∧ IsCompact E ∧
      MeasureTheory.volume E > ENNReal.ofReal (1 - η) ∧
      ∀ x s : ℝ, s ≠ 0 → ∃ n : ℕ, 1 ≤ n ∧
        x + s * dyadicPoint n ∉ E := by
  sorry
```
[S8:12–18]

**The OAI tree is present and proves the dyadic statement, but
unregistered.** The OAI `DyadicAvoidance/` tree **exists** (75 `.lean`
files over 8,456 lines with zero `sorry`) and **proves**
`dyadic_affine_avoidance` at `Main.lean:103` 

```lean
theorem dyadic_affine_avoidance :
    ∀ η : ℝ, 0 < η → η < 1 → ∃ E : Set ℝ, E ⊆ Set.Icc (0 : ℝ) 1 ∧ IsCompact E ∧ MeasureTheory.volume E > ENNReal.ofReal (1 - η) ∧ ∀ x s : ℝ, s ≠ 0 → ∃ n : ℕ, 1 ≤ n ∧ x + s * dyadicPoint n ∉ E := by
  exact Problem310Support.avoidance_of_periodic_hitting periodic_hitting_set
```
[S9:103–105]

The proof closes as a single application of
`Problem310Support.avoidance_of_periodic_hitting`, applied to the
`periodic_hitting_set` theorem at `Main.lean:81`. The absence from
`main_results` means the release does not register this formalization in
its checking workflow.

## Coverage

T2: the family carries a scope note and one comparator challenge but no
`main_results` entry. The ledger row `fam=084` records `paps 2`,
`paps_form 0`, `tier T2`, `chal 1`, `mainres 0`, `scope_note 1`,
`verification 0`, `trace` empty, `shapes resolution|uniform`, `resolves_named 1`,
`summary 1`. The family ships two LaTeX manuscripts (the dyadic and the
geometric case), a scope note, and one comparator challenge with one
`sorry` theorem; a 75-file OAI Lean tree with zero `sorry` exists and
proves the dyadic statement, but the geometric-progression headline claim
is not formalized and the work is not registered in `main_results`. The
family ships no verification bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 084 at [S1:2079] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry for 084 at [S2:242] |
| S3 | [`preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/build/paper.tex`](../../../preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/build/paper.tex) | 54 | dyadic manuscript root; title [S3:31], date [S3:33], abstract [S3:36–42] |
| S4 | [`preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/build/sections/introduction.tex`](../../../preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/build/sections/introduction.tex) | 169 | dyadic introduction; the finite-pattern argument [S4:13–17], the dyadic set [S4:19–22], the main theorem [S4:24–33], the scope-of-theory note [S4:35–39], the related slow-decreasing and additive results [S4:43–72] |
| S5 | [`preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/main.tex`](../../../preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/main.tex) | 53 | geometric manuscript root; title [S5:29], date [S5:31], abstract [S5:34–42] |
| S6 | [`preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/sections/01-introduction.tex`](../../../preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/build/sections/01-introduction.tex) | 91 | geometric introduction; the geometric set [S6:11–15], the main theorem [S6:17–24], the dyadic-subcase remark [S6:26–30], the proof mechanism [S6:34–50] |
| S7 | [`lean/docs/084.md`](../../../lean/docs/084.md) | 15 | the formalization scope note: the dyadic case only, linking the dyadic manuscript |
| S8 | [`lean/ComparatorChallenges/DyadicAvoidance.lean`](../../../lean/ComparatorChallenges/DyadicAvoidance.lean) | 24 | comparator stub: the `dyadic_affine_avoidance` target with a `sorry` [S8:12–18] |
| S9 | [`lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean`](../../../lean/OAI/MeasureTheory/DyadicAvoidance/Main.lean) | 111 | the OAI proved entry point `dyadic_affine_avoidance` [S9:103–105] |
| S10 | [`preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/build/references.bib`](../../../preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/build/references.bib) | 150 | 14-entry BibTeX bibliography of the dyadic manuscript |

## Bibliography

- Bourgain, Jean, Construction of sets of positive measure not containing an affine image of a given infinite structure (1987)
- Chlebík, Miroslav, On the Erdős similarity problem (2015)
- Cruz, Angel D., Lai, Chun-Kit, Pramanik, Malabika, Large Sets Avoiding Affine Copies of Infinite Sequences (2023)
- Cruz, Angel, Lai, Chun-Kit, Pramanik, Malabika, A proof of the Erdős similarity conjecture (2020)
- Mora Cuellar, N., Iosevich, A., Kulkarni, N., Rojas Aravena, I., Yavicoli, A., The Erdős Similarity Conjecture for Two-Fold Sumsets with a Geometric Summand (2026)
- Eigen, S. J., Putting convergent sequences into measurable sets (1985)
- Erdős, Paul, Problems (1974)
- Falconer, K. J., On a problem of Erdős on sequences and measurable sets (1984)
- Feng, De-Jun, Lai, Chun-Kit, Xiong, Ying, Erdős Similarity Problem via Bi-Lipschitz Embedding (2024)
- Humke, Paul D., Laczkovich, Miklós, A visit to the Erdős problem (1998)
- Iosevich, A., Kulkarni, N., Mora Cuéllar, N., Rojas Aravena, I., Yavicoli, A., The Erdős similarity conjecture and Rajchman measures (2026)
- Kolountzakis, Mihail N., Papageorgiou, Effie, Large sets containing no copies of a given infinite sequence (2025)
- Kolountzakis, Mihail N., Infinite patterns that can be avoided by measure (1997)
- Solymosi, David, Patterns in sparse sets (2011)
