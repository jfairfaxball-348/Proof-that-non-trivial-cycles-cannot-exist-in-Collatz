# RL268 — Radius-5 determinant-one `[2,1,1,1]` closure

Date: 2026-09-06  
Classification: **RADIUS5_KAPPA1_2111_CLOSED**

## 1. Scope

RL268 works only the inherited positive-domain Radius-5 determinant-one sector `|kappa|=1`, and only the remaining flat topology `[2,1,1,1]`.

Inherited and left unchanged:
- `D = 2^A - 3^L`;
- the parity-word numerator `Q`;
- the exact zero-flow-cut five-edge identity;
- full-`D` divisibility under the cycle hypothesis;
- `qA - mL = 1`, hence `gcd(A,L)=gcd(m,A)=1`;
- the determinant-window identity `W_i(m)=q-g_{i-1}`;
- the audited RL238 Laurent-Mignotte-Nesterenko two-logarithm dependency.

Already closed determinant-one leaves:
- `[3,2]` (RL266);
- `[3,1,1]` (RL267);
- `[2,2,1]` (RL267).

Frozen and untouched:
- `|kappa|=3`;
- `|kappa|=5`;
- Gate A;
- the fifth retained selector;
- selector enumeration;
- the general Radius-n programme.

## 2. Exact cyclic sign/order classification

Orient to `kappa=+1`. There are three positive unit edges and two negative unit edges.

For topology `[2,1,1,1]` there are exactly four anchored cyclic sign/order cases after anchoring the unique length-two component:

1. the length-two component is positive and the singleton order is `+,-,-`;
2. the length-two component is positive and the singleton order is `-,+,-`;
3. the length-two component is positive and the singleton order is `-,-,+`;
4. the length-two component is negative and all three singleton components are positive.

All four components are separated by positive zero-flow gaps. No reflection identification is used in the certificate.

## 3. Four-component support cut

Let the four positive zero gaps have total length `A-5`. One gap has length at least

`ceil((A-5)/4)`.

Cut at a longest zero gap. The physical span between the extreme nonzero-edge anchors is therefore at most

`U4 = A - ceil((A-5)/4) - 1 = floor((3A+1)/4)`.

This is a new four-component support statement. RL267's three-component support bound is not reused.

## 4. Determinant-window mixed bound

Let

`h = min(m,A-m)`,

and choose the corresponding shorter determinant window count

`r = q` if `m <= A-m`,
`r = L-q` otherwise.

The exact determinant relation gives

- if `h=m`, then `r = hL/A + 1/A`;
- if `h=A-m`, then `r = hL/A - 1/A`.

Combining the zero-flow-cut edge identity, the four-component support cut, and the exact determinant-window count gives the nonzero full-`D` edge-difference bound

`0 < |E| <= 5 * 3^(7+r) * 2^(U4-r)`.

The divisor retained throughout is the entire positive integer `D=2^A-3^L`.

## 5. Explicit infinite reduction

Put

`beta = log(2)/log(3)`.

Positive domain gives `L/A < beta`; also `h<=A/2`. Therefore

`r < beta*A/2 + 1/2`.

Using `U4 <= (3A+1)/4`, a deliberately conservative normalized bound is

`|E|/2^A < C0 * exp(-delta*A)`

where

`C0 = 5 * 3^(15/2) * 2^(1/4)`

and

`delta = log(2)/4 - (beta/2) * log(3/2) > 0`.

### Non-bracketing case

If `m/q > alpha=log(3)/log(2)`, the determinant-one argument inherited from RL266 gives

`D > (log(2)/(2A))*2^A`.

The two bounds are incompatible for every integer `A>=375`.

Hence every non-bracketing survivor has `A<=374`.

### Bracketing case

If

`m/q < alpha < A/L`,

then for `A>=237` the normalized upper bound is below `1/2`, so with

`Lambda=A log(2)-L log(3)`

we obtain

`Lambda <= 2*C0*exp(-delta*A)`.

The RL238 audited LMN specialization gives

`log Lambda >= -22 M^2 log(2)log(3)`,

with the same exact hypotheses as in RL266/RL267. In the `M=21` regime the necessary inequality forces

`A < 163052.252`.

For larger `A`, the same safe logarithmic upper bound for `M` used in RL266 is already negative at the transition and has negative derivative thereafter, so there is no large-`A` re-entry.

Thus every bracketing survivor has

`A <= 163052`.

Exact Stern-Brocot traversal around `alpha`, using only the integer comparisons `2^n ? 3^d`, gives 35 admissible upper-neighbour rows through this cutoff. The mixed size test leaves only

`(A,L;m,q) =`
`(5,3;3,2),`
`(8,5;3,2),`
`(27,17;19,12),`
`(46,29;19,12),`
`(65,41;19,12),`
`(149,94;84,53)`.

All are already inside the small-`A` exact determinant enumeration.

Combining:
- every determinant-one pair with `A<=374`; and
- the exact Stern-Brocot bracketing rows through `A<=163052`;

then applying the exact mixed size test gives precisely

**967 determinant pairs**, with maximum `A=174`.

The complete list is committed as `verification/rl268_pairs.csv`.

## 6. Complete structural finite certificate

For every one of the 967 determinant pairs, the certificate enumerates all four anchored cyclic sign/order cases and every positive four-gap composition.

For a fixed `A`, the raw gap count is

`4 * binom(A-6,3)`

when `A>=9`.

Across the exact pair list:

- gap configurations: **179,403,060**;
- structurally valid binary candidates: **9,510,691**;
- maximum structural `A`: **174**.

Counts by anchored sign/order case are:

1. `+2 ; +,-,-`: **2,405,606**;
2. `+2 ; -,+,-`: **2,410,327**;
3. `+2 ; -,-,+`: **2,405,606**;
4. `-2 ; +,+,+`: **2,289,152**.

For every structural candidate the relation

`x_i - x_(i+m) = g_i - g_(i-1)`

is solved around the single `m`-cycle, the exact five-edge numerator difference is reconstructed, and divisibility is tested against the entire positive `D`.

Result:

**full-`D` hits = 0**.

Primitivity is not used as a certificate filter, so the finite certificate is stronger than the written primitive theorem scope.

## 7. Independent red team

An independent direct earth-mover replay through `A<=18` gives:

- **21,596** raw positive-domain `[2,1,1,1]`, `|kappa|=1` instances;
- **10,798** with `kappa=+1`;
- **10,798** with `kappa=-1`;
- **0** full-`D` numerator-difference hits;
- **0** determinant-identity mismatches;
- **0** five-edge-identity mismatches after the required zero-flow cut.

The permanent negative-domain regression

`A=11, L=7, D=-139, Q=18904`

remains outside the promoted positive-domain scope.

No proper divisor of `D` is ever substituted for full `D`.

## 8. Promoted result

> In the inherited positive-domain, primitive/full-`D` Radius-5 setting, no exact-distance-5 self-rotation with `|kappa|=1` and transport topology `[2,1,1,1]` exists.

Classification: **RADIUS5_KAPPA1_2111_CLOSED**.

The only determinant-one flat topology still open is `[1,1,1,1,1]`.

Radius 5 itself is **not** yet proved: after determinant one is completed, the `|kappa|=3` and `|kappa|=5` sectors still remain unless a subsequent theorem eliminates them uniformly.
