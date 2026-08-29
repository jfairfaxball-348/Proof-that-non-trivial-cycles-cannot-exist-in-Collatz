#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
for rel in [
    "RL176_INTEGER_P_GAP_AND_MULTI_SUPPORT_CONSUMER_2026-08-29.md",
    "RL176_CERTIFIED_FACTS_AND_PROOF_LEDGER.md",
    "RL176_SESSION_STATE_AND_RL177_KICKOFF_2026-08-29.md",
    "RL176_RED_TEAM_REPORT_2026-08-29.md",
    "RL177_EARLY_P_SHIFT_MISMATCH_AND_GAP_VALUATION_TARGET.md",
    "verification/verify_rl176_integer_p_gap.py",
    "RL176_CERTIFICATES/verify_integer_p_gap_consumer.py",
]:
    if not (base/rel).is_file():
        raise SystemExit(f"FAIL: missing {rel}")

for rel in [
    "verification/verify_rl176_integer_p_gap.py",
    "RL176_CERTIFICATES/verify_integer_p_gap_consumer.py",
]:
    run=subprocess.run([sys.executable,str(base/rel)],cwd=base,text=True,capture_output=True)
    if run.returncode:
        print(run.stdout,end="")
        print(run.stderr,end="",file=sys.stderr)
        raise SystemExit(f"FAIL: {rel}")
    print(run.stdout,end="")
print("PASS: RL176 consolidated verifier completed successfully.")
