#!/usr/bin/env python3
"""Fast structural verifier for the RL114 algebraic barrier; no theorem test."""
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "START_HERE.md",
    ROOT / "RL113_TO_RL114_OWNED_INVERSE_BARRIER.md",
    ROOT / "RL114_RL115_FOURIER_DISCREPANCY_TARGET.md",
    ROOT / "audit" / "ROUTE_LEDGER.md",
]
for path in required:
    assert path.is_file(), path

report = required[1].read_text(encoding="utf-8")
target = required[2].read_text(encoding="utf-8")
ledger = required[3].read_text(encoding="utf-8")
for token in ("method barrier", "RL20", "RL79", "RL81", "Primitivity", "Raw/Farey"):
    assert token in report, token
for token in ("finite character group", "RL20", "RL79", "unbounded modulus"):
    assert token in target, token
assert "Dyadic–triadic Fourier discrepancy" in ledger
assert "no inverse theorem" in ledger

def q(word):
    value = 0
    for index, bit in enumerate(word):
        if bit == "1":
            value = 3 * value + (1 << index)
    return value

for p in range(0, 5):
    for r in range(0, 5):
        for a_bits in product("01", repeat=p):
            for b_bits in product("01", repeat=r):
                a, b = "".join(a_bits), "".join(b_bits)
                m, n = a.count("1"), b.count("1")
                d = (1 << (p + r)) - 3 ** (m + n)
                assert q(a + b) == 3 ** n * q(a) + (1 << p) * q(b)
                assert (1 << p) * q(b + a) == 3 ** m * q(a + b) + d * q(a)

RL20_WORD = (
    "110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
    "110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
    "1101101101011010"
)
d20 = (1 << len(RL20_WORD)) - 3 ** RL20_WORD.count("1")
assert q(RL20_WORD) % d20 == 322171738410077807581692882247758374512983113782519312

print("RL114 rotation-ownership algebra and red-team structure: PASS")
print("finite concatenation identities checked for component lengths 0..4")
print("RL20 retains nonzero ordinary numerator residue")
