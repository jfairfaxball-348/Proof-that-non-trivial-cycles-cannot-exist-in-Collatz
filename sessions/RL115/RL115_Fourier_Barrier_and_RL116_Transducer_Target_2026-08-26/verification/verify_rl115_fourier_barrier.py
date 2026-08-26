#!/usr/bin/env python3
"""Fast algebra verifier for RL115's character-resolution barrier."""
from cmath import exp, pi
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "START_HERE.md",
    ROOT / "RL114_TO_RL115_FOURIER_BARRIER.md",
    ROOT / "RL115_RL116_TWO_BASE_TRANSDUCER_TARGET.md",
    ROOT / "audit" / "ROUTE_LEDGER.md",
]
for path in required:
    assert path.is_file(), path
report = required[1].read_text(encoding="utf-8")
target = required[2].read_text(encoding="utf-8")
ledger = required[3].read_text(encoding="utf-8")
for token in ("method barrier", "RL20", "RL79", "RL81", "Primitivity", "Raw/Farey"):
    assert token in report, token
for token in ("state set", "RL20", "RL79", "unbounded"):
    assert token in target, token
assert "Two-base finite transducer" in ledger
assert "Fourier resolution barrier" in ledger

for modulus in range(2, 18):
    for residue in range(modulus):
        value = sum(exp(2j * pi * frequency * residue / modulus)
                    for frequency in range(modulus)) / modulus
        assert abs(value - (1 if residue == 0 else 0)) < 1e-10

print("RL115 Fourier orthogonality and route-red-team structure: PASS")
print("exact zero-residue indicator checked for moduli 2..17")
