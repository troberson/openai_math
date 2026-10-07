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
