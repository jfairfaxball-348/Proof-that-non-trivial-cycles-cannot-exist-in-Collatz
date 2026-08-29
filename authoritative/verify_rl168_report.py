#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL168_DEFECT_VALUE_ORDER_AND_RANK_CAPACITY_BARRIER_2026-08-29.md'
cert = root / 'RL168_CERTIFICATES' / 'verify_defect_value_order.py'
assert report.is_file() and cert.is_file()
assert (root / 'RL169_SIMULTANEOUS_ORDERED_GAP_TARGET.md').is_file()
text = report.read_text()
for required in ('E_j<E_k  <=>  y_j<y_k', 'single-phase rank comparison', 'm>=2^71'):
    assert required in text
subprocess.run([sys.executable, str(cert)], check=True)
print('RL168 report verifier: PASS')
