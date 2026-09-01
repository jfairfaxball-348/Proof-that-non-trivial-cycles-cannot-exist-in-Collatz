# RL210 global p-shift prefix-overlap theorem

Date: 2026-08-31. All physical H21 conclusions remain conditional on the sole
high branch `(37,0,23,-1)`. RL206-C1/C2 and the RL209 reduced predicate control.

Use the inherited constants

`A=217976794617`, `L=137528045312`, `p=65470613321`,
`u=103768467013`, `z=L-p=72057431991`, with `Ap-uL=1`.

Write `b_i=floor(Ai/L)`, `S_i=b_i-h_i`, and for `0<=t<z`

`S'_t=S_(p+t)-u`.

The acceleration law gives `S_(i+1)-S_i=a_i>=1`; hence both `S_t` and `S'_t`
are strictly increasing integer sequences. The anchors imply
`S_0=S'_0=0` and `S_1=S'_1=1`.

## RL210-T1 — exact no-carry p-shift and 56-bit overlap congruence

Because `Ap=uL+1`,

`b_(p+t)=u+floor((At+1)/L)`.

The equality `floor((At+1)/L)=floor(At/L)` fails exactly when
`At mod L=L-1`, equivalently `tB=L-1 mod L`. Since `pB=1 mod L`, the unique
such phase in one period is `t=z=L-p`. Therefore for every `0<=t<z`,

`b_(p+t)=u+b_t`, so `S'_t=b_t-h_(p+t)`.

Let an above-p tau34 source be `a=p+e`, `1<=e<z`, and put `d=3^p-2^u`.
RL209 gives

`E_a=3*2^(u+37)-2^u P_p+d R_(p,a)`.

At source height one, the inherited exact endpoint identity gives
`v2(E_a)=b_a-1`. Dividing by `2^u` and using the no-carry formula,

`F_e := 3*2^37-P_p+d R_(p,p+e)/2^u`

has exact valuation

`v2(F_e)=n_e:=b_e-1`.

For any `N<u`, strict increase gives `S_t>=t` and `S'_t>=t`; all terms with
index at least N vanish modulo `2^N`. Also
`d*3^(-p)=1-2^u*3^(-p)=1 mod 2^N`. Thus, if `e>=N`,

`F_e = 3*2^37 + sum_(t=0)^(N-1) (2^(S'_t)-2^(S_t))3^(-t) mod 2^N`.

For `N=56`, `e>=56` implies `n_e=b_e-1>=87`, hence every physical source in
that range must satisfy the independent actual-word overlap restriction

`sum_(t=0)^55 (2^(S'_t)-2^(S_t))3^(-t) = -3*2^37 mod 2^56`.      (G56)

This is not a reflected below-p theorem and not merely the endpoint identity in
new symbols: positivity of every acceleration has reduced the required global
cancellation to the two actual, independently anchored 56-step p-separated
prefixes.

## RL210-T2 — first-divergence selector

Suppose two strictly increasing exponent sequences agree before their first
mismatch m. In a sum with odd coefficients, the 2-adic valuation of their
first non-cancelling difference is the smaller exponent at m: that smaller
power of two occurs exactly once, while every later term has larger exponent.

The right side of (G56) has exact valuation 37. Therefore every physical
above-p source with `e>=56` has a first prefix mismatch m satisfying

`min(S_m,S'_m)=37`.

Since `S_m,S'_m>=m` and both are at most `b_m`, while
`b_23=36` and `b_24=38`, necessarily

`24 <= m <= 37`.

For every `t<m`, `S_t=S'_t`, equivalently `h_t=h_(p+t)`. At m one of the two
heights is exactly `b_m-37`, and the other is strictly smaller.

At `m=24`, `b_24=38`, so the exponents are `{37,38}`. An exact modulo-`2^40`
finite continuation check using only strict increase and `S_t,S'_t<=b_t`
excludes the orientation `S_24=37<S'_24=38`. Hence if the first mismatch is 24,
necessarily

`S'_24=37<S_24=38`, equivalently `h_(p+24)=1` and `h_24=0`.

The finite orientation check is reproduced by
`verification/verify_rl210_global_prefix_overlap.py`; it does not assert that the
remaining orientation is physically realizable.

## RL210-T3 — exact short-offset prefix locks

For a current necessary source with `1<=e<56`, reduce `F_e` modulo
`2^(n_e+1)`. If `n_e<37`, the fixed `3*2^37` term vanishes. When additionally
`b_(e-1)<n_e`, every paired term before e has exponent strictly below `n_e`.
Any earlier root/p-shift mismatch would therefore force `v2(F_e)<n_e`, contrary
to the exact endpoint valuation. Hence all pairs before e agree. The unpaired
root term at e must then have exponent exactly `n_e`, otherwise the valuation
would exceed `n_e`. Since source height one already gives `S'_e=n_e`,

`S_t=S'_t for 0<=t<=e`, equivalently `h_t=h_(p+t)` on that whole prefix.

On the exact current small-offset frontier, this criterion applies at `e=4` and
`e=16`. The inherited noncarry K-increment identity then gives

`K_0=K_1=...=K_(e+1)=2^37`

for either such physical source. No reflected tau34 source at phase e is used.

## Scope

These are necessary global-prefix conditions, not physical-incidence proofs or
rank deletions. They select no eta class, 011/111 state, terminal sign, or
valuation. They prove no H21 charge, no contradiction of `(37,0,23,-1)`, no Gate
A/B closure, and no global nontrivial-cycle exclusion.
