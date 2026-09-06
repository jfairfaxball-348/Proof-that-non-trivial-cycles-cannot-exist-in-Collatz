# RL267 — Radius-5 remaining determinant-one flat families

Date prepared: 2026-09-06  
Status: **PREPARED, NOT STARTED**

Incoming classification: `RADIUS5_KAPPA1_32_CLOSED`.

## Frozen work

Do not resume:
- Gate A;
- the fifth retained arithmetic selector;
- selector-by-selector enumeration;
- the general Radius-n programme.

Do not begin `|kappa|=3` or `|kappa|=5` while determinant one remains open.

## Inherited determinant-one state

For an exact Radius-5 self-rotation in the `|kappa|=1` sector:
- the flow is flat;
- `qA-mL=+/-1`;
- `gcd(A,L)=1`;
- after orienting to `kappa=+1`, there are exactly three positive unit edges and two negative unit edges;
- a zero-flow cut gives the exact edge-monomial identity for `Q(tau^m d)-Q(d)`;
- full-`D` rotation covariance gives full `D | (Q(tau^m d)-Q(d))`;
- the RL238 LMN / continued-fraction dependency and RL238/RL239 reduced-denominator correction are available only after exact hypothesis matching.

RL266 has completely closed topology `[3,2]`.

Remaining determinant-one topologies:
- `[3,1,1]`;
- `[2,2,1]`;
- `[2,1,1,1]`;
- `[1,1,1,1,1]`.

Radius 5 is not proved.

## Primary RL267 target

Attack only `[3,1,1]` first.

The compressed form is one length-three component plus two unit components, hence a three-term coefficient-weighted `2,3` S-unit relation.

Required work:
1. derive the exact cyclically invariant `[3,1,1]` component formula from the promoted edge identity;
2. retain full `D`, not a proper factor;
3. exploit `qA-mL=+/-1` before introducing any computation;
4. seek an analytic / continued-fraction / quotient reduction giving an explicit finite cutoff;
5. reuse the RL238 LMN dependency only after exact hypothesis matching;
6. preserve negative-D, nonprimitive, cyclic-wrap and numerator-index red teams;
7. use finite computation only after an explicit infinite reduction.

Do not assume the `[3,2]` binomial argument extends unchanged: `[3,1,1]` is genuinely a three-term leaf.

## Success criteria

Preferred RL267 outcomes:
- `RADIUS5_KAPPA1_311_CLOSED`;
- `RADIUS5_KAPPA1_311_REDUCED_TO_FINITE_CERTIFICATE`;
- `RADIUS5_KAPPA1_311_EXACT_BARRIER`.

Only after `[3,1,1]` reaches one of those states should the same session consider whether to continue to `[2,2,1]`.

Radius 4 remains promoted locally.
Gate B remains open.
No global exclusion theorem is assumed.
