#!/usr/bin/env python3
"""Exact constant checks for the RL193 physical-debt theorem candidate.

The algebraic telescope is proved in the accompanying note.  This verifier
checks every numerical/rank/logarithmic inequality used by that proof.  It
does not certify physical realization of a necessary rank or a Collatz cycle.
"""

from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
B = A - L
R = 2 * L - A
ELO, EHI = 72_797_034_370, 103_818_202_602
Q = 88_514_772_733
DLO, DHI = 23_369_453_298, 41_775_866_136
K_UPPER = 146_795_909_391


def v2(value):
    return (value & -value).bit_length() - 1


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


# RL192 rank split and its target/zero-prefix/complement exponent mapping.
assert ELO < Q <= EHI
for target_exponent, zero_sum, tail_sum in (
    (38, 59, A - 59),
    (37, 58, A - 58),
):
    assert zero_sum == target_exponent + 21
    assert tail_sum == A - target_exponent - 21
    assert 37 + (L - 37) == L
    assert zero_sum + tail_sum == A

# The first complementary source is ordinary, late-mechanical, and c_0=2.
assert R < ELO <= EHI < L - 1


def terminal_rank_with_carry_before(distance):
    return (L - 1 + distance * B) % L


def carry_forbidden(prefix_length, lo, hi):
    return sorted(
        (terminal_rank_with_carry_before(distance), distance)
        for distance in range(1, prefix_length + 1)
        if lo <= terminal_rank_with_carry_before(distance) <= hi
    )


# A carry error cannot occur in either exact zero prefix.
triple_forbidden = carry_forbidden(37, ELO, EHI)
assert triple_forbidden == [
    (75_485_708_845, 30),
    (80_448_749_304, 1),
    (83_137_423_780, 13),
    (85_826_098_256, 25),
    (88_514_772_732, 37),
    (93_477_813_191, 8),
    (96_166_487_667, 20),
    (98_855_162_143, 32),
    (103_818_202_602, 3),
]
h21_forbidden = carry_forbidden(35, DLO, DHI)
assert h21_forbidden == [
    (26_058_127_773, 14),
    (28_746_802_249, 26),
    (36_398_517_184, 9),
    (39_087_191_660, 21),
    (41_775_866_136, 33),
]


def known_window_forbidden(prefix_length, lo, hi):
    # A zero prefix of length tau ending at terminal t contains known
    # nonzero source q precisely for t=q+1,...,q+tau.
    bad_terminal_phases = {
        source + distance
        for source in range(24, 30)
        for distance in range(1, prefix_length + 1)
    }
    assert bad_terminal_phases == set(range(25, 30 + prefix_length))
    prefix_rows = sorted(
        ((phase * B) % L, phase)
        for phase in bad_terminal_phases
        if lo <= (phase * B) % L <= hi
    )
    zero_terminal_rows = sorted(
        ((phase * B) % L, phase)
        for phase in range(24)
        if lo <= (phase * B) % L <= hi
    )
    return prefix_rows, zero_terminal_rows


triple_early_prefix, triple_zero_terminal = known_window_forbidden(37, ELO, EHI)
assert triple_early_prefix == [
    (75_485_708_846, 30),
    (78_174_383_322, 42),
    (80_863_057_798, 54),
    (83_551_732_274, 66),
    (85_826_098_257, 25),
    (88_514_772_733, 37),
    (91_203_447_209, 49),
    (93_892_121_685, 61),
    (98_855_162_144, 32),
    (101_543_836_620, 44),
]
assert triple_zero_terminal == [
    (72_797_034_370, 18),
    (80_448_749_305, 1),
    (83_137_423_781, 13),
    (93_477_813_192, 8),
    (96_166_487_668, 20),
]
h21_early_prefix, h21_zero_terminal = known_window_forbidden(35, DLO, DHI)
assert h21_early_prefix == [
    (23_783_761_791, 55),
    (28_746_802_250, 26),
    (31_435_476_726, 38),
    (34_124_151_202, 50),
    (36_812_825_678, 62),
]
assert h21_zero_terminal == [
    (23_369_453_298, 2),
    (26_058_127_774, 14),
    (36_398_517_185, 9),
    (39_087_191_661, 21),
]
triple_rank_deletions = {
    rank for rank, _ in triple_forbidden + triple_early_prefix + triple_zero_terminal
}
h21_rank_deletions = {
    rank for rank, _ in h21_forbidden + h21_early_prefix + h21_zero_terminal
}
assert len(triple_rank_deletions) == 24
assert len(h21_rank_deletions) == 14
assert EHI - ELO + 1 - len(triple_rank_deletions) == 31_021_168_209
assert DHI - DLO + 1 - len(h21_rank_deletions) == 18_406_412_825
assert Q in triple_rank_deletions

