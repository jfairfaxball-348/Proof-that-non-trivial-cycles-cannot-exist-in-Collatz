#!/usr/bin/env python3
"""Finite regression check for the RL312 balanced shift-orbit dichotomy."""

from math import gcd


def cyclic_window_sum(word, start, length):
    A = len(word)
    return sum(word[(start + j) % A] for j in range(length))


def check_instance(word, s):
    A = len(word)
    L = sum(word)
    if (s * L) % A:
        return False

    p = s * L // A
    G = [p - cyclic_window_sum(word, i, s) for i in range(A)]
    d = gcd(A, s)
    n = A // d

    inactive = []
    for r in range(d):
        orbit = []
        cur = r
        seen = set()
        while cur not in seen:
            seen.add(cur)
            orbit.append(cur)
            cur = (cur + s) % A
        assert len(orbit) == n
        assert sum(G[i] for i in orbit) == 0

        if all(G[i] == 0 for i in orbit):
            inactive.append(r)
            weights = [
                cyclic_window_sum(word, r + k * d, d)
                for k in range(n)
            ]
            assert len(set(weights)) == 1
            assert weights[0] * n == L

    if not inactive:
        assert sum(abs(x) for x in G) >= 2 * d

    return True


def main():
    checked = 0
    for A in range(2, 14):
        for mask in range(1, 1 << A):
            word = [(mask >> i) & 1 for i in range(A)]
            L = sum(word)
            for s in range(1, A):
                if (s * L) % A == 0:
                    assert check_instance(word, s)
                    checked += 1

    assert checked == 10876
    print(f"RL312 shift-orbit dichotomy regression: PASS ({checked} instances)")


if __name__ == "__main__":
    main()
