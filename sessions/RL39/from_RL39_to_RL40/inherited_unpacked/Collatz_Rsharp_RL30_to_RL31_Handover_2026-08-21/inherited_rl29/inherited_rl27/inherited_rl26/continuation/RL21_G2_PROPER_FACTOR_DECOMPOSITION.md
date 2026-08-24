# RL21 — exact `g=2` balanced factor decomposition and a proper-factor countermodel

Date: 2026-08-20

## Status

Section 1 is **ANALYTIC**. Section 2 is an **EXACT FINITE CERTIFICATE**.

This strengthens the balanced-return pruning. In the half-balanced case `g=2`, full cycle divisibility splits into two coprime proper-factor conditions. One of them can hold exactly, with an integer near-minimum state gap, while all least-state slope geometry remains valid and radius is large. Therefore the `X+Y` gap factor alone is not the missing bridge.

## 1. Exact two-factor decomposition

Let

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`,

and let a balanced word split as

`d=uv`, `|u|=|v|=a`, `|u|_1=|v|_1=ell`.

Write

`U=Q(u)`, `V=Q(v)`.

Then

`D=X^2-Y^2=(X-Y)(X+Y)`,

and

`Q(d)=YU+XV`.

Because `X-Y` and `X+Y` are odd and

`gcd(X-Y,X+Y)=gcd(X-Y,2Y)=1`,

the two factors are coprime.

Modulo the two factors,

`Q(d) == Y(U+V) (mod X-Y)`,

`Q(d) == Y(U-V) (mod X+Y)`.

Since `Y` is a unit modulo both factors,

> **`D|Q(d)` iff both**
>
> `X-Y | U+V`                                               (R21F.1)
>
> and
>
> `X+Y | U-V`.                                              (R21F.2)

For an actual cycle with least state `R` and balanced state `x`, the block equations give

`(X-Y)(R+x)=U+V`,                                           (R21F.3)

`(X+Y)(x-R)=U-V`.                                           (R21F.4)

Thus the two proper-factor quotients are exactly the state sum and state gap.

This makes the arithmetic bottleneck precise:

- `X+Y` controls the **relative** low-state gap;
- `X-Y` controls the **absolute** low-state level through the sum.

A proof that uses only R21F.2 is missing half of the global cycle condition.

## 2. Exact countermodel to the `X+Y` factor alone

Take

`a=65`, `ell=41`, so `A=130`, `L=82`,

`X=2^65`, `Y=3^41`, and

`1 < (X/Y)^2 <16/15`.

Let

`u = 11011011010110110110101101110011011100110110110101110101011011100`,

`v = 11111111110111000111110011011011110101010111110011101000011100000`.

Both words have length `65` and weight `41`.

The exact verifier establishes:

1. every proper prefix of both `u` and `v` is supercritical:
   `3^(P_m)>2^m` for `1<=m<65`;
2. `d=uv` is primitive;
3. every proper suffix of `d` back to the root is subcritical;
4. the exact rational fixed orbit `R=Q(d)/D` is positive with a unique least rational phase at the root;
5. the canonical half cut is exactly balanced, `E=(0,0,0)`;
6. the half-cut state satisfies exactly

   `x-R=4`,                                                  (R21F.5)

   and `x<(16/15)R`;
7. exactly

   `Q(u)-Q(v)=4(X+Y)`,                                      (R21F.6)

   so the gap-factor condition R21F.2 holds with the smallest universally allowed balanced integer gap `4`;
8. nevertheless

   `X-Y does not divide Q(u)+Q(v)`,                          (R21F.7)

   hence `D does not divide Q(d)` and the absolute state level `R` is nonintegral;
9. the balanced half-rotation has cyclic adjacent-transposition distance `340`;
10. the minimum distance over all nontrivial cyclic shifts is `48`.

Numerically only for orientation,

`R ~=458.673851...`,

`x/R ~=1.00872079...`.

The exact content is R21F.5--R21F.7, not the decimals.

## 3. What this falsifies and what survives

This certificate formally retires the candidate statement

> balanced least-state geometry + `X+Y | Q(u)-Q(v)` + integer near-minimum state gap forces radius `<=3` or contradiction.

It does not falsify the full RL bridge because the other coprime factor `X-Y` fails.

The viable `g=2` target is therefore the **simultaneous two-factor problem**:

> Can the least-state/root-return constraints rule out simultaneous
>
> `X-Y | Q(u)+Q(v)` and `X+Y | Q(u)-Q(v)`
>
> for distinct equal-density blocks?

Equivalently, can one show that the two exact quotients `R+x` and `x-R` cannot simultaneously be admissible integer cycle-state data?

This is sharper than full-`D` rotation comparison and sharper than the gap factor alone.

Verifier: `verify_rl21_g2_proper_factor_countermodel.py`.
