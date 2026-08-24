# RL20 — final-return 3-adic address does not by itself select continued-fraction classes

Date: 2026-08-20

## Status

**ANALYTIC NO-GO LEMMA + EXACT FINITE WITNESS, REPAIRED AFTER RL20 PHASE-PACKING.**

This does **not** prove RL. It identifies precisely why the direct proposal

`final-return 3-adic discrete-log address + continued-fraction gate`

cannot, without an additional global ownership/divisibility input, eliminate the remaining reduced slope classes.

The first version overstated the `(n,t)=(1,1)` close as compatible with both surviving root classes modulo `9`.  RL20's later theorem that every actual cycle phase is nonzero modulo `3` removes the `R#==7 mod9` version.  The no-go conclusion nevertheless survives because the hard class `R#==91 mod144` still supports the exact `(1,1)` endpoint above the external floor.

## 1. What the two ingredients actually see

The RL20 continued-fraction gate depends only on the total exponents. Write

`g=gcd(A,L)`, `p=A/g`, `q=L/g`.

It constrains the reduced slope `p/q`.

The RL-L36 final return instead has local data

`2^t R# + 1 = 3^n q_close`,

`n=v3(2^t R#+1)`,

with `t` odd, `gcd(q_close,6)=1`, the strict-high condition `2^(n+t)>3^n`, and the nested discrete-log address

`t = lambda_n(R#) mod 2*3^(n-1)`.

In the compressed bookkeeping,

`A-L = sum_j t_j`.

Therefore the only immediate connection from the closing address to the totals is

`t_close <= A-L`.                                                    (R20D.1)

There is no congruence tying `t_close` to `A-L`, `p`, `q`, or `g`.

## 2. Correct exceptional hard weak-close branch: R# == 91 mod144, n_close=t_close=1

RL20 phase packing proves that every actual phase state is nonzero modulo `3`.

For `n_close=1`, necessarily `s=1`, `mu=0`, so the closing anchor is the actual physical predecessor

`y_close=2q_close-1`.

Hence `3 does not divide y_close`, which forces

`2^t R# == 2 (mod 9)`.

Therefore an `n_close=1` close has

- `t == 1 (mod 6)` if `R# == 1 (mod 9)`;
- `t == 3 (mod 6)` if `R# == 7 (mod 9)`.

In the hard root branch `s_root=2,t_exit=1`, the inherited root classes reduce to

`R# == 43 or 91 (mod 144)`.

Thus `t_close=1` survives only in

`R# == 91 (mod 144)`.

This one class is enough for the endpoint/CF no-go.  Freeze any sufficiently large lift of `91 mod144`.  Then

`v3(2R#+1)=1`,

`q_close=(2R#+1)/3 == 1 (mod3)`,

and the physical closing predecessor

`y_close=2q_close-1=(4R#-1)/3`

is nonzero modulo `3`, lies strictly above `R#`, and satisfies the strict-high inequality `4>3`.

So **every total exponent pair with `A-L>=1` remains compatible with the full hard-root `(n,t)=(1,1)` endpoint package in the surviving `91 mod144` class**, independently of its continued-fraction class.

## 3. Even the n_close>=2 branch does not select large slope classes

The obstruction is not confined to `n=1`.

Freeze the hard root class

`R# = 91 mod144`.

This has `R# mod16=11`, so the hard root departure satisfies

`v2(R#+1)=2`

and `t_exit=1`.

Choose a lift of this class with

`v3(8R#+1)=2`.

There are infinitely many such lifts: modulo `27`, the class modulo `9` has three lifts and only one raises the valuation above `2`. By CRT with the fixed modulo-16 root class, arbitrarily large exact-valuation lifts exist.

For such a root take

`n_close=2`, `t_close=3`.

Then the level-2 discrete-log requirement for `R#=1 mod9` is exactly `t=3 mod6`; exact valuation is built into the lift. Also

`2^(2+3)=32>9`,

and for sufficiently large `R#` the closing anchor is strictly above the root. Therefore any total pair with

`A-L>=3`                                                        (R20D.2)

is compatible with a genuine `n_close>=2` RL-L36 endpoint witness.

The exact verifier freezes the same external-floor hard-root witness already used in the radius-bridge certificate,

`R#=2361183241434822606907`,

for which both `(n,t)=(1,1)` and `(2,3)` are exact and the `(1,1)` physical predecessor is nonzero modulo `3`.

## 4. Consequence for the continued-fraction route

For a reduced slope class `(p,q)`, scaling by `g` gives

`A-L=g(p-q)`.

Therefore:

- the surviving hard `(1,1)` endpoint is compatible whenever `g(p-q)>=1`;
- the explicit `n>=2` endpoint `(2,3)` is compatible whenever `g(p-q)>=3`.

Every large above-`log_2 3` convergent has `p-q` enormous. In particular all the recorded RL20 convergents after `2/1` already have `p-q>=3`.

So the final-return address, treated only as endpoint arithmetic plus the sum relation (R20D.1), excludes **no** large continued-fraction class and no gcd class.

## 5. What extra input is now known to be indispensable

A useful coupling must make the closing address interact with something genuinely global, for example:

1. `D|Q` together with the exact identity `R#=Q/D`, not merely the local residue of `R#`;
2. minimum-state ownership of the closing/root rotations;
3. a weighted difference of two `D`-divisible rotations;
4. a global restriction on the *other* exit exponents `t_j`, strong enough that `t_close` is no longer a free summand of `A-L`.

The naive direct route

`CF class -> total A,L -> final-return address -> contradiction`

is therefore still retired.

Verifier: `verify_rl20_final_return_cf_decoupling.py`.
See also: `RL20_FINAL_RETURN_PHASE_COMPATIBILITY.md`.
