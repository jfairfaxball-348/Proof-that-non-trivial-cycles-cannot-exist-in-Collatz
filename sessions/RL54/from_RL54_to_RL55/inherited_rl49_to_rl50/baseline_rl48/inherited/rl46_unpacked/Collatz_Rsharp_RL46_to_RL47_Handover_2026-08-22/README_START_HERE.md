# RL46 → RL47 Handover — Start Here

This bundle continues the RL/3n+1 one-excursion branch after RL45.

## What changed in RL46

The major event was a **repair**: the exploratory virtual neutral-`11` pump quotient had been activating pumps without checking the prefix cap on the first actual pump column. That bug created false e=43..49 survivors and a false e=52 skeleton. The repaired quotient removes them.

After repair, the strongest certified progress is:

- analytic: `3` does not divide internal `T`; terminal `t` is even; the inherited moved-rank cap gives `t>=2`;
- analytic: `H=e-z+1` equals the discrete area `sum(d-1)`, so the target is exactly `H>=t+3=v2(T+1)`;
- exact cutoff-free: `(46,29,17)` has no prefix-cap terminal geometry at any excess;
- exact: `(65,41,24)` has one structural terminal record and its minimum excess is `125`;
- exact: `(149,94,55)` has no terminal state with `H<=t+3`;
- partial only: `(214,135,79)` was explored through layer 81 before state growth became too large.

## Mandatory first commands

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl46_structural_verifiers.sh
bash verification/run_rl46_q55_verifier.sh
```

Any failure is a stop-and-repair event.

Then read `RL46_REPAIR_AND_PREFIXCAP_PROGRESS.md` and `RL47_RESEARCH_KICKOFF_PROMPT_2026-08-22.md`.

## Strategic warning

Do not try to solve the unrestricted height-one quotient by proving its orbits settle; that quotient contains the ordinary Collatz map exactly. The live opportunity is to exploit the genuine near-minimum/prefix-cap constraints to prove the terminal area/valuation inequality uniformly.
