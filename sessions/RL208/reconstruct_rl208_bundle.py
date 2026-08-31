#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, re
HERE=Path(__file__).resolve().parent
STEM='RL208_H21_Layered_Root_Cone_Rank_Consumption_2026-08-31.zip'
parts=sorted(HERE.glob(STEM+'.b64.part*'))
assert parts and [p.name for p in parts]==[f'{STEM}.b64.part{i:02d}' for i in range(1,len(parts)+1)]
expected={}
for line in (HERE/'PART_SHA256SUMS.txt').read_text().splitlines():
    h,n=line.split(None,1); expected[n.strip()]=h
assert set(expected)=={p.name for p in parts}
for p in parts:
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected[p.name]
data=base64.b64decode(''.join(p.read_text().strip() for p in parts), validate=True)
out=HERE/STEM
out.write_bytes(data)
side=(HERE/(STEM+'.sha256')).read_text().strip().split()[0]
assert hashlib.sha256(data).hexdigest()==side
print(f'PASS reconstructed {STEM} sha256={side} bytes={len(data)} parts={len(parts)}')
