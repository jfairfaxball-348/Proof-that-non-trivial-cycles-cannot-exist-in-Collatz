#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
HERE=Path(__file__).resolve().parent
EXPECTED="58c1f11070ce10645ed76d72e79128f8401a96e5e31d2ee1a4813ed313f18bcd"
ZIP_NAME="RL149_Shell_Depth_Independence_Barrier_2026-08-28.zip"
for line in (HERE/'PART_SHA256SUMS.txt').read_text().splitlines():
  want,name=line.split('  ',1)
  assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==want
raw=base64.b64decode(''.join(p.read_text().strip() for p in sorted(HERE.glob('RL149_bundle.zip.b64.part*'))))
assert hashlib.sha256(raw).hexdigest()==EXPECTED
(HERE/ZIP_NAME).write_bytes(raw)
print('RL149 transport reconstruction: PASS')
