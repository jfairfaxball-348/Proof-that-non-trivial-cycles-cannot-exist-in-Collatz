# RL31 research kickoff

Continue from the attached RL30 audit handover as a skeptical research mathematician.

## Mandatory first actions

1. Read `RL30_AUDIT_REPORT.md` and `START_HERE.md`.
2. Run the 22 inherited/RL29 verifiers in `inherited_rl29/VERIFIER_LEDGER.txt` plus `verify_rl30_audit_quantitative_targets.py`.
3. Treat any failure as stop-and-repair.
4. Keep `R>=2^71` explicitly external and keep older LMN-dependent radius-3 leaves explicitly dependent on the published LMN theorem.
5. Do not assume `(G,H)=(12,4)` is the unique global RL branch. It is a conditional extremal order-3 subbranch.

## Primary attack — weighted synchronization / odd-or-valuation charging

Work inside the exact exceptional three-way-balanced branch first, because RL30 has validated the RL29 transport theorem there.

The obstacle is now precise:

- `Omega(e/log e)` high aligned columns has vanishing density;
- a high phase may be even;
- mapping high even phases to the preceding odd phase has unbounded multiplicity when the outgoing 2-adic valuation is large.

Seek a theorem of the form:

`sum_run gain(run) >= c e/R`

for a fixed `c>0`, where each maximal synchronized/unsynchronized excursion is charged either to:

- high odd correction factors, or
- outgoing valuation / block-type information that can be inserted into an RL24-style supporting-line inequality.

Priority subquestions:

1. For a synchronized run with common parity word, derive an exact lower bound on either the number/height of odd states or the total valuations forced by long common zero stretches.
2. Combine that with the exact global valuation sum and the existing RL24 anchors; determine the sign of valuation excess in the modified inequality rather than assuming it is beneficial.
3. Quantify the gain in normalized units `R log(lambda)/L`.
4. Test whether transport excursions can be partitioned so that repeated short `Theta(log e)` synchronized runs still pay `Theta(log e)` aggregate gain per excursion.
5. Use the 47-positive-imbalance threshold only if it can be promoted to a repeated/area budget; a one-time constant threshold cannot affect the asymptotic coefficient.

## Secondary attack — algebraic sparsification

The exact factors `B-Y` and `Bw^2-Y` are owned, but the natural `F_s` are dense. Only pursue this route if you can produce a genuinely low-support relation in the rotation phase `rho`, a proper-factor divisibility with nontrivial size control, or a resultant condition comparable to the radius-3 sparse theorem.

Do not count exact factor recovery by itself as a radius-3 bridge.

## Global discipline

Maintain the corrected DAG from RL30. Even a contradiction in the exact `(12,4)` branch is local progress, not RL closure. Any claim of closure must separately handle or eliminate:

- non-near-resonant/huge-length branch;
- strict-excursion/no-balanced-return branch;
- order-2 and general cyclotomic balanced returns;
- non-extremal order-3 sectors;
- or prove a new global reduction that makes those branches irrelevant.

At session end, update the proof-state table and package a new handover.
