#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/"RL216_PROOF_STATE.json").read_text())

assert state["format"]=="rl216-proof-state-v1"
assert state["completed_rl"]==216
assert state["incoming_rl"]==217
assert state["base_head"]=="a6b524ff8b8920ee357db83d59ebb1112a39e1fe"
assert state["incoming_authoritative_tree"]=="69e33054cccd6c18af325d98f48d491b3a28645d"
assert state["necessary_rank_count"]==13_415_865_871
assert state["above_p_source_necessary_count"]==7_091_831_284
assert state["below_p_source_necessary_count"]==6_324_034_587
assert state["root_lower_bound_integer"]==24_913_843_845_551_577_787_381
assert state["root_upper_bound_integer"]==31_285_589_992_934_194_300_574
assert state["e16_h21_prefix_count"]==45_045
assert state["targeted_e16_candidates_after_rl216"]==331_927_916
assert state["arithmetic_candidates_removed_vs_rl215"]==7_369
assert state["targeted_prefix_Q_deleted"]==43_013_953
assert state["prefixes_deleted"]==1
assert state["e16_reachable_eta_mod2187"]==469
assert state["new_rank_exclusions"]==0
assert state["state011_prefix_count"]==29_286
assert state["state111_prefix_count"]==15_759
assert state["state011_candidate_count"]==215_802_853
assert state["state111_candidate_count"]==116_125_063
assert state["surviving_mod18_candidate_counts"]=={"0":107901476,"8":58062518,"9":107901377,"17":58062545}
assert state["surviving_mod18_classes"]==[0,8,9,17]
assert state["quotient_residue_determined"] is False
assert state["physical_h21_incidence_proved"] is False
assert state["h21_charge_proved"] is False
assert state["branch_contradiction_proved"] is False
assert state["gate_a_global"]=="open"
assert state["gate_b_global"]=="open"
assert state["global_nontrivial_cycle_exclusion"]=="open"
assert state["knowledge_catalogue"]=="stale/deferred"

target=ROOT/"RL217_H21_E16_PREFIX_WIDE_MODULAR_HEIGHT_CONE_TARGET.md"
assert target.exists()
assert "331,927,916" in target.read_text()
assert "Do not enumerate" in target.read_text()

start=(ROOT/"START_HERE.md").read_text()
assert start.startswith("# RL217 incoming authoritative state")
assert "Completed predecessor: **RL216**" in start
assert "Incoming job: **RL217**" in start
assert "13,415,865,871" in start
assert "45,045 prefixes" in start

ledger=(ROOT/"RL216_CERTIFIED_FACTS_AND_PROOF_LEDGER.md").read_text()
assert "RL216-T1" in ledger and "RL216-CERT1" in ledger
assert "No necessary rank is deleted" in ledger

cert=json.loads((ROOT/"certificates/verify_rl216_e16_root_tail_cone_output.json").read_text())
assert cert["status"]=="PASS"
assert cert["canonical_prefix_Q"]==43_013_953
assert cert["prefixes_deleted"]==1
assert cert["arithmetic_candidates_removed_vs_rl215"]==7_369
assert cert["two_sided_candidates_after_rl216_targeted_deletion"]==331_927_916
assert cert["frontier"]==13_415_865_871
assert cert["new_rank_exclusions"]==0

transport=json.loads((ROOT/"transport/INHERITED_GIT_OBJECTS.json").read_text())
assert transport["base_head"]==state["base_head"]
assert transport["incoming_authoritative_tree"]==state["incoming_authoritative_tree"]
assert transport["freeze_session_path"]=="sessions/RL215"
assert transport["successor_completed_rl"]==216
assert transport["successor_incoming_rl"]==217

targets=list(ROOT.glob("RL217_*_TARGET.md"))
assert targets==[target]

print("PASS RL216 proof-state, successor uniqueness, transport pins and scope locks")
