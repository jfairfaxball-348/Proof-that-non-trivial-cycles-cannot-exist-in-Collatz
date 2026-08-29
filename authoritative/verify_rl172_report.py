#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
root=Path(sys.argv[1] if len(sys.argv)==2 else '.').resolve()
report=root/'RL172_ARC_CONTENT_PARTIAL_SUM_BARRIER_2026-08-29.md'
cert=root/'RL172_CERTIFICATES'/'verify_arc_partial_sum.py'
assert report.is_file() and cert.is_file() and (root/'RL173_NEW_PHYSICAL_TRANSPORT_TARGET.md').is_file()
for text in ('qC/3^w', 'partial sum', 'not a cycle construction'):
    assert text in report.read_text()
subprocess.run([sys.executable,str(cert)],check=True)
print('RL172 report verifier: PASS')
