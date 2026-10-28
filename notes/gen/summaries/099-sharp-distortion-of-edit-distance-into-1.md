[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 099](../index/convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md)

# 099 — The sharp distortion of edit distance into $\ell_1$

[Index page](../index/convex-and-metric-geometry/099-sharp-distortion-of-edit-distance-into-1.md)

## Original CONTENTS.md summary

The release's blurb [S1:2418] and the catalog abstract [S2:274] state
the family's claim: the least $\ell_1$ distortion of unit-cost edit
distance on words of length at most $d$ is
$\exp(\Theta(\sqrt{\log d\,\log\log d}))$, uniformly over
finite alphabets with at least two symbols, with binary words alone
forcing the lower bound. The headline manuscript's abstract


> We determine the exponential scale of the least $\ell_1$ distortion of
unit-cost edit distance on all strings of length at most $d$. For every
sufficiently large $d$, uniformly over finite alphabets of size at least
two, the distortion lies between
$\exp(c\sqrt{\log d\,\log\log d})$ and
$\exp(C\sqrt{\log d\,\log\log d})$ for absolute constants $c,C>0$.
The lower bound already holds on binary strings of one common length.
Thus the order of logarithmic distortion is sharp up to absolute constants. [S3:42–49]

The family ships three manuscripts.

## Undergraduate summary

*Edit distance* between two words is the cheapest sequence of
insertions, deletions, and substitutions (unit cost each) that turns
one word into the other. A metric *embedding* of words into
$\ell_1$ is a map $f$ preserving distances up to a factor: distances
are stretched by at most the *distortion* $D$. The family determines
how large $D$ must be, as a function of the word-length cap $d$.

The answer is an exponential in $\sqrt{\log d\,\log\log d}$: the
distortion is at least
$\exp(c\sqrt{\log d\,\log\log d})$ for some absolute $c>0$
[S4:42–50, S5:45–51] and at most
$\exp(C\sqrt{\log d\,\log\log d})$ for some absolute $C>0$
[S3:42–49]. Both bounds use words of one common length, and the
lower bound works on binary words alone, so the exponent
$\Theta(\sqrt{\log d\,\log\log d})$ is sharp up to absolute
constants.

## Graduate summary

**The headline determination** [S3:42–49]. For every
sufficiently large $d$, uniformly over finite alphabets of size at
least two, the least $\ell_1$ distortion $E(d)$ of unit-cost edit
distance on strings of length at most $d$ satisfies
$\exp(c\sqrt{\log d\,\log\log d})\le E(d)\le
\exp(C\sqrt{\log d\,\log\log d})$ for absolute $c,C>0$
[S3:42–49]. The lower bound has a witness of binary strings of
one common length [S3:48].

**The finite-circle obstructions** [S4:42–50]. Two independent
constructions of binary strings whose least $\ell_1$ distortion is
$\exp(\Omega(\sqrt{\log d\,\log\log d}))$, plus two direct
binary coding transfers with absolute distortion and logarithmic block
width [S4:46–47]. The manuscript also develops the
Ostrovsky–Rabani overlapping-substring method into a complete
finite histogram embedding at the same exponential scale, uniformly
over finite alphabets and all words of length at most $d$, including the
empty word [S4:47–50].

**The tree constructions** [S5:45–51]. Two independent
constructions of binary words of one length at most $d$ whose ordinary
edit-distance metrics require
$\exp(\Omega(\sqrt{\log d\,\log\log d}))$ $\ell_1$
distortion [S5:45–47], plus a constant-distortion binary
conversion for one prescribed input length [S5:48–49].

## History of the conjecture

Edit distance is the classical string-edit metric. The question of
how well it embeds into $\ell_1$ was open at the exponential scale:
neither the lower bound (binary obstructions) nor the upper bound
(histogram embedding) was known to the author at this precision before
these three manuscripts. The family closes the gap to absolute
constants in the exponent.

**Prior (my training data, not this repo).** I know edit distance as a
metric and that its $\ell_1$ distortion grows with word length, and I
know the Ostrovsky–Rabani histogram-embedding idea for edit
distance in $\ell_1$. The sharpness of the exponent
$\Theta(\sqrt{\log d\,\log\log d})$ — matching lower and
upper, uniform over alphabets, with the lower bound binary — is,
to my knowledge, not established in the literature I was trained on. I
cannot independently verify these three manuscripts' arguments.

## Consequences

**Sharp exponential scale.** The least $\ell_1$ distortion of
unit-cost edit distance on words of length at most $d$ is
$\exp(\Theta(\sqrt{\log d\,\log\log d}))$
[S3:42–49, S4:42–50, S5:45–51].

**Binary suffices for the lower bound.** The lower exponent is
already forced by binary words of one common length, so alphabet size
does not weaken the obstruction [S3:48, S5:45–47].

**A uniform upper embedding.** A finite histogram embedding achieves
the matching upper scale for all finite alphabets and all words of
length at most $d$, including the empty word [S4:47–50].

## Section skeleton

Three manuscripts:

