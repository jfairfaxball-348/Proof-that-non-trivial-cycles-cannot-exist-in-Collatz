#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, re
ROOT=Path(__file__).resolve().parent
name='RL209_H21_Pointwise_Root_Cone_and_Above_P_Cancellation_2026-08-31.zip'
parts=sorted(ROOT.glob(name+'.b64.part*'))
assert parts, 'no parts found'
raw=''.join(p.read_text().strip() for p in parts)
data=base64.b64decode(raw, validate=True)
out=ROOT/name
out.write_bytes(data)
side=(ROOT/(name+'.sha256')).read_text().strip().split()[0]
got=hashlib.sha256(data).hexdigest()
assert got==side, (got,side)
print(f'PASS reconstructed {name} sha256={got} parts={len(parts)}')
