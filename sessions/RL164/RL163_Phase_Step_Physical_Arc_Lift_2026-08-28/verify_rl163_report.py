#!/usr/bin/env python3
"""Fast verifier for the RL163 authoritative report."""
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL163_PHASE_STEP_PHYSICAL_ARC_LIFT_2026-08-28.md'
target = root / 'RL164_PHASE_ARC_CONTENT_TARGET.md'
cert = root / 'RL163_CERTIFICATES' / 'verify_phase_step_lift.py'
assert report.is_file() and target.is_file() and cert.is_file()
text = report.read_text()
for required in (
    'Ap=uL+1',
    'B_j=u+1_(j=L-p)+h_j-h_(sigma(j))',
    'positive odd affine content',
    'sum_j B_j=Lu+1=pA',
    'No result applies to `g>1`',
):
    assert required in text, required
subprocess.run([sys.executable, str(cert)], check=True)
print('RL163 report verifier: PASS')
