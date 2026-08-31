#!/usr/bin/env python3
"""Independent bounded RL194 weighted-speed replay; NOT PROMOTED.

Uses a different coarse filter, precision, exponent evaluation length and
mechanical digit implementation from the main scratch certificate.
"""

from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
B = A - L
P = 65_470_613_321
Z = L - P
Q = 88_514_772_733
K0 = 2**37
KLO = 128_081_997_553
ELO, EHI = 72_797_034_370, 103_818_202_602
NEWLO, NEWHI = 75_446_746_413, 102_504_571_503
END = 1_826_035
SCALE = 2**128
deletion_phases = set(range(24)) | set(range(25, 67))
known_deletions = {
    (phase * B) % L for phase in deletion_phases
} | {
    (L - 1 + distance * B) % L for distance in range(1, 38)
}
new_deletions = {rank for rank in known_deletions if NEWLO <= rank <= NEWHI}
assert len(new_deletions) == 22
assert (B * P) % L == 1  # the finite phase-to-rank map is injective


def log_enclosure(value):
    z = Fraction(value - 1, value + 1)
    series = Fraction(0)
    power = z
    for n in range(96):
        series += power / (2 * n + 1)
        power *= z * z
    return 2 * series, 2 * series + 2 * power / (193 * (1 - z * z))


ln2low, ln2high = log_enclosure(2)
ln3low, ln3high = log_enclosure(3)
dlow = A * ln2low - L * ln3high
dhigh = A * ln2high - L * ln3low
assert Fraction(2, 3) < ln2low
assert 0 < dlow < dhigh < Fraction(1, 2**40)
assert END + 37 < Z < L
assert 2 * K0 > L
assert 2 * KLO * 2**40 - 3 * KLO > L * 2**40


def exp_enclosure(value):
    assert 0 < value < 1
    partial = term = Fraction(1)
    for n in range(1, 11):
        term = term * value / n
        partial += term
    first_tail = term * value / 11
    return partial, partial + first_tail / (1 - value / 12)


def magnitude_enclosure(start, terminal_rank):
    distance = abs(terminal_rank - Q)
    if terminal_rank < Q:
        xlow = (distance * ln2low + start * dlow) / L
        xhigh = (distance * ln2high + start * dhigh) / L
        elow = exp_enclosure(xlow)[0]
        ehigh = exp_enclosure(xhigh)[1]
        return 3 * K0 * (elow - 1), 3 * K0 * (ehigh - 1)
    ylow = (distance * ln2low - start * dhigh) / L
    yhigh = (distance * ln2high - start * dlow) / L
    elow = exp_enclosure(ylow)[0]
    ehigh = exp_enclosure(yhigh)[1]
    return 3 * K0 * (1 - 1 / elow), 3 * K0 * (1 - 1 / ehigh)


rho_low = rho_high = SCALE
sum_low = {38: 0, 37: 0}
sum_high = {38: 0, 37: 0}
first = {}
exact_checks = []
eligible_counts = {37: 0, 38: 0}
survivor_counts = {37: 0, 38: 0}
survivors = []

for start in range(1, END + 1):
    source = start - 1
    # This rho is indexed by source, before the recurrence advance.
    if source >= 24:
        sum_low[37] += rho_low
        sum_high[37] += rho_high
    if source >= 29:
        sum_low[38] += rho_low
        sum_high[38] += rho_high
    digit = (A * start) // L - (A * source) // L
    assert digit in (1, 2)
    rho_low = (rho_low * 2**digit) // 3
    numerator = rho_high * 2**digit
    rho_high = -(-numerator // 3)
    assert rho_low <= rho_high

    terminal_rank = ((start + 37) * B) % L
    assert terminal_rank != Q  # only canonical start zero would give Q
    if not ELO <= terminal_rank <= EHI:
        continue
    atom = 38 if terminal_rank < Q else 37
    eligible = NEWLO <= terminal_rank <= NEWHI and terminal_rank not in new_deletions
    if eligible:
        eligible_counts[atom] += 1
    distance = abs(terminal_rank - Q)
    # Independent loose filter.  If distance>=start, both atom magnitudes
    # exceed start: lower by 2*K0/L>1, upper by
    # (2*KLO-3*KLO/2^40)/L>1.  Hence neither can meet |F|<start.
    if distance >= start:
        continue
    flow_low, flow_high = magnitude_enclosure(start, terminal_rank)
    cap_low = Fraction(sum_low[atom], SCALE)
    cap_high = Fraction(sum_high[atom], SCALE)
    assert flow_low >= cap_high or flow_high < cap_low
    compatible = flow_high < cap_low
    exact_checks.append((start, atom, compatible))
    if compatible and atom not in first:
        first[atom] = (start, terminal_rank)
    if compatible and eligible:
        survivor_counts[atom] += 1
        survivors.append((start, atom, terminal_rank))

assert first == {
    38: (190_537, 88_514_759_934),
    37: (1_826_035, 88_515_371_864),
}
assert first[38][0] + 37 == 190_574
assert first[37][0] + 37 == 1_826_072
assert eligible_counts == {37: 185_747, 38: 173_508}
assert survivor_counts == {37: 1, 38: 9}
rejected_counts = {atom: eligible_counts[atom] - survivor_counts[atom] for atom in (37, 38)}
assert rejected_counts == {37: 185_746, 38: 173_499}
assert sum(rejected_counts.values()) == 359_245
assert NEWHI - NEWLO + 1 - len(new_deletions) - sum(rejected_counts.values()) == 27_057_465_824
print('PASS independent weighted-speed replay')
print(f'complete_start_range=1..{END}')
print('independent_loose_filter=abs(terminal_rank-Q)<start')
print('rho_interval_precision_bits=128')
print('log_series_terms=96;exp_series_terms=10')
print(f'exact_candidate_comparisons={len(exact_checks)}')
print(f'first_weighted_compatible={first}')
print(f'exact_candidate_outcomes={exact_checks}')
print(f'eligible_counts={eligible_counts}')
print(f'survivor_counts={survivor_counts}')
print(f'additional_rejection_counts={rejected_counts}')
print(f'weighted_survivors={survivors}')
print('full_core_minus_finite_prefix_filter_cardinality=27057465824')
print('scope=necessary_weighted_speed_only_NOT_PROMOTED')
