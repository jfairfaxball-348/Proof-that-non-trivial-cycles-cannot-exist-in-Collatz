#!/usr/bin/env python3
from pathlib import Path
import base64,hashlib
HERE=Path(__file__).resolve().parent
EXPECTED='22046930fb34752399c3ffe847b8d955e302c0c5cf29b5359424a090d227f4dc'
ZIP='RL150_Multi_Excursion_Local_Independence_Barrier_2026-08-28.zip'
for line in (HERE/'PART_SHA256SUMS.txt').read_text().splitlines():
 want,name=line.split('  ',1); assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==want
raw=base64.b64decode(''.join(p.read_text().strip() for p in sorted(HERE.glob('RL150_bundle.zip.b64.part*'))))
assert hashlib.sha256(raw).hexdigest()==EXPECTED
(HERE/ZIP).write_bytes(raw)
print('RL150 transport reconstruction: PASS')
