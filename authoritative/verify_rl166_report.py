#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
root=Path(sys.argv[1] if len(sys.argv)==2 else '.').resolve()
report=root/'RL166_PRODUCT_MASS_PHASE_PAIR_NONFORCING_2026-08-28.md'
cert=root/'RL166_CERTIFICATES'/'verify_product_mass_nonforcing.py'
assert report.is_file() and cert.is_file() and (root/'RL167_FULL_AFFINE_PHASE_DISTRIBUTION_TARGET.md').is_file()
text=report.read_text()
for s in ('R/2>3*2^71 Delta','not a cycle construction or exclusion','full cycle-closing affine equality'):
    assert s in text
subprocess.run([sys.executable,str(cert)],check=True)
print('RL166 report verifier: PASS')
