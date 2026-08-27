#!/usr/bin/env python3
from fractions import Fraction

LO, HI = 13, 40
EXPECTED_LIMIT = 30_400_121
EXPECTED_WORST = (39, 23)

def D(L,Z):
    return 2**(L+Z) - 3**L

def q_upper(L,Z):
    # Universal transition-root bound: start with 1, end with >=1 zero.
    return 2**(Z-1) * (3**L - 2**L)

def z_min(L):
    z=1
    while D(L,z) <= 0:
        z += 1
    return z

rows=[]
worst=None
for L in range(LO, HI+1):
    z=z_min(L)
    assert D(L,z-1) < 0 < D(L,z)
    r=Fraction(q_upper(L,z), D(L,z))
    floor=r.numerator//r.denominator
    rows.append((L,z,floor))
    if worst is None or r>worst[0]:
        worst=(r,L,z,floor)

    # Exact discrete monotonicity identity for R(Z)=q_upper/D.
    # Cross multiplication shows R(Z+1)<R(Z) whenever D(Z)>0.
    for zz in range(z,z+8):
        assert q_upper(L,zz+1)*D(L,zz) < q_upper(L,zz)*D(L,zz+1)

assert (worst[1],worst[2]) == EXPECTED_WORST
assert worst[3] == EXPECTED_LIMIT
print('RL129 quotient-bound verifier: PASS')
print(f'L range={LO}..{HI}')
print(f'global_integer_quotient_limit={EXPECTED_LIMIT} worst_L={worst[1]} worst_Z={worst[2]}')
for L,z,m in rows:
    print(f'L={L} positivity_Z={z} quotient_floor={m}')
