#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=[ROOT/"START_HERE.md",ROOT/"RL118_TO_RL119_PADIC_BARRIER.md",ROOT/"RL119_RL120_NONHOMOGENEOUS_COCYCLE_TARGET.md",ROOT/"audit"/"ROUTE_LEDGER.md"]
for path in required: assert path.is_file(),path
report=required[1].read_text(); target=required[2].read_text(); ledger=required[3].read_text()
for token in ("RL20","RL79","RL81","Primitivity","Raw/Farey"): assert token in report,token
for token in ("RL20","RL79","RL81","primitivity","s!=1"): assert token in target,token
assert "non-homogeneous `+1` cocycle" in ledger
for a in range(1,25):
 for l in range(1,25):
  d=(1<<a)-3**l
  if d>0: assert d%2 and d%3
print("RL119 natural p-adic unit barrier and route-red-team structure: PASS")
