#!/usr/bin/env python3
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
out=root.parent/(root.name+".zip")
with zipfile.ZipFile(out,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        rel=p.relative_to(root).as_posix()
        info=zipfile.ZipInfo(root.name+"/"+rel,(1980,1,1,0,0,0))
        mode=0o755 if (p.stat().st_mode & 0o111) else 0o644
        info.external_attr=(mode & 0xFFFF)<<16
        info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(out)
