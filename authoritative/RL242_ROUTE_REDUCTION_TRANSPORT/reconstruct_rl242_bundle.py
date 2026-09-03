#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
HERE=Path(__file__).resolve().parent
parts=sorted(HERE.glob("RL242_Radius4_Bridge_Zero_Carry_and_Low_Counterflow_Reduction_2026-09-03.zip.b64.part*"))
raw=base64.b64decode("".join(p.read_text().strip() for p in parts))
out=HERE.parent/"RL242_Radius4_Bridge_Zero_Carry_and_Low_Counterflow_Reduction_2026-09-03.zip"
out.write_bytes(raw)
print(out)
print(hashlib.sha256(raw).hexdigest())
