#!/usr/bin/env python3
from pathlib import Path
import zipfile

root=Path(__file__).resolve().parent
out=root.parent/"RL232_H17_Cross_Family_State_Barriers_and_Owned_Long_Return_Pivot_2026-09-02.zip"
files=sorted(p for p in root.rglob("*") if p.is_file())
with zipfile.ZipFile(out,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        rel=p.relative_to(root).as_posix()
        zi=zipfile.ZipInfo("RL232_H17_Cross_Family_State_Barriers_and_Owned_Long_Return_Pivot_2026-09-02/"+rel,date_time=(1980,1,1,0,0,0))
        zi.compress_type=zipfile.ZIP_DEFLATED
        zi.external_attr=(0o100644 & 0xFFFF)<<16
        z.writestr(zi,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(out)
