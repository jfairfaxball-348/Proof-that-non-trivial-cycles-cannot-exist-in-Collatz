#!/usr/bin/env python3
"""Reconstruct and verify the RL140 portable ZIP bundle."""

import base64
import hashlib
import pathlib
import zipfile


here = pathlib.Path(__file__).resolve().parent
part = here / 'RL140_bundle.zip.b64.part01'
output = here / 'RL140_One_Deviant_Block_Contact_Obstruction_2026-08-28.zip'
data = part.read_bytes()
assert hashlib.sha256(data).hexdigest() == (
    'a15e9c5746d1ed326259d4f1cf11b0fd733a166bf4afd214f6516f8277bf130d'
)
archive = base64.b64decode(b''.join(data.split()), validate=True)
assert len(archive) == 9622
assert hashlib.sha256(archive).hexdigest() == (
    '6c263ff700d1ef44cc5f411447bb9fe9a1e8bc4a58897ea178e3137966be41ab'
)
output.write_bytes(archive)
with zipfile.ZipFile(output) as handle:
    assert handle.testzip() is None
print('RL140 bundle reconstruction: PASS')
