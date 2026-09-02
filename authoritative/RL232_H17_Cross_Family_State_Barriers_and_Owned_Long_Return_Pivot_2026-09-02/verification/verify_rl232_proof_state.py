#!/usr/bin/env python3
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
s=json.loads((root/"RL232_PROOF_STATE.json").read_text())

assert s["format"]=="rl232-proof-state-v1"
assert s["completed_rl"]==232
assert s["incoming_rl"]==233
assert s["incoming_status"]=="NOT STARTED"
assert s["success_class"]=="C"
assert s["base_head"]=="98634b88b117b9c8040dd999e05e9a94c1871b26"
assert s["frontier"]["necessary_terminal_ranks"]==13_415_865_870
assert s["frontier"]["e4_terminal_rank"]==31_435_476_727
assert s["frontier"]["e4_combined_survivors_through_transition_43"]==3_856_660_232
assert s["h17"]["required_combined_incidence_cap"]==1_615
assert s["h17"]["spacing_only_requirement"]==85_103_989
assert s["h17"]["cross_family_spacing_ge"]==1001
assert s["h17"]["A"]["k_compatible_core"]==[11_443_822_977,28_746_802_249]
assert s["h17"]["B"]["k_compatible_core"]==[72_981_981_437,100_039_806_527]
assert s["barriers"]["relaxed_B_return"]["scalar_constraints_still_do_not_exclude_relaxed_events"]==655_001
assert s["barriers"]["moving_window"]["uniform_disjoint_block_packing_cap"]==4_167_516_524
assert not s["gates"]["sole_high_branch_contradicted"]
assert not s["gates"]["gate_a_closed"]
assert not s["gates"]["gate_b_closed"]
assert not s["gates"]["global_nontrivial_cycle_exclusion"]
assert s["successor_target"]=="RL233_OWNED_LONG_RETURN_DEFECT_AND_HIGHER_MODULUS_TARGET.md"
assert (root/s["successor_target"]).exists()

kick=(root/"RL232_SESSION_STATE_AND_RL233_KICKOFF_2026-09-02.md").read_text()
assert "RL233 is prepared but **NOT STARTED**" in kick
print("PASS: RL232 proof state")
