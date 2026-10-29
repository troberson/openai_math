[Notes](../../README.md) / [Summaries](README.md) / [Probability and statistical mechanics](../index/disciplines/probability-and-statistical-mechanics.md) / [Family 222](../index/probability-and-statistical-mechanics/222-perceptron-free-energies-and-microscopic-jamming.md)

# 222 — Perceptron free energies and microscopic jamming

[Index page](../index/probability-and-statistical-mechanics/222-perceptron-free-energies-and-microscopic-jamming.md)

## Original CONTENTS.md summary

[S1:5245] (family entry):

> **222. Percepton free energies and microscopic jamming exponents.** Determines finite-temperature variational free energies for Gaussian Ising perceptrons with bounded Borel log-potentials and Gaussian spherical perceptrons with bounded continuous potentials, at every positive pattern density. A spherical extension treats bi-orthogonally invariant disorder with compact limiting singular-value distributions and no outliers. At margin −1, the quadratic-penalty spherical model has a sharp feasibility threshold and limiting gap and force laws, with system size, zero temperature, and critical density taken in that order. ([Lean](../../../lean/docs/222.md))

[S2:529] carries the `\resultentry`, so the release blurb and the overview agree.
The four manuscripts:

**Ising perceptron free energy** [S3:3, S3:5]:

> 1

**Negative spherical perceptron jamming** [S4:43, S4:45]:

> 2

**Bi-orthogonally invariant disorder** [S5:36, S5:38]:

> 3

**Spherical perceptron free energy** [S6:23, S6:25]:

> 4

## Undergraduate summary

A **perceptron** is the simplest artificial neural network: it takes a set of
input patterns, assigns random "weights" to them, and tries to classify a
new input by a weighted sum. The **free energy** measures how well the
perceptron can fit the patterns at a given "temperature" (a knob that
controls randomness). The key question is: *how many patterns can the
perceptron store before it jams* (before no weight assignment fits all
of them)? This family determines the exact free energy for several
perceptron models [S3:9–12, S4:49–61, S5:42–45,
S6:29–32, S2:529].

## Graduate summary

**Ising perceptron** [S3:9–12, S2:529]. For the Ising
perceptron with independent Gaussian patterns, the limiting free
energy is determined for every bounded Borel log-potential, at every
fixed positive temperature and pattern density. The variational
formula gives an explicit expression, and convergence is proved
both in expectation and in probability.

**Spherical perceptron** [S6:29–32, S2:529]. The same
variational formula holds for the spherical perceptron with any
bounded continuous single-pattern potential, at every positive
density and inverse temperature, with convergence in expectation
and probability. The bi-orthogonally invariant extension
[S5:42–45] treats disorder matrices with any compact
limiting singular-value distribution (no outliers).

**Microscopic jamming** [S4:49–61, S2:529]. At
margin $`-1`$ with quadratic penalty, the spherical perceptron has
a sharp feasibility threshold. The limiting gap and force laws
satisfy power-law scaling:
$`G_J(u)=u^{1-\gamma+o(1)}`$ and
$`F_J(s)=s^{1+\theta+o(1)}`$ as $`u,s\downarrow 0`$,
with $`\gamma=(2+\theta)^{-1}`$,
$`0.4126930<\gamma<0.4126934`$, and
$`0.4231063<\theta<0.4231088`$.

## History of the conjecture

The **perceptron model** (Rosenblatt, 1958) is the simplest
neural network. The **storage capacity** question — how
many random patterns can be stored before the perceptron
jams — was first addressed by Gardner (1988) in the
spherical (continuous) case. The **Ising perceptron**
extends the model to discrete (±1) spins, introducing
log-potential terms that account for the discrete constraint.
The **variational free energy formula** takes the form of an
infimum over overlap paths, generalizing the TAP (Thouless–Anderson–Palmer)
program from spin glasses. The **bi-orthogonally
invariant** extension [S5:42–45] moves from Gaussian
disorder to a broader class of disorder matrices characterized
by their limiting singular-value distribution. The
**microscopic jamming** exponents [S4:49–61] quantify
the critical behavior near the feasibility threshold,
extending the work on jamming transitions in high-dimensional
combinatorial optimization.

