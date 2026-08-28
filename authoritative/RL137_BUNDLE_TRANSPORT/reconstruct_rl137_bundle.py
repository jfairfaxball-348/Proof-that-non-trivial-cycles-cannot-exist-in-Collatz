#!/usr/bin/env python3
import base64
import hashlib
import pathlib
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
PART = HERE / "RL137_bundle.zip.b64.part01"
OUT = HERE / "RL137_Nonnegative_Defect_Multiplicity_Independent_Ceiling_2026-08-28.zip"
EXPECTED_SIZE = 10007
EXPECTED_SHA256 = "89e68b123a66964e8009dd8f49bfe9ef3648cbe9354b89a5f5942082a9e0e046"
EXPECTED_PART_SHA256 = "ada876360c3a2371fa95f23b381e829911a84b1da3382e4d294a94ba4cf111ee"

data = PART.read_bytes()
assert hashlib.sha256(data).hexdigest() == EXPECTED_PART_SHA256
# The tracked transport is line-wrapped ASCII base64 on macOS. Hash the exact
# transport bytes above, then remove only ASCII whitespace before strict decode.
raw = base64.b64decode(b"".join(data.split()), validate=True)
assert len(raw) == EXPECTED_SIZE, len(raw)
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
OUT.write_bytes(raw)
with zipfile.ZipFile(OUT) as zf:
    assert zf.testzip() is None
print("RL137 bundle reconstruction: PASS")
print(f"bytes={len(raw)} sha256={EXPECTED_SHA256}")
