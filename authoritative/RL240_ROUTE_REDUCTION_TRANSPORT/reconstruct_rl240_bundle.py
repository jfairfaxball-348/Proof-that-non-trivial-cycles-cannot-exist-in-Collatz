#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
HERE=Path(__file__).resolve().parent
parts=['RL240_Radius4_Global_Bridge_Selected_Counterflow_Reduction_2026-09-03.zip.b64.part01','RL240_Radius4_Global_Bridge_Selected_Counterflow_Reduction_2026-09-03.zip.b64.part02','RL240_Radius4_Global_Bridge_Selected_Counterflow_Reduction_2026-09-03.zip.b64.part03','RL240_Radius4_Global_Bridge_Selected_Counterflow_Reduction_2026-09-03.zip.b64.part04']
data=''.join((HERE/p).read_text().strip() for p in parts)
out=HERE/'RL240_Radius4_Global_Bridge_Selected_Counterflow_Reduction_2026-09-03.zip'
out.write_bytes(base64.b64decode(data))
h=hashlib.sha256(out.read_bytes()).hexdigest()
expected='eba20702838128f09f0afec763103b58c9b7a2f1f37cf6f7dcc60d253b691ae9'
assert h==expected,(h,expected)
print(out.name,h)
