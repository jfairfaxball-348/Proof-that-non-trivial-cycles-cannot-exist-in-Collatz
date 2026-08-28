#!/usr/bin/env python3
"""Reconstruct and verify the RL141 portable ZIP bundle."""

import base64
import hashlib
import pathlib
import zipfile


here = pathlib.Path(__file__).resolve().parent
part = here / 'RL141_bundle.zip.b64.part01'
output = here / 'RL141_Consecutive_Multiblock_Contact_Obstruction_2026-08-28.zip'
data = part.read_bytes()
assert hashlib.sha256(data).hexdigest() == (
    '509b2015ed7c3cca74e047c38feb76bc4d3fbcf6dd2b11788f5e61c478c3a451'
)
archive = base64.b64decode(b''.join(data.split()), validate=True)
assert len(archive) == 8956
assert hashlib.sha256(archive).hexdigest() == (
    '6ccdb711f609115f6b212f9e8aaa3d023345060b1210e9908c3facb6f447cff3'
)
output.write_bytes(archive)
with zipfile.ZipFile(output) as handle:
    assert handle.testzip() is None
print('RL141 bundle reconstruction: PASS')
