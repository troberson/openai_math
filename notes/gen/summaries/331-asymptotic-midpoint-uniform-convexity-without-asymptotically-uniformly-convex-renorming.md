[Notes](../../README.md) / [Summaries](README.md) / [Functional analysis](../index/disciplines/functional-analysis.md) / [Family 331](../index/functional-analysis/331-asymptotic-midpoint-uniform-convexity-without-asymptotically-uniformly-convex-renorming.md)

# 331 — Asymptotic midpoint uniform convexity without asymptotically uniformly convex renorming

[Index page](../index/functional-analysis/331-asymptotic-midpoint-uniform-convexity-without-asymptotically-uniformly-convex-renorming.md)

## Original CONTENTS.md summary

 carries the family entry:

> Constructs a real reflexive Banach space with an asymptotically midpoint uniformly convex norm but no equivalent asymptotically uniformly convex norm, extending Baudier's separation to reflexive spaces. [S1:760]

 carries the first manuscript entry as link text:

> Reflexive tree-space example [S1:760]

## Undergraduate summary

A Banach space is **asymptotically uniformly convex** (AUC) when its unit sphere gets flatter at large scales: the modulus that measures how far the midpoint of two vectors of norm $`t`$ can sit from the sphere stays positive. AUC is a property of a **norm**, not of the space --- a space is AUC renormable if some equivalent norm has it.

The **averaged midpoint modulus** is a midpoint-flavoured variant: it averages the midpoint over the sign choices of a finite family of vectors. The family's headline result is that the two notions separate inside one space: the space carries a norm whose midpoint geometry is asymptotically convex at every scale, and no equivalent norm on the same space is asymptotically uniformly convex. [S2:6–8]

The example is built from a tree. Take the countably branching tree, form the space of functions on its nodes that vanish at infinity, and give it the **segment norm** --- the norm of a function is the supremum, over all paths, of the sum of its values along the path. The space $`X`$ is the dual of the completion of that space, and the theorem states in one statement that $`X`$ is infinite-dimensional, separable, reflexive, has no equivalent AUC norm, satisfies the averaged midpoint bound at every positive scale, and forces distortion at least $`\sqrt{1+k/12}`$ on every embedding of the depth-$`k`$ countably branching diamond. [S3:99–108]

The diamond graphs are the classical obstruction in the nonlinear extension problem: a depth-$`k`$ countably branching diamond cannot be embedded into a space with distortion bounded independently of $`k`$ if the space has strong convexity. The result shows the midpoint convexity does not buy that bound, even under reflexivity. [S3:110–111]

**Proof sketch.** [S3:93–97]

1. For the classical binary James tree space, Girardi proved AUC of both the coordinate predual and the full dual. The countable branching and finite, unbounded component heights used here lead to a different behavior. [S3:93–97]
2. The **paired lemma** is the engine: for a finite ancestral set $`H`$ and vectors with $`x = P_H x`$ and $`y = Q_H y`$, the average of $`\|x+y\|`$ and $`\|x-y\|`$ is at least $`\sqrt{\|x\|^2 + \|y\|^2/12}`$, and the two-parameter version scales the second term by $`st`$ against $`\sqrt{1+12s^2}`$. [S5:37–54]
3. The **bounded-tree lemma** turns that into the renorming obstruction: given vectors indexed by tree nodes with norms between $`m`$ and $`M`$ and child increments at least $`c`$, and child increments tending weakly to zero, every equivalent norm with $`\alpha\|\cdot\| \le N \le \beta\|\cdot\|`$ has modulus zero at scale $`\alpha c/(2\beta M)`$. [S5:37–54]
4. The **lens lemma** supplies the distortion bound: if $`\|x \pm y_j\| \le R`$ and the family $`(y_j)`$ is $`\varepsilon`$-separated, then $`R^2 - \|x\|^2 \ge \varepsilon^2/48`$, which is the squared deficit the diamond bound is derived from. [S4:14–24]
5. The same pattern is reproduced in six other constructions: segment-space lenses, tree energies, a Daugavet subspace of $`L_1`$, bounded tree potentials, independent multipliers in $`L_1`$, and two recursive potentials. [S7:6–15]

## Graduate summary

**The headline theorem.** For the space $`X`$ defined by the segment norm, the theorem states five things at once: $`X`$ is infinite-dimensional, separable, and reflexive; $`X`$ has no equivalent AUC norm; its given norm satisfies $`\widehat\delta_X(t) \ge \sqrt{1+t^2/12}-1`$ for every $`t>0`$; and every embedding of the depth-$`k`$ diamond $`D_k`$ into $`X`$ has distortion at least $`\sqrt{1+k/12}`$. [S3:99–108]

