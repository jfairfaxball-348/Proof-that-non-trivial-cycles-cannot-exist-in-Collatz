#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL169_ORDERED_CHAIN_GAP_CAPACITY_BARRIER_2026-08-29.md'
cert = root / 'RL169_CERTIFICATES' / 'verify_ordered_chain_gap.py'
assert report.is_file() and cert.is_file()
assert (root / 'RL170_NONCHAIN_ORDER_PERMUTATION_TARGET.md').is_file()
text = report.read_text()
for required in ('y_k-y_j>(lambda-1)m', 'greater than `5L/2`', 'monotone-chain'):
    assert required in text
subprocess.run([sys.executable, str(cert)], check=True)
print('RL169 report verifier: PASS')
