#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL170_ORDER_PERMUTATION_BUDGET_BARRIER_2026-08-29.md'
cert = root / 'RL170_CERTIFICATES' / 'verify_order_permutation_budget.py'
assert report.is_file() and cert.is_file()
assert (root / 'RL171_ARITHMETIC_RANK_POSITION_TARGET.md').is_file()
text = report.read_text()
for required in ('mQ+2R <=', 'least-state slack exceeds', 'non-chain'):
    assert required in text
subprocess.run([sys.executable, str(cert)], check=True)
print('RL170 report verifier: PASS')
