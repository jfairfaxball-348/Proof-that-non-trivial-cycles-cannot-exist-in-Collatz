#!/usr/bin/env python3
"""RL113 structural and finite red-team verifier; no theorem judgement."""
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "START_HERE.md",
    ROOT / "RL112_TO_RL113_TOURNAMENT_AND_AUDIT.md",
    ROOT / "RL113_RL114_OWNED_SUPPORT_INVERSE_TARGET.md",
    ROOT / "audit" / "TOURNAMENT_LEDGER.md",
    ROOT / "audit" / "ROUTE_CARDS.md",
]
for path in required:
    assert path.is_file(), path

report = required[1].read_text(encoding="utf-8")
cards = required[4].read_text(encoding="utf-8")
target = required[2].read_text(encoding="utf-8")
for token in ("RL20", "RL79", "RL81", "primitivity", "Raw/Farey", "route 2"):
    assert token in report or token in cards or token in target, token
for attack in (
    "Owned inverse", "Fourier discrepancy", "Finite transducer", "S-unit legality",
    "Modular expander", "p-adic transfer", "Entropy rigidity", "Geometry transference",
    "`+1` cocycle", "Symbolic specification", "Mahler/automatic", "CEGIS strip",
):
    assert attack in cards, attack
assert "Winner" in report and "owned-support inverse" in report.lower()
assert "New analytic theorem: **none**" in report

RL20_WORD = (
    "110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
    "110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
    "1101101101011010"
)
RL20_REMAINDER = 322171738410077807581692882247758374512983113782519312

def q1(word):
    value = 0
    for index, bit in enumerate(word):
        if bit == "1":
            value = 3 * value + (1 << index)
    return value

def primitive(word):
    length = len(word)
    return all(length % period or word != word[:period] * (length // period)
               for period in range(1, length))

def canonical(word):
    return word == min(word[offset:] + word[:offset] for offset in range(len(word)))

def cyclic_distance(left, right):
    prefixes = []
    total = 0
    for a, b in zip(left, right):
        total += (a == "1") - (b == "1")
        prefixes.append(total)
    assert total == 0
    circulation = sorted(-value for value in prefixes)[(len(left) - 1) // 2]
    return sum(abs(circulation + value) for value in prefixes)

assert len(RL20_WORD) == 184 and RL20_WORD.count("1") == 116
denominator = 2 ** len(RL20_WORD) - 3 ** RL20_WORD.count("1")
assert q1(RL20_WORD) % denominator == RL20_REMAINDER != 0
rotations = [RL20_WORD[offset:] + RL20_WORD[:offset] for offset in range(len(RL20_WORD))]
assert min(cyclic_distance(rotations[i], rotations[j])
           for i in range(len(rotations)) for j in range(i + 1, len(rotations))) == 4

words = pairs = divisible = 0
for length in range(8, 18):
    for bits in product("01", repeat=length):
        word = "".join(bits)
        weight = word.count("1")
        if min(weight, length - weight) < 4 or not primitive(word) or not canonical(word):
            continue
        denominator = 2 ** length - 3 ** weight
        if denominator <= 1:
            continue
        rotations = [word[offset:] + word[:offset] for offset in range(length)]
        distances = [(cyclic_distance(rotations[i], rotations[j]), i, j)
                     for i in range(length) for j in range(i + 1, length)]
        radius = min(distance for distance, _, _ in distances)
        if radius != 4:
            continue
        words += 1
        numerators = [q1(rotation) for rotation in rotations]
        for distance, i, j in distances:
            if distance == radius:
                pairs += 1
                divisible += (numerators[j] - numerators[i]) % denominator == 0

assert (words, pairs, divisible) == (1580, 27866, 0)
print("RL113 tournament structural and finite red-team verifier: PASS")
print("RL20 radius / ownership mismatch = 4 / nonzero")
print("primitive necklaces / closest pairs / D-divisible pairs =", words, pairs, divisible)
