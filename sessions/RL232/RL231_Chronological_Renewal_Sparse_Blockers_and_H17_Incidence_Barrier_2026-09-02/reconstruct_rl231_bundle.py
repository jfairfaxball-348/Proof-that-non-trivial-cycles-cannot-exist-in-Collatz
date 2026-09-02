#!/usr/bin/env python3
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/(ROOT.name+".zip")
EXCLUDE={OUT.name}

def files():
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and p.name not in EXCLUDE:
            yield p

with zipfile.ZipFile(OUT,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files():
        rel=p.relative_to(ROOT).as_posix()
        data=p.read_bytes()
        zi=zipfile.ZipInfo(rel,date_time=(2026,9,2,0,0,0))
        zi.compress_type=zipfile.ZIP_DEFLATED
        zi.external_attr=(0o100644 & 0xFFFF)<<16
        z.writestr(zi,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(OUT)
