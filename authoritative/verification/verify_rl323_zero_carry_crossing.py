#!/usr/bin/env python3
from fractions import Fraction

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
M_FLOOR = 1 << 71

assert D == 80_448_749_305

def T(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

# 1. Exhaustive small regression for the phase-aligned D recurrence.
case_count = 0
for c in range(0, 7):
    three = 3 ** c
    for U in range(1, 80):
        for V in range(1, 80):
            bu, bv = U & 1, V & 1
            # c is a prefix-count lead. The (1,0) case requires c>=1.
            if (bu, bv) == (1, 0) and c == 0:
                continue
            cp = c + bv - bu
            if cp < 0:
                continue
            D0 = three * U - V
            D1 = (3 ** cp) * T(U) - T(V)
            if (bu, bv) == (0, 0):
                rhs = Fraction(D0, 2)
            elif (bu, bv) == (1, 1):
                rhs = Fraction(3 * D0 + three - 1, 2)
            elif (bu, bv) == (0, 1):
                rhs = Fraction(3 * D0 - 1, 2)
            else:
                rhs = Fraction(D0 + 3 ** (c - 1), 2)
            assert D1 == rhs
            if D0 > 0:
                assert D1 > 0
            case_count += 1

# 2. First-crossing arithmetic: either possible crossing type forces
#    E=-D < 3^(h-1).
cross_count = 0
for h in range(1, 10):
    for E in range(0, 3 ** h + 3):
        D0 = -E
        d11 = Fraction(3 * D0 + 3 ** h - 1, 2)
        if d11 > 0:
            assert E < 3 ** (h - 1)
            cross_count += 1
        d10 = Fraction(D0 + 3 ** (h - 1), 2)
        if d10 > 0:
            assert E < 3 ** (h - 1)
            cross_count += 1

# 3. Exact rational enclosure for Delta = a log 2 - ell log 3,
#    matching the frozen RL322 method.
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

# 4. Growth-factor bound used in the zero-count argument:
# (1+1/(3m))^ell <= 1/(1-ell/(3m)) < 1+2^-34.
t = Fraction(ELL, 3 * M_FLOOR)
assert 0 < t < Fraction(1, (1 << 34) + 1)
assert Fraction(1, 1) / (1 - t) < 1 + Fraction(1, 1 << 34)

# 5. Exact boundary check for q.
# From (D0/Y)m > Delta*2^71 and
# (D0/Y)m < (2q/3)(1+2^-34)+1,
# exclude every q <= qmax by monotonicity.
qmax = 3_182_833_229
rhs_qmax = Fraction(2 * qmax, 3) * (1 + Fraction(1, 1 << 34)) + 1
lhs_floor = Delta_lo * M_FLOOR
assert lhs_floor > rhs_qmax

qmin = qmax + 1
rmax = D - qmin
assert qmin == 3_182_833_230
assert rmax == 77_265_916_075

print("RL323_ZERO_CARRY_VERIFIER_GREEN")
print("phase_aligned_recurrence_cases", case_count)
print("first_crossing_regression_cases", cross_count)
print("delta_times_2^71_lower_gt", float(lhs_floor))
print("q_min", qmin)
print("matched_rank_r_max", rmax)
print("unconditional_structure", "zero-carry; h>=2; J<3^(h-1); eta<2^r/3")
print("conditional_scope", "exact first external survivor + inherited m>=2^71")
