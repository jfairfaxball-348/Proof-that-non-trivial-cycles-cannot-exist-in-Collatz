#!/usr/bin/env python3
"""Exact audit for RL170's non-chain order-permutation budget barrier."""
from fractions import Fraction
from itertools import product

A = 217_976_794_617
L = 137_528_045_312
M0 = 1 << 71
assert L < (1 << 38)
assert M0 > 2 * L


def ln_interval(x, terms=260):
    x2 = x * x
    term = x
    total = Fraction(0)
    for k in range(terms):
        total += term / (2 * k + 1)
        term *= x2
    lower = 2 * total
    tail = 2 * term / (2 * terms + 1) / (1 - x2)
    return lower, lower + tail


ln2_lo, ln2_hi = ln_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_interval(Fraction(1, 2))
delta_hi = A * ln2_hi - L * ln3_lo
theta_hi = L * delta_hi / ln2_lo
assert 5 * theta_hi < 1
assert delta_hi < Fraction(1, 5 * L) < Fraction(1, 2)
# e^x-1 < 2x on 0<x<1/2 supplies this strict lambda-1 bound.
lam_minus_one_upper = 2 * delta_hi
assert lam_minus_one_upper < Fraction(2, 5 * L)
assert 3 * lam_minus_one_upper < 1

# The universal comparison used in the report:
# 2*sum(q_j r_j) < 2L(L-1), while Lm-mQ > m(L-1).
assert M0 * (L - 1) > 2 * L * (L - 1)


def check_sum_identity(word):
    y = Fraction(1)
    q = Fraction(1)
    z_values = []
    q_values = []
    for exponent in word:
        z_values.append(q * y)
        q_values.append(q)
        y = (3 * y + 1) / (1 << exponent)
        q = q * (1 << exponent) / 3
    expected = len(word) + sum((len(word) - 1 - i) * q_values[i] / 3 for i in range(len(word)))
    assert sum(z_values) == expected


checks = 0
for length in range(1, 7):
    for word in product(range(1, 5), repeat=length):
        check_sum_identity(word)
        checks += 1

assert checks == sum(4 ** n for n in range(1, 7))
print('RL170 order-permutation budget verifier: PASS')
print(f'certified theta upper bound: {float(theta_hi):.18f}')
print(f'ordinary sum identities checked: {checks}')
print('universal rank budget is strictly below least-state slack: PASS')
