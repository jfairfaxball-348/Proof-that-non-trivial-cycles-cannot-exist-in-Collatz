#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
root = Path(__file__).resolve().parent
parts = sorted(root.glob('RL267_Radius5_Kappa1_311_221_Closure_2026-09-06.zip.b64.part*'))
assert parts, 'no transport parts found'
b64 = b''.join(p.read_bytes() for p in parts)
out = root / 'RL267_Radius5_Kappa1_311_221_Closure_2026-09-06.zip'
out.write_bytes(base64.b64decode(b64, validate=True))
sha = hashlib.sha256(out.read_bytes()).hexdigest()
expected = '412a96aa16b58db5184a5e263a424668bc8bb453a1b9a2711ad8c09e95fca0d9'
assert sha == expected, (sha, expected)
print(f'PASS reconstructed {out.name} SHA256={sha}')
