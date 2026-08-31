#!/usr/bin/env python3
from pathlib import Path
import hashlib, zipfile

STEM = "RL198_H21_Global_Height_Selector_and_Minimal_Prehistory_2026-08-31"
HERE = Path(__file__).resolve().parent
FILES = ['RL198_CERTIFIED_FACTS_AND_PROOF_LEDGER.md', 'RL198_CORRECTION_DEMOTION_LEDGER.md', 'RL198_FRESH_UNPACK_REVIEW.md', 'RL198_FRESH_UNPACK_VERIFICATION_2026-08-31.txt', 'RL198_H21_GLOBAL_HEIGHT_SELECTOR_AND_MINIMAL_PREHISTORY_2026-08-31.md', 'RL198_PROVENANCE.md', 'RL198_RED_TEAM_REPORT_2026-08-31.md', 'RL198_SESSION_STATE_AND_RL199_KICKOFF_2026-08-31.md', 'RL199_H21_MINIMAL_PREHISTORY_AND_TERMINAL_SIGN_TARGET.md', 'SHA256SUMS.txt', 'START_HERE.md', 'proofs/RL198_H21_GLOBAL_HEIGHT_SELECTOR.md', 'verification/run_fast_rl198_verifiers.sh', 'verification/verify_rl198_h21_global_height_selector.py']
OUT = HERE / (STEM + ".zip")

with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for rel in FILES:
        data = (HERE / rel).read_bytes()
        info = zipfile.ZipInfo(STEM + "/" + rel, date_time=(1980,1,1,0,0,0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = (0o100644 << 16)
        zf.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

got = hashlib.sha256(OUT.read_bytes()).hexdigest()
expected = (HERE / (STEM + ".zip.sha256")).read_text(encoding="utf-8").split()[0]
if got != expected:
    raise SystemExit(f"SHA256 mismatch: {got} != {expected}")
print(f"PASS reconstructed {OUT.name} {got}")
