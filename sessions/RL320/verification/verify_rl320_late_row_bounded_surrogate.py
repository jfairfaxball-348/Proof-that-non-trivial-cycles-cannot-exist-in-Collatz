#!/usr/bin/env python3
"""Exact checks for the RL320 bounded balanced-surrogate contraction.

Small integer loops are regression evidence.  The first-survivor logarithmic
comparison and the proof are classified separately in the checkpoint note.
"""

from fractions import Fraction
from math import ceil, floor


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


# Exact lower enclosure Delta>2^-41 at the first external survivor.
A = 217_976_794_617
L = 137_528_045_312
ln2_lo, ln2_hi = ln_ratio_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_ratio_interval(Fraction(1, 2))
delta_lo = A * ln2_lo - L * ln3_hi
delta_hi = A * ln2_hi - L * ln3_lo
assert delta_lo > Fraction(1, 1 << 41)
assert delta_hi < 1

# Algebraic and inward-rounding regression over exact rational models.
checks = 0
negative_theta = 0
positive_theta = 0
for x in range(5, 36):
    for y_base in range(1, x):
        d0 = x - y_base
        for height in range(1, 6):
            power = 3**height
            for minimum in range(2, 19):
                lower = Fraction(-d0 * minimum, x)
                upper = Fraction(d0 * minimum, y_base)
                if upper - lower <= 1:
                    continue
                contact_lo = floor(power * lower) + 1
                contact_hi = ceil(power * upper) - 1
                probes = {
                    contact_lo, contact_lo + 1, contact_lo + 2,
                    contact_hi - 2, contact_hi - 1, contact_hi,
                    -power - 1, -power + 1, -2, -1, 1, 2,
                    power - 1, power + 1,
                }
                for contact in sorted(probes):
                    if not contact_lo <= contact <= contact_hi:
                        continue
                    if contact % 3 == 0:
                        continue
                    scaled = Fraction(contact, power)
                    candidates = (floor(scaled), ceil(scaled))
                    carry = next((candidate for candidate in candidates
                                  if lower < candidate < upper), None)
                    assert carry is not None
                    theta = contact - power * carry
                    assert 0 < abs(theta) < power
                    n_state = minimum + carry
                    z = d0 * minimum + x * carry
                    w = d0 * minimum - y_base * carry
                    assert z > 0 and w > 0
                    assert z == x * n_state - y_base * minimum
                    assert w == x * minimum - y_base * n_state
                    assert z + w == d0 * (minimum + n_state)
                    assert z - w == (x + y_base) * carry
                    u = power * d0 * minimum + x * contact
                    v = d0 * minimum - Fraction(y_base, power) * contact
                    assert u == power * z + x * theta
                    assert v == w - Fraction(y_base, power) * theta
                    negative_theta += theta < 0
                    positive_theta += theta > 0
                    checks += 1

assert checks > 0 and negative_theta > 0 and positive_theta > 0

# Exact regression for the unbounded word-level height counterfamily.
height_checks = 0
for ell in range(2, 30):
    for a in range(ell + 1, 2 * ell):
        word = (1,) * (2 * ell) + (0,) * (2 * a - 2 * ell)
        prefix = 0
        for phase in range(2 * a + 1):
            assert a * prefix - ell * phase >= 0
            if phase < 2 * a:
                prefix += word[phase]
        cut = a + ell
        u = tuple(word[(cut + phase) % (2 * a)] for phase in range(a))
        v = tuple(word[(cut + a + phase) % (2 * a)] for phase in range(a))
        assert u == (0,) * (a - ell) + (1,) * ell
        assert v == (1,) * ell + (0,) * (a - ell)
        lead = sum(v[:a - ell]) - sum(u[:a - ell])
        assert lead == min(a - ell, ell)
        height_checks += 1

print("RL320 late-row bounded-surrogate regression: PASS")
print(f"surrogate_checks={checks}")
print(f"negative_theta_cases={negative_theta}")
print(f"positive_theta_cases={positive_theta}")
print(f"unbounded_height_family_checks={height_checks}")
print("exact_first_survivor_bound=Delta>2^-41: PASS")
print("analytic_conclusion=positive balanced surrogate with |c|<=2^35")
print("scope=regression evidence plus exact log certificate; ownership remains open")
