#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys

root = Path(sys.argv[1]) if len(sys.argv)>1 else Path(".")
req = ["RL175_CORRECTED_P_SHIFT_FLOW_CONSUMER_2026-08-29.md","RL175_CERTIFIED_FACTS_AND_PROOF_LEDGER.md","RL175_CORRECTION_DEMOTION_LEDGER.md","RL175_RED_TEAM_REPORT_2026-08-29.md","RL175_SESSION_STATE_AND_RL176_KICKOFF_2026-08-29.md","RL176_INTEGER_P_GAP_AND_MULTI_SUPPORT_TARGET.md","START_HERE.md"]
for x in req: assert (root/x).is_file(), x
text=(root/"RL175_CORRECTED_P_SHIFT_FLOW_CONSUMER_2026-08-29.md").read_text()
assert "F2 < 1/2 - Delta/16" in text
assert "6,365,000,000" in text
assert "No non-trivial cycle is excluded" in text
assert "same-root" in text.lower()
subprocess.run([sys.executable, str(root/"RL175_CERTIFICATES/verify_corrected_p_shift_consumer.py")], check=True)
print("RL175 report verifier: PASS")
