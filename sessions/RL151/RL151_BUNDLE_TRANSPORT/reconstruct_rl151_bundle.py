#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
here=Path(__file__).resolve().parent
parts=sorted(here.glob("RL151_bundle.zip.b64.part*"))
raw=base64.b64decode("".join(p.read_text().strip() for p in parts))
out=here/"RL151_Nonlocal_Successor_Mass_Ownership_Coupling_2026-08-28.zip"
out.write_bytes(raw)
print(hashlib.sha256(raw).hexdigest(), out.name)
