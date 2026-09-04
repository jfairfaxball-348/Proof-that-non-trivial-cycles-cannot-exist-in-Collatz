#!/usr/bin/env python3
from pathlib import Path
import base64,lzma,hashlib
root=Path(__file__).resolve().parent
parts=sorted(root.glob("RL247_Radius3_Radius4_Scope_Audit_2026-09-04.zip.xz.b64.part*"))
data="".join(p.read_text().strip() for p in parts)
out=root/"RL247_Radius3_Radius4_Scope_Audit_2026-09-04.zip"
out.write_bytes(lzma.decompress(base64.b64decode(data)))
h=hashlib.sha256(out.read_bytes()).hexdigest()
assert h=="0f7e750190ea1f32854887ac44627d3238114919597535450331fc3c143237cf", h
print(out.name, h)
