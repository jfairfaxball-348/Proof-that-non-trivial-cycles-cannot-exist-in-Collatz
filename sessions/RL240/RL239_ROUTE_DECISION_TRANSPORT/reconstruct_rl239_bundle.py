#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib

HERE=Path(__file__).resolve().parent
PARTS=['RL239_Radius4_Audit_Radius5_Viability_and_Route_Decision_2026-09-03.zip.b64.part01', 'RL239_Radius4_Audit_Radius5_Viability_and_Route_Decision_2026-09-03.zip.b64.part02', 'RL239_Radius4_Audit_Radius5_Viability_and_Route_Decision_2026-09-03.zip.b64.part03', 'RL239_Radius4_Audit_Radius5_Viability_and_Route_Decision_2026-09-03.zip.b64.part04']
OUT=HERE/'RL239_Radius4_Audit_Radius5_Viability_and_Route_Decision_2026-09-03.zip'
EXPECTED='28fd81440e44ac888f21e25da9cdad8fef5e5603aea9c8036c9084c27828893f'

data=''
for name in PARTS:
    data += ''.join((HERE/name).read_text(encoding='utf-8').split())
raw=base64.b64decode(data, validate=True)
got=hashlib.sha256(raw).hexdigest()
if got != EXPECTED:
    raise SystemExit(f'ZIP SHA256 mismatch: {got} != {EXPECTED}')
OUT.write_bytes(raw)
print(f'PASS reconstructed {OUT.name} SHA256 {got}')
