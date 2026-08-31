#!/usr/bin/env python3
from pathlib import Path
import hashlib, zipfile

STEM = "RL199_H21_Oriented_Lift_Index_and_Terminal_Defect_2026-08-31"
HERE = Path(__file__).resolve().parent
FILES = ['RL199_CERTIFIED_FACTS_AND_PROOF_LEDGER.md', 'RL199_CORRECTION_DEMOTION_LEDGER.md', 'RL199_FRESH_UNPACK_REVIEW.md', 'RL199_FRESH_UNPACK_VERIFICATION_2026-08-31.txt', 'RL199_H21_ORIENTED_LIFT_INDEX_AND_TERMINAL_DEFECT_2026-08-31.md', 'RL199_PROVENANCE.md', 'RL199_RED_TEAM_REPORT_2026-08-31.md', 'RL199_SESSION_STATE_AND_RL200_KICKOFF_2026-08-31.md', 'RL200_H21_ORIENTED_LIFT_GLOBAL_SELECTOR_TARGET.md', 'SHA256SUMS.txt', 'START_HERE.md', 'proofs/RL199_H21_ORIENTED_LIFT_INDEX.md', 'verification/run_fast_rl199_verifiers.sh', 'verification/verify_rl199_h21_oriented_lift.py']
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
