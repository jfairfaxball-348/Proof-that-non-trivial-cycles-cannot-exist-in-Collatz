#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, sys, zipfile

EXPECTED_NAME = 'RL134_Multiplicity_Determinant_Strip_and_Physical_Windows_2026-08-27.zip'
EXPECTED_SIZE = 16940
EXPECTED_SHA256 = '6ff26609ee5414dc7a2434b6bb3b7993577936894eb7c392395edf36ab6b21ec'

here = Path(__file__).resolve().parent
parts = sorted(here.glob('RL134_bundle.zip.b64.part*'))
if len(parts) != 8:
    raise SystemExit(f'expected 8 transport parts, found {len(parts)}')
encoded = ''.join(p.read_text(encoding='ascii').strip() for p in parts)
try:
    data = base64.b64decode(encoded, validate=True)
except Exception as exc:
    raise SystemExit(f'base64 decode failed: {exc}')
actual_sha = hashlib.sha256(data).hexdigest()
if len(data) != EXPECTED_SIZE:
    raise SystemExit(f'size mismatch: {len(data)} != {EXPECTED_SIZE}')
if actual_sha != EXPECTED_SHA256:
    raise SystemExit(f'sha256 mismatch: {actual_sha} != {EXPECTED_SHA256}')
out = here / EXPECTED_NAME
out.write_bytes(data)
with zipfile.ZipFile(out, 'r') as zf:
    bad = zf.testzip()
    if bad is not None:
        raise SystemExit(f'zip member CRC failure: {bad}')
print(f'RL134 transport reconstruction: PASS')
print(f'file={out.name}')
print(f'size={len(data)}')
print(f'sha256={actual_sha}')
