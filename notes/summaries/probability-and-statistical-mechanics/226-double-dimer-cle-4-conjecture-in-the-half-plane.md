Notes / Summaries / Probability and statistical mechanics / [Family 226](../../index/probability-and-statistical-mechanics/226-double-dimer-cle-4-conjecture-in-the-half-plane.md)

# 226 — The double-dimer $\mathrm{CLE}_4$ conjecture in the half-plane

## Original CONTENTS.md summary

The release's blurb [S1:5403]:

> We prove that the complete double-dimer loop ensemble for the Temperleyan square lattice in the upper half-plane converges to nested CLE4. The convergence holds along the full mesh limit and matches every macroscopic loop as an unparametrized curve. This resolves the half-plane Temperleyan form of the double-dimer CLE4 scaling-limit conjecture.

The manuscript's own abstract [S5:42–45] states the same result in two sentences: "We prove that the complete double-dimer loop ensemble for the Temperleyan square lattice in the upper half-plane converges to nested" [S5:42–43], and "The convergence holds along the full mesh limit and matches every macroscopic loop as an unparametrized curve." [S5:44–45] The overview's paraphrase [S2:535] says the ensemble is "the complete loop ensemble formed by two independent dimer coverings of the Temperleyan square lattice converges to nested" and that "Convergence matches every macroscopic loop as an unparametrized curve, upgrading convergence of loop observables to convergence of the loops themselves."

## Undergraduate summary

A dimer covering of a square grid is a way of tiling the grid with dominoes so
that every cell is covered exactly once. The double-dimer model takes two such
tilings independently and lays one on top of the other. Because each cell is
covered twice, once by each tiling, the overlay breaks up into closed loops:
places where the two tilings agree are traced once, places where they disagree
trace a loop that runs through both. "Superposing two independent dimer
coverings produces loops whose large-scale geometry is expected to be
conformally invariant." [S6:3–5]

The manuscript's claim is about the whole collection of these loops, not about
one loop. As the mesh size goes to zero, the collection of loops in the upper
half-plane converges to a specific random object: nested CLE4, which is an
ordinary CLE4 loop ensemble "followed recursively by conditionally independent
copies inside every loop." [S6:35–36] "This is the target space for the
theorem." [S6:80]

Convergence here is not convergence of one number. It is convergence of a
random collection of curves. "Convergence means that such matchings exist"
[S6:58–59] with every loop above a positive diameter cutoff matched by a loop
in the limit, and the matching must work for every such cutoff at once. The
manuscript proves this for the full mesh limit: "The convergence holds along
the full mesh limit and matches every macroscopic loop as an unparametrized
curve." [S5:44–45] A curve is unparametrized — only its shape and position
matter, not the speed at which it is traced.

Earlier work on this model produced probabilities: the chance that a loop
crosses a given pair of boundary points, or that loops nest in a given way.
Those results describe observable events. This manuscript describes the whole
ensemble, so it says what the collection of loops looks like as a random
planar picture, and it says so in a topology that compares collections.

## Graduate summary

The model. The upper half-plane is tiled by a square lattice whose boundary is
covered by half-edge dimers; the manuscript calls this the Temperleyan
boundary. "Take two independent matchings with this law." [S6:29] The overlay
of the two matchings is the double-dimer loop ensemble, and the law is the
uniform measure over pairs of matchings.

The mechanism. The proof is constructive. It builds the scaling limit from a
transfer matrix, proves tightness in the collection topology, and identifies
the limit by matching puncture signatures. The transfer matrix is a signed
adjacency operator between boundary states, where a boundary state records
which dimers cross the seam between columns. Complementing alternate occupancy
bits turns a boundary state into a particle state, and the column transfer is
then an exterior power of a one-particle matrix. "Changing particle number by a
large amount gives a quadratic spectral penalty and hence traversal
tightness." [S6:168–169]

