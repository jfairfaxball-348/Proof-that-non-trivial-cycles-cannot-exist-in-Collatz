#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib

HERE = Path(__file__).resolve().parent
EXPECTED = "3df4589e3593e511b9557d09fea501af75ab919fe5a50486cd06abe34c3fc058"
ZIP_NAME = "RL147_Layered_Carry_Obstruction_and_Negative_Defect_Pivot_2026-08-28.zip"

for line in (HERE / "PART_SHA256SUMS.txt").read_text().splitlines():
    if not line.strip():
        continue
    want, name = line.split("  ", 1)
    got = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
    assert got == want, (name, want, got)

parts = sorted(HERE.glob("RL147_bundle.zip.b64.part*"))
raw = base64.b64decode("".join(part.read_text().strip() for part in parts))
got = hashlib.sha256(raw).hexdigest()
assert got == EXPECTED, (EXPECTED, got)
out = HERE / ZIP_NAME
out.write_bytes(raw)
print("RL147 transport reconstruction: PASS")
print("zip =", out)
print("sha256 =", got)
