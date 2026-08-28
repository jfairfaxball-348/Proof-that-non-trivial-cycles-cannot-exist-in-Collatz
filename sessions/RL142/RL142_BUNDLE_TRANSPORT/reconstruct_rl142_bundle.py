#!/usr/bin/env python3
import base64, hashlib, pathlib, zipfile
h=pathlib.Path(__file__).resolve().parent
p=h/'RL142_bundle.zip.b64.part01'; o=h/'RL142_Cyclic_Contact_Interface_Obstruction_2026-08-28.zip'; d=p.read_bytes()
assert hashlib.sha256(d).hexdigest()=='b9300d26cacb83e56a5dc717c24deb6e377c18a4ddfc631f3cccb0a42f952cf0'
r=base64.b64decode(b''.join(d.split()),validate=True)
assert len(r)==7760 and hashlib.sha256(r).hexdigest()=='9537b9b2e8c34b8211e4160643693e7975dc0cb260ffcc4a11834e6d525d8e1b'
o.write_bytes(r)
with zipfile.ZipFile(o) as z: assert z.testzip() is None
print('RL142 bundle reconstruction: PASS')
