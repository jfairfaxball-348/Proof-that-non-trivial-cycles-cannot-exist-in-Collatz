#!/usr/bin/env python3
"""Exact small-instance regression for the RL316 row-energy checkpoint.

This verifies algebraic identities on bounded instances.  It is not a proof of
the analytic statements and is NOT PROMOTED.
"""

from itertools import combinations
from math import gcd


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


def prefix(word):
    result = [0]
    for bit in word:
        result.append(result[-1] + bit)
    return result


def prefix_potential(word):
    weight = sum(word)
    counts = prefix(word)
    return sum((1 << j) * 3 ** (weight - counts[j]) for j in range(len(word)))


def canonical_rows(word):
    length = len(word)
    weight = sum(word)
    multiplicity = gcd(length, weight)
    assert multiplicity > 1
    row_length = length // multiplicity
    row_weight = weight // multiplicity
    rows = [
        word[k * row_length:(k + 1) * row_length]
        for k in range(multiplicity)
    ]

    levels = [0]
    for row in rows:
        levels.append(levels[-1] + sum(row) - row_weight)
    cut = min(range(multiplicity), key=lambda k: levels[k])
    rows = rows[cut:] + rows[:cut]
    word = sum(rows, [])

    levels = [0]
    prefixes = []
    for row in rows:
        levels.append(levels[-1] + sum(row) - row_weight)
        prefixes.append(prefix(row))
    assert min(levels[:-1]) == 0 and levels[-1] == 0

    minimum = [
        min(levels[k] + prefixes[k][j] for k in range(multiplicity))
        for j in range(row_length + 1)
    ]
    shadow = [minimum[j + 1] - minimum[j] for j in range(row_length)]
    interfaces = [
        [levels[k] + prefixes[k][j] - minimum[j] for j in range(row_length + 1)]
        for k in range(multiplicity)
    ]
    return word, rows, levels, prefixes, shadow, interfaces


general_checks = 0
for length in range(4, 13):
    for weight in range(1, length):
        multiplicity = gcd(length, weight)
        if multiplicity <= 1 or 2 ** length <= 3 ** weight:
            continue
        for original in words(length, weight):
            word, rows, levels, prefixes, shadow, interfaces = canonical_rows(original)
            row_length = length // multiplicity
            row_weight = weight // multiplicity
            x_base = 1 << row_length
            y_base = 3 ** row_weight
            d_base = x_base - y_base
            cofactor = (x_base ** multiplicity - y_base ** multiplicity) // d_base
            shadow_q = numerator(shadow)

            assert prefix_potential(shadow) == 4 * shadow_q + d_base
            for row in rows:
                assert prefix_potential(row) == 4 * numerator(row) + (1 << row_length) - 3 ** sum(row)

            repeated_prefix = 0
            direct_energy = 0
            normalized_rows = []
            for k in range(multiplicity):
                row_energy = 0
                for j in range(row_length):
                    flat = k * row_length + j
                    height = interfaces[k][j]
                    term = (
                        (1 << flat)
                        * 3 ** (weight - repeated_prefix - height)
                        * (3 ** height - 1)
                    )
                    direct_energy += term
                    row_energy += term // (x_base ** k)
                    repeated_prefix += shadow[j]
                normalized_rows.append(row_energy)

            for k, row in enumerate(rows):
                remaining_weight = (multiplicity - k - 1) * row_weight - levels[k + 1]
                formula = (
                    3 ** ((multiplicity - k - 1) * row_weight) * (4 * shadow_q + d_base)
                    - 3 ** remaining_weight
                    * (4 * numerator(row) + x_base - 3 ** sum(row))
                )
                assert normalized_rows[k] == formula

            full_q = numerator(word)
            assert direct_energy == 4 * (shadow_q * cofactor - full_q)
            general_checks += 1


pair_checks = 0
for row_length in range(2, 11):
    for row_weight in range(1, row_length):
        x_base = 1 << row_length
        y_base = 3 ** row_weight
        if x_base <= y_base:
            continue
        cofactor = x_base + y_base
        row_words = list(words(row_length, row_weight))
        for row0 in row_words:
            positions0 = [j for j, bit in enumerate(row0) if bit]
            for row1 in row_words:
                positions1 = [j for j, bit in enumerate(row1) if bit]
                late_positions = [max(p0, p1) for p0, p1 in zip(positions0, positions1)]
                early_positions = [min(p0, p1) for p0, p1 in zip(positions0, positions1)]
                late = [int(j in late_positions) for j in range(row_length)]
                early = [int(j in early_positions) for j in range(row_length)]

                p0 = prefix(row0)
                p1 = prefix(row1)
                minimum = [min(a, b) for a, b in zip(p0, p1)]
                maximum = [max(a, b) for a, b in zip(p0, p1)]
                assert late == [minimum[j + 1] - minimum[j] for j in range(row_length)]
                assert early == [maximum[j + 1] - maximum[j] for j in range(row_length)]

                q0 = numerator(row0)
                q1 = numerator(row1)
                q_late = numerator(late)
                q_early = numerator(early)
                delta0 = q_late - q0
                delta1 = q_late - q1
                assert delta0 >= 0 and delta1 >= 0
                assert q0 + q1 == q_late + q_early
                assert delta0 + delta1 == q_late - q_early
                if q0 != q1 and (q0 - q1) % cofactor == 0:
                    assert q_late - q_early >= cofactor
                pair_checks += 1

print("RL316 row-energy regression: PASS")
print("general canonical words checked:", general_checks)
print("g=2 row pairs checked:", pair_checks)
