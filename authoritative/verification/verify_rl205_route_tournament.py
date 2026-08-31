#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys

root = Path(__file__).resolve().parents[1]

required = {
    "RL205_GLOBAL_CLOSURE_ROUTE_TOURNAMENT_2026-08-31.md": [
        "16188727234",
        "0,8,9,17 mod18",
        "owned_quotient_sensitive_gate_b_residual",
        "new_mathematical_theorems=0",
        "new_rank_exclusions=0",
        "division by `D` exposes the owned physical integer layer",
    ],
    "RL205_CERTIFIED_FACTS_AND_PROOF_LEDGER.md": [
        "16,188,727,234",
        "no new mathematical",
        "Gate B globally remains open",
    ],
    "RL205_CORRECTION_DEMOTION_LEDGER.md": [
        "No inherited theorem",
        "RL206 may not assert a modulus divisibility",
        "H21 itself remains viable",
    ],
    "RL205_RED_TEAM_REPORT_2026-08-31.md": [
        "PASS for strategic closeout",
        "RL20 fake test",
        "Coboundary/proper-factor test",
        "Gate-B claim gate",
    ],
    "RL205_SESSION_STATE_AND_RL206_KICKOFF_2026-08-31.md": [
        "16,188,727,234",
        "RL206_DQ_SENSITIVE_OWNED_GATE_B_QUOTIENT_RESIDUAL_TARGET.md",
        "H21 independent-information completion is retained as first fallback",
    ],
    "RL206_DQ_SENSITIVE_OWNED_GATE_B_QUOTIENT_RESIDUAL_TARGET.md": [
        "R_m = Q_m / D",
        "RL79 rank-one",
        "0 < |W| < M",
        "RL207 to H21 independent-information completion",
    ],
    "START_HERE.md": [
        "RL206 incoming authoritative state",
        "16,188,727,234",
    ],
}

for name, needles in required.items():
    p = root / name
    if not p.is_file():
        raise SystemExit(f"FAIL missing {name}")
    text = p.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"FAIL {name}: missing invariant {needle!r}")

manifest = root / "SHA256SUMS.txt"
if not manifest.is_file():
    raise SystemExit("FAIL missing SHA256SUMS.txt")
for line in manifest.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    digest, rel = line.split("  ", 1)
    p = root / rel
    if not p.is_file():
        raise SystemExit(f"FAIL manifest missing file {rel}")
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != digest:
        raise SystemExit(f"FAIL sha256 {rel}: {got} != {digest}")

print("PASS RL205 route-tournament invariant certificate")
print("inherited_rank_count=16188727234")
print("new_mathematical_theorems=0")
print("new_rank_exclusions=0")
print("inherited_demotion=no")
print("primary_route=owned_quotient_sensitive_gate_b_residual")
print("h21_status=retained_viable_first_fallback")
print("gate_a_global=open")
print("gate_b_global=open")
print("successor=RL206")
