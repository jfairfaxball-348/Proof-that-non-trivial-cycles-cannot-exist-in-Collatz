from pathlib import Path
import base64, hashlib

HERE = Path(__file__).resolve().parent
EXPECTED_ZIP = "fac71c9943f485217406d6dc210c5d6a9983fb66c75d8f71806233b6655e5518"
parts = sorted(HERE.glob("RL145_bundle.zip.b64.part*"))
if not parts:
    raise SystemExit("no RL145 bundle parts found")
raw = b"".join(p.read_bytes() for p in parts)
data = base64.b64decode(raw, validate=True)
out = HERE / "RL145_bundle.zip"
out.write_bytes(data)
got = hashlib.sha256(data).hexdigest()
if got != EXPECTED_ZIP:
    raise SystemExit(f"ZIP SHA mismatch: {got} != {EXPECTED_ZIP}")
print("RL145 bundle transport reconstruction: PASS")
print("zip_sha256 =", EXPECTED_ZIP)
