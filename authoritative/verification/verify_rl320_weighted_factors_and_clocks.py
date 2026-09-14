#!/usr/bin/env python3
"""Exact regression for RL320 weighted factors and clock contraction."""

from math import gcd


def v2(value):
    assert value > 0
    return (value & -value).bit_length() - 1


factor_checks = 0
for a in range(3, 13):
    x = 1 << a
    for ell in range(1, a):
        y_base = 3**ell
        if x <= y_base:
            continue
        d0 = x - y_base
        h_factor = x + y_base
        for height in range(1, ell + 1):
            power = 3**height
            for minimum in range(1, 30):
                for contact in range(-30, 31):
                    first = power * d0 * minimum + x * contact
                    second = d0 * minimum - 3 ** (ell - height) * contact
                    if first <= 0 or second <= 0:
                        continue
                    antipode = power * minimum + contact
                    assert first + power * second == d0 * (antipode + power * minimum)
                    assert first - power * second == h_factor * contact
                    assert (first - x * contact) % power == 0
                    factor_checks += 1

clock_checks = 0
equal_clock_checks = 0
for h in range(5, 180, 2):
    if gcd(h, 6) != 1:
        continue
    for kappa in range(1, 1 << 12):
        c = v2(kappa)
        for rho in range(1, min(h, 45)):
            if gcd(h, rho) != 1:
                continue
            e = v2(kappa * h + rho)
            t = v2(rho)
            if e < t:
                assert c == e
            elif t < e:
                assert c == t
            else:
                assert c > e
                equal_clock_checks += 1
            assert min(e, t) <= c
            clock_checks += 1

assert factor_checks > 0
assert clock_checks > 0
assert equal_clock_checks > 0

print("RL320 weighted-factor and three-clock regression: PASS")
print(f"weighted_factor_checks={factor_checks}")
print(f"valuation_clock_checks={clock_checks}")
print(f"equal_clock_cases={equal_clock_checks}")
print("analytic_cap=kappa<2^34 implies min(e,t)<=33 and equal e=t<=32")
print("scope=regression evidence; analytic proof is in RL320_CLOSEOUT.md")
