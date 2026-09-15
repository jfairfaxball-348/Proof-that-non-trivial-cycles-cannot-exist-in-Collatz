#!/usr/bin/env python3
"""Exact RL329 diagnostic: constant-q mechanical plateau bounds at high carry.

Active-session scratch certificate; not authoritative promotion.
"""

from fractions import Fraction
from functools import lru_cache

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
LAMBDA_UPPER = 1 + Fraction(1, 1 << 40)
M_LOWER = 1 << 71
M_UPPER = 1 << 75
HIGH_CARRY_THRESHOLD = 20_390_252_058


def log_interval_atanh(x, terms=280):
    x2 = x * x
    term = x
    total = Fraction(0)
    for index in range(terms):
        total += term / (2 * index + 1)
        term *= x2
    lower = 2 * total
    upper = lower + 2 * term / (2 * terms + 1) / (1 - x2)
    return lower, upper


ln2_lower, ln2_upper = log_interval_atanh(Fraction(1, 3))
ln3_lower, ln3_upper = log_interval_atanh(Fraction(1, 2))
delta_upper = A * ln2_upper - ELL * ln3_lower
assert delta_upper > 0


@lru_cache(maxsize=None)
def mechanical_factors(length):
    cuts = sorted({0, ELL, *((-D * step) % ELL for step in range(length + 1))})
    factors = set()
    for left, right in zip(cuts, cuts[1:]):
        for residue in {left, min(left + 1, right - 1)}:
            previous = (residue + ELL - 1) // ELL
            gaps = []
            for step in range(1, length + 1):
                current = (residue + D * step + ELL - 1) // ELL
                gaps.append(1 + current - previous)
                previous = current
            factors.add(tuple(gaps))
    assert len(factors) == length + 1
    return tuple(sorted(factors))


def forced_residue(gaps):
    constant = 0
    for step, gap in enumerate(gaps, 1):
        constant = (1 << gap) * constant + 3 ** (step - 1)
    modulus = 3 ** len(gaps)
    residue = constant * pow(pow(2, sum(gaps), modulus), -1, modulus) % modulus
    return residue, modulus


def reconstruct(endpoint, gaps):
    states = [endpoint]
    state = endpoint
    for gap in gaps:
        numerator = (1 << gap) * state - 1
        assert numerator % 3 == 0
        state = numerator // 3
        assert state & 1
        states.append(state)
    return states


def height_band_upper(height):
    # RL326 gives P < 2^(q+1) lambda m.  With m<2^75 and
    # lambda<1+2^-40 this is strictly below the integer shown here.
    return (1 << (height + 76)) + (1 << (height + 36))


def owned_survivors(height, gap_length):
    upper = height_band_upper(height)
    survivors = []
    for gaps in mechanical_factors(gap_length):
        residue, modulus = forced_residue(gaps)
        lift = max(0, (M_LOWER - residue + modulus - 1) // modulus)
        endpoint = residue + lift * modulus
        while endpoint < upper:
            if endpoint & 1:
                states = reconstruct(endpoint, gaps)
                if delta_upper * min(states) >= HIGH_CARRY_THRESHOLD:
                    survivors.append((endpoint, min(states)))
            endpoint += modulus
    return survivors


# If q is constant at height h for B_h+1 consecutive ranks, the B_h
# intervening physical gaps are exactly a rational-mechanical factor.
# The exact reconstruction below shows that such a block cannot be owned at
# high carry, so every constant-height plateau has at most B_h ranks.
FORBIDDEN_GAP_LENGTH = {
    0: 49,
    1: 51,
    2: 53,
    3: 53,
    4: 53,
    5: 55,
    6: 55,
    7: 55,
    8: 57,
}

for height, gap_length in FORBIDDEN_GAP_LENGTH.items():
    assert 3 ** gap_length > height_band_upper(height)
    assert owned_survivors(height, gap_length) == []

print("RL329_CONSTANT_HEIGHT_PLATEAU_VERIFIER_GREEN")
for height, gap_length in FORBIDDEN_GAP_LENGTH.items():
    print("q_height", height, "plateau_length_le", gap_length)
