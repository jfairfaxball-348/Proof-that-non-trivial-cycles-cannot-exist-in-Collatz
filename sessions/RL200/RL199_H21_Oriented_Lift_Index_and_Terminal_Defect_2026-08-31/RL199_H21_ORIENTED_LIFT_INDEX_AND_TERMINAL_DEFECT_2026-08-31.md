# RL199 — H21 oriented lift index, minimal prehistory, and terminal defect

Date: 2026-08-31  
Incoming authority: RL198 at `baccc6ce465de817c8f90f092d938890e0d6e52a`.  
All physical conclusions remain conditional on the sole high branch `(37,0,23,-1)`.

## 0. Outcome and classification

RL199 does not decide which of RL198's two H21 states `011,111` is globally realized, and it
does not decide the terminal orientation absolutely. It replaces both apparently separate bits by
one exact **oriented lift index** `eta` attached to the lower `tau=34` p-shift endpoint.

The exact consequences are:

1. the entire `tau=34` unit-cost tail has an affine odd-state reconstruction
   `Y_t^-=2^(34-t)3^t eta-1`,
   `Y_t^+=2^(34-t)3^t(eta+21)-1`, `0<=t<=33`;
2. the one-step `tau=35` prehistory plus the fact that every odd cycle state is a unit modulo 3
   sharpen the state selector to
   `011 <=> eta=0 (mod 9)` and `111 <=> eta=8 (mod 9)`;
3. the terminal orientation is
   `eta even <=> lower endpoint reaches height 21`,
   `eta odd <=> upper endpoint reaches height 21`;
4. therefore the two remaining bits are exactly the four necessary classes
   `eta=0,8,9,17 (mod 18)`;
5. the non-height-21 terminal endpoint imposes one exact Hensel exclusion inside each class,
   but no whole mod-18 class is removed;
6. the common pair-gap suffix through the terminal is independent of `eta`, so an oriented
   endpoint residue (or equivalent signed post-terminal datum) is genuinely required next.

This is new analytic mathematics with an exact finite arithmetic certificate. It is not a
realization theorem, H21 budget release, branch closure, Gate closure, non-trivial-cycle
exclusion, or Collatz proof.

## 1. Frozen RL198 interface

Use RL198's globally surviving H21 states `011,111`, with

- common `tau=34` and `tau=33` heights equal to 1;
- `C34=21*2^34=360777252864`;
- all 34 costs in the `tau=34` zero prefix equal to one;
- `tau=35 -> tau=34` leading cost one in `011`, two in `111`;
- one step before the terminal, common height 20 and mechanical bit 2;
- `Cpre=14*3^34=233480543795331966`;
- terminal numerator `T=7*3^35=350220815692997949`.

The p-shift gap is positive, so at an equal-height pair the ordered upper odd endpoint exceeds the
ordered lower odd endpoint by the physical numerator.

## 2. Exact oriented `tau=34` reconstruction

Let `Y_0^-<Y_0^+` be the actual odd p-pair endpoints at the `tau=34` start.
The first 33 chronological transitions are zero-defect and have pair cost one. Since the endpoint
heights agree throughout those 33 transitions, each individual acceleration exponent is one.

Thirty-three consecutive exponent-one odd steps force `Y_0^-+1` to be divisible by `2^34`.
Define the positive integer

`eta=(Y_0^-+1)/2^34`.

Because `Y_0^+-Y_0^-=C34=21*2^34`,

`Y_0^-=2^34 eta-1`,
`Y_0^+=2^34(eta+21)-1`.

For every `0<=t<=33`, direct iteration gives

`Y_t^-=2^(34-t)3^t eta-1`,
`Y_t^+=2^(34-t)3^t(eta+21)-1`.

For `t<=32`,
`3Y_t+1=2(2^(33-t)3^(t+1)s-1)` with the bracket odd, so the individual exponent
is exactly one. At `t=33`,

`Y_pre^-=2*3^33 eta-1`,
`Y_pre^+=2*3^33(eta+21)-1`,

and their difference is exactly

`42*3^33=14*3^34=Cpre`.

Thus `eta` is an absolute endpoint lift invisible to the common pair difference.

## 3. Minimal `tau=35` prehistory sharpens the state selector

The `tau=35 -> tau=34` mechanical bit is 2.

For state `011`, the common height changes `0 -> 1`, so both individual exponents are one and

`Z^-=(2Y_0^- -1)/3`,
`Z^+=(2Y_0^+ -1)/3`.

Integrality is equivalent to `eta=0 (mod 3)`.

For state `111`, the common height changes `1 -> 1`, so both exponents are two and

`Z^-=(4Y_0^- -1)/3`,
`Z^+=(4Y_0^+ -1)/3`.

Integrality is equivalent to `eta=2 (mod 3)`.

Now use one global fact that is absent from RL197's prehistory-free local interface: every odd
state on a cycle is a unit modulo 3. Indeed if an odd state `z` has odd predecessor `x` with
acceleration exponent `k>=1`, then `2^k z=3x+1=1 (mod 3)`.

Applying this to both `tau=35` endpoints yields the exact refinement

