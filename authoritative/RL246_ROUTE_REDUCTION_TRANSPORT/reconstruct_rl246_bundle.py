#!/usr/bin/env python3
from pathlib import Path
import base64, lzma, hashlib
root=Path(__file__).resolve().parent
parts=sorted(root.glob('RL246_Absolute_State_Full_Phase_Valley_Coupling_2026-09-04.zip.xz.b64.part*'))
raw=b''.join(p.read_bytes() for p in parts)
xz=base64.b64decode(raw)
zip_bytes=lzma.decompress(xz)
out=root/'RL246_Absolute_State_Full_Phase_Valley_Coupling_2026-09-04.zip'
out.write_bytes(zip_bytes)
print(hashlib.sha256(zip_bytes).hexdigest(), out.name)
