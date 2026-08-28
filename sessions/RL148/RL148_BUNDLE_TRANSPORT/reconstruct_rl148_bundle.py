#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
HERE=Path(__file__).resolve().parent
EXPECTED="8bb803d99cb7f2ccf5bf972888fa42811485b4a6926308caacef1d7d8e8cd6a9"
ZIP_NAME="RL148_Exact_Depth_Negative_Defect_Fibre_Sharpening_2026-08-28.zip"
for line in (HERE/"PART_SHA256SUMS.txt").read_text().splitlines():
    want,name=line.split("  ",1)
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==want
raw=base64.b64decode("".join(p.read_text().strip() for p in sorted(HERE.glob("RL148_bundle.zip.b64.part*"))))
assert hashlib.sha256(raw).hexdigest()==EXPECTED
(HERE/ZIP_NAME).write_bytes(raw)
print("RL148 transport reconstruction: PASS")
