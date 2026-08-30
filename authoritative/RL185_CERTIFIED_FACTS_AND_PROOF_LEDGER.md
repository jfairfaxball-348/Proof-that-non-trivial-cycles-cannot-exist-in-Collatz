# RL185 certified facts and proof ledger

Date: 2026-08-30

Scope: all new facts below remain internal to the surviving high branch `(v,H,J,d)=(37,0,23,-1)`.

## Inherited frozen facts

- RL181 exact drift: `K_(i+1)-K_i=(1/3)q_i(2^G_i-1)`.
- RL181 residue envelope: `1/2<rho_i<=1`.
- RL181 K corridor: `128,081,997,553<K_i<146,795,909,391`.
- RL184 clean 40-edge corridor floor: `10,075,174,499`.
- RL184 distinct physical nonzero-defect floor: `251,879,363`.
- Ordinary defect flow: `f_i=q_i(2^G_i-1)=rho_i(2^-b-2^-a)` for endpoint heights `(a,b)`.
- Exact total flow: `sum_i f_i=F2=3(lambda-1)2^37`.

## RL185.1 — forced-defect height envelope

**Class:** proved analytic mathematics + exact finite integer certificate.

For a clean shallow-start corridor and offset `0<=j<=39`, both endpoint heights are at most

`1+ceil(j(A-L)/L)`.

At j=39 the right side is 24. Every selected RL184 forced defect therefore has endpoint maximum at most 24.

## RL185.2 — height-dependent coverage capacity

**Class:** proved analytic mathematics + exact finite integer certificate.

For endpoint maximum `H=1,...,24`, a fixed selected defect can serve at most

`40,39,38,36,34,33,31,29,28,26,24,22,21,19,17,16,14,12,10,9,7,5,4,2`

clean corridor starts respectively.

For every H,

`cap(H)<=2^(25-H)`.

## RL185.3 — ordinary absolute corrected-flow variation

**Class:** proved analytic mathematics + exact finite integer certificate.

With `f_i=q_i(2^G_i-1)`,

`sum_(ordinary i)|f_i| > 10,075,174,499/2^26 >150`.

Consequently

`sum_(ordinary i)|K_(i+1)-K_i| >50`.

This is total variation, not net excursion.

## RL185.4 — two-sided signed flow

**Class:** proved analytic mathematics + exact rational interval certificate.

The carry flow exceeds `1/2`. The bundled rational interval verifier certifies

`0<F2<1/2`.

Therefore, over the full period,

- total negative corrected-flow mass `N>75`;
- total positive corrected-flow mass `P>75`;
- total negative K-variation `>25`;
- total positive K-variation `>25`.

All negative flow is ordinary. The ordinary signed flow is strictly negative:
`sum_(i!=t)f_i=F2-f_t<0`.

## RL185.5 — signed phase counts

**Class:** proved analytic combinatorics + exact integer certificate.

There are at least

- `10,075,175` negative ordinary defect phases;
- `10,075,175` positive defect phases including the carry;
- `10,075,174` positive ordinary defect phases.

The proof uses the height-24 localization and exact balance of threshold crossings in the closed p-rank height cycle.

## Finite certificate status

`verification/verify_rl185_signed_phase_capacity.py` checks:

- the 39-step late-bit maximum 23;
- the full height-dependent multiplicity table;
- `cap(H)<=2^(25-H)`;
- `10,075,174,499>150*2^26`;
- the signed count arithmetic;
- a rational enclosure `0<F2<1/2`.

## Closure status

No branch or global gate is closed in RL185. The remaining quantitative gap is that `>25` directional K variation is far smaller than the inherited K-corridor width. The next target is to limit how much corridor mass can postpone its first defect into the high-height tail.
