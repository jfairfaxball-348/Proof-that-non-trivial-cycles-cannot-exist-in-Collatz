# RL48 — Canonical same-root selector and phase collapse

Date: 2026-08-22

## Status

**Analytic theorem + exact regression on the audited (65,41) proper-factor countermodel.**

This note does not claim RL closure and does not invoke the inherited radius-3 theorem.  It removes the "different-root contamination" ambiguity at the `f,L` stage and replaces the three-polynomial same-root condition by one explicit scalar congruence.

## 1. Setup

Let

- `a = ell + q`,
- `X=2^a`, `Y=3^ell`, `M=X-Y`,
- `f(T)=3T^q-2`,
- `L(T)=2T^ell-1`,
- `gcd(q,ell)=1`.

In the retained branch `M>0`.  Also `gcd(M,6)=1`, because `M` is odd and is nonzero modulo 3.

Work in the unit ring

`R = Z/MZ`.

Put

`A0 = 2/3`, `B0 = 1/2` in `R`.

The relation `2^a = 3^ell (mod M)` gives

`A0^ell = B0^q`.

Choose Bezout integers `u,v` with

`u q + v ell = 1`,

and define

`rho = A0^u B0^v` in `R`.

Negative exponents are legitimate because `2` and `3` are units modulo `M`.

## 2. Canonical common-root theorem

The element `rho` satisfies

`rho^q = A0 = 2/3`,

`rho^ell = B0 = 1/2`.

Hence

`f(rho)=0`, `L(rho)=0` in `R`.

Proof: using `A0^ell=B0^q`,

`rho^q = A0^(u q) B0^(v q)`

`= A0^(1-v ell) B0^(v q)`

`= A0 (B0^q/A0^ell)^v = A0`,

and similarly

`rho^ell = B0 (A0^ell/B0^q)^u = B0`.

The common root is unique in `R`: if `r,s` both satisfy the two equations, then `h=r s^-1` satisfies `h^q=h^ell=1`; Bezout gives `h=1`.

Thus the `f,L` common root is not merely existential and not merely prime-by-prime: it is a canonical element of `Z/MZ`.

## 3. Phase polynomial evaluated at the selected root

Use the audited one-excursion phase polynomial form

`P(T)=4+3 sum_R (T^b - T^c)`,

where a one-run `R` has

- zero-based start position `t`,
- one-based start rank `m`,
- length `k`,
- `Z=t-(m-1)` zeros before the run,
- `b=q m + ell(1-Z)`,
- `c=b+kq`.

At the canonical root,

`rho^b = (rho^q)^m (rho^ell)^(1-Z)`

`= (2/3)^m (1/2)^(1-Z)`

`= 2^t / 3^m`,

because `m+Z-1=t`.

Therefore the contribution of one run is

`3(rho^b-rho^(b+kq))`

`= 2^t (3^k-2^k) / 3^(m+k-1)`.

So

`P(rho) = 4 + sum_R 2^t (3^k-2^k)/3^(m+k-1)  (mod M)`.

## 4. Collapse to the standard word polynomial Q(v)

For a binary word `v` of weight `ell`, define

`Q(v)=sum_{i:v_i=1} 2^i 3^(ell-rank(i))`,

where `rank(i)` is the one-based rank of that `1`.

Dividing by `3^ell`, the contribution of a run `(t,m,k)` is

`sum_{s=0}^{k-1} 2^(t+s)/3^(m+s)`

`= 2^t (3^k-2^k)/3^(m+k-1)`.

Hence the entire same-root phase value collapses exactly to

`boxed:  P(rho) = 4 + Q(v)/3^ell  (mod M)`.

Equivalently, since `3^ell` is a unit modulo `M`,

`boxed:  P(rho)=0  <=>  M | (Q(v)+4*3^ell)`.

Using `3^ell = 2^a (mod M)`, this is also

`Q(v) + 4*2^a = 0 (mod M)`.

This is the exact same-root scalar obstruction.  No global resultant and no gcd of separate resultants is required to identify the relevant root.

## 5. Relation to the RL45 obstruction

RL45 showed that the naive absolute resultant size bound is false on the audited `(65,41)` proper-factor countermodel.  The new selector gives a sharper diagnostic.

For `(a,ell,q)=(65,41,24)`, one Bezout choice is

`12*24 - 7*41 = 1`,

so

`rho = 2^19 / 3^12 (mod M)`.

The companion verifier checks exactly that

- `f(rho)=0 mod M`,
- `L(rho)=0 mod M`,
- direct evaluation of `P(rho)` agrees with the run formula,
- the run formula agrees with `4+Q(v)/3^ell`,
- `P(rho)` is nonzero modulo `M`, and in fact `gcd(P(rho),M)=1`.

Thus the known proper-factor countermodel is rejected by the selected-root phase scalar exactly as it should be.

## 6. Consequence for the radius-3 bridge program

The old Gate-B formulation asked for a three-polynomial same-root subresultant/Bezout object.  The root-selection part can now be made explicit:

> Any genuine full-denominator phase solution must satisfy the single congruence
>
> `M | Q(v)+4*3^ell`
>
> at the canonical root forced by `f` and `L`.

What is still missing is the **quantitative radius-3 implication**: prove that, under the retained one-excursion/proper-factor/rank-displacement hypotheses, this scalar divisibility forces the already-forbidden radius-3 configuration (or yields an equivalent contradiction).

The exact inherited radius-3 theorem is not present in the RL47->RL48 bundle, so no claim is made here that its hypotheses have yet been matched line-by-line.
