#!/usr/bin/env python3
"""Regression checks for the RL312 balanced Radius-2 checkpoint.

The analytic proof is in
RL312_BALANCED_RETURN_RADIUS2_EXCLUSION_AND_NORMALIZATION_REPAIR.md.
This verifier stress-tests the purely combinatorial structural lemma on all
binary words through length 14 and audits the tiny A<=5 primitive full-D scope.
It does not replace the all-scale analytic proof.
"""
from itertools import product
from math import gcd


def primitive(w):
    n = len(w)
    return all(tuple(w) != tuple(w[k:] + w[:k]) for k in range(1, n))


def standard_Q(w):
    L = sum(w)
    P = 0
    Q = 0
    for i, b in enumerate(w):
        if b:
            Q += (1 << i) * 3 ** (L - 1 - P)
            P += 1
    return Q


def canonical_flow(w, s):
    A = len(w)
    L = sum(w)
    assert (s * L) % A == 0
    p = s * L // A
    windows = [sum(w[(i + t) % A] for t in range(s)) for i in range(A)]
    f = [p - z for z in windows]
    assert sum(f) == 0
    for i in range(A):
        assert f[(i + 1) % A] - f[i] == w[i] - w[(i + s) % A]
    return f


def cyclic_radius_from_canonical_flow(f):
    # All cyclic flows are f+c.  An integer median minimizes the L1 norm.
    vals = sorted(f)
    med = vals[(len(vals) - 1) // 2]
    return sum(abs(x - med) for x in f)


# Exhaustive structural stress test.  Every balanced exact-Radius-2 example
# must have singleton +1/-1 defects and satisfy rL=A(n+1), hence
# r=t*a and n+1=t*ell.
checked = 0
for A in range(3, 15):
    for bits in product((0, 1), repeat=A):
        w = list(bits)
        L = sum(w)
        if L in (0, A):
            continue
        for s in range(1, A):
            if (s * L) % A:
                continue
            f = canonical_flow(w, s)
            if cyclic_radius_from_canonical_flow(f) != 2:
                continue

            # Since A>=3, a radius-2 optimum cannot use a nonzero constant
            # shift: A|c| <= 2 forces c=0.
            assert sum(abs(x) for x in f) == 2
            assert f.count(1) == 1
            assert f.count(-1) == 1
            assert all(x in (-1, 0, 1) for x in f)

            u = f.index(1)
            v = f.index(-1)
            r = (v - u) % A
            assert 1 <= r < A
            n = sum(w[(u + t) % A] for t in range(r))
            assert r * L == A * (n + 1)

            g = gcd(A, L)
            a = A // g
            ell = L // g
            assert gcd(a, ell) == 1
            assert r % a == 0
            t = r // a
            assert 1 <= t < g
            assert n + 1 == t * ell

            X = 1 << a
            Y = 3 ** ell
            # If D>0, the proper difference forced by the analytic full-D
            # argument is strictly smaller than D.
            if X > Y:
                D = X**g - Y**g
                local = X**t - Y**t
                assert 0 < local < D
            checked += 1

assert checked > 1000

# Tiny-period scope audit: there is no primitive positive full-D word at
# A<=5.  This is only a regression guard for low-shell wording.
tiny_hits = []
for A in range(1, 6):
    for bits in product((0, 1), repeat=A):
        w = list(bits)
        L = sum(w)
        if L == 0 or not primitive(w):
            continue
        D = (1 << A) - 3**L
        if D <= 1:
            continue
        Q = standard_Q(w)
        if Q % D == 0:
            tiny_hits.append((A, L, bits, D, Q // D))
assert tiny_hits == []

print(f"RL312 balanced Radius-2 regression verifier: PASS ({checked} structural cases)")
