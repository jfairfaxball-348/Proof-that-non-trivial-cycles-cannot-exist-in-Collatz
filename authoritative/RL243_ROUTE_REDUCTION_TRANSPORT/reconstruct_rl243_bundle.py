#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib

HERE=Path(__file__).resolve().parent
parts=sorted(HERE.glob('RL243_Determinant2_Halfword_Counterflow_Reduction_2026-09-03.zip.b64.part*'))
assert parts, 'no transport parts found'
data=''.join(p.read_text().strip() for p in parts)
out=HERE/'RL243_Determinant2_Halfword_Counterflow_Reduction_2026-09-03.zip'
out.write_bytes(base64.b64decode(data))
sha=hashlib.sha256(out.read_bytes()).hexdigest()
want='4e7a85402d9af86ec7c0dc3282aafcec18acf97f9c8ca1402849e99cb7afa08f'
assert sha==want,(sha,want)
print(out.name,sha,'PASS')
