# RL194 owned terminal-prefix interface

RL194 closeout proof and exact finite necessary-state certificate.
Date: 2026-08-31.

Incoming authority is the verified RL193 handover at
`4ded9b73d84cd3f9101c9eaef81d783e14390914`. The parent completed the RL194
start gate. All claims are conditional on a physical extremal
`{35,36,37}` terminal on the sole high branch `(37,0,23,-1)`.

## Result and scope

The owned odd numerator gives a local restriction not contained in the total
tail valuation: the terminal can return to zero defect in one transition
only through two exact ordered height/exponent interfaces. Neither can
remain zero on the next transition. In particular,

`not (G_(t+1)=0 and G_(t+2)=0)`.

For every initial difference other than `+3` or `-1`, the sign of the first
successor defect is forced to equal the initial sign. The accelerated
exponents are partly forced as listed below.

A complete three-transition necessary-state certificate covers all 42
ordered unequal height pairs of maximum 21, with the actual common
mechanical word `212` on all incoming extremal ranks, including both atoms.
All 42 initial pairs have necessary survivors after three transitions. This
is a precisely scoped barrier to eliminating an initial pair or atom with
this particular three-transition parity filter alone. It does not rule out
stronger congruence filters, later transitions, or additional physical
constraints. No surviving state is a physical realization.

## 1. Owned pair representation and actual mechanical word

At the terminal, the inherited exact gap and height maximum are

`Delta_t=3^37/2^21`, `max(h_t,h_(t+p))=21`, `G_t!=0`.

Let `X=y_t` and `Z=y_(t+p)` be the physical odd orbit states, with phases
interpreted periodically. Write `h=h_t`, `hp=h_(t+p)`, and `g=h-hp`.
On an ordinary p-edge the owned positive integer numerator is

- `C=2^g Z-X` if `g>0`;
- `C=Z-2^(-g)X` if `g<0`;
- `C=Z-X` if `g=0`.

Thus `Delta=C/2^max(h,hp)`; C is odd exactly when g is nonzero. At this
terminal **C is exactly `3^37`**, not a freely chosen odd numerator.
The complete initial domain is

`(h,hp)=(21,j)` or `(j,21)`, `0<=j<=20`.

Use `A=217976794617`, `L=137528045312`, `B=80448749305`,
`R=57079296007`. Terminal rank lies in the incoming
`E=[72797034370,103818202602]` minus its 24 inherited deletions.
For all of the larger interval E, the successive source-rank intervals are

- offset 0: `[72797034370,103818202602]`, above R;
- offset 1: `[15717738363,46738906595]`, below R;
- offset 2: `[96166487668,127187655900]`, above R;
- offset 3: `[39087191661,70108359893]`.

Consequently sources at offsets 0,1,2 have common mechanical bits `2,1,2`.
They avoid both the carry rank `L-1` and the mechanical-switch source
`R-1`; their successors also avoid the carry. The ordinary pair formulas
are therefore valid for all three transitions. The computation deliberately
stops at depth 3. At the fourth transition the word can split, and one rank
can transition into the carry; no fourth-transition statement is made.

This rank argument covers both RL192 atoms and a superset of the RL193
remaining ranks. It neither assumes nor asserts that an E rank is realized.
Periodically lifted chronology makes any canonical wrap harmless to the
ordinary formulas on these verified sources.

## 2. Exact transition rule

Let `alpha=v2(3X+1)`, `beta=v2(3Z+1)`, and c be the common mechanical bit.
Every physical transition obeys

`1<=alpha<=h+c`, `1<=beta<=hp+c`,

`h'=h+c-alpha`, `hp'=hp+c-beta`,

`g'=g+beta-alpha`.

For `g>0`,

`N=3C+2^g-1=2^(g+beta)Z'-2^alpha X'`.

For `g<0`,

`N=3C+1-2^(-g)=2^beta Z'-2^(-g+alpha)X'`.

For `g=0`,

`N=3C=2^beta Z'-2^alpha X'`.

If the two displayed powers of two differ, the valuation of N must be their
minimum because X',Z' are odd. If the powers agree at exponent d, then
`v2(N)>d`, and the successor difference is zero. In every permitted case,
divide by the smaller power to get C'. These are necessary conditions;
they are not asserted sufficient for a physical orbit.

The verifier checks the independent normalized recurrence on every accepted
edge:

`2^c C'/2^max(h',hp') = 3C/2^max(h,hp) + 2^-hp - 2^-h`.

## 3. First transition: exact valuation/sign table

Here `C=3^37` and `c=2`. The needed valuations are

| Initial g | `v2(N)` | Forced exponent / successor sign |
| --- | ---: | --- |
| `+1` | 1 | `alpha=1`, `g'>0` |
| `+2` | 2 | `alpha=2`, `g'>0` |
| `+3` | 5 | positive, zero, or negative cases below |
| `+4,...,+21` | 3 | `alpha=3`, `g'>0` |
| `-1` | 3 | positive, zero, or negative cases below |
| `-2,...,-21` | 1 | `beta=1`, `g'<0` |

