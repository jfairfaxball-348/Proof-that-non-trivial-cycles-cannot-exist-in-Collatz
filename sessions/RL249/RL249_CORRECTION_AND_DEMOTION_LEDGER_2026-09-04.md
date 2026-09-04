# RL249 correction and demotion ledger

Date: 2026-09-04

This ledger is binding for the RL249 closeout candidate.

## Promoted

Only the following new RL249 results are promoted:

1. beta=6 Branch-C global profile: exactly six `-1` roots, positive mass 8, `P in {-1,0,1,2}`, `sum|P|=14`, nonzero support at most 14;
2. exact q-shift mismatch/variation bound `12<=M_q<=28`, with equal mismatch orientations;
3. `a>=123`, at least 109 `P=0` roots, and a disjoint length-7 `u` versus q-shift agreement corridor;
4. ordinary zero-run propagation `0^L -> q-shifted 0^(L-9)` for `L>=10`;
5. refined ratio `log_2(3)<a/ell<=65/41` on this survivor;
6. magnitude-only phase barrier: the current `>2/6561` selected gain cannot by magnitude alone close a total phase rise `>17`.

## Demoted / not promoted

- identification of the historical RL47 `q=z+t` parameter with the current determinant-2 q;
- every explicit placement or zero-budget lower bound using that identification;
- the proposed quadratic zero-desert induction and its `z,m,a,ell` numerical consequences;
- the exploratory q-ordered covering theorem claiming `B in {13,14}` / `B=14` and `P in {-1,0,1}`;
- any Radius-4 inference from local swap geometry or large beta(E);
- any RL64 synchronized-block inference from u/q-shift agreement alone;
- the already-demoted RL246 uniform single-packet absolute phase bound.

## Closeout red-team finding

During closeout, direct cyclic-cover recomputation showed that one scratch formula used for the coprime 12-block covering lower bound was not exact. The entire downstream q-block-cover conclusion was therefore demoted rather than repaired during `CLOSEOUT_LOCK`.

No promoted item above depends on that formula.
