#!/usr/bin/env python3
from itertools import product
from fractions import Fraction


def v2(n):
    assert n != 0
    n = abs(n)
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def stats(w):
    n = len(w)
    s = sum(w)
    C = 0
    D = 0
    for r, x in enumerate(w):
        future = sum(w[r+1:])
        term = (1 << r) * (3 ** future)
        C += term
        if x == 0:
            D += term
    return n, s, C, D


def step(J, x):
    assert J & 1
    num = (3 ** x) * J + 1
    assert num % 2 == 0
    return num // 2


def simulate(J0, w):
    J = J0
    vals = [J]
    for x in w:
        assert J & 1, (J0, w, vals)
        J = step(J, x)
        vals.append(J)
    return vals


def selector(w, extra):
    # extra=1 selects first-even; extra=H+1 selects v2(exit)>H.
    n, s, C, _ = stats(w)
    mod = 1 << (n + extra)
    return (-C * pow(3 ** s, -1, mod)) % mod, mod


def reverse_terminal(k, w):
    J = 1 << k
    for x in reversed(w):
        if x == 0:
            J = 2 * J - 1
        else:
            if (2 * J - 1) % 3:
                return None
            J = (2 * J - 1) // 3
        if J <= 0 or J % 2 == 0:
            return None
    return J


word_checks = 0
danger_checks = 0
exact_v_checks = 0
phase_checks = 0
terminal_checks = 0
all11_checks = 0

# Analytic identities and legal-cylinder bijection.
for n in range(1, 10):
    residues = set()
    for w in product((0, 1), repeat=n):
        N, s, C, D = stats(w)
        assert N == n
        assert C == 3 ** s + 2 * D - (1 << n)

        r, mod = selector(w, 1)
        assert mod == 1 << (n + 1)
        assert r & 1
        vals = simulate(r, w)
        assert all(x & 1 for x in vals[:-1])
        assert vals[-1] % 2 == 0
        lhs = (3 ** s) * r + C
        assert lhs == (1 << n) * vals[-1]
        lhsR = (3 ** s) * (r + 1) + 2 * D
        assert lhsR == (1 << n) * (vals[-1] + 1)
        residues.add(r)
        word_checks += 1

        for H in range(0, 7):
            rd, modd = selector(w, H + 1)
            valsd = simulate(rd, w)
            assert all(x & 1 for x in valsd[:-1])
            assert v2(valsd[-1]) >= H + 1
            assert ((3 ** s) * rd + C) % (1 << (n + H + 1)) == 0
            # Historical phase-numerator translation for several global offsets.
            for i in (1, 2, 5):
                for p in (0, 3):
                    Phi = Fraction((1 << i) * (rd + 1), 3 ** (p + 1))
                    P = (3 ** (p + 1)) * Phi
                    assert P.denominator == 1
                    P = P.numerator
                    modp = 1 << (i + n + H + 1)
                    assert ((3 ** s) * P + (1 << (i + 1)) * D - (1 << (i + n))) % modp == 0
                    phase_checks += 1
            danger_checks += 1

        # Exact exit valuation L: one of the two next lifts has exact L.
        for L in range(1, 6):
            base_mod = 1 << (n + L)
            base = (-C * pow(3 ** s, -1, base_mod)) % base_mod
            cand = [base, base + base_mod]
            vv = [v2(simulate(c, w)[-1]) for c in cand]
            assert sorted([v == L for v in vv]) == [False, True], (w, L, cand, vv)
            assert max(vv) >= L + 1
            exact_v_checks += 1

    assert residues == set(range(1, 1 << (n + 1), 2)), (n, len(residues))

# Terminal-owned exact equality and backward criterion.
for k in range(1, 16):
    for n in range(1, 8):
        for w in product((0, 1), repeat=n):
            _, s, C, D = stats(w)
            num = (1 << (n + k)) - C
            by_formula = None
            if num % (3 ** s) == 0:
                j0 = num // (3 ** s)
                if j0 > 0 and j0 % 2 == 1:
                    vals = simulate(j0, w)
                    if vals[-1] == (1 << k):
                        by_formula = j0
                        assert (3 ** s) * (j0 + 1) + 2 * D == (1 << n) * ((1 << k) + 1)
            by_reverse = reverse_terminal(k, w)
            assert by_formula == by_reverse, (k, w, by_formula, by_reverse)
            terminal_checks += 1

# All-11 terminal collapse and LTE valuation formula.
for k in range(1, 80):
    target = (1 << k) + 1
    vv3 = 0
    z = target
    while z % 3 == 0:
        vv3 += 1
        z //= 3
    if k % 2 == 0:
        assert vv3 == 0
    else:
        kk = k
        v3k = 0
        while kk % 3 == 0:
            v3k += 1
            kk //= 3
        assert vv3 == 1 + v3k
    for n in range(1, min(12, vv3 + 2)):
        w = (1,) * n
        j0 = reverse_terminal(k, w)
        if n <= vv3:
            assert j0 is not None
            q_num = target
            assert q_num % (3 ** n) == 0
            q = q_num // (3 ** n)
            assert j0 + 1 == (1 << n) * q
            assert q & 1
        else:
            assert j0 is None
        all11_checks += 1

print('RL64 all-word cylinder verifier: PASS')
print('word identity/legal-cylinder checks =', word_checks)
print('dangerous-lift checks =', danger_checks)
print('exact-valuation lift checks =', exact_v_checks)
print('historical phase-numerator congruence checks =', phase_checks)
print('terminal ownership/backward checks =', terminal_checks)
print('all-11 terminal/LTE checks =', all11_checks)
