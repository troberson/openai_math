[Notes](../../README.md) / [Summaries](README.md) / [Convex and metric geometry](../index/disciplines/convex-and-metric-geometry.md) / [Family 090](../index/convex-and-metric-geometry/090-universal-optimality-of-the-triangular-lattice.md)

# 090 — Universal optimality of the triangular lattice

[Index page](../index/convex-and-metric-geometry/090-universal-optimality-of-the-triangular-lattice.md)

## Original CONTENTS.md summary

The release's blurb [S1:2220] and the catalog abstract [S2:256] state
the family's claim: the density-one triangular lattice minimizes the
lower limit of energy per particle for every nonnegative completely
monotone potential of squared distance among locally finite planar
configurations of centered-disk density one, and separately minimizes
unit-background renormalized Riesz energies for $`0<s<2`$ and the Coulomb
energy, resolving the Sandier–Serfaty and the two-dimensional
Brauchart–Hardin–Saff conjectures. The family ships four
manuscripts. The atomic-certificate manuscript 

> We prove that the density-one triangular lattice minimizes the lower energy
per particle for every nonnegative completely monotone function of squared
distance, among all locally finite planar configurations of centered disk
density one. The comparison includes infinite energies. The proof constructs
sharp Gaussian Fourier minorants using an atomic interpolation certificate. [S3:29–33]

## Undergraduate summary

The triangular lattice is the densest way to pack equal circles in the
plane — hexagonal packing, the arrangement honeybees, coins on a
table, and atoms in a metal all settle into. Thue proved that density
statement in 1900. This family asks a much broader question: is the
triangular lattice also the ground state of every attractive,
distance-decreasing interaction? That is the idea of *universal
optimality* — one configuration that minimizes the energy of every
potential in a large family at once.

The four manuscripts prove four interlocking theorems. Three of them
say the triangular lattice is the energy minimizer (for a very large
class of interaction potentials, and for the Coulomb and Riesz energies
specifically), and one says the hexagonal circle-packing density
$`\pi/(2\sqrt3)`$ is the *best possible* two-point Fourier bound. The
recurring proof device is a sharp Gaussian Fourier minorant: a function
that lies just below the Gaussian, has a nonnegative Fourier transform,
and touches the Gaussian exactly at the triangular-lattice points.

## Graduate summary

**The four statements.** The universal-optimality manuscript
[S4:32–39] proves the headline universal-energy inequality
with its jellium-minima corollary:

> We prove universal energy minimality for the triangular lattice in the plane.
Among locally finite configurations of centered density one, it minimizes the
lower limit of centered-ball energy averages for every nonnegative completely
monotone function of squared distance, including when the energy is infinite.
We also prove triangular minimality for planar logarithmic and Riesz
renormalized energies, with $`0<s<2`$ in the Riesz case, and the corresponding
jellium minima. The proof uses sharp Gaussian Fourier bounds, positive
mixtures, and heat-kernel comparison. [S4:32–39]

The Fourier-certificate manuscript [S5:70–75] resolves the
planar Cohn–Elkies sharpness conjecture:

> We resolve the planar Cohn–Elkies sharpness conjecture: the two-point
Fourier bound attains the optimal circle-packing density $`\pi/(2\sqrt3)`$.
We construct a radial Schwartz certificate and prove its global sign
conditions using rigorous interval arithmetic and analytic estimates.
The same certificate recovers the classical uniqueness of the triangular
packing among periodic equality cases. [S5:70–75]

The Coulomb manuscript [S6:45–51] proves the
Sandier–Serfaty conjecture:

> We prove the Sandier–Serfaty conjecture: the triangular lattice of
covolume one minimizes planar Coulomb renormalized energy over all admissible
curl-free fields with a unit uniform background. Combined with Bétermin and
Sandier's asymptotic formula, this also proves the Brauchart–Hardin–Saff
conjecture for the linear term of optimal ordered-pair logarithmic energy on
the unit two-sphere. The proof uses a direct Voronoi-cell comparison with
rigorous interval arithmetic. [S6:45–51]

