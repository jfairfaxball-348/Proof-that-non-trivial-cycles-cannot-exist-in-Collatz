from fractions import Fraction
from math import gcd

R0 = 1 << 71

# Rigorous logarithm intervals via ln z = 2*atanh((z-1)/(z+1)).
def ln_interval(x: Fraction, N: int = 240):
    x2 = x*x
    term = x
    s = Fraction(0)
    for k in range(N):
        s += term / (2*k + 1)
        term *= x2
    lo = 2*s
    tail = 2 * term / (2*N + 1) / (1 - x2)
    return lo, lo + tail

ln2_lo, ln2_hi = ln_interval(Fraction(1, 3))
ln3_lo, ln3_hi = ln_interval(Fraction(1, 2))
assert 0 < ln2_lo < ln2_hi
assert 0 < ln3_lo < ln3_hi

# RL20's last relevant upper convergent and the next lower convergent.
PU, QU = 10_439_860_591, 6_586_818_670
PL, QL = 103_768_467_013, 65_470_613_321
assert gcd(PU, QU) == gcd(PL, QL) == 1
assert PU*QL - PL*QU == 1  # Farey neighbors, U > L.

# Signs relative to beta=ln3/ln2.
delta_u_lo = PU*ln2_lo - QU*ln3_hi
delta_u_hi = PU*ln2_hi - QU*ln3_lo
delta_l_lo = PL*ln2_lo - QL*ln3_hi
delta_l_hi = PL*ln2_hi - QL*ln3_lo
assert delta_u_lo > 0
assert delta_l_hi < 0

# The upper neighbor lies strictly outside the product tube at R0.
assert delta_u_lo > Fraction(QU, 3*R0)

# First Farey mediant entering the product tube.
PS, QS = PU + PL, QU + QL
assert (PS, QS) == (114_208_327_604, 72_057_431_991)
assert gcd(PS, QS) == 1

delta_s_lo = PS*ln2_lo - QS*ln3_hi
delta_s_hi = PS*ln2_hi - QS*ln3_lo
assert delta_s_lo > 0
assert delta_s_hi <= Fraction(QS, 3*R0)

# It is also a genuine first-crossing count pair: (p-1)/q < beta < p/q.
assert (PS-1)*ln2_hi - QS*ln3_lo < 0
assert PS*ln2_lo - QS*ln3_hi > 0

# Exact floor of the threshold least-state value beyond which this first
# Farey survivor would itself be excluded: Rcrit = q/(3*delta_s).
# The delta interval is sufficiently tight to certify one integer floor.
rcrit_lo = Fraction(QS, 1) / (3*delta_s_hi)
rcrit_hi = Fraction(QS, 1) / (3*delta_s_lo)
rcrit_floor_lo = rcrit_lo.numerator // rcrit_lo.denominator
rcrit_floor_hi = rcrit_hi.numerator // rcrit_hi.denominator
assert rcrit_floor_lo == rcrit_floor_hi
RCRIT_FLOOR = rcrit_floor_lo
assert RCRIT_FLOOR == 4_358_487_209_795_430_953_242

# Shared local/global tube separation threshold floor: 3 R0 ln2.
thr_lo = 3*R0*ln2_lo
thr_hi = 3*R0*ln2_hi
thr_floor_lo = thr_lo.numerator // thr_lo.denominator
thr_floor_hi = thr_hi.numerator // thr_hi.denominator
assert thr_floor_lo == thr_floor_hi
TUBE_PRODUCT_FLOOR = thr_floor_lo
assert TUBE_PRODUCT_FLOOR == 4_909_942_519_757_819_773_358

# Algebra audit for the first-surplus fixed-count barrier:
# O^o E^e attains B=2^e(3^o-2^o), is prefix-balanced through j-1 whenever
# 2^(j-1)<=3^o<2^j, and its cylinder is M == -1 (mod 3^o).
# Check a representative finite range exactly; the proof in the note is symbolic.
barrier_checks = 0
for o in range(1, 400):
    # find first crossing j without floating point
    j = 1
    while not (pow(2, j) > pow(3, o)):
        j += 1
    if j <= o:
        continue
    e = j-o
    assert pow(2, j-1) <= pow(3, o) < pow(2, j)
    B = pow(2, e)*(pow(3, o)-pow(2, o))
    # O^o recurrence gives 3^o-2^o, then E^e doubles e times.
    b = 0
    oo = 0
    for _ in range(o):
        b = 2*b + pow(3, oo)
        oo += 1
    for _ in range(e):
        b *= 2
    assert b == B
    # Cylinder: 2^j M == B == -2^j mod 3^o.
    mod = pow(3, o)
    assert (B + pow(2, j)) % mod == 0
    # Proper-prefix balance for O^oE^e.
    for i in range(1, o+1):
        assert pow(2, i) <= pow(3, i)
    for r in range(1, e):
        assert pow(2, o+r) <= pow(3, o)
    barrier_checks += 1

print('RL83 segment-product/Farey-frontier verifier: PASS')
print('R0 =', R0)
print('Farey lower neighbor =', (PL, QL))
print('Farey upper neighbor =', (PU, QU))
print('first product-tube mediant =', (PS, QS))
print('balanced-prefix depth guaranteed through =', PS-1)
print('first-survivor R# upper-threshold floor =', RCRIT_FLOOR)
print('floor(3*R0*ln2) =', TUBE_PRODUCT_FLOOR)
print('fixed-count barrier spot checks =', barrier_checks)
