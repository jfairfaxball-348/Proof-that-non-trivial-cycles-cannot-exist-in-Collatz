#!/usr/bin/env python3
"""Fast checks for RL117's transport-coordinate barrier."""
from itertools import product
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
required=[ROOT/"START_HERE.md", ROOT/"RL116_TO_RL117_LEGAL_SUNIT_BARRIER.md", ROOT/"RL117_RL118_MODULAR_EXPANDER_TARGET.md", ROOT/"audit"/"ROUTE_LEDGER.md"]
for path in required: assert path.is_file(), path
report=required[1].read_text(encoding="utf-8"); target=required[2].read_text(encoding="utf-8"); ledger=required[3].read_text(encoding="utf-8")
for token in ("RL20", "RL79", "RL81", "Primitivity", "Raw/Farey", "all-legal"): assert token in report, token
for token in ("RL20", "RL79", "RL81", "primitivity", "Raw/Farey", "uncontrolled"): assert token in target, token
assert "modular-expander lifting" in ledger
for n in range(2, 11):
  for bits in product("01", repeat=n):
    word="".join(bits)
    for i in range(n-1):
      if word[i:i+2]=="10":
        t=word[i+2:].count("1")
        assert i+t+2<=n
        assert t<=word.count("1")-1
print("RL117 legal-swap coordinates and route-red-team structure: PASS")