**The proof device.** The atomic-certificate manuscript
[S3:29–33] is the one that builds the minorant: sharp Gaussian
Fourier minorants by an atomic interpolation certificate, including
infinite energies in the comparison. The universal-optimality manuscript
assembles the energy bound from those minorants (Gaussian energy
transfer, positive mixtures, heat-kernel comparison, [S4:32–39]);
the Coulomb manuscript closes by a *direct* Voronoi-cell comparison with
rigorous interval arithmetic, not by the minorant route [S6:45–51].

## History of the conjecture

These are named, long-standing open problems. The Cohn–Elkies
sharpness question asks whether the two-point Fourier method attains the
optimal circle-packing density; the Sandier–Serfaty conjecture
asks whether the triangular lattice minimizes planar Coulomb
renormalized energy; the Brauchart–Hardin–Saff conjecture
concerns the linear term of optimal ordered-pair logarithmic energy on
the two-sphere [S5:70–75, S6:45–51]. The universal-optimality
program for the triangular lattice is the Fourier-analytic generalization
of the Thue–Hales circle-packing result.

**Prior (my training data, not this repo).** I know circle-packing
density and the Cohn–Elkies two-point Fourier framework, and I know
the Sandier–Serfaty Coulomb-minimality and Brauchart–Hardin–Saff
spherical-logarithmic conjectures as open. Triangular-lattice minimality
of *planar* Coulomb renormalized energy (and the resulting
two-dimensional spherical-logarithmic linear term) is, to my knowledge,
not established in the literature I was trained on, and it is arguably
the most consequential of the four theorems. I cannot independently
verify these 2026 manuscripts' arguments.

## Consequences

**Universal energy minimality.** For every nonnegative completely
monotone potential of squared distance, the density-one triangular
lattice minimizes per-particle energy among locally finite centered-disk
density-one configurations, infinite energies included
[S3:29–33, S4:32–39].

**Sharp circle-packing density.** The two-point Fourier method attains
the optimal density $`\pi/(2\sqrt3)`$, with the certificate's global sign
conditions proved by rigorous interval arithmetic
[S5:70–75].

**Sandier–Serfaty resolved.** The covolume-one triangular lattice
minimizes planar Coulomb renormalized energy over admissible curl-free
fields with a unit background [S6:45–51].

**Two-dimensional Brauchart case.** The Brauchart–Hardin–Saff
conjecture for the linear term of optimal ordered-pair logarithmic energy
on the unit two-sphere follows, combined with
B\'etermin–Sandier [S6:45–51].

## Section skeleton

Four manuscripts, all with a `build/main.tex` root and a `verification/`
bundle:

- **atomic-certificate** [S3:29–33] (title [S3:23], date [S3:25]) — one
  file, no `sections/`; an inline `thebibliography` block plus a
  23-entry `references.bib` in `build/`; verification bundle with a
  `CERTIFICATE.json`, `README.md`, and `check_certificate.py`.
- **universal-optimality** [S4:32–39] (title [S4:26], date [S4:28]) —
  ten `sections/` files (uniform-gaussian-theorem, cardinal-fourier,
  quadrature-finite-data, exact-interpolation, global-signs,
  gaussian-energy-transfer, shifted-mixtures, arithmetic-verification,
  renormalized-jellium, conditional-floor-verification); a 33-entry
  `references.bib`; verification bundle with arithmetic-bounds scripts.
- **Fourier-certificate** [S5:70–75] (title [S5:64], date [S5:66]) —
  eight `sections/` files (introduction, normalization, interpolation,
  fourier, signs, certificates, independent-certification,
  rational-check); a figure `figures/half-gaps.tex` and `data/`
  coefficient files; a 12-entry `references.bib`; verification bundle
  with `verify_all.py` and interval-arithmetic scripts.
- **Coulomb** [S6:45–51] (title [S6:39], date [S6:41]) — ten
  `sections/` files (introduction, reduction, geometry, calibration,
  tails, computation, conclusion, scientific-support, history); a figure
  `figures/signed-sectors.tex`; a 19-entry `references.bib`;
  verification bundle.

