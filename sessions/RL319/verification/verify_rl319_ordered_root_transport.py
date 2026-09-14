#!/usr/bin/env python3
"""Exact regression and arithmetic check for RL319 root transport.

Small-word enumeration is regression evidence. The logarithmic comparison is
an exact rational-interval certificate.
"""

from fractions import Fraction
from itertools import combinations
from math import gcd


def ln_ratio_interval(x, terms=280):
    """Enclose log((1+x)/(1-x)) by the positive atanh series."""
    x2 = x * x
    term = x
    total = Fraction(0)
    for index in range(terms):
        total += term / (2 * index + 1)
        term *= x2
    lower = 2 * total
    tail = 2 * term / (2 * terms + 1) / (1 - x2)
    return lower, lower + tail


def cyclic_window(word, start, length):
    size = len(word)
    return tuple(word[(start + offset) % size] for offset in range(length))


transport_checks = 0
early_root_checks = 0

for a in range(3, 11):
    for ell in range(1, a):
        if gcd(a, ell) != 1 or (1 << a) <= 3**ell:
            continue
        length = 2 * a
        weight = 2 * ell
        for support_tail in combinations(range(1, length), weight - 1):
            support = (0,) + support_tail
            word = tuple(1 if index in support else 0 for index in range(length))

            prefix = 0
            defect_ok = True
            for phase in range(length + 1):
                if a * prefix - ell * phase < 0:
                    defect_ok = False
                    break
                if phase < length:
                    prefix += word[phase]
            if not defect_ok:
                continue

            assert prefix == weight
            for cut in range(length):
                u = cyclic_window(word, cut, a)
                v = cyclic_window(word, cut + a, a)
                if sum(u) != ell or sum(v) != ell:
                    continue

                count_u = 0
                count_v = 0
                ordered = True
                for phase in range(a + 1):
                    if count_u > count_v:  # u must be rankwise later
                        ordered = False
                        break
                    if phase < a:
                        count_u += u[phase]
                        count_v += v[phase]
                if not ordered:
                    continue

                root_position = (-cut) % length
                root_window_balanced = sum(word[:a]) == ell
                if root_position == 0 or root_position == a:
                    assert root_window_balanced
                elif root_position > a:  # root lies strictly inside early row v
                    assert root_window_balanced
                    early_root_checks += 1
                transport_checks += 1

assert transport_checks > 0
assert early_root_checks > 0

# First-survivor exact comparison Delta < log(1+2^-40), which implies
# 2^75(exp(Delta)-1) < 2^35.
A = 217_976_794_617
L = 137_528_045_312
ln2_lo, ln2_hi = ln_ratio_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_ratio_interval(Fraction(1, 2))
delta_hi = A * ln2_hi - L * ln3_lo
t = Fraction(1, 1 << 40)
log1p_lo, _log1p_hi = ln_ratio_interval(t / (2 + t), terms=40)
assert delta_hi > 0
assert delta_hi < log1p_lo

print("RL319 ordered-root transport regression: PASS")
print(f"ordered_balanced_cut_checks={transport_checks}")
print(f"early_row_root_implications={early_root_checks}")
print("exact_bound=2^75*(exp(Delta)-1)<2^35: PASS")
print("scope=word enumeration is evidence; log comparison is exact certificate")
