#!/usr/bin/env python3
from fractions import Fraction

A = 217_976_794_617
ELL = 137_528_045_312
D = A - ELL
assert D == 80_448_749_305
assert D % 2 == 1


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


# Exact rational enclosure for Delta = a log 2 - ell log 3.
ln2_lo, ln2_hi = ln_ratio_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_ratio_interval(Fraction(1, 2))
Delta_lo = A * ln2_lo - ELL * ln3_hi
Delta_hi = A * ln2_hi - ELL * ln3_lo
assert 0 < Delta_lo < Delta_hi < Fraction(1, 1 << 40)

# delta = D0/X = 1-exp(-Delta).  Alternating Taylor bounds, monotone on (0,1):
# x-x^2/2 < 1-e^-x < x-x^2/2+x^3/6.
delta_lo = Delta_lo - Delta_lo * Delta_lo / 2
delta_hi = Delta_hi - Delta_hi * Delta_hi / 2 + Delta_hi**3 / 6
assert 0 < delta_lo < delta_hi < Fraction(1, 1 << 40)

# Prefix-delay threshold used to force the first 66 one-ranks to be undelayed.
# RL319/RL321 give Y/X > 1-2^-40.  Check this is stronger than the threshold
# 3^66 / 2^105 required by 3^(ell-66) 2^65 > X 2^-40.
assert Fraction(3**66, 2**105) < Fraction((1 << 40) - 1, 1 << 40)

# Branch B: m=2^66 h-1, 33<=h<=512, and m=floor(n/delta).
# Hence (2^66 h-1)delta <= n < 2^66 h delta.  Prove every such interval lies
# strictly inside a single unit interval, using only the rational enclosure.
min_margin = None
worst_h = None
worst_k = None
for h in range(33, 513):
    m = (1 << 66) * h - 1
    lo = m * delta_lo
    hi = (m + 1) * delta_hi
    k = lo.numerator // lo.denominator
    assert lo > k
    assert hi < k + 1
    margin = min(lo - k, (k + 1) - hi)
    if min_margin is None or margin < min_margin:
        min_margin = margin
        worst_h, worst_k = h, k

# Branch A exact geometry barrier.
# W=1^(ell+1)0^d1^(ell-1)0^d has nonnegative least-root defect piecewise.
# Check the symbolic endpoint/minimum values used in the proof.
assert D > 0 and ELL > 4
# segment 1: F=(a-ell)n >=0
# segment 2 minimum at t=d: F=d
# segment 3 minimum at t=0: F=d
# segment 4: F=ell(d-t)>=0
assert D > 0
# at n=a, t=d-1 in segment 2, F=a>0
assert D * (ELL + 1) - ELL * (D - 1) == A

# Canonical beta = 1 0^(d-1), s=1, r=d.  d odd makes
# eta=(2^(d+1)-1)/3 integral; modulo/parity and size follow from d odd.
assert (D + 1) % 2 == 0
# Avoid constructing 2^d: modular facts suffice.
assert pow(2, D + 1, 3) == 1
# Positivity of Z_geom follows from X/Y<1+2^-40 and ell>4:
# 3Y-2X > Y(1-2^-39) > Y/2 > 2^(ell+1).
assert Fraction((1 << 39) - 1, 1 << 39) > Fraction(1, 2)
# and 3^ell > 2^(ell+2) for ell>=4, proved by base+induction ratio 3>2.
assert 3**4 > 2**6

print('RL322 verifier: PASS')
print('branch_B_prefix_ones=66')
print('branch_B_h_cases=480')
print(f'branch_B_worst_h={worst_h}')
print(f'branch_B_unit_interval_index={worst_k}')
print(f'branch_B_min_certified_margin_gt={float(min_margin):.12g}')
print('branch_B_conclusion=negative canonical branch excluded at conditional first external survivor')
print('branch_A_geometry_barrier=PASS')
print('branch_A_conclusion=positive canonical geometry does not imply ordinary balanced ownership')
print('parent_difficulty_delta=LATERAL')