**Prior (my training data, not this repo).** The spherical
perceptron capacity (Gardner 1988), the TAP program for spin
glasses, and the Ising extension are standard. The exact
variational formula for the full Borel log-potential class,
the bi-orthogonally invariant extension, and the precise
jamming exponents are the novel contributions. I cannot
confirm these results independently from training alone.

## Consequences

- **The Ising perceptron free energy**
  [S3:9–12]: an explicit variational formula for
  every bounded Borel log-potential, at every positive
  density and temperature.
- **The spherical perceptron free energy**
  [S6:29–32]: the same formula for bounded continuous
  single-pattern potentials.
- **The bi-orthogonal extension**
  [S5:42–45]: the formula extends to disorder
  matrices with any compact limiting singular-value
  distribution.
- **The jamming exponents**
  [S4:49–61]: sharp power-law scaling of the gap
  and force near the feasibility threshold, with
  numerically bounded exponents $`\gamma\in
  (0.4126930, 0.4126934)`$ and $`\theta\in
  (0.4231063, 0.4231088)`$.

## Section skeleton

Four manuscripts: [S3] (title [S3:3], date [S3:5])
— `main.tex` under `build/` with `sections/` and
`preamble.tex`; [S4] (title [S4:43], date [S4:45])
— `main.tex` under `build/`; [S5] (title [S5:36],
date [S5:38]) — `paper.tex` under `build/`;
[S6] (title [S6:23], date [S6:25]) — `paper.tex`
under `build/` with `figures/` and `references.bib`.
The family ships no `verification/` bundle.

## Comparison with the formalized statement

The release formalises this family at tier T2 with one
scope note [S7] and three comparator stubs [S8] [S9]
[S10], but **no** `main_results` entry and **no** OAI
tree. The scope note [S7:10–16] describes three
targets: (1) finiteness of the Ising-perceptron
variational value — "a supporting well-definedness
result" that "does not assert convergence of the
finite-system pressure"; (2) the variational formula for
the spherical-perceptron limiting pressure with
convergence in expectation and probability; (3) the
spherical linear-field dual formula and bounded
stationary-field approximation. The three comparator
stubs carry these targets: `IsingFiniteness.lean`
[S8] states `variationalValue_real_of_continuous`
[S8:86–89] and ends in `sorry`;
`PerceptronFreeEnergy.lean` [S9] carries the
variational formula theorem [S9:98–105] and ends
in `sorry`; `SphericalField.lean` [S10] states
`spherical_linear_field_formula` [S10:552–554]
and ends in `sorry`. No proved copy exists under
`lean/OAI/`. The gap is the formalization itself: the
release set the targets and described the scope, but
shipped no proof. The reading is of source text only.

## Coverage

The ledger row `fam=222` [S11] records the tier and
the counts: `tier=T2`, `paps=4`, `paps_form=0`,
`chal=3`, `mainres=0`, `scope_note=1`,
`verification=0`, `trace=`. The T2 shape is
"scope note and comparator stubs exist, no
formalization": the release identified three target
theorems, wrote a scope note, and created three
challenge stubs with `sorry`, but did not produce a
`main_results` entry or an OAI proof. The
`paps_form=0` against `paps=4` confirms that none of
the four manuscripts is named as a formalization
source in the yaml. There is no verification bundle
and no reasoning trace. The shape flags are
`bound|density`, and `resolves_named=0`.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | [`CONTENTS.md`](../../../CONTENTS.md) | 9167 | the release's catalog — family entry [S1:5245] |
| S2 | [`overview.tex`](../../../overview.tex) | 861 | the release's `\resultentry` list — 222 at [S2:529] |
| S3 | [`preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/build/main.tex`](../../../preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/build/main.tex) | 26 | manuscript 1 of 4 (Ising perceptron free energy); title [S3:3], date [S3:5], abstract [S3:8–13] |
| S4 | [`preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/build/main.tex`](../../../preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/build/main.tex) | 10355 | manuscript 2 of 4 (negative spherical perceptron jamming); title [S4:43], date [S4:45], abstract [S4:48–62] |
| S5 | [`preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/build/paper.tex`](../../../preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/build/paper.tex) | 1465 | manuscript 3 of 4 (bi-orthogonally invariant disorder); title [S5:36], date [S5:38], abstract [S5:41–46] |
| S6 | [`preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/build/paper.tex`](../../../preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/build/paper.tex) | 1578 | manuscript 4 of 4 (spherical perceptron free energy); title [S6:23], date [S6:25], abstract [S6:28–33] |
| S7 | [`lean/docs/222.md`](../../../lean/docs/222.md) | 24 | scope note — the formalization's Scope at [S7:10–16] and its three comparator links at [S7:22–24] |
| S8 | [`lean/ComparatorChallenges/IsingFiniteness.lean`](../../../lean/ComparatorChallenges/IsingFiniteness.lean) | 94 | comparator stub — `variationalValue_real_of_continuous` at [S8:86–89] with its `sorry` at [S8:89] |
| S9 | [`lean/ComparatorChallenges/PerceptronFreeEnergy.lean`](../../../lean/ComparatorChallenges/PerceptronFreeEnergy.lean) | 111 | comparator stub — the variational formula theorem at [S9:98–105] with its `sorry` at [S9:105] |
| S10 | [`lean/ComparatorChallenges/SphericalField.lean`](../../../lean/ComparatorChallenges/SphericalField.lean) | 557 | comparator stub — `spherical_linear_field_formula` at [S10:552–554] with its `sorry` at [S10:554] |
| S11 | [`notes/gen/tables/catalog.tsv`](../../../notes/gen/tables/catalog.tsv) | 374 | the ledger row `fam=222`; regenerate with `python3 notes/scripts/build_catalog.py`. Ours, not in the release |

