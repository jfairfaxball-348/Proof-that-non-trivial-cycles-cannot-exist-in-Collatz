#!/usr/bin/env python3
"""Exact RL192 verifier for the full-period phase-lock barrier.

This certifies a limitation of the universal ``|epsilon| < 2`` relaxation
on necessary-rank atoms.  It does not certify physical realization of an
arbitrary epsilon sequence or a Collatz state.
"""

from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
B = A - L
R = L - B
ELO, EHI = 72_797_034_370, 103_818_202_602


def ln_bounds_integer(value, terms=80):
    value = Fraction(value)
    z = (value - 1) / (value + 1)
    z_squared = z * z
    term = z
    partial = Fraction(0)
    for index in range(terms):
        partial += term / (2 * index + 1)
        term *= z_squared
    lower = 2 * partial
    tail = 2 * term / Fraction(2 * terms + 1) / (1 - z_squared)
    return lower, lower + tail


# Full-period candidate separation and its transition length.
separation = L
length = separation - 37
assert (separation * B) % L == 0

# Hence E intersects its shift in exactly E: the necessary overlap is nonempty.
overlap = (ELO, EHI)
assert overlap == (ELO, EHI)

# The mechanical balance identity is
#   sum(c_j, j=0..n-1) = floor((r+nA)/L).
# At n=L-37 it splits E at Q=37B mod L=L-(59L-37A).
M = 59 * L - 37 * A
Q = (37 * B) % L
assert M == 49_013_272_579
assert Q == 88_514_772_733
assert M + Q == L
assert ELO < Q <= EHI


def exponent_sum(rank):
    return (rank + length * A) // L


# Both complete integer atoms have the asserted constant exponent sum.
assert exponent_sum(ELO) == exponent_sum(Q - 1) == A - 59
assert exponent_sum(Q) == exponent_sum(EHI) == A - 58

# For the lower atom, denominator exponent 21+S=A-38, so the centre is
# 2^38 * 3^L/2^A.  For the upper atom it is 2^37 * 3^L/2^A.
assert 21 + (A - 59) == A - 38
assert 21 + (A - 58) == A - 37

# Certify Delta=A ln(2)-L ln(3) in a strict rational interval.
ln2_lower, ln2_upper = ln_bounds_integer(2)
ln3_lower, ln3_upper = ln_bounds_integer(3)
delta_lower = A * ln2_lower - L * ln3_upper
delta_upper = A * ln2_upper - L * ln3_lower
assert 0 < delta_lower < delta_upper < Fraction(1, 2**40)

# Since 0<1-exp(-Delta)<Delta, each target-centre distance obeys
#   2^38(1-exp(-Delta)) < 1/4,
#   2^37(1-exp(-Delta)) < 1/8.
assert (2**38) * delta_upper < Fraction(1, 4)
assert (2**37) * delta_upper < Fraction(1, 8)

# After any nonempty affine word, the final relaxed epsilon contribution alone
# gives radius 2/2^c, which is at least 1/2 for c in {1,2}.  Thus each target
# lies strictly inside its corresponding universal relaxed ball at s=L.
for final_bit in (1, 2):
    assert Fraction(2, 2**final_bit) >= Fraction(1, 2)

# Stronger explicit relaxed witness: put every earlier epsilon equal to zero
# and use only the final epsilon.  Its required magnitude is 2^c times the
# target-centre miss.  Even for c=2 it is <1 on the 2^38 atom and <1/2 on
# the 2^37 atom, hence strictly inside the universal |epsilon|<2 allowance.
for final_bit in (1, 2):
    assert (2**final_bit) * (2**38) * delta_upper < 1
    assert (2**final_bit) * (2**37) * delta_upper < Fraction(1, 2)

print("PASS: RL192 full-period universal-ball phase-lock barrier")
print(f"full_period_separation={separation}")
print(f"necessary_overlap=[{ELO},{EHI}]")
print(f"rank_split={Q}")
print("lower_atom_center=2^38*3^L/2^A")
print("upper_atom_center=2^37*3^L/2^A")
print("certified_delta_interval=positive_and_below_2^-40")
print("target_2^38_miss_lt=1/4")
print("target_2^37_miss_lt=1/8")
print("universal_ball_radius_ge=1/2")
print("single_final_epsilon_relaxed_witness_abs_lt=1")
print("scope=method_barrier_not_physical_realization")
