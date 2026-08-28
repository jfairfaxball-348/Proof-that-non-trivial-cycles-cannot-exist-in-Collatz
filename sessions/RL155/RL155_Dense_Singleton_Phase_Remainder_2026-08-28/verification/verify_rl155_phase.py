#!/usr/bin/env python3
"""Exact toy checks for the RL155 full-modulus singleton phase identity."""

from math import gcd

def check(a, l, h):
    assert gcd(a, l) == 1 and len(h) == l + 1 and h[0] == h[-1] == 0
    x, y, d = 2**a, 3**l, 2**a - 3**l
    # Find Ap-mL=1.
    p = pow(a, -1, l)
    m = (a*p - 1)//l
    assert a*p - m*l == 1
    rho = (pow(2, m, d) * pow(pow(3, p, d), -1, d)) % d
    b = [(a*j)//l for j in range(l + 1)]
    s = [b[j] - h[j] for j in range(l + 1)]
    assert all(s[j + 1] - s[j] >= 1 for j in range(l))
    q = sum(3**(l - 1 - j)*2**s[j] for j in range(l))
    phase = sum(pow(rho, a*j - l*s[j], d) for j in range(l)) % d
    assert (q % d == 0) == (phase == 0)
    for j in range(l):
        r = (a*j) % l
        assert a*j - l*s[j] == r + l*h[j]
    # Reducing modulo 3*T^l-2 produces one positive coefficient at each
    # residue r=Aj mod l; coprimality prevents inter-phase collisions.
    H = max(h)
    coeff = [0]*l
    for j in range(l):
        coeff[(a*j) % l] += (2**h[j])*(3**(H-h[j]))
    assert all(c > 0 for c in coeff)

check(5, 3, [0, 0, 1, 0])
check(7, 4, [0, 0, 1, 1, 0])
print("RL155 singleton full-modulus phase identity: PASS")
print("phase_exponent=Aj-LS_j=(Aj mod L)+Lh_j")
print("binomial_remainder_has_one_strictly_positive_coefficient_per_residue=PASS")
print("scope=exact algebraic reduction; no cycle exclusion")
