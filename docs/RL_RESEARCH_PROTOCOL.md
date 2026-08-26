# RL research protocol

`AGENTS.md` is the binding operational contract. This document is its durable map for human and Codex workers.

The conveyor is `authoritative/ → one RL job → verified freeze → sessions/RL.../ + new authoritative/`. The single incoming state is `authoritative/`; `sessions/` preserves completed generations in their existing layouts and `Archive/` preserves older historical conventions. Neither a prior conversation nor scratch work can change that authority.

At job start, record `BASE_HEAD`, snapshot the tracked authoritative tree, verify the incoming sidecar and internal manifest, and run the current fresh-unpack fast suite. Once this passes, use verification economy: do not replay historical expensive certificates unless the live target requires it or a failure/contradiction demands repair.

Work only in `.rl-work/RL<current>/`. Checkpoint meaningful exact batches, candidate claims, discovered minima, failed routes, and long computations. A checkpoint is explicitly non-authoritative and may disappear with its execution environment.

Keep analytic theorems, exact certificates, inherited certificates, evidence, conjectures, barriers, demotions, and obligations distinct. Preserve the incoming scope and named red teams. On any integrity failure, contradiction, scope error, range gap, failed red team, or invalidated floor, stop ordinary work and repair from the last sound frontier.

Only a completed and independently verified handover can become an atomic transition. No partial research commit is allowed.
