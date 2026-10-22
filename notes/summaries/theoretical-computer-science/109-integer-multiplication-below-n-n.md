Notes / Summaries / Theoretical computer science / [Family 109](../../index/theoretical-computer-science/109-integer-multiplication-below-n-n.md)

# 109 — Integer multiplication below $n\log n$

## Undergraduate summary

For sixty years the fastest way to multiply very large numbers was the
Schönhage–Strassen algorithm, and it was widely believed that nothing could
beat $n \log n$ bit operations for $n$-bit inputs. This paper proves that
belief false. It builds one specific machine — a fixed finite-alphabet
Turing machine with a fixed finite number of tapes, written out as a finite
table of rules — that multiplies two $n$-bit integers in time
$O(n (\log n)^{1-\kappa})$, where $\kappa = 2^{-182}$. [S2:28]

The exponent is unimaginably small ($\kappa \approx 2.4 \times 10^{-55}$),
so the machine is slower than the best known algorithms for any realistic
input. The point is not speed. It is that the exponent is strictly below 1,
so the $n \log n$ barrier is broken, and the theorem "refutes an eventual
$\Omega(n \log n)$ lower bound for every fixed multiplication machine in
this model." [S3:34-36]

The authors are explicit that this is a complexity result, not an
engineering one: "The bound is asymptotic through all input lengths. The
constants and thresholds in the construction are extremely large; the
algorithm is intended to establish a bit-complexity bound." [S3:32-34]

The trick is a two-stage argument. The first stage is an algorithm in a
restricted streaming model, where data is read in a fixed number of passes
over fixed streams. The second stage converts that algorithm into a real
Turing machine. The saving comes from two tape procedures: "The first
procedure interchanges two disjoint contiguous address fields" of $u$ bits
in a fixed cost $O(V u^\tau)$ with $\tau < 1$ [S3:59-61], and the second
applies a butterfly operation simultaneously on selected coordinate bits.
"Each record is a polynomial with complex fixed-point coefficients, and"
the operation acts coefficientwise. [S3:70-72]

## Graduate summary

**The model.** "A machine has one fixed finite alphabet and one fixed
finite number of one-dimensional tapes. A step reads and writes at most one
cell on each tape and moves each head by at most one cell." [S5:4-6] The
logical volume $V$ counts stored data bits; "Work tapes and duplicate
streams are charged in time but do not increase" $V$ in recurrences.
[S5:24-25] Every elementary scan — digit permutations, digit moves,
splitting on a digit, cyclic row merging — is proved to cost $O(V)$, and
"The bounds include shape preparation, counter initialization and resets,
and returning or clearing the visited portions of work tapes."
[S5:76-78]

**The setup.** "Splitting the inputs into radix digits reduces
multiplication to convolution of short integer coefficients." [S3:40-41]
The Gaussian-resampling reduction of Harvey and van der Hoeven replaces the
Fourier transforms by multidimensional transforms whose axis lengths are
powers of two; powers of $y$ then serve as roots of unity in the remaining
axes, and multiplying by such a root is a signed shift. "In this
representation, the transform calculation consists of address
rearrangements, signed shifts, and two-point butterfly operations."
[S3:52-53] Scanning a $\Theta(n)$-bit array at each of $\Theta(\log n)$
levels already costs $\Theta(n \log n)$, so "We therefore need savings in
both movement and arithmetic. Two tape procedures supply them" [S3:56-57]
— and "Although its final effect is an exact permutation, its intermediate
steps form pointwise XOR combinations of data. The final permutation is
exact for arbitrary initial auxiliary values." [S3:62-64]

**Where the power saving comes from.** "Each procedure arises from its own
fixed linear network that exchanges two banks of values, with prescribed
signs, and restores every auxiliary value." [S3:84-86] "A wire's fixed
place in the network is called its role." [S3:86] Rows are distributed
cyclically among the $W$ roles, and a scalar gate is applied pointwise to
matching addresses. The finite construction attaches subspaces of a fixed
$m$-dimensional space to gates and terminals: "The construction uses
three-element subsets: gather and scatter create coefficients depending on
intersection size, and auxiliary wires cancel the unwanted
coefficients." [S3:127-130] "Orthogonality of the corresponding indicator
vectors permits the subspace assignments." [S3:130-131] The decisive
property is that the total number $s$ of smaller calls satisfies $s < Wm$:
a recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on
streams of volume $V/W$, so dividing by volume and multiplying the parameter
by $m$ increases the recursive contribution by $s/W < m$. "This strict
inequality is the source of the power saving." [S3:138-139] The address
coordinates are changed "by whole-chunk moves and controlled shifts,
followed by a deterministic correction of the explicitly identified
exceptional addresses." [S3:140-143]

