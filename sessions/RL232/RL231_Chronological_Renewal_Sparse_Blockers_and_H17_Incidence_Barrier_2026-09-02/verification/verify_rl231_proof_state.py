#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"RL231_PROOF_STATE.json"
s=json.loads(p.read_text())
assert s["format"]=="rl231-proof-state-v1"
assert s["completed_rl"]==231
assert s["incoming_rl"]==232
assert s["incoming_rl_started"] is False
assert s["success_class"]=="B"
assert s["branch_contradiction_proved"] is False
assert s["necessary_rank_count"]==13_415_865_870
assert s["e4_terminal_rank"]==31_435_476_727
assert s["e4_terminal_rank_excluded"] is False
assert s["e4_combined_survivors_through_transition_43"]==3_856_660_232
assert s["gate_a_global"]=="open"
assert s["gate_b_global"]=="open"
assert s["global_nontrivial_cycle_exclusion"]=="open"
assert s["ordinary_abs_corrected_flow_gt_numerator"]==234_578_279_671
assert s["ordinary_abs_corrected_flow_gt_denominator"]==352_321_536
assert s["further_uniform_charge_requires_combined_h17_incidence_le"]==1615
assert s["spacing_only_combined_h17_requirement_ge"]==85_103_989
assert s["knowledge_catalogue"]=="stale/deferred"
print("PASS: RL231 proof-state verifier")
