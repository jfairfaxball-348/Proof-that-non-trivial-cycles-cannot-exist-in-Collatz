#!/usr/bin/env python3
"""Portable proof-state and scope-lock checks for the RL223 handover."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    state = json.loads((ROOT / "RL223_PROOF_STATE.json").read_text(encoding="utf-8"))
    assert state["format"] == "rl223-proof-state-v1"
    assert state["completed_rl"] == 223
    assert state["incoming_rl"] == 224
    assert state["incoming_rl_started"] is False
    assert state["necessary_rank_count"] == 13_415_865_871
    assert state["e16_phase51_candidates"] == 139_581_280
    assert state["e16_h21_prefix_count"] == 45_045
    assert state["new_candidate_deletions"] == 0
    assert state["new_prefix_deletions"] == 0
    assert state["new_rank_exclusions"] == 0
    assert state["gate_a_global"] == state["gate_b_global"] == "open"
    assert state["branch_contradiction_proved"] is False
    assert state["global_nontrivial_cycle_exclusion"] == "open"
    assert state["physical_h21_incidence_proved"] is False
    assert state["analytic_count_only_q_upper_bound_inclusive"] == 283_635
    assert state["analytic_admissible_modulus_count"] == 94_544
    assert state["bounded_probe_eligible_moduli"] == 340
    assert state["bounded_probe_surjective_moduli"] == 340
    assert state["bounded_probe_largest_minimal_prefix_length"] == 16
    assert state["knowledge_catalogue"] == "stale/deferred"

    certificate = ROOT / "certificates" / "rl223_bounded_residue_probe.json"
    assert sha256(certificate) == state["authoritative_bounded_probe_sha256"]
    cert = json.loads(certificate.read_text(encoding="utf-8"))
    exact_scope = "PROMOTED_BY_RL223_AT_UNCONSTRAINED_COUNT_ONLY_SCOPE"
    assert cert["promotion_status"] == exact_scope
    assert cert["analytic_block_switch_lemma"]["promotion_status"] == exact_scope
    assert cert["bounded_search"]["tested_modulus_count"] == 340
    assert cert["bounded_search"]["saturated_modulus_count"] == 340
    assert cert["bounded_search"]["unsaturated_moduli"] == []

    targets = list(ROOT.glob("*TARGET*.md"))
    assert [path.name for path in targets] == [
        "RL224_CANDIDATE_COUPLED_LEGAL_TAIL_LANGUAGE_ENDPOINT_TARGET.md"
    ]
    theorem = (ROOT / "RL223_ODD_MODULUS_COUNT_ONLY_SATURATION_THEOREM.md").read_text(encoding="utf-8")
    ledger = (ROOT / "RL223_CERTIFIED_FACTS_AND_PROOF_LEDGER.md").read_text(encoding="utf-8")
    target = targets[0].read_text(encoding="utf-8")
    assert "does **not** describe candidate-specific" in theorem
    assert "No actual legal H21 continuation residue set was computed" in theorem
    assert "0 candidates, 0 prefixes, and 0 ranks" in theorem
    assert "94,544" in ledger and "340 / 340" in ledger
    assert "NOT STARTED" in target
    assert "remaining length, remaining odd count" in target

    print("RL223 PROOF STATE AND SCOPE LOCKS: PASS")
    print("completed=223 incoming=224 started=false deletions=0/0/0 gates=open/open")


if __name__ == "__main__":
    main()
