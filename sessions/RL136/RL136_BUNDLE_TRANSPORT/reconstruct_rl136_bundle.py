#!/usr/bin/env python3
import base64, hashlib, pathlib, zipfile

HERE = pathlib.Path(__file__).resolve().parent
PART = HERE / "RL136_bundle.zip.b64.part01"
OUT = HERE / "RL136_Owned_Defect_Excursion_Isolation_and_Triangular_Packing_2026-08-27.zip"
EXPECTED_SIZE = 18061
EXPECTED_SHA256 = "6da49c03461eae98825181b5f1741386dcb5bf210dc086295bf3e164c8001856"
EXPECTED_PART_SHA256 = "d32b49403f1fb55f7a142e470477046cd093836fef912bc01d5977b78e727822"

data = PART.read_bytes()
assert hashlib.sha256(data).hexdigest() == EXPECTED_PART_SHA256
raw = base64.b64decode(data, validate=True)
assert len(raw) == EXPECTED_SIZE, len(raw)
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
OUT.write_bytes(raw)
with zipfile.ZipFile(OUT) as zf:
    bad = zf.testzip()
    assert bad is None, bad
print("RL136 bundle reconstruction: PASS")
print(f"bytes={len(raw)} sha256={EXPECTED_SHA256}")
