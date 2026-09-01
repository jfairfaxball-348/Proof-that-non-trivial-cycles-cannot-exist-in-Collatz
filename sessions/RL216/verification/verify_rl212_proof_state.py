#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/"RL212_PROOF_STATE.json").read_text())
out=json.loads((ROOT/"certificates/verify_rl212_e16_quotient_residue_output.json").read_text())
trans=json.loads((ROOT/"transport/INHERITED_GIT_OBJECTS.json").read_text())

assert state["completed_rl"]==212 and state["incoming_rl"]==213
assert state["base_head"]=="61ddae2d2e35d6a6e412d04498d5b0b945192cba"
assert state["incoming_authoritative_tree"]=="875ed0a54081e596eb21edde255e84d3d5970ab4"
assert state["necessary_rank_count"]==13_415_865_871
assert state["new_rank_exclusions"]==0
assert state["e16_root_prefix_count"]==108_950
assert state["e16_h21_compatible_prefix_count"]==45_046
assert state["e16_state011_prefix_count"]==29_286
assert state["e16_state111_prefix_count"]==15_760
assert state["first_informative_ternary_power"]==7
assert state["e16_h21_reachable_mod2187"]==469
assert state["e16_h21_universe_mod2187"]==486
assert state["e16_forbidden_eta_mod2187"]==[0, 53, 431, 891, 917, 972, 1160, 1295, 1458, 1493, 1565, 1620, 1701, 1862, 2060, 2088, 2106]
assert state["root_unit_lift_unique"] is True
assert state["terminal_valuation_crt_independent"] is True
assert state["terminal_parity_selected"] is False
assert state["physical_h21_incidence_proved"] is False
assert state["h21_charge_proved"] is False
assert state["gate_a_global"]=="open" and state["gate_b_global"]=="open"
assert state["global_nontrivial_cycle_exclusion"]=="open"

assert out["status"]=="PASS"
assert out["root_prefix_count"]==state["e16_root_prefix_count"]
assert out["h21_compatible_prefix_count"]==state["e16_h21_compatible_prefix_count"]
assert out["forbidden_eta_mod2187"]==state["e16_forbidden_eta_mod2187"]
assert out["root_unit_lift_unique_for_h21_prefixes"] is True
assert out["terminal_valuation_crt_independent"] is True
assert out["new_rank_exclusions"]==0

assert trans["base_head"]==state["base_head"]
assert trans["incoming_authoritative_tree"]==state["incoming_authoritative_tree"]
assert trans["freeze_session_path"]=="sessions/RL211"
assert trans["successor_completed_rl"]==212 and trans["successor_incoming_rl"]==213

targets=sorted(p.name for p in ROOT.glob("*TARGET*.md"))
assert targets==["RL213_H21_E16_TERNARY_HOLES_AND_GLOBAL_CONSUMER_TARGET.md"]

print("PASS RL212 proof-state, successor uniqueness, transport pins and scope locks")
