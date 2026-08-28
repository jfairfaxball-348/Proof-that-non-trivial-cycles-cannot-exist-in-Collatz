#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, zipfile

HERE = Path(__file__).resolve().parent
EXPECTED = "6c3ff5b8a87a29ee0ae5c21176c3c51f087c09648680b5c68cb5f2c968215913"
ZIP_NAME = "RL152_Global_Depth_Budget_and_Reciprocal_Width_Bridge_2026-08-28.zip"

for line in (HERE/"PART_SHA256SUMS.txt").read_text().splitlines():
    want, name = line.split("  ", 1)
    got = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
    assert got == want, (name, got, want)

raw = base64.b64decode("".join(
    p.read_text().strip() for p in sorted(HERE.glob("RL152_bundle.zip.b64.part*"))
))
got = hashlib.sha256(raw).hexdigest()
assert got == EXPECTED, (got, EXPECTED)

out = HERE/ZIP_NAME
out.write_bytes(raw)
with zipfile.ZipFile(out) as zf:
    bad = zf.testzip()
    assert bad is None, bad

print("RL152 transport reconstruction: PASS")
print(f"zip_sha256={got}")