## Bibliography

- A. Abbara, B. Aubin, F. Krzakala, and L. Zdeborová, Rademacher complexity and spin glasses: a link between the replica and statistical theories of learning, in _Proceedings of the First Mathematical and Scientific Machine Learning Conference_, _Proc. Mach. Learn. Res._ **107** (2020). PMLR article page.
- M. Aizenman, R. Sims and S. L. Starr, _Extended variational principle for the Sherrington–Kirkpatrick spin-glass model_, Physical Review B **68** (2003), 214403. doi:10.1103/PhysRevB.68.214403.
- M. Aizenman, R. Sims, and S. L. Starr, Extended variational principle for the Sherrington–Kirkpatrick spin-glass model, _Phys. Rev. B_ **68** (2003), 214403. doi:10.1103/PhysRevB.68.214403.
- P. Charbonneau, J. Kurchan, G. Parisi, P. Urbani and F. Zamponi, _Exact theory of dense amorphous hard spheres in high dimension. III. The full replica symmetry breaking solution_, Journal of Statistical Mechanics: Theory and Experiment (2014), P10009. doi:10.1088/1742-5468/2014/10/P10009. Preprint version: arXiv:1310.2549v5.
- S. Chatterjee, _A generalization of the Lindeberg principle_, The Annals of Probability **34** (2006), no. 6, 2061–2076. doi:10.1214/009117906000000575.
- A. Auffinger and W.-K. Chen, _The Parisi formula has a unique minimizer_, Communications in Mathematical Physics **335** (2015), 1429–1444. doi:10.1007/s00220-014-2254-z.
- H.-B. Chen, V. Issa and J.-C. Mourrat, _The convex structure of the Parisi formula for multi-species spin glasses_, preprint (2025). arXiv:2508.06397.
- W.-K. Chen, _The Aizenman–Sims–Starr scheme and Parisi formula for mixed $`p`$-spin spherical models_, Electronic Journal of Probability **18** (2013), no. 94, 1–14. doi:10.1214/EJP.v18-2580.
- E. Gardner and B. Derrida, _Optimal storage properties of neural network models_, Journal of Physics A: Mathematical and General **21** (1988), 271–284. doi:10.1088/0305-4470/21/1/031.
- E. Gardner and B. Derrida, Optimal storage properties of neural network models, _J. Phys. A: Math. Gen._ **21** (1988), no. 1, 271–284. doi:10.1088/0305-4470/21/1/031.
- F. vom Ende and G. Dirr, The $`d`$-majorization polytope, _Linear Algebra Appl._ **649** (2022), 152–185. doi:10.1016/j.laa.2022.05.005. arXiv:1911.01061v5.
- M. Boué and P. Dupuis, _A variational representation for certain functionals of Brownian motion_, The Annals of Probability **26** (1998), 1641–1659. doi:10.1214/aop/1022855876.
- S. Franz, G. Parisi, M. Sevelev, P. Urbani and F. Zamponi, _Universality of the SAT-UNSAT (jamming) threshold in non-convex continuous constraint satisfaction problems_, SciPost Physics **2** (2017), 019. doi:10.21468/SciPostPhys.2.3.019.
- E. Gardner, _The space of interactions in neural network models_, Journal of Physics A: Mathematical and General **21** (1988), 257–270. doi:10.1088/0305-4470/21/1/030.
- E. Gardner, The space of interactions in neural network models, _J. Phys. A: Math. Gen._ **21** (1988), no. 1, 257–270. doi:10.1088/0305-4470/21/1/030.
- F. Guerra, _Broken replica symmetry bounds in the mean field spin glass model_, Communications in Mathematical Physics **233** (2003), 1–12. doi:10.1007/s00220-002-0773-5.
- S. Ghirlanda and F. Guerra, General properties of overlap probability distributions in disordered spin systems. Towards Parisi ultrametricity, _J. Phys. A: Math. Gen._ **31** (1998), no. 46, 9149–9155. doi:10.1088/0305-4470/31/46/006.
- G. H. Hardy, J. E. Littlewood, and G. Pólya, _Inequalities_, second edition, Cambridge University Press, 1952.
- Y. Kabashima, Inference from correlated patterns: a unified theory for perceptron learning and linear vector channels, _J. Phys.: Conf. Ser._ **95** (2008), 012001. doi:10.1088/1742-6596/95/1/012001.
- T. Shinzato and Y. Kabashima, Perceptron capacity revisited: classification ability for correlated patterns, _J. Phys. A: Math. Theor._ **41** (2008), 324013. doi:10.1088/1751-8113/41/32/324013.
- B. S. Kashin, Diameters of some finite-dimensional sets and classes of smooth functions, _Math. USSR-Izv._ **11** (1977), no. 2, 317–333. doi:10.1070/IM1977v011n02ABEH001719.
- J. Ko, The Crisanti–Sommers formula for spherical spin glasses with vector spins, preprint, 2019. arXiv:1911.04355.
- E. Lerner, G. Düring and M. Wyart, _Low-energy non-linear excitations in sphere packings_, Soft Matter **9** (2013), 8252–8263. doi:10.1039/C3SM50515D.
- F. Mezzadri, How to generate random matrices from the classical compact groups, _Notices Amer. Math. Soc._ **54** (2007), 592–604. arXiv:math-ph/0609050.
- A. Montanari, Y. Zhong and K. Zhou, _Tractability from overparametrization: The example of the negative perceptron_, Probability Theory and Related Fields **188** (2024), 805–910. doi:10.1007/s00440-023-01248-y. arXiv:2110.15824.
- M. Bayati and A. Montanari, _The LASSO risk for gaussian matrices_. Author manuscript, Appendix F, Theorem F.1. .
- J.-C. Mourrat, _Un-inverting the Parisi formula_, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **61** (2025), no. 4, 2709–2720. doi:10.1214/24-AIHP1487. Preprint (2023), arXiv:2308.10715v2.
- H.-B. Chen and J.-C. Mourrat, On the free energy of vector spin glasses with nonconvex interactions, _Probab. Math. Phys._ **6** (2025), no. 1, 1–80. doi:10.2140/pmp.2025.6.1. arXiv:2311.08980v3.
- J.-C. Mourrat, Nonconvex interactions in mean-field spin glasses, _Probab. Math. Phys._ **2** (2021), no. 2, 281–339. doi:10.2140/pmp.2021.2.281.
- J.-C. Mourrat, The Parisi formula is a Hamilton–Jacobi equation in Wasserstein space, _Canad. J. Math._ **74** (2022), no. 3, 607–629. doi:10.4153/S0008414X21000031.
- J.-C. Mourrat, Free energy upper bound for mean-field vector spin glasses, _Ann. Inst. Henri Poincaré Probab. Stat._ **59** (2023), no. 3, 1143–1182. doi:10.1214/22-AIHP1292.
- OpenAI, _The free energy of the spherical random perceptron_, OpenAI Math Release preprint OAI:The-free-energy-of-the-spherical-random-perceptron-September-24-2026, 2026.
- D. Panchenko, _A connection between the Ghirlanda–Guerra identities and ultrametricity_, The Annals of Probability **38** (2010), 327–347, Theorem 2(a). doi:10.1214/09-AOP484.
- D. Panchenko, _On the Dovbysh–Sudakov representation result_, Electronic Communications in Probability **15** (2010), 330–338. doi:10.1214/ECP.v15-1562.
- D. Panchenko, _The Parisi ultrametricity conjecture_, Annals of Mathematics **177** (2013), 383–393. doi:10.4007/annals.2013.177.1.8.
- J.-C. Mourrat and D. Panchenko, Extending the Parisi formula along a Hamilton–Jacobi equation, _Electron. J. Probab._ **25** (2020), no. 23, 1–17. doi:10.1214/20-EJP432.
- D. Panchenko, A connection between the Ghirlanda–Guerra identities and ultrametricity, _Ann. Probab._ **38** (2010), no. 1, 327–347. doi:10.1214/09-AOP484.
- D. Panchenko, On the Dovbysh–Sudakov representation result, _Electron. Commun. Probab._ **15** (2010), no. 31, 330–338. doi:10.1214/ECP.v15-1562.
- D. Panchenko, The Parisi ultrametricity conjecture, _Ann. of Math._ (2) **177** (2013), no. 1, 383–393. doi:10.4007/annals.2013.177.1.8.
- D. Panchenko, Free energy in the mixed $`p`$-spin models with vector spins, _Ann. Probab._ **46** (2018), no. 2, 865–896. doi:10.1214/17-AOP1194.
- D. Panchenko, Free energy in the Potts spin glass, _Ann. Probab._ **46** (2018), no. 2, 829–864. doi:10.1214/17-AOP1193. arXiv:1512.00370v3.
- S. Franz and G. Parisi, _The simplest model of jamming_, Journal of Physics A: Mathematical and Theoretical **49** (2016), 145001. doi:10.1088/1751-8113/49/14/145001. arXiv:1501.03397.
- V. A. Marchenko and L. A. Pastur, _Distribution of eigenvalues for some sets of random matrices_, Mathematics of the USSR–Sbornik **1** (1967), 457–483. doi:10.1070/SM1967v001n04ABEH001994.
- G. Györgyi and P. Reimann, Beyond storage capacity in a single model neuron: continuous replica symmetry breaking, _J. Stat. Phys._ **101** (2000), 679–702. arXiv:cond-mat/0003360.
- D. Ruelle, A mathematical reformulation of Derrida's REM and GREM, _Comm. Math. Phys._ **108** (1987), no. 2, 225–239. doi:10.1007/BF01210613.
- M. Stojnic, _Another look at the Gardner problem_, preprint (2013). arXiv:1306.3979.
- E. Bolthausen and A.-S. Sznitman, _On Ruelle's probability cascades and an abstract cavity method_, Communications in Mathematical Physics **197** (1998), 247–276. doi:10.1007/s002200050450.
- E. Bolthausen and A.-S. Sznitman, On Ruelle's probability cascades and an abstract cavity method, _Comm. Math. Phys._ **197** (1998), no. 2, 247–276. doi:10.1007/s002200050450.
- D. Panchenko and M. Talagrand, On one property of Derrida–Ruelle cascades, _C. R. Math. Acad. Sci. Paris_ **345** (2007), no. 11, 653–656. doi:10.1016/j.crma.2007.10.035.
- M. Shcherbina and B. Tirozzi, Rigorous solution of the Gardner problem, _Comm. Math. Phys._ **234** (2003), no. 3, 383–422. doi:10.1007/s00220-002-0783-3.
- M. Wyart, _Marginal stability constrains force and pair distributions at random close packing_, Physical Review Letters **109** (2012), 125502. doi:10.1103/PhysRevLett.109.125502.
- G. Parisi and F. Zamponi, _A proof of an identity for the critical exponents of jamming_, Journal of Statistical Mechanics: Theory and Experiment (2026), 073301. doi:10.1088/1742-5468/ae7bd7. arXiv:2606.03300.
- A. Montanari and K. Zhou, _Which exceptional low-dimensional projections of a Gaussian point cloud can be found in polynomial time?_, preprint, 2024, version 3, October 17, 2025. arXiv:2406.02970v3.
