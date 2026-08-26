#!/usr/bin/env python3
"""Exact finite audit for the RL107 roof/blue-alignment test."""

from itertools import product


def inverse_word_state(maximum: int, word: tuple[int, ...]) -> int:
    """Apply ordinary inverse letters: 0 -> 2x, 1 -> (2x-1)/3."""
    x = maximum
    for letter in word:
        if letter == 0:
            x *= 2
        else:
            assert (2 * x - 1) % 3 == 0
            x = (2 * x - 1) // 3
    return x


def least_even_cylinder_representative(word: tuple[int, ...]) -> int:
    modulus = 2 * 3 ** sum(word)
    for maximum in range(2, modulus + 1, 2):
        try:
            inverse_word_state(maximum, word)
        except AssertionError:
            continue
        return maximum
    raise AssertionError("missing inverse cylinder representative")


checks = 0
# Depth-two blue-comb/roof equality: Q=(4*2^k-5)/9.
for k in range(3, 3001, 6):
    q = (4 * (2 ** k + 1)) // 9 - 1
    p = (2 ** (k + 1) - 1) // 3
    assert 9 * q == 4 * (2 ** k) - 5
    assert 3 * p + 1 == 2 ** (k + 1)
    assert (3 * q + 1) // 2 == p
    assert (3 * p + 1) // 2 == 2 ** k
    checks += 1

# Same roof start and the same raw counts can have different least inverse
# cylinder representatives.  This is a finite audit of the two exact
# counterexamples used in the report, not a first-Farey word search.
power_word = tuple(map(int, "1110001011"))
nonpower_word = tuple(map(int, "1100001111"))
assert len(power_word) == len(nonpower_word) == 10
assert sum(power_word) == sum(nonpower_word) == 6
assert power_word[:2] == nonpower_word[:2] == (1, 1)
power_maximum = least_even_cylinder_representative(power_word)
nonpower_maximum = least_even_cylinder_representative(nonpower_word)
assert power_maximum == 512
assert nonpower_maximum == 1106
assert power_maximum & (power_maximum - 1) == 0
assert nonpower_maximum & (nonpower_maximum - 1) != 0
assert inverse_word_state(power_maximum, power_word) > 0
assert inverse_word_state(nonpower_maximum, nonpower_word) > 0
checks += 2

print("RL107 roof/blue alignment verifier: PASS")
print("exact roof-comb checks =", checks - 2)
print("same-count inverse-cylinder counterexamples = 2")
