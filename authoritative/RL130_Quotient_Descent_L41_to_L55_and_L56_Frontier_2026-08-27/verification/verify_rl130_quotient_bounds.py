#!/usr/bin/env python3
from fractions import Fraction

LO, HI = 41, 55
EXPECTED_LIMIT = 6_496_657_853
EXPECTED_WORST = (54, 32)


def D(L, Z):
    return 2 ** (L + Z) - 3 ** L


def q_upper(L, Z):
    return 2 ** (Z - 1) * (3 ** L - 2 ** L)


def z_min(L):
    Z = 1
    while D(L, Z) <= 0:
        Z += 1
    return Z


rows = []
worst = None
for L in range(LO, HI + 1):
    Z = z_min(L)
    assert D(L, Z - 1) < 0 < D(L, Z)
    ratio = Fraction(q_upper(L, Z), D(L, Z))
    ceiling = ratio.numerator // ratio.denominator
    rows.append((L, Z, ceiling))
    if worst is None or ratio > worst[0]:
        worst = (ratio, L, Z, ceiling)
    # Exact cross-multiplied discrete monotonicity in the positive-D tail.
    for z in range(Z, Z + 16):
        assert q_upper(L, z + 1) * D(L, z) < q_upper(L, z) * D(L, z + 1)

assert (worst[1], worst[2]) == EXPECTED_WORST
assert worst[3] == EXPECTED_LIMIT
print('RL130 quotient-bound verifier: PASS')
print(f'L range={LO}..{HI}')
print(f'global_integer_quotient_limit={EXPECTED_LIMIT} worst_L={worst[1]} worst_Z={worst[2]}')
for L, Z, ceiling in rows:
    print(f'L={L} positivity_Z={Z} quotient_floor={ceiling}')
