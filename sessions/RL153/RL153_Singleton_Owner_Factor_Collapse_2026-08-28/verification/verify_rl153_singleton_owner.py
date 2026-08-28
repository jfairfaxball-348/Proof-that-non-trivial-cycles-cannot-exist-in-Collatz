#!/usr/bin/env python3
"""Exact algebra checks for RL153's singleton factor-collapse reduction."""

from fractions import Fraction

def factor(x, y, g):
    return sum(x**t * y**(g - 1 - t) for t in range(g))

# The polynomial factorization used in the repeated-block ownership route.
for x, y in [(2, 3), (5, 2), (11, 7)]:
    for g in range(1, 8):
        f = factor(x, y, g)
        assert x**g - y**g == (x - y)*f
    assert factor(x, y, 1) == 1

# Check the defect-level numerator identity on small exact profiles.  It is
# an integer identity; it is not a model or construction of a Collatz cycle.
def check_profile(a, l, h):
    assert len(h) == l + 1 and h[0] == h[-1] == 0
    b = [(a*j)//l for j in range(l + 1)]
    assert all(0 <= h[j] <= b[j] for j in range(l + 1))
    H = max(h)
    B = [3**(l - 1 - j)*2**b[j] for j in range(l)]
    qh = sum(B[j] // (2**h[j]) for j in range(l))
    qc = sum(B)
    rhs = qc
    for ell in range(1, H + 1):
        r = sum(B[j] for j in range(l) if h[j] < ell)
        rhs += (2**(H - ell))*r
    assert (2**H)*qh == rhs
    # The original one-block modulus is odd, so multiplying by 2^H cannot
    # change divisibility by it.
    modulus = 2**a - 3**l
    assert modulus % 2
    assert (qh % modulus == 0) == (rhs % modulus == 0)

check_profile(5, 3, [0, 0, 1, 0])
check_profile(7, 4, [0, 0, 1, 1, 0])
check_profile(8, 5, [0, 0, 1, 2, 1, 0])

print("RL153 singleton-owner verifier: PASS")
print("repeated_block_factor_F1=1")
print("singleton_contact_divisibility=tautological")
print("residual_condition=full_ordinary_modulus_X_minus_Y")
print("scope=analytic reduction/method barrier; no g=1 exclusion")

