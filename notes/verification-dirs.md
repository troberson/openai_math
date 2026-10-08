# What the `verification` column counts

Measured 2026-10-06 by reading the files each bundle ships. No `lake`, `lean`, or comparator run, and
**no verification program was executed** — see "Not checked".

The ledger's `verification` column counts `preprints/<slug>/verification/` directories: **30 dirs over
22 families** (059, 067, 087, 090, 101, 107, 119, 153, 187, 189, 205, 210, 229, 266, 268, 269, 272,
348, 352, 361, 367, 371). `inputs` counts 4 `INPUTS.md` (057, 157, 251, 259); `covmd` counts 2
`verification/COVERAGE.md`, both in family 348.

A verification bundle is a **finite-arithmetic certificate**, not a proof check. The bundles that
document themselves say so:

| Fam | Bundle | Scope limit, verbatim |
|---|---|---|
| 348 | `manifest.json` (both dirs) | "Supporting exact arithmetic package only; no theorem certification claim" |
| 348 | `COVERAGE.md` (both dirs, byte-identical) | "The verifier checks finite polynomial, coefficient, and rational-integral claims, not the manuscript's geometric or analytic reductions." |
| 268 | `README.md` | "They verify finite scalar, thermal, and trial calculations, not the analytic proof." · "The programs embed their finite inputs and do not read the stored JSON files as premises." |
| 361 | `README.md` | "This optional check performs exact integer spectral-selection comparisons for ambient dimension `n=16` and cutoff `k=50000`. It does not construct the metric or verify the complete counterexample." |
| 090 | `An-atomic-certificate…/README.md` | "The checker verifies the finite blocks, parameter-polytope bounds, envelope comparisons, and Bernstein tables, not the article's analytic propagation and energy-transfer arguments." · "`CERTIFICATE.json` identifies the checker and documented command; it is static metadata, not an execution receipt." |
| 090 | `A-sharp-Fourier-certificate…/README.md` | "The main command checks the finite matrix, residual, Bernstein, and scalar comparisons. The analytic quadrature, continuum, and infinite-tail arguments remain in the article." |
| 090 | `Universal-optimality…/README.md` | "These commands check finite arithmetic, not the manuscript's analytic reductions." · "They do not execute the separate floor-rounded matrix construction." |
| 090 | `Triangular-minimality…/README.md` | "`data/certificate-record.txt` … is evidence for readers, not an input to the runner." · "The wrapper does not read the manuscript." |
| 107 | `README.md` | "This command does not run the numerical checks." (the inventory check verifies byte counts and SHA-256 only) |

So a `verification` value of 1 is evidence that a family ships a reproducible **finite computation**,
and the bundle's own text states that the analytic/geometric reductions are outside it. It is not
evidence that the theorem was checked.

## How documented the bundles are

- **12 of 30** ship a `README.md` with a run command and success criteria: 087, 090 (×4), 107, 119,
  229, 268, 348 (×2), 361. **18 ship no README** — a command is not recoverable from the bundle.
- **2 of 30** ship `manifest.json` (both 348 dirs) with `scope`, `main_command`, `network_required`,
  `third_party_dependencies`, and per-file sha256. The other 28 have no manifest.
- **2 of 30** ship `COVERAGE.md` (both 348 dirs).
- Success criteria are bundle-specific and deliberately narrow: exit status 0 **plus** a printed
  marker (`PASS`, `"all_passed": true`, `"status": "pass"`, `passed: true` with a stated record
  count). Two READMEs warn that files on disk prove nothing: "A failed run may leave older or partial
  result files; those files do not establish success for that run" (090) and "file presence alone is
  not success" (090).
- **8 of the 12** READMEs insist Python assertions stay enabled (`-O`, `-OO`, `PYTHONOPTIMIZE`
  forbidden): 087, 090 (×2), 119, 229, 268, 361. **2** reject `NDEBUG` in the C++ programs (090
  `Triangular-minimality`, 229). The checks live inside `assert` statements, so an optimized run is a
  no-op. The two 348 bundles are the only ones that say the opposite — "Checks remain active under
  Python `-O`" — because their verifier compares output rather than asserting.

## Every bundle and its own entry point (read 2026-10-07)

Measured by `python3 notes/scripts/extract_verification_dirs.py` — report-only; it reads the bundles as
text, runs nothing, and writes nothing. `python3 notes/scripts/verify_verification_dirs.py --mutant`
resolves every anchor in this section, checks every quotation against the line it cites, and re-derives
every count here from the bundles on disk.