Two estimates carry the geometric content. The transfer section opens by naming the first: "Our first geometric estimate bounds the number of times the double-dimer loops can cross a slab of fixed positive width." [S7:4–5] "The first bounds the total number
of disjoint traversals of a fixed-width slab, including multiple traversals by
a single loop." [S6:146–148] "The second controls the signed crossing counts
of arcs whose endpoints reach prescribed opposite sides of the slab"
[S6:148–150] "Both estimates come from a transfer matrix counting dimer
configurations column by column." [S6:157–158] The short-segment section defines the object the estimate counts: "A tested arc is a cycle subarc, in its cycle direction, with one endpoint in each deep region." [S8:38–40] The first is a spectral
estimate; the second is a positivity identity. "This separation of a local
operator estimate from a planar positivity argument is the main technical
mechanism." [S6:176–178]

The statements. Proposition 3.1 bounds the number of slab traversals.
Proposition 4.1 is the local opposite-sign estimate: it controls the signed
crossing counts of arcs reaching prescribed opposite sides of a slab.
Proposition 4.2 gives preliminary compactness of the loop collection: "Every
subsequential limit has finitely many loops above every positive diameter, and
convergence retains all its nonconstant entries." [S9:395–396] The localization
section couples the half-plane model to finite rectangles — "the two
independent half-plane matchings can be coupled with two independent uniform
matchings of" [S9:26–27] a large rectangle, so that the two matching states
agree on a fixed compact set with probability arbitrarily close to one.
Lemma 5.1 identifies the visible puncture signatures with the loops of a
standard nested CLE4 collection, and Lemma 5.2 shows that no limiting path has
an empty signature, so each limiting path has exactly the trace of its
corresponding loop and traverses it with absolute degree one. Every nonconstant limiting entry is one canonical CLE4 loop as a curve, and "loop as a curve, and every canonical loop occurs once." [S10:174] Lemma 5.3 separates the
topological step from the identification: it restricts convergence from the
closed-disk collection space to the interior collection space.

The collection topology. Convergence is defined by matching all loops above a
positive diameter cutoff, so the target space is a space of collections of
curves, and the metric is chosen so that this matching is what convergence
means. "It is convenient to use a compatible metric" [S6:63] on collections, so that convergence is defined by matching all loops above a positive diameter cutoff. The interior restriction lemma is what makes compact
containment in that space work.

Backtracking. A limiting path can trace a loop more than once. The manuscript
excludes this by a second grid refinement: "A second grid refinement then
excludes backtracking along that trace." [S6:193–194]

## History of the conjecture

Exact dimer enumeration on the square lattice is the classical starting point.
"Exact dimer enumeration on the square lattice was developed by Kasteleyn"
[S6:102–103] and Temperley and Fisher, and the signed transfer-matrix structure
the manuscript uses was clarified by Gessel and Viennot. Lieb worked the
transfer-matrix method out for the dimer problem directly.

The connection to CLE4 comes through the Gaussian free field. "Kenyon proved
convergence of appropriately normalized dimer-height fluctuations" to the
Gaussian free field [S6:107–108], and that field limit "does not by itself give
convergence of loop curves" [S6:111]. Kenyon's 2014 paper proved conformal invariance of loops in the
double-dimer model, and Kenyon and Wilson's boundary-partition work identified
the limiting pairing probabilities: "For alternating black and white
boundary nodes in the half-plane, they showed that the limiting
double-dimer pairing probabilities agree with those for the corresponding
Gaussian-free-field contour lines." [S6:115–118] "This identifies the
boundary pairings, while leaving convergence of the paths open." [S6:118–119]

The CLE4 target is Sheffield and Werner's construction, cited by its title
"Conformal loop ensembles: the Markovian characterization and the loop-soup
construction," [S11:129–130] Bai and Wan's
crossing estimates for simple conformal loop ensembles, and the double-dimer
tau-function work of Basok and Chelkak, whose cylindrical-event probabilities
are the observable-level precursor. Basok and Izyurov's 2025 preprint treats
the nesting of double-dimer loops and the convergence of the nesting field,
which is the local-fluctuation level, below full curve convergence.

