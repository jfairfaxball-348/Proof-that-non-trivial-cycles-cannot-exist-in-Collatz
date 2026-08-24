#!/usr/bin/env python3
"""Exact arithmetic verifier for the RL49 strengthened phase-resonance exclusion.

What is machine-checked here:
  * rigorous rational intervals for ln 2 and ln 3;
  * the strengthened external prefix floor R_ext = 4*3^44+2;
  * the corresponding phase bound C/R_ext, C=398/45;
  * the rigorous Legendre gate and absence of surviving above-beta convergents below it;
  * the exact c_41,c_42,c_43 continued-fraction data;
  * c_41's positive linear form is already larger than the phase bound;
  * c_41 and c_42 are Farey neighbours and c_43=c_41+c_42.

The final extension from the Legendre gate up to denominator q_43 uses the elementary
Farey-neighbour lemma stated/proved in the companion markdown note.
"""
from fractions import Fraction

C = Fraction(398, 45)
R_EXT = 4 * 3**44 + 2


def log_interval_int(x: int, terms: int = 340):
    """Rigorous atanh-series interval for log(x), x a positive integer."""
    y = Fraction(x - 1, x + 1)
    y2 = y * y
    s = Fraction(0)
    yp = y
    for n in range(terms):
        s += yp / (2 * n + 1)
        yp *= y2
    lo = 2 * s
    tail = 2 * yp / ((2 * terms + 1) * (1 - y2))
    return lo, lo + tail


def ratio_interval(nlo, nhi, dlo, dhi):
    assert 0 < dlo <= dhi
    return nlo / dhi, nhi / dlo


def cf_prefix_interval(lo, hi, max_terms=100):
    out = []
    for _ in range(max_terms):
        a_lo = lo.numerator // lo.denominator
        a_hi = hi.numerator // hi.denominator
        if a_lo != a_hi:
            break
        a = a_lo
        out.append(a)
        lo2 = lo - a
        hi2 = hi - a
        if lo2 <= 0:
            break
        lo, hi = 1 / hi2, 1 / lo2
    return out


def convergents(cf):
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    for i, a in enumerate(cf):
        p = a * pm1 + pm2
        q = a * qm1 + qm2
        yield i, p, q
        pm2, pm1 = pm1, p
        qm2, qm1 = qm1, q


def linform_interval(p, q, l2, u2, l3, u3):
    # p ln2 - q ln3
    return p * l2 - q * u3, p * u2 - q * l3


l2, u2 = log_interval_int(2)
l3, u3 = log_interval_int(3)
blo, bhi = ratio_interval(l3, u3, l2, u2)
cf = cf_prefix_interval(blo, bhi, 100)
assert len(cf) >= 45, len(cf)

phase_bound = C / R_EXT
legendre_floor = Fraction(R_EXT, 1) * l2 / (2 * C)
Q_LEG = legendre_floor.numerator // legendre_floor.denominator
assert Q_LEG == 154_354_788_168_703_375_435, Q_LEG

conv = {i: (p, q, *linform_interval(p, q, l2, u2, l3, u3))
        for i, p, q in convergents(cf)}

# No above-beta convergent at or below the rigorous Legendre gate can meet
# log(zeta) < zeta-1 < C/R_EXT.
survivors = []
for i, (p, q, dlo, dhi) in conv.items():
    if q <= Q_LEG and dlo > 0 and dlo < phase_bound:
        survivors.append((i, p, q, dlo, dhi))
assert survivors == [], [(i, q) for i, _, q, _, _ in survivors]

# Exact relevant convergents.
p41, q41, d41lo, d41hi = conv[41]
p42, q42, d42lo, d42hi = conv[42]
p43, q43, d43lo, d43hi = conv[43]

assert (p41, q41) == (
    123_139_092_617_126_647_266,
    77_692_117_359_936_589_403,
)
assert (p42, q42) == (
    202_780_263_237_295_321_099,
    127_940_101_513_462_006_853,
)
assert (p43, q43) == (
    325_919_355_854_421_968_365,
    205_632_218_873_398_596_256,
)

# c41 is above beta, c42 below beta, c43 above beta.
assert d41lo > 0
assert d42hi < 0
assert d43lo > 0

# Crucial strengthened-floor exclusion of the formerly surviving c41.
assert d41lo > phase_bound

# Farey-neighbour structure and next upper convergent.
assert abs(p41 * q42 - p42 * q41) == 1
assert p43 == p41 + p42
assert q43 == q41 + q42
assert Q_LEG > q42
assert Q_LEG < q43

# q43 itself is NOT excluded by this phase bound; it is the next live spine point.
assert d43hi < phase_bound

print('RL49 strengthened phase/Farey verifier: PASS')
print('R_ext = 4*3^44+2 =', R_EXT)
print('phase bound C/R_ext =', phase_bound)
print('rigorous Legendre gate Q_LEG =', Q_LEG)
print('no surviving above-beta convergent at q <= Q_LEG')
print('c41 linear-form lower bound exceeds phase bound: PASS')
print('Farey neighbours c41/c42 and c43=c41+c42: PASS')
print('therefore companion lemma excludes every ell < q43')
print('new denominator floor ell >=', q43)
print('next live pair a,ell,q =', p43, q43, p43-q43)
