#!/usr/bin/env python3
from pathlib import Path
import zipfile
HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'RL224_Candidate_Coupled_Height_Closure_and_E16_Rank_Deletion_2026-09-01.zip'
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(HERE.rglob('*')):
        if not p.is_file(): continue
        zi=zipfile.ZipInfo(str(Path(HERE.name)/p.relative_to(HERE)),date_time=(2026,9,1,0,0,0))
        zi.compress_type=zipfile.ZIP_DEFLATED; zi.external_attr=0o100644<<16
        z.writestr(zi,p.read_bytes())
print(OUT)
