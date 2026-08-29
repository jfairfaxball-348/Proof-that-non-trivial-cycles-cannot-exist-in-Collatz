#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
parts=sorted(Path('.').glob('RL178_bundle.zip.b64.part*'))
if not parts:
    raise SystemExit('FAIL: no RL178 base64 parts')
data=base64.b64decode(''.join(p.read_text().strip() for p in parts))
out=Path('RL178_Negative_Compensation_and_Height_Return_2026-08-29.zip')
out.write_bytes(data)
sha=hashlib.sha256(data).hexdigest()
expected='8b3c8927e103dea8300cbddfdc3b334192e8e00bb82fe5866507fc31d7e085b5'
if sha!=expected:
    raise SystemExit(f'FAIL: sha256 {sha} != {expected}')
print(f'PASS: reconstructed {out} sha256={sha}')
