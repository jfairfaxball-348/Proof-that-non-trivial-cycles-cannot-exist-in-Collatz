#!/usr/bin/env python3
"""Fast verifier for the RL164 authoritative report."""
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1] if len(sys.argv) == 2 else '.').resolve()
report = root / 'RL164_ARC_CONTENT_OVERLAP_BARRIER_2026-08-28.md'
target = root / 'RL165_NONLOCAL_ARC_OWNERSHIP_TARGET.md'
cert = root / 'RL164_CERTIFICATES' / 'verify_arc_content_overlap.py'
assert report.is_file() and target.is_file() and cert.is_file()
text = report.read_text()
for phrase in ('B_j>=p', 'y_j == -3^(-p)C_j', '3C_j+2^(B_j)=3^p+2^(a_j)C_(j+1)', 'not independent congruences', 'No cycle is excluded'):
    assert phrase in text, phrase
subprocess.run([sys.executable, str(cert)], check=True)
print('RL164 report verifier: PASS')
