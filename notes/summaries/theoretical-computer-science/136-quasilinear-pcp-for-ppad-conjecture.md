Notes / Summaries / Theoretical computer science / [Family 136](../../index/theoretical-computer-science/136-quasilinear-pcp-for-ppad-conjecture.md)

# 136 — The quasilinear PCP-for-PPAD conjecture

## Undergraduate summary

PPAD is the class of search problems whose solutions are guaranteed by a
parity argument: in a directed graph where every node has at most one
predecessor and one successor, if you start at a source, you must end
somewhere else. Its canonical problem, "End-of-Line, asks for an endpoint
other than a specified source, when the graph is described by predecessor
and successor circuits." [S3:5-6] Papadimitriou defined the class in 1994,
in *On the Complexity of the Parity Argument and Other Inefficient Proofs of
Existence* [S5:198-204], and it is the class that contains Nash equilibrium.

A PCP theorem says a proof can be checked by reading a few bits. For NP
this was proved in 1992. For PPAD, Babichenko, Papadimitriou and Rubinstein
conjectured the analogue in 2016: "Babichenko, Papadimitriou, and
Rubinstein formulated the PCP-for-PPAD conjecture as a quasilinear reduction
from End-of-Line to generalized circuits in which both the allowed numerical
error and the allowed fraction of violated gates are positive
constants" [S3:19-22]. A generalized circuit is a network of gates over
numbers in $[0,1]$; "Generalized circuits provide another useful language
for this class: a solution assigns real values in $[0,1]$ to wires and
approximately satisfies local arithmetic, comparison, and Boolean
constraints." [S3:6-9]

The hard part is the word "robust". "The failure fraction is the essential
robustness requirement: the decoder must succeed even if an adversary
chooses which constraints to violate." [S3:23-24] And the size must be
quasilinear: "The quasilinear size requirement is a separate restriction on
the reduction." [S3:25] "Ordinary polynomial-time PPAD-hardness, even with
constant numerical error, does not provide it." [S3:26-27]

This paper proves the conjecture. "We give a positive resolution of the
quasilinear PCP-for-PPAD conjecture." [S3:48] The main theorem produces
fixed constants $\eps, \delta$, a fixed polynomial, and two deterministic
algorithms $R$ and $D$ such that an End-of-Line instance of length $N$
becomes a generalized circuit of encoding length at most
$A N \lceil \log_2(N+2) \rceil^b$, and any assignment that fails a
$\delta$ fraction of gates still decodes to a solution. "The conclusion
about $D$ is universal over the locations and values of the failed
gates." [S3:174-176]

## Graduate summary

**The definitions.** End-of-Line is a pair of Boolean circuits $S, P$ with
$P(0^n) = 0^n$, $S(0^n) \ne 0^n$, $P(S(0^n)) = 0^n$; a solution is a string
$v \ne 0^n$ with $P(S(v)) \ne v$ or $S(P(v)) \ne v$. [S3:71-87] A
generalized circuit has one output and at most two inputs per gate, cycles
allowed, parameters binary-encoded rationals in $[0,1]$, and five arithmetic
gate types (Constant, Scale, Copy, Add, Subtract) plus Less, Or, And, Not,
each $\eps$-satisfied by an implication. [S3:89-126] An acceptable
assignment is rational, of encoding length at most $p(M)$, and
$\eps$-satisfies at least $(1-\delta)|T|$ gates; "Failed gates may violate
their relations arbitrarily, but all their nodes still have one globally
consistent value in $[0,1]$." [S3:132-134] The Boolean predicates make the
error parameter nonmonotone: "increasing $\eps$ can activate an antecedent
that was previously vacuous." [S3:137-138] The authors use one actual
tolerance throughout, and their later upper bounds "do not reclassify a
satisfied Boolean gate at a larger tolerance." [S3:141-142]

**The geometry.** "We begin with the geometric target of the reduction.
Replace the End-of-Line graph by a locally evolving directed graph with a
known source, no isolated vertices, and the same endpoint-decoding
property." [S3:183-185] Each vertex is a separated binary word; in the box
$[-1,2]^{4m}$, "each edge $u\to v$ traces a polygon that first changes a
copy of $E_u$ to $E_v$, changes a repeated control bit, updates the other
copy, and resets the control bit." [S3:188-190] Rounded corners join the
polygons into paths, and "Every other path endpoint encodes an End-of-Line
answer." [S3:193] A bounded displacement field $v$ on the box uses the
directed tangent and inward normal close to a path and a fixed direction
farther away, so the clipped move has norm at least a fixed multiple of the
step outside a fixed neighborhood of the endpoints. The catch: "The proof
must also provide local numerical access to the field: it cannot inspect
the entire encoded graph when computing one coordinate of $v$."
[S3:203-205]

