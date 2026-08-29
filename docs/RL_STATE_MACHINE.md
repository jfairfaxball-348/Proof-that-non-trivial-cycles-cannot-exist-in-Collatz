# RL state machine

```text
Committed authority
  → start gate (HEAD + snapshot + incoming verification)
  → ignored local research/checkpoints
  → closeout reserve reached OR user says finish/close/commit-push
  → CLOSEOUT_LOCK (no new research)
  → compact CLOSEOUT_STATE.md + candidate handover in .rl-work/
  → complete close-out verification
  → one atomic RL transition commit
  → push/advance intended remote branch/ref
  → post-commit readback of sessions/ + authoritative/
  → new committed authority
```

`CLOSEOUT_LOCK` is one-way for the current RL unless the user explicitly instructs the worker to resume mathematical research. While locked, do not start new mathematics, scans, historical audits, or optional improvements. Use the compact closeout checkpoint and candidate handover instead of rebuilding conversational context. A failure in packaging or verification enters only the minimum necessary stop-and-repair, then returns directly to the closeout path.

The worker should preserve a closeout reserve rather than consuming the whole session on exploration. When capacity can be estimated, roughly the final 15–20% is reserved for packaging, verification, Git promotion, remote-ref advancement, and sanity checks. When capacity cannot be estimated, stop conservatively after a meaningful result once continuing could endanger completion.

An interruption from the local-research or candidate state returns to the prior committed authority: leave `authoritative/` and `sessions/` untouched, refresh the local checkpoint, and make no research-state commit. If closeout had begun, preserve `.rl-work/RL<current>/CLOSEOUT_STATE.md` with the exact remaining operations.

A start-gate or close-out failure enters stop-and-repair. Freeze the last valid dependency, record the demotion or correction, rerun only the necessary checks, and do not promote until the whole gate passes. If the failure occurs during `CLOSEOUT_LOCK`, do not reopen the sustained attack after repair.

A local commit alone is not the terminal state. The transition is complete only when the intended remote branch/ref points at that commit and a post-commit read confirms the frozen completed generation under `sessions/` and the new incoming generation under `authoritative/`.

After an atomic transition, treat the new `authoritative/` generation as fresh: set a new `BASE_HEAD`, snapshot it, and rerun the ordinary start gate. A long macro-session may repeat this loop, but never combines numbered transitions and should begin another RL only if enough capacity remains to preserve a fresh closeout reserve.