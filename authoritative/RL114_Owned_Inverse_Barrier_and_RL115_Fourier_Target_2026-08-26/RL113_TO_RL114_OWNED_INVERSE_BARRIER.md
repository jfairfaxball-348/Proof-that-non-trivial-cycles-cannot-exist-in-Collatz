# RL114 — owned-support inverse barrier and route transition

Date: 2026-08-26

## Outcome and classification

RL114 tested the mandatory first route from the RL113 tournament: a
two-/three-term near-extremizer theorem derived from the two owned conditions
`D|Q(u)` and `D|Q(v)` for a zero-flow-cut closest pair. No such theorem is
proved. In particular, no threshold for “near-extremal” coefficient mass is
promoted, no support congruence is claimed, and no radius reduction follows.

The analytic result is a **method barrier** for the attempted
subtraction-based formulation. For a pair of rotations, full ownership at the
second root is a consequence of full ownership at the first root. Subtracting
the two conditions then retains only `D|S`, precisely the sparse-multiple
interface already supplied by RL109. Keeping an individual numerator instead
of subtracting retains the whole-word integrality condition, not a new local
two-/three-term support condition. Thus this attack has not supplied the new
ownership-sensitive input its own target required.

This is not a proof that every conceivable owned-support inverse theorem is
false. It is a stop record for this route in its RL113/RL114 formulation. Per
the binding fallback ledger, the next live route is dyadic–triadic Fourier
discrepancy.

All global closure statements remain open: Gate A globally, Gate B globally,
nontrivial-cycle exclusion, and Collatz closure.

## Exact rotation algebra

For a binary word `c`, let `|c|` be its length, `wt(c)` its number of ones,
and use the inherited unit numerator

`Q(c)=sum_(i:c_i=1) 2^i 3^(# ones strictly after i)`.

For words `a,b`, direct splitting of the sum gives

`Q(ab)=3^wt(b) Q(a)+2^|a| Q(b)`.                         (1)

Put `p=|a|`, `r=|b|`, `m=wt(a)`, `n=wt(b)`, and
`D=2^(p+r)-3^(m+n)`.  Applying (1) to `ab` and `ba` yields

`2^p Q(ba) = 3^m Q(ab) + D Q(a)`.                        (2)

Because `D` is odd, (2) proves

`D|Q(ab)  ==>  D|Q(ba)`.                                 (3)

Iterating (3) gives the same implication for every cyclic rotation. In the
ordinary cycle setting, this agrees with the inherited physical statement:
once `Q(r)/D` is an integer at an appropriately rooted parity word, the
parity recursion supplies the corresponding owned orbit states. The second
selected divisibility condition therefore does not add an independent
congruence to the first.

For the RL109 pair, choose the common zero-flow cut before applying the
fixed-cut swap formula. This common re-root changes both displayed rotations
but preserves that they are rotations of the same word; under actual
ownership each re-rooted numerator is still divisible by `D`. Then the
fixed-cut transport identity gives

`S=Q(v)-Q(u)=sum_j epsilon_j 2^(a_j)3^(b_j)`.

If both roots are owned, subtraction gives `D|S`; this is already RL109.3.
Conversely, retaining `D|Q(u)` retains the entire word numerator rather than
a relation determined by a two- or three-term subconfiguration. Equation (2)
is the exact accounting that prevented an unsupported claim that the two
conditions furnish a second local support congruence.

## Why the mandatory lemma stops here

The requested lemma had to define thresholds and prove that a selected
two-/three-term near-extremizer, *using both owned conditions*, forced a
specific forbidden support congruence. The only candidate deduction obtained
by comparing the two roots was their difference, `D|S`; RL110 already proves
that all-legal support geometry and maximum-coefficient bounds do not make
that condition small when `R>=4`. No additional inequality, selection rule,
or physical-strip fact was found that uses `D|Q(u)` without simply retaining
the original full numerator condition. Consequently selecting a numerical
threshold now would be unsupported, and calling its conclusion an inverse
theorem would violate the RL114 stop rule.

## Mandatory red teams

- **RL20:** its frozen radius-four word has `D∤Q`; it cannot enter (3) as an
  owned input. A conclusion that uses only its local support or `D|S` would
  therefore fail the discriminator. RL114 makes no such conclusion.
- **RL79:** for generalized increment `s`, the owned statement is only
  `D|sQ`. Equation (2) may be multiplied by `s`, but it does not cancel `s`;
  the ordinary unscaled premise is retained exactly.
- **RL81:** `Q/D` is called an actual state only under the full divisibility
  premise and parity recursion. No quotient from a local support sum is
  treated as physical.
- **Primitivity:** it is still needed in RL109 to select distinct physical
  rotations and obtain `S!=0`; equations (1)--(3) do not create distinctness.
- **Scope:** this report makes no Raw/Farey assertion. Its algebra is global
  only conditional on the inherited hypothetical ordinary primitive cycle.
- **Finite work:** non-promoted local probes exhaustively inspected primitive
  canonical words through length 18 for zero-flow-cut pairs of radii 2 and 3
  (24,068 pairs), and through length 17 for radii 4 through 10 (1,002,070
  pairs). They found no case with `D|S` while `D∤Q(u)` after the necessary
  common re-root. These observations have no positive owned input and are not
  a theorem, certificate, or inverse result.

## Dependencies, correction, and next step

The report depends on RL109's ordinary numerator/zero-flow-cut interface and
RL110's all-legal-support barrier. No inherited theorem is corrected or
demoted. The clarification is only that a zero-flow cut has to be used as a
common re-root before the fixed-cut swap expansion; otherwise the displayed
numerator difference is not the one expanded by that cut.

The route decision is a **barrier/stop**, not a mathematical closure. Start
RL115 with the Fourier route exactly as stated in the next target and retain
the full RL113 fallback order.
