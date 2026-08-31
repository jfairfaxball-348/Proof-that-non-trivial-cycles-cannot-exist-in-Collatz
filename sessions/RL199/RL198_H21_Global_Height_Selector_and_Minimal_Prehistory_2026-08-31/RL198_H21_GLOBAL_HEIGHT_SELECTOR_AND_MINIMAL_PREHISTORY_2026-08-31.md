# RL198 — H21 Global Height Selector and Minimal Prehistory

Date: 2026-08-31  
Incoming authority: RL197 at `68e51bcc260c237b192e9ded3fe0df0b0e512f24`.  
All physical conclusions remain conditional on the sole high branch `(37,0,23,-1)`.

## Outcome

RL198 decides the global H21 height-scale selector left open by RL197.

RL197 proved that every surviving H21 `{33,34,35}` co-owner has six locally admissible
shallow common-height triples

`000,010,011,100,110,111`

at starts `tau=35,34,33`, and that the desired canonical owned p-shift zero edge exists
exactly when `e34=0`.

The inherited exact first-defect prehistory law from RL186 is not scale blind.  For a
zero-defect prefix of length `tau`, if `C_0` is its owned starting numerator and the positive
transition costs are `d_j>=1`, then

`v_2(C_0)=sum_(j<tau)d_j >= tau`.

Applying this to RL197's exact H21 numerators gives

`C34 = 21*2^(33+e34)`,
so `33+e34 >= 34`, hence **`e34=1`**;

and

`C33 = 63*2^(32+e33)`,
so `32+e33 >= 33`, hence **`e33=1`**.

Thus exactly two RL197 local states survive the global physical prehistory:

`011,111`.

This is a genuine global selector theorem, not another blindness barrier.  It is a synthesis
of inherited exact prehistory with RL197's newly isolated local interface.  It therefore
continues the H21 line under the user-specified branch rule.

## 1. Exact selector

RL197 gives

`Delta34=21*2^33`, `Delta33=63*2^32`

and, at common p-pair height `e_j`,

`C_j=2^(e_j) Delta_j`.

Because `e34,e33 in {0,1}`,

`v_2(C34)=33+e34`,
`v_2(C33)=32+e33`.

RL186's exact zero-prefix valuation law gives `2^tau|C_0` for a physical clean shallow
zero-prefix start whose first defect is at offset `tau`.  The H21 `tau=34` and `tau=33`
co-owners are precisely such starts in the inherited joint-terminal construction.
Therefore

`v_2(C34)>=34`, `v_2(C33)>=33`.

The displayed binary ranges force `e34=e33=1`.

This is fully consistent with RL190's independently reconstructed H21 start rows
`C34=21*2^34`, `C33=63*2^33`.  No inherited theorem is repaired or demoted.

## 2. State collapse and zero-edge exclusion

Intersecting `e34=e33=1` with RL197's six-state local interface leaves

`011,111`.

RL197's canonical middle zero-edge cases were exactly `000,100`; their intersection with
the global survivor set is empty.  Hence the `tau=34 -> tau=33` edge and its p-shifted copy
cannot both be height zero on a physical H21 co-owner.

The conclusion is stronger on the complete co-owned zero prefix.  At `tau=34`, the common
height is one.  Section 3 proves every transition cost in that 34-step zero prefix equals
one.  Along a zero-defect/common-height transition,

`d_j=c_j+M_j-M_(j+1)`,

so with `d_j=1` and `c_j in {1,2}`,

`M_(j+1)=M_j+c_j-1 >= M_j`.

The common height therefore never falls from one to zero on the `tau=34` suffix.
The extra leading `tau=35 -> tau=34` transition is `0 -> 1` in state `011` or
`1 -> 1` in state `111`.  It is not zero-zero in either case.

Therefore **the entire H21 co-owned `tau=35` zero-defect prefix contains no
p-shift-compatible height-zero chronological edge**.