**The layers.** The fast simultaneous synthetic butterfly layer applies a
complex network to a common butterfly layer on several axes at once; "Two
consequences explain the layout." [S6:26] The polynomial length grows
faster than every fixed power of $p$, so a scan of a record pays for
polynomial work on its address, and $K/\log p \to \infty$, which makes the
exceptional set in a packed change of address bits small enough to repair by
sorting. The target cost is $O(V d^{\lambda'})$ with $\lambda' < 1$,
"whereas separate butterfly factors would require $D$ whole-array passes."
[S6:31-32] "We implement those changes by moving whole address chunks.
Splitting complete rows among the network's wire roles then reduces the
volume of each recursive call." [S6:37-40] Grouped packed rectangles
generalize the rectangular layout so a supplied descriptor lists groups with
different spectator lengths: "Each group is a complete rectangle, so the
full rectangular algorithm, including its deterministic repair, can be
applied to one group at a time." [S9:7-9] "The only additional work is
reading the group descriptors and passing consecutive groups through the
same local tapes." [S9:9-10]

**The assembled bound.** The assembly section lists nine normalized costs
whose dominant powers of $p$ have margins below one; "Direct substitution
gives" $g_2 = 2^{-181}$, $g_3 = 2^{-129}$, $g_4 > 2^{-51}$, $g_7 = 2^{-75}$,
so $\min_i g_i = 2^{-181} = 2\kappa$. [S7:861-867] "This explicit slack
will cover any remaining fixed power of" $\log p$. [S7:866-867] The
axis-exposure bookkeeping is characteristic: the machine can "peel a single
excess bit when widths differ by one, exchange their equal-width parts, and
restore the bit." [S7:887-888]

**Closing the product.** "The remaining proof places these procedures
inside the multiplication reduction and accounts for every change of
representation." [S3:147-148] The radix-digit coefficient list is placed on
a product of distinct prime cyclic axes by a Chinese-remainder map that
preserves convolution; Bluestein's chirp identity converts the middle
transform into normalized cyclic convolution; a phase twist changes the last
cyclic coordinate into a polynomial modulo $y^r + 1$. "Finally, the source
permutation retained during resampling cancels across the two forward source
transforms, their pointwise product, and the opposite-sign transform."
[S3:170-172] "A compatible choice of rational parameters makes all terms in
its cost table fit" the main theorem. [S3:175-176]

**The transposition consequence.** Harvey and van der Hoeven prove that any
multiplication machine with worst-case cost $M(m)$ yields a fixed
multitape transposition machine with cost $O(M(m) + m \lg\lg\max(n_1,n_2))$.
[S8:8-10] Under the $(\lg m)^{1-\kappa}$ bound the second term is
$o((\lg m)^{1-\kappa})$, so an $n \times n$ binary matrix can be transposed
in $O(n^2 (\lg n)^{1-\kappa})$ time; "Dimensions equal to one cause no
exception, since our convention gives" $\lg 1 = 1$. [S8:47-48] The
interface plumbing is spelled out: "it uses standard binary representations
of the operands and product." [S8:23-24] "This fixes a canonical binary
representation of the product." [S8:30] If a tape orientation requires
reversal, "read the stored word backward while writing it forward on a
spare tape." [S8:31-32]

## History of the conjecture

Karatsuba's recursive construction, published jointly with Ofman in 1962,
gave a binary multiplication circuit of size $O(n^{\log_2 3})$
[S4:4-6]; "Toom's subsequent use of polynomial evaluation and
interpolation gave circuit size" $n \exp(O(\sqrt{\log n}))$ [S4:6-8], and
"Cook adapted Toom's method to the Turing-machine setting"
[S4:10-11]. In the multitape model, the 1971 Schönhage–Strassen paper
established $O(n \log n \log\log n)$; it is *Schnelle Berechnung von
Kettenkatastrophen*, Acta Informatica 1(2), 185–193. [S10:131-138]

Fürer improved the bound to $n \log n \, 2^{O(\log^* n)}$ in 2007; "De,
Kurur, Saha and Saptharishi developed a modular-arithmetic route to the
same scale" [S4:21-22]; "Later improvements made the exponential factor"
$8^{\log^* n}$ and then $4^{\log^* n}$ [S4:23-24]; and "Harvey and van der
Hoeven proved the unconditional" $O(n \log n)$ bound [S4:25-26], in *Integer
multiplication in time $O(n \log n)$*, Annals of Mathematics 190(2),
503–544. [S10:14-21]

The manuscript is careful about which model each bound lives in: "The
multitape bounds just cited concern that fixed model." [S4:28] Linear-time
multiplication on storage-modification machines, and a smaller-than-$\log n$
factor in a unit-cost RAM model with polynomial preprocessing, are both
named, and "Neither result establishes the bound in the fixed finite-tape
model of" the main theorem. [S4:33-34]

The transform machinery is inherited: "The transform methods behind these
bounds also underlie the present construction." [S4:36-37] "More
specifically, the proof adapts Harvey and van der Hoeven's
Gaussian-resampling identity, contraction bounds, and short-convolution
procedures" [S4:50-52]; "Their framework already permits arbitrary
dimension. Here the source and target permutations remain in the transform
identity, while the faster tape procedures perform the required axis
movements." [S4:53-55] Calls to the established $O(n \log n)$ multiplier
are ordinary subroutine calls, and "they do not invoke the improved theorem
recursively." [S4:61-62] Pippiger's 1980 *On the complexity of
multiplication* (Acta Informatica 13(4), 315–324) [S10:113-120] and
Lecerf's 1969 *Une méthode de transposition. Applications to certain
multiplications* (Mathematical Machines and Perception 1(3), 15–24)
[S10:122-130] are the two ancestors the construction leans on for the
fixed-tape side.

The release dates the manuscript September 23, 2026 and lists OpenAI as author [S1:5], typesetting the title as "Integer multiplication below" with the logarithm in math [S1:12]. Its own entry states the result as a disproof: the machine
multiplies "on one fixed finite-alphabet Turing machine with finitely many
one-dimensional tapes" [S11:296], and its index line repeats the same
phrasing [S12:2695]. The release does not mention the matrix-transposition
consequence; that is the manuscript's own section 10.

## Consequences

The main theorem's companion corollary extends the same exponent to two
more operations: "There are deterministic machines with fixed finite
alphabets and fixed finite numbers of one-dimensional tapes performing the
following tasks" in $O(n (\lg n)^{1-\kappa})$ worst-case time — exact
division, returning quotient and remainder, and integer square root.
[S3:196-198] The route is classical: "The classical Newton reductions
described by" Brent compute reciprocal and square-root approximations at
geometrically increasing precisions, and "Their multiplication costs are
bounded by a geometric sum controlled by the last precision, and exact
remainder and square tests recover the required integer answers."
[S3:208-213]

Three things follow. First, the $n \log n$ optimality conjecture for the
multitape bit model is false, so any future lower-bound program for
multiplication must be stated in a model that excludes this construction.
Second, matrix transposition inherits the same exponent through the Harvey–
van der Hoeven interface, so the two problems are separated on one machine.
Third, the method is a template: the streaming-model cost bound and the
simulation are separate theorems, so any future streaming algorithm below
$n \log n$ can be pushed through the same conversion.

The caveat is the constant. $\kappa = 2^{-182}$ is the residue of a chain of
fixed inequalities [S7:866-867], not a practical improvement, and the
machine's transition table is finite but astronomically large.

## Sources

| # | File | Lines | Role |
| --- | --- | --- | --- |
| S1 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/README.md` | 17 | release title, author, date, citation |
| S2 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/main.tex` | 51 | abstract |
| S3 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/00-introduction.tex` | 216 | main theorem, corollary, proof outline |
| S4 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/01-history.tex` | 164 | prior bounds and inherited methods |
| S5 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/02-streams.tex` | 208 | machine model and elementary scans |
| S6 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/05-layers.tex` | 996 | simultaneous butterfly layers |
| S7 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/08-assembly.tex` | 1007 | the assembled cost bound |
| S8 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/10-transposition.tex` | 48 | the matrix-transposition consequence |
| S9 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/11-grouped-rectangles.tex` | 160 | grouped packed rectangles |
| S10 | `preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/references.bib` | 301 | the prior literature cited |
| S11 | `overview.tex` | 859 | the release's own entry |
| S12 | `CONTENTS.md` | 9142 | the release's own index line |

## Links

- [S1](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/README.md)
- [S2](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/main.tex)
- [S3](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/00-introduction.tex)
- [S4](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/01-history.tex)
- [S5](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/02-streams.tex)
- [S6](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/05-layers.tex)
- [S7](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/08-assembly.tex)
- [S8](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/10-transposition.tex)
- [S9](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/sections/11-grouped-rectangles.tex)
- [S10](../../../preprints/Integer-multiplication-below-n-log-n-September-23-2026/build/references.bib)
- [S11](../../../overview.tex)
- [S12](../../../CONTENTS.md)

## Bibliography

**27 entries** from `references.bib`:
- Karatsuba, A., Ofman, Yu.. *Multiplication of Many-Digital Numbers by Automatic Computers*. (1962) [KaratsubaOfman1962]
- Toom, A. L.. *The Complexity of a Scheme of Functional Elements Simulating the Multiplication of Integers*. (1963) [Toom1963]
- Sch{\"o}nhage, Arnold, Strassen, Volker. *Schnelle {Multiplikation} gro{\ss}er {Zahlen}*. (1971) [SchonhageStrassen1971]
- F{\"u}rer, Martin. *Faster Integer Multiplication*. (2007) [Furer2007]
- F{\"u}rer, Martin. *Faster Integer Multiplication*. (2009) [Furer2009]
- Nussbaumer, H. J.. *Fast Polynomial Transform Algorithms for Digital Convolution*. (1980) [Nussbaumer1980]
- Nussbaumer, H. J., Quandalle, P.. *Computation of Convolutions and Discrete {Fourier} Transforms by Polynomial Transforms*. (1978) [NussbaumerQuandalle1978]
- Dutt, A., Rokhlin, V.. *Fast {Fourier} Transforms for Nonequispaced Data*. (1993) [DuttRokhlin1993]
- Rosser, J. Barkley, Schoenfeld, Lowell. *Approximate Formulas for Some Functions of Prime Numbers*. (1962) [RosserSchoenfeld1962]
- De, Anindya, Kurur, P. P., Saha, Chandan, Saptharishi, Ramprasad. *Fast Integer Multiplication Using Modular Arithmetic*. (2013) [DeKururSahaSaptharishi2013]
- … and 17 more
