# RL211 certified facts and proof ledger

Date: 2026-08-31. Canonical current classification record after completing RL211.
All physical conclusions remain conditional on the sole high branch `(37,0,23,-1)`.

## New proved analytic mathematics

### RL211-T1 — exact absolute `e=4` H21 selector
For the surviving above-p short offset `e=4`, RL210 gives
`h_t=h_(p+t)` for `0<=t<=4` and
`K_0=...=K_5=2^37`. The H21 source is `a=p+4`, so inherited RL199 gives
`h_(p+4)=1` and `y_(p+4)=2^34 eta-1`. Hence `h_4=1`.

The exact mechanical digits are `c_0,c_1,c_2,c_3=1,2,1,2`. With
`h_0=h_1=0`, nonnegative heights and every acceleration exponent positive,
there are exactly three possible root prefixes through phase 4:
- heights `00001`, exponents `1211`, affine numerator `Q=85`;
- heights `00101`, exponents `1121`, affine numerator `Q=73`;
- heights `00111`, exponents `1112`, affine numerator `Q=65`.

Since `rho_4=2^6/3^4` and `K_4=2^37`,
`y_(p+4)-y_4=3^4*2^32`.
Thus
`y_4=2^34 eta-1-3^4*2^32`.
For a root prefix with numerator `Q`,
`2^5 y_4=3^4 y_0+Q`. Integrality of `y_0` gives, modulo `3^4=81`,
the three exact lift residues
`eta=45,3,56 (mod 81)` in the order above.
Inherited RL199 permits only `eta=0 or 8 (mod 9)`, so only the first prefix survives:
`h_0...h_4=00001`, `a_0...a_3=1211`, and `eta=45 (mod 81)`.

### RL211-T2 — root p-gap unit refinement
At the absolute root, `h_0=h_p=0`, `rho_0=1`, and `K_0=2^37`, hence
`y_p-y_0=2^37`.
Both `y_0` and `y_p` are physical odd cycle states and therefore units modulo 3.
The three lifts of `eta=45 (mod 81)` modulo 243 give
`(y_0,y_p) mod 3` equal respectively to
`(1,0)`, `(0,2)`, `(2,1)` for
`eta=45,126,207 (mod 243)`.
Only the final pair has both entries units. Therefore every physical H21 realization
of the exact `e=4` necessary rank satisfies

`eta = 207 (mod 243)`.

In particular it is in inherited state `011` (`eta=0 mod 9`), so state `111` and
the eta classes `8,17 (mod 18)` are excluded at this offset. Terminal sign/parity
remains open because adding 243 reverses parity.

### RL211-T3 — exact denominator/flat-K barrier
RL195 proves that, for a complete globally admissible height word, the odd part of
the reduced denominator of every normalized p-gap `Delta_i=K_i/rho_i` is the same
global denominator, and exact `K_0=2^37` already forces that denominator to be one.
Consequently re-testing integrality through a matched RL210 flat-K prefix cannot
supply an independent contradiction: whenever `K_t=2^37`,
`Delta_t=3^t*2^(37-b_t)` is manifestly dyadic.
The same remains true at the first mismatch phase `m`, because `K_m=K_0`.
This retires the proposed “flat K implies an integral gap” shortcut; normalized gaps
need only be dyadic, not integral.

## Exact certificate

`verification/verify_rl211_absolute_e4_selector.py` exhausts the three admissible
`e=4` root prefixes, recomputes all affine numerators and eta residues, checks the
mod-9 state filter, the three mod-243 lifts, and the root p-gap unit filter.
It also checks the displayed flat-K dyadic identities for `t=0..37`.

## Inherited state retained

Necessary terminal rank count remains **13,415,865,871**:
`7,091,831,284` above p and `6,324,034,587` below p.
RL210's `e>=56` first-divergence selector `24<=m<=37`, smaller exponent 37,
and exact `m=24` orientation obstruction are unchanged.
The six above-p short offsets remain `4,16,28,33,40,45`; RL211 adds the selector
above only to `e=4`.
The inherited H21 classes remain globally `0,8,9,17 mod18`; at `e=4` only the
state-011 pair `0,9 mod18` remains.
No physical H21 incidence, H21 charge, rank deletion, sole-branch contradiction,
Gate A/Gate B closure, nontrivial-cycle exclusion or global Collatz closure is proved.

## Open obligations

The strongest next live consumers are:
1. apply the same absolute endpoint/root-closure mechanism to `e=16` with an exact,
compressed quotient-state/residue representation rather than raw prefix enumeration;
2. couple the `24<=m<=37` first-divergence identities to a complete-word quotient-state
residue or absolute endpoint moment not erased by the RL195 denominator theorem;
3. treat `e=28,33,40,45` separately unless a common absolute consumer is proved.