## Comparison with the formalized statement

**Scope note** [S7:8–16]. The formalization covers three selected
statements: the density-one triangular-lattice energy minimum, the sharp
radial Schwartz Gaussian minorants (with their explicit atomic
interpolation construction), and the planar Cohn–Elkies sharpness
certificate:

> The formalization proves that the density-one triangular lattice minimizes lower energy per particle among all locally finite planar configurations of centered-disk density one, for every nonnegative completely monotone function of squared distance. Infinite energies are allowed in the comparison.

It also constructs sharp radial Schwartz minorants for every Gaussian potential: each minorant lies below the Gaussian, has nonnegative real Fourier transform, agrees with the Gaussian at nonzero triangular-lattice points, and vanishes on nonzero dual-lattice points after Fourier transformation. For the stated parameter range, the formalization includes the explicit atomic interpolation construction. [S7:10–12]

The Cohn–Elkies certificate conditions, with the periodic-uniqueness
exclusion:

> The planar Cohn–Elkies sharpness conjecture asks whether the two-point Fourier method attains the optimal circle-packing density. The formalization constructs a radial Schwartz function $`f`$ on $`\mathbb R^2`$ with $`\widehat f(0)=1`$, $`f(0)=2/\sqrt3`$, $`\widehat f`$ real and nonnegative everywhere, and $`f(x)\le0`$ whenever $`\|x\|\ge1`$. These are the sharp Fourier certificate conditions yielding density $`\pi/(2\sqrt3)`$. The separate uniqueness statement for periodic equality cases is outside this selected theorem. [S7:14]

The scope note links **two** of the four manuscripts (the
atomic-certificate and the Fourier-certificate papers)
[S7:5–6], and names four comparator statements
[S7:18–23]. The release records `scope: "Partial progress."` and
`review: status: unchecked`; zero `sorry` in the Lean source is not a
comparator pass, and the library has not been built here.

**Four comparator stubs, each with a `sorry`.** The universal-energy
target 

```lean
theorem universal_energy_minimum (g : ℝ → ℝ) (C : Set Plane)
    (hg : AdmissiblePotential g) (hC : LocallyFinite C) (hd : DensityOne C) :
    latticeEnergy g ≤ energy g C ∧ latticeEnergy g = energy g A := by
  sorry
```
[S9:66–69]

The planar-packing target, with the normalized-certificate definition
[S11:28–31] and the open theorem [S11:36–38]:

```lean
def SharpCertificate (f : SchwartzMap Plane ℝ) : Prop :=
  Radial f ∧ fourier f 0 = 1 ∧ f 0 = 2 / Real.sqrt 3 ∧
    (∀ ξ, (fourier f ξ).im = 0 ∧ 0 ≤ (fourier f ξ).re) ∧
    (∀ x, 1 ≤ ‖x‖ → f x ≤ 0)

end SharpPlanar

/-- The sharp Fourier certificate theorem. -/
theorem sharp_fourier_certificate :
    ∃ f : SchwartzMap SharpPlanar.Plane ℝ, SharpPlanar.SharpCertificate f := by
  sorry
```
[S11:28–38]

The two minorant targets sit at [S8:239–245] (with `sorry`
[S8:246]) and [S10:263–269] (with `sorry` [S10:270]).

**The OAI tree proves all four comparator statements, but the release
registers nothing.** The two OAI trees exist with zero `sorry`: the
`Analysis/Triangular` tree (276 `.lean` files over 68,778 lines) and the
`Analysis/PlanarPacking` tree (562 files over 916,013 lines). They prove
the universal-energy minimum at `Universal.lean:9` 

