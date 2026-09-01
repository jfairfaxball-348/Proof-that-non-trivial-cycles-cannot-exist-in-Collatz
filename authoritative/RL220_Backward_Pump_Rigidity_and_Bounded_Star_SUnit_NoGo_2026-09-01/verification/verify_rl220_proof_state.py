#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/"RL220_PROOF_STATE.json").read_text())
assert state["format"]=="rl220-proof-state-v1"
assert state["completed_rl"]==220
assert state["incoming_rl"]==221
assert state["incoming_rl_target"]=="RL221 Global Constraint Intersection / Minimal Contradiction Core"
assert state["research_base_head"]=="d17e71714a6ae3d0ffe504e4c59d7f6d73c6935d"
assert state["necessary_rank_count"]==13_415_865_871
assert state["e16_phase51_candidates"]==139_581_280
assert state["e16_h21_prefix_count"]==45_045
assert state["phase51_live_cylinders"]==3_132_617
assert state["phase51_max_2adic_precision_bits"]==25
assert state["e16_terminal_rank"]==34_124_151_203
assert state["new_candidate_deletions"]==0
assert state["new_prefix_deletions"]==0
assert state["new_rank_exclusions"]==0
assert state["root_first_accelerated_v2_all_live_prefixes"]==1
assert state["b38_value"]==25185954575304774473045
assert state["b38_pre_phase51_exact_matches"]==0
assert state["gate_a_global"]=="open"
assert state["gate_b_global"]=="open"
assert state["global_nontrivial_cycle_exclusion"]=="open"
assert state["knowledge_catalogue"]=="stale/deferred"

proof=(ROOT/"proofs/RL220_BACKWARD_PUMP_RIGIDITY_AND_BOUNDED_STAR_REDUCTION.md").read_text()
for needle in (
    "RL220-T1 — fixed-block infinite-integrality rigidity",
    "RL220-T3 — bounded-star rectangular classification",
    "RL220-T4 — exact S-unit/exponential pullback",
    "does not cover correlated/nonrectangular parameter domains",
):
    assert needle in proof

corr=(ROOT/"RL220_CORRECTION_DEMOTION_LEDGER.md").read_text()
assert "No inherited mathematical claim is corrected or demoted" in corr
assert "S-unit reduction is not a solved S-unit theorem" in corr

targets=list(ROOT.glob("RL221_*TARGET.md"))
assert len(targets)==1, targets
assert targets[0].name=="RL221_GLOBAL_CONSTRAINT_INTERSECTION_MINIMAL_CONTRADICTION_CORE_TARGET.md"
text=targets[0].read_text()
for needle in (
    "Global Constraint Intersection / Minimal Contradiction Core",
    "theorem-level SAT/SMT/constraint-intersection problem",
    "Minimal Missing Bridge Set",
    "do the walls already touch?",
):
    assert needle in text
kick=(ROOT/"RL220_SESSION_STATE_AND_RL221_KICKOFF_2026-09-01.md").read_text()
assert "previously prepared local-thread RL221 target is **not promoted**" in kick
assert "changes no RL220 mathematics or classification" in kick
print("PASS RL220 proof-state / unique-successor verifier")
print("completed_rl=220 incoming_rl=221 target_count=1")
print("successor=global_constraint_intersection_minimal_contradiction_core")
print("candidate_deletions=0 rank_exclusions=0 gates=open")
