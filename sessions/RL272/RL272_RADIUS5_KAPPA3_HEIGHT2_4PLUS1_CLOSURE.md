# RL272 — Radius-5 `|kappa|=3` height-two mass-four-plus-one closure

Date: 2026-09-07  
Classification: **RADIUS5_KAPPA3_SECTOR_CLOSED**

## 1. Scope

RL272 works only the sole remaining `|kappa|=3` Radius-5 topology inherited from RL271: the height-two mass-four-plus-one family.

Frozen and untouched:
- `|kappa|=5`;
- Gate A;
- the fifth retained arithmetic selector;
- selector-by-selector enumeration;
- the general Radius-n programme.

Inherited:
- `D=2^A-3^L>1`;
- full-`D` divisibility of every rotated numerator in the theorem setting;
- exact source/target reversal between `kappa=-3` and `kappa=+3`;
- `qA-mL=kappa`;
- `gcd(A,L)|3` and `gcd(m,A)|3`;
- the parity-word numerator
  `Q(d)=sum_{i:d_i=1} 2^i 3^(L-r_i)`;
- RL266's audited LMN two-logarithm cutoff mechanism;
- RL271's correction that determinant-three work must not impose the false blanket restriction `q<L`.

RL271 already closes every flat `|kappa|=3` family. This session closes only the height-two remainder.

## 2. Exact oriented normal form

Reverse source and target when necessary, so `kappa=+3`.

A height-two mass-four-plus-one flow with skew `+3` is forced to consist of:
- one positive `1,2,1` component, of signed mass `+4`;
- one separate negative singleton, of signed mass `-1`.

Cut in a zero-flow gap immediately before the positive core. After a cyclic renumbering,

`g_0=1, g_1=2, g_2=1, g_u=-1`

and all other `g_i=0`, with

`4 <= u <= A-2`.

Let `x` be the cut source word, `y=tau^m x`, and

`R_i=sum_{j=0}^i x_j`, `S_i=sum_{j=0}^i y_j`.

Because the cut median is zero,

`g_i=R_i-S_i`

and

`x_i-y_i=g_i-g_(i-1)`.

The six nonzero boundary differences are therefore forced:

- `x_0=x_1=1`, `y_0=y_1=0`;
- `x_2=x_3=0`, `y_2=y_3=1`;
- `x_u=0`, `y_u=1`;
- `x_(u+1)=1`, `y_(u+1)=0`.

At every other index `x_i=y_i`.

## 3. Exact two-term numerator identity

Let

`r=R_u`.

The four core boundary terms give

`-3^(L-1) - 2*3^(L-2) + 4*3^(L-1) + 8*3^(L-2)
 = 15*3^(L-2)`.

The negative singleton contributes

`2^u 3^(L-r-1) - 2^(u+1)3^(L-r-1)
 = -2^u 3^(L-r-1)`.

Hence the exact integer identity is

`Q(y)-Q(x)
 = 15*3^(L-2) - 2^u 3^(L-r-1)`.

Writing

`v=r-1`

gives

`Q(y)-Q(x)
 = 3^(L-r-1) (15*3^v - 2^u)`.

Since `gcd(D,6)=1`, full-`D` divisibility implies

`D | E`, where `E=15*3^v-2^u`.

The complementary representative is

`E*=15*2^(A-u)-3^(L-v)`,

and the exact relation

`2^(A-u) E - 3^v E* = -D`

shows that `D|E` iff `D|E*`.

The arc counts satisfy

`1 <= v <= u`

and

`0 <= L-v <= A-u`.

Choosing the shorter of the two physical arcs therefore gives the universal nonzero-difference bound

`D <= |E_short| <= 16*3^floor(A/2)`.

The nonzero condition is inherited from the theorem scope: a primitive nontrivial rotation gives a different binary word, and the fixed-`(A,L)` numerator map is injective.

## 4. Determinant-three analytic reduction

The determinant relation is

`qA-mL=3`.

The height-two core already forces `L>=3`, so `1<=q<=L`, and

`A/L - m/q = 3/(qL)`.

Let

`alpha=log(3)/log(2)`

and

`Lambda=A log(2)-L log(3)>0`.

### 4.1 Non-bracketing case

If

`m/q > alpha`,

then

`Lambda > 3 log(2)/q > 3 log(2)/A`.

Using `log(2)>2/3`, and `1-exp(-Lambda)>Lambda/2` for `0<Lambda<=1` (with the `Lambda>=1` case even stronger), gives

