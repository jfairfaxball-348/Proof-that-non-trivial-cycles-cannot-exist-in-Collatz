#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL165_SHALLOW_PHASE_PAIR_NONFORCING_2026-08-28.md'
target = root / 'RL166_PHASE_DISTRIBUTION_OWNERSHIP_TARGET.md'
cert = root / 'RL165_CERTIFICATES' / 'verify_shallow_phase_nonforcing.py'
assert report.is_file() and target.is_file() and cert.is_file()
text = report.read_text()
for phrase in ('No two shallow phases are inverse-phase neighbours', 'local grammar only', 'not a physical Collatz-cycle construction', 'No frontier changes'):
    assert phrase in text, phrase
subprocess.run([sys.executable, str(cert)], check=True)
print('RL165 report verifier: PASS')
