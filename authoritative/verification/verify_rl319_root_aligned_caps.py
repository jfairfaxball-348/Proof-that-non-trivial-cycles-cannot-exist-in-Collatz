#!/usr/bin/env python3
"""Exact rational-interval verifier for RL319 root-aligned caps."""

from fractions import Fraction


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


A = 217_976_794_617
L = 137_528_045_312
ln2_lo, ln2_hi = ln_ratio_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_ratio_interval(Fraction(1, 2))
delta_lo = A * ln2_lo - L * ln3_hi
delta_hi = A * ln2_hi - L * ln3_lo

t = Fraction(1, 1 << 40)
log1p_lo, _log1p_hi = ln_ratio_interval(t / (2 + t), terms=40)

assert delta_lo > 0
assert delta_hi < log1p_lo
assert log1p_lo < t

# exp(Delta)-1 < 2^-40 gives the state-gap cap.
assert Fraction(1 << 75, 1 << 40) == 1 << 35

# D0/H=tanh(Delta/2)<Delta/2<2^-41 gives the carry cap.
assert delta_hi / 2 < Fraction(1, 1 << 41)
assert Fraction(1 << 75, 1 << 41) == 1 << 34

print("RL319 root-aligned cap verifier: PASS")
print("state_gap_cap=G<2^35")
print("first_row_difference_cap=v2(G)<=34")
print("cofactor_quotient_cap=0<=kappa<2^34")
print("scope=root-aligned first-survivor g=2 branch")
