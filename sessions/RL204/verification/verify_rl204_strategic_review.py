#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]

def text(name):
    return (ROOT / name).read_text(encoding="utf-8")

ledger = text("RL204_CERTIFIED_FACTS_AND_PROOF_LEDGER.md")
correction = text("RL204_CORRECTION_DEMOTION_LEDGER.md")
report = text("RL204_STRATEGIC_REVIEW_AUDIT_AND_ROADMAP_2026-08-31.md")
kickoff = text("RL204_SESSION_STATE_AND_RL205_KICKOFF_2026-08-31.md")
target = text("RL205_GLOBAL_CLOSURE_ROUTE_TOURNAMENT_AND_INDEPENDENT_INFORMATION_TARGET.md")
start = text("START_HERE.md")

checks = {
    "rank_count": "16,188,727,234" in ledger and "remaining_necessary_ranks=16188727234" in ledger,
    "eta_classes": "0,8,9,17 mod18" in ledger,
    "no_new_math": "new_mathematical_theorems=0" in ledger and "new_rank_exclusions=0" in ledger,
    "no_demotion": "inherited_demotion=no" in ledger and "No inherited theorem" in correction,
    "h21_preserved": "H21 is retained, not demoted" in ledger and "not** a mathematical" in correction,
    "decision": "pivot now to a focused global closure route tournament in rl205" in report.lower(),
    "successor_unique": "incoming successor job RL205" in kickoff and "# RL205 target" in target,
    "gate_b_redteam": "D|Q" in target and "coboundary" in target and "D∤Q" in target,
    "plus1_redteam": "generalized-increment" in target or "generalized\n  increment" in target,
    "h21_independence": "independent-information" in target and "a>p" in target,
    "start_decision": "pivot now to rl205" in start.lower(),
}
failed=[k for k,v in checks.items() if not v]
if failed:
    print("FAIL RL204 strategic-review invariant certificate")
    print("failed=" + ",".join(failed))
    sys.exit(1)
print("PASS RL204 strategic-review invariant certificate")
print("inherited_rank_count=16188727234")
print("new_mathematical_theorems=0")
print("new_rank_exclusions=0")
print("inherited_demotion=no")
print("h21_status=retained_viable_not_automatic_next")
print("decision=pivot_now_to_RL205_route_tournament")
print("successor=RL205")
