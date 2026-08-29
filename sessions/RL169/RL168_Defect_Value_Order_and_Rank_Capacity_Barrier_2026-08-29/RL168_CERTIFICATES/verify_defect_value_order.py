#!/usr/bin/env python3
"""Exact audit for RL168's defect-exponent order and rank-capacity barrier."""
from fractions import Fraction
from itertools import product
from math import gcd

A = 217_976_794_617
L = 137_528_045_312
M0 = 1 << 71
assert gcd(A, L) == 1
assert L < (1 << 38)
# With log(2)>1/2, this is the exact arithmetic margin used in the
# order-plus-odd-packing capacity comparison.
assert (1 << 70) > 2 * L


def ln_interval(x, terms=260):
    """Rational atanh-series enclosure for log((1+x)/(1-x))."""
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
epsilon_hi = delta_hi / ln2_lo
theta_hi = L * epsilon_hi
assert 5 * theta_hi < 1

# If E_k-E_j>=1 and -(L-1)<=j-k<=L-1, the numerator of
# log_2(q_j/(lambda*q_k))*L is
# E_k-E_j-theta+(j-k)*theta/L.  The certified theta<1/5 makes its
# uniform lower bound strictly positive.
theta_cap = Fraction(1, 5)
assert 1 - theta_cap - Fraction(L - 1, L) * theta_cap > 0

cases = 0
for length in range(2, 8):
    for word in product(range(1, 5), repeat=length):
        total = sum(word)
        if gcd(total, length) != 1 or (1 << total) <= 3 ** length:
            continue
        partial = [0]
        for exponent in word:
            partial.append(partial[-1] + exponent)
        heights = [total * j // length - partial[j] for j in range(length)]
        if min(heights) < 0:
            continue
        E = [total * j - length * partial[j] for j in range(length)]
        assert E[0] == 0 and min(E) == 0
        assert len(set(E)) == length
        for e in E:
            rank = sum(other < e for other in E)
            assert 0 <= rank <= e
        cases += 1

assert cases > 0
print('RL168 defect-value order verifier: PASS')
print(f'certified theta upper bound: {float(theta_hi):.18f}')
print(f'coprime nonnegative-defect rank cases checked: {cases}')
print('order margin and external-floor rank-capacity arithmetic: PASS')
