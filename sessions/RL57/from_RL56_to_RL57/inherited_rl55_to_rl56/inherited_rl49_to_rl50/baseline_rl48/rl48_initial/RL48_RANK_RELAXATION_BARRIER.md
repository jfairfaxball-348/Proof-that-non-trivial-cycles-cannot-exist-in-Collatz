# RL48 — Barrier theorem for the RL47 separable rank relaxation

Date: 2026-08-22

## Status

**Analytic theorem.**  This is a limitation theorem for the existing RL47 relaxed rank-transport proof method, not a counterexample to the desired terminal inequality.

## 1. Setup

Retain RL47 notation

- `zeta=2^a/3^ell`, with `1<zeta` and `zeta^2<16/15`,
- `q=a-ell`,
- even `t>=2`,
- `k=t+3`,
- terminal zero count `z=q-t`,
- `r=ell-3`,
- `m=a-k-1`,
- weights `w_j=2^a_j/3^j`, `1<=j<=r`.

RL47's coordinate cap is

`2^(a_j+3) 3^(2ell) <= 3^(j+1) 2^(2a)`.

Put

`C=(3/8) zeta^2`.

Then the cap exponent is

`U_j=floor(log2(C 3^j))`.

The terminal-room exponent is

`R_j=m-r+j-1 = z+j-2`.

Because `U_{j+1}-U_j` is always at least one, the backward strict-order envelope used by the RL47 verifier is exactly

`A_j=min(U_j,R_j)`.

## 2. First 72 ranks are cap-limited when z>=42

Assume `z>=42`.

For `1<=j<=72`, using `C<2/5`, it is enough to show

`(2/5)3^j < 2^(z+j-1)`.

The worst endpoint is `(z,j)=(42,72)`, where this reduces to the exact integer inequality

`3^72 < 5*2^112`.

Hence `U_j<=R_j` for all first 72 ranks, so `A_j=U_j` there.

The near-resonance window also guarantees that there are at least 72 moved ranks whenever `z>=42`: since `q=z+t>=44` and

`q-(log2(3)-1)ell = log2(zeta) < (1/2)log2(16/15)`,

one gets `ell>=76`, hence `r=ell-3>=73`.

## 3. Baseline lower bound inside the enlarged relaxation

For a cap-limited rank,

`2^U_j > (C 3^j)/2`,

so

`w_j > C/2`.

The synchronized baseline in the RL47 relaxed maximization is

`2 sum_j w_j`.

The first 72 cap-limited ranks alone therefore contribute strictly more than

`72 C`.

Under a hypothetical strict violation the displacement budget is

`B=t+2>=4`.

The first displacement marginal on each cap-limited rank is `w_j/2>C/4`.  The exact greedy concave maximizer therefore gains more than `C` from four available budget units.

Thus the RL47 relaxed maximum is strictly larger than

`73 C = (219/8) zeta^2`.

## 4. This already exceeds the exact terminal target

The exact terminal target is

`Lambda = 14 + (27/2) zeta (1-2^-k)`.

Since `k>=5`,

`Lambda <= 14 + (837/64) zeta`.

For `zeta>=1`,

`(219/8)zeta^2 - 14 - (837/64)zeta`

is increasing, and at `zeta=1` equals

`19/64 > 0`.

Therefore

`relaxed_max > (219/8)zeta^2 > Lambda`.

## 5. Barrier theorem

> **RL48 barrier theorem.** Under the retained near-resonance hypotheses, the exact RL47 separable cap/room + total-displacement relaxation cannot certify a strict-violation exclusion whenever
>
> `z=q-t >= 42`.

Equivalently, this proof method can only possibly exclude the strip

`q-t <= 41`.

This is a theorem about the proof relaxation, not about the real automaton.

## 6. Strategic consequence

The requested "uniformization" of RL47's finite-pair rank envelope cannot close Gate A by algebraically polishing the same separable relaxation.  For large near-resonant pairs and small/moderate `t`, it is structurally guaranteed to lie above the terminal target.

A successful Gate-A proof needs at least one new coupling invariant linking the many synchronized height-one ranks.  The natural missing object is a quotient of the deterministic height-one `00/11` dynamics (or an exact telescoping identity for its synchronized rank mass), because low area alone permits arbitrarily many zero-area synchronized ranks.
