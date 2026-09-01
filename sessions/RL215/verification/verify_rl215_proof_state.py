#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/"RL215_PROOF_STATE.json").read_text())

assert state["format"]=="rl215-proof-state-v1"
assert state["completed_rl"]==215
assert state["incoming_rl"]==216
assert state["base_head"]=="478e5cace212ed60cfb8cca56ccd3496c8381b68"
assert state["incoming_authoritative_tree"]=="5f0b71bb04c21f2e0654d658a932ca4432ebfaee"
assert state["necessary_rank_count"]==13_415_865_871
assert state["above_p_source_necessary_count"]==7_091_831_284
assert state["below_p_source_necessary_count"]==6_324_034_587
assert state["root_lower_bound_integer"]==24_913_843_845_551_577_787_381
assert state["root_upper_bound_integer"]==31_285_589_992_934_194_300_574
assert state["e16_h21_prefix_count"]==45_046
assert state["two_sided_candidates_before_terminal_filter"]==331_935_455
assert state["terminal_hensel_removed_inside_window"]==170
assert state["two_sided_candidates_after_terminal_filter"]==331_935_285
assert state["arithmetic_candidates_removed_vs_rl214_post_terminal"]==1_297_883_646
assert state["prefixes_deleted"]==0
assert state["new_rank_exclusions"]==0
assert state["surviving_mod18_classes"]==[0,8,9,17]
assert state["quotient_residue_determined"] is False
assert state["physical_h21_incidence_proved"] is False
assert state["h21_charge_proved"] is False
assert state["branch_contradiction_proved"] is False
assert state["gate_a_global"]=="open"
assert state["gate_b_global"]=="open"
assert state["global_nontrivial_cycle_exclusion"]=="open"
assert state["knowledge_catalogue"]=="stale/deferred"

target=ROOT/"RL216_H21_E16_SECOND_DISCRETE_OR_SUCCESSOR_ANCHOR_TARGET.md"
assert target.exists()
assert "331,935,285" in target.read_text()

start=(ROOT/"START_HERE.md").read_text()
assert start.startswith("# RL216 incoming authoritative state")
assert "Completed predecessor: **RL215**" in start
assert "Incoming job: **RL216**" in start
assert "13,415,865,871" in start

ledger=(ROOT/"RL215_CERTIFIED_FACTS_AND_PROOF_LEDGER.md").read_text()
assert "RL215-T1" in ledger and "RL215-CERT1" in ledger
assert "No physical H21 incidence/charge" in ledger

cert=json.loads((ROOT/"certificates/verify_rl215_arc_sandwich_output.json").read_text())
assert cert["status"]=="PASS"
assert cert["frontier"]==13_415_865_871
assert cert["new_rank_exclusions"]==0
assert cert["two_sided_candidates_after_terminal_filter"]==331_935_285

transport=json.loads((ROOT/"transport/INHERITED_GIT_OBJECTS.json").read_text())
assert transport["base_head"]==state["base_head"]
assert transport["incoming_authoritative_tree"]==state["incoming_authoritative_tree"]
assert transport["freeze_session_path"]=="sessions/RL214"
assert transport["successor_completed_rl"]==215
assert transport["successor_incoming_rl"]==216

targets=list(ROOT.glob("RL216_*_TARGET.md"))
assert targets==[target]

print("PASS RL215 proof-state, successor uniqueness, transport pins and scope locks")
