#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from itertools import product

R0 = 1 << 71
P0 = 123_139_092_617_126_647_266
Q0 = 77_692_117_359_936_589_403
QMAX = 93_226_756_704_262_400_759
NMAX = 2_578_333_030_765_879_156_036
SIGMA0 = 32_245_142_102_746_531_540
DELTA0 = 13_201_833_154_443_526_323

# Exact rational atanh-series log intervals, same method as the audited RL73/RL49 verifier.
def log_interval_int(x: int, terms: int = 260):
    y = Fraction(x - 1, x + 1)
    y2 = y * y
    s = Fraction(0)
    yp = y
    for n in range(terms):
        s += yp / (2*n + 1)
        yp *= y2
    lo = 2*s
    tail = 2*yp / ((2*terms + 1)*(1-y2))
    return lo, lo + tail

def linform_interval(p, q, l2, u2, l3, u3):
    return p*l2 - q*u3, p*u2 - q*l3

def Q(word):
    P = 1
    R = 1
    C = 0
    for b in word:
        if b == 0:
            P *= 2
        else:
            C = 3*C + P
            R *= 3
            P *= 2
    return C

def shortcut_step(x):
    if x & 1:
        return 1, (3*x + 1)//2
    return 0, x//2

# 1. Exact segment product identity on actual legal shortcut trajectories.
segment_checks = 0
for X in range(1, 181):
    x = X
    bits = []
    odd_prod = Fraction(1)
    for n in range(1, 13):
        b, y = shortcut_step(x)
        bits.append(b)
        if b:
            odd_prod *= Fraction(3*x + 1, 3*x)
        x = y
        s = sum(bits)
        rhs = Fraction(2**n, 3**s) * Fraction(x, X)
        assert odd_prod == rhs
        segment_checks += 1

# 2. Universal Q(y) >= 3^r - 2^r on bounded words.
qy_checks = 0
for n in range(0, 11):
    for w in product((0,1), repeat=n):
        r = sum(w)
        assert Q(w) >= 3**r - 2**r
        qy_checks += 1

# 3. Pump-coordinate unimodularity, inverse, gcd preservation and zeta identity.
coord_checks = 0
for ell in range(1, 60):
    for a in range(1, 120):
        Sigma = 2*ell - a
        Delta = 2*a - 3*ell
        assert 3*Sigma + 2*Delta == a
        assert 2*Sigma + Delta == ell
        assert gcd(abs(Sigma), abs(Delta)) == gcd(a, ell)
        # Exact rational identity works for arbitrary integral exponents; handle negatives explicitly.
        def qpow(fr, e):
            return fr**e if e >= 0 else Fraction(1,1)/(fr**(-e))
        lhs = Fraction(2**a, 3**ell)
        rhs = qpow(Fraction(8,9), Sigma) * qpow(Fraction(4,3), Delta)
        assert lhs == rhs
        coord_checks += 1
assert 3*SIGMA0 + 2*DELTA0 == P0
assert 2*SIGMA0 + DELTA0 == Q0
assert gcd(SIGMA0, DELTA0) == 1

# 4. Exact closed-pump product-excess formulas on canonical pumps.
pump_checks = 0
for q in range(1, 9):
    for m in range(1, 13):
        # c=10 on the v/B half: fixed point alpha=1.
        x = 1 + 3*(4**q)*m
        y = 1 + 3*(3**q)*m
        prod_seg = Fraction(4,3)**q * Fraction(y, x)
        assert prod_seg - 1 == (Fraction(4,3)**q - 1) / x
        # Direct trajectory is legal and has word (10)^q.
        z = x
        bits=[]
        pdir=Fraction(1)
        for _ in range(2*q):
            b,z2=shortcut_step(z); bits.append(b)
            if b: pdir *= Fraction(3*z+1,3*z)
            z=z2
        assert bits == [1,0]*q and z == y and pdir == prod_seg
        pump_checks += 1

        # c=101: fixed point alpha=-7.
        x2 = -7 + 3*(8**q)*m
        y2 = -7 + 3*(9**q)*m
        assert x2 > 0 and y2 > 0
        prod2 = Fraction(8,9)**q * Fraction(y2, x2)
        assert prod2 - 1 == Fraction(7, x2) * (1 - Fraction(8,9)**q)
        z=x2; bits=[]; pdir=Fraction(1)
        for _ in range(3*q):
            b,z2=shortcut_step(z); bits.append(b)
            if b: pdir *= Fraction(3*z+1,3*z)
            z=z2
        assert bits == [1,0,1]*q and z == y2 and pdir == prod2
        pump_checks += 1

# 5. Formal canonical-prefix product stress identity.
prefix_checks = 0
for N in [19, 43, 67, R0 + ((19-R0) % 24), R0 + 10_000 + ((19-(R0+10_000)) % 24)]:
    assert N % 24 == 19
    x111 = Fraction(27*N + 127, 8)
    pi111 = Fraction(1) + Fraction(19, 27*(N+4))
    assert pi111 == Fraction(8,27) * x111 / (N+4)
    for p in range(0, 14):
        pump = Fraction(1) + Fraction(7,1) * (1-Fraction(8,9)**p) / x111
        total = pi111 * pump
        claimed = Fraction(1) + (Fraction(75,1)-Fraction(56,1)*Fraction(8,9)**p) / (27*(N+4))
        assert total == claimed
        prefix_checks += 1

# 6. Exact rational-log certificate inherited in method from RL73/RL49.
l2,u2 = log_interval_int(2)
l3,u3 = log_interval_int(3)
lam_lo, lam_hi = linform_interval(P0,Q0,l2,u2,l3,u3)
assert lam_lo > 0
B = Fraction(79, 9*(R0-2))
# Proves lambda0 < B < 2 lambda0, hence any full-phase multiple g*lambda0 < B has g=1.
assert lam_hi < B
assert B < 2*lam_lo

# Reproduce the RL73 universal denominator gate exactly.
Qmax_frac = l2/(2*B)
assert Qmax_frac.numerator // Qmax_frac.denominator == QMAX

# Rigorous interval for 2+79/(9 lambda0): both interval endpoints have the same integer floor.
Nu_lo = Fraction(2) + Fraction(79,9) / lam_hi
Nu_hi = Fraction(2) + Fraction(79,9) / lam_lo
assert Nu_lo.numerator // Nu_lo.denominator == NMAX
assert Nu_hi.numerator // Nu_hi.denominator == NMAX

print('RL77 product/CF/scale verifier: PASS')
print('segment product checks =', segment_checks)
print('Q(y) lower-bound checks =', qy_checks)
print('pump-coordinate checks =', coord_checks)
print('canonical pump-product checks =', pump_checks)
print('canonical-prefix stress checks =', prefix_checks)
print('RL73 survivor p0 =', P0)
print('RL73 survivor q0 =', Q0)
print('universal reduced-denominator gate =', QMAX)
print('first-branch gcd forced = 1')
print('first-branch N upper endpoint =', NMAX)
print('Sigma0 =', SIGMA0)
print('Delta0 =', DELTA0)
