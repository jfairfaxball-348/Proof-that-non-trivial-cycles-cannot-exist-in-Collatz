#!/usr/bin/env python3
"""Independent RL195 denominator audit on exactly the supplied toy domain.

NOT PROMOTED. Fixed points are solved by affine composition, independently
of the candidate's positive-window reconstruction. No actual phase scan.
"""

from fractions import Fraction as Q
from itertools import product
from math import gcd


def odd_denominator(x):
    d = x.denominator
    while d % 2 == 0:
        d //= 2
    return d


def verify(A, L, p, u, h):
    c = tuple(A * (i + 1) // L - A * i // L for i in range(L))
    a = tuple(c[i] + h[i] - h[(i + 1) % L] for i in range(L))
    assert min(a) >= 1 and sum(a) == A
    assert A * p - u * L == 1
    D, d = 2**A - 3**L, 3**p - 2**u
    assert D > 0 and gcd(D, 6) == gcd(D, d) == 1
    slope, intercept = Q(1), Q(0)
    for exponent in a:
        slope, intercept = 3 * slope / 2**exponent, (3 * intercept + 1) / 2**exponent
    assert 0 < slope < 1
    y0 = intercept / (1 - slope)
    y = [y0]
    for exponent in a:
        y.append((3 * y[-1] + 1) / 2**exponent)
    assert y[-1] == y0

    q0 = [Q(1)]
    for exponent in a:
        q0.append(q0[-1] * 2**exponent / 3)
    lam = Q(2**A, 3**L)
    alpha = Q(3**p, 2**u)
    beta = (alpha - 1) / (lam - 1)
    assert q0[-1] == lam

    def q(i):
        turns, phase = divmod(i, L)
        return lam**turns * q0[phase]

    def T(i):
        return q(i) * y[i % L]

    def rho(i):
        return Q(2 ** (A * i // L), 3**i)

    def arc(i, n):
        power, numerator = 0, 0
        for k in range(n):
            numerator = 3 * numerator + 2**power
            power += a[(i + k) % L]
        return power, numerator

    denominators = {yi.denominator for yi in y}
    assert len(denominators) == 1
    Dred = y0.denominator
    assert Dred & 1 and D % Dred == 0
    gaps, arcs = 0, 0
    for i in range(L):
        assert q(i) == rho(i) / 2**h[i]
        Yi = sum((q(i + j) for j in range(L)), Q(0))
        Ci = sum((q(i + j) for j in range(p)), Q(0))
        assert y[i] == Yi / (3 * (lam - 1) * q(i))
        K = alpha * T(i + p) - T(i)
        assert 3 * K == alpha * Ci + beta * Yi
        Delta = K / rho(i)
        _, Pi = arc(i, p)
        _, Ri = arc(i, L)
        assert Ri > 0 and Ri & 1 and y[i] == Q(Ri, D)
        assert D // gcd(D, Ri) == Dred
        assert gcd(D, d * Ri + Pi * D) == gcd(D, Ri)
        assert Delta == (d * y[i] + Pi) / 2 ** (u + h[i])
        target = (i + p) % L
        carry = A * (i + p) // L - A * i // L - u
        assert carry == int(i == L - p)
        assert Delta == Q(2**carry) * y[target] / 2**h[target] - y[i] / 2**h[i]
        assert odd_denominator(Delta) == Dred
        assert (odd_denominator(Delta) == 1) == (y[i].denominator == 1)
        if Dred == 1:
            assert y[i].numerator & 1
            value = 3 * y[i].numerator + 1
            assert value % 2 ** a[i] == 0
            assert (value // 2 ** a[i]) & 1
        for n in range(1, L + 1):
            power, Pn = arc(i, n)
            assert 2**power * y[(i + n) % L] == 3**n * y[i] + Pn
            assert 3 * (T(i + n) - T(i)) == sum((q(i + j) for j in range(n)), Q(0))
            arcs += 1
        gaps += 1
    return y0, alpha * T(p) - T(0), Dred, gaps, arcs


raw = 0
accepted = {}
for tail in product(range(4), repeat=4):
    raw += 1
    h = (0,) + tail
    c = (1, 2, 1, 2, 2)
    if any(c[i] + h[i] - h[(i + 1) % 5] < 1 for i in range(5)):
        continue
    accepted[h] = verify(8, 5, 2, 3, h)
expected_heights = {
    (0, 0, 0, 0, 0), (0, 0, 0, 0, 1),
    (0, 0, 1, 0, 0), (0, 0, 1, 0, 1),
    (0, 0, 1, 1, 0), (0, 0, 1, 1, 1), (0, 0, 1, 1, 2),
}
assert raw == 256 and set(accepted) == expected_heights
assert sum(row[3] for row in accepted.values()) == 35
assert sum(row[4] for row in accepted.values()) == 175
assert {row[2] for row in accepted.values()} == {13}
assert accepted[(0, 0, 0, 0, 0)][:2] == (Q(319, 13), Q(48, 13))
assert verify(2, 1, 1, 1, (0,)) == (Q(1), Q(1), 1, 1, 1)
print("PASS independent RL195 affine-composition reconstruction audit")
print("raw_arrays=256; exact_admissible_height_words=7; gaps=35; arcs=175")
print("common_odd_denominator=13 for all7 toys; trivial_integral_case=1")
print("all_zero_y0=319/13; all_zero_K0=48/13")
print("not_an_actual_constant_phase_scan_or_high_branch_realization")