**The two scales.** "The present reduction needs two further properties
simultaneously: quasilinear total storage and robustness to an arbitrary
fixed fraction of failed gates." [S3:209-211] The outer scale encodes
vertex words and program traces by a constant-rate, constant-distance,
constant-locality code on a square grid. Rather than testing polynomial
identities directly, "encode polynomial remainders recording the equation
residuals, and retain certificates for the intermediate products and linear
computations that produce them." [S3:235-237] "On exact codewords, a
nonzero remainder differs from zero at a constant fraction of positions.
The code's commuting row and column constraints also permit whole-row or
whole-column comparisons that give a constant gap for an incorrect
certificate identity." [S3:237-240] All stored components are tested on one
fixed list of neighboring positions, "so more certificates enlarge a symbol
without diluting the gap." [S3:241-242]

Incremental update is the hard part: "One tape edit can change all these
encoded arrays." [S3:244] Before an allowed edit, each retained array's
finite difference is prepared; "Each new increment has lower assigned
polynomial degree in the logical tape entries, so this recursion has bounded
depth. Once preparation is complete, adding the increments updates the
whole retained tuple to its canonical value on the new tape; the
preparation can then be reversed." [S3:248-251] The long linear computation
runs one small group of Fourier frequencies at a time, and "A clock records
progress and scratch space is reused. Thus the preparation's elapsed time
lengthens the represented path rather than the data stored at a
vertex." [S3:256-258]

**One fixed binary port.** "A polynomial-size robust construction applied
directly to an $N$-bit vertex would not give the required size. Instead we
apply it only to the $L$-bit outer symbols." [S3:262-264] The inner
construction supplies one injective encoding of $L$ bits into
$\operatorname{poly}(L)$ bits, with encoding and correction radius chosen
before the number of symbols a local function inspects. "All polynomial
factors in $L$ remain fixed powers of $\log N$." [S3:278-279] The inner
graph is one computation path with blank work at its source and output
$f(s)$ at its sink; polynomial charts encode its tapes and certificates, and
their dependencies are kept separate for each read-only input, "the
input-dependent parts of the source and its first successor have the same
formulas in every later invocation." [S3:288-289]

**Synchronization under gate failures.** The generalized circuit has many
physical replicas of each geometric coordinate; "A fixed-degree expander
average $A$ couples the replicas." [S3:316-317] "First, boundedness of the
update and the expander gap force the replicas close to their means, without
assuming that any decision is correct." [S3:323-325] Randomized threshold
offsets control ambiguous comparisons and the gate-failure budget controls
the circuits containing a failed gate; "the printed circuit assigns
replicas a deterministically enumerated list of fixed tapes of size
polynomial in $L$." [S3:329-331] Expensive Boolean decision gadgets are
shared by groups of output replicas, whose many designated outputs "ensure
that failures concentrated on extraction wires still spoil only a controlled
fraction of the group." [S3:336-338] "An estimate that keeps clipping inside
the replica contraction argument then makes the mean an approximate fixed
point. The displacement lower bound forces $\bar X$ near an endpoint.
Rounding its first block and applying the global binary and outer decoders
yields the required End-of-Line answer." [S3:341-345]

**The imported inputs.** "The outer code uses ternary Goldbach,
fixed-generator prime-quotient expansion, and an effective least-prime
bound" [S3:366-368]; its simultaneous systematic encoders, matrix twists
and joint correction guarantees are proved in the manuscript, because "a
general locally testable code theorem" such as the Dinur–Evra–Livne–Lubotzky–Mozes
result "does not by itself supply this combination." [S3:369-371] "The
inner binary construction uses the corrected scalar line test and two
group-theoretic inputs" [S3:371-373], and "The all-modulus
Margulis--Gabber--Galil bound supplies the local and replica walks"
[S3:374-375]. The inner fields and groups are introduced afresh and are
distinct from the outer construction's. [S3:376-377]

## History of the conjecture

The conjecture's authors are the same people who established the hardness it
was meant to strengthen. Papadimitriou's 1994 paper defined PPAD
[S5:198-204]. Chen, Deng and Teng built the generalized-circuit intermediary
in 2007, in *Settling the Complexity of Computing Two-Player Nash
Equilibria* [S5:281-284], and Daskalakis, Goldberg and Papadimitriou's 2009
*The Complexity of Computing a Nash Equilibrium* [S5:293-300] used the same
arithmetic, comparison and Boolean gadgets. Rubinstein established
constant-error hardness with every gate required to be satisfied, in
*Inapproximability of Nash Equilibrium* [S5:210-217], and his 2016
*Settling the Complexity of Computing Approximate Two-Player Nash
Equilibria* [S5:226-232] combined encoded-path geometry, a locally evolving
End-of-Line, and a holographic proof system; it established quasipolynomial
hardness for constant-error two-player Nash under the exponential-time
hypothesis for PPAD, "while leaving the PCP-for-PPAD conjecture open and
identifying composition as a remaining question" [S3:39-41] The present
reduction's encoded paths and restricted access have "a close predecessor in
Rubinstein's holographic proof system" [S3:207-208].

