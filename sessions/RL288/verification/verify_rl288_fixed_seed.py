#!/usr/bin/env python3
"""Portable RL288 targeted regression verifier.

Analytic claims are proved in the RL288 report. This checks the exact normalized
recurrences, bounded fixed-seed prefix regressions, explicit reverse-00 families,
and common-seed first-deviation synchronization through length 16.

The inherited RL285 H<=22 exhaustive certificate remains authoritative finite
evidence and is not duplicated here. This script does NOT prove Gate A.
"""
from collections import deque


def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def k_step(d, K, x):
    if K % 2 == 0:
        if x == 1:
            return d, 3 * K // 2
        return d, (K + 3 ** d - 1) // 2
    if x == 1:
        if d <= 1:
            return None
        return d - 1, (K - 1) // 2
    return d + 1, 3 * (K + 3 ** d) // 2


def step_JH(d, J, H, x):
    K = J + 2 ** d - 1
    st = k_step(d, K, x)
    if st is None:
        return None
    d2, K2 = st
    return d2, K2 - 2 ** d2 + 1, H + d - 1


def step_with_y(d, J, H, x):
    K = J + 2 ** d - 1
    y = x if K % 2 == 0 else 1 - x
    st = step_JH(d, J, H, x)
    if st is None:
        return None
    return st, y


def shadow_U(bits):
    U = -7
    for n, b in enumerate(bits):
        if b:
            U = 3 * U + 2 ** n
    return U


def first_dev(bits):
    p = (1, 0, 1)
    for i, b in enumerate(bits):
        if b != p[i % 3]:
            return i
    return None


def check_transition_formulas(max_len=16):
    paths = [((1, -13, 0), (), ())]
    transition_checks = 0
    common_checked = 1  # include empty prefix
    formula_checks = 0
    sync_checks = 0
    observed_departures = set()

    for n in range(1, max_len + 1):
        new = []
        for st, xb, yb in paths:
            d, J, H = st
            K = J + 2 ** d - 1
            M = K - 1
            T = J + 2 ** d - 3 ** d
            for x in (0, 1):
                out = step_with_y(d, J, H, x)
                if out is None:
                    continue
                st2, y = out
                d2, J2, H2 = st2
                K2 = J2 + 2 ** d2 - 1
                M2 = K2 - 1
                T2 = J2 + 2 ** d2 - 3 ** d2

                # M recurrences.
                if K % 2 == 0 and x == 1:
                    assert M2 == (3 * M + 1) // 2
                elif K % 2 == 0 and x == 0:
                    assert M2 == (M + 3 ** d - 2) // 2
                elif K % 2 == 1 and x == 1:
                    assert M2 == (M - 2) // 2
                else:
                    assert M2 == (3 * M + 3 ** (d + 1) + 1) // 2

                # T=K+1-3^d recurrences.
                if K % 2 == 0 and x == 0:
                    assert T2 == T // 2
                elif K % 2 == 0 and x == 1:
                    assert T2 == (3 * T + 3 ** d - 1) // 2
                elif K % 2 == 1 and x == 1:
                    assert T2 == (T + 3 ** (d - 1)) // 2
                else:
                    assert T2 == (3 * T - 1) // 2

                xx, yy = xb + (x,), yb + (y,)
                new.append((st2, xx, yy))
                transition_checks += 1
                common_checked += 1

                Ux, Uy = shadow_U(xx), shadow_U(yy)
                assert 3 ** d2 * Ux - Uy == 2 ** n * T2
                formula_checks += 1

                fx, fy = first_dev(xx), first_dev(yy)
                assert fx == fy
                sync_checks += 1
                if fx is not None:
                    assert v2(Ux) == fx
                    assert v2(Uy) == fx
                if fx is not None and fx == n - 1:
                    assert d2 == 1 and H2 == 0
                    observed_departures.add(J2)
        paths = new

    assert common_checked == 39166, common_checked
    assert observed_departures == {-28, -6, -4}, observed_departures

    forced = set()
    for J in observed_departures:
        out = step_with_y(1, J, 0, 0)
        assert out is not None
        (d2, J2, H2), y = out
        assert y == 1 and d2 == 2 and H2 == 0
        forced.add((d2, J2, H2))
    assert forced == {(2, -39, 0), (2, -6, 0), (2, -3, 0)}
    return transition_checks, common_checked, formula_checks, sync_checks


def check_first_positive_analytic_cases():
    # Small-depth exceptional cases used by the analytic proof.
    # d=3, A=3 first-positive ascent: parent J in {0,-2,-4,-6}.
    vals = []
    for J in (0, -2, -4, -6):
        Mchild = (3 * J + 34) // 2
        vals.append((J, Mchild, v2(Mchild)))
    assert vals == [(0, 17, 0), (-2, 14, 1), (-4, 11, 0), (-6, 8, 3)]

    # d=2, A=1 ascent from boundary J=0 gives M=5.
    Jchild = 3
    assert Jchild + 2 ** 2 - 2 == 5

    # Equality witness is genuinely reachable via x=000.
    st = (1, -13, 0)
    for x in (0, 0, 0):
        st = step_JH(*st, x)
    assert st == (3, 2, 1)
    M = st[1] + 2 ** st[0] - 2
    A = st[2] + st[0] - 1
    assert (M, v2(M), A) == (8, 3, 3)


def check_reverse_00():
    cases = 0
    for k in range(25, 80, 2):
        for L in range(1, 9):
            vals = [1 + 2 ** (L-i) * (2 ** k - 1) for i in range(L + 1)]
            assert vals[-1] == 2 ** k
            for i in range(L):
                J = vals[i]
                assert J > 0 and J % 2 == 1
                assert (J + 1) // 2 == vals[i + 1]
                assert v2(J) == 0
            cases += 1
    return cases


def check_fixed_shift_degeneracy():
    # Once first deviation is s<n and v2(U)=s, adding c*2^n cannot alter v2.
    checks = 0
    sample_words = [
        (0,), (1, 1), (1, 0, 0), (1, 0, 1, 0),
        (1, 0, 1, 1, 1), (1, 0, 1, 1, 0, 1),
    ]
    for w in sample_words:
        s = first_dev(w)
        if s is None:
            continue
        U = shadow_U(w)
        assert v2(U) == s
        n = len(w)
        for c in (-7, -2, -1, 1, 3, 10):
            assert v2(U + c * 2 ** n) == s
            checks += 1
    return checks


def main():
    trans, prefixes, formula, sync = check_transition_formulas(16)
    check_first_positive_analytic_cases()
    reverse_cases = check_reverse_00()
    shift_checks = check_fixed_shift_degeneracy()

    print("RL288 fixed-seed verifier: PASS")
    print(f"legal_transition_checks={trans}")
    print(f"common_seed_prefixes_checked_including_empty={prefixes}")
    print(f"two_shadow_formula_checks={formula}")
    print(f"first_deviation_sync_checks={sync}")
    print("common_departure_boundary_states=J(-28,-6,-4)")
    print("forced_off_boundary_roots=(d2,J-39,H0);(d2,J-6,H0);(d2,J-3,H0)")
    print("first_positive_equality_witness=(d3,J2,H1)")
    print(f"explicit_reverse_00_rays_checked={reverse_cases}")
    print(f"fixed_shift_degeneracy_checks={shift_checks}")
    print("inherited_H22_certificate=NOT_DUPLICATED")
    print("gate_A=NOT_CLAIMED")


if __name__ == "__main__":
    main()
