# RL237 verification

Fast closeout suite:

```bash
bash verification/run_fast_rl237_verifiers.sh
```

It reconstructs all 7,531 retained full-prefix atomic cells, discharges generic-safe cells, evaluates exact local K budgets on the 17 genuine generic-overage candidates, verifies the final coupled schedule, invariant-specific cap arithmetic, flow lower bound, saturation slope, and RL238 freeze/pivot proof-state guard.

The promoted chronological recurrence scans are additionally represented by:

- `DEEP_RECURRENCE_OUTPUT.txt` — frozen exact run output from this RL237 session;
- `verification/verify_rl237_deep_recurrence.py` — self-contained exact deep verifier.

The deep verifier replays `320102` carry-word atoms in total. It is intentionally not part of the routine fast suite because the H20 spacing-5597 scan is computationally expensive. This preserves both verification economy and exact replayability.