```lean
theorem universal_energy_minimum (g : ℝ → ℝ) (C : Set Plane)
    (hg : AdmissiblePotential g) (_hC : LocallyFinite C) (hd : DensityOne C) :
    latticeEnergy g ≤ energy g C ∧ latticeEnergy g = energy g A := by
  have hb (α : ℝ) (hα : 0<α) :
      TriangularUniversal.latticeEnergy (TriangularUniversal.gaussPot α)≤
        TriangularUniversal.energy (TriangularUniversal.gaussPot α) C := by
    rw [←latticeEnergy_eq_support]
    exact gaussian_energy_bound hd α hα
  have hu := TriangularUniversal.universal_from_gaussian_bounds hd hb hg
  constructor
  · rw [latticeEnergy_eq_support]
    exact hu.1
```
[S12:9–20]

the atomic minorants at `Main.lean:75` [S13:75–90], which the
construction-variant at `GaussianMinorants.lean:73` [S14:73–81]
derives by stripping the construction witness:

```lean
theorem sharp_gaussian_minorants_atomic (α : ℝ) (hα : 0 < α) :
    ∃ f : SchwartzMap Plane ℝ,
      Radial f ∧ (∀ x, f x ≤ gaussian α x) ∧
      (∀ w, (realFourier f w).im = 0 ∧ 0 ≤ (realFourier f w).re) ∧
      (∀ a ∈ A, a ≠ 0 → f a = gaussian α a) ∧
      (∀ w ∈ dualA, w ≠ 0 → realFourier f w = 0) ∧
      (1 ≤ α → Construction.HasAtomicConstruction α f) := by
  let p := gaussianPair α hα
  refine ⟨p.first, p.first_radial, p.minorant, ?_, ?_, ?_, ?_⟩
  · intro w
    rw [p.fourier_first]
    exact ⟨rfl, p.positive w⟩
  · intro a ha ha0
    obtain ⟨n, hn⟩ := A_radial_node ha ha0
    exact p.contact a n hn
  · intro w hw hw0
```
[S13:75–90]

```lean
theorem sharp_gaussian_minorants_with_construction (α : ℝ) (hα : 0 < α) :
    ∃ f : SchwartzMap Plane ℝ,
      Radial f ∧ (∀ x, f x ≤ gaussian α x) ∧
      (∀ w, (realFourier f w).im = 0 ∧ 0 ≤ (realFourier f w).re) ∧
      (∀ a ∈ A, a ≠ 0 → f a = gaussian α a) ∧
      (∀ w ∈ dualA, w ≠ 0 → realFourier f w = 0) ∧
      (1 ≤ α → AtomicConstruction α f) := by
  obtain ⟨f, hradial, hminorant, hfourier, hcontact, hzero, hconstruction⟩ :=
    sharp_gaussian_minorants_atomic α hα
```
[S14:73–81]

and the Cohn–Elkies certificate at `PlanarPacking/Main.lean:32`
[S15:32–34], closing as a single term
`\langle normalizedCandidate, normalizedCandidate_certificate
\rangle`:

```lean
theorem sharp_fourier_certificate :
    ∃ f : SchwartzMap SharpPlanar.Plane ℝ, SharpPlanar.SharpCertificate f :=
  ⟨SharpPlanar.normalizedCandidate,SharpPlanar.normalizedCandidate_certificate⟩
```
[S15:32–34]

**Structural absence (T2).** None of the four comparator configs
(`AtomicGaussian`, `TriangularEnergy`, `TriangularGaussian`,
`PlanarPacking`) appears in `formalization.yaml`, and none of the four
manuscripts appears in its `sources:` listing — so the ledger
records `paps_form 0` and `mainres 0`. The proofs exist in the OAI tree
and no `sorry` remains, but the release registers the family in none of
its checking workflow. And the family's headline
Sandier–Serfaty Coulomb statement and Riesz/jellium theorems are
not among the four comparator statements at all, so the OAI tree proves
them neither.

## Coverage

