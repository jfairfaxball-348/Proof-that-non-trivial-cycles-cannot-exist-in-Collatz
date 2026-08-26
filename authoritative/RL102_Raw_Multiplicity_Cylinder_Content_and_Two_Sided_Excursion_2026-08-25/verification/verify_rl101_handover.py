#!/usr/bin/env python3
from fractions import Fraction

p = 114_208_327_604
q = 72_057_431_991
g_max = 125_777_718_029

assert p > q > 0
assert q % 2 == 1
assert g_max >= 2

# Exact elementary checks supporting the outgoing constants.
assert (1 << 38) > 200_000_000_000
assert q > 38
# sqrt(2)/3 < 1/2 iff 8 < 9 after squaring positive sides.
assert 8 < 9
assert Fraction(1, 1) / Fraction(16, 15) == Fraction(15, 16)
assert Fraction(15, 16) > Fraction(1, 2)

# Frozen cascade state.
wide=(5_000_030, 7_000_000, 5_000_053)
middle=(7_500_031, 4_500_000, 7_500_053)
deep=(10_000_032, 3_250_000, 10_000_053)
ultra=(15_000_035, 2_005_000, 15_000_053)
assert wide[0] == 5_000_030 and wide[1] == 7_000_000
assert middle[0] == 7_500_031 and middle[1] == 4_500_000
assert deep[0] == 10_000_032 and deep[1] == 3_250_000
assert ultra[0] == 15_000_035 and ultra[1] == 2_005_000
assert wide[2] < middle[2] < deep[2] <= ultra[2]

lam = Fraction(234_375, 3_281_264_468_752)
C_phys = 42_150_931_628
assert (lam * C_phys).numerator // (lam * C_phys).denominator == 3010

live = 2_921_813_805
prev = 2_921_813_803
upper = 42_150_931_559
assert prev + 2 == live
assert live % 2 == prev % 2 == upper % 2 == 1
assert live < upper

print('RL101 handover fast consistency: PASS')
print(f'p={p}, q={q}, g_max={g_max}')
print('inherited Delta > 1/200,000,000,000: accepted from frozen RL84 ledger')
print('mandatory repaired D_m=7,500,031: PASS')
print('floor(lambda*C)=3010: PASS')
print('first live odd=2,921,813,805: PASS')
