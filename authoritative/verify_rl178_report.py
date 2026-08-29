#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
required=[
    'RL178_NEGATIVE_COMPENSATION_AND_HEIGHT_RETURN_2026-08-29.md',
    'RL178_CERTIFIED_FACTS_AND_PROOF_LEDGER.md',
    'RL178_CORRECTION_DEMOTION_LEDGER.md',
    'RL178_RED_TEAM_REPORT_2026-08-29.md',
    'RL178_SESSION_STATE_AND_RL179_KICKOFF_2026-08-29.md',
    'RL179_V37_NEGATIVE_RETURN_AND_ZERO_HEIGHT_TRANSITION_TARGET.md',
    'RL178_CERTIFICATES/README.md',
    'RL178_CERTIFICATES/verify_second_transition_consumer.py',
    'verification/verify_rl178_second_transition.py',
    'START_HERE.md',
]
for rel in required:
    p=root/rel
    if not p.is_file():
        raise SystemExit(f'FAIL: missing {rel}')
report=(root/'RL178_NEGATIVE_COMPENSATION_AND_HEIGHT_RETURN_2026-08-29.md').read_text()
for needle in [
    '(v,H,J,d)=(37,0,23,+1)',
    'is impossible',
    'G_i<0',
    'phase `29`',
    'Surviving necessary states are **not** promoted as physical existence',
]:
    if needle not in report:
        raise SystemExit(f'FAIL: report missing marker: {needle}')
for rel in [
    'verification/verify_rl178_second_transition.py',
    'RL178_CERTIFICATES/verify_second_transition_consumer.py',
]:
    run=subprocess.run([sys.executable,str(root/rel)],cwd=root,text=True,capture_output=True)
    if run.returncode:
        print(run.stdout,end='')
        print(run.stderr,end='')
        raise SystemExit(f'FAIL: {rel}')
    print(run.stdout,end='')
print('PASS: RL178 consolidated verifier completed successfully.')
