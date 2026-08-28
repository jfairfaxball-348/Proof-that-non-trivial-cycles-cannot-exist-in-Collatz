#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
p=Path(__file__).resolve().parent
part=p/'RL159_bundle.zip.b64.part01'
out=p/'RL159_Joint_Distinguished_Root_SNF_and_Tautology_Barrier_2026-08-28.zip'
raw=base64.b64decode(part.read_text())
out.write_bytes(raw)
expected='a9e793f25998c6615e5a916d0666b0a8f049d8a33552eed6c26fb2b552c5cb83'
got=hashlib.sha256(raw).hexdigest()
assert got==expected,(got,expected)
print(got, out.name)
