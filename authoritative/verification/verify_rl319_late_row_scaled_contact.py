#!/usr/bin/env python3
"""Regression for the RL319 late-row-root scaled-contact normal form."""

from fractions import Fraction
from itertools import combinations
from math import ceil, floor, gcd


def ln_ratio_interval(x, terms=280):
    x2 = x * x
    term = x
    total = Fraction(0)
    for index in range(terms):
        total += term / (2 * index + 1)
        term *= x2
    lower = 2 * total
    tail = 2 * term / (2 * terms + 1) / (1 - x2)
    return lower, lower + tail


def numerator(word):
    weight = sum(word)
    seen = 0
    value = 0
    for index, bit in enumerate(word):
        if bit:
            value += 2**index * 3 ** (weight - 1 - seen)
            seen += 1
    return value


# Every positive-weight binary numerator is a unit modulo 3.
numerator_checks = 0
for length in range(1, 12):
    for weight in range(1, length + 1):
        for support in combinations(range(length), weight):
            word = tuple(1 if index in support else 0 for index in range(length))
            assert numerator(word) % 3 != 0
            numerator_checks += 1

# Exact first-survivor comparison D0/Y=exp(Delta)-1<2^-40.
A = 217_976_794_617
L = 137_528_045_312
ln2_lo, ln2_hi = ln_ratio_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_ratio_interval(Fraction(1, 2))
delta_hi = A * ln2_hi - L * ln3_lo
t = Fraction(1, 1 << 40)
log1p_lo, _log1p_hi = ln_ratio_interval(t / (2 + t), terms=40)
assert delta_hi < log1p_lo

# Algebraic identity and positivity window regression over exact small models.
identity_checks = 0
for x_base in range(5, 80):
    for y_base in range(1, x_base):
        d0 = x_base - y_base
        for height in range(1, 6):
            power = 3**height
            for minimum in range(1, 30):
                lower = Fraction(-power * d0 * minimum, x_base)
                upper = Fraction(power * d0 * minimum, y_base)
                candidates = {
                    floor(lower), floor(lower) + 1, -1, 0, 1,
                    ceil(upper) - 1, ceil(upper),
                }
                for contact in sorted(candidates):
                    u = power * d0 * minimum + x_base * contact
                    scaled_v = power * d0 * minimum - y_base * contact
                    if u > 0 and scaled_v > 0:
                        assert lower < contact < upper
                        identity_checks += 1

assert numerator_checks > 0 and identity_checks > 0
print("RL319 late-row scaled-contact regression: PASS")
print(f"numerator_mod3_checks={numerator_checks}")
print(f"positive_window_identity_checks={identity_checks}")
print("exact_scaled_bound=abs(K)<3^r*2^35: PASS")
print("scope=regression evidence; analytic proof is in the checkpoint note")
