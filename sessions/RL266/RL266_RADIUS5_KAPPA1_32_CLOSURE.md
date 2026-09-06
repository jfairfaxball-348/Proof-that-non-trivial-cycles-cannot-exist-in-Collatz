# RL266 — Radius-5 determinant-one `[3,2]` closure

Date: 2026-09-06  
Classification: **RADIUS5_KAPPA1_32_CLOSED**

## 1. Scope

RL266 worked only the inherited Radius-5 determinant-one sector `|kappa|=1`.

Frozen and untouched:
- Gate A;
- the fifth retained arithmetic selector;
- selector-by-selector enumeration;
- the general Radius-n programme.

Inherited from RL265:
- `D=2^A-3^L`;
- the parity-word numerator
  `Q(d)=sum_{i:d_i=1} 2^i 3^(L-r_i)`;
- exact cyclic earth-mover flow `g`;
- exact Radius-5 determinant relation
  `qA-mL=kappa`;
- in the determinant-one sector, `gcd(A,L)=1`;
- the only possible `|kappa|=1` topologies are
  `[3,2]`, `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, `[1,1,1,1,1]`;
- under full `D`, every rotation has numerator divisible by full `D`.

This session proves only the `[3,2]` leaf. Radius 5 remains open.

## 2. Zero-flow cut and exact edge identity

Every flat `|kappa|=1` flow has at least one zero-flow edge. Cut immediately after such an edge and rotate source and target together. Rotation preserves full-`D` divisibility by the inherited root-crossing identity.

With cut words `x,y=tau^m x`, let

`R_i=sum_{j=0}^i x_j`.

The cut makes the optimal flow equal to the ordinary prefix discrepancy. Since a flat determinant-one flow has `g_i in {-1,0,1}`, resolving it into adjacent swaps gives the exact integer identity

`Q(y)-Q(x)
 = sum_{g_i=+1} 2^i 3^(L-R_i)
 - sum_{g_i=-1} 2^i 3^(L-R_i-1)`.

This is not merely a congruence.

Because `sum |g_i|=5` and `sum g_i=+1`, there are exactly three positive edges and two negative edges. The `kappa=-1` orientation is obtained by interchanging source and target.

## 3. `[3,2]` component compression

For `kappa=+1`, a `[3,2]` flow has a positive component of length three and a negative component of length two.

Summing the edge monomials inside a component and factoring the minimum geometric powers gives

`P = C3 * 2^a * 3^b`,
`N = C2 * 2^c * 3^d`,

with

`C3 in {7,9,13,19}`,
`C2 in {3,5}`.

After choosing the zero-flow cut so the positive component precedes the negative component, `a<c` and `b>=d`. Since `gcd(D,6)=1`, full-D divisibility is equivalent after removing common powers to

`D | (C3*3^v - C2*2^u)`

where

`u=c-a`,
`v=b-d`.

Here `u` is the physical arc length between the component anchors and `v` is the number of ones on that arc, so

`0 <= v <= u`.

Using `2^A == 3^L (mod D)`, the complementary representative is

`D | (C3*2^(A-u) - C2*3^(L-v))`.

The complementary arc obeys

`0 <= L-v <= A-u`.

Choose the shorter physical arc. Then its exponents `u_* , v_*` obey

`0 <= v_* <= u_* <= floor(A/2)`.

Therefore every nonzero full-D `[3,2]` difference satisfies the safe universal bound

`D <= |E| <= 24 * 3^floor(A/2)`.

No high-density coefficient refinement is needed for this bound.

## 4. Determinant-one rational split

Orient to `kappa=+1`:

`qA-mL=1`.

Hence

`gcd(A,L)=gcd(m,q)=1`

and

`A/L - m/q = 1/(qL)`.

Let

`alpha=log(3)/log(2)`,
`Lambda=A log(2)-L log(3)`.

Positive domain means `D>1`, hence `Lambda>0` and `A/L>alpha`.

There are exactly two cases.

### 4.1 Non-bracketing

If `m/q>alpha`, then

`A/L-alpha > A/L-m/q = 1/(qL)`,

so

`Lambda > log(2)/q > log(2)/A`.

For `0<Lambda<=1`, `1-exp(-Lambda)>Lambda/2`; for `Lambda>=1`, the same final lower bound below is weaker than `1-exp(-1)`. Thus

`D = 2^A(1-exp(-Lambda))
   > (log(2)/(2A)) 2^A`.

For every integer `A>=57`,

`(log(2)/(2A)) 2^A > 24 * 3^floor(A/2)`.

The verifier checks the two parity bases and the monotone two-step ratio. Therefore no non-bracketing `[3,2]` candidate exists for `A>=57`.

### 4.2 Bracketing

The only remaining infinite case is

`m/q < alpha < A/L`,
`qA-mL=1`.

From the safe numerator bound,

`1-exp(-Lambda) <= 24 (sqrt(3)/2)^A`.

For `A>=27` the right side is `<1/2`, hence

`Lambda <= 48 (sqrt(3)/2)^A`.

## 5. Audited LMN dependency and cutoff

RL238 already audited the Laurent-Mignotte-Nesterenko two-logarithm specialization used here. RL266 introduces no new external transcendence theorem.

For

`Lambda=A log(2)-L log(3) != 0`,

the inherited audited bound is

`log Lambda >= -22 M^2 log(2) log(3)`

with

`M=max(log(A/log(3)+L/log(2))+0.06, 21)`.

The hypotheses match exactly:
- bases are the multiplicatively independent rationals `2` and `3`;
- coefficients are positive integers `A,L`;
- `Lambda>0`;
- determinant one already gives reduced `L/A`.

Thus the RL238/RL239 reduced-denominator/multiple correction causes no multiplicity in this leaf: `gcd(A,L)=1` already.

Combining the LMN lower bound with the exponential upper bound gives the necessary inequality

`log(48)+A log(sqrt(3)/2)
 +22 M^2 log(2)log(3) >= 0`.

Using only `L<A`, the `M=21` regime extends to more than `5.27e8`. In that regime the necessary inequality gives

`A < 51389.677`.

For larger `A`, replacing `M` by the safe upper bound

`log(A(1/log(3)+1/log(2)))+0.06`

already makes the necessary expression negative at the transition, and its derivative remains negative thereafter. Hence there is no large-`A` re-entry.

Every bracketing survivor therefore satisfies

`A <= 51389`.

## 6. Exact Stern-Brocot finite certificate

The remaining bracket is a determinant-one Farey/Stern-Brocot bracket around `alpha`.

The portable verifier traverses the Stern-Brocot path using exact integer comparisons

`2^n ? 3^d`

and never floating-point decisions. Restricting the upper endpoint to `A<=51389` gives exactly 33 admissible upper-neighbour rows satisfying

`0<m<A`, `0<q<L`, `qA-mL=1`.

The first five are

`(A,L;m,q) =
 (5,3;3,2),
 (8,5;3,2),
 (27,17;19,12),
 (46,29;19,12),
 (65,41;19,12)`,

and the last is

`(24727,15601;1054,665)`.

The exact integer size test

`D <= 24*3^floor(A/2)`

leaves only four rows:

`(5,3;3,2)`,
`(8,5;3,2)`,
`(27,17;19,12)`,
`(46,29;19,12)`.

All lie below the independent structural cutoff `A<=56`.

## 7. Gap-free structural finite certificate for `A<=56`

Every `kappa=+1`, `[3,2]` flow can be cyclically normalized to

`+++ 0^r -- 0^s`

with `r,s>=1`.

Determinant one implies `gcd(m,A)=1`. For each `A,m,r`, the relation

`x_i-x_(i+m)=g_i-g_(i-1)`

runs around a single `m`-cycle and determines all possible binary words. The verifier enumerates:
- every `7<=A<=56`;
- every `1<=m<A` with `gcd(m,A)=1`;
- every `r,s>=1` with `r+s=A-5`;
- every binary solution;
- only then the inherited positive-domain condition `D>1`.

This gives exactly 7,040 canonical positive-domain structural candidates.

For every candidate:
- the direct integer `Q(tau^m x)-Q(x)` equals the independent five-edge formula;
- the component coefficients lie in the exact sets above;
- the complementary shorter-arc bound holds;
- full `D` is tested directly.

Result:

`full-D hits = 0`.

Primitivity is not used as a filter. All 7,040 candidates happen to be primitive. There are 434 proper-factor-only candidates with `gcd(Q(tau^m x)-Q(x),D)>1` but not full `D`; none is counted as a theorem hit.

The four LMN/Stern-Brocot coarse survivors contribute 0, 2, 14 and 26 canonical candidates respectively, total 42, and all are already included in the 7,040-candidate certificate.

## 8. Independent red team

A second implementation brute-forces all positive-domain words through `A<=18` using the inherited earth-mover definition, without the canonical `[3,2]` parametrization.

It reproduces:
- 10,382 raw `[3,2]` distance-5 instances;
- 4,774 with `|kappa|=1`;
- 2,387 with `kappa=+1`;
- 2,387 with `kappa=-1`;
- zero full-D hits in the `|kappa|=1` `[3,2]` sector.

The weighted canonical orbit count through `A<=18` agrees with the 2,387 positive-orientation raw instances.

The negative-D sentinel `A=11,L=7,D=-139` is retained only as a scope check and is outside this positive-domain theorem.

## 9. Promoted result and remaining work

Promoted local leaf:

> In the inherited positive-domain, primitive/full-`D` Radius-5 setting, no exact-distance-5 self-rotation with `|kappa|=1` and transport topology `[3,2]` exists.

The finite certificate is stronger than the written primitive scope because it does not filter nonprimitive candidates.

Not proved:
- the remaining determinant-one topologies `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, `[1,1,1,1,1]`;
- the `|kappa|=3` or `|kappa|=5` sectors;
- the full Radius-5 local theorem;
- Gate A or Gate B;
- any global non-trivial-cycle exclusion;
- any general Radius-n theorem.

RL267 should remain in `|kappa|=1` and attack `[3,1,1]` next.
