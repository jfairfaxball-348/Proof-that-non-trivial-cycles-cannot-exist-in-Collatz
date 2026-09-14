#!/usr/bin/env python3
"""Portable RL318 -> RL319 handover marker verifier."""

from pathlib import Path


root = Path(__file__).resolve().parents[1]
required = {
    "RL318_CLOSEOUT.md": [
        "Status: CLOSED AND FROZEN",
        "physical even / shadow odd",
        "0<delta<2S+h",
    ],
    "RL318_PROOF_LEDGER.md": [
        "RL318",
        "physical",
        "0<delta",
    ],
    "RL318_SESSION_STATE_AND_RL319_KICKOFF.md": [
        "CLOSED AND FROZEN",
        "RL319",
    ],
    "RL319_FIRST_REVERSE_MISMATCH_CROSSING_TARGET.md": [
        "Status: PREPARED, NOT STARTED",
        "crossing",
    ],
    "RL318_RED_TEAM_REPORT.md": [
        "MECHANICAL EXTRACTION ONLY; NO MATHEMATICAL CHANGE",
        "RL79 remains binding",
        "RL263--RL264 remain binding",
        "Gate A remains open",
    ],
}

for name, needles in required.items():
    path = root / name
    if not path.is_file() and "sessions/RL318" in root.as_posix():
        path = Path(__file__).resolve().parents[3] / "authoritative" / name
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"missing required marker {needle!r} in {name}")

print("RL318->RL319 portable handover verifier: PASS")
print("RL318 red-team extraction: PASS")
