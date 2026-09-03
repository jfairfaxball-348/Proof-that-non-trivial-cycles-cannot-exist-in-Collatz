#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
HERE=Path(__file__).resolve().parent
name='RL241_Radius4_Bridge_Full_Phase_Nine_Lift_Reduction_2026-09-03.zip'
parts=sorted(HERE.glob(name+'.b64.part*'))
if not parts:
    raise SystemExit('FAIL: no transport parts')
expected={}
for line in (HERE/'PART_SHA256SUMS.txt').read_text().splitlines():
    h,n=line.split(None,1); expected[n.strip()]=h
payload=''
for p in parts:
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got != expected.get(p.name):
        raise SystemExit(f'FAIL part hash {p.name} {got}')
    payload += ''.join(p.read_text().split())
out=HERE/name
out.write_bytes(base64.b64decode(payload,validate=True))
got=hashlib.sha256(out.read_bytes()).hexdigest()
print(got, out.name)
if got != '98697aae2b112202b27bb334cbe21126d181182ea8e9f839f703a1b8422017b8':
    raise SystemExit('FAIL reconstructed zip sha256')
