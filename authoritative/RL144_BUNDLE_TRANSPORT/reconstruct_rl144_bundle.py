#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, zipfile, io
HERE=Path(__file__).resolve().parent
EXPECTED_ZIP="7786053a7c2b96acfed18a96e409210402d85bf7927be1e6e938dbbc35f6f8df"
parts=sorted(HERE.glob("RL144_bundle.zip.b64.part??"))
assert len(parts)==9
expected={}
for line in (HERE/"PART_SHA256SUMS.txt").read_text().splitlines():
    h,name=line.split(None,1); expected[name.strip()]=h
for p in parts:
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected[p.name]
text=b"".join(p.read_bytes() for p in parts)
data=base64.b64decode(text)
assert hashlib.sha256(data).hexdigest()==EXPECTED_ZIP
out=HERE.parent/"RL144_RL143_Run_Fibre_Population_Repair_2026-08-28.zip"
out.write_bytes(data)
with zipfile.ZipFile(io.BytesIO(data)) as z:
    assert z.testzip() is None
print("RL144 transport reconstruction: PASS")
print("zip_sha256 =", EXPECTED_ZIP)
