#!/usr/bin/env python3
from fractions import Fraction

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
M_FLOOR = 1 << 71
QMAX = 3_182_833_229

assert D == 80_448_749_305

# Exact atanh-series enclosure inherited from RL322/RL323.
def ln_ratio_interval(x, terms=280):
    x2 = x * x
    term = x
    total = Fraction(0)
    for k in range(terms):
        total += term / (2 * k + 1)
        term *= x2
    lo = 2 * total
    tail = 2 * term / (2 * terms + 1) / (1 - x2)
    return lo, lo + tail

ln2_lo, ln2_hi = ln_ratio_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_ratio_interval(Fraction(1, 2))
Delta_lo = A * ln2_lo - ELL * ln3_hi
Delta_hi = A * ln2_hi - ELL * ln3_lo

assert 0 < Delta_lo < Delta_hi < Fraction(1, 1 << 40)

# Frozen RL323 boundary.
rhs_qmax = Fraction(2 * QMAX, 3) * (1 + Fraction(1, 1 << 34)) + 1
lhs_floor = Delta_lo * M_FLOOR
assert lhs_floor > rhs_qmax

# RL324 lower-side adjacent prefix: rigorous worst-case loss < (X/Y)/3
# and frozen X/Y < 1 + 2^-40.
loss_cap = (1 + Fraction(1, 1 << 40)) / 3
margin = lhs_floor - loss_cap - rhs_qmax
assert margin > 0

qmin = QMAX + 1
rmax = D - qmin
assert qmin == 3_182_833_230
assert rmax == 77_265_916_075

# Small exhaustive regression for the valid interior matched-defect recurrence.
# Odd states P,Q take exact odd-to-odd gaps a,b where divisibility holds.
def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

rec_cases = 0
for P in range(1, 400, 2):
    a = v2(3 * P + 1)
    P1 = (3 * P + 1) >> a
    for Q in range(1, 400, 2):
        b = v2(3 * Q + 1)
        Q1 = (3 * Q + 1) >> b
        for d in range(0, 9):
            Delta = (1 << d) * P - Q
            d1 = d + a - b
            if d1 < 0:
                continue
            Delta1 = (1 << d1) * P1 - Q1
            assert (1 << b) * Delta1 == 3 * Delta + (1 << d) - 1
            if Delta > 0:
                assert Delta1 > 0
            rec_cases += 1

# Unit-minus-one orientation from positive small defect.
orient_cases = 0
for d in range(1, 12):
    cell = 1 << d
    for P in range(1, 100, 2):
        for nu in range(1, cell):
            Q = cell * P - nu
            assert Q // cell == P - 1
            assert Q % cell == cell - nu
            orient_cases += 1

# Exact local propagation barrier family.
barrier_cases = 0
for a in range(2, 25):
    mod = 1 << (a + 1)
    # Find the unique odd residue class modulo 2^(a+1) with exact valuation a.
    residue = None
    for P in range(1, mod, 2):
        if v2(3 * P + 1) == a:
            residue = P
            break
    assert residue is not None
    # Take a large representative so all local states are positive and large.
    P = residue + 1000 * mod
    assert v2(3 * P + 1) == a
    Q = 8 * P - 1
    assert Q & 1
    assert v2(3 * Q + 1) == 1
    P1 = (3 * P + 1) >> a
    Q1 = (3 * Q + 1) >> 1
    d1 = a + 2
    Delta1 = (1 << d1) * P1 - Q1
    assert Delta1 == 5
    assert Q1 // (1 << d1) == P1 - 1
    barrier_cases += 1

print("RL324_PARENT_BRIDGE_VERIFIER_GREEN")
print("delta_times_2^71_lower_gt", float(lhs_floor))
print("old_q_boundary_margin_gt", float(lhs_floor - rhs_qmax))
print("new_lower_side_margin_gt", float(margin))
print("q_min", qmin)
print("matched_rank_r_max", rmax)
print("interior_recurrence_cases", rec_cases)
print("unit_minus_one_orientation_cases", orient_cases)
print("local_barrier_cases", barrier_cases)
print("scope", "analytic structure + exact rational first-survivor boundary; local loops regression only")
