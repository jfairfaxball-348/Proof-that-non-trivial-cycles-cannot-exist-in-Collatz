# RL45 — reduced phase polynomial and obstruction to the naive resultant benchmark

Date: 2026-08-22

## Status

Sections 1–2 are **analytic** consequences of the audited RL43 one-excursion phase bridge.  Section 3 is an **exact finite counterexample/certificate** to a proposed universal resultant-size strategy.

This does not produce an RL counterexample.  It shows that the RL45 target

`0 < |Res(3T^q-2,P)|_(3') < X-Y`

cannot be proved from the current one-excursion geometry + proper-factor constraints alone.

## 1. Exact reduction modulo the short binomial

Let

`f(T)=3T^q-2`, `q=a-ell`,

and

`P(T)=4+3 sum_r (T^(b_r)-T^(c_r))`,

with

`c_r-b_r=k_r q`, `k_r>=1`.

Write

`b=sq+r`, `0<=r<q`.

Modulo `f`,

`T^q = 2/3`,

so each run pair reduces exactly to

`3(T^b-T^(b+kq))`

`= [2^s(3^k-2^k)/3^(s+k-1)] T^r` modulo `f`.

Thus the degree-`<q` rational remainder has **positive coefficients**.

## 2. New no-collision lemma for one excursion

For a run of the full half word `v`, let

- `t` be its start position;
- `m` its one-based start rank;
- `Z=t-(m-1)` the number of zero bits preceding the run.

Then

`b=a m-ell t`

` = (a-ell)m + ell(1-Z)`

` = q m + ell(1-Z)`.

Hence

`b mod q = ell(1-Z) mod q`.

In the one-excursion geometry, if the local excursion has `z` zero columns and the terminal synchronized zero suffix has length `t_out`, then

`q=z+t_out`.

The local word ends in zero, so every run starts after a distinct zero count

`0<=Z<=z-1<=q-1`.

Because `gcd(ell,q)=1`, distinct `Z` give distinct residue classes `b mod q` (the `q=1` case is vacuous, with at most one class).

Therefore:

> **After reducing `P` modulo `3T^q-2`, different one-runs do not collide with each other.**

There is no hidden coefficient cancellation available from collecting run residues.  The only possible collision with the constant term is the unique run with `Z=1`, for which `b=0 mod q`.

This sharpens the RL44 observation that all reduced pair coefficients are positive: in the live one-excursion geometry they are also supported on distinct run residue classes.

## 3. Exact obstruction from the audited `(65,41)` countermodel

Use the audited RL43 proper-factor countermodel

`(a,ell,q)=(65,41,24)`.

It satisfies:

- near resonance;
- `gcd(a,ell)=1`;
- one canonical positive excursion;
- the exact proper-factor identity `U-V=4(X+Y)`;
- all current one-excursion geometric/run constraints;
- but intentionally fails the missing full-denominator phase condition.

For its phase polynomial:

- `deg(P)=405`;
- the exact remainder modulo `f=3T^24-2` has degree `23`;
- the 23 runs occupy 23 distinct reduced exponent classes.

The companion verifier computes the exact integer resultant both directly and through the rational remainder.  Removing all factors of `3` gives

- 3-free resultant bit length: `652`;
- `(X-Y)` bit length: `59`;
- in fact

`|Res(f,P)|_(3') > 2^592 (X-Y)`.

For the same countermodel the exact gcd is

`gcd(|Res(f,P)|_(3'), X-Y)=1`.

Therefore the desired universal estimate

`|Res(f,P)|_(3') < X-Y`

is false by an enormous margin on the current admissible proper-factor geometry.

## 4. Interpretation

This does **not** refute the phase bridge.  An actual RL solution would additionally satisfy

`P(rho)=0 mod (X-Y)`,

which the countermodel does not.

It does refute a proof plan in which one hopes to bound the 3-free resultant below `X-Y` using only:

- short-binomial reduction;
- run pairing `c-b=kq`;
- positivity;
- support `R<=e+1`;
- near resonance;
- the proper-factor one-excursion geometry.

The coefficient-height problem is not a minor technical loss: the reduced norm can be hundreds of bits too large even at `(65,41)`.

A viable radius-3 transplant must therefore use extra arithmetic beyond a universal absolute-size bound.  More plausible replacements are:

1. control the **gcd** of `Res(f,P)` with the comparator resultant `Res(f,2T^ell-1)=X-Y`, rather than the absolute size of `Res(f,P)`; the countermodel's gcd is already `1`;
2. more sharply, derive a **same-root subresultant/Bezout obstruction** using `f`, `L=2T^ell-1`, and `P` simultaneously.  A plain gcd of two resultants can contain spurious primes coming from different roots of `f`; the full phase condition requires `P` to vanish at the specific root shared by `f` and `L` modulo `X-Y`;
3. exploit the full phase divisibility to force a restricted coefficient congruence before taking any global norm.

The original RL19 argument succeeds because its sparse polynomial is tiny enough that a raw norm bound works.  RL45 now has an exact reason that the same quantitative step does not transplant directly.
