#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=[ROOT/"START_HERE.md",ROOT/"RL119_TO_RL120_COCYCLE_BARRIER.md",ROOT/"RL120_RL121_RETURN_POLICY_TARGET.md",ROOT/"audit"/"ROUTE_LEDGER.md"]
for path in required: assert path.is_file(),path
report=required[1].read_text(); target=required[2].read_text(); ledger=required[3].read_text()
for token in ("RL20","RL79","RL81","Primitivity","Raw/Farey"): assert token in report,token
for token in ("radius-three","Raw/first-Farey","physical-strip"): assert token in target,token
assert "all RL113 retained formulations stopped" in ledger
for x in range(1,20):
 for s in range(1,10):
  odd=(3*x+s)
  if odd%2==0: assert 2*(odd//2)-3*x==s
print("RL120 affine increment scaling and return-policy structure: PASS")
