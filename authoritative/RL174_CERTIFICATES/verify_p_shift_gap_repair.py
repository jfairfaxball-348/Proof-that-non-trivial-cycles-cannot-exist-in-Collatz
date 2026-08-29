#!/usr/bin/env python3
"""Exact audit for RL174 p-shift correction and physical-gap constants."""
from fractions import Fraction
from math import gcd

A0 = 217_976_794_617
L0 = 137_528_045_312
P0 = 65_470_613_321
U0 = 103_768_467_013


def pow2(g):
    return Fraction(2**g, 1) if g >= 0 else Fraction(1, 2**(-g))


def pow3neg(g):
    return Fraction(1, 3**g) if g >= 0 else Fraction(3**(-g), 1)


def word_data(word):
    L = len(word)
    A = sum(word)
    assert gcd(A, L) == 1 and 2**A > 3**L
    p = pow(A, -1, L)
    S = [0]
    for a in word:
        S.append(S[-1] + a)
    h = [A*j // L - S[j] for j in range(L)]
    assert min(h) >= 0 and h[0] == 0
    q = [Fraction(2**S[j], 3**j) for j in range(L)]
    G = []
    for i in range(L):
        shifted = S[(i+p) % L] + (A if i+p >= L else 0)
        G.append(shifted - S[p] - S[i])
    F3 = sum(q[i] * (pow3neg(G[i]) - 1) for i in range(L))
    F2 = sum(q[i] * (pow2(G[i]) - 1) for i in range(L))

    # Unique positive rational cyclic trajectory for the ordinary +1 recurrence.
    alpha = Fraction(1)
    beta = Fraction(0)
    for a in word:
        alpha = alpha * Fraction(3, 2**a)
        beta = beta * Fraction(3, 2**a) + Fraction(1, 2**a)
    y0 = beta / (1 - alpha)
    ys = [y0]
    for a in word[:-1]:
        ys.append((3*ys[-1] + 1) / 2**a)
    lam = Fraction(2**A, 3**L)
    assert F2 == 3 * (lam - 1) * (ys[p] - ys[0])
    return A, L, p, h, G, F3, F2, tuple(ys)


# RL173's arithmetic values remain correct for its auxiliary 3^{-G} functional.
old_neg = word_data((1, 4))
old_pos = word_data((1, 4, 3))
assert old_neg[5] == Fraction(-52, 81)
assert old_pos[5] == Fraction(176, 27)
# But the corrected accelerated physical functional uses 2^G, not 3^{-G}.
assert old_neg[6] == Fraction(14, 3) > 0
assert old_pos[6] == Fraction(2, 9) > 0

# Correct local sign-nonforcing witnesses for the accelerated physical functional.
neg = word_data((2, 5, 4))
pos = word_data((1, 4))
assert neg[:5] == (11, 3, 2, [0, 1, 0], [0, 2, -1])
assert neg[6] == Fraction(-28, 9)
assert pos[6] == Fraction(14, 3)
assert neg[6] < 0 < pos[6]

# First-survivor Bezout constants.
assert A0 * P0 - L0 * U0 == 1
assert 0 < P0 < L0


def log_bounds(n, terms=100):
    """Exact atanh-series enclosure for log(n), n>0 rational integer here."""
    z = Fraction(n - 1, n + 1)
    z2 = z*z
    term = z
    s = Fraction(0)
    for k in range(terms):
        s += term / (2*k + 1)
        term *= z2
    lo = 2*s
    hi = lo + 2*term / ((2*terms + 1) * (1 - z2))
    return lo, hi


l2lo, l2hi = log_bounds(2)
l3lo, l3hi = log_bounds(3)
Dlo = A0*l2lo - L0*l3hi
Dhi = A0*l2hi - L0*l3lo
assert Dlo > 0
# Recheck inherited 5 theta < 1 by a sufficient interval inequality.
assert 5 * L0 * Dhi < l2lo

# Below-side neighbour discrepancy d_- = u log2 - p log3.
dmlo = U0*l2lo - P0*l3hi
dmhi = U0*l2hi - P0*l3lo
assert dmlo + 6*Dlo > 0      # d_- > -6 Delta
assert dmhi + 5*Dhi < 0      # d_- < -5 Delta

# New quantitative physical floors.
assert 6 * Dlo > Fraction(1, 186_000_000_000)
assert 2**71 * Dlo > 2_120_000_000
assert 3 * 2**71 * Dlo * Dlo > Fraction(1, 176)

# Height-zero upper window.  For 0<x<1, exp(x)-1 < x/(1-x).
assert 7 * Dhi < 1
upper_F_h0 = 3 * 2**75 * (Dhi/(1-Dhi)) * ((7*Dhi)/(1-7*Dhi))
assert upper_F_h0 < Fraction(2, 3)

print('RL174 p-shift correction/gap verifier: PASS')
print('old auxiliary F3 witnesses retained: -52/81, 176/27')
print('correct F2 sign witnesses: 14/3, -28/9')
print('first survivor Bezout: A*p-L*u=1')
print('internal physical floor: F2 > 1/186000000000')
print('external-floor conditional: y_p-y_0 >= 2120000002 and F2 > 1/176')
print('height-zero internal window: F2 < 2/3')
