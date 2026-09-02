#!/usr/bin/env python3
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'RL235_Repaired_Sparse_Family_Charging_and_H20_185_Target_2026-09-02.zip'
files=sorted(p for p in ROOT.rglob('*') if p.is_file())
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        rel=Path(ROOT.name)/p.relative_to(ROOT)
        info=zipfile.ZipInfo(str(rel).replace('\\','/'),date_time=(1980,1,1,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=(0o100644<<16)
        z.writestr(info,p.read_bytes())
print(OUT)
