#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, zipfile
HERE=Path(__file__).resolve().parent
NAME="RL154_Bidirectional_Singleton_Transfer_and_Terminal_Height_Barrier_2026-08-28.zip"
EXPECTED="a613305213b343c758e30869df8ab79e4f9c27b4413c598c9b3ea389ecda13ee"
for line in (HERE/"PART_SHA256SUMS.txt").read_text().splitlines():
    want,name=line.split("  ",1)
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==want
raw=base64.b64decode("".join(p.read_text().strip() for p in sorted(HERE.glob("RL154_bundle.zip.b64.part*"))))
assert hashlib.sha256(raw).hexdigest()==EXPECTED
(HERE/NAME).write_bytes(raw)
with zipfile.ZipFile(HERE/NAME) as zf: assert zf.testzip() is None
print("RL154 transport reconstruction: PASS")