- **headline** [S3:42–49] (title [S3:35], date [S3:38]) — a 58-line
  `main.tex` under `build/` plus five `sections/` files
  (introduction, displacement, construction, binary, upper) and a
  `thebibliography` block in `bibliography.tex`; 7 `.tex` files, 1,101
  lines.
- **finite circles** [S4:42–50] (title [S4:34], date [S4:37]) — a
  62-line `main.tex` under `build/` plus eight `sections/` files
  (introduction, preliminaries, masks, coding, mask-binary, excluded,
  assembly, upper) and a `thebibliography` block in `bibliography.tex`;
  12 `.tex` files, 2,403 lines.
- **tree constructions** [S5:45–51] (title [S5:38], date [S5:41]) — a
  64-line `main.tex` under `build/` plus six `sections/` files
  (introduction, preliminaries, finite-tree, torus-construction,
  torus-obstruction, consequences, polynomial-code) and a
  `thebibliography` block in `references.tex`; 10 `.tex` files, 1,751
  lines.

No manuscript ships a `verification/` bundle.

## Comparison with the formalized statement

**Scope note** [S6:11]. The formalized result determines the
exponential scale of the least $\ell_1$ distortion of unit-cost edit
distance on strings of length at most $d$: for every sufficiently
large $d$, uniformly over finite alphabets with at least two symbols,
the distortion lies between
$\exp(c\sqrt{\log d\,\log\log d})$ and
$\exp(C\sqrt{\log d\,\log\log d})$ for absolute $c,C>0$. The
lower bound has a witness of binary strings of one common length, and
the same scale controls the supremum over finite alphabets [S6:11].
The scope note **excludes** the binary conversion and the companion
upper embedding theorem [S6:19]. It names four comparators
[S6:23–28].

**The structural absence.** The family is at tier T2: the ledger row
records `mainres 0` and `paps_form 0`. `formalization.yaml` carries no
`main_results` entry naming any comparator theorem for this family,
and none of the three manuscripts appears in its `sources:` listing.
The scope note and four comparator stubs exist, but the release has not
registered a single declaration as a family result. The comparator
`EditDistance.lean` carries the headline claim as a `sorry`-terminated
theorem 

```lean
theorem edit_distance_main : EditDistortion.MainClaim.{u} := by
  sorry
```
[S7:67–68]

**What the OAI tree does carry.** Under the tree's
`OAI/Combinatorics/` directory there are four substantial packages
matching the four comparators: `EditDistance` (45 files, 6,275 lines),
`FiniteCircle` (36 files, 9,787 lines), `BinaryEdit` (82 files,
10,207 lines), and `TreeEdit` (30 files, 6,334 lines) — 193 files
over 32,603 lines, zero `sorry`. A `main_results` registration would
link the scope note's four comparators to declarations in these
packages, but none is registered. The release records
`scope: "Partial progress."` and `review: status: unchecked`; zero
`sorry` in the Lean source is not a comparator pass, and the library
has not been built here.

## Coverage

T2: the family is structurally unformalized in the release's own
record. The ledger row `fam=099` records `paps 3`, `paps_form 0`,
`tier T2`, `chal 4`, `mainres 0`, `scope_note 1`, `verification 0`,
`trace` empty, `shapes bound|partial|uniform`, `resolves_named 0`,
`summary 1`. The family ships three LaTeX manuscripts (1,101 + 2,403 +
1,751 lines), a scope note naming four comparators, and four
`sorry`-terminated comparator stubs. The OAI tree carries four
unregistered formalization packages (193 files over 32,603 lines,
zero `sorry`) matching the four comparators, but no `main_results`
entry links them and none of the three manuscripts is in
`formalization.yaml`'s `sources:`. The family ships no verification
bundle and no reasoning trace.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 099 at [S1:2418] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{099} at [S2:274] |
| S3 | [`preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/build/main.tex`](../../../preprints/Edit-Distance-in-l1-Matching-Bounds-up-to-Constants-in-the-Exponent-September-27-2026/build/main.tex) | 58 | headline manuscript root; title [S3:35], date [S3:38], abstract [S3:42–49] |
| S4 | [`preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/build/main.tex`](../../../preprints/Finite-Circle-Obstructions-Binary-Codes-and-Histogram-Embeddings-for-Edit-Distance-September-27-2026/build/main.tex) | 62 | companion manuscript root (finite circles); title [S4:34], date [S4:37], abstract [S4:42–50] |
| S5 | [`preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/build/main.tex`](../../../preprints/Tree-Constructions-for-the-l1-Distortion-of-Binary-Edit-Distance-September-27-2026/build/main.tex) | 64 | companion manuscript root (tree constructions); title [S5:38], date [S5:41], abstract [S5:45–51] |
| S6 | [`lean/docs/099.md`](../../../lean/docs/099.md) | 28 | the formalization scope note: the scope paragraph [S6:11], the exclusion line [S6:19], and the four-row comparator table [S6:23–28] |
| S7 | [`lean/ComparatorChallenges/EditDistance.lean`](../../../lean/ComparatorChallenges/EditDistance.lean) | 70 | headline comparator stub: the `MainClaim` def [S7:56–61], the `edit_distance_main` theorem [S7:67], and the `sorry` [S7:68] |
