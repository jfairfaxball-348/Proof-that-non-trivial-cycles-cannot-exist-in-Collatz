#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
s=json.loads((root/"RL236_PROOF_STATE.json").read_text())
assert s["completed_rl"]==236 and s["incoming_rl"]==237
assert s["classification"]=="Success B"
assert s["closeout_repair"] is True
assert s["h20_four_owner"]["spacing_ge"]==3032
assert s["h20_four_owner"]["occurrence_cap"]==45358853
assert s["ordinary_abs_flow_gt"]==742
assert s["next_blocker"]["spacing_sufficient"]==210
assert s["gate_A"]=="open" and s["gate_B"]=="open"
assert any(">763" in x for x in s["withdrawn"])
print("PASS: RL236 proof-state and successor guard")
print("completed_rl=236 incoming_rl=237 classification=Success B closeout_repair=yes")
print("Gates=open scratch_763=withdrawn knowledge_catalogues=stale/deferred")
