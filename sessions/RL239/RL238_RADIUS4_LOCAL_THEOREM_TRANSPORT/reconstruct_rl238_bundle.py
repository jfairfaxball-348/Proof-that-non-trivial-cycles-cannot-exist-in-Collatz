#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
HERE=Path(__file__).resolve().parent
name='RL238_Radius4_Local_Theorem_Authoritative_2026-09-03.zip'
parts=sorted(HERE.glob(name+'.b64.part*'))
if not parts:
    raise SystemExit('FAIL: no transport parts')
expected={}
for line in (HERE/'PART_SHA256SUMS.txt').read_text().splitlines():
    h,n=line.split(None,1); expected[n.strip()]=h
for p in parts:
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got!=expected.get(p.name):
        raise SystemExit(f'FAIL part checksum {p.name}')
payload=''.join(p.read_text().strip() for p in parts)
out=HERE/name
out.write_bytes(base64.b64decode(payload,validate=True))
print(hashlib.sha256(out.read_bytes()).hexdigest(), out.name)
