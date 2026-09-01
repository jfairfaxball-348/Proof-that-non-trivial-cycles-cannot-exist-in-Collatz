#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
p=json.loads((ROOT/"RL221_PROOF_STATE.json").read_text())

assert p["format"]=="rl221-proof-state-v1"
assert p["completed_rl"]==221
assert p["incoming_rl"]==222
assert p["incoming_rl_target"]=="RL222 Full-Period Quotient-Residue / Candidate-Wise Return Coupling"
assert p["constraint_core_selected_family_count"]==5
assert p["constraint_core_selected_intersection_nonempty"] is True
assert p["constraint_type_guard_proved"] is True
assert p["e16_phase51_candidates"]==139_581_280
assert p["e16_h21_prefix_count"]==45_045
assert p["necessary_rank_count"]==13_415_865_871
assert p["e16_terminal_rank"]==34_124_151_203
assert p["new_candidate_deletions"]==0
assert p["new_prefix_deletions"]==0
assert p["new_rank_exclusions"]==0
assert p["physical_h21_incidence_proved"] is False
assert p["h21_charge_proved"] is False
assert p["branch_contradiction_proved"] is False
assert p["gate_a_global"]=="open"
assert p["gate_b_global"]=="open"
assert p["global_nontrivial_cycle_exclusion"]=="open"
assert p["quotient_residue_Qfull_over_D_mod_D"]=="undetermined"
assert p["knowledge_catalogue"]=="stale/deferred"

w=p["explicit_common_witness"]
assert w=={
    "Q16":43079489,
    "eta":3722043165201,
    "eta_mod18":9,
    "eta_mod2187":864,
    "k":28821,
    "minimum_height_through_phase51":1,
    "state":"011",
    "terminal_nu":3,
    "y0":24921895945404894117887,
}

targets=list(ROOT.glob("RL222_*_TARGET.md"))
assert len(targets)==1
assert targets[0].name=="RL222_FULL_PERIOD_QUOTIENT_RESIDUE_CANDIDATE_RETURN_COUPLING_TARGET.md"

print("PASS RL221 proof-state / unique-successor verifier")
print("completed_rl=221 incoming_rl=222 target_count=1")
print("intersection_nonempty=true type_guard=true")
print("candidate_deletions=0 rank_exclusions=0 gates=open")