For example, `v2(3^38-1)=3` and `v2(3^38+7)=5`, checked exactly modulo
64; the other rows follow by comparing unequal valuations. In the `g>=4`
row, `g+beta>=5`, so the valuation 3 forces `alpha=3`, retaining positive
sign. The other nonexceptional rows follow identically.

The complete exceptional interfaces are:

- `g=+3`, initial `(21,18)`:
  - `alpha=5`, `3<=beta<=20`: positive successor;
  - `beta=2`, `6<=alpha<=23`: negative successor;
  - only `(alpha,beta)=(4,1)`: zero successor
    `(h',hp',C')=(19,19,(3^38+7)/16)`.
- `g=-1`, initial `(20,21)`:
  - `beta=3`, `3<=alpha<=22`: negative successor;
  - `alpha=2`, `4<=beta<=23`: positive successor;
  - only `(alpha,beta)=(1,2)`: zero successor
    `(h',hp',C')=(21,21,(3^38-1)/4)`.

In both zero cases, `v2(C')=1`. At the next source, equal successor heights
would require equal exponents `alpha'=beta'>=1` and
`v2(3C')>alpha'`. This is impossible because `v2(3C')=1`. Hence an
immediate zero return must immediately become nonzero again. This proves
the claimed two-source prohibition analytically, independently of the
three-transition enumeration.

The signs here are also the signs of the ordinary epsilon and weighted
flow, because rho is positive. This local sign persistence does not itself
give a long chronological ordering, excursion, spacing improvement, or an
H21 budget reduction.

## 4. Exact finite certificate

Run, from the package root:

`python3 verification/verify_rl194_owned_prefix.py`

The enumerated domain is exactly all 42 initial pairs, then all integers
alpha and beta within the nonnegative-height caps on every surviving state,
for exactly three transitions with word `212`. Finite rank cells split at
every possible carry/switch/digit boundary, so the rank-word check is
gap-free without scanning billions of individual ranks.

| Successor offset | Distinct necessary states | Accepted graph edges | Negative / zero / positive states |
| --- | ---: | ---: | --- |
| 1 | 540 | 540 | 268 / 2 / 270 |
| 2 | 4,202 | 4,517 | 2,182 / 16 / 2,004 |
| 3 | 25,417 | 30,977 | 14,766 / 16 / 10,635 |

State merging uses the full `(h,hp,C)` triple. Edges are counted from each
distinct current state, not as physical paths. Separately retaining the
initial signed difference proves that every one of the 42 initial pairs
has a surviving necessary path through depth 3. There are 44 possible
four-source sign patterns in this necessary graph. These are not claimed
to be physically realizable.

Completed range: all 42 initial pairs and all three stated transitions.
Uncovered range: transition depth >=4 is outside this certificate, not a
partially computed extension. No large or historical scan was launched.

## 5. Classification and dependencies

- **Proved analytic mathematics, conditional:** the first-transition
  exponent/sign restrictions; the two exact immediate-zero interfaces; the
  prohibition on consecutive zeros at terminal offsets 1 and 2.
- **Exact finite necessary-state certificate:** complete depth-3 counts and
  coverage, with no realization assertion.
- **Method barrier:** this particular depth-3 parity propagation does not
  eliminate any of the 42 input pairs and cannot distinguish the two atoms,
  which have the same covered mechanical word.
- **Open:** physical realization/exclusion, stronger owned congruence or
  sign-location correlation, later transitions, H21 incidence, and all
  inherited branch/global obligations.

Incoming authority definitions and target:
`authoritative/RL193_PHYSICAL_DEBT_TELESCOPE_VALUATION_AND_PHASE_INCIDENCE_2026-08-31.md`
and `authoritative/RL194_SIGN_WEIGHT_ORDERING_AND_OWNED_PREFIX_CONGRUENCE_TARGET.md`.
The current proof/correction ledgers and named red team were read.

Narrow live provenance consulted only to identify the load-bearing owned
pair representation:

- RL181 Section 4, frozen under
  `sessions/RL182/RL181_Shallow_Pair_Gap_Corridor_and_Normalized_Width_Occupancy_2026-08-30/`,
  for `Delta=C/2^max(h,hp)` and the physical odd/even pair formulas;
- RL187 Section 2 and RL188 Sections 1-2, frozen under sessions/RL188 and
  sessions/RL189, for the exact terminal invariant `(C,H)=(3^37,21)`;
- the byte-preserved incoming
  `authoritative/verification/verify_rl178_inherited_early_window.py`, whose
  generic exact transition identity agrees with the rule independently
  written and cross-checked here.

No inherited claim is repaired or demoted. The incoming 24 E deletions,
14 H21 deletions, canonical/carry rules, spacing >=1001, N35 bound,
ordinary-flow bound, and binding H21 budget are unchanged.
