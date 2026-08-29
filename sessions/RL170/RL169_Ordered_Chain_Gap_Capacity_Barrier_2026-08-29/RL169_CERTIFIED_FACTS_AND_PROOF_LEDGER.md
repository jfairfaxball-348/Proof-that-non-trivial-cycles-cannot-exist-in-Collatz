# RL169 certified facts and proof ledger

## New analytic facts

- RL169.1: forward chronological pairs with increasing lifted defects have
  state gap greater than `(lambda-1)m`.
- RL169.2: direct monotone-chain capacity is greater than `5L/2`, so it
  cannot limit a chain of at most `L` phases.

## Exact finite audit

- `RL169_CERTIFICATES/verify_ordered_chain_gap.py` passed: inherited theta
  bound, exact capacity arithmetic, and 5,460 ordinary affine increment
  checks.

## Carried limitations

- No cycle is constructed or excluded.
- Only monotone-chain aggregation is exhausted; non-chain simultaneous
  structure remains a live research target.
