# RL89 authoritative handover — start here

This bundle freezes the completed RL88 session and selects the RL89 near-capacity block-rigidity attack.

Read in this order:

1. `RL88_SESSION_STATE_AND_KICKOFF_2026-08-25.md`
2. `RL88_MULTI_BLOCK_RESET_BUDGET_AND_NESTED_FULL_D_CYLINDER.md`
3. `RL89_NEAR_CAPACITY_BLOCK_RIGIDITY_AND_ODD_COFACTOR_PACKING_TARGET.md`

Then run:

`bash verification/run_fast_rl88_verifiers.sh`

The incoming RL88 bundle was checksum-clean and its RL87 fast verifier passed.  Under the verification-economy rule, historical expensive certificates are not to be replayed unless a live dependency fails or an apparent contradiction triggers stop-and-repair.
