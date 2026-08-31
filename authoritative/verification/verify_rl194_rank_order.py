#!/usr/bin/env python3
"""RL194 exact canonical rank/K-order necessary-state checks."""

from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
B = A - L
Q = 88_514_772_733
P = 65_470_613_321
Z = L - P
K0 = 2**37
K_LOWER = 128_081_997_553
K_UPPER = 146_795_909_391
E_LOWER = 72_797_034_370
E_UPPER = 103_818_202_602
NEW_LOWER = 75_446_746_413
NEW_UPPER = 102_504_571_503


def log_bounds(value, terms=80):
    value = Fraction(value)
    assert value >= 1
    z = (value - 1) / (value + 1)
    z2 = z * z
    term = z
    partial = Fraction(0)
    for index in range(terms):
        partial += term / (2 * index + 1)
        term *= z2
    lower = 2 * partial
    tail = 2 * term / ((2 * terms + 1) * (1 - z2))
    return lower, lower + tail


def floor(value):
    return value.numerator // value.denominator


ln2_lo, ln2_hi = log_bounds(2)
ln3_lo, ln3_hi = log_bounds(3)
delta_lo = A * ln2_lo - L * ln3_hi
delta_hi = A * ln2_hi - L * ln3_lo
assert 0 < delta_lo < delta_hi < Fraction(1, 2**40)
assert ln2_lo > Fraction(2, 3)
assert Fraction(L - 1, 2**40) < Fraction(1, 6)
assert ln2_lo - (L - 1) * delta_hi > Fraction(1, 2)
assert (A * P - 1) % L == 0
assert (B * P) % L == 1
assert (Z * B) % L == L - 1

# If r<s, (s-r)ln2 + (i-j)delta > (s-r)/2 for canonical
# phases i,j; no enumeration of L phases is used or required.

lo_log_lo, lo_log_hi = log_bounds(Fraction(K_UPPER, K0))
hi_log_lo, hi_log_hi = log_bounds(Fraction(K0, K_LOWER))

# Uniform enclosing intervals for the real terminal-rank corridor cuts,
# including the full canonical phase correction 0<=a<L.
lower_cut_lo = Q - L * lo_log_hi / ln2_lo
lower_cut_hi = Q - L * lo_log_lo / ln2_hi + (L - 1) * delta_hi / ln2_lo
upper_cut_lo = Q + L * hi_log_lo / ln2_hi
upper_cut_hi = Q + L * hi_log_hi / ln2_lo + (L - 1) * delta_hi / ln2_lo

assert floor(lower_cut_lo) == floor(lower_cut_hi) == NEW_LOWER - 1
assert floor(upper_cut_lo) == NEW_UPPER - 1
assert floor(upper_cut_hi) == NEW_UPPER


def start_phase(terminal_rank):
    return ((terminal_rank - Q) * P) % L


def scaled_log_k_over_k0_bounds(terminal_rank):
    """Bounds on L*log(F(r)/K0), not on log(F(r)/K0)."""
    coefficient = Q - terminal_rank
    phase = start_phase(terminal_rank)
    if coefficient >= 0:
        return (
            coefficient * ln2_lo + phase * delta_lo,
            coefficient * ln2_hi + phase * delta_hi,
        )
    return (
        coefficient * ln2_hi + phase * delta_lo,
        coefficient * ln2_lo + phase * delta_hi,
    )


def scaled_log_k_over_upper_bounds(terminal_rank):
    lo, hi = scaled_log_k_over_k0_bounds(terminal_rank)
    return lo - L * lo_log_hi, hi - L * lo_log_lo


def scaled_log_k_over_lower_bounds(terminal_rank):
    lo, hi = scaled_log_k_over_k0_bounds(terminal_rank)
    return lo + L * hi_log_lo, hi + L * hi_log_hi


# Four exact endpoint tests, with rational margins.  The analytic rank-order
# theorem supplies the gap-free coverage of the entire rank interval.
endpoint_rows = (
    (NEW_LOWER - 1, 76_452_012_903, 'upper', Fraction(1, 10), Fraction(3, 25)),
    (NEW_LOWER, 4_394_580_912, 'upper', -Fraction(13, 20), -Fraction(16, 25)),
    (NEW_UPPER, 134_680_116_098, 'lower', Fraction(3, 40), Fraction(2, 25)),
    (NEW_UPPER + 1, 62_622_684_107, 'lower', -Fraction(69, 100), -Fraction(17, 25)),
)
for rank, phase, bound, rational_lo, rational_hi in endpoint_rows:
    assert start_phase(rank) == phase
    assert 0 <= phase <= L - 38
    enclosure = (
        scaled_log_k_over_upper_bounds(rank)
        if bound == 'upper'
        else scaled_log_k_over_lower_bounds(rank)
    )
    assert rational_lo < enclosure[0] < enclosure[1] < rational_hi

