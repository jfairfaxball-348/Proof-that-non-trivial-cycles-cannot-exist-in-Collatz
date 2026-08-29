#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, re

base=Path(__file__).resolve().parent
parts=sorted(base.glob('RL177_bundle.zip.b64.part*'))
if not parts:
    raise SystemExit('FAIL: no RL177 bundle parts found')
raw=base64.b64decode(b''.join(p.read_bytes() for p in parts), validate=True)
out=base/'RL177_Early_P_Shift_Mismatch_Compensation_and_Height_Split_2026-08-29.zip'
out.write_bytes(raw)
side=(base/(out.name+'.sha256')).read_text(encoding='utf-8').strip()
m=re.fullmatch(r'([0-9a-f]{64})\s+(.+)',side)
if not m or m.group(2)!=out.name:
    raise SystemExit('FAIL: malformed outer sidecar')
got=hashlib.sha256(raw).hexdigest()
if got!=m.group(1):
    raise SystemExit(f'FAIL: reconstructed ZIP hash {got} != {m.group(1)}')
print('PASS: RL177 bundle reconstructed with matching SHA-256.')
print(got, out.name)
