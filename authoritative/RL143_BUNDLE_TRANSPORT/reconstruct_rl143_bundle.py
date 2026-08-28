#!/usr/bin/env python3
import base64,hashlib,pathlib,zipfile
h=pathlib.Path(__file__).resolve().parent;p=h/'RL143_bundle.zip.b64.part01';o=h/'RL143_Height_One_Run_Fibre_Exclusion_2026-08-28.zip';d=p.read_bytes()
assert hashlib.sha256(d).hexdigest()=='86c307c6d1c23d38daa0ce40840e4f08905e1bce8295eba47ac79835cfbdd7fd'
r=base64.b64decode(b''.join(d.split()),validate=True);assert len(r)==5436 and hashlib.sha256(r).hexdigest()=='d724e96083cc90dc194c9238b042a56270d93911f22cdf13953c2b46d7f293c7'
o.write_bytes(r)
with zipfile.ZipFile(o) as z:assert z.testzip() is None
print('RL143 bundle reconstruction: PASS')
