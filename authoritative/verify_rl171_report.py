#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
root=Path(sys.argv[1] if len(sys.argv)==2 else '.').resolve()
report=root/'RL171_RESIDUE_RANK_COORDINATE_BARRIER_2026-08-29.md'
cert=root/'RL171_CERTIFICATES'/'verify_residue_rank_decomposition.py'
assert report.is_file() and cert.is_file() and (root/'RL172_TRANSPORTED_HEIGHT_PHYSICAL_TARGET.md').is_file()
for text in ('rank(r)=sum_', 'p`, residue succession', 'coordinate barrier'):
    assert text in report.read_text()
subprocess.run([sys.executable,str(cert)],check=True)
print('RL171 report verifier: PASS')
