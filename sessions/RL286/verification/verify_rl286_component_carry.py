#!/usr/bin/env python3
"""Portable RL286 component carry / coupon-defect regression verifier.

This is bounded regression support for the analytic RL286 identities.
It does not prove Gate A or the global post-column 2-adic inequality.
"""
from fractions import Fraction

RHO = Fraction(2, 3)


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


def y_from(d, K, x):
    return x if K % 2 == 0 else 1 - x


def zero_ranks(w):
    ones = 0
    out = []
    for b in w:
        if b:
            ones += 1
        else:
            out.append(ones)
    return out


def shadow_W(bits):
    W = -6
    for n, b in enumerate(bits):
        if b == 0:
            W += 2 ** n
        else:
            W *= 3
    return W


def generate_excursions(K0, max_len=12):
    assert K0 % 2
    st = k_step(1, K0, 0)
    assert st is not None
    d, K = st
    assert (d, y_from(1, K0, 0)) == (2, 1)

    frontier = [(d, K, 0, (0,), (1,), Fraction(2, 1))]
    out = []
    while frontier:
        d, K, H, xw, yw, q = frontier.pop()
        if len(xw) > 1 and d == 1:
            out.append((K0, K, H, xw, yw, q))
            continue
        if len(xw) >= max_len:
            continue
        for x in (0, 1):
            st = k_step(d, K, x)
            if st is None:
                continue
            d2, K2 = st
            y = y_from(d, K, x)
            frontier.append(
                (
                    d2,
                    K2,
                    H + d - 1,
                    xw + (x,),
                    yw + (y,),
                    q * Fraction(2, 3 ** x),
                )
            )
    return out


def metrics(ex):
    K0, K1, H, xw, yw, q = ex
    u = zero_ranks(xw)
    v = zero_ranks(yw)
    assert len(u) == len(v)
    hs = [b - a for a, b in zip(u, v)]
    z = len(u)
    c = [Fraction(2 ** j, 1) * RHO ** u[j] for j in range(z)]
    D = sum(
        (cj * (1 - RHO ** hj) for cj, hj in zip(c, hs)),
        Fraction(0),
    )
    return K0, K1, H, xw, yw, q, u, v, hs, z, D


def main():
    checked = 0
    one_zero = 0

    for K0 in range(-199, 200, 2):
        for ex in generate_excursions(K0, 12):
            (
                _K0,
                _K1,
                H,
                xw,
                yw,
                q,
                u,
                _v,
                hs,
                z,
                D,
            ) = metrics(ex)

            L = len(xw)
            r = sum(xw)
            C = shadow_W(xw) - shadow_W(yw)

            assert sum(hs) == H
            assert C == 3 ** r * D
            assert Fraction(C, 2 ** L) == D / q

            exponents = []
            for j, (uj, hj) in enumerate(zip(u, hs)):
                for t in range(hj):
                    exponents.append(j + uj + t)

            assert len(exponents) == H
            assert exponents
            assert min(exponents) == 0
            assert max(exponents) <= H - 1
            assert exponents.count(0) == 1

            if z == 1:
                one_zero += 1
                assert C == 3 ** H - 2 ** H

            checked += 1

    assert checked == 13_909
    assert one_zero == 199

    print("RL286 component carry verifier: PASS")
    print(f"first_return_excursions={checked}")
    print(f"one_zero_excursions={one_zero}")
    print("carry_coupon_bridge_failures=0")
    print("height_cell_support_failures=0")
    print("global_gate_A_theorem=NOT_CLAIMED")


if __name__ == "__main__":
    main()
