#!/usr/bin/env python3
"""Exact toy checks for RL157's corrected singleton phase polynomial."""
from math import gcd

def check(A, L, h):
    assert gcd(A, L) == 1 and h[0] == h[-1] == 0 and max(h) > 0
    D = 2**A - 3**L
    p = pow(A, -1, L)
    u = (A*p - 1)//L
    assert A*p-u*L == 1
    rho = pow(2, u, D) * pow(pow(3, p, D), -1, D) % D
    assert (2*pow(rho, L, D)-1) % D == 0
    b = [(A*j)//L for j in range(L+1)]
    S = [b[j]-h[j] for j in range(L+1)]
    assert all(S[j+1]-S[j] >= 1 for j in range(L))
    Q = sum(3**(L-1-j)*2**S[j] for j in range(L))
    raw = sum(pow(rho, A*j-L*S[j], D) for j in range(L)) % D
    H = max(h)
    coeff = [0]*L
    for j in range(L):
        r = (A*j) % L
        assert A*j-L*S[j] == r+L*h[j]
        coeff[r] += 2**(H-h[j])
    reduced = sum(coeff[r]*pow(rho, r, D) for r in range(L)) % D
    assert reduced == pow(2, H, D)*raw % D
    assert (Q % D == 0) == (raw == 0) == (reduced == 0)
    assert all(c > 0 for c in coeff) and gcd(*coeff) == 1 and 1 in coeff

check(5, 3, [0, 0, 1, 0])
check(7, 4, [0, 0, 1, 1, 0])
check(8, 5, [0, 0, 1, 1, 1, 0])
print("RL157 corrected phase normalization: PASS")
print("binomial=2T^L-1; dense_coefficient=2^(H-h_j)")
print("primitive_dense_remainder=PASS")
print("scope=necessary resultant target; no singleton exclusion")