T2: the family carries a scope note and four comparator challenges but
no `main_results` entry and no `sources:` entry. The ledger row
`fam=090` records `paps 4`, `paps_form 0`, `tier T2`, `chal 4`,
`mainres 0`, `scope_note 1`, `verification 4`, `trace` empty,
`shapes resolution|density|uniform`, `resolves_named 1`, `summary 1`.
The family ships four LaTeX manuscripts (each with a `verification/`
bundle), a scope note covering two of them, and four comparator
challenges each carrying one `sorry` theorem; a 276-file and a 562-file
OAI tree with zero `sorry` together prove all four comparator
statements, but the release registers the family in `main_results` and
`sources` nowhere.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's blurb for family 090 at [S1:2220] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the catalog's \resultentry{090} at [S2:256] |
| S3 | [`preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/build/main.tex`](../../../preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/build/main.tex) | 2473 | atomic-certificate manuscript root; title [S3:23], date [S3:25], abstract [S3:29–33] |
| S4 | [`preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/build/main.tex`](../../../preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/build/main.tex) | 55 | universal-optimality manuscript root; title [S4:26], date [S4:28], abstract [S4:32–39] |
| S5 | [`preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/build/main.tex`](../../../preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/build/main.tex) | 100 | Fourier-certificate manuscript root; title [S5:64], date [S5:66], abstract [S5:70–75] |
| S6 | [`preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/build/main.tex`](../../../preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/build/main.tex) | 66 | Coulomb manuscript root; title [S6:39], date [S6:41], abstract [S6:45–51] |
| S7 | [`lean/docs/090.md`](../../../lean/docs/090.md) | 23 | the formalization scope note: the scope prose at [S7:10–14] and the comparator table at [S7:18–23] |
| S8 | [`lean/ComparatorChallenges/AtomicGaussian.lean`](../../../lean/ComparatorChallenges/AtomicGaussian.lean) | 252 | comparator stub (atomic minorants): the statement [S8:239–245] and the `sorry` [S8:246] |
| S9 | [`lean/ComparatorChallenges/TriangularEnergy.lean`](../../../lean/ComparatorChallenges/TriangularEnergy.lean) | 74 | comparator stub (universal energy): the statement [S9:66–68] and the `sorry` [S9:69] |
| S10 | [`lean/ComparatorChallenges/TriangularGaussian.lean`](../../../lean/ComparatorChallenges/TriangularGaussian.lean) | 275 | comparator stub (minorants with construction): the statement [S10:263–269] and the `sorry` [S10:270] |
| S11 | [`lean/ComparatorChallenges/PlanarPacking.lean`](../../../lean/ComparatorChallenges/PlanarPacking.lean) | 40 | comparator stub (Fourier certificate): the certificate def and open theorem [S11:28–38] |
| S12 | [`lean/OAI/Analysis/Triangular/Energy/Universal.lean`](../../../lean/OAI/Analysis/Triangular/Energy/Universal.lean) | 26 | the OAI proven `universal_energy_minimum` [S12:9–20] |
| S13 | [`lean/OAI/Analysis/Triangular/Main.lean`](../../../lean/OAI/Analysis/Triangular/Main.lean) | 102 | the OAI proven `sharp_gaussian_minorants_atomic` [S13:75–90] |
| S14 | [`lean/OAI/Analysis/Triangular/GaussianMinorants.lean`](../../../lean/OAI/Analysis/Triangular/GaussianMinorants.lean) | 89 | the OAI proven `sharp_gaussian_minorants_with_construction` [S14:73–81] |
| S15 | [`lean/OAI/Analysis/PlanarPacking/Main.lean`](../../../lean/OAI/Analysis/PlanarPacking/Main.lean) | 36 | the OAI proven `sharp_fourier_certificate` [S15:32–34] |

## Bibliography

