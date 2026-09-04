#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib, json, lzma
r=Path(__file__).resolve().parent
m=json.loads((r/'TRANSPORT_MANIFEST.json').read_text())
s=''.join((r[p['name']]).read_text() for p in m['parts'])
xz=base64.b64decode(s)
assert hashlib.sha256(xz).hexdigest()==m['xz_sha256']
z=lzma.decompress(xz)
assert hashlib.sha256(z).hexdigest()==m['canonical_zip_sha256']
(r/m['canonical_zip_name']).write_bytes(z)
print('PASS',m['canonical_zip_name'],m['canonical_zip_sha256'])
