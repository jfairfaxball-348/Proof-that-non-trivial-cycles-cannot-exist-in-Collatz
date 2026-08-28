#!/usr/bin/env python3
import base64,hashlib,pathlib,zipfile
h=pathlib.Path(__file__).resolve().parent;p=h/'RL139_bundle.zip.b64.part01';o=h/'RL139_Compressed_Defect_Full_Ownership_Obstruction_2026-08-28.zip';d=p.read_bytes()
assert hashlib.sha256(d).hexdigest()=='7c75707f793f40f8fec48c953ff0b91df93a779f54d90e6fb259228d032136d9'
r=base64.b64decode(b''.join(d.split()),validate=True);assert len(r)==6717 and hashlib.sha256(r).hexdigest()=='39205cf0822c3ac0e924551ec3cf1e43e47aa0e5503c6d5916458d267600b25a';o.write_bytes(r)
with zipfile.ZipFile(o) as z: assert z.testzip() is None
print('RL139 bundle reconstruction: PASS')
