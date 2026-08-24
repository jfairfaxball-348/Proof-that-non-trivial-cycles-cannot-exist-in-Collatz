# RL21 — balanced-return divisibility: rotation redundancy, proper-factor form, and a strengthened countermodel

Date: 2026-08-20

## Status

Sections 1--3 are **ANALYTIC**. Section 4 is an **EXACT FINITE CERTIFICATE**.

This note sharply narrows the RL20 balanced-return programme.

The main conclusions are:

1. `D|Q` for a second rotation is not an independent condition; rotation divisibility is automatic from the first rotation.
2. In the special balanced case `g=2`, the useful global condition is the proper-factor equation

   `(X+Y)(x-R#)=Q(u)-Q(v)`.

3. Even a very strong package of least-root/suffix slope geometry plus an exact long balanced return does **not** force bounded rotation radius. A length-970 rational fixed-orbit model satisfies all those local/ordered constraints and has all-rotation minimum distance `110`, while failing only the genuine integer-cycle condition `D|Q`.

Thus the live balanced-return distinction is now isolated to **integrality / proper-factor congruence / state ownership**, not to local slope geometry or a second copy of full-`D` divisibility.

## 1. Rotation divisibility is automatic

Split a full word as `d=uv`, with

- `|u|=m`, `|u|_1=p`,
- total length `A`, total weight `L`,
- `U=Q(u)`, `V=Q(v)`,
- `D=2^A-3^L`.

The concatenation identity gives

`Q(uv)=3^(L-p) U + 2^m V`,

`Q(vu)=3^p V + 2^(A-m) U`.

Therefore

`2^m Q(vu)-3^p Q(uv)=D U`.                                (R21B.1)

Because `gcd(6,D)=1`, both `2^m` and `3^p` are units modulo `D`. Hence

> **`D|Q(uv)` if and only if `D|Q(vu)`.**                 (R21B.2)

So the phrase “two `D`-divisible rotations” must not be treated as two independent arithmetic constraints. A single `D`-divisible word already makes every rotation `D`-divisible.

For an actual cycle with states

`R=Q(uv)/D`, `x=Q(vu)/D`,

R21B.1 is just the prefix state equation

`2^m x-3^p R=U`.                                           (R21B.3)

Likewise

`Q(vu)-Q(uv)=D(x-R)`.                                      (R21B.4)

Thus the most direct “nonzero multiple of `D` trapped below `D`” attempt cannot come merely from the fact that the balanced state is close to the least state: the multiplier is the positive integer state gap `x-R`.

## 2. Balanced canonical cut

Now assume the cut is canonical and exactly balanced:

`m=j a`, `p=j ell`,

where `A=g a`, `L=g ell`, `X=2^a`, `Y=3^ell`, and `z=X/Y`.

Then R21B.3 becomes

`X^j x-Y^j R=U`.                                           (R21B.5)

The complementary segment gives

`X^(g-j) R-Y^(g-j) x=V`.                                   (R21B.6)

The near-resonant least-state geometry still gives

`R < x <= z^(g-j) R`,                                      (R21B.7)

so

`0 < x-R <= [z^(g-j)-1]R`.                                 (R21B.8)

In an actual cycle both balanced endpoints are odd; since every phase is nonzero modulo `3`, the state gap is at least `2`, and is at least `4` in the inherited `R# == 1 (mod 6)` branch.

This is genuine integrality/ownership information. It is absent from rational fixed-orbit models.

## 3. Special proper-factor form when `g=2`

Take `g=2` and a proper balanced cut `j=1`. Then

`d=uv`, `|u|=|v|=a`, `|u|_1=|v|_1=ell`.

The two block equations are

`X x=Y R+U`,

`X R=Y x+V`.

Adding and subtracting gives

`(X-Y)(R+x)=U+V`,                                          (R21B.9)

`(X+Y)(x-R)=U-V`.                                          (R21B.10)

Thus the balanced integer state gap is exactly the quotient

> **`x-R = [Q(u)-Q(v)]/(X+Y)`.**                           (R21B.11)

This exposes the relevant proper factor. The factor `X+Y` divides the full denominator

`D=X^2-Y^2=(X-Y)(X+Y)`.

For a genuine cycle, `X+Y | Q(u)-Q(v)` and the quotient is a positive integer state gap. This is the first place where `D|Q` contributes something not already visible in the rational least-state geometry.

However, no bounded-radius conclusion follows from the local geometry alone; Section 4 supplies an exact countermodel.


## 3A. Two elementary integrality/ownership consequences

### Near-minimum odd states are `3 mod 4`

Let `R` be the least state of a nontrivial positive cycle and let `x` be an odd cycle state with

`R < x < (16/15)R`.

If `x == 1 (mod 4)`, its first two full-parity bits are `10`, and after those two steps the state is

`(3x+1)/4 < (4/5)R+1/4 < R`

for every nontrivial least state `R>=2`. This contradicts leastness. Hence

> **every balanced near-minimum odd state satisfies `x == 3 (mod 4)`.** (R21B.12)

The same argument applied to the least odd state itself gives `R == 3 (mod 4)` in every nontrivial positive cycle. Therefore every balanced state gap obeys

