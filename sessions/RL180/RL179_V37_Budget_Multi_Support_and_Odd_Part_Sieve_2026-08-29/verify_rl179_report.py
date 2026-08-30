#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
required=[
    'RL179_V37_BUDGET_MULTI_SUPPORT_AND_ODD_PART_SIEVE_2026-08-29.md',
    'RL179_CERTIFIED_FACTS_AND_PROOF_LEDGER.md',
    'RL179_CORRECTION_DEMOTION_LEDGER.md',
    'RL179_RED_TEAM_REPORT_2026-08-29.md',
    'RL179_SESSION_STATE_AND_RL180_KICKOFF_2026-08-29.md',
    'RL180_MULTI_SUPPORT_RESIDUE_DEFICIT_AND_ODD_PART_LIFT_TARGET.md',
    'RL179_CERTIFICATES/README.md',
    'RL179_CERTIFICATES/verify_v37_budget_and_sieve.py',
    'verification/verify_rl179_budget_and_sieve.py',
    'START_HERE.md',
]
for rel in required:
    if not (root/rel).is_file():
        raise SystemExit(f'FAIL: missing {rel}')
report=(root/'RL179_V37_BUDGET_MULTI_SUPPORT_AND_ODD_PART_SIEVE_2026-08-29.md').read_text()
for needle in [
    'F2>1/3',
    'at least **two** positive corrected-flow phases after phase 29',
    'Theorem RL179.3 — no phase-30 zero return',
    'Theorem RL179.4 — mod-8 zero-height sieve',
    'is **not excluded**',
    'Surviving necessary states are not promoted as physical existence',
]:
    if needle not in report:
        raise SystemExit(f'FAIL: report missing marker: {needle}')
for rel in [
    'verification/verify_rl179_budget_and_sieve.py',
    'RL179_CERTIFICATES/verify_v37_budget_and_sieve.py',
]:
    run=subprocess.run([sys.executable,str(root/rel)],cwd=root,text=True,capture_output=True)
    if run.returncode:
        print(run.stdout,end=''); print(run.stderr,end='')
        raise SystemExit(f'FAIL: {rel}')
    print(run.stdout,end='')
print('PASS: RL179 consolidated verifier completed successfully.')
