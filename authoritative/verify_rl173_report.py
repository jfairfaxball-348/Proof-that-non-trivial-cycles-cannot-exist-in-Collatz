#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
root=Path(sys.argv[1] if len(sys.argv)==2 else '.').resolve()
report=root/'RL173_P_SHIFT_WEIGHTED_FLOW_SIGN_NONFORCING_2026-08-29.md'
cert=root/'RL173_CERTIFICATES'/'verify_p_shift_sign_nonforcing.py'
assert report.is_file() and cert.is_file() and (root/'RL174_PHYSICAL_GAP_TARGET.md').is_file()
for text in ('F=-52/81', 'F=176/27', 'Neither word is asserted to be a physical cycle'):
    assert text in report.read_text()
subprocess.run([sys.executable,str(cert)],check=True)
print('RL173 report verifier: PASS')
