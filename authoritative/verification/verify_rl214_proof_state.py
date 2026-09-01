#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/"RL214_PROOF_STATE.json").read_text())

assert state["format"]=="rl214-proof-state-v1"
assert state["completed_rl"]==214
assert state["incoming_rl"]==215
assert state["base_head"]=="f0dbcb3fa0aba3d943cf4f1f91d2ff407ba9520e"
assert state["incoming_authoritative_tree"]=="3f568c15ee37b418c4d1113c05460b98c9170098"
assert state["necessary_rank_count"]==13_415_865_871
assert state["above_p_source_necessary_count"]==7_091_831_284
assert state["below_p_source_necessary_count"]==6_324_034_587
assert state["ownership_root_bridge_proved"] is True
assert state["root_cap"]=="29*y0<48*L*K0"
assert state["root_cap_integer_max"]==31_285_589_992_934_194_300_574
assert state["e16_h21_prefix_count"]==45_046
assert state["bounded_root_candidates_before_terminal_filter"]==1_629_819_720
assert state["terminal_hensel_removed_candidates"]==789
assert state["bounded_root_candidates_after_terminal_filter"]==1_629_818_931
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

target=ROOT/"RL215_H21_E16_MOD_D2_OR_P_ARC_ANCHOR_TARGET.md"
assert target.exists()
assert "Q(d) modD^2" in target.read_text()
assert "1,629,818,931" in target.read_text()

start=(ROOT/"START_HERE.md").read_text()
assert start.startswith("# RL215 incoming authoritative state")
assert "Completed predecessor: **RL214**" in start
assert "Incoming job: **RL215**" in start
assert "13,415,865,871" in start

ledger=(ROOT/"RL214_CERTIFIED_FACTS_AND_PROOF_LEDGER.md").read_text()
assert "RL214-T1" in ledger and "RL214-T2" in ledger
assert "RL214-CERT1" in ledger and "RL214-B1" in ledger
assert "No physical H21 incidence/charge" in ledger

correction=(ROOT/"RL214_CORRECTION_DEMOTION_LEDGER.md").read_text()
assert "No inherited theorem or exact finite certificate is demoted" in correction
assert "1,629,819,720" in correction

cert=json.loads((ROOT/"certificates/verify_rl214_ownership_quotient_output.json").read_text())
assert cert["status"]=="PASS"
assert cert["frontier"]==13_415_865_871
assert cert["new_rank_exclusions"]==0
assert cert["bounded_root_candidates_after_terminal_filter"]==1_629_818_931

transport=json.loads((ROOT/"transport/INHERITED_GIT_OBJECTS.json").read_text())
assert transport["base_head"]==state["base_head"]
assert transport["incoming_authoritative_tree"]==state["incoming_authoritative_tree"]
assert transport["freeze_session_path"]=="sessions/RL213"
assert transport["successor_completed_rl"]==214
assert transport["successor_incoming_rl"]==215

targets=list(ROOT.glob("RL215_*_TARGET.md"))
assert targets==[target]

print("PASS RL214 proof-state, successor uniqueness, transport pins and scope locks")
