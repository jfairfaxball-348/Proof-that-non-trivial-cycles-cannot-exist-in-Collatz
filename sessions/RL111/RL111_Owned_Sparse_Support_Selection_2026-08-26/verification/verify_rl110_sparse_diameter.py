#!/usr/bin/env python3
"""Exact finite checks for the RL110 numerator-diameter/support calculations.

Local work only; this is not an authoritative certificate.
"""
from itertools import product


def q1(word):
    value = 0
    for index, bit in enumerate(word):
        if bit == "1":
            value = 3 * value + (1 << index)
    return value


def cyclic_flow_distance(left, right):
    cumulative = 0
    discrepancies = []
    for a, b in zip(left, right):
        cumulative += (a == "1") - (b == "1")
        discrepancies.append(cumulative)
    assert cumulative == 0
    circulation = sorted(-value for value in discrepancies)[(len(left) - 1) // 2]
    return sum(abs(circulation + value) for value in discrepancies)


# The exact extrema follow from the positive adjacent-swap identity.  Verify
# them independently by exhaustive enumeration for small binary words.
word_checks = swap_checks = 0
for length in range(2, 12):
    values_by_weight = {}
    max_swap_by_weight = {}
    for letters in product("01", repeat=length):
        word = "".join(letters)
        weight = word.count("1")
        values_by_weight.setdefault(weight, []).append(q1(word))
        for index in range(length - 1):
            if word[index:index + 2] == "10":
                suffix_ones = word[index + 2:].count("1")
                coefficient = (1 << index) * 3**suffix_ones
                swapped = word[:index] + "01" + word[index + 2:]
                assert q1(swapped) - q1(word) == coefficient
                max_swap_by_weight[weight] = max(max_swap_by_weight.get(weight, 0), coefficient)
                swap_checks += 1
        word_checks += 1
    for weight in range(1, length):
        zeros = length - weight
        minimum = 3**weight - 2**weight
        maximum = 2**zeros * minimum
        assert min(values_by_weight[weight]) == minimum
        assert max(values_by_weight[weight]) == maximum
        assert max_swap_by_weight[weight] == 2**(zeros - 1) * 3**(weight - 1)


# The frozen RL20 word demonstrates why geometry alone cannot supply |S|<D.
rl20 = (
    "110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
    "110110110101101101011011011010110110101101101101011011010110110110101101101011011010"
    "1101101101011010"
)
length = len(rl20)
weight = rl20.count("1")
denominator = 2**length - 3**weight
rl20_denominator = denominator
closest = []
for left_index in range(length):
    left = rl20[left_index:] + rl20[:left_index]
    for right_index in range(left_index + 1, length):
        right = rl20[right_index:] + rl20[:right_index]
        if cyclic_flow_distance(left, right) == 4:
            closest.append(abs(q1(right) - q1(left)))
assert closest and min(closest) > denominator
assert q1(rl20) % denominator != 0


# A small primitive radius-4 local geometry example contains the extremal
# coefficient scale and still has every closest rotation difference above D.
small = "00010111"
length = len(small)
weight = small.count("1")
denominator = 2**length - 3**weight
distances = []
for offset in range(1, length):
    rotated = small[offset:] + small[:offset]
    distance = cyclic_flow_distance(small, rotated)
    distances.append((distance, abs(q1(rotated) - q1(small))))
assert min(distance for distance, _ in distances) == 4
assert all(difference > denominator for distance, difference in distances if distance == 4)
assert q1(small) % denominator != 0

print("RL110 sparse diameter verifier: PASS")
print("exhaustive words checked =", word_checks)
print("single-swap identities checked =", swap_checks)
print("RL20 minimum radius-4 sparse difference / D > 1 =", min(closest) > rl20_denominator)
print("RL20 ownership discriminator Q mod D =", q1(rl20) % rl20_denominator)
print("small primitive radius-4 local red team =", small)
print("small red-team ownership discriminator Q mod D =", q1(small) % denominator)