**The target problem.** The paper names what it answers: "This gives a negative answer to the reflexive diamond question recorded as Problem 39 in [S3:110–111]" the Baudier--Lancien manuscript, and it adds that the metric obstruction is unchanged by equivalent renorming, although the numerical constants refer to the specified dual norm. 

**The renorming obstruction.** The bounded-tree lemma is the negative half: for a real Banach space $`Y`$ carrying, for every height $`h`$, vectors indexed by $`\mathbb{N}^{\le h}`$ with norms between $`m`$ and $`M`$ and child increments at least $`c`$, and with child increments tending weakly to zero at each nonterminal node, every equivalent norm $`N`$ with $`\alpha\|\cdot\|\le N\le\beta\|\cdot\|`$ obeys $`\overline\delta_N(\alpha c/(2\beta M)) = 0`$. The same conclusion holds for one infinite tree with these properties. [S5:37–54]

**The six companion manuscripts.** Each proves the separation in a different machinery, with its own constants:

- **Midpoint lenses in segment spaces.** The tail estimate is proved in the full dual of the finite-height forest space and in the coordinate predual of the infinite-tree space, controlling the mass of a vector outside a finite ancestral support by the square-root defect of the common radius. [S8:54–62]
- **Distortion of countably branching diamonds from midpoint and tree energies.** The all-pairs bound is unconditional: every embedding of the depth-$`k`$ diamond with distortion $`D`$ satisfies $`1+k/4 \le D^2`$, in the full dual of the completed finite-height forest space and in the closed coordinate span of the dual of the infinite-tree space. [S10:53–59]
- **Exact asymptotic moduli in a Daugavet subspace of $`L_1`$.** For a closed infinite-dimensional subspace of $`L_1[0,1]`$ with precompact unit ball in measure and the Daugavet property, the moduli are computed exactly: the averaged midpoint modulus is $`\max(t/2, t-1)`$ and the one-sided asymptotic modulus is $`\max(0, t-2)`$, the same formulas hold for the infimum over unit vectors, and every equivalent norm fails AUC. [S12:63–76]
- **Midpoint convexity from bounded tree potentials and path costs.** Four spaces are built; they are complete, separable, and infinite-dimensional, their averaged midpoint modulus is at least $`\sqrt{1+t^2/4}-1`$ for $`0 \lt t \lt 1`$, and no space linearly isomorphic to one of them is asymptotically uniformly convex. [S13:63–71]
- **Independent products in real $`L_1`$.** For a positive, nonconstant multiplier with mean one and finite second moment, the closed span of the path products is infinite-dimensional and has no equivalent AUC norm, and the averaged midpoint modulus is at least $`\frac{7t}{480}\mathbb{E}[(|G|-20/t)_+]`$ for a standard real Gaussian $`G`$. [S15:57–71]
- **Midpoint convexity from two recursive potentials.** The root-sum, zero-root, and joined spaces are infinite-dimensional and have no equivalent AUC norm; the root-sum and joined spaces have averaged midpoint modulus at least $`t^3/128`$ for $`0 \lt t \lt 1`$, the root-sum modulus is positive for every $`t>0`$, and the zero-root and joined spaces are reflexive. [S17:65–77]

**What the formalization says.** The scope note is precise about what the Lean formalization proves. "The formalization proves that the full dual of the specified segment-norm completion is infinite-dimensional, separable, and reflexive [S18:15]", with the $`\sqrt{1+t^2/12}-1`$ averaged midpoint bound, the failure of AUC for every equivalent norm, and the $`\sqrt{1+k/12}`$ diamond bound. 

The forest results are narrower than the manuscript's span: the general-forest and word-forest conclusions retain the finite-ancestor and equivalent-norm hypotheses, including the scale $`\alpha/(2\beta)`$, and "they do not identify that span with the full dual or assert reflexivity for every forest. [S18:17]" 

The scope note also records an assumption count: "Twenty-two of those companion inputs are assumed in these deductions; the diamond distortion bound above does not require them. [S18:25]" 

The last scope paragraph is explicit that assumptions are part of the statements: "The separation, sequence, support, and head assumptions in these results are essential parts of their statements. [S18:41]" 

**Formalization status.** The ledger records family 331 at tier T3: 7 manuscripts, 7 formalized, 1 scope note, 7 comparator challenges, 7 `main_results` entries, 0 reasoning traces, 0 verification bundles. The seven comparator configs the scope note links are `ForestSpace`, `MidpointLenses`, `DiamondDistortion`, `DaugavetModuli`, `BoundedTreePotentials`, `IndependentProducts`, `RecursivePotentials`. A comparator file is a challenge stub stating the target the release set itself; the proved version, where it exists, lives under `lean/OAI/`. Nothing here proves the formalization elaborates --- no Lean or comparator run was performed, which is the standing rule for this catalog.

