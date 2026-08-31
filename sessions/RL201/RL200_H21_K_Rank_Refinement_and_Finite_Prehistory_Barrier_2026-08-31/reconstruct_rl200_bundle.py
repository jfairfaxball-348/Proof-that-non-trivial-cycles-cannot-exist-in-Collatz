#!/usr/bin/env python3
from pathlib import Path
import hashlib, zipfile

STEM = "RL200_H21_K_Rank_Refinement_and_Finite_Prehistory_Barrier_2026-08-31"
HERE = Path(__file__).resolve().parent
FILES = ['RL200_CERTIFIED_FACTS_AND_PROOF_LEDGER.md', 'RL200_CORRECTION_DEMOTION_LEDGER.md', 'RL200_FRESH_UNPACK_REVIEW.md', 'RL200_FRESH_UNPACK_VERIFICATION_2026-08-31.txt', 'RL200_H21_K_RANK_REFINEMENT_AND_FINITE_PREHISTORY_BARRIER_2026-08-31.md', 'RL200_PROVENANCE.md', 'RL200_RED_TEAM_REPORT_2026-08-31.md', 'RL200_SESSION_STATE_AND_RL201_KICKOFF_2026-08-31.md', 'RL201_H21_ORIENTED_ENDPOINT_RANK_MOMENT_TARGET.md', 'START_HERE.md', 'proofs/RL200_H21_K_RANK_AND_PREHISTORY.md', 'verification/run_fast_rl200_verifiers.sh', 'verification/verify_rl200_h21_k_rank_and_prehistory.py', 'SHA256SUMS.txt']
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
