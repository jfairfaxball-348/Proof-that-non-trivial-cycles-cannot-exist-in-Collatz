#!/usr/bin/env python3
"""Exact checks for RL156's state/Bézout notation repair."""

from math import gcd

def check(A, L, h):
    assert gcd(A, L) == 1 and len(h) == L + 1
    D = 2**A - 3**L
    # u, unlike the physical least state M, is solely a Bezout coefficient.
    p = pow(A, -1, L)
    u = (A*p - 1)//L
    assert A*p - u*L == 1
    rho = (pow(2, u, D) * pow(pow(3, p, D), -1, D)) % D
    assert pow(rho, L, D) == pow(2, -1, D)
    b = [(A*j)//L for j in range(L + 1)]
    S = [b[j] - h[j] for j in range(L + 1)]
    assert all(S[j + 1] - S[j] >= 1 for j in range(L))
    Q = sum(3**(L - 1 - j) * 2**S[j] for j in range(L))
    phase = sum(pow(rho, A*j - L*S[j], D) for j in range(L)) % D
    assert (Q % D == 0) == (phase == 0)
    H = max(h)
    coefficients = [0] * L
    for j in range(L):
        r = (A*j) % L
        assert A*j - L*S[j] == r + L*h[j]
        coefficients[r] += 2**h[j] * 3**(H-h[j])
    assert all(c > 0 for c in coefficients)

check(5, 3, [0, 0, 1, 0])
check(7, 4, [0, 0, 1, 1, 0])
print("RL156 state/Bezout notation repair: PASS")
print("least_state_symbol=M; bezout_symbol=u; Ap-uL=1")
print("full_modulus_phase_numerator_equivalence=PASS")
print("scope=notation repair; no singleton exclusion")
