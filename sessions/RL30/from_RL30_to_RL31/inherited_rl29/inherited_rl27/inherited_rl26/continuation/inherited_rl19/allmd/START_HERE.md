# RL19 START HERE — exact radius-3 closure + global least-state packing

Date: 2026-08-20

This bundle supersedes RL18 as the working handover. It **does not claim a proof of RL or of the Collatz conjecture**.

## Main result of RL19

The final exact-radius-3 leaf

`gcd(A,L)=3`, `gcd(A,m)=1`

is now closed for primitive full-`D` self-rotations, conditional on the inherited audited RL10/RL17 reduction chain.

The closure is analytic and does not use the old `a<=80` scan. The proof is in `RL19_CUBIC_SKEW_ANALYTIC_CLOSURE.md` and splits into:

1. exact weak interlacing of the three jump events with their inverse-step translate;
2. a short-order obstruction for the one-gap-`a` boundary;
3. an Eisenstein lift/norm bound for the interior skew sector;
4. small nonzero resultant bounds for the only two extreme sectors;
5. equal gaps imply nonprimitivity.

The dedicated verifier is `verify_rl19_cubic_skew_closure.py`.

## Global RL progress

RL itself remains **OPEN**. Exact radius 3 is only a local theorem; no global theorem currently forces an RL object to encounter radius 3.

RL19 adds three radius-independent analytic tools:

- exact positive lift and arbitrary-radius weighted-difference identity;
- exact odd/even weighted populations plus least-state state packing;
- exact odd-step product identity
  `2^A/3^L = prod_(odd phases) (1+1/(3x_i))`,
  giving the stronger logarithmic packing bound
  `log(2^A/3^L) <= 1/(3R#)+(1/6)log(1+2(L-1)/R#)`.

These force a near-resonance/huge-length dichotomy but do not yet contradict RL.

## Important caution on the old bounded-radius bridge

During RL19 a length-184 local-grammar countermodel was found in-session suggesting that RL-L27/RL-L36/RL-L54 alone do not force a radius-3 distinguished pair. However the exact binary word/certificate was not frozen into the artifact set before closeout.

Therefore this bundle labels that falsification as **COMPUTATIONAL/SESSION EVIDENCE, NOT YET A FROZEN CERTIFICATE**. The next session should reconstruct and freeze the countermodel before treating the bridge as formally retired. In any event, no such local countermodel is a counterexample to RL because it does not establish the global `D|Q` condition.

## Run first

From this directory:

```bash
python verify_rl18_repairs.py
python verify_rl18_global_orbit_identity.py
python verify_rl18_cubic_norm_reduction.py
python inherited/verify_rl12_same_direction_canonical.py
python inherited/verify_rl13_p3_j0_interior.py
python verify_rl19_cubic_skew_closure.py
python verify_rl19_global_weighted_population.py
python verify_rl19_global_odd_step_product.py
```

Treat any assertion failure as a stop-and-repair event.

Note: the inherited RL12 checker is slow enough to exceed some hosted per-command limits. A completed fresh PASS log from the RL18/RL19 session is retained at `logs/RL12_FRESH_RECHECK_LOG.txt`; do not reinterpret a host timeout as a mathematical failure.

## Reading order

1. `RL19_PROOF_STATUS_AND_BRANCH_LEDGER.md`
2. `RL19_CUBIC_SKEW_ANALYTIC_CLOSURE.md`
3. `RL19_GLOBAL_WEIGHTED_POPULATION_AND_STATE_PACKING.md`
4. `RL19_GLOBAL_ODD_STEP_PRODUCT_BOUND.md`
5. `RL18_GLOBAL_ORBIT_SUM_IDENTITY.md`
6. `RL18_EXTERNAL_DEPENDENCY_AUDIT.md`
7. `RL19_SESSION_CLOSEOUT.md`
8. `NEXT_SESSION_KICKOFF_PROMPT.md`

Maintain the evidence labels exactly: **ANALYTIC**, **EXTERNAL: LMN**, **EXACT FINITE CERTIFICATE**, **EXTERNAL COMPUTATIONAL INPUT**, **COMPUTATIONAL EVIDENCE**, **OPEN**.