A README section names **28** of the **30** bundles: **27** carry `## Verification` and **1** carries
`## Run the verification code` (family 059,
`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/README.md:18`).
**2** bundles ship a `verification/` tree their README never mentions, and both are family 269:

- `preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/verification/rows.txt`
- `preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/verification/rows.txt`

Each is 20 lines and 1436 bytes, and the two files are **byte-identical**. Neither bundle ships a
program, a manifest, a README, or any second file: for these two the ledger's `verification` column is
the only machine-readable pointer. The manuscripts do print the data —
`\lstinputlisting{../verification/rows.txt}` at
`preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/build/sections/08-arithmetic.tex:21`
and the same include at
`preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/build/appendices/retained-blocks.tex:619`
— so what family 269 ships is a **printed data table**, not a runnable check.

### The entry-point rule

Applied in order per bundle; the first rule that fires is the entry point:

1. `verification/README.md`
2. `verification/<sub>/README.md` (alphabetically first)
3. `verification/<sub>/README.txt`
4. a `main_command` / `checker` / `command` string in a JSON manifest named `manifest.json`,
   `CERTIFICATE.json`, `CERTIFICATE-SUPPORT-MANIFEST.json`, `BUILD-INPUTS.json`, or
   `package-manifest.json`
5. a top-level `verification/` script whose name begins `verify`, `reproduce`, `run`, or `check`
6. none

Over the 30 bundles: **12** top-level `README.md`, **6** a subdirectory `README.md`, **5** a top-level
script by name, **1** a subdirectory `README.txt`, **6** with **no entry point**.

Rule 4 fires for **0** bundles — the two family-348 dirs that declare `main_command` are claimed by
rule 1 first. The 6 with no entry point are the two 269 dirs above plus 352, 059, 189 and 272; those
four **are** named by a README section, which supplies the command itself, so for them the run command
lives in the manuscript README and not in the bundle.

