#!/usr/bin/env python3
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
p = 65_470_613_321
u = 103_768_467_013

assert A*p - L*u == 1
assert p + 37 < L

# Inherited certified premise:
# Delta > 1 / 1_116_000_000_000.
# Since exp(Delta)-1 > Delta and F2 < 1/2,
# g_p < 1/(6 Delta) < 1_116_000_000_000 / 6.
gap_strict_upper = Fraction(1_116_000_000_000, 6)
assert gap_strict_upper == 186_000_000_000
assert gap_strict_upper < 2**38

# New internal lattice 4 | g_p.
max_gap = int(gap_strict_upper) - 4
assert max_gap == 185_999_999_996
assert max_gap % 4 == 0
assert max_gap // 4 == 46_499_999_999

# High valuation branches.
assert 2**36 < gap_strict_upper
assert 3 * 2**36 > gap_strict_upper
assert 2**37 < gap_strict_upper
assert 3 * 2**37 > gap_strict_upper

# External-assisted transform:
# 3*2^71*Delta > 6,365,000,000 and s>5 Delta imply
# g_p > 5*2^71*Delta > 31,825,000,000 / 3.
external_strict_lower = Fraction(31_825_000_000, 3)
first_integer = external_strict_lower.numerator // external_strict_lower.denominator + 1
external_min_multiple4 = ((first_integer + 3) // 4) * 4
assert external_min_multiple4 == 10_608_333_336
assert external_min_multiple4 % 4 == 0
assert external_min_multiple4 <= max_gap

print("PASS: RL176 integer p-gap arithmetic checks completed successfully.")
print(f"A={A}")
print(f"L={L}")
print(f"p={p}")
print(f"u={u}")
print(f"Ap-uL={A*p-L*u}")
print(f"g_p strict upper < {int(gap_strict_upper):,}")
print(f"4-lattice maximum = {max_gap:,}")
print(f"first mismatch must occur by J=36 because g_p < 2^38")
print(f"external-assisted 4-lattice minimum = {external_min_multiple4:,}")
