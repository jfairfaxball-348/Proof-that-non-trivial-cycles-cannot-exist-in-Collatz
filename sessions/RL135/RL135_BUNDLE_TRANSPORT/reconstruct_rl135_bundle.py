#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, zipfile

HERE = Path(__file__).resolve().parent
OUT = HERE / 'RL135_Multiplicity_Defect_Lift_and_Mesoscopic_State_Ceilings_2026-08-27.zip'
EXPECTED_SIZE = 17429
EXPECTED_SHA256 = '12e7124e4167ae8422481b29829f8f908883eba9563ae35d2da2e8a0e9501c01'

checks = {}
for line in (HERE / 'PART_SHA256SUMS.txt').read_text().splitlines():
    h, name = line.split(None, 1)
    checks[name.strip()] = h

parts = sorted(HERE.glob('RL135_bundle.zip.b64.part*'))
assert parts, 'no bundle parts found'
for p in parts:
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    assert got == checks[p.name], f'part hash mismatch: {p.name}'

encoded = ''.join(p.read_text(encoding='ascii') for p in parts)
data = base64.b64decode(encoded, validate=True)
assert len(data) == EXPECTED_SIZE, (len(data), EXPECTED_SIZE)
assert hashlib.sha256(data).hexdigest() == EXPECTED_SHA256
OUT.write_bytes(data)
with zipfile.ZipFile(OUT) as zf:
    bad = zf.testzip()
    assert bad is None, f'ZIP CRC failure: {bad}'
print('RL135 bundle reconstruction: PASS')
print(f'bytes={len(data)}')
print(f'sha256={EXPECTED_SHA256}')
print(f'parts={len(parts)}')
