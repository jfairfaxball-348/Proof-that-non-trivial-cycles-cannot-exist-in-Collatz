# RL199 proof — H21 oriented lift index

Date: 2026-08-31. Scope remains the inherited sole high branch `(37,0,23,-1)`.

## 1. `tau=34` affine tail

RL198 gives common height 1, `C34=21*2^34`, and 34 unit pair-costs before the first defect.
The first 33 transitions remain zero-defect, so both individual exponents are one.

If `Y_0^-` is the lower ordered odd endpoint, 33 consecutive exponent-one transitions imply
`2^34 | (Y_0^-+1)`. Put `eta=(Y_0^-+1)/2^34`. Then

`Y_0^-=2^34 eta-1`,
`Y_0^+=2^34(eta+21)-1`.

Induction under `Y -> (3Y+1)/2` gives, for `0<=t<=33`,

`Y_t^-=2^(34-t)3^t eta-1`,
`Y_t^+=2^(34-t)3^t(eta+21)-1`.

For `t<=32`, the bracket after removing the factor 2 from `3Y_t+1` is odd, proving the exponent is
exactly one. At `t=33` the difference is `42*3^33=14*3^34`.

## 2. State bit from one predecessor layer

At `tau=35 -> tau=34`, mechanical bit 2 gives exponent 1 in state `011` and exponent 2 in
state `111`.

Thus the lower `tau=35` endpoint is respectively

`(2Y_0^- -1)/3` or `(4Y_0^- -1)/3`.

Their integrality conditions are `eta=0 mod 3` and `eta=2 mod 3`.

Every odd cycle state is nonzero modulo 3: if `2^k z=3x+1`, then `2^k z=1 mod 3`.
Imposing this on both `tau=35` endpoints and reducing the displayed formulas modulo 9 gives

`011 <=> eta=0 mod 9`,
`111 <=> eta=8 mod 9`.

## 3. Terminal bit

At `t=33` write `Y_pre(s)=2*3^33 s-1`, where `s=eta` or `eta+21`. Then

`3Y_pre(s)+1=2(3^34s-1)`,

so `k(s)=1+v2(3^34s-1)`.

Exactly one of `eta,eta+21` is even. For the even parameter the factor in parentheses is odd,
so that endpoint has `k=1` and terminal height `20+2-1=21`.

For the odd parameter let `nu=v2(3^34s-1)>=1`; its terminal height is
`20+2-(1+nu)=21-nu`. Hence the signed p-defect is `+nu` when `eta` is even and `-nu`
when `eta` is odd. Nonnegative height is exactly `nu<=21`.

In both orientations, the physical terminal numerator is the height-adjusted difference
`21*3^34=7*3^35`.

## 4. Hensel cut

For odd `s`, `nu>=22` iff `3^34s=1 mod 2^22`, equivalently

`s=3^(-34)=1893305 mod 2^22`.

Combine this with `eta=0 or 8 mod 9` and whether the odd parameter is `eta+21` or `eta`.
CRT gives modulus `9*2^22=37748736` and the four forbidden residues recorded in the main report.

## 5. Information boundary

The tail difference is

`Y_t^+-Y_t^-=21*2^(34-t)3^t`,

which contains no `eta`. RL198 already fixes the corresponding common heights and mechanical bits.
The terminal height-adjusted numerator is also independent of orientation. Therefore this complete
unoriented common-pair interface cannot select `eta`.

The inherited K drift
`K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`, with `q_i=rho_i 2^(-h_i)`,
gives the signed formula in the report by substituting
`(h_i,G_i)=(21,+nu)` or `(21-nu,-nu)`.

No physical realization or global closure follows from these local identities.
