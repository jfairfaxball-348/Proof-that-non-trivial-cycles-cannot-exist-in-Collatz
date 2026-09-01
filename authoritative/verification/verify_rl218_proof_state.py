#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
s=json.loads((ROOT/"RL218_PROOF_STATE.json").read_text())

assert s["format"]=="rl218-proof-state-v1"
assert s["completed_rl"]==218 and s["incoming_rl"]==219
assert s["base_head"]=="ffcc8711a8512b6f8d05438b6247ec1cb1d9d46c"
assert s["incoming_authoritative_tree"]=="2a6df1f35fbe68689aa8dad10b1db26db77efbcc"
assert s["necessary_rank_count"]==13415865871
assert s["inherited_necessary_rank_count"]==13415865871
assert s["above_p_source_necessary_count"]==7091831284
assert s["below_p_source_necessary_count"]==6324034587
assert s["e16_phase51_candidates"]==139581280
assert s["e16_h21_prefix_count"]==45045
assert s["e16_terminal_rank"]==34124151203
assert s["e16_reachable_eta_mod2187"]==469
assert s["state011_survivors"]==90749885
assert s["state111_survivors"]==48831395
assert s["mod18_survivors"]=={"0":35622831,"8":19167422,"9":55127054,"17":29663973}
assert s["phase51_live_cylinders"]==3132617
assert s["phase51_max_2adic_precision_bits"]==25
assert s["phase51_survivor_digest_sha256"]=="abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05"
assert s["new_analytic_result_groups"]==[]
assert s["new_exact_certificates"]==[]
assert s["new_method_barriers"]==[]
assert s["new_rank_exclusions"]==0 and s["new_prefix_deletions"]==0
assert s["scratch_status"]=="unavailable_not_promoted"
assert s["rl218_target_status"]=="unfinished_reissued_to_rl219"
assert s["physical_h21_incidence_proved"] is False
assert s["h21_charge_proved"] is False
assert s["branch_contradiction_proved"] is False
assert s["gate_a_global"]=="open" and s["gate_b_global"]=="open"
assert s["global_nontrivial_cycle_exclusion"]=="open"

start=(ROOT/"START_HERE.md").read_text()
target=(ROOT/"RL219_CERTIFIED_BLUE_LATTICE_RECOGNITION_CONTINUATION_TARGET.md").read_text()
ledger=(ROOT/"RL218_CERTIFIED_FACTS_AND_PROOF_LEDGER.md").read_text()
notice=(ROOT/"RL218_UNRECOVERED_CODEX_SCRATCH.md").read_text()
assert "# RL219 incoming authoritative state" in start
assert "Completed predecessor: **RL218**" in start
assert "# RL219 target" in target and "Recovery-first rule" in target
assert "No new RL218 theorem" in ledger
assert "NOT PROMOTED" in notice
assert not (ROOT/"RL218_CERTIFIED_BLUE_LATTICE_RECOGNITION_EXPLORATION_TARGET.md").exists()

print("PASS RL218 interrupted-closeout proof-state guard")
print("completed_rl=218 incoming_rl=219")
print("frontier=13415865871 e16_candidates=139581280 prefixes=45045")
print("new_math=0 scratch=unavailable_not_promoted")
print("gate_a=open gate_b=open global_nontrivial_cycle_exclusion=open")
