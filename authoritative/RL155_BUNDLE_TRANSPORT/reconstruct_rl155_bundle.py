#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, zipfile
HERE=Path(__file__).resolve().parent
NAME="RL155_Dense_Singleton_Phase_Remainder_2026-08-28.zip"
EXPECTED="92507023292e803583af4e3812d34a740971df89989c1416da945446c12ad424"
for line in (HERE/"PART_SHA256SUMS.txt").read_text().splitlines():
    want,name=line.split("  ",1)
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==want
raw=base64.b64decode("".join(p.read_text().strip() for p in sorted(HERE.glob("RL155_bundle.zip.b64.part*"))))
assert hashlib.sha256(raw).hexdigest()==EXPECTED
(HERE/NAME).write_bytes(raw)
with zipfile.ZipFile(HERE/NAME) as zf: assert zf.testzip() is None
print("RL155 transport reconstruction: PASS")
