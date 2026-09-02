#!/usr/bin/env python3
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/"RL237_Coupled_H20_Recurrence_Charge_Saturation_and_H21_Returnability_2026-09-02.zip"
files=sorted(p for p in ROOT.rglob("*") if p.is_file())
with zipfile.ZipFile(OUT,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        rel=p.relative_to(ROOT.parent).as_posix()
        info=zipfile.ZipInfo(rel,(2026,9,2,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        info.external_attr=(0o100644<<16)
        z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(OUT)