## History of the conjecture

The separation sits on the James-tree literature. The manuscript records that for the classical binary James tree space, Girardi proved AUC of both the coordinate predual and the full dual, and that the countable branching and finite, unbounded component heights used here lead to a different behavior. [S3:93–97]

The diamond-graph side comes from the countably branching diamond and the tree-space embedding literature; the manuscript's citation record names the Baudier--Lancien manuscript as the source of the problem it answers, and the release's own blurb describes the result as extending Baudier's separation to reflexive spaces. [S1:760]

The Daugavet companion sits in the Daugavet-property literature: the manuscript states its exact modulus formulas for the class of closed infinite-dimensional subspaces of $`L_1[0,1]`$ with precompact unit ball in measure, and the citation record in the manuscript's README names the citation key `DaugavetExactModuli`. [S11:37–45]

## Consequences

The consequence the manuscript states for itself is a negative answer to a recorded problem: a reflexive space whose midpoint geometry is asymptotically convex at every scale, and whose diamond distortion is unbounded in depth, with the metric obstruction invariant under equivalent renorming and the numerical constants tied to the specified dual norm. [S3:110–111]

The catalog consequence is that two properties treated as close relatives are separable inside one space. The seven manuscripts make that separation robust: it holds in tree-segment spaces, in a Daugavet subspace of $`L_1`$, in bounded-potential completions, in independent-product spans of $`L_1`$, and in three recursive-potential spaces, with four distinct modulus constants ($`\sqrt{1+t^2/12}-1`$, $`\sqrt{1+t^2/4}-1`$, $`\max(t/2,t-1)`$, $`t^3/128`$) and two distinct diamond bounds ($`\sqrt{1+k/12}`$, $`\sqrt{1+k/4}`$).

The formalization's own limits are part of the record: the forest results do not identify the closed coordinate span with the full dual, and the graph deductions carry twenty-two companion assumptions the diamond bound does not need. Reading the scope note is what tells you which half of the manuscript's claim the Lean code carries. [S18:17]

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`overview.tex`](../../../overview.tex) | 861 | Family entry, line 758 |
| S2 | [`preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/main.tex`](../../../preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/main.tex) | 27 | Abstract, lines 6--14 |
| S3 | [`preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/sections/introduction.tex`](../../../preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/sections/introduction.tex) | 144 | Main theorem 99--108, negative answer 110--113, Girardi 93--97 |
| S4 | [`preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/sections/diamonds.tex`](../../../preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/sections/diamonds.tex) | 102 | Lens lemma, lines 14--24 |
| S5 | [`preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/sections/obstruction.tex`](../../../preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/build/sections/obstruction.tex) | 98 | Bounded-tree lemma, lines 37--54 |
| S6 | [`preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/README.md`](../../../preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/README.md) | 17 | The manuscript's citation record, lines 11--12 |
| S7 | [`preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/build/main.tex`](../../../preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/build/main.tex) | 41 | Abstract, lines 6--15 |
| S8 | [`preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/build/sections/introduction.tex`](../../../preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/build/sections/introduction.tex) | 178 | Tail estimate theorem, lines 54--62 |
| S9 | [`preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/build/main.tex`](../../../preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/build/main.tex) | 24 | Abstract, lines 6--13 |
| S10 | [`preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/build/sections/introduction.tex`](../../../preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/build/sections/introduction.tex) | 192 | All-pairs distortion theorem, lines 53--59 |
| S11 | [`preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/build/main.tex`](../../../preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/build/main.tex) | 51 | Abstract, lines 37--45 |
| S12 | [`preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/build/sections/introduction.tex`](../../../preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/build/sections/introduction.tex) | 123 | Exact moduli theorem, lines 63--76 |
| S13 | [`preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/build/sections/constrained.tex`](../../../preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/build/sections/constrained.tex) | 280 | Four-space theorem, lines 63--71 |
| S14 | [`preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/build/main.tex`](../../../preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/build/main.tex) | 42 | Abstract, lines 28--34 |
| S15 | [`preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/build/sections/introduction.tex`](../../../preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/build/sections/introduction.tex) | 138 | Main theorem, lines 57--71 |
| S16 | [`preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/build/main.tex`](../../../preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/build/main.tex) | 58 | Abstract, lines 38--47 |
| S17 | [`preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/build/sections/foundations.tex`](../../../preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/build/sections/foundations.tex) | 203 | Recursive-potential theorem, lines 65--77 |
| S18 | [`lean/docs/331.md`](../../../lean/docs/331.md) | 53 | Scope note: formalized claims and retained hypotheses |
