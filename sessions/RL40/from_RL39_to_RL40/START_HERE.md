# Collatz R# RL35 -> RL36 handover

Date: 2026-08-21
Status: **RL remains open.** This bundle freezes the strongest current global packing theorem (RL35), its exact certificates, the post-RL30 proof corrections, and the recommended next structural attack.

## Read first

1. `RL35_PROOF_STATUS_AND_NEXT_ATTACK.md`
2. `RL31_TO_RL35_PROGRESS_LEDGER.md`
3. `NEXT_SESSION_KICKOFF_PROMPT.md`
4. `RL35_FRESH_VERIFIER_RERUN.txt`
5. `rl31_to_rl35_additions/RL35_ANCHOR_RUN_CHARGING_AND_CF_GATE.md`
6. `rl31_to_rl35_additions/verify_rl35_anchor_run_charging.py`

For the audited pre-RL31 dependency tree, open the nested inherited bundle:

`inherited/Collatz_Rsharp_RL30_to_RL31_Handover_2026-08-21.zip`

Its `RL30_AUDIT_REPORT.md` and `NEXT_SESSION_KICKOFF_PROMPT.md` remain the authoritative correction to the earlier branch picture.

## Current strongest theorem

RL35 proves, for `R >= 10000`, the global charging inequality

`lambda * Q(R)^L <= T(R)^(12A-19L) * S(R)^(8L-5A)`

with

`Q(R)=1+1/(2000R)`,
`T(R)=256R/(256R-319)`,
`S(R)=(531441R+1568693)/(531441R)`.

Consequently

`limsup R log(lambda)/L <= 0.245797537816914843649...`.

Using the inherited **external computational** input `R >= 2^71`, the exact continued-fraction certificate gives

`L/gcd(A,L) >= 57,699,734,483`.

The next relevant convergent denominator is

`65,470,613,321`,

so RL35 does **not** cross a qualitative CF gate and does not close RL.

## What materially changed after RL30

- RL31: finite balanced-prefix envelope in the exceptional `(G,H)=(12,4)` order-3 branch.
- RL32: repaired the global support-line saturation picture using the exact high-run valuation inequality.
- RL33: forced-successor coupling for the exceptional direct type-II `k=3,h=1` block.
- RL34: grouped the forced `k=3 -> k=2` pair into an induced superblock and repaired continuation coverage (`h=13` base).
- RL35: converted deterministic successor dynamics plus nonanchor support slack into a **fixed global charging gain**.

The conceptual gain is more important than the constant: local support extremizers cannot concatenate at their individual maxima indefinitely.

## Do not accidentally regress

- `(G,H)=(12,4)` is only an exceptional extremal order-3 subbranch, not the whole RL problem.
- Closed radius-3 leaves do not by themselves close RL; the missing object is a global-to-sparse bridge.
- `R >= 2^71` is external computational input, not proved analytically here.
- Radius-3 leaves using Laurent-Mignotte-Nesterenko still depend on that published theorem.
- A local statement of the form “long resynchronization implies proportionally long preceding unsynchronized excursion” is false from gap dynamics alone.
- Do not spend the next session only shaving the RL35 coefficient unless it crosses a real branch threshold.

## Highest-value next target

Export the RL35 **successor-dynamics + slack-charging** paradigm to a branch that is still genuinely open in the RL30 DAG:

1. order-2 / `g=2` simultaneous-factor branch, preferred;
2. strict-excursion / no-balanced-return branch, second choice;
3. sparse algebraic bridge for higher cyclotomic returns only if the relation stays genuinely low-support.

The goal for RL36 should be a branch-closing lemma or a new bridge resource, not merely another decimal improvement.
