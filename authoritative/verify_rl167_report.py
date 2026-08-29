#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL167_FULL_AFFINE_PHASE_CLOSURE_RANK_ONE_BARRIER_2026-08-28.md'
cert = root / 'RL167_CERTIFICATES' / 'verify_full_affine_rank_one.py'
assert report.is_file() and cert.is_file()
assert (root / 'RL168_LEAST_STATE_PHASE_VALUE_CORRELATION_TARGET.md').is_file()
text = report.read_text()
for required in ('2^(a_j) N_(j+1)=3N_j+D', 'rho^L=1/2', 'not an existence result for a word'):
    assert required in text
subprocess.run([sys.executable, str(cert)], check=True)
print('RL167 report verifier: PASS')
