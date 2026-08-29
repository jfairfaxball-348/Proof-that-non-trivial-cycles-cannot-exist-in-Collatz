#!/usr/bin/env python3
"""Exact audit for RL169's ordered-chain affine gap barrier."""
from fractions import Fraction
from itertools import product

A = 217_976_794_617
L = 137_528_045_312
assert L < (1 << 38)


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
# log(2)<1 turns theta<1/5 into the required Delta bound.
assert delta_hi < Fraction(1, 5 * L)
assert delta_hi < Fraction(1, 2)
# e^x-1 < 2x for 0<x<1/2; this is the analytic bound used in the report.
assert 2 * delta_hi < Fraction(2, 5 * L)
assert Fraction(1, 1) / (2 * delta_hi) > Fraction(5 * L, 2) > L


def check_increment(word):
    """Check z_(j+1)-z_j=q_j/3 for an exact rational trajectory."""
    y = Fraction(1)
    q = Fraction(1)
    for exponent in word:
        z = q * y
        next_y = (3 * y + 1) / (1 << exponent)
        next_q = q * (1 << exponent) / 3
        assert next_q * next_y - z == q / 3
        y, q = next_y, next_q


checks = 0
for length in range(1, 7):
    for word in product(range(1, 5), repeat=length):
        check_increment(word)
        checks += 1

assert checks == sum(4 ** n for n in range(1, 7))
print('RL169 ordered-chain gap verifier: PASS')
print(f'certified theta upper bound: {float(theta_hi):.18f}')
print(f'ordinary affine increment words checked: {checks}')
print('chain capacity lower bound > 5L/2 > L: PASS')
