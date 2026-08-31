# RL194 — exact chronological weighted-speed filter

RL194 closeout proof on the sole high branch
`(v,H,J,d)=(37,0,23,-1)`, conditional on a hypothetical physical extremal
terminal.  No surviving necessary rank or first permitted phase is realized.

## 1. Canonical indexing and the required displacement

Use the verified RL193 constants A, L, B, p, z=L-p, Q=37B mod L,
`K0=2^37`, `Klow=128081997553` and delta.  Write a for the canonical
start of the tau=37 zero prefix, and r for its terminal rank.  Its start
rank is `(r-Q) mod L`, and `a=((r-Q)p) mod L`.

The new rank-order derivation, independently reproduced by direct
substitution in rho, gives both atoms one formula:

`K_a=K0 exp(((Q-r)ln2+a delta)/L)`.                       (1)

For r<Q this follows from start rank r-Q+L and target 2^38; for r>Q it
follows from start rank r-Q and target 2^37.  Q is already excluded.

The exact chronological prefix is

`F_a=sum_(0<=i<a)f_i=3(K_a-K0)`.

It is positive on the lower atom and negative on the upper atom.  RL193's
canonical terminal floor 71 rules out a wrapped terminal in phases 0..36,
and rules out a=0 independently through the excluded rank Q.  Thus every
physical terminal can be represented as `t=a+37` within the canonical
interval, with `a>=34`.  The finite checks below include a larger domain
starting at a=1 for convenience.

## 2. A genuine chronological envelope

Every tested a is below z, so the prefix contains no carry.  At each of its
ordinary sources, nonnegative integer heights give

`|epsilon_i|=|2^(-h_(i+p))-2^(-h_i)|<1`,

and hence `|f_i|<rho_i<=1`.  The canonically anchored early signature gives
`f_0=...=f_23=0` and `f_24,...,f_28<0`.

For a>=29 define

`Wplus(a)=sum_(29<=i<a)rho_i`,
`Wminus(a)=sum_(24<=i<a)rho_i`.

Then necessarily

- lower atom: `0<F_a<Wplus(a)`;
- upper atom: `0<-F_a<Wminus(a)`.

For smaller a the empty-sum/known-sign cases are excluded directly; they
also fail the coarse tests below.  These bounds concern an actual
chronological prefix.  No variation-to-excursion conversion is used.

The simpler bound `|F_a|<a` provides a fast exact rejection test.  Let
`d=|r-Q|>=1`.  On the lower atom, `exp(x)>1+x` and `ln2>2/3` yield

`F_a>2K0*d/L`,

so `2K0*d<aL` is necessary.  On the upper atom put
`x=(d ln2-a delta)/L>0`.  Positivity follows from
`ln2>(L-1)delta`.  Since K_a>Klow,

`-F_a=3K_a(exp(x)-1)>3Klow*x`

`      >(2Klow*d-3Klow*a/2^40)/L`.

Thus the upper necessary integer test is

`2Klow*d*2^40<a*(L*2^40+3Klow)`.

Failure of either coarse test is a proved exclusion, not an uncomputed
candidate.  Only coarse survivors need the sharper exponential comparison.

## 3. Gap-free exact arithmetic

The verifier checks every canonical start `1<=a<=1826035`, with no skipped
phase.  For each start it computes the exact terminal rank, applies the
incoming E membership and coarse necessary test, and, for every coarse hit,
compares rigorous intervals for `|F_a|` with the appropriate W envelope.

Logarithms use 80 exact rational atanh-series terms plus their positive
geometric tail.  For `0<x<1`, exp(x) uses degrees 0..8, with tail at most

`[x^9/9!]/[1-x/10]`.

For the upper atom, reciprocal positive exponential bounds enclose
`1-exp(-x)`.  Every interval comparison is strictly resolved; no floating-
point result decides inclusion or exclusion.  Decimal displays are optional
diagnostics only.

To enclose all mechanical weights cheaply, set M=2^96 and begin with exact
scaled rho interval `[M,M]`.  At source i, first add its interval to the
appropriate prefix sum, then use its exact mechanical bit c_i to update

`lower_(i+1)=floor(2^c_i lower_i/3)`,
`upper_(i+1)=ceil(2^c_i upper_i/3)`.

Induction encloses every actual rho_i, and integer summation encloses every
W.  Both final sum widths are below 2^-40.  The code asserts each tested
comparison is resolved.  This is outward-rounded exact rational arithmetic,
not floating-point simulation.

## 4. New canonical terminal floors

The first weighted-envelope-compatible lower start is

`a=190537`, `r=88514759934`, `start_rank=137528032513`.

The first upper start is

`a=1826035`, `r=88515371864`, `start_rank=599131`.

Both boundary ranks pass the separate new corridor and inherited isolated-
deletion tests, but are not asserted to be physical.  All earlier applicable
starts are excluded.  Adding the 37-source prefix length gives the global
conditional floors

`lower-atom terminal phase >=190574`,

`upper-atom terminal phase >=1826072`.

An actual start at or beyond z automatically lies after these floors; no
claim about a carry-containing speed envelope is needed for the floor proof.

For comparison only, the unit-speed test first admits lower start190537
and upper start1444961; replacing a by the actual Wminus is what removes
the upper start1444961 and the next candidate1635498.

## 5. Exact finite rank-set refinement

Intersect the complete scanned starts with the new corridor

`[75446746413,102504571503]`

minus its 22 retained RL193 deletions.  Since B is invertible modulo L and
the scanned range is shorter than L, each start contributes a distinct rank.
There are 173508 eligible lower and 185747 eligible upper ranks.

Exactly ten pass this weighted envelope in the entire scanned range:

| start a | atom T | terminal rank |
| ---: | ---: | ---: |
| 190537 | 2^38 | 88514759934 |
| 381074 | 2^38 | 88514747135 |
| 571611 | 2^38 | 88514734336 |
| 762148 | 2^38 | 88514721537 |
| 952685 | 2^38 | 88514708738 |
| 1143222 | 2^38 | 88514695939 |
| 1333759 | 2^38 | 88514683140 |
| 1524296 | 2^38 | 88514670341 |
| 1714833 | 2^38 | 88514657542 |
| 1826035 | 2^37 | 88515371864 |

Thus this finite filter removes a further 173499 lower and 185746 upper
ranks, 359245 in total, disjoint from the previous deletions.  The combined
necessary-rank set has exact cardinality

`27057825069-359245=27057465824`.

To test its new finite deletion rule at a rank r, compute
`a=((r-Q)p) mod L`.  If `1<=a<=1826035`, retain r only when it is one of
the ten listed survivors; outside that interval this new finite rule makes
no decision.  The corridor and inherited isolated deletions apply separately.
This is a necessary-state cardinality, not a physical terminal population.

## 6. Classification and reproducibility

The displacement formula and chronological envelope are **proved analytic
mathematics**, conditional on physical terminals.  The gap-free scan,
resolved exact intervals, first compatible phases, ten survivors and rank
counts form an **exact finite necessary-state certificate** on starts
1..1826035.  Starts after1826035 are outside the scan's claimed range; no
unbounded separation theorem is asserted.

Run `python3 verification/verify_rl194_chronological_speed.py` from the
package root.

No rank is realized.  H21 counts and charging remain unchanged; no
improvement to the inherited spacing >=1001 between distinct extremal
terminals is claimed.  The sole high branch and all global gates remain open.
The new floors are anchored to the inherited canonical origin; they cannot
be freely transferred to every cyclic relabeling.
