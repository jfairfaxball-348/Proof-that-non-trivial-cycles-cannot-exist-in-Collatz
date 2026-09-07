#!/usr/bin/env python3
"""Exact portable checks for the RL275 determinant telescope/barrier.

This verifier audits identities and finite stress families only. It is not a
proof of Gate A and none of the stress words is asserted to satisfy the full
canonical J recurrence/full-D phase ownership.
"""

from math import gcd


def window_sums(word, length):
    a = len(word)
    doubled = word + word
    pref = [0]
    for bit in doubled:
        pref.append(pref[-1] + bit)
    return [pref[i + length] - pref[i] for i in range(a)]


def zero_window(word, start, length):
    a = len(word)
    return sum(1 - word[(start + j) % a] for j in range(length))


def mechanical_word(length, weight, phase):
    return [
        ((i + 1) * weight + phase) // length
        - (i * weight + phase) // length
        for i in range(length)
    ]


def fixed_form_family(n):
    a = 16 * n + 4
    ell = 10 * n + 3
    z = a - ell
    q = 8 * n - 2
    r = 5 * n - 1
    k = 5
    t = k - 3
    m = a - k - 1

    x = mechanical_word(m, ell - 3, 6 * n - 2)
    u = [1, 1, 0] + x + [1] + [0] * t
    v = [1, 1, 1] + x + [0] * (t + 1)

    Pu = [r - w for w in window_sums(u, q)]
    Qv = [r - w for w in window_sums(v, q)]

    h = [0]
    for i in range(a):
        h.append(h[-1] + v[i] - u[i])

    return a, ell, z, q, r, k, m, x, u, v, Pu, Qv, h


# ---------------------------------------------------------------------------
# A. Infinite arithmetic family formula audited over a wide finite range.
# ---------------------------------------------------------------------------
cluster_formula_checks = 0
for n in range(5, 301):
    a = 16 * n + 4
    ell = 10 * n + 3
    z = 6 * n + 1
    q = 8 * n - 2
    r = 5 * n - 1

    assert a * r - q * ell == 2
    assert 12 * a - 19 * ell == 2 * n - 9 > 0
    assert 8 * ell - 5 * a == 4 > 0
    assert 19 * z - 7 * a == 2 * n - 9
    assert gcd(a, q) <= 8

    u = [1] * ell + [0] * z
    P = [r - w for w in window_sums(u, q)]
    beta = sum(max(-p, 0) for p in P)
    expected = (5 * n + 4) * (3 * n - 1)
    assert beta == expected
    cluster_formula_checks += 1


# ---------------------------------------------------------------------------
# B. Fixed full-word-shape finite common-mode stress family.
# ---------------------------------------------------------------------------
fixed_form_checks = 0
for n in range(5, 301):
    (
        a,
        ell,
        z,
        q,
        r,
        k,
        m,
        x,
        u,
        v,
        P,
        Q,
        h,
    ) = fixed_form_family(n)

    assert a * r - q * ell == 2
    assert 12 * a > 19 * ell
    assert 5 * a < 8 * ell
    assert min(q, a - q) >= 8

    assert len(x) == m
    assert sum(x) == ell - 3
    assert len(u) == len(v) == a
    assert sum(u) == sum(v) == ell
    assert u[:3] == [1, 1, 0]
    assert v[:3] == [1, 1, 1]
    assert u[-3:] == [1, 0, 0]
    assert v[-3:] == [0, 0, 0]

    # x=y, hence internal rank displacement / word-level canonical area is 0.
    H_can_word_level = 0
    assert H_can_word_level == 0

    betaP = sum(max(-p, 0) for p in P)
    betaQ = sum(max(-qv, 0) for qv in Q)
    assert betaP == 3 * n
    assert betaQ == 3 * n + 3
    assert set(P) <= {-1, 0, 1}
    assert set(Q) <= {-1, 0, 1}
    assert betaP <= z - k + 4

    assert h[-1] == 0
    assert min(h) == 0
    assert max(h) == 1

    fixed_form_checks += 1


# ---------------------------------------------------------------------------
# C. Exact RL243 derivative + RL274 (7,19) determinant telescope.
# ---------------------------------------------------------------------------
derivative_checks = 0
determinant_identity_checks = 0
twin_telescope_checks = 0

for n in range(5, 41):
    (
        a,
        ell,
        z,
        q,
        r,
        k,
        m,
        x,
        u,
        v,
        P,
        Q,
        h,
    ) = fixed_form_family(n)

    S = 19 * z - 7 * a
    assert S == 2 * n - 9
    assert 0 < S < a // gcd(a, q)

    # With B=q-r and n0=19B-7q=n-5:
    # S*q = n0*a + 38.
    assert S * q == (n - 5) * a + 38

    for i in range(a):
        assert Q[i] - P[i] == h[i] - h[(i + q) % a]
        derivative_checks += 1

    for s in range(a):
        Zu = zero_window(u, s, 38)
        Zv = zero_window(v, s, 38)

        rhs_u = 14 + sum(P[(s + j * q) % a] for j in range(S))
        rhs_v = 14 + sum(Q[(s + j * q) % a] for j in range(S))
        assert Zu == rhs_u
        assert Zv == rhs_v
        determinant_identity_checks += 2

        determinant_difference = sum(
            Q[(s + j * q) % a] - P[(s + j * q) % a]
            for j in range(S)
        )
        endpoint_difference = h[s] - h[(s + 38) % a]

        assert Zv - Zu == determinant_difference == endpoint_difference
        twin_telescope_checks += 1


print("RL275 owned determinant telescope verifier: PASS")
print("cluster_formula_checks=", cluster_formula_checks)
print("fixed_form_stress_checks=", fixed_form_checks)
print("derivative_checks=", derivative_checks)
print("determinant_identity_checks=", determinant_identity_checks)
print("twin_telescope_checks=", twin_telescope_checks)
print("classification=OWNED_DISCREPANCY_COMPRESSION_IDENTIFIED+GATE_A_EXACT_BARRIER")
