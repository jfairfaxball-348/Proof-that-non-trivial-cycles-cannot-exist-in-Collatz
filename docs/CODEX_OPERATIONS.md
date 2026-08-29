# Codex operations

Run commands from the repository root with `python3 tools/rl_conveyor.py`.

```sh
python3 tools/rl_conveyor.py status
python3 tools/rl_conveyor.py verify-incoming
python3 tools/rl_conveyor.py init-checkpoint
python3 tools/rl_conveyor.py check-snapshot .rl-work/RL102/authoritative-snapshot.json
```

`status` discovers the current incoming RL from the actual `authoritative/` convention. `verify-incoming` verifies the outer SHA-256 sidecar, fresh-unpacks the bundle, verifies its internal SHA-256 manifest, and runs portable `verification/verify_*.py` checks. When a handover stores its ZIP through the documented lossless Base64 transport instead of as a top-level ZIP, it first verifies every transport part and reconstructs the archive only in a temporary directory. It fails closed if the convention is ambiguous or incomplete.

`init-checkpoint` is the only write-capable command. It creates ignored `.rl-work/RL<current>/CHECKPOINT.md`, `STATE.json`, `commands.log`, `artifacts/`, and the start snapshot. Refresh these records at material milestones; record partial scans as **NOT PROMOTED** with their exact uncovered range.

Before a proposed promotion, run `check-snapshot` and `check-promotion .rl-work/RL<current>/candidate`. `preflight SNAPSHOT CANDIDATE` performs both checks. These utilities never stage, move, delete, or commit tracked research state and deliberately refuse an incomplete candidate. They complement, but never replace, the target-specific mathematical and red-team judgement.

## Closeout reserve and lock

Codex must preserve enough context/compute/tool budget to finish the full repository transition. When capacity can be estimated, reserve roughly the final 15–20% for closeout. If it cannot be estimated, stop exploration conservatively once another research step could put packaging, verification, commit, or push at risk.

On a user instruction such as **finish**, **finish up**, **close out**, **close session**, **handover**, or **commit/push**, enter `CLOSEOUT_LOCK` immediately. The same lock should be entered proactively when the closeout reserve is reached.

Create or refresh `.rl-work/RL<current>/CLOSEOUT_STATE.md` with the compact state needed to complete promotion: `BASE_HEAD`, snapshot identity, current/next RL, promoted results and corrections, candidate hashes/blob identities, completed verification, any active repair issue, exact remaining operations, expected commit message, and target branch/ref. Treat this as deliberate context compression; do not spend remaining capacity rebuilding history already frozen in the handover.

While locked, do no new mathematics, scans, historical audits, or opportunistic improvements. Run only the deterministic sequence described in `docs/CLOSEOUT_LOCK.md`: candidate freeze → red teams/verifiers → bundle/sidecar → fresh unpack → manifest/fast suite → snapshot check → one atomic Git transition → push/ref move → remote/post-commit sanity check. A closeout failure permits only the minimum stop-and-repair needed to restore a valid candidate, followed by an immediate return to closeout.

Where direct Git-object operations are available, prefer constructing the final tree/commit and advancing the branch ref once rather than consuming context on a sequence of per-file commits. With ordinary local Git, stage the complete transition, inspect it, create one commit, push it, and read the remote ref back. A local commit that has not reached the intended remote branch is not a completed RL closeout.

Ignored checkpoints are only as durable as the local execution environment. If cross-machine persistence of unfinished work is needed, use an explicitly approved non-authoritative branch or external artifact/issue store; do not place partial research state on the authoritative branch.