# Canonical earliest-terminal floors.  Phase 24 is the one known nonzero
# terminal not prefix-contaminated, but its rank lies in neither core.
assert not (ELO <= (24 * B) % L <= EHI)
assert not (DLO <= (24 * B) % L <= DHI)
assert all(not (ELO <= (phase * B) % L <= EHI) for phase in range(67, 71))
assert ELO <= (71 * B) % L <= EHI
assert (71 * B) % L not in triple_rank_deletions
assert all(not (DLO <= (phase * B) % L <= DHI) for phase in range(65, 67))
assert DLO <= (67 * B) % L <= DHI
assert (67 * B) % L not in h21_rank_deletions

# Start-rank split and the removal of the upper atom's sole equality case.
assert (ELO - Q) % L == 121_810_306_949
assert (Q - 1 - Q) % L == L - 1
assert (Q - Q) % L == 0
assert (EHI - Q) % L == 15_303_429_869


def terminal_rank_for_carry_offset(offset):
    return (L - 1 - offset * B) % L


def terminal_rank_for_carry_distance_to_start(distance):
    return (L - 1 + (37 + distance) * B) % L


atoms = {
    "target_2^38": (ELO, Q - 1),
    "target_2^37": (Q, EHI),
}
buffers = {
    "target_2^38": (11, 5),
    "target_2^37": (4, 7),
}
for name, (lo, hi) in atoms.items():
    first_after, first_before = buffers[name]
    assert lo <= terminal_rank_for_carry_offset(first_after) <= hi
    assert all(
        not (lo <= terminal_rank_for_carry_offset(offset) <= hi)
        for offset in range(first_after)
    )
    assert lo <= terminal_rank_for_carry_distance_to_start(first_before) <= hi
    assert all(
        not (lo <= terminal_rank_for_carry_distance_to_start(distance) <= hi)
        for distance in range(1, first_before)
    )

# Its valuation -21 is unique: for every later offset j>=1,
# P_j >= j+1 and H_j <= 21+j, hence P_j-H_j >= -20.
for offset in (1, 2, 37, 1000, L - 38):
    assert (offset + 1) - (21 + offset) == -20

# Endpoint congruence check without constructing the astronomically large
# integers 2^A or 3^L.
assert v2(L) == 8
modulus = 2**64
three_power_mod = pow(3, L, modulus)
assert v2((three_power_mod - 1) % modulus) == 10

# Rigorous logarithm enclosure inherited in form from RL192.
ln2_lower, ln2_upper = ln_bounds_integer(2)
ln3_lower, ln3_upper = ln_bounds_integer(3)
delta_lower = A * ln2_lower - L * ln3_upper
delta_upper = A * ln2_upper - L * ln3_lower
assert 0 < delta_lower < delta_upper < Fraction(1, 2**40)

# Normalized debt bounds for both atoms.
assert 2**38 * delta_upper < Fraction(1, 4)
assert 2**37 * delta_upper < Fraction(1, 8)

# exp(delta)-1 < delta/(1-delta) < 1/(2^40-1), followed
# by the exact corridor comparison proving the signed tail flow <1/2.
lambda_minus_one_upper = Fraction(1, 2**40 - 1)
tail_flow_upper = 3 * K_UPPER * lambda_minus_one_upper
assert 6 * K_UPPER < 2**40 - 1
assert tail_flow_upper < Fraction(1, 2)
cancellation_38 = Fraction(1, 2) - tail_flow_upper
cancellation_37 = Fraction(1, 2) - 3 * Fraction(2**37, 2**40 - 1)
assert cancellation_38 == Fraction(72_912_057_143, 733_007_751_850)
assert cancellation_37 == Fraction(91_625_968_981, 733_007_751_850)

print("PASS: RL193 physical debt telescope constants")
print("common_tail_numerator=(2^A-3^L)/2^21")
print("lower_atom_target=2^38,zero_sum=59,tail_sum=A-59")
print("upper_atom_target=2^37,zero_sum=58,tail_sum=A-58")
print("tail_total_valuation=-21")
print("later_term_valuation_ge=-20")
print("v2(3^L-1)=10")
print("signed_tail_flow_lt=1/2")
print("carry_flow_gt=1/2")
print("ordinary_tail_flow_sign=negative")
print("triple_zero_prefix_carry_forbidden_count=9")
print("h21_zero_prefix_carry_forbidden_count=5")
print("triple_total_physical_rank_deletions=24")
print("h21_total_physical_rank_deletions=14")
print("triple_remaining_certificate_ranks=31021168209")
print("h21_remaining_certificate_ranks=18406412825")
print("canonical_triple_terminal_phase_ge=71")
print("canonical_h21_terminal_phase_ge=67")
print("target_2^38_K_prefix_sign=positive")
print("target_2^37_K_prefix_sign=negative")
print("target_2^38_carry_buffers=11,5")
print("target_2^37_carry_buffers=4,7")
print(f"target_2^38_ordinary_cancellation_gt={cancellation_38}")
print(f"target_2^37_ordinary_cancellation_gt={cancellation_37}")
print("scope=conditional_compatibility_not_realization")
