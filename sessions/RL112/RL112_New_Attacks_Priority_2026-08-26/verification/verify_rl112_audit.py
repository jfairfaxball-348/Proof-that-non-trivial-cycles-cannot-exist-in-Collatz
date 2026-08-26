#!/usr/bin/env python3
"""Structural verifier for the RL112 audit package; no theorem judgement."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    root / "START_HERE.md",
    root / "RL111_TO_RL112_FREEZE_AND_FULL_AUDIT.md",
    root / "RL112_NEW_ATTACKS_PRIORITY_TARGET.md",
    root / "audit" / "LEMMA_AND_RESULT_REGISTRY.md",
]
for path in required:
    assert path.is_file(), path
audit = required[1].read_text(encoding="utf-8")
target = required[2].read_text(encoding="utf-8")
registry = required[3].read_text(encoding="utf-8")
assert "Gate A globally, Gate B globally, non-trivial-cycle exclusion" in audit
assert "**open**" in audit
assert "RL101" in audit and "RL112" in audit
assert target.count("**") >= 24, "expected twelve named slate items"
assert registry.count("| RL") >= 20, "expected canonical registry entries"
for token in ("RL20", "RL79", "RL81", "primitivity", "Raw/Farey"):
    assert token in audit or token in registry or token in target, token
print("RL112 audit package structural verifier: PASS")
