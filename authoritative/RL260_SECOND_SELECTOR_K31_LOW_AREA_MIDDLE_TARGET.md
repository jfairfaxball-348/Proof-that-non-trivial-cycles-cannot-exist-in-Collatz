# RL260 — second-selector k=31 exact low-area middle target

Date prepared: 2026-09-05
Status: **PREPARED, NOT STARTED**

## Incoming promoted state

RL259 identifies the unique next arithmetic selector beyond the eliminated
first frontier as

`(a,ell,z,q,r,H_sel,n)=(1119,706,413,802,506,14,10)`.

At this selector:

- exact terminal exponents reduce to `k in {31,33}`;
- `k=33 => H_can>=33`, so `k=33` is Gate-A safe;
- `k=31` contracts to exactly 8,976 flank x-pattern pairs after the exact
  area-budget and root-capacity tests;
- the middle length for every retained `k=31` pair is 1068.

Thus the only branch at this selector still simultaneously unresolved by Gate
A and Gate B is the finite `k=31` family.

## Unique target

Work only on the RL259-owned 8,976-pair `k=31` family.

1. Perform exact terminal inversion for the retained left flanks from the
   corrected internal endpoint `(d,J)=(1,2^31)` before the omitted terminal
   `10`.
2. Under Gate-A danger `H_can<=30`, combine exact right-prefix area,
   terminal-suffix area, and the unavoidable bridge lower bound to contract
   to the genuinely low-area prefix/suffix realizations.
3. For every surviving low-area realization, run the exact middle state-set
   automaton for the 1068-site middle, or use an exact repeat/empty certificate
   that excludes the required terminal predecessor for every future depth.
4. If every Gate-A-dangerous realization is excluded, promote the targeted
   certificate `k=31 => H_can>=31`, remove this second selector from the
   simultaneous unresolved branch, and identify the next arithmetic selector.
5. If any realization remains live, isolate the smallest exact live branch and
   hand over the cheapest audited Gate-B/Radius-4 route rather than weakening
   the model.

## Binding safeguards

- Do not identify `H_sel` with `H_can`.
- Use the corrected endpoint `J=2^31` before the omitted terminal `10`.
- Do not resurrect the demoted RL256 backward-tree or relaxed MILP routes.
- Do not apply Radius 4 without every audited primitive/full-D/exact-distance
  hypothesis.
- Radius 5 remains inactive unless a later authoritative session activates it.

Gate A remains open uniformly.
Gate B remains open.
RL259 does not invoke Radius 4.
