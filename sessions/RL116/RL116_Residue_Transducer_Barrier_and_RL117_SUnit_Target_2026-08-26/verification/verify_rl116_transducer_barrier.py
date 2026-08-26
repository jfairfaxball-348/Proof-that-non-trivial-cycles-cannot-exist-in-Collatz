#!/usr/bin/env python3
"""Fast structural verifier for the RL116 direct-residue barrier."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
required = [ROOT / "START_HERE.md", ROOT / "RL115_TO_RL116_RESIDUE_TRANSDUCER_BARRIER.md", ROOT / "RL116_RL117_LEGAL_SUNIT_GAP_TARGET.md", ROOT / "audit" / "ROUTE_LEDGER.md"]
for path in required: assert path.is_file(), path
report = required[1].read_text(encoding="utf-8")
target = required[2].read_text(encoding="utf-8")
ledger = required[3].read_text(encoding="utf-8")
for token in ("barrier", "RL20", "RL79", "RL81", "Primitivity", "Raw/Farey"): assert token in report, token
for token in ("RL20", "RL79", "RL81", "primitivity", "Raw/Farey"): assert token in target, token
assert "legal S-unit gap" in ledger
for d in range(2, 65):
    for r in range(d):
        for s in range(d):
            if r != s:
                c = (-r) % d
                assert (r + c) % d == 0 and (s + c) % d != 0
print("RL116 direct-residue separation and route-red-team structure: PASS")