`D > 2^A/A`.

The exact integer inequalities

`2^45 > 16*45*3^22`

and

`2^46 > 16*46*3^23`

hold. On either parity class the two-step ratio improves by

`4A/(3(A+2)) > 1`

for `A>6`.

Therefore every non-bracketing candidate has

`A <= 44`.

### 4.2 Bracketing case

If

`m/q < alpha < A/L`,

the numerator bound gives

`D/2^A <= 16*3^floor(A/2)/2^A`.

For `A>=25` this is `<1/2`, hence

`Lambda <= 2D/2^A
        <= 32 (sqrt(3)/2)^A`.

This is strictly stronger than the `48 (sqrt(3)/2)^A` upper bound used in RL266's already-promoted LMN bracketing cutoff. The RL266 no-reentry argument therefore applies a fortiori and yields

`A <= 51389`.

No coprimality assumption is used in this LMN step; only the inherited two-logarithm inequality for positive integer coefficients `A,L` is reused.

## 5. Exact size scan

Every theorem candidate, bracketing or not, must satisfy both

`A <= 51389`

and

`0 < D <= 16*3^floor(A/2)`.

The verifier scans this condition using exact integers only. For fixed `A`, `2^A-3^L` decreases monotonically in `L`, so the scan descends from the largest positive-domain power of three and stops as soon as the bound fails.

For `A>=6` it finds exactly **90** size-compatible `(A,L)` pairs.

The largest possible `A` is only

`A=27`.

Thus all remaining structural work is rigorously finite before any word reconstruction begins.

## 6. Gap-free structural certificate through `A=27`

For every

- `6 <= A <= 27`;
- `4 <= u <= A-2`;
- `1 <= m < A`;

the verifier sets

`g=(1,2,1,0,...,0,-1,0,...,0)`

with the singleton at `u` and solves exactly

`x_i-x_(i+m)=g_i-g_(i-1)`.

On each addition-by-`m` cycle, all relative bit values are determined; the verifier enumerates every `0/1` offset compatible with that cycle. It does not filter by primitivity.

After retaining only `D>1`, the exact certificate contains **149** canonical positive-domain states:

- `A=6`: 1;
- `A=9`: 4;
- `A=12`: 6;
- `A=15`: 16;
- `A=18`: 10;
- `A=21`: 36;
- `A=24`: 28;
- `A=27`: 48.

Every state satisfies the determinant identity and the exact two-term numerator formula.

Finite-state diagnostics:
- `gcd(m,A)=3` for all 149 states;
- `gcd(A,L)=1` for 114 states;
- `gcd(A,L)=3` for 35 states;
- proper-factor-only numerator differences: 5;
- full-`D` numerator-difference hits: **0**.

The observed `gcd(m,A)=3` is a finite-certificate fact, not used as an infinite structural assumption.

Therefore the height-two mass-four-plus-one `|kappa|=3` leaf is closed.

## 7. Independent small-range red team

A separate implementation brute-forces every positive-domain binary word through `A<=15`, every nontrivial shift, and **every optimal median**, rather than using the canonical height-two parametrization.

It finds:
- 708 height-two `4+1`, `|kappa|=3` optimal-flow occurrences;
- 354 in the `+3` orientation;
- 354 in the `-3` orientation;
- 702 distinct word/shift instances, with six `A=6` instances carrying two relevant optimal medians;
- exact agreement of the positive-orientation orbit count with the canonical reconstruction;
- zero two-term formula mismatches after exact source/target reversal and cyclic normalization;
- 30 proper-factor-only numerator-difference cases;
- zero full-`D` numerator-difference hits;
- zero actual full-`D` source words in this replay.

The permanent negative-domain sentinel

`A=11, L=7, D=-139, Q=18904, n=-136`

is reproduced and remains outside the positive-domain theorem scope.

## 8. Promoted result

Promoted local leaf:

> In the inherited positive-domain primitive/full-`D` Radius-5 setting, no exact-distance-5 self-rotation with `|kappa|=3` and height-two mass-four-plus-one transport topology exists.

Together with RL271, **every** `|kappa|=3` Radius-5 topology is now closed.

Therefore the promoted classification is

**RADIUS5_KAPPA3_SECTOR_CLOSED**.

Radius 5 itself remains open because `|kappa|=5` is not yet closed.

Gate A, Gate B, the fifth selector, selector enumeration, the general Radius-n programme, and global non-trivial-cycle exclusion are not proved or advanced here.
