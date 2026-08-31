#!/usr/bin/env python3
from pathlib import Path, PurePosixPath
import hashlib, zipfile
HERE=Path(__file__).resolve().parent
STEM='RL201_H21_Absolute_Endpoint_Moment_and_Coupled_Prehistory_2026-08-31'
records=[]
for line in (HERE/'SHA256SUMS.txt').read_text().splitlines():
    expected,name=line.split(maxsplit=1)
    path=PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected
    records.append(name)
assert len(records)==len(set(records))
names=sorted(records+['SHA256SUMS.txt'])
out=HERE/(STEM+'.zip')
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name in names:
        info=zipfile.ZipInfo(STEM+'/'+name,date_time=(1980,1,1,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED; info.create_system=3
        info.external_attr=(0o100644<<16)
        z.writestr(info,(HERE/name).read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
expected=(HERE/(STEM+'.zip.sha256')).read_text().split()[0]
assert hashlib.sha256(out.read_bytes()).hexdigest()==expected
print('PASS deterministic RL201 bundle reconstruction '+expected)
