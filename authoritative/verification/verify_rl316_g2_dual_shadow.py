#!/usr/bin/env python3
"""Exact regression for the RL316 g=2 dual-shadow checkpoint.

The bounded checks and frozen RL21 witness are evidence only.  The theorem is
proved analytically in the accompanying checkpoint note and is NOT PROMOTED.
"""

from fractions import Fraction
from itertools import combinations


def numerator(word):
    weight = sum(word)
    seen = 0
    value = 0
    for index, bit in enumerate(word):
        if bit:
            value += (1 << index) * 3 ** (weight - 1 - seen)
            seen += 1
    return value


def words(length, weight):
    for support in combinations(range(length), weight):
        word = [0] * length
        for index in support:
            word[index] = 1
        yield word


def envelopes(row0, row1):
    positions0 = [j for j, bit in enumerate(row0) if bit]
    positions1 = [j for j, bit in enumerate(row1) if bit]
    late = [0] * len(row0)
    early = [0] * len(row0)
    for p0, p1 in zip(positions0, positions1):
        late[max(p0, p1)] = 1
        early[min(p0, p1)] = 1
    return late, early


checked = 0
for length in range(2, 11):
    for weight in range(1, length):
        x_base = 1 << length
        y_base = 3 ** weight
        if x_base <= y_base:
            continue
        d_base = x_base - y_base
        cofactor = x_base + y_base
        full_d = d_base * cofactor
        population = list(words(length, weight))
        for row0 in population:
            q0 = numerator(row0)
            for row1 in population:
                q1 = numerator(row1)
                if q0 <= q1:
                    continue
                late, early = envelopes(row0, row1)
                q_late = numerator(late)
                q_early = numerator(early)
                low_state = Fraction(y_base * q0 + x_base * q1, full_d)
                high_state = Fraction(x_base * q0 + y_base * q1, full_d)
                gap = high_state - low_state
                epsilon = q_late - q0
                reduced_late = Fraction(q_late, d_base)
                reduced_early = Fraction(q_early, d_base)
                n_value = q_late - d_base * low_state

                assert gap == Fraction(q0 - q1, cofactor)
                assert q_late + q_early == q0 + q1
                assert epsilon >= 0
                assert q_late == d_base * low_state + x_base * gap + epsilon
                assert q_early == d_base * low_state - y_base * gap - epsilon
                assert reduced_late - high_state == low_state - reduced_early
                assert reduced_late + reduced_early == low_state + high_state
                assert 0 < reduced_early < low_state < high_state < reduced_late
                assert n_value == x_base * gap + epsilon
                assert n_value + q_early == d_base * high_state
                checked += 1


# Frozen RL21 X+Y-factor countermodel.  It saturates the late/early envelope
# gap and the n=XG lower edge, while deliberately failing X-Y ownership.
u_text = "11011011010110110110101101110011011100110110110101110101011011100"
v_text = "11111111110111000111110011011011110101010111110011101000011100000"
u = [int(bit) for bit in u_text]
v = [int(bit) for bit in v_text]
length = 65
weight = 41
x_base = 1 << length
y_base = 3 ** weight
d_base = x_base - y_base
cofactor = x_base + y_base
q0 = numerator(u)
q1 = numerator(v)
late, early = envelopes(u, v)
q_late = numerator(late)
q_early = numerator(early)
assert q0 - q1 == 4 * cofactor
assert (q0 + q1) % d_base != 0
assert q_late == q0
assert q_late - q_early == 4 * cofactor
assert q_late - q0 == 0
assert q_late - d_base * Fraction(y_base * q0 + x_base * q1, d_base * cofactor) == 4 * x_base


# RL38's unique area-seven local crossing is the quotient-one saturation.
local0 = [1, 0, 1, 0, 0, 0]
local1 = [0, 0, 0, 0, 1, 1]
late, early = envelopes(local0, local1)
assert numerator(late) - numerator(early) == (1 << 6) + 3 ** 2

print("RL316 g=2 dual-shadow regression: PASS")
print("ordered bounded row pairs checked:", checked)
print("RL21 H-factor saturation replay: PASS")
print("RL38 area-seven saturation replay: PASS")
