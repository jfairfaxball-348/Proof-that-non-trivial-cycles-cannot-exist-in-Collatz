#!/usr/bin/env python3
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "RL222_Full_Period_Quotient_Residue_Structural_Blindness_2026-09-01.zip"
ROOT = HERE.name
with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for p in sorted(HERE.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(HERE)
        data = p.read_bytes()
        zi = zipfile.ZipInfo(str(Path(ROOT) / rel), date_time=(2026,9,1,0,0,0))
        zi.compress_type = zipfile.ZIP_DEFLATED
        zi.external_attr = 0o100644 << 16
        zf.writestr(zi, data)
print(OUT)
