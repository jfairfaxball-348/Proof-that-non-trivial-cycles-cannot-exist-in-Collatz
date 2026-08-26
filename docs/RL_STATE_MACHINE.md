# RL state machine

```text
Committed authority
  → start gate (HEAD + snapshot + incoming verification)
  → ignored local research/checkpoints
  → candidate handover in .rl-work/
  → complete close-out verification
  → one atomic RL transition commit
  → new committed authority
```

An interruption from the local-research or candidate state returns to the prior committed authority: leave `authoritative/` and `sessions/` untouched, refresh the local checkpoint, and make no research-state commit.

A start-gate or close-out failure enters stop-and-repair. Freeze the last valid dependency, record the demotion or correction, rerun only the necessary checks, and do not promote until the whole gate passes.

After an atomic transition, treat the new `authoritative/` generation as fresh: set a new `BASE_HEAD`, snapshot it, and rerun the ordinary start gate. A long macro-session may repeat this loop, but never combines numbered transitions.
