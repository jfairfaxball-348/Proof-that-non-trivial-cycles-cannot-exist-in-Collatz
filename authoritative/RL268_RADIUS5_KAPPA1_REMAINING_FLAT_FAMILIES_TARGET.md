# RL268 — Radius-5 remaining determinant-one flat families

Date prepared: 2026-09-06  
Status: **PREPARED, NOT STARTED**

Incoming classification: `RADIUS5_KAPPA1_311_221_CLOSED`.

## Frozen work

Do not resume:
- Gate A;
- the fifth retained arithmetic selector;
- selector-by-selector enumeration;
- the general Radius-n programme.

Do not begin `|kappa|=3` or `|kappa|=5` while determinant one remains open.

## Inherited determinant-one state

For an exact positive-domain Radius-5 self-rotation in `|kappa|=1`:
- the flow is flat;
- after orienting to `kappa=+1`, `qA-mL=1`;
- `gcd(A,L)=gcd(m,A)=1`;
- there are three positive unit edges and two negative unit edges;
- the exact zero-flow-cut edge identity and full-`D` divisibility are inherited;
- the exact determinant window identity `W_i(m)=q-g_{i-1}` is now promoted;
- the audited RL238 LMN dependency may be reused only after exact hypothesis matching.

Closed determinant-one topologies:
- `[3,2]` (RL266);
- `[3,1,1]` (RL267);
- `[2,2,1]` (RL267).

Remaining:
- `[2,1,1,1]`;
- `[1,1,1,1,1]`.

Radius 5 is not proved.

## Primary RL268 target

Attack only `[2,1,1,1]` first.

Required work:
1. derive every cyclic component-order/sign case without omission;
2. derive the exact component/edge formula from the promoted edge identity;
3. retain full `D`, not a proper factor;
4. exploit `qA-mL=1` and the exact window identity before computation;
5. prove a new infinite reduction appropriate to four components — do **not** assume the RL267 three-component support bound unchanged;
6. reuse RL238 LMN only after exact hypothesis matching and preserve the reduced-denominator/multiple correction;
7. preserve negative-D, nonprimitive, cyclic-wrap, component-order, proper-factor and numerator-index red teams;
8. use finite computation only after an explicit infinite reduction.

Preferred outcomes:
- `RADIUS5_KAPPA1_2111_CLOSED`;
- `RADIUS5_KAPPA1_2111_REDUCED_TO_FINITE_CERTIFICATE`;
- `RADIUS5_KAPPA1_2111_EXACT_BARRIER`.

Only after `[2,1,1,1]` reaches one of those states should the same session consider `[1,1,1,1,1]`.

Radius 4 remains promoted locally. Gate B remains open. No global exclusion theorem is assumed.
