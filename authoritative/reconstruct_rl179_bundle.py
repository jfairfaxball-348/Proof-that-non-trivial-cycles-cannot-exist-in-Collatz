#!/usr/bin/env python3
from pathlib import Path
import base64
root=Path(__file__).resolve().parent
parts=sorted(root.glob('RL179_bundle.zip.b64.part*'))
if not parts:
    raise SystemExit('FAIL: no RL179 base64 parts found')
data=''.join(p.read_text().strip() for p in parts)
out=root/'RL179_V37_Budget_Multi_Support_and_Odd_Part_Sieve_2026-08-29.zip'
out.write_bytes(base64.b64decode(data,validate=True))
print(out.name)