| Fam | Bundle | Entry point | What the entry point says, verbatim |
|---|---|---|---|
| 269 | `A-Fock-space-inequality…` | **none** | One file, `verification/rows.txt`; the manuscript typesets it (`preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/build/sections/08-arithmetic.tex:21`). |
| 268 | `A-boundary-field-gap…` | `verification/README.md` | *"They verify finite scalar, thermal, and trial calculations, not the analytic proof."* (`preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/verification/README.md:54`) |
| 361 | `A-counterexample-to-integer-degree…` | `verification/README.md` | *"It does not construct the metric"* (`preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/verification/README.md:4`); command at `preprints/A-counterexample-to-integer-degree-harmonic-dimension-comparison-September-25-2026/verification/README.md:11`. |
| 352 | `A-finite-time-singularity…` | **none** | 3 scripts, no README; the manuscript section runs them and says *"The certificate is silent on success."* (`preprints/A-finite-time-singularity-of-Calabi-flow-on-projective-space-September-24-2026/README.md:40`) |
| 090 | `A-sharp-Fourier-certificate…` | `verification/README.md` | *"A failed run may leave older or partial result files; those files do not establish success for that run."* (`preprints/A-sharp-Fourier-certificate-for-planar-circle-packing-September-23-2026/verification/README.md:14`) |
| 101 | `A-sharp-entropy-bound…` | `verification/verify_scalar.py` | *"it is not a formal proof assistant for those calculus statements."* (`preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/verification/verify_scalar.py:14`); the run command is a comment at `preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/verification/verify_scalar.py:4`, and `preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/verification/verify_scalar.py:30` says *"Deliberately not assert: verification also works under python -O."* |
| 059 | `Ambiently-homeomorphic…` | **none** | 3 files under `support/` and `validation/`; the `## Run the verification code` section says *"These checks cover the finite arithmetic, not the lattice-theoretic or topological arguments."* (`preprints/Ambiently-homeomorphic-isolated-hypersurfaces-of-multiplicities-two-and-three-September-24-2026/README.md:28`) |
| 090 | `An-atomic-certificate…` | `verification/README.md` | *"`CERTIFICATE.json` identifies the checker and documented command; it is static metadata, not an execution receipt."* (`preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/README.md:13`) |
| 153 | `Arithmetic-classification…` | `verification/verify_degree31.py` | No prose; a 487-line script whose comments state the arithmetic contract — *"strictly less than half the linear term on the disk boundary."* (`preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/verification/verify_degree31.py:171`); command at `preprints/Arithmetic-classification-and-non-Pisot-singularity-for-Bernoulli-convolutions-October-3-2026/verification/verify_degree31.py:5`. |
| 107 | `Complex-Matrix-Multiplication…` | `verification/README.md` | *"This command does not run the numerical checks."* (`preprints/Complex-Matrix-Multiplication-Below-2.258-and-Rectangular-Bounds-September-24-2026/verification/README.md:23`) |
| 189 | `Cycle-clique-Ramsey-numbers` | **none** | 3 scripts and 3 data files under `code/` and `data/`; the manuscript section says of the shipped traces *"they are not separate proof objects for an additional independent minimal validator."* (`preprints/Cycle-clique-Ramsey-numbers-September-25-2026/README.md:26`) |
| 272 | `Entanglement-with-zero-distillable-secret-key…` | **none** | 3 scripts and 3 outputs, no README; the manuscript section runs each script and `cmp`s its output against the shipped file (`preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/README.md:31`). |
| 266 | `Exact-Fourier-certificates…` | `verification/run.py` | *"The verifier differs from the source printed in the paper."* — the wrapper refuses to run unless `verify.py` hashes to a literal written into it (`preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/verification/run.py:15`) |
| 210 | `Foulkes-Conjecture…` | `verification/verify_computations.py` | *"Default / --check is read-only and does not execute either C++ program."* (`preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/verification/verify_computations.py:4`) |
| 119 | `Hellinger-contraction…` | `verification/README.md` | *"These commands check finite arithmetic. The manuscript supplies the analytic argument connecting it to the theorem."* (`preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/verification/README.md:40`) |
| 348 | `Positively-curved-Einstein-four-manifolds` | `verification/README.md` | *"Exact arithmetic verification"* (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/README.md:1`); the bundle's scope is in the 348 section below. |
| 187 | `Snaky-in-21-Maker-moves` | `verification/supporting/route21/README.md` | *"The 21-move certificate"* (`preprints/Snaky-in-21-Maker-moves-September-25-2026/verification/supporting/route21/README.md:1`); two commands, `python3 primary.py` and `python3 independent.py` (`preprints/Snaky-in-21-Maker-moves-September-25-2026/verification/supporting/route21/README.md:6`). |
| 371 | `Stable-Self-Similar-Blowup…` | `verification/certificates/README.md` | *"The verifier does not establish the analytic arguments connecting its finite comparisons to the theorem."* (`preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/verification/certificates/README.md:42`) |
| 107 | `Staggered-extraction…` | `verification/data/README.md` | *"This command verifies the finite parameter bound, not the mathematical extraction proof."* (`preprints/Staggered-extraction-for-exact-matrix-multiplication-over-every-field-September-24-2026/verification/data/README.md:18`) |
| 067 | `The-Campana-Peternell-conjecture…` | `verification/verify.py` | No prose at all: a 167-line script whose checks are `assert` statements over SymPy matrices (`preprints/The-Campana-Peternell-conjecture-in-dimension-six-September-25-2026/verification/verify.py:139`). |
| 087 | `The-Mahler-Conjecture…` | `verification/README.md` | *"The output directory must not exist. `reproduce.py` checks the program hashes"* (`preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/verification/README.md:15`) |
| 229 | `The-Reconstruction-Threshold…Four-State-Potts` | `verification/checks/README.txt` | *"It does not repeat the full C++ traversals."* (`preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/verification/checks/README.txt:29`) |
| 367 | `The-critical-dimension…` | `verification/checks/README.md` | *"This command verifies finite algebra and coefficient comparisons, not the analytic reduction, the correspondence between mathematical formulas and code, or the whole proof."* (`preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/verification/checks/README.md:13`) |
| 229 | `The-exact-reconstruction-threshold…three-state` | `verification/README.md` | *"Do not use Python's `-O` or `-OO` options or define `NDEBUG`."* (`preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/verification/README.md:5`) |
| 268 | `The-periodic-spin-one-Haldane-gap` | `verification/computations/README.md` | *"Verification requires no GPU or network access."* (`preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/verification/computations/README.md:13`) |
| 090 | `Triangular-minimality…` | `verification/README.md` | *"The wrapper does not read the manuscript."* (`preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/verification/README.md:39`) |
| 269 | `Uniform-Stability-of-the-Spherical-Laughlin-Gap` | **none** | One file, `verification/rows.txt`, byte-identical to the other 269 bundle's; typeset at `preprints/Uniform-Stability-of-the-Spherical-Laughlin-Gap-October-5-2026/build/appendices/retained-blocks.tex:619`. |
| 205 | `Universal-Tensor-Squares…` | `verification/computation/README.md` | *"These commands check finite character and capacity cases, not the article's general recurrence, pruning, or analytic arguments."* (`preprints/Universal-Tensor-Squares-for-Symmetric-Groups-September-24-2026/verification/computation/README.md:21`) |
| 090 | `Universal-optimality-of-the-triangular-lattice` | `verification/README.md` | *"These commands check finite arithmetic, not the manuscript's analytic reductions."* (`preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026/verification/README.md:44`) |
| 348 | `Zero-Plane-Rigidity-for-Einstein-Four-Manifolds` | `verification/README.md` | *"Exact arithmetic verification"* (`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/README.md:1`); the bundle's scope is in the 348 section below. |

**Reading the column against the ledger.** The ledger's `verification` column sums to 30 dirs over 22 families,
and the set of families with `verification` > 0 is exactly the set of families carrying a
`verification/` directory — the join is clean, so the column is a correct *count*. What it is not is a
pointer: for the 6 bundles with no entry point, and for the 2 family-269 bundles in particular, nothing
inside the bundle says how to run it, and for family 269 nothing in the manuscript README says it exists.

## What the 348 bundle checks, and what it omits (read 2026-10-07)

Every count here comes from `python3 notes/scripts/extract_verification_348.py`, which reads the two
bundles as text and runs nothing. `python3 notes/scripts/verify_verification_dirs.py` re-derives those
counts independently, resolves every anchor in this section, and checks every quotation against the
lines it cites; it writes nothing.

**The two dirs are one bundle shipped twice.** Of the 9 files they share, **7 are byte-identical** —
`verify.py` (28,511 B), `polynomial.py`, `results.json` (447,073 B), `COVERAGE.md`,
`dependencies.json`, `portability_check.py`, `portability-results.json` — and **2 differ**:
`README.md` (768 B vs 855 B, the extra bullet naming the scalar script) and `manifest.json`, which
hashes `README.md`. The Zero-Plane dir carries one extra file, `check_scalar_certificates.py`. So the
ledger's `verification` value of 2 for family 348 counts two copies of one arithmetic check, not two
independent checks.

**What the check is.** `verify.py` is 504 lines with 6 `check_*` functions (at lines 157, 170, 271,
334, 373, 397). `--check` recomputes everything and compares the serialized JSON against the shipped
file (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:496`):

