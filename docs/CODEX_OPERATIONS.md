# Codex operations

Run commands from the repository root with `python3 tools/rl_conveyor.py`.

```sh
python3 tools/rl_conveyor.py status
python3 tools/rl_conveyor.py verify-incoming
python3 tools/rl_conveyor.py init-checkpoint
python3 tools/rl_conveyor.py check-snapshot .rl-work/RL102/authoritative-snapshot.json
```

`status` discovers the current incoming RL from the actual `authoritative/` convention. `verify-incoming` verifies the outer SHA-256 sidecar, fresh-unpacks the bundle, verifies its internal SHA-256 manifest, and runs portable `verification/verify_*.py` checks. It fails closed if the current convention is ambiguous or incomplete.

`init-checkpoint` is the only write-capable command. It creates ignored `.rl-work/RL<current>/CHECKPOINT.md`, `STATE.json`, `commands.log`, `artifacts/`, and the start snapshot. Refresh these records at material milestones; record partial scans as **NOT PROMOTED** with their exact uncovered range.

Before a proposed promotion, run `check-snapshot` and `check-promotion .rl-work/RL<current>/candidate`. `preflight SNAPSHOT CANDIDATE` performs both checks. These utilities never stage, move, delete, or commit tracked research state and deliberately refuse an incomplete candidate. They complement, but never replace, the target-specific mathematical and red-team judgement.

Ignored checkpoints are only as durable as the local execution environment. If cross-machine persistence of unfinished work is needed, use an explicitly approved non-authoritative branch or external artifact/issue store; do not place partial research state on the authoritative branch.
