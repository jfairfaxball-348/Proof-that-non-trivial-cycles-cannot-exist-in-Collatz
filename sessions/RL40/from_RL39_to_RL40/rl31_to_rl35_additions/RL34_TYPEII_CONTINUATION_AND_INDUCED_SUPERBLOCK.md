# RL34 — type-II continuation rigidity and induced-superblock support

Date: 2026-08-21

## Status

**ANALYTIC for `R>=800`**, with an exact finite symbolic certificate. The continued-fraction consequence additionally uses the inherited external computational input `R>=2^71`.

This supersedes RL33's coefficient while retaining its induced-block successor theorem.

## 1. Type-II continued high runs have first valuation exactly 1

Let `H=(4R-1)/3` and `f(x)=(9x+5)/8`. A type-II terminal high has the form

`z=f(x_last)` with `x_last<H`, hence `z<f(H)`.

If the high run continues, the next odd state must still be at least `H`. But if the outgoing valuation were at least 2,

`next <= (3z+1)/4 < (3f(H)+1)/4 < H`,

because

`H-(3f(H)+1)/4=(10R-37)/48>0`.

Therefore every continued type-II high run begins with valuation exactly `1`.

For consecutive high states `a,b`, the exact correction-pair identity is

`F(a)F(b)=1+(2^nu+3)/(9a)`.

Hence the type-II first-pair bounds improve to

`P_II,1=P_II,2=(12R+2)/(12R-3)`,

and, using `a>=f^3(R)` for `k=3`,

`P_II,3=(6561R+12325)/(6561R+9765)`.

## 2. The direct `k=3` exceptional block forces a `k=2` successor

Let

`a2=(256R-319)/243`,

`a1=(32R-23)/27`.

These are the `k=3/k=2` and `k=2/k=1` low-chain boundaries.

For the direct type-II `k=3,h=1` block, call it `E`, the next low is

`g3(x)=(2187x+3767)/2048`.

The exact certificate proves

`g3(R)>=a2`,

`g3(a2)<a1`.

Thus every `E` block is followed by a block whose low-chain length is exactly `k=2`.

If that successor is itself the direct type-II `k=2,h=1` block, its low map is

`g2(y)=(243y+319)/256`.

The two correction products collapse exactly:

`P_E(x) P_T(g3(x))`

`=(531441x+1568693)/(531441x)`.

This is decreasing in `x`, so for `x>=R` define the induced superblock bound

`S(R)=(531441R+1568693)/(531441R)`.

Also retain

`T(R)=256R/(256R-319)`

for the direct type-II `k=2,h=1` block.

## 3. New supporting line

The support anchors are now

- `T`: `(n,V)=(5,8)`;
- induced `S=E+T`: `(n,V)=(12,19)`.

Solving for the affine exponents gives the local comparison

`P <= T^(12V-19n) S^(8n-5V)`.

The exceptional `E` block is never used alone: it is paired with its forced `k=2` successor. If that successor is `T`, use the exact `S`; otherwise use the product of the safe `E` and successor bounds.

The verifier checks:

- every non-`E` residue seed `h=1,...,12`;
- every `E+k=2` successor seed;
- the special `E,h=13` representative needed because `E,h=1` is paired rather than individually supported;
- the period-12 extension;
- monotonicity in actual valuation.

For `h->h+12`, the support gains exactly `S`, while the product gains at most `P_HH^6`; the exact certificate proves

`P_HH^6 <= S`.

## 4. Global theorem

After the cyclic itemization and multiplication,

`lambda <= T^(12A-19L) S^(8L-5A)`.

Put

`beta=log(3)/log(2)` and `x=log(lambda)/L`.

Using

`A/L=beta+x/log(2)`,

we obtain

`x <= N/D`,

where

`N=(12beta-19)log T +(8-5beta)log S`,

`D=1-(12log T-5log S)/log 2`.

The asymptotic coefficient is

`lim R*x`

`=(12beta-19)*(319/256)`

` +(8-5beta)*(1568693/531441)`

`=0.246297537816914843649363119811...`.

## 5. Continued-fraction consequence

At the inherited external floor `R0=2^71`, rigorous rational log intervals and exact continued-fraction reconstruction give

> **`L/gcd(A,L) >= 57,641,137,625`.**

The next relevant denominator remains

`65,470,613,321`,

so this is a quantitative improvement, not a qualitative CF-gate crossing and not RL closure.

Verifier: `verify_rl34_typeII_continuation_support.py`.
