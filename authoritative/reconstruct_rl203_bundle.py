#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
here=Path(__file__).resolve().parent
transport=here/'RL203_H21_Dyadic_Prefix_Information_Boundary_2026-08-31_BUNDLE_TRANSPORT'
parts=sorted(transport.glob('*.zip.b64.part*'))
if not parts:
    raise SystemExit('no transport parts')
raw=base64.b64decode(''.join(p.read_text() for p in parts))
out=here/'RL203_H21_Dyadic_Prefix_Information_Boundary_2026-08-31.zip'
out.write_bytes(raw)
print(hashlib.sha256(raw).hexdigest(), out.name)
