#!/usr/bin/env python3
from base64 import b64decode
from hashlib import sha256
from pathlib import Path
HERE=Path(__file__).resolve().parent
NAME="RL158_Dense_Resultant_Character_Ambiguity_and_Distinguished_Root_2026-08-28.zip"
EXPECTED="6d2990826727f56a38d24d794001d929c01cbc4b1d88c16b8d0c96df04e17e1b"
raw=b64decode((HERE/'RL158_bundle.zip.b64.part01').read_bytes())
assert sha256(raw).hexdigest()==EXPECTED
(HERE/NAME).write_bytes(raw)
print('RL158 transport reconstruction: PASS')
