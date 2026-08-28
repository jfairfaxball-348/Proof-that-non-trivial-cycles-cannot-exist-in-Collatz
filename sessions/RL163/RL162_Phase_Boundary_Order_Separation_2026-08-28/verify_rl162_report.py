#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
required = [
    'START_HERE.md',
    'RL162_PHASE_BOUNDARY_ORDER_SEPARATION_2026-08-28.md',
    'RL162_CERTIFIED_FACTS_AND_PROOF_LEDGER.md',
    'RL162_RED_TEAM_REPORT_2026-08-28.md',
    'RL162_SESSION_STATE_AND_RL163_KICKOFF_2026-08-28.md',
    'RL163_PHASE_ORDER_PHYSICAL_BRIDGE_TARGET.md',
    'RL162_FRESH_UNPACK_REVIEW.md',
    'RL162_FRESH_UNPACK_VERIFICATION_2026-08-28.txt',
    'RL162_CERTIFICATES/verify_rl162_phase_boundary_order.py',
    'SHA256SUMS.txt',
]
for rel in required:
    if not (root / rel).is_file():
        raise SystemExit(f'MISSING {rel}')
report = (root / 'RL162_PHASE_BOUNDARY_ORDER_SEPARATION_2026-08-28.md').read_text()
state = (root / 'RL162_SESSION_STATE_AND_RL163_KICKOFF_2026-08-28.md').read_text()
assert 'not a cycle construction' in report
assert '**OPEN.**' in state
r = subprocess.run([sys.executable, str(root / 'RL162_CERTIFICATES/verify_rl162_phase_boundary_order.py')], text=True, capture_output=True)
if r.returncode:
    print(r.stdout)
    print(r.stderr, file=sys.stderr)
    raise SystemExit(r.returncode)
assert 'RL162 phase-boundary order-separation verifier: PASS' in r.stdout
print('RL162 REPORT VERIFIER PASS')
print(r.stdout.strip())