- state `011`: `eta=0 (mod 9)`, with `(Z^-,Z^+)=(2,1) (mod 3)`;
- state `111`: `eta=8 (mod 9)`, with `(Z^-,Z^+)=(1,2) (mod 3)`.

No stronger state choice is inferred: both congruence classes remain arithmetically possible.

## 4. Terminal orientation and exact signed defect

At the preterminal source, for a parameter `s` equal to `eta` or `eta+21`,

`Y_pre(s)=2*3^33 s-1`

and

`3Y_pre(s)+1=2(3^34 s-1)`.

Hence the final individual acceleration exponent is

`k(s)=1+v2(3^34 s-1)`.

The two parameters `eta` and `eta+21` have opposite parity.

- If `eta` is even, `3^34 eta-1` is odd. The lower endpoint has exponent one and rises
  from height 20 with mechanical bit 2 to height 21.
- If `eta` is odd, `eta+21` is even. The upper endpoint has exponent one and reaches height 21.

Let `nu>=1` be the 2-adic valuation of the odd-parameter factor:

- for even `eta`, `nu=v2(3^34(eta+21)-1)`;
- for odd `eta`, `nu=v2(3^34 eta-1)`.

Then the other terminal endpoint has height `21-nu`, and the signed terminal p-defect is exactly

`G_terminal=+nu` for even `eta`,
`G_terminal=-nu` for odd `eta`.

Physical nonnegative height requires `1<=nu<=21`.

The terminal physical numerator is orientation-blind. In either sign case the height-adjusted
difference is

`21*3^34=7*3^35=T`.

Thus RL198's `Cpre mod 8=6` is upgraded to a complete conditional orientation theorem, but an
absolute sign still requires `eta mod 2`.

## 5. Four mod-18 classes and the terminal Hensel cut

Combining the mod-9 state selector with parity gives the exact necessary dictionary:

| `eta mod 18` | H21 state | height-21 endpoint | terminal defect |
| ---: | --- | --- | --- |
| 0 | `011` | lower | positive |
| 8 | `111` | lower | positive |
| 9 | `011` | upper | negative |
| 17 | `111` | upper | negative |

For the odd parameter `s`, the forbidden case `nu>=22` is exactly

`s = 3^(-34) (mod 2^22)`.

The unique residue is

`3^(-34) mod 2^22 = 1893305`.

With modulus `M=9*2^22=37748736`, physical nonnegative terminal height excludes exactly one
`eta` residue inside each mod-18 class:

- class 0: `eta != 18670500 (mod M)`;
- class 8: `eta != 1893284 (mod M)`;
- class 9: `eta != 6087609 (mod M)`;
- class 17: `eta != 27059129 (mod M)`.

Each mod-18 class contains `M/18=2097152` lift residues modulo `M`; only one is removed.
Consequently the terminal nonnegativity/Hensel condition does not choose either remaining bit.
Every surviving residue class has arbitrarily large positive representatives, so these are local
arithmetic witnesses only, not physical-cycle realizations.

## 6. Exact blindness boundary and first signed K consumer

For `0<=t<=33` the common pair difference

`Y_t^+-Y_t^-=21*2^(34-t)3^t`

is independent of `eta`. The common heights and mechanical bits through the RL198 zero prefix are
also fixed, and the terminal numerator remains `T` for either orientation.

Therefore any consumer that factors only through the RL198 `tau=34`-or-later **unoriented**
common heights, common pair numerators, and mechanical bits cannot recover `eta mod 9` or
`eta mod 2`. This is a scoped information-loss theorem, not a claim that all global constraints
are blind.

The inherited RL181 K-drift does expose the terminal sign one step later. If `rho` is the
mechanical weight at the terminal source, then

`K_next-K_terminal
 = +rho(2^nu-1)/(3*2^21)` for even `eta`,
`K_next-K_terminal
 = -rho(2^nu-1)/(3*2^21)` for odd `eta`.

Since `rho<=1` and `nu<=21`, its magnitude is strictly less than `1/3`.
RL199 does not have a certified subunit rank-resolved K consumer, so no sign is inferred from
the existing coarse K corridor. The formula identifies an exact future consumer rather than
reviving a variation-to-excursion inference.

## 7. Classification and next datum

New analytic mathematics:

1. exact oriented lift parameterization of the complete `tau=34` unit-cost tail;
2. exact `eta mod 9` selector for `011` versus `111`;
3. exact parity selector for terminal orientation and signed defect formula;
4. exact four-class `eta mod 18` dictionary;
5. exact Hensel nonnegative-height exclusion modulo `9*2^22`;
6. scoped common-pair information-loss theorem;
7. signed subunit K-drift bridge.

Exact finite certificate:
`verification/verify_rl199_h21_oriented_lift.py`.

The next non-aggregate datum is an oriented absolute endpoint lift: enough information to determine
`eta mod 18` (or to exclude one of its four classes). Equivalent targets include the lower
`tau=34` endpoint modulo the required 3-adic/2-adic lifts, the signed terminal defect, or an exact
rank-resolved K successor constraint.

No H21 state is excluded, no H21 charge is released, and all Gate/global obligations remain open.
