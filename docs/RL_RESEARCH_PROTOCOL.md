# RL research protocol

`AGENTS.md` is the binding operational contract. This document is its durable map for human and Codex workers.

The conveyor is `authoritative/ → one RL job → verified freeze → sessions/RL.../ + new authoritative/`. The single incoming state is `authoritative/`; `sessions/` preserves completed generations in their existing layouts and `Archive/` preserves older historical conventions. Neither a prior conversation nor scratch work can change that authority.

At job start, record `BASE_HEAD`, snapshot the tracked authoritative tree, verify the incoming sidecar and internal manifest, and run the current fresh-unpack fast suite. Once this passes, use verification economy: do not replay historical expensive certificates unless the live target requires it or a failure/contradiction demands repair.

Work only in `.rl-work/RL<current>/`. Checkpoint meaningful exact batches, candidate claims, discovered minima, failed routes, and long computations. A checkpoint is explicitly non-authoritative and may disappear with its execution environment.

Keep analytic theorems, exact certificates, inherited certificates, evidence, conjectures, barriers, demotions, and obligations distinct. Preserve the incoming scope and named red teams. On any integrity failure, contradiction, scope error, range gap, failed red team, or invalidated floor, stop ordinary work and repair from the last sound frontier.

## Reserved closeout phase

A worker must preserve enough remaining context/compute/tool capacity to finish the repository transaction. When capacity is estimable, reserve roughly the final 15–20% for closeout; otherwise stop conservatively once continued exploration could threaten a clean promotion. Stabilizing one more marginal result is less important than leaving one complete, auditable RL generation.

An explicit user request to **finish**, **finish up**, **close out**, **close session**, **make the handover**, or **commit/push** enters `CLOSEOUT_LOCK` immediately. The worker may also enter it proactively when the closeout reserve is reached. Once locked, new mathematics, scans, historical audits, and opportunistic improvements stop. Create `.rl-work/RL<current>/CLOSEOUT_STATE.md` as a compact context-compression record and execute only the verify/package/promote/push/post-check sequence in `docs/CLOSEOUT_LOCK.md`.

A failure during closeout permits only the smallest necessary stop-and-repair, followed by a direct return to closeout. Closeout is complete only after the intended remote branch/ref points at the new atomic transition commit and the committed `sessions/` and `authoritative/` paths have been read back successfully.

Only a completed and independently verified handover can become an atomic transition. No partial research commit is allowed.