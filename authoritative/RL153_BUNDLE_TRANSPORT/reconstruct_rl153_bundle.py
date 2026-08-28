#!/usr/bin/env python3
from pathlib import Path
import base64
import hashlib
import zipfile

HERE = Path(__file__).resolve().parent
ZIP_NAME = "RL153_Singleton_Owner_Factor_Collapse_2026-08-28.zip"
EXPECTED = "3e006696a97861cc2f095e83022602c302f952f9ed2f6e735ae5eee376be5b7e"

for line in (HERE / "PART_SHA256SUMS.txt").read_text().splitlines():
    want, name = line.split("  ", 1)
    got = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
    assert got == want, (name, got, want)

raw = base64.b64decode("".join(
    p.read_text().strip() for p in sorted(HERE.glob("RL153_bundle.zip.b64.part*"))
))
got = hashlib.sha256(raw).hexdigest()
assert got == EXPECTED, (got, EXPECTED)

out = HERE / ZIP_NAME
out.write_bytes(raw)
with zipfile.ZipFile(out) as zf:
    assert zf.testzip() is None

print("RL153 transport reconstruction: PASS")
print(f"zip_sha256={got}")
