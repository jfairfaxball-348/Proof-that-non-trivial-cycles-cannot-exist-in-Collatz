#!/usr/bin/env python3
"""Losslessly reconstruct the RL157 bundle from its committed base64 part."""
from base64 import b64decode
from hashlib import sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME = "RL157_Phase_Normalization_Repair_and_Dense_Resultant_2026-08-28.zip"
EXPECTED = "04a5aed103d8287550f51f8ecdfdea4bd5bf18023e60c5488bb37348c785608d"
raw = b64decode((HERE / "RL157_bundle.zip.b64.part01").read_bytes())
assert sha256(raw).hexdigest() == EXPECTED
(HERE / NAME).write_bytes(raw)
print("RL157 transport reconstruction: PASS")
