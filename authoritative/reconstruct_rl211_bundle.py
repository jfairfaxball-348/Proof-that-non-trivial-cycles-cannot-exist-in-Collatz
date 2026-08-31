#!/usr/bin/env python3
import hashlib
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT=Path(__file__).resolve().parent
PKG="RL211_Absolute_E4_Eta_Selector_and_Denominator_Barrier_2026-08-31"
MANIFEST=ROOT/"SHA256SUMS.txt"
OUT=ROOT/f"{PKG}.zip"
SIDECAR=ROOT/f"{PKG}.zip.sha256"

lines=[line.strip() for line in MANIFEST.read_text().splitlines() if line.strip()]
payload=[]
for line in lines:
    digest, rel=line.split("  ",1)
    data=(ROOT/rel).read_bytes()
    assert hashlib.sha256(data).hexdigest()==digest
    payload.append(rel)

names=sorted(payload+["SHA256SUMS.txt"])
with ZipFile(OUT,"w",compression=ZIP_DEFLATED,compresslevel=9) as zf:
    for rel in names:
        zi=ZipInfo(f"{PKG}/{rel}",date_time=(2026,8,31,0,0,0))
        zi.compress_type=ZIP_DEFLATED
        zi.external_attr=(0o644 & 0xFFFF)<<16
        zf.writestr(zi,(ROOT/rel).read_bytes())

expected=SIDECAR.read_text().split()[0]
actual=hashlib.sha256(OUT.read_bytes()).hexdigest()
assert actual==expected
print(f"PASS reconstructed {OUT.name} sha256={actual}")
