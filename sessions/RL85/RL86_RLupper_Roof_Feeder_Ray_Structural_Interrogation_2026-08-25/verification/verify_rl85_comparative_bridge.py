#!/usr/bin/env python3
"""Fast exact arithmetic guard for RL85.

The analytic proofs are in RL85_RLSHARP_RLFLAT_COMPARATIVE_BRIDGE_AND_FIRST_FAREY_PHYSICAL_SCALE.md.
This script checks only finite arithmetic/transcription consequences.
"""

P = 114_208_327_604
Q = 72_057_431_991
E = P - Q
C = 200_000_000_000
UCONST = 2 * C  # 400,000,000,000
Z = 40_249_491_324_522_944

# First-Farey exponent compression.
H = (3 * Q + 7) // 8
ZEROS = Q - H
assert H == 27_021_536_997
assert ZEROS == 45_035_894_994
assert Q - H == (5 * Q) // 8

# Finite rational threshold used in 400e9*(3/2)^q < 3^H.
assert pow(256, 513) > UCONST * pow(243, 513)
a, r = divmod(Q, 8)
assert a >= 513
assert pow(2, r) >= pow(3, (5 * r) // 8)

# The physical maximum bound is below one full even cylinder modulus.
assert 2**39 > C
assert Q >= 39

# General synchronized-return span: n+1 < 8H/5.
B = (8 * H - 1) // 5 - 1
assert B == 43_234_459_194

# Canonical pump corollaries.
R10 = B // 2
assert R10 == 21_617_229_597
R101_GENERAL = B // 3
assert R101_GENERAL == 14_411_486_398
R101_STRONG = (H - 1) // 2
assert R101_STRONG == 13_510_768_498

# RL73 giant-macro intersection packing count.
DISTINCT = Z // (B + 1) + 1
assert DISTINCT == 930_959

# RL82 maximum residue classes -> immediate predecessor classes.
M_CLASSES = (26, 80, 152)
P_CLASSES = tuple(((2 * m - 1) // 3) % 108 for m in M_CLASSES)
assert P_CLASSES == (17, 53, 101)
assert all(x % 3 == 2 for x in P_CLASSES)
assert all((4 * m - 2) // 3 > m for m in M_CLASSES)  # even inverse 2P exceeds roof residue representative

# Elementary inequalities used analytically.
assert 3**5 < 2**8

print("RL85 comparative-bridge verifier: PASS")
print(f"first Farey pair = ({P}, {Q})")
print(f"e = {E}")
print(f"h = {H}")
print(f"forced leading ternary zeros = {ZEROS}")
print(f"closed quotient return span <= {B}")
print(f"c=10 repeat depth <= {R10}")
print(f"c=101 repeat depth <= {R101_STRONG} (strong endpoint bound)")
print(f"RL73 intersection spaced-distinct J count >= {DISTINCT}")
print(f"roof predecessor classes mod108 = {P_CLASSES}")
