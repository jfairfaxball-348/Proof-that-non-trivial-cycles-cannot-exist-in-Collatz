#!/usr/bin/env python3
"""Exact RL329 diagnostic: physically owned three-positive bridges at high carry.

This is an active-session scratch certificate, not authoritative promotion.
It reconstructs every q-run of length three returning 0 -> positive -> 0,
every adjacent zero pair of total 47..98, every rational-mechanical factor,
and every odd endpoint lift in the inherited physical state band.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
M_LOWER = 1 << 71
STATE_UPPER = (1 << 76) + (1 << 36)
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
    return tuple(states)


def band_realizations(gaps):
    residue, modulus = forced_residue(gaps)
    lift = max(0, (M_LOWER - residue + modulus - 1) // modulus)
    endpoint = residue + lift * modulus
    while endpoint < STATE_UPPER:
        if endpoint & 1:
            yield endpoint, reconstruct(endpoint, gaps)
        endpoint += modulus


def high_carry_owned(states):
    return delta_upper * min(states) >= HIGH_CARRY_THRESHOLD


# For q_0=q_4=0, q_1,q_2,q_3>0 and physical gap changes bounded below
# by -1, the complete positive excursion shapes are the five Catalan paths.
Q_SHAPES = (
    (1, 1, 1),
    (1, 2, 1),
    (2, 1, 1),
    (2, 2, 1),
    (3, 2, 1),
)

rows = []
for zero_total in range(47, 99):
    gap_length = zero_total + 2
    factors = mechanical_factors(gap_length)
    for left_zero in range(max(1, zero_total - 49), min(49, zero_total - 1) + 1):
        right_zero = zero_total - left_zero
        for baseline in factors:
            for shape in Q_SHAPES:
                q = (0,) + shape + (0,)
                gaps = list(baseline)
                valid = True
                for offset in range(4):
                    position = left_zero - 1 + offset
                    gaps[position] += q[offset + 1] - q[offset]
                    if gaps[position] < 1:
                        valid = False
                        break
                if not valid:
                    continue
                for endpoint, states in band_realizations(tuple(gaps)):
                    if high_carry_owned(states):
                        left_plateau = states[:left_zero]
                        right_plateau = states[left_zero + 3 :]
                        assert len(left_plateau) == left_zero
                        assert len(right_plateau) == right_zero
                        rows.append(
                            (
                                left_plateau,
                                right_plateau,
                                left_zero,
                                right_zero,
                                shape,
                                endpoint,
                            )
                        )

counts = Counter(row[2] + row[3] for row in rows)
assert counts == {47: 288, 48: 104, 49: 44, 50: 20, 51: 5, 52: 2}
assert len(rows) == 463
assert max(counts) == 52
assert not any(row[2] == 49 and row[3] == 49 for row in rows)

# Exact consecutive ownership: equality of the first state on the shared zero
# plateau is necessary; deterministic ordinary dynamics then fixes that plateau.
left_index = defaultdict(list)
for index, row in enumerate(rows):
    left_index[(row[2], row[0][0])].append(index)

links = []
for first_index, first in enumerate(rows):
    for second_index in left_index[(first[3], first[1][0])]:
        links.append((first_index, second_index))

pair_links = {
    ((rows[first][2], rows[first][3]), (rows[second][2], rows[second][3]))
    for first, second in links
}
assert len(links) == 2
assert pair_links == {((2, 45), (45, 2))}

print("RL329_THREE_POSITIVE_OWNERSHIP_VERIFIER_GREEN")
print("three_positive_counts", dict(sorted(counts.items())))
print("three_positive_survivors", len(rows))
print("three_positive_max_zero_total", max(counts))
print("three_positive_exact_links", len(links))
print("three_positive_pair_links", pair_links)
print("N49_to_N49_survivors", 0)