assert NEW_LOWER < Q - 2 < Q + 1 < NEW_UPPER

# Intersect the already certified RL193 deletions with the new corridor.
# Domains: every carry distance 1..37, known zero phase 0..23, and every
# terminal 25..66 whose 37-source prefix meets the known nonzero window.
carry_ranks = {(L - 1 + distance * B) % L for distance in range(1, 38)}
early_ranks = {(phase * B) % L for phase in range(25, 67)}
zero_ranks = {(phase * B) % L for phase in range(24)}
old_deletions = {
    rank for rank in carry_ranks | early_ranks | zero_ranks
    if E_LOWER <= rank <= E_UPPER
}
new_deletions = {rank for rank in old_deletions if NEW_LOWER <= rank <= NEW_UPPER}
assert len(old_deletions) == 24
assert len(new_deletions) == 22
assert old_deletions - new_deletions == {E_LOWER, E_UPPER}
assert NEW_UPPER - NEW_LOWER + 1 - len(new_deletions) == 27_057_825_069
assert (NEW_LOWER - E_LOWER) + (E_UPPER - NEW_UPPER) == 3_963_343_142
assert 31_021_168_209 - 27_057_825_069 == 3_963_343_140
assert Q - 1 in new_deletions and Q in new_deletions
assert Q - 2 not in new_deletions and Q + 1 not in new_deletions

# RL193 already rules out all canonical terminal phases below 71.  These
# complete added finite ranges sharpen the overall/atom-specific floors.
assert [(phase * B) % L for phase in (71, 72, 73)] == [
    73_211_342_863, 16_132_046_856, 96_580_796_161
]
assert all(not (NEW_LOWER <= (phase * B) % L <= NEW_UPPER) for phase in range(71, 73))
assert Q < (73 * B) % L <= NEW_UPPER
assert (73 * B) % L not in new_deletions
assert all(not (NEW_LOWER <= (phase * B) % L < Q) for phase in range(71, 78))
assert NEW_LOWER <= (78 * B) % L < Q
assert (78 * B) % L not in new_deletions

# Quantified chronological prefix signs.  Monotonicity means the closest
# not-yet-deleted ranks Q-2 and Q+1 supply uniform conditional bounds.
assert start_phase(Q - 2) == 6_586_818_670
assert start_phase(Q + 1) == P
x_lower = (2 * ln2_lo + start_phase(Q - 2) * delta_lo) / L
y_lower = (ln2_lo - P * delta_hi) / L
assert x_lower > 0 and y_lower > 0
assert 3 * K0 * x_lower > Fraction(417, 100)
assert 3 * K0 * y_lower / (1 + y_lower) > Fraction(19, 10)

# The inherited four carry buffers remain attained by necessary ranks after
# the contiguous corridor refinement (not a physical realization assertion).
for lo, hi, after, before in (
    (NEW_LOWER, Q - 2, 11, 5),
    (Q + 1, NEW_UPPER, 4, 7),
):
    assert all(not lo <= (L - 1 - distance * B) % L <= hi for distance in range(after))
    assert lo <= (L - 1 - after * B) % L <= hi
    assert (L - 1 - after * B) % L not in new_deletions
    assert all(not lo <= (L - 1 + (37 + distance) * B) % L <= hi for distance in range(1, before))
    assert lo <= (L - 1 + (37 + before) * B) % L <= hi
    assert (L - 1 + (37 + before) * B) % L not in new_deletions

print('PASS rank order: rho is strictly decreasing in canonical rank')
print('uniform_log_gap_gt=rank_difference/(2L)')
print('same_terminal_K_formula=2^37*exp(((Q-r)*ln2+a*delta)/L)')
print(f'exact_corridor_rank_core=[{NEW_LOWER},{NEW_UPPER}]')
print('endpoint_coverage=global_analytic_monotonicity_plus_four_exact_checks')
print('retained_inherited_rank_deletions=22')
print('corridor_only_certificate_rank_cardinality=27057825069')
print('additional_necessary_ranks_excluded_beyond_RL193=3963343140')
print('corridor_only_canonical_terminal_floor_overall_and_upper=73')
print('corridor_only_canonical_terminal_floor_lower=78')
print('lower_atom_prefix_flow_gt=417/100')
print('upper_atom_prefix_flow_lt=-19/10')
print('carry_buffers_unchanged=11/5,4/7')
print('scope=conditional_necessary_state_only; see separate weighted-speed refinement')