- Henry Cohn and Stephen D. Miller. Some properties of optimal functions for sphere packing in dimensions $`8`$ and $`24`$, 2016. Version 1, March 15, 2016. .
- Douglas P. Hardin and Nathaniel J. Tenpas. Universally optimal periodic configurations in the plane.  Discrete Analysis, 2025. Paper No. 26, 63 pp. doi:10.19086/da.144978.
- J. W. S. Cassels. On a problem of Rankin about the Epstein zeta-function.  Proceedings of the Glasgow Mathematical Association, 4(2):73–80, 1959. See corrigendum, volume 6 (1963), page 116, and the 1964 corrections by Ennola and Diananda. doi:10.1017/S2040618500033906.
- J. W. S. Cassels. Corrigendum.  Proceedings of the Glasgow Mathematical Association, 6(2):116, 1963. Corrigendum to ``On a problem of Rankin about the Epstein zeta-function''. doi:10.1017/S2040618500034833.
- P. H. Diananda. Notes on two lemmas concerning the Epstein zeta-function.  Proceedings of the Glasgow Mathematical Association, 6(4):202–204, 1964. doi:10.1017/S2040618500035036.
- Veikko Ennola. A lemma about the Epstein zeta-function.  Proceedings of the Glasgow Mathematical Association, 6(4):198–201, 1964. doi:10.1017/S2040618500035024.
- R. A. Rankin. A minimum problem for the Epstein zeta-function.  Proceedings of the Glasgow Mathematical Association, 1(4):149–158, 1953. doi:10.1017/S2040618500035668.
- Emanuel Carneiro, Friedrich Littmann, and Jeffrey D. Vaaler. Gaussian subordination for the Beurling–Selberg extremal problem.  Transactions of the American Mathematical Society, 365(7):3493–3534, 2013. doi:10.1090/S0002-9947-2013-05716-9.
- Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska. {Universal optimality of the $`E_8`$ and Leech lattices and interpolation formulas}.  Annals of Mathematics, 196(3):983–1082, 2022. doi:10.4007/annals.2022.196.3.3.
- Jihad Titi and Jürgen Garloff. Matrix methods for the tensorial Bernstein form.  Applied Mathematics and Computation, 346:254–271, 2019. doi:10.1016/j.amc.2018.08.049.
- Markus Faulhuber, Irina Shafkulovska, and Ilia Zlotnikov. A note on energy minimization in dimension 2.  Proceedings of the American Mathematical Society, Series B, 11:664–679, 2024. doi:10.1090/bproc/247.
- Henry Cohn and Matthew de Courcy-Ireland. The Gaussian core model in high dimensions.  Duke Mathematical Journal, 167(13):2417–2455, 2018. doi:10.1215/00127094-2018-0018.
- Hugh L. Montgomery. Minimal theta functions.  Glasgow Mathematical Journal, 30(1):75–85, 1988. doi:10.1017/S0017089500007047.
- Serge Bernstein. Sur les fonctions absolument monotones.  Acta Mathematica, 52:1–66, 1929. doi:10.1007/BF02592679.
- M. J. Dubourdieu. Sur un théor{\`e}me de M. S. Bernstein relatif {\`a} la transformation de Laplace-Stieltjes.  Compositio Mathematica, 7:96–111, 1940. .
- Henry Cohn and Noam Elkies. New upper bounds on sphere packings I.  Annals of Mathematics, 157(2):689–714, 2003. doi:10.4007/annals.2003.157.689.
- OpenAI. A sharp Fourier certificate for planar circle packing. OpenAI Math Release preprint OAI:A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026, 2026.
- OpenAI. Universal optimality of the triangular lattice. OpenAI Math Release preprint OAI:Universal-optimality-of-the-triangular-lattice-September-23-2026, 2026.
- Thomas Leblé. The hexagonal lattice is universally locally optimal, 2025. Version 1, submitted November 5, 2025. .
- Naser Talebizadeh Sardari. Higher Fourier interpolation on the plane, 2021. Version 2, May 4, 2021. .
- Danylo Radchenko and Maryna Viazovska. Fourier interpolation on the real line. { Publications Mathématiques de l'IHÉS}, 129:51–81, 2019. doi:10.1007/s10240-018-0101-z.
- Henry Cohn and Abhinav Kumar. Universally optimal distribution of points on spheres.  Journal of the American Mathematical Society, 20(1):99–148, 2007. doi:10.1090/S0894-0347-06-00546-7.
- D. V. Widder. Necessary and sufficient conditions for the representation of a function as a Laplace integral.  Transactions of the American Mathematical Society, 33(4):851–892, 1931. doi:10.1090/S0002-9947-1931-1501621-6.
