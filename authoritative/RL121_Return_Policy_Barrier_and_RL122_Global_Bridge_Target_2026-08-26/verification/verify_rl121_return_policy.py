#!/usr/bin/env python3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "START_HERE.md",
    ROOT / "RL120_TO_RL121_RETURN_POLICY_BARRIER.md",
    ROOT / "RL121_RL122_GLOBAL_BRIDGE_GENERATION_TARGET.md",
    ROOT / "audit" / "OPEN_OBLIGATION_FRONTIER.md",
]
for p in required:
    assert p.is_file(), p
report = required[1].read_text(encoding="utf-8")
target = required[2].read_text(encoding="utf-8")
frontier = required[3].read_text(encoding="utf-8")
for token in ("RL20", "RL79", "RL81", "Primitivity", "Raw/Farey"):
    assert token in report, token
for token in ("radius-three", "Gate-A", "physical-strip", "full-ownership"):
    assert token in target, token
for token in ("Radius-three global producer", "Gate-A universal consumer", "Global physical/support force"):
    assert token in frontier, token
assert report.count("absent") >= 3
assert "No inherited theorem is demoted" in report
assert frontier.count("OPEN") >= 7
print("RL121 return-policy registry barrier and open-frontier structure: PASS")
