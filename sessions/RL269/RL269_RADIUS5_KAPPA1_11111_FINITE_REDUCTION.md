# RL269 — Radius-5 determinant-one `[1,1,1,1,1]` finite reduction

Date: 2026-09-06  
Classification: **RADIUS5_KAPPA1_11111_REDUCED_TO_FINITE_CERTIFICATE**

## 1. Scope

RL269 works only the inherited positive-domain Radius-5 determinant-one sector `|kappa|=1`, and only the final flat topology `[1,1,1,1,1]`.

Inherited unchanged:
- `D = 2^A - 3^L > 1`;
- the parity-word numerator `Q`;
- the exact zero-flow-cut five-edge identity;
- full-`D` divisibility under the cycle hypothesis;
- after orienting to `kappa=+1`, `qA-mL=1`;
- `gcd(A,L)=gcd(m,A)=1`;
- the determinant-window identity `W_i(m)=q-g_{i-1}`;
- the audited RL238 Laurent-Mignotte-Nesterenko two-logarithm dependency and its large-`A` no-reentry argument.

Already closed determinant-one leaves:
- `[3,2]` (RL266);
- `[3,1,1]` and `[2,2,1]` (RL267);
- `[2,1,1,1]` (RL268).

Frozen and untouched:
- `|kappa|=3`;
- `|kappa|=5`;
- Gate A;
- the fifth retained selector;
- selector enumeration;
- the general Radius-n programme.

## 2. Exact cyclic sign/order classification

Orient to `kappa=+1`. Flat distance five has three positive unit-flow components and two negative unit-flow components.

For `[1,1,1,1,1]`, all five components are singleton nonzero edges separated by positive zero-flow gaps. Up to cyclic rotation, and without using a reflection quotient, there are exactly two cyclic sign necklaces:

1. the two negative singleton components are adjacent in component order, represented by `+,+,+,-,-`;
2. the two negative singleton components are separated, represented by `+,+,-,+,-`.

The `kappa=-1` orientation is obtained by interchanging source and target.

## 3. Five-component support cut

The five positive zero gaps have total length `A-5`. Hence one gap has length at least

`ceil((A-5)/5)`.

Cut at a longest zero gap. The physical span between the extreme nonzero-edge anchors is at most

`U5 = A - ceil((A-5)/5) - 1 = floor(4A/5)`.

This is a new five-component support statement; no lower-component support constant is reused.

## 4. Determinant-window mixed bound

Let

`h = min(m,A-m)`

and choose the corresponding shorter determinant-window count

`r = q` if `m <= A-m`,
`r = L-q` otherwise.

From `qA-mL=1`:
- if `h=m`, then `r = hL/A + 1/A`;
- if `h=A-m`, then `r = hL/A - 1/A`.

Combining the exact five-edge identity, the five-component support cut, and the determinant-window count gives the nonzero full-`D` edge-difference bound

`0 < |E| <= 5 * 3^(7+r) * 2^(U5-r)`.

The divisor is always the complete positive integer `D=2^A-3^L`; no proper factor is substituted.

## 5. Explicit infinite reduction

Put

`beta = log(2)/log(3)`

and

`delta = log(2)/5 - (beta/2)*log(3/2) > 0`.

Positive domain gives `L/A < beta`, while `h<=A/2`. Therefore `r < beta*A/2 + 1/2`. Since `U5<=4A/5`, the exact mixed bound implies the deliberately enlarged normalized estimate

`|E|/2^A < C0 * exp(-delta*A)`

with

`C0 = 5 * 3^(15/2)`.

The favorable factor `2^(-1/2)` available from the sharper constant is discarded; this makes the promoted cutoff conservative.

### Non-bracketing branch

If `m/q > alpha=log(3)/log(2)`, the inherited determinant-one argument gives

`D > (log(2)/(2A))*2^A`.

The lower bound for `D` and the normalized upper bound for `|E|` are incompatible for every integer `A>=1713`.

Hence every non-bracketing survivor has

`A <= 1712`.

### Bracketing branch

If

`m/q < alpha < A/L`,

then from `A>=984` onward the normalized upper bound is below `1/2`. With

`Lambda = A log(2)-L log(3)`,

full-`D` divisibility and `0<|E|` give the necessary estimate

`Lambda <= 2*C0*exp(-delta*A)`.

The audited RL238 LMN specialization gives

`log Lambda >= -22 M^2 log(2)log(3)`.

In the `M=21` regime the resulting necessary inequality has root

`690205 < A_root < 690206`.

The same safe logarithmic upper bound for `M` and negative-derivative argument already audited in RL266/RL268 is negative at the large-`A` transition and remains decreasing, so there is no large-`A` re-entry.

Therefore every bracketing survivor has

`A <= 690205`.

## 6. Exact determinant-pair cover

An exact Stern-Brocot traversal around `alpha`, using integer comparisons of `2^n` and `3^d`, has 36 upper-neighbour rows through the bracketing cutoff.

Applying the exact five-component mixed size test leaves only seven coarse bracketing rows:

`(A,L;m,q) =`
- `(5,3;3,2)`;
- `(8,5;3,2)`;
- `(27,17;19,12)`;
- `(46,29;19,12)`;
- `(65,41;19,12)`;
- `(149,94;84,53)`;
- `(233,147;84,53)`.

Combining:
- every positive-domain determinant-one pair with `A<=1712`; and
- the exact Stern-Brocot bracketing rows through `A<=690205`;

then applying the exact mixed bound gives precisely

**2,234 determinant pairs**, with maximum **`A=690`**.

This is an explicit infinite-to-finite reduction.

## 7. Why RL269 stops at finite reduction

For a fixed surviving `A`, each cyclic sign order has five positive zero gaps summing to `A-5`, hence

`binom(A-6,4)`

raw positive-gap configurations. There are two cyclic sign orders. Across the exact 2,234-pair cover this gives

**618,391,058,390**

naive two-order gap configurations.

Blindly extending RL268's raw gap loop is therefore not a sensible certificate strategy. RL269 does not claim that this finite set has been exhausted.

The next generation should compress the finite certificate algebraically before enumeration. A promising exact relation to exploit is

`x_i - x_(i+m) = g_i - g_(i-1)`

around the single `m`-cycle together with `qA-mL=1`; any stronger alternation/interlacing consequence must be proved before it is used as a filter.

## 8. Independent small-range red team

A direct word-level replay through `A<=18` gives:
- **8,996** positive-domain `[1,1,1,1,1]`, `|kappa|=1` instances;
- exact orientation split **4,498 / 4,498**;
- **0** full-`D` numerator-difference hits;
- **714** proper-factor-only instances;
- **0** determinant mismatches;
- **0** zero-cut five-edge-identity mismatches on all `kappa=+1` instances.

The permanent inherited negative-domain sentinel `A=11,L=7,D=-139,Q=18904` remains outside the promoted `D>1` scope.

## 9. Promoted result

> The inherited positive-domain Radius-5 determinant-one `[1,1,1,1,1]` leaf is rigorously reduced to an explicit finite certificate consisting of 2,234 determinant pairs with maximum `A=690`.

Classification: **RADIUS5_KAPPA1_11111_REDUCED_TO_FINITE_CERTIFICATE**.

This leaf is **not closed**. Consequently the determinant-one sector is still open, and `|kappa|=3` and `|kappa|=5` remain frozen. Radius 5, Gate B and global non-trivial-cycle exclusion remain open.
