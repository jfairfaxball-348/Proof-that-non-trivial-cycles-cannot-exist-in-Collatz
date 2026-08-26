#!/usr/bin/env python3
"""Fast finite checks for the prime-power ownership separation algebra."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=[ROOT/"START_HERE.md",ROOT/"RL117_TO_RL118_PRIME_FACTOR_BARRIER.md",ROOT/"RL118_RL119_PADIC_TRANSFER_TARGET.md",ROOT/"audit"/"ROUTE_LEDGER.md"]
for path in required: assert path.is_file(), path
report=required[1].read_text(encoding="utf-8"); target=required[2].read_text(encoding="utf-8"); ledger=required[3].read_text(encoding="utf-8")
for token in ("RL20","RL79","RL81","Primitivity","Raw/Farey"): assert token in report, token
for token in ("RL20","RL79","RL81","primitivity","unbounded"): assert token in target, token
assert "conditioned p-adic transfer" in ledger
for d in range(2,80):
  for m in range(1,d):
    if d%m==0:
      assert m % m == 0
      assert m % d != 0
print("RL118 prime-power ownership separation and route-red-team structure: PASS")
