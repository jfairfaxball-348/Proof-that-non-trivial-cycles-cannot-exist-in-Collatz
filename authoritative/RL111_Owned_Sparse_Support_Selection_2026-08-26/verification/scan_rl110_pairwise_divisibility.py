#!/usr/bin/env python3
"""Finite RL110 red team; NOT an authoritative/global certificate.

It exhausts primitive binary necklaces of lengths 8 through 17 with positive
D, minimum cyclic rotation distance exactly four, and checks every closest
rotation pair for the pairwise condition D | (Q(v)-Q(u)).
"""
from itertools import product


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


def canonical_necklace(word):
    return word == min(word[offset:] + word[:offset] for offset in range(len(word)))


def cyclic_distance(left, right):
    cumulative = 0
    flow_prefixes = []
    for a, b in zip(left, right):
        cumulative += (a == "1") - (b == "1")
        flow_prefixes.append(cumulative)
    assert cumulative == 0
    circulation = sorted(-value for value in flow_prefixes)[(len(left) - 1) // 2]
    return sum(abs(circulation + value) for value in flow_prefixes)


total_words = total_pairs = divisible_pairs = 0
for length in range(8, 18):
    words = pairs = divisible = 0
    for bits in product("01", repeat=length):
        word = "".join(bits)
        weight = word.count("1")
        if min(weight, length - weight) < 4 or not primitive(word) or not canonical_necklace(word):
            continue
        denominator = 2**length - 3**weight
        if denominator <= 1:
            continue
        rotations = [word[offset:] + word[:offset] for offset in range(length)]
        numerators = [q1(rotation) for rotation in rotations]
        table = [(cyclic_distance(rotations[i], rotations[j]), i, j)
                 for i in range(length) for j in range(i + 1, length)]
        radius = min(distance for distance, _, _ in table)
        if radius != 4:
            continue
        words += 1
        for _, i, j in table:
            if cyclic_distance(rotations[i], rotations[j]) == radius:
                pairs += 1
                if (numerators[j] - numerators[i]) % denominator == 0:
                    divisible += 1
    print(f"length={length}: necklaces={words}, closest_pairs={pairs}, D-divisible_pairs={divisible}")
    assert divisible == 0
    total_words += words
    total_pairs += pairs
    divisible_pairs += divisible

print("RL110 pairwise-divisibility finite red team: PASS")
print("primitive necklaces checked =", total_words)
print("closest pairs checked =", total_pairs)
print("D-divisible pairs =", divisible_pairs)
