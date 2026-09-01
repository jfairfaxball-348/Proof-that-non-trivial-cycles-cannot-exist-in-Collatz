#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
state = json.loads((root / "RL222_PROOF_STATE.json").read_text())

assert state["completed_rl"] == 222
assert state["incoming_rl"] == 223
assert state["e16_phase51_candidates"] == 139581280
assert state["e16_h21_prefix_count"] == 45045
assert state["necessary_rank_count"] == 13415865871
assert state["e16_terminal_rank"] == 34124151203
assert state["new_candidate_deletions"] == 0
assert state["new_prefix_deletions"] == 0
assert state["new_rank_exclusions"] == 0
assert state["gate_a_global"] == "open"
assert state["gate_b_global"] == "open"
assert state["global_nontrivial_cycle_exclusion"] == "open"
assert state["physical_h21_incidence_proved"] is False
assert state["denominator_certified_lower_bound"] > state["root_upper_bound_integer"]
assert "no wrap" in state["qfull_mod_D2_status"]
assert state["local_two_adic_tail_prefix_selector"].startswith("proved structurally automatic")
targets = list(root.glob("RL223_*_TARGET.md"))
assert len(targets) == 1

print("PASS RL222 proof-state / unique-successor verifier")
print("completed_rl=222 incoming_rl=223 target_count=1")
print("candidate_deletions=0 prefix_deletions=0 rank_exclusions=0")
print("gates=open knowledge_catalogue=stale/deferred")
