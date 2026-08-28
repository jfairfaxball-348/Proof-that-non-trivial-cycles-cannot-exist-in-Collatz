#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib

HERE=Path(__file__).resolve().parent
EXPECTED="bec5394a93979b5791958054acb37023f3d37d8fc52fd8969b02aab7b4ee726f"
ZIP_NAME="RL146_Contact_Carry_Order_Closure_2026-08-28.zip"

for line in (HERE/"PART_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    want,name=line.split("  ",1)
    data=(HERE/name).read_bytes()
    got=hashlib.sha256(data).hexdigest()
    assert got==want, (name,want,got)

parts=sorted(HERE.glob("RL146_bundle.zip.b64.part*"))
raw=base64.b64decode("".join(p.read_text().strip() for p in parts))
got=hashlib.sha256(raw).hexdigest()
assert got==EXPECTED, (EXPECTED,got)
out=HERE/ZIP_NAME
out.write_bytes(raw)
print("RL146 transport reconstruction: PASS")
print("zip =", out)
print("sha256 =", got)
