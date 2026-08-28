#!/usr/bin/env python3
"""Fast verifier for an unpacked RL161 report directory."""
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
required = [
    'START_HERE.md',
    'RL161_HOMOGENEOUS_GLOBAL_BRIDGE_BARRIER_2026-08-28.md',
    'RL161_CERTIFIED_FACTS_AND_PROOF_LEDGER.md',
    'RL161_RED_TEAM_REPORT_2026-08-28.md',
    'RL161_SESSION_STATE_AND_RL162_KICKOFF_2026-08-28.md',
    'RL162_NONHOMOGENEOUS_OWNERSHIP_BRIDGE_TARGET.md',
    'RL161_FRESH_UNPACK_REVIEW.md',
    'RL161_FRESH_UNPACK_VERIFICATION_2026-08-28.txt',
    'RL161_CERTIFICATES/verify_rl161_homogeneous_bridge.py',
    'SHA256SUMS.txt',
]
for rel in required:
    if not (root / rel).is_file():
        raise SystemExit(f'MISSING {rel}')
report = (root / 'RL161_HOMOGENEOUS_GLOBAL_BRIDGE_BARRIER_2026-08-28.md').read_text()
state = (root / 'RL161_SESSION_STATE_AND_RL162_KICKOFF_2026-08-28.md').read_text()
assert 'does not exclude non-trivial cycles' in report
assert '**OPEN.**' in state
r = subprocess.run([sys.executable, str(root / 'RL161_CERTIFICATES/verify_rl161_homogeneous_bridge.py')], text=True, capture_output=True)
if r.returncode:
    print(r.stdout)
    print(r.stderr, file=sys.stderr)
    raise SystemExit(r.returncode)
assert 'RL161 homogeneous global-bridge verifier: PASS' in r.stdout
print('RL161 REPORT VERIFIER PASS')
print(r.stdout.strip())
