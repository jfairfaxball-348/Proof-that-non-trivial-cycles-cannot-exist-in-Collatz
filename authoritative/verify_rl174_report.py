#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL174_CORRECTION_AND_PHYSICAL_P_SHIFT_GAP_FLOOR_2026-08-29.md'
ledger = root / 'RL174_CORRECTION_DEMOTION_LEDGER.md'
cert = root / 'RL174_CERTIFICATES' / 'verify_p_shift_gap_repair.py'
target = root / 'RL175_CORRECTED_P_SHIFT_FLOW_CONSUMER_TARGET.md'
for path in (report, ledger, cert, target):
    assert path.is_file(), path
text = report.read_text()
for needle in (
    'q_i^(p)=2^(S_(p+i)-S_p)/3^i = q_i 2^(G_i)',
    'F2 := sum_i q_i(2^(G_i)-1)',
    'F2>3m(lambda-1)^2',
    '> 1/176',
    'h_p=0  =>  F2<2/3',
    'No non-trivial cycle is excluded',
):
    assert needle in text, needle
lt = ledger.read_text()
assert 'DEMOTED' in lt and '3^(-G_i)' in lt and '2^(G_i)' in lt
subprocess.run([sys.executable, str(cert)], check=True)
print('RL174 report verifier: PASS')
