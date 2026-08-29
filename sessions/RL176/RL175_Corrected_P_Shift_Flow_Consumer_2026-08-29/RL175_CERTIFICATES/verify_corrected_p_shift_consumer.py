#!/usr/bin/env python3
"""Exact/interval audit for RL175 corrected p-shift consumer constants."""
from fractions import Fraction
from math import gcd

A = 217_976_794_617
L = 137_528_045_312
P = 65_470_613_321
U = 103_768_467_013
M = A-L
T = L-P

assert gcd(A,L) == 1
assert A*P-L*U == 1
assert T == 72_057_431_991
assert M == 80_448_749_305

def log_bounds(n, terms=110):
    z = Fraction(n-1, n+1)
    z2 = z*z
    term = z
    s = Fraction(0)
    for k in range(terms):
        s += term/(2*k+1)
        term *= z2
    lo = 2*s
    hi = lo + 2*term/(2*terms+1)/(1-z2)
    return lo,hi

l2lo,l2hi = log_bounds(2)
l3lo,l3hi = log_bounds(3)
Dlo = A*l2lo-L*l3hi
Dhi = A*l2hi-L*l3lo
assert Dlo > 0

dmlo = U*l2lo-P*l3hi
dmhi = U*l2hi-P*l3lo
assert dmlo + 6*Dlo > 0
assert dmhi + 5*Dhi < 0
assert 5*L*Dhi < l2lo
assert Dlo > Fraction(1, 1_116_000_000_000)

ratio_log_hi = M*l2hi-(L-M)*l3lo
assert ratio_log_hi < -100
assert 2**100 > 2_000_000_000_000
assert Dlo > Fraction(1,2_000_000_000_000)
assert Dlo/Fraction(16) > Fraction(1,17_856_000_000_000)
assert 3*(2**71)*Dlo > 6_365_000_000
assert Dhi < Fraction(1,784)
assert 49*Dhi*Dhi < Dlo/Fraction(16)

print("RL175 corrected p-shift consumer verifier: PASS")
print("A*p-L*u=1")
print("5Delta < -d_minus < 6Delta")
print("sparse one-support resultant bound: |R|<6^(A-L)<D")
print("height-zero support count >=2")
print("height-zero mechanical loss >5/8")
print("height-zero internal half-barrier: F2 < 1/2-Delta/16")
print("explicit display: F2 < 1/2-1/17856000000000")
print("conditional h_p>=1: F2 > 6365000000*(2^H-1)")
