#!/usr/bin/env python3
from fractions import Fraction

A = 217_976_794_617
L = 137_528_045_312
G = 771_316_334_039
K = 2*L - A
R_HI = 99_205_514_478

assert L < A < 2*L
assert K == 57_079_296_007
# Mechanical c=1 symbols cannot be consecutive because (A-L)/L > 1/2.
assert 2*(A-L) > L
assert 3*(A-L) < 2*L
# There are actual c-pattern short gaps c=1,2,1 in one reduced block.
# With c2-runs of length one or two, their exact count is 5L-3A.
assert 5*L - 3*A == 33_709_842_709 > 0

# A local valid height-one transition across c=[1,2,1,2] can have
# h=[0,0,1,1,0], producing a=[1,1,1,3].  Thus height one permits
# three consecutive a=1 gaps (an ordinary odd run of length four).
c = [1,2,1,2]
h = [0,0,1,1,0]
a = [c[j] + h[j] - h[j+1] for j in range(4)]
assert a == [1,1,1,3]

# Explicit population mismatch: one odd run of length four contributes
# O2=3 two-odd starts but only one depth-(2,1) terminal CRT boundary.
odd_runs = [4]
O2 = sum(max(r-1, 0) for r in odd_runs)
C21 = sum(r >= 2 for r in odd_runs)
assert O2 == 3 and C21 == 1 and O2 != C21

# Exhaust the finite local transition possibilities proving no four
# consecutive a=1 gaps when c in {1,2}, c=1 never consecutive, h in {0,1},
# and all accelerated exponents are positive.
from itertools import product
for cs in product((1,2), repeat=4):
    if any(cs[i] == cs[i+1] == 1 for i in range(3)):
        continue
    for hs in product((0,1), repeat=5):
        aa = [cs[j] + hs[j] - hs[j+1] for j in range(4)]
        if min(aa) >= 1:
            assert aa != [1,1,1,1]

# Log enclosure: atanh series gives ln 2 from x=1/3 and ln 3 from x=1/2.
def log_interval(x, N=260):
    x2 = x*x
    t = x
    s = Fraction()
    for k in range(N):
        s += t/(2*k+1)
        t *= x2
    lo = 2*s
    hi = lo + 2*t/(2*N+1)/(1-x2)
    return lo, hi

l2_lo, l2_hi = log_interval(Fraction(1,3))
l3_lo, l3_hi = log_interval(Fraction(1,2))
d_lo = A*l2_lo - L*l3_hi
d_hi = A*l2_hi - L*l3_lo
assert d_lo > 0
assert G*d_hi < 1

# Favorable carried RL137 state ceiling m < R/(3 Delta).
M = Fraction(R_HI, 1)/(3*d_lo)

def repaired_lower(g):
    return Fraction(162,13) * (g*K - 3)

def favorable_upper(g):
    return 6*M/(1-g*d_hi)

def ratio(g):
    return repaired_lower(g)/favorable_upper(g)

# After clearing positive constants, ratio is proportional to
# (g*K-3)(1-g*d_hi), a concave quadratic.  Its rational vertex is:
vertex = (K + 3*d_hi)/(2*K*d_hi)
g0 = vertex.numerator // vertex.denominator
candidates = sorted(set([1, G, max(1,min(G,g0)), max(1,min(G,g0+1))]))
best_g = max(candidates, key=ratio)
best = ratio(best_g)
assert best_g == 556_387_125_038
assert best < Fraction(896241, 1_000_000)
assert best < 1

# Diagnostic coefficient needed at the same best point.
current_coeff = Fraction(162,13)
required_coeff = current_coeff / best
assert required_coeff > Fraction(13904,1000)
assert required_coeff < Fraction(13905,1000)

print('RL144 run-fibre population repair: PASS')
print('best_g =', best_g)
print('best_ratio < 0.896241')
print('required coefficient in (13.904, 13.905)')