```
        require(RESULTS_FILE.read_text(encoding="utf-8") == encoded,
                "Recomputed exact results differ from bundled results.json")
```

A passing run therefore shows that the shipped numbers are reproducible from the shipped code. It does
not compare any number with the manuscript. Shipped counts, from `results.json` in both dirs:
**53** identities, **21** interval certificate rows (**15** reported + **6** supplementary),
**12** triangle certificate rows (**9** carrying a determinant floor), **24** exact-value assertions,
over **41** subinterval records.

**Four things it does not cover.**

1. **The reductions.** `COVERAGE.md` says the verifier checks "finite polynomial, coefficient, and
   rational-integral claims, not the manuscript's geometric or analytic reductions", and the
   manuscript defers to it: *"Its coverage record distinguishes those executed reconstructions from
   the collection identities and geometric reductions proved in the text."*
   (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/build/sections/07-certificates.tex:14`).
   The optional scalar script is explicit about the split: *"The accompanying mathematical proof
   supplies the compactness, separation, calculus, Jacobi comparison, and Sobolev arguments."*
   (`preprints/Zero-Plane-Rigidity-for-Einstein-Four-Manifolds-October-4-2026/verification/check_scalar_certificates.py:14`).
2. **The manuscript-to-literal link.** **9** `scalar_claim` keys name a printed value
   (`eq9.printed_minimum`, `eq9.printed_minimum.endpoint_lower`, `eq22.printed_CBE.8.0`, …) and each
   compares a computed minimum against a rational literal written into `verify.py`. Nothing in the
   bundle parses the manuscript, so the mapping from a printed number in the PDF to that literal is
   made by hand and is not re-checked by the command.
3. **`all_passed` is not an aggregation.** It is assigned unconditionally at the end of `compute()`
   (`preprints/Positively-curved-Einstein-four-manifolds-September-23-2026/verification/verify.py:477`):

   ```
           "all_passed": True,
   ```

   Every check aborts through `require` (13 occurrences) on the
   first failure, and each record is appended with `"passed": True` only after its check passes —
   **151** such occurrences in `results.json`, and no negative record anywhere. `results.json` is a
   transcript of a completed run, not a table of independent verdicts.
4. **The reference is regenerable.** `dependencies.json` ships `regenerate_command:
   python -B verify.py --write`, which overwrites `results.json` beside the script. The file
   `--check` compares against is not fixed by anything outside the bundle.

**Manifest gaps.** Both `manifest.json` files list 8 files, and every listed sha256 and byte count
matches what is on disk (0 mismatches). Neither hashes `manifest.json` itself, and the Zero-Plane
manifest omits `check_scalar_certificates.py` — the only file unique to that directory. That file
imports `sympy` while `dependencies.json` declares `"third_party_dependencies": []`, so the one
undeclared third-party import in family 348 is in the one file the manifest does not list.

**The coverage file names only shipped artifacts.** `COVERAGE.md` points at `results.json`, `verify.py`,
`polynomial.py`, and `README.md`; all four are present in both directories. The family-318 pattern — a
coverage document naming files that do not exist — does not fire here, which is what makes 348's scope
statement safe to quote.

**The method is sufficient, not necessary.** An interval certificate requires every Bernstein
coefficient of the polynomial, on each subinterval, to be at or above a stated floor; a triangle
certificate additionally requires the exact zero pattern to match (`actual_zeros == expected_zeros`).
A Bernstein bound is a sufficient condition for a lower bound, so a bound the bundle cannot certify is
not evidence that the bound is false — and the bundle records only the bounds it chose to certify.

**The bundle self-tests.** `portability-results.json` ships **11** checks, **8** of them negative
tests naming a rejection: **7** whose names end in `rejected` (`altered_saved_results`,
`incorrect_zero_locations`, `violated_coefficient_floor`, `univariate_degree_truncation`,
`triangle_degree_truncation`, `inexact_polynomial_division`, `floating_point_coefficient`) plus
`incorrect_printed_triple_rejected_under_O`, which appends the flag it tests. The other three are
`relocated_run_from_different_cwd`, `optimized_python_checks_remain_active`, and
`original_runtime_files_unchanged`. This is the only bundle among the 30 that demonstrates its own
checks fail on bad input; the report is a shipped artifact, not a run this session performed.

## Requirements, for anyone who wants to run them

Python only, standard library: 348 (×2, Python ≥ 3.10), 361, 090 `An-atomic-certificate`, 268
(scalar + trial programs). Pinned third-party: 090 `A-sharp-Fourier-certificate` and
`Universal-optimality` (`python-flint==0.9.0`); 087 and 119 (SymPy 1.14.0); 268 thermal program
(NumPy + SciPy). C++ toolchain: 119 (C++17 with signed `__int128`), 229 (g++ C++17, `__int128`,
UBSan), 090 `Triangular-minimality` (g++ C++17, OpenMP, Boost.Multiprecision). 107's inventory check
is Python ≥ 3.9 stdlib. `network_required` is false where stated; 090 and 348 need the full paper
source tree present because manifests hash `build/` sources.

## Not checked

- **Nothing was executed.** No `verify.py`, `reproduce.py`, or certificate program was run, so no
  family here has a passing run in this record. Running them needs a virtualenv (system Python is
  PEP 668 externally managed) and, for four bundles, a C++17 toolchain.
- The 18 undocumented bundles were counted, not read for scope; their limits are unstated, not known
  to be absent.
- Certificate *contents* were not audited: no check that a bundle's finite claims are the ones the
  manuscript uses, and no recomputation of any bound.
- `results.json`/`CERTIFICATE.json`-style stored outputs were not compared with freshly generated
  output. Several READMEs state the stored files are not premises; that was taken at face value.
- Family 318's `SUPPORT-COVERAGE.md` is a different case: it names a `support/r-ce/` bundle,
  `BUILDING.md`, and `SUPPORT-COVERAGE.json` that do not exist on disk.

Specific to the 348 section above:

- The shipped `portability-results.json` is the release's own report. Its 11 checks, including the 8
  negative tests, were **read, not executed** here, so "the bundle demonstrates its checks fail on bad
  input" is a claim about the artifact, not an observation made in this session.
- The 9 printed-value literals in `verify.py` were **not** compared with the numbers printed in the two
  manuscripts. The hand-transcription gap is described from the code's shape; no mismatch was looked
  for, so none is recorded.
- Manuscript references to the bundle were found by matching `verify.py` or `COVERAGE.md` in
  `build/**/*.tex` — 3 hits. A reference phrased without either token would not have been found.
- `check_scalar_certificates.py` was read for its imports and its scope sentence, not audited line by
  line; its SymPy use is reported from the import, not from what it computes.