> **`4 | (x-R)` and in particular `x-R >=4`.**              (R21B.13)

This strengthens the parity-only gap `>=2` without using the inherited `k=0` residue class.

### First block disagreement equals the 2-adic gap valuation when `g=2`

Let `u,v` be distinct binary words of the same length `a` and weight `ell`, and let `r` be their first differing zero-based bit position. Then

> **`v2(Q(u)-Q(v))=r`.**                                   (R21B.14)

Proof: all contributions before `r` cancel because the two words have equal total weight and identical prefixes there. At bit `r`, exactly one word contributes `2^r` times an odd power of `3`; every later contribution is divisible by `2^(r+1)`.

In the balanced `g=2` cycle equation R21B.10, `X+Y` is odd. Hence

> **`r = v2(x-R)`.**                                      (R21B.15)

So integrality identifies the common-prefix length of the two half-cycle parity blocks exactly with the 2-adic valuation of the near-minimum state gap. This is a genuine ownership invariant absent from the rational countermodels.

In particular R21B.13 implies `r>=2`. In the inherited hard root class `R == 11 (mod 16)`, if the balanced state also starts in the hard `1101` class then `16 | (x-R)` and `r>=4`; if instead it begins with at least three consecutive odd bits, then its residue is `7 (mod 8)` while `R ==3 (mod8)`, forcing `v2(x-R)=2` and hence `r=2`.

## 4. Strengthened balanced-return rational countermodel

### 4.1 Reduced counts

Take

`a=485`, `ell=306`, `g=2`,

so

`A=970`, `L=612`,

`X=2^485`, `Y=3^306`,

and exactly

`1 < lambda=(X/Y)^2 < 16/15`.

### 4.2 First block

Construct a length-485 weight-306 word `B` by setting

`P_0=0`,

for `1<=m<485`, `P_m` is the least integer with `3^(P_m)>2^m`,

and `P_485=306`.

Then `B_m=P_(m+1)-P_m`.

Thus every proper prefix of `B` is supercritical,

`3^(P_m)>2^m` for `1<=m<485`,

while the full block is the first exact reduced-slope undercritical cut

`2^485>3^306`.

The block begins `1101...` and ends `...10`.

### 4.3 Second block

Let `C` be obtained from `B` by performing the following 100 pairwise nonoverlapping adjacent swaps `01 -> 10`, using zero-based positions inside `B`:

`[325,75,157,390,422,70,81,200,471,116,233,333,241,384,251,392,67,289,59,433,306,281,108,463,460,327,295,51,371,173,411,254,387,189,35,403,159,373,48,319,360,86,352,227,230,346,94,5,154,279,37,8,273,181,130,186,43,56,363,222,430,417,205,292,92,357,466,132,111,162,382,419,322,214,32,265,195,474,349,167,398,97,479,308,414,40,170,119,100,211,121,216,428,303,203,10,105,314,165,468]`.

These swaps preserve block length and weight. They also preserve the beginning `1101...` and ending `...10`.

Set

`d=BC`.

### 4.4 Exact properties

The verifier proves all of the following exactly.

1. `d` is primitive.
2. `D=2^970-3^612>0` and `lambda<16/15`.
3. Both canonical blocks have weight `306`, so the block imbalance path is

   `E=(0,0,0)`.

   Thus the cut at 485 is an exact balanced return.
4. The word begins `1101...`; the balanced rotation also begins `1101...`; the full word ends `...10`.
5. Every proper root prefix through length 484 is supercritical:

   `3^(P_m)>2^m`.
6. Every proper suffix back to the root is subcritical:

   `2^k>3^(E_k)`.
7. The exact rational fixed orbit `R=Q(d)/D` is positive and has a **unique least rational phase at the root**.
8. The balanced phase `x` at cut 485 satisfies

   `R < x < (16/15)R`.

9. The cyclic adjacent-transposition distance between the two balanced halves is `200`.
10. Among all nontrivial cyclic shifts of the 970-bit word, the minimum adjacent-transposition distance is exactly

    `110`, attained at shift `65`.
11. `D does not divide Q(d)`.

So this model obeys the least-state rational orbit geometry, the long root prefix envelope, the suffix envelope, the exact balanced return, the near-minimum balanced phase, primitivity, and the endpoint bit grammar, while remaining very far outside radius 3.

It is **not** an RL object because its fixed state is nonintegral. Equivalently, the proper-factor quotient in R21B.11 is not the required integer cycle-state gap and the full `D|Q` condition fails.

## 5. Strategic consequence

Retire the following candidate arguments unless they add new hypotheses:

1. “a second `D`-divisible rotation is a second independent divisibility condition”;
2. “balanced return plus least-state slope envelopes force radius `<=3`”;
3. “balanced return plus a long supercritical-prefix window forces bounded transport radius”.

The sharpened live target is:

> **Use integrality/state ownership to obstruct the proper-factor quotient.**

For `g=2`, this means attacking

`X+Y | Q(u)-Q(v)`

under the exact least-state and endpoint constraints, with quotient `x-R` a positive admissible integer.

For general `g`, seek the analogous proper cyclotomic factor/state-gap relation rather than reusing full-`D` rotation divisibility.

Verifier: `verify_rl21_balanced_return_countermodel.py`.
