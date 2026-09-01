# RL215 — complementary-arc positivity and exact e=16 two-sided root window

Date: 2026-09-01. Classification: **proved analytic mathematics plus exact finite arithmetic certificate** at the scopes separated below.

All physical implications remain conditional on a physical H21 realization of the sole inherited high branch `(37,0,23,-1)`. Arithmetic root candidates are not physical words, populations or cycles.

## 1. Complementary-arc identity

Retain
`A=217976794617`, `L=137528045312`, `p=65470613321`,
`u=103768467013`, `z=L-p=72057431991`, `K0=2^37`, and `Ap-uL=1`.

RL214 phase-aligns the H21 root with the complete owned word and proves
`y_p-y_0=K0`. The remaining `z=L-p` accelerated odd steps return from `y_p`
to `y_L=y_0` and use total acceleration exponent `A-u`.

Let `P_z>0` be the ordinary affine numerator of this nonempty complementary arc.
Exact iteration gives

`2^(A-u)y_0 = 3^z y_p + P_z
             = 3^z(y_0+K0)+P_z`.

With
`gamma=2^(A-u)/3^z`, this is

`(gamma-1)y_0 = K0 + P_z/3^z > K0`.                  (C1)

Thus the complementary arc supplies the inequality opposite to RL214's positive
p-arc cap:

`y_0 > K0/(gamma-1)`.                                (C2)

This uses complete-cycle return and positivity of a different full arc. It is not
`Q mod D=0`, the collapsed RL201 endpoint moment, or the RL214 p-arc positivity
inequality rewritten.

## 2. Portable rational lower bound

Write `delta=A ln2-L ln3=ln(lambda)`. The inherited defect is
`0<delta<2^-40`. From `Ap-uL=1` and `z=L-p`,

`L ln(gamma) = ln2 + z delta`.                        (C3)

Use the positive atanh expansion

`ln2 = 2 sum_(n>=0) 1/((2n+1)3^(2n+1))`.

Keeping `n=0,...,6` and bounding the remaining geometric tail with
`1/(2n+1)<=1/15` gives the exact rational upper bound

`ln2 < U := 13274467117/19151007876`.

Hence

`0 < ln(gamma) < x := (U+z/2^40)/L < 1`.

For `0<x<1`, the power-series comparison
`e^x < 1/(1-x)` gives

`gamma-1 < x/(1-x)`.

Combining with (C2),

`y_0 > K0(1-x)/x
     = 99502176389773321825857103001223487471747072
       /3993850848813907800727`.

Therefore every physical root in this scope satisfies the integer lower bound

**`y_0 >= 24,913,843,845,551,577,787,381`.**          (C4)

Together with the inherited RL214 upper bound,

**`24,913,843,845,551,577,787,381
   <= y_0
   <= 31,285,589,992,934,194,300,574`.**              (C5)

## 3. Exact projection onto the RL214 e=16 progressions

RL214 supplies 45,046 H21-compatible exact prefixes. For each prefix,

`y_0=y_0^* + (3*2^58)k`

with the inherited upper cap giving `kmax=36180` or `36181`.

Projecting (C4) exactly onto each progression gives:

- `kmin=28812` for **26,133** prefixes;
- `kmin=28813` for **18,913** prefixes.

Joint lower/upper counts are:

- `(kmin,kmax)=(28812,36180)`: **26,133** prefixes;
- `(28813,36180)`: **8,519** prefixes;
- `(28813,36181)`: **10,394** prefixes.

Thus the two-sided interval contains exactly **331,935,455** bounded arithmetic
root candidates before the ordinary terminal Hensel filter.

The inherited terminal condition removes exactly **170** candidates inside this
new window, one candidate in each of 170 distinct prefixes. Exactly

**331,935,285**

bounded arithmetic candidates remain.

Relative to RL214's post-terminal family of 1,629,818,931, the new independent
complementary-arc inequality removes **1,297,883,646 arithmetic candidates**
(about 79.63%) without brute-force enumeration.

Every one of the 45,046 prefixes survives, with 7,367 to 7,369 candidates after
the terminal filter. Both H21 states survive. Exact post-filter candidate counts are:

- mod18 class 0: 107,901,476;
- mod18 class 8: 58,066,202;
- mod18 class 9: 107,901,377;
- mod18 class 17: 58,066,230.

State totals are 215,802,853 for 011 and 116,132,432 for 111.
All 469 RL212 reachable eta residues modulo2187 remain represented.

The canonical exact witness digest is
`f059976b3627bde3b97e009b2f7ae6dd055d23eee7e5a641704fa61663962fe7`.

## 4. Scope and consequence

RL215 supplies a genuinely independent full-word/arc datum of the kind requested
by the RL215 target: positivity of the complementary return arc creates a global
lower root bound and a two-sided finite window.

It does **not** determine `Q mod D^2` or `(Q/D) mod D`. It deletes no H21 prefix,
state, mod18 class or necessary terminal rank. The e=16 terminal rank remains
`34,124,151,203`, and the global necessary frontier remains **13,415,865,871**:
7,091,831,284 above p and 6,324,034,587 below p.

A shifted e=16 p-arc roof estimate was also checked. It is strictly weaker at the
current progression scale (its lower k threshold is 1,251 or 1,252 below (C4)),
so it supplies no additional deletion and is not promoted as a separate consumer.

No physical H21 incidence/charge, branch contradiction, Gate closure or global
nontrivial-cycle exclusion is proved.