The 2016 conjecture paper is *Can Almost Everybody be Almost Happy?* [S5:1-7].
The 2024 Pure-Circuit paper, *Pure-Circuit: Tight Inapproximability for
PPAD* [S5:32-41], is the source of the gate conventions the manuscript
adopts, and the 2026 Fisher-markets paper, *Fisher Markets with
Approximately Optimal Bundles and the Need for a PCP Theorem for PPAD*
[S5:16-26], is where the distinction between the original quasilinear
formulation and the weaker positive-failure-fraction version is made
explicit. [S3:29-32] Golowich's 2026 fine-grained work derives sharper
two-player Nash lower bounds for vanishing approximation error under PCP for
PPAD together with the exponential-time hypothesis; "These time lower bounds
retain their additional exponential-time hypothesis; the result here
concerns the conjectured reduction itself." [S3:45-46]

The release's entry says it plainly: "Resolves the quasilinear PCP-for-PPAD
conjecture." [S6:349] Its index line adds the shape of the result: "Such
assignments always exist, giving robust local verification with only
quasilinear size overhead." [S7:3277] The manuscript's own abstract states
the same: "We prove the quasilinear-size PCP-for-PPAD conjecture of
Babichenko, Papadimitriou, and Rubinstein." [S2:49-51] The README names the
manuscript "The PCP-for-PPAD conjecture: a quasilinear reduction"
[S1:12], dated September 25, 2026 [S1:5].

## Consequences

The theorem's decoder is universal, and the totality proof is separate:
"In fact, the soundness argument applies to arbitrary real assignments
meeting the gate-failure budget; rationality is needed for the finite search
relation and its computational decoder. The totality proof supplies an
assignment satisfying every gate on a fixed rational mesh. Neither tolerance
tends to zero with $N$." [S3:175-179]

The applications are the point. "supplies the positive failed-gate premise
in the cited reductions to equilibrium problems" [S4:3-4] — for weak
approximate Nash, relative bimatrix Nash, course allocation, markets with
approximately optimal bundles, stationary equilibria in discounted games,
and approximate Hylland–Zeckhauser allocation. [S3:381-386] "For each
target we state the precise approximation and encoding conventions before
its consequence." [S3:386-388] The preparation is explicit: "The Boolean
tolerance in Definition is nonmonotone. We therefore remove Boolean gates
before reducing numerical tolerances or controlling fan-out." [S4:15-17]

The flagship consequence is polymatrix Nash. "Babichenko, Papadimitriou,
and Rubinstein reduce positive-gap generalized circuits to weak approximate
Nash search, where a fixed fraction of players may have deviation gain
larger than a fixed positive error" [S4:147-150]; "An $n$-player two-action
polymatrix game is specified by an undirected interaction graph and, for
each edge, a pair of rational $2$-by-$2$ payoff matrices." [S4:155-157] The
corollary fixes constants $\eps_{\rm w}, \delta_{\rm w}$ and a polynomial
$p_{\rm w}$ such that finding a rational product profile of encoding length
at most $p_{\rm w}(L)$ with at most $\lfloor \delta_{\rm w} n \rfloor$
players exceeding regret $\eps_{\rm w}$ is PPAD-hard. "No further regret
bound is imposed on the players counted on the left." [S4:184] The game
side is normalized: matrices with entries in $[0,1/3]$ and graphs of
maximum degree at most three, and "The encoding explicitly lists all
players, edges, and matrices, so its length is at least" $n$.
[S4:160-161]

Two things to keep straight. First, "These consequences use fixed-gap
circuit hardness" [S3:391]; the quasilinear complete-output bound is the
additional assertion, so the size claim is what the conjecture added.
Second, the manuscript's own appendix collects "the separate full-macrograph
and unrestricted-product variants; these are not prerequisites for the
fixed-port composition." [S3:363-364]

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/README.md` | 18 | release title, author, date, citation |
| S2 | `preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/main.tex` | 78 | abstract |
| S3 | `preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/sections/01-introduction.tex` | 393 | definitions, main theorem, proof strategy, consequences |
| S4 | `preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/sections/11-weak-nash.tex` | 785 | circuit preparation and the equilibrium corollaries |
| S5 | `preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/references.bib` | 466 | the prior literature cited |
| S6 | `overview.tex` | 859 | the release's own entry |
| S7 | `CONTENTS.md` | 9142 | the release's own index line |

## Links

- [S1](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/README.md)
- [S2](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/main.tex)
- [S3](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/sections/01-introduction.tex)
- [S4](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/sections/11-weak-nash.tex)
- [S5](../../../preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/build/references.bib)
- [S6](../../../overview.tex)
- [S7](../../../CONTENTS.md)