This closes the specific RL196/RL197 H21 zero-edge-consumer route.  It does not exclude the
H21 co-owner itself or release its binding charging budget.

## 3. Saturated valuation budgets

With the selector fixed,

`C34=21*2^34=360777252864`, so `v_2(C34)=34`.

RL186 gives

`sum_(j<34)d_j=34`

with 34 positive integers `d_j>=1`.  Hence every one of those 34 costs is exactly one.

Similarly,

`C33=63*2^33=541165879296`, `v_2(C33)=33`,

so all 33 costs in the `tau=33` zero prefix are one.

At `tau=35` there are exactly two cases:

- state `011`: `C35=7*2^35`, valuation 35, so all 35 costs are one;
- state `111`: `C35=7*2^36`, valuation 36.  Its final 34-cost suffix already sums to 34,
  so the leading `tau=35 -> tau=34` cost is exactly two.

Thus the remaining `e35` ambiguity is equivalently one exact leading-cost bit:
`d_lead=1` versus `d_lead=2`.

## 4. Exact preterminal physical interface

The surviving H21 terminal rank lies in

`D=[23369453298,41775866136]`

minus the inherited 14 deletions.  One chronological source before the terminal has rank

`(r-B) mod L in [80448749305,98855162143]`.

This interval lies strictly above `R=57079296007`, so the final source mechanical bit is
exactly `c=2`.

For the `tau=34` start, RL187's exact terminal ownership identity is

`Dsum=tau+ell+h_start-H`,

where `ell` counts `c=2` bits along the prefix.  Insert

`Dsum=34`, `tau=34`, `h_start=1`, `H=21`

to obtain `ell=20`.

The final source itself has `c=2`; therefore the first 33 zero-to-zero transitions contain
19 `c=2` bits.  Starting at common height one and using `d=1` throughout gives the common
height immediately before the terminal:

`M_pre = 1+19 = 20`.

The common owned numerator at that source is also exact.  Starting from

`C33=63*2^33`

and applying 32 zero transitions of unit cost,

`C_pre = 3^32 C33 / 2^32 = 14*3^34`
`=233480543795331966`.

It satisfies

`C_pre mod 8 = 6`

and

`3*C_pre/2 = 7*3^35 = 350220815692997949 = T`.

Thus the final ordinary transition begins from a common p-pair height `(20,20)`,
has mechanical bit 2, and reaches the H21 first defect of maximum height 21 with exact
terminal numerator `T`.

The congruence `C_pre == 6 (mod 8)` ensures the two preterminal odd owned states have
different mod-4 classes; one receives acceleration exponent one and rises to terminal
height 21.  RL198 does **not** determine which endpoint it is.  That owned orientation/sign
bit is the sharp next datum.

## 5. Classification and scope

Promoted analytic mathematics / exact synthesis:

1. global H21 selector `e34=e33=1`;
2. exact global survivor set `{011,111}`;
3. exclusion of the RL197 canonical middle zero edge and, more strongly, every
   p-shift-compatible zero edge in the co-owned `tau=35` zero-defect prefix;
4. exact unit-cost saturation of the `tau=34` and `tau=33` suffixes and the
   `d_lead in {1,2}` interpretation of `e35`;
5. exact preterminal interface: common height 20, mechanical bit 2,
   numerator `14*3^34`, terminal numerator `7*3^35`.

The RL186 zero-prefix valuation theorem and RL187/RL190 joint-terminal framework are inherited
inputs.  RL197's six-state result remains correct as a local, prehistory-free interface
classification.

Exact finite certificate:
`verification/verify_rl198_h21_global_height_selector.py`.

Not claimed:

- physical realization or exclusion of either `011` or `111`;
- determination of `e35`;
- determination of the final owned endpoint orientation/sign;
- relaxation of the binding H21 `{33,34,35}` charge budget;
- exclusion of the H21 family or the sole high branch;
- Gate A/Gate B, non-trivial-cycle, or global Collatz closure.
