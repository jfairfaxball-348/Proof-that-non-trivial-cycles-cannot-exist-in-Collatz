# RL20 — final-return phase compatibility sharpens the hard root branch

Date: 2026-08-20

## Status

**ANALYTIC**, using the RL20 theorem that every phase state of a nontrivial positive cycle is nonzero modulo `3`, plus the inherited k=0 root residue classes and RL-L36 final-return equation.

This does not prove RL.  It repairs one overstatement in the earlier RL20 final-return/CF decoupling note and isolates the unique hard-root branch in which the closing exponent `t_close=1` can occur.

## 1. The missing physical-state condition when n_close=1

RL-L36 writes the final return as

`2^t R# + 1 = 3^n q`,

with `gcd(q,6)=1` and `n=s+mu` for the physical final plateau start.

If

`n_close=1`,

then necessarily

`s=1`, `mu=0`.

So the canonical closing anchor is not merely an auxiliary red anchor: it is the actual physical odd predecessor of the root,

`y_close = 2 q - 1`.

RL20 proved that every phase state of a nontrivial positive cycle is nonzero modulo `3`.  Therefore

`3 does not divide y_close`.

Since `q` is a 3-adic unit, this forces

`q == 1 (mod 3)`.

Dividing the exact return equation by `3` modulo `9` gives the equivalent phase-compatibility congruence

`2^t R# == 2 (mod 9)`.                                      (R20F.1)

## 2. Exact n_close=1 address modulo 6

The powers of `2 mod 9` have order `6`.  Since the inherited k=0 branch has

`R# mod 9 in {1,7}`,

(R20F.1) gives:

- if `R# == 1 (mod 9)`, then `t_close == 1 (mod 6)`;
- if `R# == 7 (mod 9)`, then `t_close == 3 (mod 6)`.

Thus the earlier statement that `(n,t)=(1,1)` is endpoint-compatible with both surviving mod-9 root classes is false once the new RL20 phase-state theorem is imposed.

For `R# == 7 (mod 9)`, the formal `t=1` return has an actual predecessor divisible by `3`, so it cannot be a cycle phase.

## 3. Consequence in the hard root branch

The hard root branch

`s_root=2`, `t_exit=1`

has

`R# == 11 (mod 16)`.

Intersecting this with the inherited six k=0 classes modulo `144`

`{7,43,55,79,91,127}`

leaves exactly

`R# == 43 or 91 (mod 144)`.

These are respectively

`43 == 7 (mod 9)`,

`91 == 1 (mod 9)`.

Hence:

- hard class `91 mod 144`: an `n_close=1` return has `t_close == 1 (mod 6)`, so `t_close=1` is possible;
- hard class `43 mod 144`: an `n_close=1` return has `t_close == 3 (mod 6)`, so `t_close>=3`.

For `n_close>=2`, inherited RL-L36 already gives `t_close>=3` by strict-highness (and in fact the level-2 address begins at `3 mod 6` for the `91` class and `5 mod 6` for the `43` class).

Therefore:

> **The only hard-root branch in which `t_close=1` can occur is**
>
> `R# == 91 (mod 144)`, `n_close=1`, `t_close=1`.            (R20F.2)

Every other hard-root final return has `t_close>=3`.

## 4. Closing-defect consequence

RL-L46 writes the closing affine error as

`e_close = 1-2^(-t_close)`

because the next/root plateau has zero 3-adic normalization valuation.

Its lower defect estimate is

`D/2^A > e_close/(R#+1)`.

Thus every hard-root branch outside the unique exceptional branch (R20F.2) satisfies

`D/2^A > 7/[8(R#+1)]`.                                     (R20F.3)

This extends the old `n_close>=2` strengthening to the entire hard `43 mod 144` class and to every non-`t=1` close in the `91 mod 144` class.

## 5. Strategic consequence

The difficult hard-root branch is now narrower than recorded in the first RL20 notes.

The final-return/CF no-go remains valid after repair: the single surviving class `R# == 91 mod 144` still supports the exact `(n,t)=(1,1)` close above the external floor, so endpoint arithmetic alone still does not select large continued-fraction slope classes.

But future global work should not call `(1,1)` universal across the hard root branch.  The genuinely weak closing branch is the single residue/address package (R20F.2).

Verifier: `verify_rl20_final_return_phase_compatibility.py`.
