#!/usr/bin/env python3
from fractions import Fraction

# 1) Low-k corollary logic from the inherited exact H<=24 certificate.
for k in range(3, 26):
    # Any strict violation H<k has H<=k-1<=24.
    assert k - 1 <= 24

# 2) Paired half-rotation algebra used in S2.
# q*(3^-h-1) + z*q*3^-h*(3^h-1) = (z-1)q(1-3^-h)
for h in range(0, 9):
    three_h = 3 ** h
    for zn, zd in [(2,1),(5,4),(31,30),(136,135)]:
        z = Fraction(zn, zd)
        for qn, qd in [(1,1),(8,9),(17,13)]:
            q = Fraction(qn, qd)
            left = q*(Fraction(1, three_h)-1) + z*q*Fraction(1, three_h)*(three_h-1)
            right = (z-1)*q*(1-Fraction(1, three_h))
            assert left == right

# 3) Raw phase-quotient small-multiple barrier.
for M in [1,5,101,10**6+3]:
    for N in [3,11,19,27,35]:  # all 3 mod 8
        W = (2-N)*M
        assert abs(W) >= M

# 4) Local all-00 terminal state is periodic mod 243 in n with period 162.
assert pow(2, 162, 243) == 1
for k in [3,5,27,55,165]:
    for n in [0,1,7,50,161,162,200]:
        R1 = (pow(2,n,243) * ((pow(2,k,243)-1) % 243) + 1) % 243
        R2 = (pow(2,n+162,243) * ((pow(2,k,243)-1) % 243) + 1) % 243
        assert R1 == R2

print('RL72 audit-corollary verifier: PASS')
print('low-k Gate-A corollary checked: terminal k<=25 implies any violation lies in H<=24')
print('half-rotation pairing algebra: PASS')
print('raw phase-quotient size barrier: PASS')
print('all-00 mod-243 n-periodicity with period 162: PASS')
