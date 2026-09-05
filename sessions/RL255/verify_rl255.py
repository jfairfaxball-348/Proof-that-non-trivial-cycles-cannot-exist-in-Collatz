#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, floor, log2

def resonance(a, ell):
    p2 = 1 << a
    p3 = 3 ** ell
    return p2 > p3 and 15 * p2 * p2 < 16 * p3 * p3

def det_solutions(a, ell):
    g = gcd(a, ell)
    if 2 % g:
        return []
    aa = a // g
    ll = ell // g
    rhs = (-2) // g
    inv = pow(ll, -1, aa)
    q0 = (rhs * inv) % aa
    out = []
    for j in range(g):
        q = q0 + j * aa
        if 0 < q < a:
            r = (q * ell + 2) // a
            if a * r - q * ell == 2:
                out.append((q, r))
    return out

def tent_capacity(g):
    return ((g - 2) ** 2) // 4

def min_x_for_mass(b):
    x = 1
    while (x * x) // 4 < b + 2:
        x += 1
    return x

def capacity_a_min(b):
    return 3 * b + min_x_for_mass(b) - 1

def f(x):
    return ((x + 1) ** 2) // 4

for x in range(80):
    for y in range(80):
        assert f(x + y) >= f(x) + f(y)

assert capacity_a_min(260) == 812
assert capacity_a_min(355) == 1102
assert capacity_a_min(356) == 1105
assert tent_capacity(1100 - 3 * 354 + 3) >= 356
assert tent_capacity(1100 - 3 * 355 + 3) < 357

uniform = []
for a in range(1, 1101):
    emin = (94 * a + 148) // 149
    emax = (12 * a - 1) // 19
    for ell in range(max(1, emin), min(a - 1, emax) + 1):
        if not resonance(a, ell):
            continue
        z = a - ell
        if z < 287:
            continue
        for q, r in det_solutions(a, ell):
            B = q - r
            H = 19 * z - 7 * a
            n = 19 * B - 7 * q
            if H <= 0:
                continue
            halving = (H % 2 == 0 and n % 2 == 0)
            b = 260 if halving else 355
            if z < b + 27:
                continue
            if a < capacity_a_min(b):
                continue
            uniform.append((a, ell, z, q, r, H, n, b))

assert uniform == [(1100, 694, 406, 317, 200, 14, 4, 260)]

rho = log2(3)
phase_width = 0.5 * log2(16 / 15)
gap = 694 * (233 / 147 - rho) + 1 / 147
assert gap > phase_width
assert Fraction(1, 1) - Fraction(147, 233) == Fraction(86, 233)
assert 19 * Fraction(86, 233) - 7 == Fraction(3, 233)

def guaranteed_zeros(start, length):
    stop = start + length
    count = 0
    for i in range(-28, 0):
        if start <= i < stop:
            count += 1
    if start <= 2 < stop:
        count += 1
    return count

starts38 = list(range(-51, -13))
excesses = [guaranteed_zeros(s, 38) - 14 for s in starts38]
assert len(starts38) == 38
assert all(x > 0 for x in excesses)
assert sum(excesses) == 358
assert 358 - 2 == 356
assert 75 * Fraction(3, 233) < 1

prepack = []
postpack = []
for a in range(1, 1987):
    emin = (147 * a + 232) // 233
    emax = (12 * a - 1) // 19
    for ell in range(max(1, emin), min(a - 1, emax) + 1):
        if not resonance(a, ell):
            continue
        z = a - ell
        if z < 383:
            continue
        for q, r in det_solutions(a, ell):
            B = q - r
            H = 19 * z - 7 * a
            n = 19 * B - 7 * q
            if H <= 0 or (H % 2 == 0 and n % 2 == 0):
                continue
            if a < capacity_a_min(356):
                continue
            rec = (a, ell, z, q, r, H, n, a - 36 * H)
            prepack.append(rec)
            if a - 36 * H >= 3 * 356:
                postpack.append(rec)

assert len(prepack) == 14
assert postpack == [(1986, 1253, 733, 1352, 853, 25, 17, 1086)]

a, ell, z, q, r, H, n = 1100, 694, 406, 317, 200, 14, 4
B = q - r
K = H // 2
t = n // 2
assert K == 7 and t == 2
assert K * q == t * a + 19
assert K * B == t * z + 7
assert capacity_a_min(354) <= 1100
assert capacity_a_min(355) > 1100
assert 406 - 260 + 4 == 150

print("RL255 verifier: PASS")
