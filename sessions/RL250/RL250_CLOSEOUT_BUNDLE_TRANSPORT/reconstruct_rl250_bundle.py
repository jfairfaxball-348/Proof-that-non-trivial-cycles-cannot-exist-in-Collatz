#!/usr/bin/env python3
from pathlib import Path
import base64, json, hashlib
root=Path(__file__).resolve().parent
m=json.loads((root/'TRANSPORT_MANIFEST.json').read_text())
data=''.join((root/p).read_text().strip() for p in m['parts'])
out=root/m['canonical_zip']
out.write_bytes(base64.b64decode(data))
h=hashlib.sha256(out.read_bytes()).hexdigest()
assert h==m['canonical_zip_sha256'], (h,m['canonical_zip_sha256'])
print(out.name,h)
