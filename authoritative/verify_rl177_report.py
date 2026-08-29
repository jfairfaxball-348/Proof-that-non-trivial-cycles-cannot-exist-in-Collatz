#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

base=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
required=[
    'RL177_EARLY_P_SHIFT_MISMATCH_COMPENSATION_2026-08-29.md',
    'RL177_CERTIFIED_FACTS_AND_PROOF_LEDGER.md',
    'RL177_CORRECTION_DEMOTION_LEDGER.md',
    'RL177_RED_TEAM_REPORT_2026-08-29.md',
    'RL177_SESSION_STATE_AND_RL178_KICKOFF_2026-08-29.md',
    'RL178_NEGATIVE_COMPENSATION_AND_HEIGHT_RETURN_TARGET.md',
    'RL177_CERTIFICATES/README.md',
    'RL177_CERTIFICATES/verify_early_mismatch_consumer.py',
    'verification/verify_rl177_early_mismatch.py',
]
for rel in required:
    if not (base/rel).is_file():
        raise SystemExit(f'FAIL: missing {rel}')
for rel in [
    'RL177_CERTIFICATES/verify_early_mismatch_consumer.py',
    'verification/verify_rl177_early_mismatch.py',
]:
    run=subprocess.run([sys.executable,str(base/rel)],cwd=base,text=True,capture_output=True)
    if run.returncode:
        print(run.stdout,end='')
        print(run.stderr,end='',file=sys.stderr)
        raise SystemExit(f'FAIL: {rel}')
    print(run.stdout,end='')
print('PASS: RL177 consolidated verifier completed successfully.')
