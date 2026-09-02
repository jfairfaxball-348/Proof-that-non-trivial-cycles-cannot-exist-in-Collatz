#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]
s=json.loads((p/"RL237_PROOF_STATE.json").read_text())
assert s["completed_rl"]==237
assert s["incoming_rl"]==238
assert s["classification"]=="Success B"
assert s["program_status"]=="frozen_returnable"
assert s["pivot"]=="Gate B radius 4"
assert s["recurrence"]["H20_323334"]["spacing_ge"]==210
assert s["recurrence"]["H20_3136"]["spacing_ge"]==5597
assert s["recurrence"]["H21_3435_returnability"]["spacing_ge"]==3032
assert s["charging"]["atomic_cells"]==7531
assert s["charging"]["ordinary_abs_flow_gt"]==742.4232
assert s["charging"]["next_blocker"]["spacing_needed"]==22242932
assert s["gate_A"]=="open" and s["gate_B"]=="open"
assert s["radius3"]=="proved_inherited_but_global_bridge_open"
assert s["radius4"]=="RL238_active_pivot_not_started"
target=(p/"RL238_RADIUS4_GATE_B_PIVOT_TARGET.md").read_text()
assert "radius 4" in target.lower()
assert "Gate B" in target
assert "frozen" in target.lower()
print("PASS: RL237 proof-state / freeze / RL238 pivot guard")
print("completed_rl=237 incoming_rl=238 classification=Success B")
print("charging_program=frozen_returnable")
print("RL238_target=Gate_B_radius_4")
print("Gates=open radius3_bridge=open")
