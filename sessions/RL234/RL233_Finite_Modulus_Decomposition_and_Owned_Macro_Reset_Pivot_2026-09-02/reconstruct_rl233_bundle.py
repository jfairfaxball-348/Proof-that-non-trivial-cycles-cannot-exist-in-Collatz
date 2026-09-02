#!/usr/bin/env python3
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
out=root.parent/(root.name+'.zip')
with zipfile.ZipFile(out,'w') as z:
    for p in sorted(root.rglob('*')):
        if not p.is_file(): continue
        rel=p.relative_to(root)
        zi=zipfile.ZipInfo(str(Path(root.name)/rel), date_time=(2026,9,2,0,0,0))
        zi.compress_type=zipfile.ZIP_DEFLATED
        zi.create_system=3
        zi.external_attr=(0o100644 & 0xFFFF)<<16
        z.writestr(zi,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(out)
