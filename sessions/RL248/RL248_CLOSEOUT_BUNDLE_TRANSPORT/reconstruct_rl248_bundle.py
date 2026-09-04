#!/usr/bin/env python3
from pathlib import Path
import base64,lzma,hashlib,json
root=Path(__file__).resolve().parent
m=json.loads((root/'TRANSPORT_MANIFEST.json').read_text())
data=''.join((root/p).read_text().strip() for p in m['parts'])
raw=lzma.decompress(base64.b64decode(data))
h=hashlib.sha256(raw).hexdigest()
assert h==m['zip_sha256'], (h,m['zip_sha256'])
out=root/m['zip']
out.write_bytes(raw)
print('RL248 transport reconstruction: PASS')
print(h, out.name)
