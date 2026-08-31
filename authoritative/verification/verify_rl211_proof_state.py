#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/"RL211_PROOF_STATE.json").read_text())
out=json.loads((ROOT/"certificates/verify_rl211_absolute_e4_selector_output.json").read_text())
trans=json.loads((ROOT/"transport/INHERITED_GIT_OBJECTS.json").read_text())
assert state["completed_rl"]==211 and state["incoming_rl"]==212
assert state["base_head"]=="ed6abb6f939b14f4ed8c2583c5784b10ab453b0c"
assert state["incoming_authoritative_tree"]=="c5cc9bed4c0e1ec09f799859982ebb79c5030c47"
assert state["necessary_rank_count"]==13_415_865_871
assert state["new_rank_exclusions"]==0
assert state["e4_eta_mod243"]==207 and state["e4_h21_state"]=="011"
assert state["flat_k_denominator_barrier_proved"] is True
assert state["physical_h21_incidence_proved"] is False
assert state["h21_charge_proved"] is False
assert state["gate_a_global"]=="open" and state["gate_b_global"]=="open"
assert state["global_nontrivial_cycle_exclusion"]=="open"
assert out["eta_mod243"]==207 and out["surviving_root_heights"]=="00001"
assert trans["base_head"]==state["base_head"]
assert trans["incoming_authoritative_tree"]==state["incoming_authoritative_tree"]
assert trans["freeze_session_path"]=="sessions/RL210"
targets=sorted(p.name for p in ROOT.glob("*TARGET*.md"))
assert targets==["RL212_H21_E16_QUOTIENT_RESIDUE_AND_FIRST_DIVERGENCE_TARGET.md"]
print("PASS RL211 proof-state, successor uniqueness, transport pins and scope locks")
