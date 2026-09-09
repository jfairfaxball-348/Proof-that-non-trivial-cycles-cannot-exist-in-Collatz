#!/usr/bin/env python3
"""Portable RL285 regression/certificate verifier.

Certified finite claim:
  Exhaustive normalized-state closure from (d,J,H)=(1,-13,0) through H<=22
  contains no positive state violating
      nu_2(K-1) <= H+d-1,  K=J+2^d-1.

The script also runs bounded regressions for the shifted-shadow/Ferrers identities.
It does NOT claim a proof of the global Gate-A theorem.
"""
from collections import deque
from itertools import product

R = 22


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


def exhaustive_raw_closure():
    start = (1, -13, 0)
    q = deque([start])
    seen = {start}
    while q:
        d, J, H = q.popleft()
        for x in (0, 1):
            st = step_JH(d, J, H, x)
            if st is None or st[2] > R or st in seen:
                continue
            seen.add(st)
            q.append(st)
    return seen


def shadow_W(bits):
    # W_empty=-6; append 0: W+=2^n; append 1: W*=3
    W = -6
    for n, b in enumerate(bits):
        if b == 0:
            W += 2 ** n
        else:
            W *= 3
    return W


def prefix_dominant(x, y):
    # canonical convention: y has at least as many 1s in every prefix
    sx = sy = 0
    for a, b in zip(x, y):
        sx += a
        sy += b
        if sy < sx:
            return False
    return True


def one_positions(bits):
    return [i for i, b in enumerate(bits) if b]


def ferrers_regression(max_n=8):
    checked = 0
    rigid = 0
    for n in range(1, max_n + 1):
        words = list(product((0, 1), repeat=n))
        for x in words:
            for y in words:
                if sum(x) != sum(y) or not prefix_dominant(x, y):
                    continue
                ax = one_positions(x)
                by = one_positions(y)
                if any(b > a for a, b in zip(ax, by)):
                    raise AssertionError((x, y, ax, by))
                lhs = shadow_W(x) - shadow_W(y)
                # Rank formula, equivalent to the Ferrers-cell expansion.
                r = len(ax)
                rhs = sum(3 ** (r - j - 1) * (2 ** ax[j] - 2 ** by[j]) for j in range(r))
                assert lhs == rhs, (x, y, lhs, rhs)
                moved = [j for j in range(r) if ax[j] > by[j]]
                if moved:
                    bstar = min(by[j] for j in moved)
                    assert lhs != 0
                    assert v2(lhs) == bstar, (x, y, lhs, bstar, v2(lhs))
                    rigid += 1
                checked += 1
    return checked, rigid


def main():
    seen = exhaustive_raw_closure()
    positive = [(d, J, H) for d, J, H in seen if J > 0]

    assert len(seen) == 3_837_389, len(seen)
    assert len(positive) == 584_154, len(positive)
    assert max(d for d, J, H in positive) == 7

    violations = []
    equalities = []
    for d, J, H in positive:
        M = J + 2 ** d - 2  # K-1
        A = H + d - 1
        vv = v2(M)
        if vv > A:
            violations.append((d, J, H, vv, A))
        if vv == A:
            equalities.append((d, J, H))

    assert violations == [], violations[:10]
    assert sorted(equalities) == [(1, 8, 3), (2, 6, 2), (3, 2, 1)], sorted(equalities)

    ferrers_checked, rigid_checked = ferrers_regression(8)

    print("RL285 prefix/2-adic verifier: PASS")
    print(f"height_cap={R}")
    print(f"raw_reachable_states={len(seen)}")
    print(f"positive_raw_states={len(positive)}")
    print(f"max_positive_depth={max(d for d, J, H in positive)}")
    print("post_column_2adic_violations=0")
    print("post_column_2adic_equalities=(d1,J8,H3);(d2,J6,H2);(d3,J2,H1)")
    print(f"ferrers_pairs_checked={ferrers_checked}")
    print(f"first_displacement_rigidity_cases={rigid_checked}")
    print("global_gate_A_theorem=NOT_CLAIMED")


if __name__ == "__main__":
    main()
