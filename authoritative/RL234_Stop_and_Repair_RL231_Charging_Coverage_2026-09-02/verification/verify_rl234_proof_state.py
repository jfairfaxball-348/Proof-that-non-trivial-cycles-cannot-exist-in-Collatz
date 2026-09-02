#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=json.loads((R/"RL234_PROOF_STATE.json").read_text())
assert p["completed_rl"]==234
assert p["incoming_rl"]==235
assert p["classification"]=="STOP_AND_REPAIR"
assert p["frontier"]==13415865870
assert p["e4_rank_live"]==31435476727
assert p["e4_combined_survivors"]==3856660232
assert p["preserved"]["combined_h17_spacing_ge"]>=1001
assert p["preserved"]["rl233_finite_modulus_decomposition"] is True
assert p["repair"]["first_invalid_dependency"]=="RL231_sparse_family_charging_coverage"
assert p["repair"]["counterexample"]["owners"]==[32,33,34,35]
assert p["scratch_flow_figures_promoted"] is False
assert p["open"]=={"sole_high_branch":True,"gate_a":True,"gate_b":True,"global_exclusion":True}
assert p["successor_target"]=="RL235_REPAIR_RL231_SPARSE_FAMILY_CHARGING_COVERAGE_AND_REBASE_H17_TARGET.md"
assert (R/p["successor_target"]).exists()
print("PASS: RL234 proof-state and successor guard")
print("completed_rl=234 incoming_rl=235 classification=STOP_AND_REPAIR")
print("frontier=13415865870 e4_rank=31435476727 survivors=3856660232")
print("preserved_H17_spacing_ge=1001 preserved_RL233_modulus_decomposition=yes Gates=open")
