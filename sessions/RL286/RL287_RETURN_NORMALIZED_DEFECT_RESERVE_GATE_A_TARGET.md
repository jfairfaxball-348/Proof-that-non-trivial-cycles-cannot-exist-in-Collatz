# RL287 — return-normalized defect reserve for Gate A

Date prepared: 2026-09-09
Status: PREPARED, NOT STARTED

## Incoming classification

RL286 closed as

`EXCURSION_CARRY_COUPON_DEFECT_BRIDGE_AND_STATE_RESERVE_BARRIER_PROVED`.

Gate A remains open with exact residual

`k>=25`, `k` odd, `H_can<k`.

## Frozen RL286 bridge

For every genuine positive first-return excursion `E`:

- `C_E=W_x-W_y`;
- `C_E=3^r D_E/Q_in`;
- `C_E/2^L=D_E/Q_out`;
- the component has exactly `h` carry/coupon cells;
- every cell exponent lies in `0,...,h-1`;
- the unique lowest exponent is `0`.

The one-zero family satisfies

`C_E=3^h-2^h`

so

`C_E/2^h=(3/2)^h-1`.

Therefore a state-free height-only component carry budget is impossible.

## Mission

Find the missing **state-dependent reserve** carried between positive first-return components.

Preferred target:

Construct a quantity `R` on positive boundary/checkpoint states such that

1. arbitrary zero-height positive boundary retention transports `R` exactly or monotonically;
2. a first-return excursion of height `h` can increase dangerous carry demand only by `h` plus a rigorously debited amount of `R`;
3. the reserve cannot be replenished for free by positive neutral boundary loops;
4. at terminal `J=2^k`, the resulting cumulative demand is at least `k`;
5. summing the component inequalities yields `k<=H_can`.

Equivalent acceptable outcomes:

- prove the checkpoint theorem `nu_2(J)<=H`;
- prove the global post-column inequality `nu_2(K-1)<=H+d-1`;
- prove the equivalent positive high-divisibility sign theorem;
- obtain a new exact structural invariant that materially contracts the residual.

## Required ingredients to test first

1. **One-zero reserve.**
   Use the exact inherited law
   `h=nu_2(J_in+4)`
   to identify what arithmetic reserve is consumed by the unbounded one-zero normalized defect.

2. **Multi-zero pricing.**
   Combine RL281's `F=Q(J+3)` checkpoint increment and full-mass pricing with
   `C_E/2^L=D_E/Q_out`.

3. **Boundary quotient.**
   Close the reserve under arbitrary zero-height positive boundary retention parametrically. Do not replace the boundary subsystem with a fixed finite shifted-valuation table.

4. **Falsification.**
   Test any proposed reserve on the known neutral positive boundary loop and on genuine low-height excursions before promoting it.

## Forbidden repeats

Do not:

- revive blockwise `nu_2(J)` monotonicity;
- assume one carry bit per height unit;
- treat coupon defect and Ferrers carry as independent constraints;
- replace the reserve by a fixed finite offset/valuation table;
- make a larger raw height-cap search the principal route;
- merge Gate B into Gate A;
- scan the fifth selector;
- start Radius 6+.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.
