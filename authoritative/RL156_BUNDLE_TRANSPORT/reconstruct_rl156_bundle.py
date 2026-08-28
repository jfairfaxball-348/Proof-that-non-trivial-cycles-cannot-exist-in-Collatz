#!/usr/bin/env python3
"""Losslessly reconstruct the RL156 bundle from its committed base64 part."""

from base64 import b64decode
from hashlib import sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME = "RL156_Bezout_State_Notation_Repair_2026-08-28.zip"
EXPECTED = "1f07b1cd426c694a245ce7a2f9a662bfbe8d66364bba5da072544a802d75d693"
part = HERE / "RL156_bundle.zip.b64.part01"
raw = b64decode(part.read_bytes())
out = HERE / NAME
out.write_bytes(raw)
actual = sha256(raw).hexdigest()
assert actual == EXPECTED, (actual, EXPECTED)
print("RL156 transport reconstruction: PASS")
