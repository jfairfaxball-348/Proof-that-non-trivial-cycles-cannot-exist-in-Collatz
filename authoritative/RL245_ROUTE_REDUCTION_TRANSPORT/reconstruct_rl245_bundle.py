#!/usr/bin/env python3
from pathlib import Path
import base64,lzma,hashlib
root=Path(__file__).resolve().parent
parts=sorted(root.glob("RL245_Paired_Physical_Valley_Ownership_Repair_and_State_Coupling_2026-09-04.zip.xz.b64.part*"))
assert parts, "no transport parts"
data="".join(p.read_text(encoding="ascii").strip() for p in parts)
raw=lzma.decompress(base64.b64decode(data))
out=root/"RL245_Paired_Physical_Valley_Ownership_Repair_and_State_Coupling_2026-09-04.zip"
out.write_bytes(raw)
h=hashlib.sha256(raw).hexdigest()
assert h=="abd41536bf69ce3a12fa5a8ae5358bc6df3527ca8d1603b245c70e0f986de48e", (h,"abd41536bf69ce3a12fa5a8ae5358bc6df3527ca8d1603b245c70e0f986de48e")
print(out)
print("sha256=",h)