Prior (my training data, not the manuscript's record): the double-dimer CLE4
conjecture is Kenyon's 2014 statement, and what was proved before this
manuscript was convergence of single loops and of boundary pairing
probabilities, not of the full collection. The full-ensemble convergence in a
domain with a Temperleyan boundary is the part I would have recorded as open.
The manuscript's own citations are the record; this paragraph is my prior on
the conjecture's standing, and the manuscript does not state it.

## Consequences

The result upgrades observable convergence to curve convergence. The prior
results fixed the probabilities of crossing and nesting events; this fixes the
law of the collection as a random planar picture. That makes the collection
topology, not a single observable, the object being converged, and the interior
restriction lemma is the piece that separates compact containment in the
interior space from the identification of the curves.

The method separates two things that are usually combined in conformal
invariance proofs: a spectral estimate on a local operator, and a positivity
identity on planar loop configurations. The manuscript states that separation
as its main technical mechanism. [S6:176–178]

Open directions the manuscript leaves: the Temperleyan boundary is the specific
model, and the manuscript does not treat other boundary conditions; the
collection topology is defined by positive-diameter cutoffs, so loops below the
cutoff are not controlled; and the identification is by puncture signatures,
which requires the puncture set to be dense, so the coupling is with a standard
nested CLE4 collection realized on a standard Borel space.

## Comparison with the formalized statement

Nothing. The ledger records tier T0 for this family, with no scope note, no
comparator challenge, no `main_results` entry, no reasoning trace, and no
verification bundle. The manuscript's LaTeX is the only source, and the
release's `formalized` flag for this manuscript is 0. The repo readme's
reasoning-summary table, "We are also releasing abridged summaries of the
model's reasoning, covering the following results:" [S3:24], lists ten families
and 226 is not among them. The claim is a conformal-invariance statement about
a random collection of curves; nothing in the Lean library reaches it, and no
certificate ships with it.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `CONTENTS.md` | 9142 | The release's blurb for family 226 at line 5403. |
| S2 | `overview.tex` | 859 | The catalog abstract at line 535. |
| S3 | `README.md` | 51 | The repo readme, which attributes no reasoning trace to this family. |
| S4 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/README.md` | 17 | Citation-only manuscript readme: the model, the result, the method, no provenance. |
| S5 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/main.tex` | 55 | The abstract at lines 42–45. |
| S6 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/10-introduction.tex` | 259 | The theorem statement, the collection topology, the prior work, the mechanism. |
| S7 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/20-transfer.tex` | 518 | The transfer matrix, the particle representation, the slab traversal bound. |
| S8 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/30-short-segment.tex` | 546 | Proposition 3.1, the short-segment crossing estimate. |
| S9 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/40-localization.tex` | 494 | Proposition 4.1, the local opposite-sign estimate, and Proposition 4.2. |
| S10 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/50-identification.tex` | 218 | Lemma 5.1, Lemma 5.2, Lemma 5.3, and the full-limit argument. |
| S11 | `preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/references.tex` | 147 | The bibliography: Kasteleyn, Temperley-Fisher, Gessel-Viennot, Kenyon, Kenyon-Wilson, Sheffield-Werner, Dubédat, Basok-Chelkak, Basok-Izyurov, Bai-Wan. |

## Links

- [S1](../../../CONTENTS.md)
- [S2](../../../overview.tex)
- [S3](../../../README.md)
- [S4](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/README.md)
- [S5](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/main.tex)
- [S6](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/10-introduction.tex)
- [S7](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/20-transfer.tex)
- [S8](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/30-short-segment.tex)
- [S9](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/40-localization.tex)
- [S10](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/sections/50-identification.tex)
- [S11](../../../preprints/The-curve-scaling-limit-of-half-plane-double-dimers-September-23-2026/build/references.tex)
