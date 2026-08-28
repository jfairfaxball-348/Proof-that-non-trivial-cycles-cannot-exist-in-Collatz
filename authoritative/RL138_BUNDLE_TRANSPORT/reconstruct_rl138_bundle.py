#!/usr/bin/env python3
import base64, hashlib, pathlib, zipfile
HERE=pathlib.Path(__file__).resolve().parent
part=HERE/'RL138_bundle.zip.b64.part01'
out=HERE/'RL138_Terminal_Local_Defect_Barrier_2026-08-28.zip'
data=part.read_bytes()
assert hashlib.sha256(data).hexdigest()=='b4742b915575b173e14e089d7a8992e2fe4d622a4d711c6520996530db73c41a'
raw=base64.b64decode(b''.join(data.split()), validate=True)
assert len(raw)==7133
assert hashlib.sha256(raw).hexdigest()=='f58dae08bd0973f200b163b38c3538fcb8b69a52c59bb351a8646e49f23ff29e'
out.write_bytes(raw)
with zipfile.ZipFile(out) as z: assert z.testzip() is None
print('RL138 bundle reconstruction: PASS')
